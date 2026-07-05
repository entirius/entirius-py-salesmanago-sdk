# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from dataclasses import dataclass
from typing import Literal

from salesmanago_sdk.dto import DTO


@dataclass
class LoyaltyContact:
    addressType: Literal["email", "contact_id", "tag", "stage"] | None = None
    value: str | None = None


@dataclass
class LoyaltyData(DTO):
    # https://docs.salesmanago.pl/#zwracanie-liczby-punkt-w-w-programie-lojalno-ciowym
    contacts: list[LoyaltyContact]
    email: str | None = None
    loyaltyProgram: str | None = None


@dataclass
class ModifyPointsData(DTO):
    # https://docs.salesmanago.pl/#dodawanie-usuwanie-punkt-w-kontaktu-dla-loyalty-program
    contacts: list[LoyaltyContact]
    points: str | None = None
    modificationType: str | None = None
    comment: str | None = None
    loyaltyProgram: str | None = None
