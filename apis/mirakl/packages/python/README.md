# mirakl-seller

Unofficial Python client for the Mirakl marketplace seller API. Not affiliated with, endorsed by or sponsored by Mirakl SAS.

Mirakl runs marketplaces for retailers, called operators, such as Best Buy. Each operator has its own Mirakl instance, so this client talks to your operator's instance: the base URL and the API key both come from that operator's seller back office. Features and custom fields vary by operator, so a call that works on one marketplace may be refused or return other fields on another.

**Alpha.** Mirakl has no public sandbox, so this package is tested only against a mock built from the public spec, never against a live instance. If you use it for real, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Before you start

* You need your own shop API key, created in your operator's seller back office. This package ships with no key.
* You need your operator's Mirakl URL, such as `https://marketplace.example.com`. There is no default.
* Only shop API keys are supported. Partner OAuth2 tokens from `auth.mirakl.net` are not yet; a custom `credentials` provider can send one meanwhile.

## How this differs from Mirakl's SDKs

Mirakl's only official SDKs are for PHP (`mirakl/sdk-php-shop`, under a proprietary licence) and a Java SDK for its customers. This package is a Python alternative, generated from Mirakl's published OpenAPI spec, with siblings to follow in other languages in [the same repository](https://github.com/fdhoff/api-sdks). Every language passes one shared conformance suite, so retries, paging, jobs, errors and redaction behave the same in each. It adds:

* sync and async clients with typed models;
* iterators that walk every page, by offset or by page token;
* waits for imports and exports, and a download helper for the file URLs exports return;
* your `shop_id` set once per client;
* your key kept out of every error and log line.

## Install

The package is not on PyPI yet. From a clone of this repository:

```sh
pip install ./apis/mirakl/packages/python
```

Requires Python 3.10 or later.

## Quickstart

```python
from mirakl_seller import MiraklClient, NotFoundError

with MiraklClient("your-shop-api-key", base_url="https://marketplace.example.com") as client:
    for order in client.orders.iter(order_state_codes="SHIPPING", max=100):
        print(order.order_id, order.order_state, order.total_price)

    try:
        client.offers.get(1)
    except NotFoundError as error:
        print(error.status, error.raw_body)
```

If your key covers several shops, pass `shop_id` once. Every call sends it, unless the call passes its own:

```python
from mirakl_seller import MiraklClient

with MiraklClient("your-shop-api-key", base_url="https://marketplace.example.com", shop_id=2001) as client:
    print(client.shop.get().shop_name)
    print(client.shop.get(shop_id=2002).shop_name)
```

The async client has the same methods:

```python
from mirakl_seller import AsyncMiraklClient

async with AsyncMiraklClient("your-shop-api-key", base_url="https://marketplace.example.com") as client:
    async for offer in client.offers.iter(max=100):
        print(offer.shop_sku, offer.quantity)
```

Your key is read from nowhere and stored nowhere: you pass it in, and the client sends it only to your `base_url`.

## Imports and exports

Mirakl runs bulk work in the background. An import or export call returns an ID, and the matching `wait_for_` method polls the status until the job ends. It returns the final status whether the job succeeded or failed, so you can fetch the error report. Mirakl allows about one status call a minute, so the default `interval` is 60 seconds; the default `timeout` is an hour, after which `JobTimeoutError` is raised with the last status in `result`.

```python
from mirakl_seller import MiraklClient

with MiraklClient("your-shop-api-key", base_url="https://marketplace.example.com") as client:
    started = client.offers.import_stock(file=("stock.csv", b"offer-sku;quantity\nsku-1;5\n"))
    status = client.offers.wait_for_stock_import(started.import_id, interval=60)
    print(status.status, status.lines_in_success, status.lines_in_error)
    if status.has_error_report:
        with client.offers.download_stock_import_error_report(status.import_id) as report:
            print(report.read().decode())
```

An export's status lists file URLs. Fetch them with `download_url`, which sends your key only to your `base_url`'s scheme, host and port, and never to another host, even after a redirect:

```python
from mirakl_seller import MiraklClient

with MiraklClient("your-shop-api-key", base_url="https://marketplace.example.com") as client:
    started = client.orders.export({"start_date": "2026-01-01T00:00:00Z"})
    status = client.orders.wait_for_export(started.tracking_id)
    for url in status.urls or []:
        with client.download_url(url) as file:
            print(file.content_type, len(file.read()))
```

| Job | Start | Wait |
| --- | --- | --- |
| Offer import | `offers.import_` (OF01) | `offers.wait_for_import` (OF02) |
| Product import | `products.import_` (P41) | `products.wait_for_import` (P42) |
| Stock import | `offers.import_stock` (STO01) | `offers.wait_for_stock_import` (STO02) |
| Offer export | `offers.export` (OF52) | `offers.wait_for_export` (OF53) |
| Order export | `orders.export` (OR13) | `orders.wait_for_export` (OR14) |
| Transaction export | `accounting.export_transactions` (TL03) | `accounting.wait_for_transaction_export` (TL04) |

A price import (`offers.import_prices`, PRI01) has no wait: Mirakl reports it only through `offers.list_price_imports`, filtered by `import_id`.

## Configuration

`MiraklClient` and `AsyncMiraklClient` take the API key, then these keywords:

| Argument | Default | Meaning |
| --- | --- | --- |
| `base_url` | Required | Your operator's Mirakl URL, without `/api`. The key is sent to it |
| `shop_id` | None | The shop every call acts for, unless the call passes its own `shop_id` |
| `credentials` | None | A `Credentials` provider that sets each request's credentials, instead of the API key |
| `user_agent` | None | Sent as `User-Agent` when given |
| `timeout` | `30.0` | Seconds to wait on each attempt |
| `max_retries` | `3` | Retries after the first attempt |
| `retry_base_delay` | `0.5` | Base in seconds of the exponential backoff |
| `rate_limit_wait` | `10.0` | Seconds to wait after a 429 with no usable `Retry-After` |
| `max_retry_wait` | `60.0` | Longest `Retry-After` to wait for, in seconds. A longer one raises `RateLimitedError` at once |
| `http_transport` | None | An httpx transport to use instead of the network |

## Behaviour

* **Methods** are grouped by resource, such as `client.orders`, `client.offers`, `client.shipments`, `client.returns` and `client.accounting`, with models in `mirakl_seller.models`. The names match the TypeScript package's in snake_case, except that `import` is a Python keyword, so the import methods are `import_`. All 116 current operations have a method, and each method's docstring names its Mirakl API code, such as OR11, so you can find it in Mirakl's docs. The 11 deprecated operations are left out, as are OF54, OR15 and TL05, whose URLs come from an export's status: use `download_url` for those.
* **Authentication:** the key is sent as the whole `Authorization` header, with no `Bearer` or other prefix.
* **Pagination:** `list` methods return one page and `iter` methods walk all of them. Orders, offers, invoices, products and promotions page by `offset` up to `total_count`; the others send each page's `next_page_token` back as `page_token`. Iterators start where your own `offset` or `page_token` says, and page forward only.
* **Timeouts:** `timeout` is the time allowed for each attempt, including reading the whole response. The async client enforces it exactly. The sync client checks it as data arrives, so a stalled read can overrun by up to one timeout.
* **Retries:** 429 on every method, honouring `Retry-After` up to `max_retry_wait` seconds, otherwise after `rate_limit_wait` seconds. 5xx, timeouts and connection failures on GET only, with exponential backoff. Writes are not retried after those, because a repeat could act twice.
* **Errors** derive from `ApiError`. Error responses raise an `HttpError` subclass, such as `NotFoundError` or `PermissionDeniedError`, with `status`, `retry_after` and `raw_body`, the body as text with your key removed. Mirakl documents no error body, so the client does not parse one.
* **Logging** goes to the `mirakl_seller` logger. It holds methods, URLs and statuses, never your key or response bodies. Download URLs are logged without their query, which may hold a signature.
* **Requests** can be a generated model or a plain mapping. Models validate strictly, and send only the fields you set. Method arguments are checked against their declared types and raise pydantic's `ValidationError` before anything is sent.
* **Responses** are parsed tolerantly, because the spec has not been confirmed against a live instance. A field that does not fit its declared type keeps its raw value instead of failing the call, a missing required field reads as `None`, and unknown fields, such as an operator's custom fields, are kept. An empty 204 returns `None`. A body that does not fit its declared type at all raises `DecodeError` with the body in `raw_body`.
* **Files:** reports, documents and CSV error reports return a `Download`; read it in a `with` block. Uploads take `bytes` or `(filename, bytes)`.
* **Model names** are made from Mirakl's API codes, such as `OR11Response200Orders` for an order, and match the other language packages. TODO: plainer names, shared by every package.

## Limits

* Only shop API keys are supported. TODO: partner OAuth2 client-credentials tokens from `auth.mirakl.net`, if users ask. The `credentials` argument already accepts a custom provider.
* A wait cannot pass `shop_id` per call; it uses the client's.
* AF01, OF61, OR72, P31, RE01 and S30 have no documented paging, so they have no iterator.

## Testing

Every test runs against a mock built from the spec. Mirakl has no public sandbox, and the tests never use a real key or call a live instance.

## Design

See the [architecture document](https://github.com/fdhoff/api-sdks/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code. It does not cover Mirakl's spec, which is fetched at build time and not included, and grants no right to the Mirakl name.
