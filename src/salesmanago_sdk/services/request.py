# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from __future__ import annotations

import json
import time
from typing import TYPE_CHECKING

import requests
from requests import Response

from salesmanago_sdk.settings import SALESMANAGO_API_URL

if TYPE_CHECKING:
    from salesmanago_sdk.services.client import SalesmanagoClient


class Request:
    method: str
    resource: str
    auth: SalesmanagoClient
    headers: dict | None
    params: dict | None
    data: dict | None

    def __init__(
        self, method: str, auth: SalesmanagoClient, resource: str, params=None, headers: dict = None, data: dict = None
    ):
        self.method = method
        self.resource = resource
        self.auth = auth
        self.headers = headers
        self.params = params
        self.data = data

    def create_headers(self):
        if type(self.headers) != dict:
            self.headers = {}
        self.headers["Content-Type"] = "application/json;charset=UTF-8"
        self.headers["Accept"] = "application/json, application/json"

    def authorize(self):
        # Tworzy pary klucz-wartość autoryzacji, którą podaje się w body requesta
        self.data["requestTime"] = int(time.time())
        for key, value in vars(self.auth).items():
            if not key.startswith("__") and not callable(value):
                self.data[key] = value

    def convert_data_to_json(self):
        self.data = json.dumps(self.data, indent=4)

    def _build_url(self) -> str:
        return SALESMANAGO_API_URL + self.resource

    def make_request(self) -> Response:
        self.authorize()
        self.create_headers()
        self.convert_data_to_json()
        res = requests.request(method=self.method, url=self._build_url(), headers=self.headers, data=self.data)
        return res
