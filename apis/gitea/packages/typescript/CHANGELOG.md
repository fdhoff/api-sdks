# Changelog

This package follows semantic versioning and stays on 0.x until outside users confirm its behaviour against real Gitea instances.

## 0.1.0-alpha.1 (unreleased)

The first alpha.

* Typed client for the 533 current operations of the Gitea API at v28.3.0, generated from the spec, for Node.js 22 or later, as ESM and CommonJS, with no runtime dependencies. Each method's comment names its operationId.
* An instance URL you supply, with no default, to which the client adds `/api/v1`, so sub-path installs work.
* An access token, or Basic authentication with an optional one-time password, and an optional `sudo` user, all redacted from errors and logs. A custom `credentials` provider can replace them.
* Async iterators on 110 paged operations, following the `Link` header without fetching it.
* Typed errors with the status, Gitea's error message and the raw body, retries, rate-limit handling, cancellation and redacted logging.
