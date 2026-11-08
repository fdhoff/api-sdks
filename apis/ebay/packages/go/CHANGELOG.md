# Changelog

This module follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

## 0.1.0-alpha.1 (2026-11-08)

The first alpha.

* Typed client for 310 operations across 20 Sell, Commerce and Developer contracts, generated from the public contracts, one sub-package per API, with `context.Context` on every call.
* Application tokens minted from the client credentials grant, and minted again before they expire or after a 401.
* User tokens: an authorization request with state and the RuName as redirect URI, code exchange and refresh. The refresh token carries over, and each new user token goes to the `WithOnToken` function. Concurrent 401s share one refresh.
* Each operation gets an application or a user token by its scopes, and goes to its own host in production or the sandbox.
* Optional request signing with a Key Management key pair, adding `x-ebay-signature-key`.
* Typed errors carrying the first error's `errorId` and message, and `ErrorDetails` for the whole `errors` list.
* Pagination iterators, retries, rate-limit handling and redacted logging.
