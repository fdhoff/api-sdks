# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## 0.1.0-alpha.1 (unreleased)

* Async client for every operation, generated from the public spec, with `Result`-based errors.
* Retries, rate-limit handling, pagination streams, typed errors and redacted logging.
* Tolerant response decoding: a field that does not fit its type, and any unknown field, is kept in the model's `extra` map.
