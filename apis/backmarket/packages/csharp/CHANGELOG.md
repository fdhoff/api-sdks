# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## 0.1.0-alpha.1 (2026-11-07)

* Async client for all 40 operations, generated from the public spec, targeting .NET 10.
* Retries, rate-limit handling, pagination as `IAsyncEnumerable`, typed exceptions and redacted logging.
* Tolerant responses: values that do not fit, and unknown fields, are kept in `Extra`.
* An optional or single-type union property has its type, such as `Competitor.MinPrice` as `MonetaryAmount` and `BackgroundTask.LastActionError` as `string`, rather than `object`.
* A blank `page` or `cursor` in a `next` link is a decode error, as in the other languages, rather than being sent.
* A gzip success body that ends early throws `ApiDecodeException` instead of returning partial or empty data.
* Success bodies are returned as they are. The token is still removed from exceptions and logs.
* `Retry-After` dates are read as leniently as in Python: RFC 850, asctime, two-digit years, missing seconds and named or numeric zones.
* `BuybackOrderState.New` replaces `VarNew`, and `BuybackMessageAuthor.BackMarket` replaces `Backmarket`.
* Docs: an unlisted integer enum value is kept in the property, and a custom `HttpHandler` must not resend a failed write.
