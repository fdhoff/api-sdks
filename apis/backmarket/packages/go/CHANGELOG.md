# Changelog

This module follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

* Breaking: `Task` is `BackgroundTask`, as in every other language.
* Breaking: the module path is now `github.com/fdhoff/api-sdks/apis/backmarket/packages/go`, following the repository rename. Update imports from `github.com/fdhoff/backmarket-seller-sdk/apis/backmarket/packages/go`. `0.1.0-alpha.1` stays at the old path.
* `APIError.Error()` includes the cause, such as the DNS or TLS failure behind "the connection failed", with the token removed. `errors.Is` and `errors.As` still reach the cause.
* The token is also removed where it appears path- or query-escaped, as in the URL of a timeout or connection error, and from the cause of a decode error.
* An empty success body where the spec declares JSON returns an error matching `ErrDecode` instead of an empty model.
* Breaking: integer enum members are named after their meaning, such as `OrderStatePendingShipment` instead of `OrderState3`. This covers `OrderState`, `OrderLineState`, `ListingStateValue`, `ProductCondition` and `ReturnReason`; the wire values are unchanged.
* An empty 204 response returns a nil result, even where the spec also declares JSON, instead of an error matching `ErrDecode`.
* Binary response and request bodies are read and sent as raw bytes where the spec declares them. No operation in this package does yet.

## 0.1.0-alpha.1 (2026-11-07)

* Typed client for all 40 operations, generated from the public spec, with `context.Context` on every call.
* Retries, rate-limit handling, pagination iterators, typed errors and redacted logging.
* A request that cannot be encoded is not sent, and returns an error wrapping the encoder's own rather than an `APIError`.
* An optional or single-type union field has its type, such as `Competitor.MinPrice` as `*MonetaryAmount` and `Task.LastActionError` as `*string`, rather than `any`.
