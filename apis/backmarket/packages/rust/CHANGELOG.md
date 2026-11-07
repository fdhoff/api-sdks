# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## 0.1.0-alpha.1 (2026-11-07)

* Async client for every operation, generated from the public spec, with `Result`-based errors.
* Retries, rate-limit handling, pagination streams, typed errors and redacted logging.
* Tolerant response decoding: a field that does not fit its type, and any unknown field, is kept in the model's `extra` map.
* An optional or single-type union field has its type, such as `Competitor::min_price` as `MonetaryAmount` and `Task::last_action_error` as `String`, rather than `serde_json::Value`.
* Float query and form values are sent as Go and TypeScript send them: `100.0` as `100`, with no exponent, and `NaN` and infinities are sent rather than dropped.
* A gzip body of several members is read in full.
* A request that cannot be built is an `Api` error and is not retried as a connection failure.
