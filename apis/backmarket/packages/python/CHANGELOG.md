# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## 0.1.0a1 (unreleased)

* Typed sync and async clients for all 40 operations, generated from the public spec.
* Retries, rate-limit handling, pagination iterators, typed errors and redacted logging.
* `max_retry_wait`: a `Retry-After` above it, 60 seconds by default, raises `RateLimitedError` instead of blocking.
* `timeout` now covers each whole attempt, so a body that keeps trickling cannot outlast it.
* A compressed body that cannot be decompressed raises a typed error instead of a raw httpx error.
* Tolerant response parsing no longer fails when an object holds a field under both its API and Python names.
* A `next` link that is not a valid URL raises `DecodeError` instead of a raw `ValueError`.
