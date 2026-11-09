# Changelog

This crate follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

* A PATCH without a body sends `Content-Length: 0`, as the other languages' HTTP libraries do, and `MessageSigner` signs it.

## 0.1.0-alpha.1 (2026-11-08)

The first alpha.

* Async client for 310 operations across 20 Sell, Commerce and Developer contracts, generated from the public contracts, one module per API.
* Application tokens minted from the client credentials grant, and minted again before they expire or after a 401.
* User tokens: an authorization URL with state and the RuName as redirect URI, code exchange and refresh. The refresh token carries over, and each new user token goes to an `on_token` callback.
* Each operation gets an application or a user token by its scopes, and goes to its own host in production or the sandbox.
* Optional request signing with a Key Management key pair, adding `x-ebay-signature-key`, behind the default `signing` feature.
* Typed errors, with the body's whole `errors` list from `error_details`.
* Pagination streams, retries, rate-limit handling and redacted logging.
