# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against real Gitea instances.

## 0.1.0-alpha.1 (unreleased)

The first alpha.

* Async client with typed models for the 533 current operations of the Gitea API at v28.3.0, generated from the spec, targeting .NET 10 and .NET 8. Each method's XML doc comment ends with its operationId, and every method takes a `CancellationToken`.
* An instance URL you supply, with no default, to which the client adds `/api/v1`, so sub-path installs work.
* `GiteaCredentials.Token` or `GiteaCredentials.Basic`, with an optional one-time password, and an optional `Sudo` user, all redacted from exceptions and logs.
* `ListAll…Async` and `SearchAll…Async` iterators on 112 paged operations, pages of strings included, following the `Link` header without fetching it.
* An `HttpClient` of your own, such as one from `IHttpClientFactory`, or an `HttpMessageHandler`.
* Typed exceptions by status, with Gitea's error message in `Detail` and the raw body, retries, rate-limit handling and redacted logging.
