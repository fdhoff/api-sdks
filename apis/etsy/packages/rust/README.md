# etsy-seller

Unofficial async Rust client for the Etsy Open API v3. This project is unofficial and is not affiliated with, endorsed by, or supported by Etsy.

The term 'Etsy' is a trademark of Etsy, Inc. This Application uses Etsy's API, but is not endorsed or certified by Etsy.

**Alpha.** It is tested only against a mock built from the public spec, never against the live API. If you use it for real, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Before you start

* You need your own Etsy app, approved by Etsy, and its keystring and shared secret. This crate ships with no key, and an app's key may not be shared or transferred.
* Etsy's [API Terms of Use](https://www.etsy.com/legal/api) apply to everything you build with it. Among other things, Etsy content you show must be no more than 6 hours old, and the API may not be used for scraping or to train AI models.

## Install

The crate is not on crates.io yet. From a clone of this repository, in your `Cargo.toml`:

```toml
[dependencies]
etsy-seller = { path = "path/to/api-sdks/apis/etsy/packages/rust" }
```

Requires Rust 1.85 or later and a Tokio runtime. TLS is rustls by default. For your platform's TLS library instead, set `default-features = false, features = ["native-tls"]`.

With default features off and neither TLS feature, the crate builds but every `https` call fails with `ErrorKind::Connection`, after the usual retries for a GET. That is only right if you pass an `http_client` whose `reqwest` has TLS enabled through your own dependency.

## Quickstart

```rust,no_run
use etsy_seller::{Client, ErrorKind, ListingsListActiveParams};
use futures_util::TryStreamExt;

# async fn example() -> Result<(), Box<dyn std::error::Error>> {
let client = Client::builder()
    .api_key("your-keystring")
    .shared_secret("your-shared-secret")
    .build()?;

let params = ListingsListActiveParams { keywords: Some("ceramic mug".into()), limit: Some(100), ..Default::default() };
let mut listings = client.listings().iter_active(&params);
while let Some(listing) = listings.try_next().await? {
    println!("{:?} {:?}", listing.listing_id, listing.title);
}

match client.shops().get(1).await {
    Ok(shop) => println!("{:?}", shop.shop_name),
    Err(error) if error.kind() == ErrorKind::NotFound => println!("{:?}", error.detail()),
    Err(error) => return Err(error.into()),
}
# Ok(())
# }
```

Calls that read or change a shop's private data need an OAuth access token as well as your key:

```rust,no_run
use etsy_seller::{Client, ReceiptsListParams, Token};
use futures_util::TryStreamExt;

# async fn example() -> Result<(), Box<dyn std::error::Error>> {
let client = Client::builder()
    .api_key("your-keystring")
    .shared_secret("your-shared-secret")
    .access_token("12345678.your-access-token")
    .refresh_token("12345678.your-refresh-token")
    // Store both tokens: the old refresh token stops working.
    .on_token(|token: &Token| println!("new token for user {:?}", token.user_id()))
    .build()?;

let me = client.users().get_me().await?;
let params = ReceiptsListParams { was_shipped: Some(false), ..Default::default() };
let mut receipts = client.receipts().iter(me.shop_id.unwrap_or_default(), &params);
while let Some(receipt) = receipts.try_next().await? {
    println!("{:?}", receipt.receipt_id);
}
# Ok(())
# }
```

An access token lasts an hour. When a call that needs one is refused with a 401, the client exchanges the refresh token for a new pair once, passes it to `on_token`, and retries the call. Concurrent calls, and an explicit `client.oauth().refresh()`, share one refresh. If the refresh fails, the call fails with the refresh's error, such as a 400 `invalid_grant`, rather than the 401. `on_token` runs while the client holds its token lock, so it must not block on `client.oauth().refresh()`, `exchange_code`, or a call that could get a 401: those wait for the lock forever. Store the token and return.

Your credentials are read from nowhere and stored nowhere: you pass them in, and the client sends them only to the server you selected.

## Getting a token

Etsy uses the OAuth 2 authorization code flow with PKCE. The client builds the authorization URL with a fresh `state` and code verifier, then trades the code Etsy sends back for a token:

```rust,no_run
use etsy_seller::{AuthorizationOptions, Client};

# async fn example() -> Result<(), Box<dyn std::error::Error>> {
let client = Client::builder()
    .api_key("your-keystring")
    .shared_secret("your-shared-secret")
    .on_token(|token| println!("store {token:?}"))
    .build()?;

let redirect_uri = "https://example.com/callback";
let request = client.oauth().authorization_url(redirect_uri, &["listings_r", "shops_r"], AuthorizationOptions::default())?;
// Send the user to request.url, and keep request.state and request.code_verifier until they return.

let (returned_state, code) = (request.state.clone(), "code-from-the-redirect"); // read both from the redirect's query
if returned_state != request.state {
    return Err("state mismatch".into());
}
let token = client.oauth().exchange_code(code, &request.code_verifier, redirect_uri).await?;
println!("{:?}", token.user_id());
# Ok(())
# }
```

