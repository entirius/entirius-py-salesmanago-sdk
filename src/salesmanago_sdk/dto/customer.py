# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from dataclasses import dataclass
from typing import ClassVar, Literal

from marshmallow import Schema

from salesmanago_sdk.dto import DTO


@dataclass
class CustomerContactAddress:
    streetAddress: str | None = None
    zipCode: str | None = None
    city: str | None = None
    country: str | None = None


@dataclass
class CustomerContact(DTO):
    email: str | None = None
    phone: str | None = None
    name: str | None = None
    externalId: str | None = None
    address: CustomerContactAddress = None
    contactId: str | None = None


@dataclass
class BatchDeleteContact(DTO):
    addresseeType: Literal["email", "contact_id", "tag", "funnel", "stage", "id"] | None = None
    value: str | None = None
    optValue: str | None = None


@dataclass
class CustomerData(DTO):
    # "https://docs.salesmanago.pl/#dodawanie-nowego-lub-modyfikacja-istniej-cego-kontaktu"
    contact: CustomerContact | None = None
    province: str | None = None
    birthday: str | None = None
    forceOptIn: bool | None = None
    forceOptOut: bool | None = None
    forcePhoneOptIn: bool | None = None
    forcePhoneOptOut: bool | None = None
    tags: list[str] | None = None
    removeTags: list[str] | None = None
    Schema: ClassVar[type[Schema]] = Schema


@dataclass
class DeleteCustomerData(DTO):
    # "https://docs.salesmanago.pl/#usuwanie-kontaktu"
    email: str


@dataclass
class BatchDeleteCustomerData(DTO):
    # "https://docs.salesmanago.pl/#usuwanie-wielu-kontakt-w-na-raz"
    contacts: list[BatchDeleteContact]
