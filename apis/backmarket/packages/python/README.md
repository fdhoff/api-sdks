# backmarket-seller

Unofficial Python client for the Back Market Seller API. This project is unofficial and is not affiliated with, endorsed by, or supported by Back Market.

**Alpha.** It is tested only against a mock built from the public spec, never against the live API. If you use it for real, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Install

```sh
pip install --pre backmarket-seller
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

## Configuration

`BackMarketClient` and `AsyncBackMarketClient` take the same arguments. `token` is positional and the rest are keywords.

| Argument | Default | Meaning |
| --- | --- | --- |
| `token` | Required | Your API token, sent verbatim |
| `user_agent` | Required | `BM-{Company}-{Integration};contact@example.com` |
| `locale` | Required | Sent as `Accept-Language`, for example `fr-fr` |
| `region` | None | `Region.EU`, `Region.NA` or `Region.AP`. Pass this or `base_url` |
| `environment` | `Environment.PRODUCTION` | Or `Environment.PREPROD` |
| `base_url` | None | A server root, for tests against a mock. Your token is sent to it |
| `timeout` | `30.0` | Seconds to wait on each attempt |
| `max_retries` | `3` | Retries after the first attempt |
| `retry_base_delay` | `0.5` | Base in seconds of the exponential backoff |
| `rate_limit_wait` | `10.0` | Seconds to wait after a 429 with no usable `Retry-After` |
| `max_retry_wait` | `60.0` | Longest `Retry-After` to wait for, in seconds. A longer one raises `RateLimitedError` at once |
| `http_transport` | None | An httpx transport to use instead of the network |

```python
from backmarket_seller import BackMarketClient, Environment, Region

with BackMarketClient(
    "your-token",
    user_agent="BM-YourCompany-YourIntegration;you@example.com",
    locale="en-us",
    region=Region.NA,
    environment=Environment.PREPROD,
    timeout=10.0,
) as client:
    print(client.orders.list(page_size=10))
```

## Behaviour

* **Methods** are grouped by resource: `categories`, `listings`, `tasks`, `orders`, `buyback`, `shipping`, `care` and `backbox`.
* **Pagination:** `list` methods return one page and `iter` methods walk all of them, following `next` only for its position, against your configured server.
* **Timeouts:** `timeout` is the time allowed for each attempt, including reading the whole response. The async client enforces it exactly. The sync client checks it as data arrives, so a stalled read can overrun by up to one timeout.
* **Retries:** 429 on every method, honouring `Retry-After` up to `max_retry_wait` seconds, otherwise after `rate_limit_wait` seconds. A longer `Retry-After` raises `RateLimitedError` at once, with the header in `retry_after`. 5xx, timeouts and connection failures on GET only, with exponential backoff, because a repeated `POST` could repeat a refund.
* **Errors** derive from `ApiError` and carry `status`, `code`, `request_id` and `raw_body` with your token removed. `WafBlockedError` also has `cf_ray`.
* **Logging** goes to the `backmarket_seller` logger. It holds methods, URLs and statuses, never your token or response bodies.
* **Requests** can be a generated model or a plain mapping. Models validate strictly, and send only the fields you set. Method arguments are checked against their declared types and limits, such as `page_size` up to 50, and raise pydantic's `ValidationError` before anything is sent.
* **Responses** are parsed tolerantly, because the spec has not been confirmed against the live API. A field that does not fit its declared type keeps its raw value instead of failing the call, a missing required field reads as `None`, and unknown fields are kept. A body that does not fit its declared type at all, such as a list where an object belongs, raises `DecodeError` with the body in `raw_body`.
* **Uploads** take `bytes` or `(filename, bytes)`.

## Design

See the [architecture document](https://github.com/fdhoff/api-sdks/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code, and grants no right to the Back Market name.
