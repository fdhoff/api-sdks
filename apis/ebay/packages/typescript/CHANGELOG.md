# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

* An empty, `.` or `..` path value throws `TypeError` before anything is sent, instead of a request to another endpoint, such as the list endpoint for `..`.
* An iteration whose next link returns to a page it already requested, such as page A, then B, then A again, now throws `DecodeError` instead of fetching the same pages until the rate limit runs out. Before, only a next link that repeated the one just sent was caught.
* The runtime can poll an asynchronous job until it ends, and download a URL a response returns, sending credentials only to the base URL's origin. No operation in this package uses either yet.

## 0.1.0-alpha.2 (2026-11-09)

* `client.postOrder` and the `ebay-sell/post-order` subpath cover the Post-Order API's 29 remaining operations on cancellations, returns, item-not-received inquiries and cases. They take the seller's user token and the client's `marketplaceId`. Return files are uploaded as base64 in a JSON body.
* An application token 401 and a user token 401 at the same time each refresh their own token. Before, the second call skipped its refresh and failed.
* An empty or blank `appScopes` throws a `TypeError` when the client is built, instead of minting with a bare `scope=`.
* The docs say `onToken` must not call the client, since the refresh that called it waits for it.

## 0.1.0-alpha.1 (2026-11-08)

The first alpha.

* Typed client for 310 operations across 20 Sell, Commerce and Developer contracts, generated from the public contracts, for Node.js 22 or later, as ESM and CommonJS, with no runtime dependencies. Each API is a subpath export with its own models.
* Application tokens minted from the client credentials grant, and minted again before they expire or after a 401. Concurrent calls share one mint.
* User tokens: an authorization URL with state and the RuName as redirect URI, code exchange and refresh. The refresh token carries over, and each new user token goes to an `onToken` callback, which the call waits for.
* Each operation gets an application or a user token by its scopes, and goes to its own host in production or the sandbox.
* Optional request signing with a Key Management key pair, adding `x-ebay-signature-key`.
* Typed errors carrying the body's `errors` list.
* An operation that may answer an empty 204 resolves to `undefined`, and its return type says so.
* The 26 Inventory and Marketing operations that answer 204 with no body, such as `inventoryItems.delete`, and Marketing's `reportTasks.create`, which answers 202, resolve to `void`.
* Pagination iterators, retries, rate-limit handling, cancellation and redacted logging.
