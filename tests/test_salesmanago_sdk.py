# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import logging
import os
import random

import pytest
from faker import Faker

from salesmanago_sdk.dto.customer import (
    BatchDeleteContact,
    BatchDeleteCustomerData,
    CustomerContact,
    CustomerContactAddress,
    CustomerData,
    DeleteCustomerData,
)
from salesmanago_sdk.services.client import SalesmanagoClient

logger = logging.getLogger(__name__)

CLIENT_ID = os.environ.get("SALESMANAGO_CLIENT_ID")
API_KEY = os.environ.get("SALESMANAGO_API_KEY")
SHA = os.environ.get("SALESMANAGO_SHA")
OWNER = os.environ.get("SALESMANAGO_OWNER")

pytestmark = pytest.mark.skipif(
    not all([CLIENT_ID, API_KEY, SHA, OWNER]),
    reason="Salesmanago credentials not set (SALESMANAGO_CLIENT_ID/API_KEY/SHA/OWNER env vars)",
)

salesmanago_client = SalesmanagoClient(clientId=CLIENT_ID, apiKey=API_KEY, sha=SHA, owner=OWNER)


def test_create_customer():
    """Test that create the customer with random data"""
    fake = Faker()
    customer_data = CustomerData(
        contact=CustomerContact(
            email=fake.email(),
            phone=fake.phone_number(),
            name=fake.name(),
            externalId="U" + str(random.randint(1000, 9999)),
            address=CustomerContactAddress(
                streetAddress=fake.street_address(), zipCode=fake.zipcode(), city=fake.city(), country=fake.country()
            ),
        ),
        province=fake.state(),
        birthday=fake.date_of_birth().strftime("%Y%m%d"),
        forceOptIn=True,
        forceOptOut=True,
        forcePhoneOptIn=True,
        forcePhoneOptOut=True,
        # tags=[fake.word() for i in range(3)],
        tags=["TO_DELETE"],
        removeTags=[fake.word() for i in range(2)],
    )
    try:
        response = salesmanago_client.create_or_modify_customer(customer_data=customer_data)
    except Exception as e:
        print(e)


def test_modify_customer():
    """Test that modifies the customer with random data"""
    fake = Faker()
    customer_data = CustomerData(
        contact=CustomerContact(
            email="gilbertabigail@example.org",
            phone=fake.phone_number(),
            name=fake.name(),
            externalId="U" + str(random.randint(1000, 9999)),
            address=CustomerContactAddress(
                streetAddress=fake.street_address(), zipCode=fake.zipcode(), city=fake.city(), country=fake.country()
            ),
        ),
        province=fake.state(),
        birthday=fake.date_of_birth().strftime("%Y%m%d"),
        forceOptIn=True,
        forceOptOut=True,
        forcePhoneOptIn=True,
        forcePhoneOptOut=True,
        # tags=[fake.word() for i in range(3)],
        tags=["TO_DELETE"],
        removeTags=[fake.word() for i in range(2)],
    )
    try:
        response = salesmanago_client.create_or_modify_customer(customer_data=customer_data)
    except Exception as e:
        print(e)


def test_delete_customer():
    """Test that delete the customer by specify email"""
    delete_customer_data = DeleteCustomerData(
        email="mhernandez@example.com",
    )
    try:
        response = salesmanago_client.delete_customer(delete_customer_data=delete_customer_data)
    except Exception as e:
        print(e)


def test_batch_delete_customer():
    """Test that batch delete the customers by specify email/contact_id/tag/funnel/stage/id"""
    batch_delete_customer_data = BatchDeleteCustomerData(
        contacts=[
            BatchDeleteContact(
                addresseeType="email",
                value="bridgesnatalie@example.net",
            )
        ]
    )
    try:
        response = salesmanago_client.batch_delete_customer(batch_delete_customer_data=batch_delete_customer_data)
    except Exception as e:
        print(e)
