# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

* `client.PostOrder` and the `EbaySell.PostOrder` namespace cover the Post-Order API's 29 remaining operations on cancellations, returns, item-not-received inquiries and cases. They take the seller's user token and the client's `MarketplaceId`. Return files are uploaded as base64 in a JSON body.
* The runtime can poll an asynchronous job until it ends, and download a URL a response returns, sending credentials only to the base URL's origin. A new public `ApiJobTimeoutException` carries the last status in `Result` when a job outlasts its timeout. No operation in this package uses either yet.

## 0.1.0-alpha.1 (2026-11-08)

The first alpha.

* Async client for 310 operations across 20 Sell, Commerce and Developer contracts, generated from the public contracts, one namespace per API, targeting .NET 10 and .NET 8.
* Application tokens minted from the client credentials grant, and minted again before they expire or after a 401.
* User tokens: an authorization request with state and the RuName as redirect URI, code exchange and refresh. The refresh token carries over, and each new user token goes to an `OnToken` callback. Concurrent 401s share one refresh.
* Each operation gets an application or a user token by its scopes, and goes to its own host in production or the sandbox.
* Optional request signing with a Key Management key pair, adding `x-ebay-signature-key`.
* Typed exceptions carrying the first error's `errorId` and message, and `Errors` for the whole `errors` list.
* Pagination as `IAsyncEnumerable`, retries, rate-limit handling and redacted logging.
