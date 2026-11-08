# Spec audit

Audit of the pinned upstream spec (`apis/etsy/spec/upstream/lock.json`, `info.version` 3.0.0): OpenAPI 3.0.2, 107 operations on 77 paths, 83 schemas, one server. It was written from the public spec and the Prism mock only; nothing here has been checked against the live API.

The spec carries no licence and reserves all rights, so it is never committed. The build fetches it from the URL in `lock.json` and checks its SHA-256. It is served as JSON, which the pipeline reads as YAML, so the cache keeps the `openapi.yaml` name. The overlay quotes no upstream prose.

Each gap is handled in one place, as for the other APIs: the overlay, the runtime, generator config, or left open.

## Corrected in the overlay

| ID | Gap | Correction |
| --- | --- | --- |
| E1 | 49 schemas set `default: null`, 44 of them on a type that is not nullable. Spectral rejects each as an invalid default. | Every null default removed: it means the same as no default. |
| E2 | Rate limits apply to every call, and a 429 carries `retry-after` and the `x-limit-per-second`, `x-remaining-this-second`, `x-limit-per-day` and `x-remaining-today` headers. The spec declares 429 on only one operation, the video upload, with no headers. | A shared `RateLimited` response with those headers and the error body, declared on every operation, replacing the video upload's own 429. |

## Authentication

Runtime:

* Every request sends `x-api-key: <keystring>:<shared_secret>`. The root security is `api_key` alone, and 31 operations inherit it.
* The other 76 operations declare one requirement holding both `api_key` and `oauth2`, so they also need `Authorization: Bearer <access token>`. Key-only operations must not send the bearer token.
* The access token comes from OAuth 2 authorization code with PKCE. The token endpoint is not in the spec; refresh is the runtime's and each package's job.

## Pagination

16 GET operations take `limit` (1 to 100, default 25) and `offset`, and answer `{count, results}`. The iterator advances `offset` by the results received and stops at an empty page or once `offset` reaches `count`.

## Request bodies

24 operations send `application/x-www-form-urlencoded`, 3 `multipart/form-data` and 4 JSON. Array fields in form bodies follow the 3.0 default, one field per value.

## Mock limits

* Prism rejects any array field in a form body, with or without an explicit `encoding`, so a case that sends one must script its response.
* Prism generates `count` from the schema, which has no minimum, so a mocked page can report a negative total. Paging cases that depend on `count` are scripted.

## Open

* Whether Etsy accepts repeated fields for form arrays, as the spec implies, needs live confirmation.
* How to clear a list field, such as `tags`, in an update. The 3.0 default sends nothing for an empty list, and the spec does not say what Etsy expects instead, so every SDK sends nothing and the field is left unchanged.
* Which statuses besides 429 carry the rate-limit headers.
