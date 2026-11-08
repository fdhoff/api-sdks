# api-sdks

Unofficial, spec-driven SDKs for third-party APIs, one directory per API under `apis/`. Each is generated from the API's public OpenAPI spec and tested against a mock built from it.

| API | Directory | Status |
| --- | --- | --- |
| Back Market Seller API | [`apis/backmarket/`](apis/backmarket/) | Alphas in Python, TypeScript, Go, C# and Rust |
| Etsy Open API | — | In progress, not yet in this repository |

Every SDK here is unofficial and is not affiliated with, endorsed by, or supported by the company whose API it calls, including Back Market.

## Back Market Seller API

The Python and TypeScript SDKs are alphas on PyPI and npm: see [`apis/backmarket/packages/python/`](apis/backmarket/packages/python/README.md) and [`apis/backmarket/packages/typescript/`](apis/backmarket/packages/typescript/README.md). The Go SDK is a tagged alpha: see [`apis/backmarket/packages/go/`](apis/backmarket/packages/go/README.md). The C# and Rust SDKs are alphas on NuGet and crates.io: see [`apis/backmarket/packages/csharp/`](apis/backmarket/packages/csharp/README.md) and [`apis/backmarket/packages/rust/`](apis/backmarket/packages/rust/README.md).

### Quickstart

Every SDK installs from its registry. Pass in your own API token.

#### Python

```sh
pip install --pre backmarket-seller
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

#### TypeScript

Requires Node 22 or later.

```sh
npm install backmarket-seller@alpha
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

#### Go

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

The [Go README](apis/backmarket/packages/go/README.md) covers installing, errors, configuration and behaviour.

#### C#

Requires .NET 8 or later.

```sh
dotnet add package BackMarketSeller --prerelease
```

Every call is async, and pages are walked with `await foreach`:

```csharp
using var client = new BackMarketClient("your-token", new BackMarketClientOptions
{
    UserAgent = "BM-YourCompany-YourIntegration;you@example.com",
    Locale = "fr-fr",
    Region = Region.EU,
});

await foreach (var order in client.Orders.ListAllAsync())
{
    Console.WriteLine(order.OrderId);
}
```

The [C# README](apis/backmarket/packages/csharp/README.md) covers installing, errors, configuration and behaviour.

#### Rust

Requires Rust 1.85 or later and a Tokio runtime.

```sh
cargo add backmarket-seller@0.1.0-alpha.1
```

Every call is async and returns a `Result`, and pages are walked as a `Stream`:

```rust
let client = Client::builder("your-token", "BM-YourCompany-YourIntegration;you@example.com", "fr-fr")
    .region(Region::Eu)
    .build()?;

let mut orders = client.orders().iter(&OrdersListParams::default());
while let Some(order) = orders.try_next().await? {
    println!("{:?}", order.order_id);
}
```

The [Rust README](apis/backmarket/packages/rust/README.md) covers installing, errors, configuration and behaviour.

### Live API reports

Every test runs against a mock built from the public spec, so nothing here is confirmed against the live API. If you use an SDK for real, please report what you find, working or not, as a GitHub issue. The packages stay on 0.x until those reports confirm their behaviour.

One gap to watch for: where the spec declares a JSON success body, every SDK treats an empty body as a decode error. A write that really answers with nothing, such as the buyback listing update (`202`) or a listing create or update, would then fail even though the API accepted it. If you see that, please report the operation and status. Confirmed cases are fixed in the overlay.

## Layout

| Path | Contents |
| --- | --- |
| `toolchain/` | Generic pipeline, templates, runtime and conformance runner |
| `apis/backmarket/spec/upstream/` | `lock.json`, which pins the upstream OpenAPI spec by URL and SHA-256. The spec is not in this repository; it is fetched at build time into a gitignored cache here |
| `apis/backmarket/spec/overlay.yaml` | Our corrections, in [OpenAPI Overlay](https://spec.openapis.org/overlay/v1.0.0.html) format |
| `apis/backmarket/packages/` | Per-language package config and generated clients |
| `apis/backmarket/conformance/` | Language-neutral test cases and the reference driver |
| `apis/backmarket/docs/spec-audit.md` | Known gaps in the spec and where each is handled |
| `apis/etsy/` | The same for Etsy's Open API v3: spec pin, overlay, conformance cases and spec audit. No package yet |

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
npm run generate:csharp         # regenerate the C# client; needs Java 21 and .NET 10
npm run conformance:csharp      # build the driver and run the cases against the C# client on .NET 10
npm run conformance:csharp:net8
npm run generate:rust           # regenerate the Rust client; needs Java 21 and rustfmt
npm run conformance:rust        # build the Rust driver and run the cases against it
```

The scripts work on `apis/backmarket` by default. Set `API` to use another directory under `apis/`, for example `API=<api> npm run spec:build`. They need a POSIX shell.

Once the spec is cached, the build and tests need no network. A hash mismatch stops the build; the error says how to recover.

A daily job opens a pull request when the upstream spec changes. See [Spec updates](docs/architecture.md#spec-updates).

All tests run against the mock. The project uses no live credentials.

## Licence

Apache-2.0: see [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE). The licence covers only this project's own code.

The upstream OpenAPI specs are not in this repository. They are fetched at build time, belong to Back Market and Etsy, and are not covered by this licence. The licence grants no right to the Back Market or Etsy names.

This project is unofficial and is not affiliated with Back Market or Etsy.
