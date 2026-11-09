# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

* An empty, `.` or `..` path value throws `ArgumentException`, and a `null` one `ArgumentNullException`, before anything is sent, instead of a request to another endpoint, such as the list endpoint for `..`, or with the `{name}` placeholder left in for `null`.
* **Breaking:** the 45 methods whose operations may answer 204 now return `Task<T?>`, so the compiler warns before a `null` result from an empty 204 is dereferenced. `CreateOrReplaceAsync` on inventory items is one.
* A `ListAll…Async` iterator stops at an empty 204 page instead of throwing `ApiDecodeException` partway through `await foreach`.
* `client.PostOrder` and the `EbaySell.PostOrder` namespace cover the Post-Order API's 29 remaining operations on cancellations, returns, item-not-received inquiries and cases. They take the seller's user token and the client's `MarketplaceId`. Return files are uploaded as base64 in a JSON body.
* A multipart file part sends `filename*` only when the name is not ASCII, and never with quote marks inside it. It used to send the quoted name, so servers that read `filename*` first, such as ASP.NET Core, Django and Werkzeug, kept the quote marks as part of the file name. A `"` or `\` in the name is escaped. An empty name, or one with a control character such as CR or LF, throws `ArgumentException` before anything is sent.
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
