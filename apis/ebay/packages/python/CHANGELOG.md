# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

* `MessageSigner` signs `content-length: 0` for a PATCH without a body, as httpx sends it, instead of raising.
* Breaking: the 26 Inventory and Marketing operations that answer 204 with no body, such as `inventory_items.delete`, and Marketing's `report_tasks.create`, which answers 202, return `None` instead of being typed as returning `Error`.
* Binary response and request bodies are read and sent as raw bytes where the spec declares them. No operation in this package does yet.

## 0.1.0a1 (2026-11-08)

The first alpha.

* Typed sync and async clients for 310 operations across 20 Sell, Commerce and Developer contracts, generated from the public contracts, one module per API.
* Application tokens minted from the client credentials grant, and minted again before they expire or after a 401.
* User tokens: an authorization URL with state and the RuName as redirect URI, code exchange and refresh. The refresh token carries over, and each new user token goes to an `on_token` callback.
* Each operation gets an application or a user token by its scopes, and goes to its own host in production or the sandbox.
* Optional request signing with a Key Management key pair, adding `x-ebay-signature-key`.
* Typed errors carrying the body's `errors` list.
* Pagination iterators, retries, rate-limit handling and redacted logging.
