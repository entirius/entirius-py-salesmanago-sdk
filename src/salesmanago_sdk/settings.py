# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from django.conf import settings

SALESMANAGO_API_URL = getattr(settings, "SALESMANAGO_API_URL", "https://www.salesmanago.pl/api/")
