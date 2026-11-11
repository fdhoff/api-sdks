# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## 0.1.0a1 (unreleased)

The first alpha.

* Typed sync and async clients for the 117 current operations of the seller API, generated from the public spec, with each method's docstring naming its Mirakl API code.
* `accounting.generate_documents` (DR76), added upstream on 2026-11-11, issues accounting documents and generates their files.
* A base URL you supply for your operator's instance, with no default, and your shop API key as the whole `Authorization` header, redacted from errors and logs. A custom `credentials` provider can replace the key.
* `shop_id` as a client default, which each call can override.
* Iterators on the 21 paged operations, by offset or by page token.
* Waits for the offer, product and stock imports and the offer, order and transaction exports, and `download_url` for export file URLs, which sends the key only to the base URL's origin.
* Typed errors with the status and raw body, and retries and rate-limit handling.
