# Changelog

This crate follows semantic versioning and stays on 0.x until outside users confirm its behaviour against a live Mirakl instance.

## 0.1.0-alpha.1 (unreleased)

The first alpha.

* An async client with typed models for the 117 current operations of the Mirakl seller API, generated from the public spec. Each method's documentation names its Mirakl API code.
* `document_requests().generate_documents` (DR76), added upstream on 2026-11-11, issues accounting documents and generates their files.
* A required base URL for your operator's instance, and your shop API key as the whole `Authorization` header, redacted from errors and logs.
* `shop_id` on the client, sent on every call that leaves it unset, with a per-call override.
* Streams on the 21 paged operations: offset (`offset`, `max`, `total_count`) and seek (`page_token`, `next_page_token`).
* Wait methods that poll the six imports and exports until they end, with an interval and a deadline. Dropping the future stops them.
* `Client::download_url` for export files, which sends your key only to your instance's origin.
* Typed errors with the status and raw body, retries, rate-limit handling and redacted logging, with rustls or native TLS and your own `reqwest::Client`.
