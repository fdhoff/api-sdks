# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against a live Mirakl instance.

## 0.1.0-alpha.1 (unreleased)

The first alpha.

* Typed client for the 116 current operations of the Mirakl seller API, generated from the public spec, for Node.js 22 or later, as ESM and CommonJS, with no runtime dependencies. Each method's comment names its Mirakl API code.
* A required base URL for your operator's instance, and your shop API key as the whole `Authorization` header, redacted from errors and logs. A custom credential provider can replace the key.
* `shopId` on the client, sent as `shop_id` on every call that leaves it unset, with a per-call override.
* Iterators on the 21 paged operations: offset (`offset`, `max`, `total_count`) and seek (`page_token`, `next_page_token`).
* Wait methods that poll the six imports and exports until they end, with an interval, a deadline and cancellation.
* `downloadUrl` for export files, which sends your key only to your instance's origin.
* Typed errors with the status and raw body, retries, rate-limit handling, cancellation and redacted logging.
