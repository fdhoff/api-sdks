# Live conformance

The mock cases check what each client sends. The live scenarios check that Gitea itself accepts it: they run each package against a real, disposable Gitea container at the pinned release, in CI on pull requests that touch Gitea, the conformance runner or a runtime, on main, and weekly. See `.github/workflows/live-gitea.yml`.

The suite never touches gitea.com or any other real instance. The runner refuses an instance URL that is not on this machine, and the container, its users and its token are made for one run and then removed.

## What runs

* `conformance/live/image.json` pins the official `gitea/gitea` image by digest, at the tag in `spec/upstream/lock.json`.
* `conformance/live/bootstrap.sh` starts it with SQLite, `INSTALL_LOCK=true` and a fixed `ROOT_URL`, and fails unless `/api/v1/version` reports the pinned version. It then creates a synthetic admin with `gitea admin user create` inside the container, a plain user, and an admin access token through the API with Basic auth. The passwords are random per run, and in CI they and the token are masked in the log.
* `conformance/live/run.mjs` runs every scenario in `conformance/live/scenarios/` through a driver, using the driver protocol of the mock cases. Requests go through a small proxy that passes everything through, response headers included, and records each request, so a step can count its pages.
* Each package has its own live driver. Python's is `packages/python/live/driver.py`, the conformance driver sending each request unchanged. TODO: TypeScript, Go, C# and Rust add theirs as each package lands.

## Scenario format

A scenario says what to call and what to assert, not exact wire bytes.

```yaml
scenario: pagination
client: { token: '{{token}}' }        # optional; this is the default
steps:
  - name: create-an-issue               # unique within the scenario
    repeat: 5                           # optional: run 5 times, with {{i}} from 1 to 5
    client: { username: '{{user}}', password: '{{user_password}}' }  # optional, instead of the scenario's
    request:                            # as in the mock cases: operation, params, body, multipart, paginate
      operation: issueCreateIssue
      params: { owner: '{{admin}}', repo: 'paging-{{run}}' }
      body: { title: 'Synthetic issue {{i}}' }
    save: issue                         # optional: later steps read the result as {{issue.number}}
    expect:                             # every key is optional
      result: { number: '{{i}}' }       # a subset match; { $regex: pattern } matches a string
      error: { kind: not_found, status: 404 }  # instead of result, count and unique
      count: 5                          # the number of items a paginated call returned
      unique: number                    # a field no two items share
      requests: 3                       # the number of HTTP requests the step sent
      wire:                             # checked on every request the step sent
        path_match: '/contents/docs%2Fnotes\.md$'
        headers_match: { accept: '^application/json$' }
```

`{{admin}}`, `{{admin_password}}`, `{{user}}`, `{{user_password}}` and `{{token}}` come from the bootstrap, and `{{run}}` is random per scenario, so names never collide. A value that is a single placeholder keeps the type of what it names, so a saved issue number stays a number. Every step also checks that no token, password or encoded Basic credential reaches the result, error or logs.

## What the scenarios settle

* **Paths:** every client sends a path parameter as one segment, so `docs/live/notes.md` goes as `docs%2Flive%2Fnotes.md`. Gitea v28.3.0 accepts it for contents and raw files.
* **Diffs:** the client asks for a commit diff with its default `Accept: application/json`, and Gitea v28.3.0 returns the text anyway. See the TODO in `conformance/README.md`.
* **Paging:** five issues two to a page take three requests, following `Link`, and each issue is seen once. Gitea's links name its `ROOT_URL`, which differs from the address the client is given, and the client never fetches them.

## Running it locally

You need Docker, Node 22, Python 3.10 or later, and `openssl`. From the repository root:

```sh
npm ci --ignore-scripts
python -m pip install ./apis/gitea/packages/python
apis/gitea/conformance/live/bootstrap.sh "${TMPDIR:-/tmp}/gitea-live.json"
node apis/gitea/conformance/live/run.mjs --settings "${TMPDIR:-/tmp}/gitea-live.json" --driver "python apis/gitea/packages/python/live/driver.py --mode sync"
docker rm --force gitea-live && rm "${TMPDIR:-/tmp}/gitea-live.json"
```

The container listens on `127.0.0.1:3000`. Set `GITEA_LIVE_PORT` or `GITEA_LIVE_CONTAINER` to use another port or container name. The settings file holds the run's synthetic credentials; delete it with the container.

## Upgrading Gitea

When the spec pin moves to a new tag, `image.json` must move with it: the bootstrap and `tests/live.test.mjs` fail until its tag matches. Take the new digest of the multi-architecture index from Docker Hub. TODO: have the spec drift job bump `image.json` in the same pull request.
