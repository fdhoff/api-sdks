# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against a live Mirakl instance.

## 0.1.0-alpha.1 (unreleased)

The first alpha.

* Async client for the 116 current operations of the Mirakl seller API, generated from the public spec, targeting .NET 10 and .NET 8. Each method's XML doc comment names its Mirakl API code, and every method takes a `CancellationToken`.
* A required base URL for your operator's instance, and your shop API key as the whole `Authorization` header, redacted from exceptions and logs.
* `ShopId` on the client options, sent as `shop_id` on every call that leaves it unset, with a per-call override.
* `ListAll…Async` iterators on the 21 paged operations: offset (`offset`, `max`, `total_count`) and seek (`page_token`, `next_page_token`).
* `WaitFor…Async` methods that poll the six imports and exports until they end, with an interval, a deadline and cancellation.
* `DownloadUrlAsync` for export files, which sends your key only to your instance's origin.
* An `HttpClient` of your own, such as one from `IHttpClientFactory`, or an `HttpMessageHandler`.
* Typed exceptions with the status and raw body, retries, rate-limit handling and redacted logging.
