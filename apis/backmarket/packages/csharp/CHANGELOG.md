# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## 0.1.0-alpha.1 (unreleased)

* Async client for all 40 operations, generated from the public spec, targeting .NET 10.
* Retries, rate-limit handling, pagination as `IAsyncEnumerable`, typed exceptions and redacted logging.
* Tolerant responses: values that do not fit, and unknown fields, are kept in `Extra`.
