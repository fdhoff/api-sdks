# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

* An empty, `.` or `..` path value throws `ArgumentException`, and a `null` one `ArgumentNullException`, before anything is sent, instead of a request to another endpoint, such as the list endpoint for `..`, or with the `{name}` placeholder left in for `null`.
* A `ListAll…Async` iterator stops at an empty 204 page instead of throwing `ApiDecodeException` partway through `await foreach`.
* The repository moved to `fdhoff/api-sdks`; the package's repository and documentation links point there.
* Targets .NET 8 as well as .NET 10.
* A constructor takes your own `HttpClient`, and `services.AddBackMarketSeller(token, options)` registers the client with `IHttpClientFactory`. Writes are still never resent.
* Writes reuse pooled connections instead of opening one each. The token and other headers are sent per request, not set on the `HttpClient`.
* The package has a project URL, Source Link, a symbols package and an icon.
* An empty success body where the spec declares JSON throws `ApiDecodeException` instead of returning an empty model or string.
* An `HttpClient` whose `DefaultRequestHeaders.ExpectContinue` is `true` is refused with `ArgumentException`. It overrode the client's own setting, so a failed write could be resent.
* Docs: a plain `new HttpClient()` follows redirects, and a resilience handler added to every client, as in .NET Aspire's service defaults, retries writes unless configured not to.
* Breaking: integer enum members are named after their meaning, such as `OrderState.PendingShipment` instead of `Value3`. This covers `OrderState`, `OrderLineState`, `ListingStateValue`, `ProductCondition` and `ReturnReason`; the wire values are unchanged.
* A null item in a list parameter is skipped instead of throwing.
* An empty 204 response returns `null`, even where the spec also declares JSON, instead of throwing `ApiDecodeException`.
* New public `Download` and `RawBody` types, for binary response and request bodies. No operation in this package uses them yet.
* A page whose items field is missing or not a list throws `ApiDecodeException` for link-paged operations too, instead of ending as an empty last page.
* A file part of a multipart upload is sent with `Content-Type: application/octet-stream`.
* A multipart file part sends `filename*` only when the name is not ASCII, and never with quote marks inside it. It used to send the quoted name, so servers that read `filename*` first, such as ASP.NET Core, Django and Werkzeug, kept the quote marks as part of the file name. A `"` or `\` in the name is escaped. An empty name, or one with a control character such as CR or LF, throws `ArgumentException` before anything is sent.
* The runtime can poll an asynchronous job until it ends, and download a URL a response returns, sending credentials only to the base URL's origin. A new public `ApiJobTimeoutException` carries the last status in `Result` when a job outlasts its timeout. No operation in this package uses either yet.

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
