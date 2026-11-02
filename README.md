# backmarket-seller-sdk

Unofficial spec-driven SDKs for the Back Market Seller API.

This project is unofficial and is not affiliated with, endorsed by, or supported by Back Market.

The Python and TypeScript SDKs are unpublished alphas: see [`apis/backmarket/packages/python/`](apis/backmarket/packages/python/README.md) and [`apis/backmarket/packages/typescript/`](apis/backmarket/packages/typescript/README.md). The Go SDK is an untagged alpha: see [`apis/backmarket/packages/go/`](apis/backmarket/packages/go/README.md). C# and Rust will follow in that order.

## Quickstart

None of the SDKs is published yet. Install one from a checkout of this repository, and pass in your own API token.

### Python

```sh
pip install ./apis/backmarket/packages/python
```

```python
from backmarket_seller import BackMarketClient, Region

with BackMarketClient(
    "your-token",
    user_agent="BM-YourCompany-YourIntegration;you@example.com",
    locale="fr-fr",
    region=Region.EU,
) as client:
    for order in client.orders.iter():
        print(order.order_id)
```

The [Python README](apis/backmarket/packages/python/README.md) covers async use, errors, configuration and behaviour.

### TypeScript

Requires Node 22 or later. Build a tarball, then `npm install` it in your project:

```sh
cd apis/backmarket/packages/typescript
npm ci --ignore-scripts
npm run build
npm pack
```

```ts
import { BackMarketClient } from 'backmarket-seller';

const client = new BackMarketClient({
  token: 'your-token',
  userAgent: 'BM-YourCompany-YourIntegration;you@example.com',
  locale: 'fr-fr',
  region: 'eu',
});

for await (const order of client.orders.iter()) {
  console.log(order.order_id);
}
```

The [TypeScript README](apis/backmarket/packages/typescript/README.md) covers CommonJS, errors, configuration and behaviour.

### Go

Requires Go 1.24 or later. Every call takes a context and pages are walked with `range`:

```go
client, err := backmarketseller.NewClient(
	"your-token",
	"BM-YourCompany-YourIntegration;you@example.com",
	"fr-fr",
	backmarketseller.WithRegion(backmarketseller.RegionEU),
)
if err != nil {
	log.Fatal(err)
}
for order, err := range client.Orders.Iter(context.Background(), nil) {
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(*order.OrderID)
}
```

The [Go README](apis/backmarket/packages/go/README.md) covers installing from a checkout, errors, configuration and behaviour.

## Live API reports

Every test runs against a mock built from the public spec, so nothing here is confirmed against the live API. If you use an SDK for real, please report what you find, working or not, as a GitHub issue. The packages stay on 0.x until those reports confirm their behaviour.

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
npm run generate:typescript     # regenerate the TypeScript client; needs Java 21 and `npm ci --ignore-scripts` in the package
npm run conformance:typescript  # run the cases against the ESM build; `npm run build` in the package first
npm run conformance:typescript:cjs
npm run generate:go             # regenerate the Go client; needs Java 21 and Go 1.24 or later
npm run conformance:go          # build the driver and run the cases against the Go client
```

Once the spec is cached, the build and tests need no network. A hash mismatch stops the build; the error says how to recover.

A daily job opens a pull request when the upstream spec changes. See [Spec updates](docs/architecture.md#spec-updates).

All tests run against the mock. The project uses no live credentials.

## Licence

Apache-2.0: see [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE). The licence covers only this project's own code.

The upstream OpenAPI spec is not in this repository. It is fetched at build time, belongs to Back Market, and is not covered by this licence. The licence grants no right to the Back Market name.

This project is unofficial and is not affiliated with Back Market.
