# ebay-sell

Unofficial async Rust client for eBay's Sell, Commerce and Developer REST APIs. This project is unofficial.

eBay is a trademark of eBay Inc. This project is not affiliated with, endorsed by or sponsored by eBay Inc.

**Alpha.** It is tested only against a mock built from the public contracts, never against the live API. If you use it for real, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Before you start

* You need your own keyset from the eBay Developers Program: an App ID, a Cert ID and, for user tokens, a RuName. This crate ships with no keys or tokens.
* A production keyset stays disabled until you either set up the Marketplace Account Deletion notification endpoint or are granted an exemption from it. The sandbox has no such step.
* The [eBay API License Agreement](https://developer.ebay.com/join/api-license-agreement) applies to everything you build with this crate, and following it is up to you. Among other things:
  * eBay content may not be used to train AI or machine-learning models (§9.10).
  * Content you show must be refreshed: listings at least every 6 hours, and other content at least every 24 hours (§8.1).
  * eBay content may not be used for price modelling or arbitrage (§9.5, §9.6).
  * Restricted APIs need eBay's approval before you call them.
* Sellers domiciled in the EU or UK must sign some calls with a key from the Key Management API: see [Signing](#signing).

## Install

The crate is not on crates.io yet. From a clone of this repository, in your `Cargo.toml`:

```toml
[dependencies]
ebay-sell = { path = "path/to/api-sdks/apis/ebay/packages/rust" }
```

Requires Rust 1.85 or later and a Tokio runtime. The default features are `rustls` and `signing`. For your platform's TLS library instead, set `default-features = false, features = ["native-tls"]`, and add `signing` back if you sign calls.

With default features off and neither TLS feature, the crate builds but every `https` call fails with `ErrorKind::Connection`, after the usual retries for a GET. That is only right if you pass an `http_client` whose `reqwest` has TLS enabled through your own dependency.

## Quickstart

```rust,no_run
use ebay_sell::taxonomy::CategoryTreesGetDefaultIdParams;
use ebay_sell::{Client, ErrorKind};

# async fn example() -> Result<(), Box<dyn std::error::Error>> {
let client = Client::builder()
    .client_id("your-app-id")
    .client_secret("your-cert-id")
    .build()?;

let trees = client.taxonomy().category_trees();
let params = CategoryTreesGetDefaultIdParams { marketplace_id: Some("EBAY_US".into()) };
if let Some(tree) = trees.get_default_id(&params).await? {
    println!("{:?}", tree.category_tree_id);
}

match trees.get("0").await {
    Ok(tree) => println!("{:?}", tree.category_tree_version),
    Err(error) if error.kind() == ErrorKind::NotFound => {
        println!("{:?} {:?} {:?}", error.status(), error.code(), error.detail());
    }
    Err(error) => return Err(error.into()),
}
# Ok(())
# }
```

With a client ID and secret the client mints application tokens itself, from the client credentials grant, and mints a new one shortly before each expires. Operations that act for a seller need a user token instead:

```rust,no_run
use ebay_sell::fulfillment::OrdersListParams;
use ebay_sell::{Client, Token};
use futures_util::TryStreamExt;

# async fn example() -> Result<(), Box<dyn std::error::Error>> {
let client = Client::builder()
    .client_id("your-app-id")
    .client_secret("your-cert-id")
    .user_token("v^1.1#your-user-token")
    .refresh_token("v^1.1#your-refresh-token")
    .on_token(|token: &Token| {
        // Store the new access token. The refresh token stays the same.
        let _ = &token.access_token;
    })
    .marketplace_id("EBAY_US")
    .build()?;

let params = OrdersListParams {
    filter: Some("orderfulfillmentstatus:{NOT_STARTED|IN_PROGRESS}".into()),
    ..Default::default()
};
let mut orders = client.fulfillment().orders().iter(&params);
while let Some(order) = orders.try_next().await? {
    println!("{:?}", order.order_id);
}
# Ok(())
# }
```

A user token lasts two hours and its refresh token about 18 months. When a call is refused with a 401, the client refreshes the user token once, passes it to `on_token`, and retries the call. Concurrent calls share one refresh. If the refresh fails, the call returns the refresh's error, such as `ErrorKind::BadRequest` for `invalid_grant`, not the 401. `on_token` runs while the client holds its token locks, so it must not block on `client.oauth().refresh()` or on a call with the client: those wait for it forever. Store the token and return.

Your credentials are read from nowhere and stored nowhere: you pass them in, and the client sends them only to the environment you selected. Cloning a `Client` is cheap and shares its tokens and connection pool.

## Getting a user token

eBay uses the OAuth 2 authorization code grant, with your RuName as the redirect URI. The client builds the authorization URL with a fresh `state`, then trades the code eBay sends to your accept URL for a user token:

```rust,no_run
use ebay_sell::Client;

# async fn example() -> Result<(), Box<dyn std::error::Error>> {
let client = Client::builder()
    .client_id("your-app-id")
    .client_secret("your-cert-id")
    .ru_name("your-ru-name")
    .build()?;

let request = client.oauth().authorization_url(
    &["https://api.ebay.com/oauth/api_scope/sell.fulfillment"],
    None,
    None,
)?;
// Send the user to request.url, and keep request.state until they return.

let (returned_state, code) = (request.state.clone(), "code-from-the-redirect"); // read both from the redirect's query
if returned_state != request.state {
    return Err("state mismatch".into());
}
let token = client.oauth().exchange_code(code).await?;
println!("{:?}", token.expires_in);
# Ok(())
# }
```

After `exchange_code` the client uses the new token, and `client.oauth().refresh(&[])` replaces it on demand. `client.oauth().app_token(true)` mints an application token now. `authorization_url` and `Token` are also exported on their own.

## Signing

eBay requires sellers domiciled in the EU or UK to sign calls that move money or return financial data, such as those of the Finances API. Create a key pair once with the Key Management API, store its private key, which eBay returns only once, and pass both halves to the client as a `SigningKey`:

```rust,no_run
# #[cfg(feature = "signing")]
# mod example {
use ebay_sell::finances::SellerFundsGetSummaryParams;
use ebay_sell::key_management::models::CreateSigningKeyRequest;
use ebay_sell::{Client, SigningKey};

# pub async fn example() -> Result<(), Box<dyn std::error::Error>> {
let client = Client::builder()
    .client_id("your-app-id")
    .client_secret("your-cert-id")
    .build()?;
let request = CreateSigningKeyRequest { signing_key_cipher: Some("ED25519".into()), ..Default::default() };
let created = client.key_management().signing_keys().create(&request).await?;
// Store created.private_key and created.jwe somewhere safe.

let signing_key = SigningKey::new(
    created.private_key.unwrap_or_default(),
    created.jwe.unwrap_or_default(),
);
let client = Client::builder()
    .user_token("v^1.1#your-user-token")
    .signing_key(signing_key)
    .build()?;
let params = SellerFundsGetSummaryParams { x_ebay_c_marketplace_id: Some("EBAY_GB".into()) };
let summary = client.finances().seller_funds().get_summary(&params).await?;
println!("{:?}", summary.and_then(|summary| summary.total_funds));
# Ok(())
# }
# }
```

Each request then carries `x-ebay-signature-key`, `Signature-Input`, `Signature` and, when it has a body, `Content-Digest`, as RFC 9421 describes. Ed25519 and RSA keys both work. Signing is the `signing` feature, on by default.

## Configuration

Set these on `Client::builder()`. Set `client_id` and `client_secret`, a token, or both.

| Method | Default | Meaning |
| --- | --- | --- |
| `client_id` | none | Your keyset's App ID |
| `client_secret` | none | Your keyset's Cert ID. Sent with the App ID only to the token endpoint |
| `ru_name` | none | Your RuName, for the authorization code grant |
| `app_token` | none | An application token to use instead of minting one |
| `user_token` | none | A user access token, sent on operations that act for a seller |
| `refresh_token` | none | Lets the client replace an expired user token itself |
| `on_token` | none | Called with every new user `Token`, from `exchange_code` and every refresh |
| `app_scopes` | `API_SCOPE` | The scopes of minted application tokens, at least one |
| `user_scopes` | none | The scopes to ask for on refresh. eBay keeps the original grant's when this is not given |
| `environment` | `production` | `production` or `sandbox`. Picks the API hosts and the authorization URL |
| `hosts` | none | Your own base URL for each of `api`, `apiz` and `apim`, for tests against a mock. Your credentials are sent to them |
| `marketplace_id` | none | Sent as `X-EBAY-C-MARKETPLACE-ID` on operations that take it, unless a call passes its own |
| `content_language` | none | Sent as `Content-Language` on operations that take it, unless a call passes its own |
| `signing_key` | none | A `SigningKey` that signs every request. Needs the `signing` feature |
| `user_agent` | none | Sent as `User-Agent` when given |
| `timeout` | 30 s | Time allowed for each attempt, including reading the whole response |
| `max_retries` | 3 | Retries after the first attempt |
| `retry_base_delay` | 500 ms | Base of the exponential backoff |
| `rate_limit_wait` | 10 s | Wait after a 429 with no usable `Retry-After` |
| `max_retry_wait` | 60 s | Longest `Retry-After` to wait for. A longer one fails with `ErrorKind::RateLimited` at once |
| `http_client` | none | A `reqwest::Client` to use instead of the crate's own |

## Behaviour

* **Methods** are grouped by API and then by resource, such as `client.fulfillment().orders()`, `client.inventory().inventory_items()`, `client.post_order().returns()`, `client.account().fulfillment_policies()` and `client.taxonomy().category_trees()`. Each API is also a module, such as `ebay_sell::fulfillment`, with its parameter structs at its root and its models in `ebay_sell::fulfillment::models`. 339 of the 346 operations in the 21 contracts have a method; see Limits.
* **Tokens:** an operation that accepts an application token's scope gets the application token, and every other operation gets the user token. With no application token and no way to mint one, the user token is sent instead. Basic authentication with your App ID and Cert ID goes only to the token endpoint.
* **Hosts:** most operations go to `api.ebay.com`. Finances, Identity, Key Management and payment disputes go to `apiz.ebay.com`, and most of Media to `apim.ebay.com`. Each operation goes to its own host in the environment you chose.
* **Pagination:** `list` methods return one page and `iter` methods return a stream of every item, following each page's `next` link. A stream ends after yielding an error.
* **Retries:** 429 on every method, honouring `Retry-After` up to `max_retry_wait`, otherwise after `rate_limit_wait`. 5xx, timeouts and connection failures on GET only, with exponential backoff, because a repeated `POST` could create an offer twice. A 401 is retried once, after a new application token or a refreshed user token.
* **Errors** are one `Error` type with a `kind()`, such as `ErrorKind::NotFound`, and `status()`, `code()` and `detail()` (the first entry's `errorId` and `message`), `retry_after()` and `raw_body()`, with every credential removed. `error_details(&error)` returns the body's whole `errors` list as `ErrorDetail`s.
* **Logging** goes through the `log` crate, at debug and info levels, and holds operation names, methods, URLs and statuses, never your credentials or response bodies.
* **Requests** take generated models, which send only the fields you set. eBay declares many numbers as strings, such as `limit` and `offset`, so pass them as strings.
* **Responses** are decoded tolerantly, because the contracts have not been confirmed against the live API. Every field is an `Option` because a required field can be missing. A field that does not fit its declared type stays `None` and keeps its raw value in the model's `extra` map, and so do unknown fields and nulls. Operations that may answer 204 return an `Option`, and an empty 204 is `None`. A body whose top level is not the declared type fails with `ErrorKind::Decode`, with the body in `raw_body()`.
* **Debug output** of the client, its builder, tokens and signing keys hides every secret.

## Limits

* Operations that send or return a raw file are not generated yet: video uploads and document downloads in Media, task input and result files in Feed, dispute evidence files in Fulfillment and report downloads in Marketing. They will follow.
* The Feedback API's list operations have no iterator. Page them with `offset` and `limit`.

## Design

See the [architecture document](https://github.com/fdhoff/api-sdks/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code. It does not cover eBay's contracts, which are fetched at build time and not included, and grants no right to the eBay name.
