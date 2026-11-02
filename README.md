# backmarket-seller-sdk

Unofficial spec-driven SDKs for the Back Market Seller API.

This project is unofficial and is not affiliated with, endorsed by, or supported by Back Market.

The Python SDK is an unpublished alpha: see [`apis/backmarket/packages/python/`](apis/backmarket/packages/python/README.md). TypeScript, Go, C# and Rust will follow in that order.

## Layout

| Path | Contents |
| --- | --- |
| `toolchain/` | Generic pipeline, templates, runtime and conformance runner |
| `apis/backmarket/spec/upstream/` | `lock.json`, which pins the upstream OpenAPI spec by URL and SHA-256. The spec is not in this repository; it is fetched at build time into a gitignored cache here |
| `apis/backmarket/spec/overlay.yaml` | Our corrections, in [OpenAPI Overlay](https://spec.openapis.org/overlay/v1.0.0.html) format |
| `apis/backmarket/packages/` | Per-language package config and generated clients |
| `apis/backmarket/conformance/` | Language-neutral test cases and the reference driver |
| `apis/backmarket/docs/spec-audit.md` | Known gaps in the spec and where each is handled |

`toolchain/` must not name this API or contain its endpoints or schemas; a test enforces that. This boundary keeps later extraction cheap and is not a framework.

Generated output is never edited by hand. To correct the spec, add an action to `apis/backmarket/spec/overlay.yaml` and record why in `apis/backmarket/docs/spec-audit.md`; the build fails if an action stops matching.

## Design

See [`docs/architecture.md`](docs/architecture.md) for the pipeline, runtime contract, testing limits and the decisions behind them.

## Working on the spec

Requires Node 22 or later.

```sh
npm ci --ignore-scripts
npm run spec:fetch   # download the pinned spec if it is not cached, and check it against its lock
npm run spec:verify  # check the cached spec against its lock, offline
npm run spec:build   # apply the overlay, fetching first if needed, writing apis/backmarket/build/openapi.yaml
npm run spec:lint
npm run mock         # serve the built spec on http://127.0.0.1:4010
npm run conformance  # run the conformance cases with the reference driver
npm run spec:pin     # re-pin to the current upstream spec
npm run generate:python         # regenerate the Python client; needs Java 21 and the package's dev tools
npm run conformance:python      # run the cases against the sync Python client
npm run conformance:python:async
```

Once the spec is cached, the build and tests need no network. A hash mismatch stops the build; the error says how to recover.

All tests run against the mock. The project uses no live credentials.

## Licence

Apache-2.0: see [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE). The licence covers only this project's own code.

The upstream OpenAPI spec is not in this repository. It is fetched at build time, belongs to Back Market, and is not covered by this licence. The licence grants no right to the Back Market name.

This project is unofficial and is not affiliated with Back Market.