The redirect URI must be one registered for your app. After `exchange_code` the client uses the new token, and `client.oauth().refresh()` replaces it on demand. `authorization_url` and `code_challenge` are also available on their own.

## Configuration

`Client::builder()` takes these settings before `build()`:

| Setting | Default | Meaning |
| --- | --- | --- |
| `api_key` | None | Your app's keystring. Required |
| `shared_secret` | None | Your app's shared secret. Required. Sent with the keystring as `x-api-key` on every call |
| `access_token` | None | An OAuth access token, sent verbatim as a bearer token on calls that need one |
| `refresh_token` | None | Lets the client replace an expired access token itself |
| `on_token` | None | Called with every new `Token`, from `exchange_code` and every refresh |
| `user_agent` | None | Sent as `User-Agent` when set |
| `base_url` | `https://openapi.etsy.com` | A server root, for tests against a mock. Your credentials are sent to it |
| `timeout` | 30 seconds | Deadline for each attempt, covering the whole response |
| `max_retries` | 3 | Retries after the first attempt |
| `retry_base_delay` | 500 ms | Base of the exponential backoff |
| `rate_limit_wait` | 10 seconds | Wait after a 429 with no usable `Retry-After` |
| `max_retry_wait` | 60 seconds | Longest `Retry-After` to wait for |
| `http_client` | None | Your own `reqwest::Client`, for a proxy, TLS roots or a shared pool |

A `Client` is cheap to clone and safe to share between tasks. Clones share their tokens.

With `http_client`, the client still sends its own headers and applies its timeout and retries, but redirects follow your client's policy. Build it with `reqwest::redirect::Policy::none()` to keep your credentials on the server you selected: under reqwest's default policy, a 307 or 308 to the same host resends a write's body with your credentials. Retries of failures stay GET-only only if your client has no retry policy of its own. The crate re-exports the `reqwest` it uses as `etsy_seller::reqwest`.

## Behaviour

* **Methods** are grouped by resource, such as `listings()`, `listing_images()`, `listing_inventory()`, `receipts()`, `transactions()`, `shops()`, `shipping_profiles()` and `users()`. Every one of the API's 107 operations has a method. Every method is `async` and returns `Result<T, Error>`.
* **Credentials:** `x-api-key` goes on every call. The access token goes only on calls whose spec asks for OAuth, never on public reads.
* **Pagination:** `list` methods return one page, and `iter` methods return a `Stream` of every item. Each page's `offset` advances by the number of results received, from the `offset` you pass, until an empty page or `count`. A stream ends after yielding an error.
* **Retries:** 429 on every method, honouring `Retry-After`, otherwise after `rate_limit_wait`. A `Retry-After` longer than `max_retry_wait`, such as at the daily limit, fails at once with `ErrorKind::RateLimited`, with the header in `Error::retry_after`. 5xx, timeouts and connection failures on GET only, with exponential backoff, because a repeated POST could create a listing twice.
* **Cancellation:** dropping a call's future stops it, including any wait before a retry. Wrap a call in `tokio::time::timeout` for an overall deadline; `timeout` applies to each attempt.
* **Redirects** are never followed by the default client. A 3xx fails with `ErrorKind::Api`, so your credentials stay on the server you selected.
* **Errors** are one `Error` type. Match on `error.kind()`, an `ErrorKind` such as `NotFound`, `Conflict` or `RateLimited`, and read `status()`, `detail()` (the body's `error` text), `retry_after()` and `raw_body()`, with every credential removed.
* **Logging** goes through the `log` crate, at debug and info levels, and holds operation names, methods, URLs and statuses, never your credentials or response bodies.
* **Requests:** parameter and model fields are `Option`s, so a `None` field is not sent. Build them with `..Default::default()`. Form bodies are fields of the method's params struct, sent form-encoded, beside any query parameters. An empty list sends nothing, so an update leaves that field as it was. A body the spec marks optional takes `&body` or `None`.
* **Responses** are decoded tolerantly, because the spec has not been confirmed against the live API. Every field is an `Option` because a required field can be missing. A field that does not fit its declared type stays `None` and keeps its raw value in the model's `extra` map, and so do unknown fields and nulls. Serialising a model with `serde_json` gives all of it back with the API's field names. A body whose top level is not the declared type fails with `ErrorKind::Decode`, with the body in `raw_body()`.
* **Uploads** take `File` values, with an optional name.

## Design

See the [architecture document](https://github.com/fdhoff/api-sdks/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code, and grants no right to the Etsy name.
