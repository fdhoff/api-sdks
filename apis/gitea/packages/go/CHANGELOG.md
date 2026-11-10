# Changelog

This module follows semantic versioning and stays on 0.x until outside users confirm its behaviour against real Gitea instances.

## 0.1.0-alpha.1 (unreleased)

The first alpha.

* Typed client for the 533 current operations of the Gitea API at v28.3.0, generated from the spec, with `context.Context` on every call and each method's operationId in its doc comment.
* An instance URL you supply, with no default, to which the client adds `/api/v1`, so sub-path installs work.
* An access token through `Token`, or Basic authentication through `Basic` and `BasicWithOTP`, and an optional `WithSudo` user, with every secret redacted from errors and logs. Credentials of your own can replace them through the `Credentials` interface.
* Iterators on all 112 paged operations, following the `Link` header without fetching it, including the two whose pages hold strings.
* Raw files, media and archives download as their exact bytes; diffs, patches and signing keys return text.
* Typed errors with the status, Gitea's error message in `Detail` and the raw body, and retries and rate-limit handling.
