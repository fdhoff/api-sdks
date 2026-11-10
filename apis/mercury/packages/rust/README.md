# mercury-banking

Unofficial async Rust client for the Mercury API. Not affiliated with, endorsed by or sponsored by Mercury Technologies, Inc.

Mercury is a financial technology company, not a bank. Its banking services are provided through partner banks.

**Alpha.** It is tested only against a mock built from the public spec, never against the live API. If you use it for real, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Before you start

* You need your own API token, created in the Mercury dashboard. This crate ships with no token. The `secret-token:` prefix is part of the token: pass it whole.
* A read-write token works only from IP addresses you allowlist on Mercury's side. A read-only token needs no allowlist.
* Mercury deletes tokens that go unused for 45 days, and downgrades tokens whose scope is broader than their use. Give each token only what it needs.
* The sandbox at `sandbox.mercury.com` holds dummy data and needs a token created there. A production token does not work in the sandbox, and a sandbox token does not work in production.
* OAuth2 is not supported yet. Mercury approves each OAuth2 integration individually.

## How this differs from Mercury's SDKs

Mercury publishes an official Go SDK, and none for Rust. This crate is generated from Mercury's published OpenAPI spec, as are its siblings in Python, TypeScript, Go and C# in [the same repository](https://github.com/fdhoff/api-sdks). Every language passes one shared conformance suite, so retries, paging, errors and redaction behave the same in each. It adds:

* typed models and async methods for every documented operation;
* retries for the four money-moving writes, safe because each carries your `idempotencyKey`;
* streams that walk every page;
* a verifier for the `Mercury-Signature` webhook header;
* your token kept out of every error and log line.

## Install

The crate is not on crates.io yet. From a clone of this repository, add it by path:

```toml
[dependencies]
mercury-banking = { path = "apis/mercury/packages/rust" }
```

Requires Rust 1.85 or later and a Tokio runtime. TLS is rustls by default. For your platform's TLS library instead, set `default-features = false, features = ["native-tls", "webhooks"]`.

With default features off and neither TLS feature, the crate builds but every `https` call fails with `ErrorKind::Connection`, after the usual retries for a GET. That is only right if you pass an `http_client` whose `reqwest` has TLS enabled through your own dependency. The `webhooks` feature, on by default, brings in `aws-lc-rs` for `verify_webhook`.

## Quickstart

```rust,no_run
use futures_util::TryStreamExt;
use mercury_banking::{AccountsListParams, Client, ErrorKind, TransactionsListParams};

# async fn example() -> Result<(), Box<dyn std::error::Error>> {
let client = Client::builder().token("secret-token:your-token").build()?;

let mut accounts = client.accounts().iter(&AccountsListParams::default());
while let Some(account) = accounts.try_next().await? {
    println!("{:?} {:?}", account.name, account.available_balance);
}

let params = TransactionsListParams {
    limit: Some(100),
    status: Some(vec!["sent".to_owned()]),
    ..Default::default()
};
let mut transactions = client.transactions().iter(&params);
while let Some(transaction) = transactions.try_next().await? {
    println!("{:?} {:?}", transaction.counterparty_name, transaction.amount);
}

match client.recipients().get("00000000-0000-4000-8000-000000000000").await {
    Ok(recipient) => println!("{:?}", recipient.name),
    Err(error) if error.kind() == ErrorKind::NotFound => println!("{:?}", error.raw_body()),
    Err(error) => return Err(error.into()),
}
# Ok(())
# }
```

Try it against the sandbox first, with a token created there:

```rust,no_run
use mercury_banking::{Client, RecipientsListParams};

# async fn example() -> Result<(), Box<dyn std::error::Error>> {
let client = Client::builder()
    .token("secret-token:your-sandbox-token")
    .environment("sandbox")
    .build()?;
let params = RecipientsListParams { limit: Some(10), ..Default::default() };
let page = client.recipients().list(&params).await?;
for recipient in page.recipients.unwrap_or_default() {
    println!("{:?}", recipient.name);
}
# Ok(())
# }
```

Your token is read from nowhere and stored nowhere: you pass it in, and the client sends it only to the environment you selected.

## Moving money

`accounts().send_money`, `accounts().request_send_money`, `accounts().transfer` and `transfer_requests().create` require an `idempotencyKey`. Mercury carries out a request with a given key once, so the client retries these calls after a 5xx, a timeout or a dropped connection, sending the same body and key each time. It never makes up or changes a key. Use a fresh one for each payment you mean to make, such as a UUID from the `uuid` crate:

```rust,no_run
use mercury_banking::Client;
use mercury_banking::models::{PostTransactionApiRequest, PostTransactionPaymentMethod};

# async fn example(idempotency_key: String) -> Result<(), Box<dyn std::error::Error>> {
let client = Client::builder().token("secret-token:your-token").build()?;
let payment = PostTransactionApiRequest {
    recipient_id: Some("00000000-0000-4000-8000-000000000002".to_owned()),
    amount: Some(12.5),
    payment_method: Some(PostTransactionPaymentMethod::Ach),
    idempotency_key: Some(idempotency_key),
    ..Default::default()
};
// The first argument is your account's ID.
let transaction = client
    .accounts()
    .send_money("00000000-0000-4000-8000-000000000001", &payment)
    .await?;
println!("{:?} {:?}", transaction.id, transaction.status);
# Ok(())
# }
```

Store the key with the payment, so that a retry of your own, after a crash, sends the same one.

## Webhooks

Mercury signs every webhook with the endpoint's secret, in the `Mercury-Signature` header. Mercury's sandbox sends no webhooks, so check your handler with your own test payloads. Pass the raw body, exactly as it arrived:

