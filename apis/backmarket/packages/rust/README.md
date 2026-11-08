# backmarket-seller

Unofficial async Rust client for the Back Market Seller API. This project is unofficial and is not affiliated with, endorsed by, or supported by Back Market.

**Alpha.** It is tested only against a mock built from the public spec, never against the live API. If you use it for real, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Install

```sh
cargo add backmarket-seller@0.1.0-alpha.1
```

Requires Rust 1.85 or later and a Tokio runtime. TLS is rustls by default. For your platform's TLS library instead:

```sh
cargo add backmarket-seller@0.1.0-alpha.1 --no-default-features --features native-tls
```

With default features off and neither TLS feature, the crate builds but every `https` call fails with `ErrorKind::Connection`, after the usual retries for a GET. That is only right if you pass an `http_client` whose `reqwest` has TLS enabled through your own dependency.

## Quickstart

```rust,no_run
use backmarket_seller::{Client, ErrorKind, OrdersListParams, Region};
use futures_util::TryStreamExt;

# async fn example() -> Result<(), Box<dyn std::error::Error>> {
let client = Client::builder()
    .token("your-token")
    .user_agent("BM-YourCompany-YourIntegration;you@example.com")
    .locale("fr-fr")
    .region(Region::Eu)
    .build()?;

let params = OrdersListParams { page_size: Some(50), ..Default::default() };
let mut orders = client.orders().iter(&params);
while let Some(order) = orders.try_next().await? {
    println!("{:?}", order.order_id);
}

match client.listings().get("00000000-0000-4000-8000-000000000001").await {
    Ok(listing) => println!("{:?}", listing.sku),
    Err(error) if error.kind() == ErrorKind::NotFound => println!("{:?}", error.request_id()),
    Err(error) => return Err(error.into()),
}
# Ok(())
# }
```

Your token is read from nowhere and stored nowhere: you pass it in, and the client sends it only to the server you selected.

## Configuration

`Client::builder()` takes these settings before `build()`:

| Setting | Default | Meaning |
| --- | --- | --- |
| `token` | None | Your API token. Required |
| `user_agent` | None | Required, in the form `BM-{Company}-{Integration};contact@example.com` |
| `locale` | None | Sent as `Accept-Language`, for example `fr-fr`. Required |
| `region` | None | `Region::Eu`, `Region::Na` or `Region::Ap`. Set this or `base_url` |
| `environment` | `Environment::Production` | Or `Environment::Preprod` |
| `base_url` | None | A server root, for tests against a mock. Your token is sent to it |
| `timeout` | 30 seconds | Deadline for each attempt, covering the whole response |
| `max_retries` | 3 | Retries after the first attempt |
| `retry_base_delay` | 500 ms | Base of the exponential backoff |
| `rate_limit_wait` | 10 seconds | Wait after a 429 with no usable `Retry-After` |
| `max_retry_wait` | 60 seconds | Longest `Retry-After` to wait for |
| `http_client` | None | Your own `reqwest::Client`, for a proxy, TLS roots or a shared pool |

A `Client` is cheap to clone and safe to share between tasks.

With `http_client`, the client still sends its own headers and applies its timeout and retries, but redirects follow your client's policy. Build it with `reqwest::redirect::Policy::none()` to keep your token on the server you selected: under reqwest's default policy, a 307 or 308 to the same host resends a write's body with your token. Retries of failures stay GET-only only if your client has no retry policy of its own; one set with `reqwest::ClientBuilder::retry` can resend a write. The crate re-exports the `reqwest` it uses as `backmarket_seller::reqwest`.

## Behaviour

* **Methods** are grouped by resource: `categories()`, `listings()`, `tasks()`, `orders()`, `buyback()`, `shipping()`, `care()` and `backbox()`. Every method is `async` and returns `Result<T, Error>`.
* **Pagination:** `list` methods return one page, and `iter` methods return a `Stream` of every item, following `next` only for its position, against your configured server. A stream ends after yielding an error.
* **Retries:** 429 on every method, honouring `Retry-After`, otherwise after `rate_limit_wait`. A `Retry-After` longer than `max_retry_wait` fails at once with `ErrorKind::RateLimited`, with the header in `Error::retry_after`. 5xx, timeouts and connection failures on GET only, with exponential backoff, because a repeated POST could repeat a refund.
* **Cancellation:** dropping a call's future stops it, including any wait before a retry. Wrap a call in `tokio::time::timeout` for an overall deadline; `timeout` applies to each attempt.
* **Redirects** are never followed by the default client. A 3xx fails with `ErrorKind::Api`, so your token stays on the server you selected.
* **Errors** are one `Error` type. Match on `error.kind()`, an `ErrorKind` such as `NotFound` or `RateLimited`, and read `status()`, `code()`, `request_id()`, `retry_after()`, `cf_ray()` and `raw_body()`, which has your token removed. `ErrorKind::is_permission` is true for all three kinds of 403.
* **Logging** goes through the `log` crate, at debug and info levels, and holds operation names, methods, URLs and statuses, never your token or response bodies.
* **Requests:** model and parameter fields are `Option`s, so a `None` field is not sent. Build them with `..Default::default()`. A field the API types in several ways, such as a price, is a `serde_json::Value`. Date-times are `chrono::DateTime<FixedOffset>`. A body the spec marks optional takes `&body` or `None`, and `None` sends no body.
* **Responses** are decoded tolerantly, because the spec has not been confirmed against the live API. Every field is an `Option` because a required field can be missing. A field that does not fit its declared type, such as a date-time that is not RFC 3339, stays `None` and keeps its raw value in the model's `extra` map, and so do unknown fields and nulls. Serialising a model with `serde_json` gives all of it back with the API's field names. An enumeration keeps a value it does not list as `Unlisted`. A body whose top level is not the declared type fails with `ErrorKind::Decode`, with the body in `raw_body()`.
* **Uploads** take `File` values, with an optional name.

## Design

See the [architecture document](https://github.com/fdhoff/backmarket-seller-sdk/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code, and grants no right to the Back Market name.
