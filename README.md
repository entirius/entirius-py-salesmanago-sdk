# salesmanago-sdk

SALESmanago marketing automation SDK — customer create/modify/delete over the SALESmanago REST API.

## Installation

```shell
pip install entirius-py-salesmanago-sdk
```

## Usage

```python
from salesmanago_sdk.services.client import SalesmanagoClient
from salesmanago_sdk.dto.customer import CustomerData, CustomerContact

client = SalesmanagoClient(clientId="...", apiKey="...", sha="...", owner="...")
client.create_or_modify_customer(
    customer_data=CustomerData(contact=CustomerContact(email="user@example.com")),
)
```

`SALESMANAGO_API_URL` is read from Django settings (defaults to the public endpoint) — configure it in your project's
settings if you need to override it.

## Development

```shell
make install     # sync dependencies (uv)
make check       # lint + format check (ruff)
make test        # test suite (pytest) — integration tests skipped without SALESMANAGO_* credentials
```

Development and agent instructions: [AGENTS.md](AGENTS.md).

## License

Mozilla Public License 2.0 — see [LICENSE](LICENSE).
