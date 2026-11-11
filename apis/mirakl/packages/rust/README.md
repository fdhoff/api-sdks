# mirakl-seller

Unofficial async Rust client for the Mirakl seller API. Not affiliated with, endorsed by or sponsored by Mirakl SAS.

Mirakl runs marketplaces for operators, such as Best Buy. Each operator has its own Mirakl instance, and this client talks to the seller (shop) API of the one you sell on, so the base URL is per operator.

**Alpha.** There is no public sandbox, so it is tested only against a mock built from the public spec, never against a live instance. If you use it for real, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Before you start

* You need your operator's base URL and your own shop API key. Both come from that operator's seller back office. This crate ships with neither.
* Features, roles and custom fields vary by operator. An operation your operator has not enabled fails with an error from its instance.
* Only shop API keys are supported.

## How this differs from Mirakl's SDKs

Mirakl's own SDKs are for PHP and Java, for its customers. There is none for Rust. This crate is generated from Mirakl's published OpenAPI spec, as are its siblings in other languages in [the same repository](https://github.com/fdhoff/api-sdks). Every language passes one shared conformance suite, so retries, paging, jobs, errors and redaction behave the same in each. It adds:

* typed models and async methods for all 117 current operations;
* streams that walk every page;
* wait methods that poll an import or export until it ends;
* `download_url` for export files, which sends your key only to your operator's instance;
* your key kept out of every error and log line.

## Install

The crate is not on crates.io yet. From a clone of this repository, add it by path:

```toml
[dependencies]
mirakl-seller = { path = "apis/mirakl/packages/rust" }
```

Requires Rust 1.85 or later and a Tokio runtime. TLS is rustls by default. For your platform's TLS library instead, set `default-features = false, features = ["native-tls"]`.

With default features off and neither TLS feature, the crate builds but every `https` call fails with `ErrorKind::Connection`, after the usual retries for a GET. That is only right if you pass an `http_client` whose `reqwest` has TLS enabled through your own dependency.

## Quickstart

```rust,no_run
use futures_util::TryStreamExt;
use mirakl_seller::{AccountGetParams, Client, ErrorKind, OffersGetParams, OrdersListParams};

# async fn example() -> Result<(), Box<dyn std::error::Error>> {
let client = Client::builder()
    .base_url("https://your-operator.mirakl.net")
    .api_key("your-shop-api-key")
    .build()?;

let shop = client.account().get(&AccountGetParams::default()).await?;
println!("{:?} {:?}", shop.shop_id, shop.shop_name);

let params = OrdersListParams {
    order_state_codes: Some("SHIPPING".to_owned()),
    ..Default::default()
};
let mut orders = client.orders().iter(&params);
while let Some(order) = orders.try_next().await? {
    println!("{:?} {:?}", order.order_id, order.order_state);
}

match client.offers().get(1, &OffersGetParams::default()).await {
    Ok(offer) => println!("{:?}", offer.offer_id),
    Err(error) if error.kind() == ErrorKind::NotFound => println!("{:?}", error.raw_body()),
    Err(error) => return Err(error.into()),
}
# Ok(())
# }
```

Your key is read from nowhere and stored nowhere: you pass it in, and the client sends it only to your base URL.

## Shops

A key that covers several shops picks one with `shop_id`. Set it once on the client, and override it on any call:

```rust,no_run
use mirakl_seller::{AccountGetParams, Client};

# async fn example() -> Result<(), Box<dyn std::error::Error>> {
let client = Client::builder()
    .base_url("https://your-operator.mirakl.net")
    .api_key("your-shop-api-key")
    .shop_id(2001)
    .build()?;
let own = client.account().get(&AccountGetParams::default()).await?;
let other = AccountGetParams { shop_id: Some(2002) };
let other = client.account().get(&other).await?;
println!("{:?} {:?}", own.shop_id, other.shop_id);
# Ok(())
# }
```

## Imports and exports

Imports and exports run in the background. Start one, then wait for it: a wait polls the status every minute by default, since Mirakl allows about one status call a minute, and returns the final status, whether the job completed or failed. A failed import still returns its status, so you can fetch its error report:

```rust,no_run
use std::time::Duration;

use mirakl_seller::{
    Client, File, OffersDownloadImportErrorReportParams, OffersStartImportParams, WaitOptions,
};

# async fn example() -> Result<(), Box<dyn std::error::Error>> {
let client = Client::builder()
    .base_url("https://your-operator.mirakl.net")
    .api_key("your-shop-api-key")
    .build()?;
let csv = "sku;product-id;product-id-type;price;quantity;state\n";
let params = OffersStartImportParams {
    file: Some(File::new("offers.csv", csv)),
    import_mode: Some("NORMAL".to_owned()),
    ..Default::default()
};
let started = client.offers().start_import(&params).await?;
let import_id = started.import_id.ok_or("no import ID")?;
let options = WaitOptions {
    interval: Duration::from_secs(60),
    timeout: Duration::from_secs(3600),
};
let status = client.offers().wait_for_import(import_id, options).await?;
if status.has_error_report == Some(true) {
    let params = OffersDownloadImportErrorReportParams::default();
    let report = client
        .offers()
        .download_import_error_report(import_id, &params)
        .await?;
    println!("{}", String::from_utf8_lossy(&report.bytes().await?));
}
println!("{:?}", status.status);
# Ok(())
# }
```

An export's status lists the URLs of its files. Fetch each with `download_url`. Your key goes only to the base URL's scheme, host and port, and never again once a redirect leaves them, so files stored elsewhere are fetched without it:

```rust,no_run
use mirakl_seller::models::Of52Request;
use mirakl_seller::{Client, OffersStartExportParams, WaitOptions};

# async fn example() -> Result<(), Box<dyn std::error::Error>> {
let client = Client::builder()
    .base_url("https://your-operator.mirakl.net")
    .api_key("your-shop-api-key")
    .build()?;
let request = Of52Request {
    export_type: Some("application/json".to_owned()),
    ..Default::default()
};
let params = OffersStartExportParams::default();
let started = client.offers().start_export(&request, &params).await?;
let tracking_id = started.tracking_id.ok_or("no tracking ID")?;
let status = client
    .offers()
    .wait_for_export(&tracking_id, WaitOptions::default())
    .await?;
for url in status.urls.unwrap_or_default() {
    let file = client.download_url(&url).await?;
    println!("{} {}", file.content_type().to_owned(), file.bytes().await?.len());
}
# Ok(())
# }
```

| Starts | Waits | Status |
| --- | --- | --- |
| `offers().start_import` (OF01) | `offers().wait_for_import` | OF02 |
| `stock().start_import` (STO01) | `stock().wait_for_import` | STO02 |
| `products().start_import` (P41) | `products().wait_for_import` | P42 |
| `offers().start_export` (OF52) | `offers().wait_for_export` | OF53 |
| `orders().start_export` (OR13) | `orders().wait_for_export` | OR14 |
| `transactions().start_export` (TL03) | `transactions().wait_for_export` | TL04 |

`WaitOptions::default()` polls every 60 seconds for up to an hour. A wait still running at its timeout fails with `ErrorKind::JobTimeout`, and `Error::job_status` holds the last status. Dropping the future stops it, between polls included. Price imports (PRI01) have no wait, because their status is a list to filter, not one import to fetch: call `prices().list_imports`.

## Configuration

`Client::builder()` takes these settings before `build()`:

| Setting | Default | Meaning |
| --- | --- | --- |
| `base_url` | None | Your operator's Mirakl instance. Required. Your key is sent to it |
| `api_key` | None | Your shop API key, sent as the whole `Authorization` header, with no scheme. Required |
| `shop_id` | None | Sent as `shop_id` on every call that leaves its own unset |
| `user_agent` | None | Sent as `User-Agent` when given |
| `timeout` | 30 seconds | Deadline for each attempt, covering the whole response |
| `max_retries` | 3 | Retries after the first attempt |
| `retry_base_delay` | 500 ms | Base of the exponential backoff |
| `rate_limit_wait` | 10 seconds | Wait after a 429 with no usable `Retry-After` |
| `max_retry_wait` | 60 seconds | Longest `Retry-After` to wait for |
| `http_client` | None | Your own `reqwest::Client`, for a proxy, TLS roots or a shared pool |

A `Client` is cheap to clone and safe to share between tasks.

With `http_client`, the client still sends its own headers and applies its timeout and retries, but redirects follow your client's policy. Build it with `reqwest::redirect::Policy::none()` to keep your key on your base URL, and so that `download_url` decides where your key goes. A retry policy of your client's own, set with `reqwest::ClientBuilder::retry`, can resend any write. The crate re-exports the `reqwest` it uses as `mirakl_seller::reqwest`.

## Behaviour

* **Methods** are grouped by resource: `account()`, `shop_documents()`, `platform()`, `shipping()`, `offers()`, `prices()`, `stock()`, `products()`, `orders()`, `shipments()`, `returns()`, `threads()`, `document_requests()`, `invoices()`, `billing_cycles()`, `transactions()`, `promotions()` and `picklists()`, with models in `mirakl_seller::models`. Each method's documentation ends with Mirakl's API code, such as OR11, so you can find it in Mirakl's docs. Every method is `async` and returns `Result<T, Error>`.
* **Not included:** the 11 deprecated operations, and the three placeholder paths for export files, which `download_url` replaces.
* **Pagination:** `list` methods return one page, and `iter` methods return a `Stream` of every item. Six operations page by `offset` and `max` up to `total_count`; the others send each page's `next_page_token` back as `page_token`. Streams start where your own `offset` or `page_token` says, keep `shop_id` on every page, and end after yielding an error.
* **Retries:** 429 on every method, honouring `Retry-After`, otherwise after `rate_limit_wait`. A `Retry-After` longer than `max_retry_wait` fails at once with `ErrorKind::RateLimited`, with the header in `Error::retry_after`. 5xx, timeouts and connection failures on GET only, with exponential backoff. Writes are not retried, because a repeat could act twice.
* **Cancellation:** dropping a call's future stops it, including any wait before a retry. Wrap a call in `tokio::time::timeout` for an overall deadline; `timeout` applies to each attempt.
* **Redirects** are never followed by the default client, except by `download_url`. A 3xx fails with `ErrorKind::Api`, so your key stays on your base URL.
* **Errors** are one `Error` type. Match on `error.kind()`, an `ErrorKind` such as `NotFound`, `Permission` or `BadRequest`, and read `status()`, `retry_after()` and `raw_body()`, the body as text with your key removed. Mirakl's docs define no error body, so the client does not parse one.
* **Logging** goes through the `log` crate, at debug and info levels, and holds operation names, methods, URLs and statuses, never your key or response bodies. It leaves out the query of a `download_url` URL, which may hold a signature.
* **Requests:** model and parameter fields are `Option`s, so a `None` field is not sent. Build them with `..Default::default()`. A field the API types in several ways is a `serde_json::Value`.
* **Responses** are decoded tolerantly, because the spec has not been confirmed against a live instance. Every field is an `Option` because a required field can be missing. A field that does not fit its declared type stays `None` and keeps its raw value in the model's `extra` map, and so do unknown fields and nulls. Serialising a model with `serde_json` gives all of it back with the API's field names. A body whose top level is not the declared type fails with `ErrorKind::Decode`, with the body in `raw_body()`.
* **Files:** error reports, documents and invoices return a `Download`, read with `chunk()` or `bytes()` within the client's timeout. Uploads take `File` values, with an optional name.
* **Naming:** the offer and product import operations' `import` path parameter is `import_id`, the ID their start methods return. The deprecated `importId` and `paymentType` fields, camelCase duplicates of `import_id` and `payment_type`, are `deprecated_import_id` and `deprecated_payment_type`.

## Limits

* Partner OAuth2 tokens are not built in, and there is no custom credential provider yet.
* Wait methods send only the job's ID and the client's `shop_id`, not a per-call `shop_id`.
* Model names follow Mirakl's API codes, such as `Or11Response200Orders`, rather than names of their own.

## Testing

Every test runs against a mock built from the spec. No test uses a real key or calls a Mirakl instance.

## Design

See the [architecture document](https://github.com/fdhoff/api-sdks/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code. It does not cover Mirakl's spec, which is fetched at build time and not included, and grants no right to the Mirakl name.
