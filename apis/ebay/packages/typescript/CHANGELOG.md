# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

## 0.1.0-alpha.1 (2026-11-08)

The first alpha.

* Typed client for 310 operations across 20 Sell, Commerce and Developer contracts, generated from the public contracts, for Node.js 22 or later, as ESM and CommonJS, with no runtime dependencies. Each API is a subpath export with its own models.
* Application tokens minted from the client credentials grant, and minted again before they expire or after a 401. Concurrent calls share one mint.
* User tokens: an authorization URL with state and the RuName as redirect URI, code exchange and refresh. The refresh token carries over, and each new user token goes to an `onToken` callback, which the call waits for.
* Each operation gets an application or a user token by its scopes, and goes to its own host in production or the sandbox.
* Optional request signing with a Key Management key pair, adding `x-ebay-signature-key`.
* Typed errors carrying the body's `errors` list.
* An operation that may answer an empty 204 resolves to `undefined`, and its return type says so.
* Pagination iterators, retries, rate-limit handling, cancellation and redacted logging.
