# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## Unreleased

* An empty success body where the spec declares JSON raises `DecodeError` instead of returning `None`. Where the spec declares text, it reads as `""`.
* Method arguments are checked against their declared types and limits, such as `page_size` up to 50, and raise `ValidationError` before a request is sent. Previously they were sent as given.
* A response body that does not fit its declared type at all raises `DecodeError` with the body in `raw_body`, instead of returning the decoded JSON. Fields inside an object are still parsed tolerantly.
* That `DecodeError` carries the response `status`, and its `raw_body` is the text as received rather than the JSON re-encoded.
* Methods with no declared response return `None`, as typed, instead of any body the API sent.
* Breaking: integer enum members are named after their meaning, such as `OrderState.PENDING_SHIPMENT` instead of `NUMBER_3`. This covers `OrderState`, `OrderLineState`, `ListingStateValue`, `ProductCondition` and `ReturnReason`; the wire values are unchanged.
* Breaking: the `Task` model is `BackgroundTask`, and its module `backmarket_seller.models.task` is `backmarket_seller.models.background_task`, as in every other language.

## 0.1.0a2 (2026-11-07)

* Requests now send `Accept-Encoding: gzip`, the only compression the client decodes. httpx otherwise asked for deflate, and br or zstd when their packages were installed, and every such response failed with `DecodeError`.

## 0.1.0a1 (2026-11-07)

* Typed sync and async clients for all 40 operations, generated from the public spec.
* Retries, rate-limit handling, pagination iterators, typed errors and redacted logging.
* `max_retry_wait`: a `Retry-After` above it, 60 seconds by default, raises `RateLimitedError` instead of blocking.
* `timeout` now covers each whole attempt, so a body that keeps trickling cannot outlast it.
* A compressed body that cannot be decompressed raises a typed error instead of a raw httpx error.
* A gzip success body that ends early raises `DecodeError` instead of returning partial or empty data.
* Tolerant response parsing no longer fails when an object holds a field under both its API and Python names.
* A `next` link that is not a valid URL raises `DecodeError` instead of a raw `ValueError`.
