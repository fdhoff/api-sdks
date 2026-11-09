# Conformance suite

Language-neutral YAML cases, kept under `apis/<api>/conformance/cases/`, run in CI for every language. A language is not supported until it passes.

```text
runner ── JSON lines ──> driver (one per language) ── HTTP ──> harness ──> Prism, or a scripted response
```

The harness records every request a client sends, so a case can assert the exact wire traffic. It answers from the Prism mock built from the spec, which also rejects requests the spec does not allow, or from a script, for what Prism cannot do: response sequences, delays, slow bodies, dropped connections and undeclared statuses.

## Running it

```sh
npm run spec:build
node toolchain/conformance/run.mjs apis/<api> --driver "<command that starts the driver>"
```

It prints one line per case and exits non-zero if any case fails.

## Case format

Each file in `cases/` holds a `cases:` list. `apis/<api>/conformance/defaults.yaml` holds a `client:` map merged under every case's `client`, and optionally a `secrets:` list naming client settings, besides `token`, that are credentials. Each named secret needs a synthetic value in `client:`.

```yaml
cases:
  - name: retries-then-succeeds        # unique, kebab-case
    client:                            # optional; see Client settings
      max_retries: 1
    request:
      operation: list-items            # an operationId in the built spec
      params: { page: 2 }              # path, query and header parameters, by wire name
      body: { quantity: 1 }            # optional JSON body
      multipart: { message: hello }    # optional multipart fields, instead of body
      raw_body_base64: JVBERg==        # optional raw request body as base64, instead of body
      paginate: true                   # optional: iterate every page
    mock:                              # exactly one of prism or responses
      responses:                       # one per request, in order
        - status: 500
          headers: { retry-after: '1' }
          body: { error: nope }        # a mapping or list is sent as JSON, a string verbatim
          body_base64: JVBERg==        # optional: exact body bytes as base64, instead of body
          delay_ms: 0
          trickle_ms: 50               # optional: send the body one byte at a time, this far apart
          gzip: true                   # optional: gzip the body if the request accepts gzip
          cut: -8                      # optional: send only the first n bytes, or drop the last -n
        - status: 200
          body: []
    wire:                              # every request the client must send, in order
      - method: GET
        host: files                    # optional: the host key the request went to
        path: /items
        query: { page: '2' }           # exact; omitted means no query string
        headers: { authorization: 'Basic {{token}}' }
        headers_match: { content-type: '^application/json' }  # regular expressions
        headers_absent: [accept-language]
        body: { quantity: 1 }          # JSON-equal to the request body
        parts: { files: [a, b] }       # multipart parts by name, each name's values in order; instead of body
        body_base64: JVBERg==          # the exact body bytes as base64; instead of body
        content_digest: true           # optional: Content-Digest is the SHA-256 of the exact body bytes
        min_delay_ms: 900              # time since the previous request
      - method: GET
        path: /items
        query: { page: '2' }
    expect:                            # exactly one of result, result_keys or error
      result: []                       # subset match; lists must have the same length
      logs_required: true              # optional: the client must have logged something
```

* `mock: { prism: { code: 404 } }` answers from Prism instead, asking for that declared status. Prism ignores a code the operation cannot serve for the client's `Accept` header, so check the mock before relying on one. `prism: {}` takes the first success response.
* `- drop: true` in `responses` reads the request, records it, then closes the connection with no response. It stands alone, with no `status` or other key.
* `gzip: true` compresses the body and sets `Content-Encoding: gzip`, but only when the request's `Accept-Encoding` allows gzip, as a server would. `cut` applies to the bytes sent, compressed or not, and `Content-Length` matches them.
* `{{http_date+2s}}` in a scripted header expands to an HTTP date that many seconds ahead, when the response is sent. HTTP dates are whole seconds, so the moment it names is up to a second sooner.
* `content_digest: true` asserts that `Content-Digest` is `sha-256=:<base64>:` of the exact bytes received. `fixtures/signing` has cases for a signed request, which an API that signs can copy.
* `parts` lists every part of a multipart body: a list sends one part per item, so two files are two `files` parts.
* A client whose operations are served from several hosts maps each host key `K` to `<base_url>/_host/K`. The harness records `K` as the request's `host`, removes the prefix, and matches or forwards to Prism the operation's own path. A wire item with `host` asserts the key; one without it does not check. `toolchain/conformance/fixtures/cases/hosts/` has synthetic cases to copy.
* A binary download's `result` is `{ content_type, base64 }`: the response's `Content-Type`, empty if it has none, and every byte of the body as base64. `toolchain/conformance/fixtures/cases/binary/` has synthetic cases for downloads, raw uploads and a text response that is not JSON.
* `result_keys: [id]` asserts that those keys exist, for Prism responses whose values come from spec examples. On a list it checks the first element.
* `error` is a subset match on the driver's error object.
* `{{token}}` in `mock`, `wire` and `expect` expands to the case's token, and `{{<name>}}` to each other secret.

Every case also asserts that the token and every other secret appear nowhere in the driver's result, error or logs.

## Client settings

Values a case or `defaults.yaml` may set. The runner adds `base_url` and `token`. `token` can be overridden; it is always synthetic.

| Setting | Meaning |
| --- | --- |
| `base_url` | Server root; the client must send every request here |
| `token` | Credential |
| Each name in `secrets` | Another credential, defined by the API's cases |
| `user_agent` | `User-Agent` value |
| `locale` | Client-level locale |
| `timeout_ms` | Per-attempt deadline, covering the whole response |
| `max_retries` | Retries after the first attempt |
| `retry_base_delay_ms` | Backoff base for retried failures |
| `rate_limit_wait_ms` | Wait after a rate limit with no usable `Retry-After` |
| `max_retry_wait_ms` | Longest `Retry-After` to wait for |
| `header_defaults` | Client-level values for header parameters that take one, by header name |
| `environment` | A named host map. A driver given one sends each host key's requests to `<base_url>/_host/<hostname>`, the hostname that environment maps the key to, so a wire item's `host` checks the map |

## Driver protocol

A driver is a small executable that lives beside its language package and calls the public client. It reads one JSON object per line on stdin, writes one per line on stdout, and exits at end of input. Anything else goes to stderr.

Input:

```json
{"case": "<name>", "client": {"base_url": "...", "token": "..."}, "request": {"operation": "...", "params": {}}}
```

Output is one of these, with `logs` holding what the client logged at its most verbose level:

```json
{"result": <decoded body, with wire field names>, "logs": []}
{"error": {"kind": "...", "status": 429}, "logs": []}
```

A paginated request's `result` is the list of items across all pages. A driver reports any exception the client raised as `error`; one it cannot express makes it exit, which aborts the run. The error kinds are defined by each API's cases.
