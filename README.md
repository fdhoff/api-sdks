# backmarket-seller-sdk

Unofficial spec-driven SDKs for the Back Market Seller API.

This project is unofficial and is not affiliated with, endorsed by, or supported by Back Market.

No SDK is usable yet. Python, Go, C# and Rust will ship in that order.

## Layout

| Path | Contents |
| --- | --- |
| `toolchain/` | Generic pipeline, templates, runtime and conformance runner |
| `apis/backmarket/spec/upstream/` | The upstream OpenAPI spec, verbatim, with its pin in `lock.json` |
| `apis/backmarket/spec/overlay.yaml` | Our corrections, in [OpenAPI Overlay](https://spec.openapis.org/overlay/v1.0.0.html) format |
| `apis/backmarket/packages/` | Per-language package config and generated clients |
| `apis/backmarket/conformance/` | Language-neutral test cases |
| `apis/backmarket/docs/spec-audit.md` | Known gaps in the spec and where each is handled |

`toolchain/` must not name this API or contain its endpoints or schemas; a test enforces that. This boundary keeps later extraction cheap and is not a framework.

Generated output is never edited by hand. To correct the spec, add an action to `apis/backmarket/spec/overlay.yaml` and record why in `apis/backmarket/docs/spec-audit.md`; the build fails if an action stops matching.

## Working on the spec

Requires Node 22 or later.

```sh
npm ci --ignore-scripts
npm run spec:verify  # check the pinned spec against its lock
npm run spec:build   # apply the overlay, writing apis/backmarket/build/openapi.yaml
npm run spec:lint
npm run mock         # serve the built spec on http://127.0.0.1:4010
npm run spec:fetch   # re-pin to the current upstream spec
```

All tests run against the mock. The project uses no live credentials.
