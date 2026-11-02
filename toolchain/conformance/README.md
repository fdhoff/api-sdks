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

Each file in `cases/` holds a `cases:` list. `apis/<api>/conformance/defaults.yaml` holds a `client:` map merged under every case's `client`.

```yaml
cases:
  - name: retries-then-succeeds        # unique, kebab-case
    client:                            # optional; see Client settings
      max_retries: 1
    request:
      operation: list-items            # an operationId in the built spec
      params: { page: 2 }              # path and query parameters, by wire name
      body: { quantity: 1 }            # optional JSON body
      multipart: { message: hello }    # optional multipart fields, instead of body
      paginate: true                   # optional: iterate every page
    mock:                              # exactly one of prism or responses
      responses:                       # one per request, in order
        - status: 500
          headers: { retry-after: '1' }
          body: { error: nope }        # a mapping or list is sent as JSON, a string verbatim
          delay_ms: 0
          trickle_ms: 50               # optional: send the body one byte at a time, this far apart
        - status: 200
          body: []
    wire:                              # every request the client must send, in order
      - method: GET
        path: /items
        query: { page: '2' }           # exact; omitted means no query string
        headers: { authorization: 'Basic {{token}}' }
        headers_match: { content-type: '^application/json' }  # regular expressions
        headers_absent: [accept-language]
        body: { quantity: 1 }          # JSON-equal to the request body
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
* `{{http_date+2s}}` in a scripted header expands to an HTTP date that many seconds ahead, when the response is sent. HTTP dates are whole seconds, so the moment it names is up to a second sooner.
* `result_keys: [id]` asserts that those keys exist, for Prism responses whose values come from spec examples. On a list it checks the first element.
* `error` is a subset match on the driver's error object.
* `{{token}}` in `mock` and `wire` expands to the case's token.

Every case also asserts that the token appears nowhere in the driver's result, error or logs.

## Client settings

Values a case or `defaults.yaml` may set. The runner adds `base_url` and `token`. `token` can be overridden; it is always synthetic.

| Setting | Meaning |
| --- | --- |
| `base_url` | Server root; the client must send every request here |
| `token` | Credential |
| `user_agent` | `User-Agent` value |
| `locale` | Client-level locale |
| `timeout_ms` | Per-attempt deadline, covering the whole response |
| `max_retries` | Retries after the first attempt |
| `retry_base_delay_ms` | Backoff base for retried failures |
| `rate_limit_wait_ms` | Wait after a rate limit with no usable `Retry-After` |
| `max_retry_wait_ms` | Longest `Retry-After` to wait for |

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
