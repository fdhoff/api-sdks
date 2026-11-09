# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

* A POST or PUT without a body sends `Content-Length: 0`, as the other languages' HTTP libraries do.
* The repository moved to `fdhoff/api-sdks`; the package's repository and documentation links point there.
* An empty success body where the spec declares JSON is an `ErrorKind::Decode` error instead of a default model.
* Breaking: integer enum members are named after their meaning, such as `OrderState::PendingShipment` instead of `Variant3`. This covers `OrderState`, `OrderLineState`, `ListingStateValue`, `ProductCondition` and `ReturnReason`; the wire values are unchanged.
* Breaking: `Client::builder()` takes no arguments. Set `token`, `user_agent` and `locale` with builder methods; `build()` fails if one is missing.
* Breaking: date-time fields and parameters are `chrono::DateTime<FixedOffset>`, not `String`. A value that is not RFC 3339 stays in `extra`.
* An optional request body also takes `&body`, so `Some(&body)` is no longer needed.
* Breaking: `models::Task` is `models::BackgroundTask`, as in every other language.
* `rustls`, the default, and `native-tls` features choose the TLS library.
* `ClientBuilder::http_client` takes your own `reqwest::Client`, and the crate re-exports `reqwest` and `chrono`.
* Docs: with `http_client`, a same-host 307 or 308 under reqwest's default policy resends a write, and a reqwest retry policy can resend one. With neither TLS feature, every `https` call fails as a connection error.
* An empty 204 response returns the type's default, even where the spec also declares JSON, instead of an `ErrorKind::Decode` error.
* Binary response and request bodies are read and sent as raw bytes where the spec declares them. No operation in this package does yet.
* A file in a multipart body is sent with `Content-Type: application/octet-stream`, as the other languages' HTTP libraries do.
* A page whose items field is missing or not a list is an `ErrorKind::Decode` error for link-paged operations too, instead of an empty last page.

## 0.1.0-alpha.1 (2026-11-07)

* Async client for every operation, generated from the public spec, with `Result`-based errors.
* Retries, rate-limit handling, pagination streams, typed errors and redacted logging.
* Tolerant response decoding: a field that does not fit its type, and any unknown field, is kept in the model's `extra` map.
* An optional or single-type union field has its type, such as `Competitor::min_price` as `MonetaryAmount` and `Task::last_action_error` as `String`, rather than `serde_json::Value`.
* Float query and form values are sent as Go and TypeScript send them: `100.0` as `100`, with no exponent, and `NaN` and infinities are sent rather than dropped.
* A gzip body of several members is read in full.
* A request that cannot be built is an `Api` error and is not retried as a connection failure.