```rust
# #[cfg(feature = "webhooks")]
# mod example {
use mercury_banking::reqwest::header::HeaderMap;
use mercury_banking::webhooks::{SIGNATURE_HEADER, WebhookOptions, verify_webhook};

fn handle(body: &[u8], headers: &HeaderMap, secret: &str) -> u16 {
    let header = headers.get(SIGNATURE_HEADER).and_then(|value| value.to_str().ok()).unwrap_or("");
    match verify_webhook(body, header, secret, &WebhookOptions::default()) {
        Ok(()) => 200,
        Err(error) => {
            println!("rejected: {error}");
            400
        }
    }
}
# }
```

The signature is an HMAC-SHA256 of `<timestamp>.<raw body>`, compared in constant time. A timestamp more than 5 minutes old is rejected, so replays fail: set `WebhookOptions::tolerance` to change that. A header may carry several signatures while you rotate a secret; any one that matches is enough. `WebhookError` says which check failed, and never holds the secret or the body.

## Configuration

`Client::builder()` takes these settings before `build()`:

| Setting | Default | Meaning |
| --- | --- | --- |
| `token` | None | Your API token. Required |
| `environment` | `production` | `production` or `sandbox` |
| `hosts` | None | Your own base URL for each of `api` and `vault`, for tests against a mock. The token is sent to them |
| `user_agent` | None | Sent as `User-Agent` when given |
| `timeout` | 30 seconds | Deadline for each attempt, covering the whole response |
| `max_retries` | 3 | Retries after the first attempt |
| `retry_base_delay` | 500 ms | Base of the exponential backoff |
| `rate_limit_wait` | 10 seconds | Wait after a 429 with no usable `Retry-After` |
| `max_retry_wait` | 60 seconds | Longest `Retry-After` to wait for |
| `http_client` | None | Your own `reqwest::Client`, for a proxy, TLS roots or a shared pool |

A `Client` is cheap to clone and safe to share between tasks.

With `http_client`, the client still sends its own headers and applies its timeout and retries, but redirects follow your client's policy. Build it with `reqwest::redirect::Policy::none()` to keep your token on the hosts you selected. A retry policy of your client's own, set with `reqwest::ClientBuilder::retry`, can resend any write. The crate re-exports the `reqwest` it uses as `mercury_banking::reqwest`.

## Behaviour

* **Methods** are grouped by resource, such as `accounts()`, `transactions()`, `recipients()`, `cards()` and `invoices()`, with models in `mercury_banking::models`. All 89 operations in the API reference have a method. Every method is `async` and returns `Result<T, Error>`.
* **Hosts:** every operation goes to `api.mercury.com`, except `cards().reveal`, which goes to `vault-api.mercury.com`. In the sandbox both go to `api-sandbox.mercury.com`.
* **Pagination:** `list` methods return one page, and `iter` methods return a `Stream` of every item. Most send each page's `page.nextPage` back as `start_after`. `accounts().iter_transactions` pages by `offset`, and `treasury().iter_transactions` by its `cursor`. Streams start where your own `start_after`, `offset` or `cursor` says, page forward only, and end after yielding an error.
* **Retries:** 429 on every method, honouring `Retry-After`, otherwise after `rate_limit_wait`. A `Retry-After` longer than `max_retry_wait` fails at once with `ErrorKind::RateLimited`, with the header in `Error::retry_after`. 5xx, timeouts and connection failures on GET, and on the four money-moving writes when their `idempotencyKey` is set, with exponential backoff. Other writes are not retried, because a repeat could act twice.
* **Cancellation:** dropping a call's future stops it, including any wait before a retry. Wrap a call in `tokio::time::timeout` for an overall deadline; `timeout` applies to each attempt.
* **Redirects** are never followed by the default client. A 3xx fails with `ErrorKind::Api`, so your token stays on the hosts you selected.
* **Errors** are one `Error` type. Match on `error.kind()`, an `ErrorKind` such as `NotFound`, `Permission` or `Conflict`, and read `status()`, `retry_after()` and `raw_body()`, the body as text with your token removed. Mercury declares no error body, so the client does not parse one.
* **Logging** goes through the `log` crate, at debug and info levels, and holds operation names, methods, URLs and statuses, never your token or response bodies, so card numbers from `cards().reveal` stay out of it.
* **Requests:** model and parameter fields are `Option`s, so a `None` field is not sent. Build them with `..Default::default()`. A field the API types in several ways is a `serde_json::Value`. IDs are `&str`.
* **Responses** are decoded tolerantly, because the spec has not been confirmed against the live API. Every field is an `Option` because a required field can be missing. A field that does not fit its declared type stays `None` and keeps its raw value in the model's `extra` map, and so do unknown fields and nulls. Serialising a model with `serde_json` gives all of it back with the API's field names. An enumeration keeps a value it does not list as `Unlisted`. A body whose top level is not the declared type fails with `ErrorKind::Decode`, with the body in `raw_body()`.
* **Files:** `invoices().download_pdf`, `statements().download_pdf` and `safes().download_document` return a `Download`, read with `chunk()` or `bytes()` within the client's timeout. Uploads take `File` values, with an optional name.
* **Naming:** `receipts().match_transaction` is Mercury's receipt match, renamed because `match` is a Rust keyword.

## Limits

* The optional `Idempotency-Key` header on budget and receipt writes is not exposed yet, so those calls are sent without one and not retried.
* Streams do not page backward with `end_before`. Call `list` with it instead.

## Testing

Every test runs against a mock built from the spec, never with a real token.

## Design

See the [architecture document](https://github.com/fdhoff/api-sdks/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code. It does not cover Mercury's spec, which is fetched at build time and not included, and grants no right to the Mercury name.
