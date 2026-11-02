# backmarket-seller

Unofficial Python client for the Back Market Seller API. This project is unofficial and is not affiliated with, endorsed by, or supported by Back Market.

**Alpha, and not published yet.** It is tested only against a mock built from the public spec, never against the live API. If you use it for real, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Install

From a checkout of this repository, until it is published:

```sh
pip install ./apis/backmarket/packages/python
```

Requires Python 3.10 or later.

## Quickstart

```python
from backmarket_seller import BackMarketClient, NotFoundError, Region

with BackMarketClient(
    "your-token",
    user_agent="BM-YourCompany-YourIntegration;you@example.com",
    locale="fr-fr",
    region=Region.EU,
) as client:
    for order in client.orders.iter(page_size=50):
        print(order.order_id)

    try:
        client.listings.get("00000000-0000-4000-8000-000000000001")
    except NotFoundError as error:
        print(error.status, error.request_id)
```

The async client has the same methods:

```python
from backmarket_seller import AsyncBackMarketClient, Region

async with AsyncBackMarketClient(
    "your-token",
    user_agent="BM-YourCompany-YourIntegration;you@example.com",
    locale="fr-fr",
    region=Region.EU,
) as client:
    async for order in client.orders.iter():
        print(order.order_id)
```

Your token is read from nowhere and stored nowhere: you pass it in, and the client sends it only to the server you selected.

## Behaviour

* **Methods** are grouped by resource: `categories`, `listings`, `tasks`, `orders`, `buyback`, `shipping`, `care` and `backbox`.
* **Pagination:** `list` methods return one page and `iter` methods walk all of them, following `next` only for its position, against your configured server.
* **Retries:** 429 on every method, honouring `Retry-After`, otherwise after `rate_limit_wait` seconds. 5xx, timeouts and connection failures on GET only, with exponential backoff, because a repeated `POST` could repeat a refund.
* **Errors** derive from `ApiError` and carry `status`, `code`, `request_id` and `raw_body` with your token removed. `WafBlockedError` also has `cf_ray`.
* **Logging** goes to the `backmarket_seller` logger. It holds methods, URLs and statuses, never your token or response bodies.
* **Requests** can be a generated model or a plain mapping. Models validate strictly, and send only the fields you set.
* **Responses** are parsed tolerantly, because the spec has not been confirmed against the live API. A field that does not fit its declared type keeps its raw value instead of failing the call, a missing required field reads as `None`, and unknown fields are kept. A response that is not an object at all comes back as decoded JSON, so check types if you depend on them.
* **Uploads** take `bytes` or `(filename, bytes)`.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code, and grants no right to the Back Market name.
