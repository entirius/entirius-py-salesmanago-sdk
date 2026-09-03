# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import json
from collections.abc import Callable
from dataclasses import dataclass

import pytest

from salesmanago_sdk.dto.loyalty import LoyaltyContact, LoyaltyData
from salesmanago_sdk.exceptions import SalesmanagoError
from salesmanago_sdk.services import request as request_module
from salesmanago_sdk.services.client import SalesmanagoClient

ADD_CONTACT_URL = "https://www.salesmanago.pl/api/loyalty/program/v1/addContact"


@dataclass
class _StubResponse:
    """Minimal stand-in for requests.Response — the validators only read these two attributes."""

    status_code: int
    text: str


@pytest.fixture
def client() -> SalesmanagoClient:
    return SalesmanagoClient(
        clientId="novatrade", apiKey="ENT-APIKEY-0001", sha="ENT-SHA-0001", owner="ops@novatrade.example"
    )


@pytest.fixture
def loyalty_data() -> LoyaltyData:
    return LoyaltyData(contacts=[LoyaltyContact(addressType="email", value="buyer@novatrade.example")])


@pytest.fixture
def http_calls(monkeypatch) -> Callable[[int, dict], list[dict]]:
    """Replace the HTTP transport with a stub returning a fixed response; returns the recorded calls."""

    def _stub(status_code: int, body: dict) -> list[dict]:
        calls: list[dict] = []

        def fake_request(method, url, headers=None, data=None):
            calls.append({"method": method, "url": url, "payload": json.loads(data)})
            return _StubResponse(status_code=status_code, text=json.dumps(body))

        monkeypatch.setattr(request_module.requests, "request", fake_request)
        return calls

    return _stub


def test_add_contact_to_loyalty_program_returns_response_body(client, loyalty_data, http_calls):
    """Test that a successful call returns the parsed response body"""
    http_calls(200, {"success": True, "message": [], "contactId": "ENT-CONTACT-0001"})

    response = client.add_contact_to_loyalty_program(loyalty_data=loyalty_data)

    assert response == {"success": True, "message": [], "contactId": "ENT-CONTACT-0001"}


def test_add_contact_to_loyalty_program_posts_to_the_add_contact_endpoint(client, loyalty_data, http_calls):
    """Test that the contact is sent with POST to the loyalty addContact resource"""
    calls = http_calls(200, {"success": True})

    client.add_contact_to_loyalty_program(loyalty_data=loyalty_data)

    assert [(call["method"], call["url"]) for call in calls] == [("POST", ADD_CONTACT_URL)]


def test_add_contact_to_loyalty_program_omits_unset_loyalty_fields(client, loyalty_data, http_calls):
    """Test that fields left unset are dropped from the payload instead of being sent as null"""
    calls = http_calls(200, {"success": True})

    client.add_contact_to_loyalty_program(loyalty_data=loyalty_data)

    payload = calls[0]["payload"]
    assert payload["contacts"] == [{"addressType": "email", "value": "buyer@novatrade.example"}]
    assert "email" not in payload
    assert "loyaltyProgram" not in payload
    assert payload["clientId"] == "novatrade"


def test_add_contact_to_loyalty_program_raises_when_response_is_not_success(client, loyalty_data, http_calls):
    """Test that a 200 response flagged as unsuccessful is rejected"""
    http_calls(200, {"success": False, "message": ["contact already in the program"]})

    with pytest.raises(SalesmanagoError, match="Salesmanago response is not correct."):
        client.add_contact_to_loyalty_program(loyalty_data=loyalty_data)


def test_add_contact_to_loyalty_program_raises_when_api_responds_with_error(client, loyalty_data, http_calls):
    """Test that an unhandled error status is surfaced with the API message"""
    http_calls(422, {"message": "loyalty program not found"})

    with pytest.raises(SalesmanagoError, match="loyalty program not found"):
        client.add_contact_to_loyalty_program(loyalty_data=loyalty_data)
