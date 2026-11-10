# Spec audit

Audit of the pinned upstream spec (`apis/gitea/spec/upstream/lock.json`, Gitea `v28.3.0`, retrieved 2026-11-09): OpenAPI 3.0.3, 537 operations, 234 schemas, one placeholder server and a placeholder `info.version`. It was written from the public spec, Gitea's public documentation, the Prism mock and one unauthenticated read of gitea.com; nothing else here has been checked against a live instance.

This project is not affiliated with, endorsed by or sponsored by the Gitea project or Gitea Limited.

## Source

Gitea generates the spec into its repository, and each release tag serves it at its own URL, `https://raw.githubusercontent.com/go-gitea/gitea/<tag>/templates/swagger/v1-openapi3.generated.json`. Its `info.license` is MIT. Like every other API's spec it is not committed: the build fetches it from the URL in `lock.json` and checks its SHA-256. The pipeline reads the JSON as YAML, so the cache keeps the `openapi.yaml` name. The overlay quotes no upstream prose.

`info.version` is the build placeholder `0.0.0+GITEA-API-APP-VERSION`, so `lock.json` records the release in `tag`. A tag's URL never changes, so the drift job never sees new content there. Instead:

* `spec/upstream-url.mjs` prints the spec URL and tag of the newest stable `vN.N.N` release, read with `git ls-remote --tags`. Release candidates are skipped. The drift job pins that URL, which moves `lock.json` to the new URL, hash and tag, and regenerates.
* `spec/check-upstream.mjs` runs in the drift workflow's `upstream` job and fails while a newer stable release is unpinned, or when the lock's URL is not its tag's spec URL.

## Corrected in the overlay

| ID | Gap | Correction |
| --- | --- | --- |
| G1 | 4 operations are deprecated. | Removed, leaving 533 operations. Their replacements are below. `/org/{org}/repos` and `/repos/{owner}/{repo}/times/{user}` are left with no operation and removed too. |
| G2 | The server is the build placeholder `/GITEA-API-APP-SUBURL/api/v1`. | `https://gitea.example.com/api/v1`. Every instance has its own URL, so there are no hosts or environments and the caller always supplies the base URL, which may include a sub-path such as `https://example.com/git`. |
| G3 | Of the 7 security schemes, `Token` and `AccessToken` send a token in the query string and are deprecated upstream, and `SudoParam` duplicates `SudoHeader` in the query string. Each security requirement names one scheme alone, so the one-time password and Sudo never join a credential. | The three query schemes are removed: a credential must never sit in a URL, where proxies and logs keep it. The requirements become a token or Basic, Basic optionally with `TOTPHeader`, and either one optionally with `SudoHeader`. See Authentication. |
| G4 | `error`, `forbidden`, `unauthorized`, `validationError`, `repoArchivedError` and `invalidTopicsError` declare `message` and `url` as response headers, and `notFound` and `conflict` declare nothing, while Gitea sends a JSON body with those fields. 55 operations declare no error response at all. | Each of those responses gets the `APIError` body, with `message` and `url`, and loses the headers. `invalidTopicsError`'s body also holds `invalidTopics`, which `APIError` allows. The 55 operations get `error` as 400, `unauthorized` as 401, `forbidden` as 403, `notFound` as 404, `validationError` as 422 and `error` as 5XX. |
| G5 | `repoDownloadCommitDiffOrPatch` and `repoDownloadPullDiffOrPatch` declare a JSON string but return text. `repoGetArchive` declares no body but returns an archive. `repoCreateReleaseAttachment` offers a raw `application/octet-stream` body declared as an object, beside the multipart form that carries the same file. | The two diffs are `text/plain` and the archive `application/octet-stream` binary. The release attachment keeps only its multipart form, since the toolchain takes one request media type per operation. TODO: offer the raw upload, with `name` in the query, if users ask. |

## Deprecated operations

| Removed | Replacement |
| --- | --- |
| `createOrgRepoDeprecated` | `createOrgRepo` |
| `issueDeleteCommentDeprecated` | `issueDeleteComment` |
| `issueEditCommentDeprecated` | `issueEditComment` |
| `userTrackedTimes` | `repoTrackedTimes` with `user` |

## Authentication

Runtime: users supply credentials at runtime.

* An access token goes as `Authorization: token <token>`, the `AuthorizationHeaderToken` scheme.
* Basic takes a username and password. With two-factor authentication on, it adds the current one-time password as `X-GITEA-OTP`, which Gitea reads only with Basic.
* Either one may add `Sudo: <username>` to act as another user, which needs an admin.

Every secret, and the encoded Basic header, is redacted from logs and errors. TODO: OAuth2 bearer tokens, which Gitea also accepts, if users ask.

## Pagination

* 112 operations take `page` and `limit`, and Gitea gives the next page only in an RFC 8288 `Link` header, whose URLs start with the server's configured root URL. `sdk.yaml` sets `paging: { style: link_header, rel: next, params: [page, limit] }`, so the iterator copies only `page` and `limit` out of the `next` link into its own request and never fetches it. That root URL can differ from the client's, behind a proxy for example.
* 94 of them answer a top-level list, so their iterators read `items: $`. The other 18 hold their items under a field: `workflow_runs` (6, including `ListActionTasks`), `jobs` (6), `data` (`repoSearch`, `teamSearch` and `userSearch`), `topics` (`repoListTopics` and `topicSearch`) and `statuses` (`repoGetCombinedStatusByRef`).
* The spec declares `X-Total-Count` on only 3 responses and `Link` on none. Neither the mock nor the generators need them, since the scripted cases set them and the runtimes read response headers directly, so the overlay does not add them.
* `GetTree` pages with `page` and `per_page`, and `repoGetWikiPageRevisions` with `page` alone. Neither has an iterator. TODO: page them if users find they truncate.

## Paths

Path parameters are each one segment. A file path such as `docs/guide/intro.md` in `contents/{filepath}`, `raw/{filepath}`, `media/{filepath}` or `editorconfig/{filepath}` is therefore sent as `docs%2Fguide%2Fintro.md`, which is what every runtime already does, and `paths.yaml` pins it. One unauthenticated read on gitea.com on 2026-11-09 accepted both `/` and `%2F`, and the later live suite is to confirm `%2F` on the pinned release. Gitea's own Go SDK sends `/`. Some reverse proxies refuse an encoded slash, Apache's default among them. TODO: send a file path's `/` as is if users behind such a proxy report 404s.

## Files

* Binary downloads: `repoGetRawFile`, `repoGetRawFileOrLFS` and, after G5, `repoGetArchive`.
* Text: the four signing keys (`getSigningKey`, `getSigningKeySSH`, `repoSigningKey` and `repoSigningKeySSH`), and after G5 the two diffs. `renderMarkdownRaw` takes a `text/plain` body.
* Multipart uploads: `issueCreateIssueAttachment`, `issueCreateIssueCommentAttachment` and `repoCreateReleaseAttachment`, each with one `attachment` file part. Their inline bodies get names in `packages/names.yaml`. The two issue uploads send the same body, which generators share under the first one's name.
* `downloadArtifact` answers 302 to the artifact's blob, and `orgIsMember` 303. Neither declares a body.

## Inline models

`packages/names.yaml` names the inline bodies that generators would otherwise name after their operationId: the three attachment uploads, and the `teamSearch` and `userSearch` results, each a `data` list with an `ok` flag. `repoSearch` already uses the `SearchResults` schema.

## Open

* Lint warns that 512 operations have no description and that `info` has no contact. Neither affects generation.
* `invalidTopicsError`'s extra `invalidTopics` field reaches users only through the error's raw body.
