# gitea-rest

Unofficial TypeScript client for the Gitea API. Not affiliated with, endorsed by or sponsored by the Gitea project or Gitea Limited.

Gitea is a self-hosted Git service. This client talks to any Gitea instance, your own or [gitea.com](https://gitea.com), at the URL you give it. Its methods and types are generated from the API spec of one pinned Gitea release, v28.3.0, so an older or newer instance may lack an operation or send other fields.

**Alpha.** It is tested against a mock built from the spec, and a disposable Gitea container is next. It has not yet been confirmed against real instances. If you use it, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Before you start

* You need your instance's URL, such as `https://gitea.example.com`, or `https://example.com/git` for an instance under a sub-path. There is no default. The client adds `/api/v1`.
* You need your own credentials: an access token, made under Settings → Applications on your instance, or a username and password. This package ships with none.
* Keep your credentials on a server. Never ship them to a browser.

## How this differs from other SDKs

Gitea's only official SDK is for Go, `code.gitea.io/sdk/gitea`. On npm, `gitea-js` is a generated client whose last release, v1.23, was in January 2025. This package tracks the pinned Gitea release, and is generated from its spec with siblings in other languages in [the same repository](https://github.com/fdhoff/api-sdks). Every language passes one shared conformance suite, so retries, paging, errors and redaction behave the same in each. It adds:

* typed methods for all 533 current operations, with no runtime dependencies;
* async iterators that walk every page by following the `Link` header;
* errors typed by status, carrying Gitea's error message;
* your token, password and one-time password kept out of every error and log line.

## Install

The package is not on npm yet. From a clone of this repository:

```sh
cd apis/gitea/packages/typescript
npm ci && npm run build && npm pack
npm install /path/to/gitea-rest-0.1.0-alpha.1.tgz
```

Requires Node.js 22 or later. It ships as ESM and CommonJS.

## Quickstart

```ts
import { GiteaClient, NotFoundError } from 'gitea-rest';

const client = new GiteaClient({ baseUrl: 'https://gitea.example.com', token: 'your-access-token' });

const me = await client.currentUser.get();
console.log(me.login);

for await (const issue of client.issues.iter('your-org', 'your-repo', { state: 'open', limit: 50 })) {
  console.log(issue.number, issue.title);
}

try {
  await client.repos.get('your-org', 'missing-repo');
} catch (error) {
  if (!(error instanceof NotFoundError)) throw error;
  console.log(error.status, error.detail);
}
```

Your credentials are read from nowhere and stored nowhere: you pass them in, and the client sends them only to your `baseUrl`.

## Authentication

Pass one of these:

* **An access token**, as `token`. It is sent as `Authorization: token <token>`.
* **A username and password**, sent with Basic authentication. If your account has two-factor authentication on, add the current one-time password as `otp`; it is sent as `X-GITEA-OTP`. A one-time password expires within a minute, so this suits a short task, such as creating an access token to use from then on.
* **A `credentials` provider**, an object with `apply` and `secrets`, for anything else, such as an OAuth2 bearer token.

With a token or a username and password, `sudo` acts as another user, sent as `Sudo`. That needs an admin's credentials.

```ts
import { GiteaClient } from 'gitea-rest';

const client = new GiteaClient({
  baseUrl: 'https://gitea.example.com',
  username: 'your-username',
  password: 'your-password',
  otp: '123456',
});
const token = await client.users.createToken('your-username', { name: 'scripts', scopes: ['read:repository'] });
console.log(token.name);
```

## Configuration

`new GiteaClient(options)` takes:

| Option | Default | Meaning |
| --- | --- | --- |
| `baseUrl` | required | Your instance's URL, without `/api/v1`. Your credentials are sent to it |
| `token` | none | An access token |
| `username`, `password` | none | Basic authentication, instead of a token |
| `otp` | none | A one-time password, sent as `X-GITEA-OTP` with Basic only |
| `sudo` | none | A user to act as, sent as `Sudo` |
| `credentials` | none | Your own `Credentials` provider, instead of the others |
| `userAgent` | none | Sent as `User-Agent` when given |
| `timeoutMs` | `30000` | Milliseconds to wait on each attempt |
| `maxRetries` | `3` | Retries after the first attempt |
| `retryBaseDelayMs` | `500` | Base in milliseconds of the exponential backoff |
| `rateLimitWaitMs` | `10000` | Milliseconds to wait after a 429 with no usable `Retry-After` |
| `maxRetryWaitMs` | `60000` | Longest `Retry-After` to wait for, in milliseconds. A longer one throws `RateLimitedError` at once |
| `fetch` | global `fetch` | A `fetch` to use instead |
| `logger` | none | Receives `debug` and `info` lines |

Every method also takes `{ signal }`, an `AbortSignal` that cancels the call.

## Behaviour

* **Methods** are grouped by area: `repos`, `branches`, `tags`, `contents`, `commits`, `git`, `pulls`, `releases`, `wiki`, `issues`, `labels`, `milestones`, `projects`, `hooks`, `actions`, `orgs`, `teams`, `users`, `currentUser`, `notifications`, `packages`, `admin` and `misc`. Model types are exported from the package root. Every method's comment ends with its Gitea operationId, such as `(issueListIssues)`, so you can find it in Gitea's API docs. Where an organization or your own account has the same kind of resource as a repository, the method ends in `ForOrg` or `ForUser`, such as `hooks.listForOrg` and `actions.listRunnersForUser`. The 4 deprecated operations are left out.
* **Pagination:** `list` and `search` methods return one page, and the matching `iter` methods walk all of them with `for await`. Gitea names the next page only in each response's `Link` header. The iterator copies its `page` and `limit` into its own next request, with your other arguments, and never fetches the link itself, whose host is your instance's configured root URL and may differ from your `baseUrl`. A link back to a page already sent throws `DecodeError`.
* **Paths:** each path argument is one URL segment, so a file path such as `docs/intro.md` is sent as `docs%2Fintro.md`.
* **Timeouts:** `timeoutMs` is the time allowed for each attempt, including reading the whole response.
* **Retries:** 429 on every method, honouring `Retry-After` up to `maxRetryWaitMs`, otherwise after `rateLimitWaitMs`. 5xx, timeouts and connection failures on GET only, with exponential backoff. Writes are not retried after those, because a repeat could act twice.
* **Errors** derive from `ApiError`. Error responses throw an `HttpError` subclass, such as `NotFoundError`, `ConflictError` or `UnprocessableError`, with `status`, `detail`, Gitea's error message when the body has one, `retryAfter` and `rawBody`, the body as text. Every credential is removed from all of them. Compare `error.kind` to narrow the type.
* **Logging** goes only to the `logger` you pass. It holds methods, URLs and statuses, never your credentials or response bodies.
* **Responses** are not checked at all, because the spec has not been confirmed against every release. The types describe what the spec declares: a field can hold another type, a required field can be missing, and unknown fields are kept. Check values if you depend on them. An empty 204 resolves to `undefined`, and a JSON body that does not parse throws `DecodeError`.
* **Files:** raw files, media and archives resolve to a `Download`; read it once with `bytes()` or `body`. Diffs, patches and signing keys resolve to text. Attachment uploads take a `Blob`, a `Uint8Array` or `{ filename, content }`.

## Limits

* `repos.listTopics` and `admin.listUnadoptedRepos` return one page of strings, with no iterator yet.
* `git.getTree` and `wiki.listPageRevisions` page differently from the rest, and have no iterator.
* OAuth2 bearer tokens have no option of their own. TODO: add one if users ask; a `credentials` provider can send one meanwhile.

## Testing

Every test runs against a mock built from the spec, with synthetic credentials. The tests never use a real account or call a real instance. A suite that runs against a disposable Gitea container in CI is next.

## Design

See the [architecture document](https://github.com/fdhoff/api-sdks/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code. It does not cover Gitea's spec, which is fetched at build time and not included, and grants no right to the Gitea name.
