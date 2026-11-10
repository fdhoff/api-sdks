# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## 0.1.0a2 (2026-11-10)

* A model in a multipart body is sent as JSON, not as its Python repr, and a mapping is sent as compact JSON.
* An empty, `.` or `..` path value raises `ValueError` before anything is sent, instead of a request to another endpoint, such as the list endpoint for `..`.
* A tuple or frozenset passed as an array argument is sent as one value per item, as a list is. Before, it was sent as its Python repr.
* An iteration whose next link returns to a page it already requested, such as page A, then B, then A again, now raises `DecodeError` instead of fetching the same pages until the rate limit runs out. Before, only a next link that repeated the one just sent was caught.
* `ebay_sell.post_order` and `client.post_order` cover the Post-Order API's 29 remaining operations on cancellations, returns, item-not-received inquiries and cases. They take the seller's user token and the client's `marketplace_id`. Return files are uploaded as base64 in a JSON body.
* `MessageSigner` signs `content-length: 0` for a PATCH without a body, as httpx sends it, instead of raising.
* Breaking: the 26 Inventory and Marketing operations that answer 204 with no body, such as `inventory_items.delete`, and Marketing's `report_tasks.create`, which answers 202, return `None` instead of being typed as returning `Error`.
* An application token 401 and a user token 401 at the same time each refresh their own token. Before, the second call skipped its refresh and failed.
* An empty `app_scopes` raises `ValueError` when the client is built, instead of minting with a bare `scope=`.
* The docs say `on_token` must not call the client, since it runs while the token locks are held.
* Binary response and request bodies are read and sent as raw bytes where the spec declares them. No operation in this package does yet.
* The runtime can poll an asynchronous job until it ends, and download a URL a response returns, sending credentials only to the base URL's origin. No operation in this package uses either yet.

## 0.1.0a1 (2026-11-08)

The first alpha.

* Typed sync and async clients for 310 operations across 20 Sell, Commerce and Developer contracts, generated from the public contracts, one module per API.
* Application tokens minted from the client credentials grant, and minted again before they expire or after a 401.
* User tokens: an authorization URL with state and the RuName as redirect URI, code exchange and refresh. The refresh token carries over, and each new user token goes to an `on_token` callback.
* Each operation gets an application or a user token by its scopes, and goes to its own host in production or the sandbox.
* Optional request signing with a Key Management key pair, adding `x-ebay-signature-key`.
* Typed errors carrying the body's `errors` list.
* Pagination iterators, retries, rate-limit handling and redacted logging.
