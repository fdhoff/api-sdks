# Changelog

This crate follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

* An empty, `.` or `..` path value is an `ErrorKind::Api` error and nothing is sent, instead of a request to another endpoint, such as the list endpoint for `..`.
* `ebay_sell::post_order` and `client.post_order()` cover the Post-Order API's 29 remaining operations on cancellations, returns, item-not-received inquiries and cases. They take the seller's user token and the client's marketplace ID. Return files are uploaded as base64 in a JSON body.
* A PATCH without a body sends `Content-Length: 0`, as the other languages' HTTP libraries do, and `MessageSigner` signs it.
* Breaking: the 26 Inventory and Marketing operations that answer 204 with no body, such as `inventory_items().delete`, and Marketing's `report_tasks().create`, which answers 202, return `()` instead of `Option<models::Error>`.
* An application token 401 and a user token 401 at the same time each refresh their own token. Before, the second call skipped its refresh and failed.
* `build` returns an error when `app_scopes` has no scope, instead of minting with a bare `scope=`.
* The docs say `on_token` must not block on the client, since it runs while the token locks are held.
* The runtime can poll an asynchronous job until it ends, and download a URL a response returns, sending credentials only to the base URL's origin. A job still running at the deadline is an `ErrorKind::JobTimeout` error, whose `Error::job_status` holds its last status. No operation in this package uses either yet.

## 0.1.0-alpha.1 (2026-11-08)

The first alpha.

* Async client for 310 operations across 20 Sell, Commerce and Developer contracts, generated from the public contracts, one module per API.
* Application tokens minted from the client credentials grant, and minted again before they expire or after a 401.
* User tokens: an authorization URL with state and the RuName as redirect URI, code exchange and refresh. The refresh token carries over, and each new user token goes to an `on_token` callback.
* Each operation gets an application or a user token by its scopes, and goes to its own host in production or the sandbox.
* Optional request signing with a Key Management key pair, adding `x-ebay-signature-key`, behind the default `signing` feature.
* Typed errors, with the body's whole `errors` list from `error_details`.
* Pagination streams, retries, rate-limit handling and redacted logging.
