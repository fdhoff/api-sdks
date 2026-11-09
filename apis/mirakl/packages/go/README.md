# miraklseller

Unofficial Go client for the Mirakl marketplace seller API. Not affiliated with, endorsed by or sponsored by Mirakl SAS.

**Alpha.** It is tested only against a mock built from the public spec, never against the live API. If you use it for real, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Before you start

* Mirakl is software that marketplace operators run, each on its own instance. You sell on an operator's marketplace, such as Best Buy's, and that operator gives you its base URL. There is no shared host: every client needs one.
* There is no public sandbox. Ask your operator whether it has a test instance before you call a live one.
* You need your shop's API key, which you create in the operator's back office. This module ships with no key. It is sent as the whole `Authorization` header, with no `Bearer` or other scheme.
* A key can cover several shops. Pick one with `WithShopID`, or per call with the `ShopID` field; without either, the operator uses the key's default shop.
* Mirakl publishes official SDKs only in PHP, and in Java for its customers. This module is generated from Mirakl's published OpenAPI spec, as are its siblings in [the same repository](https://github.com/fdhoff/api-sdks), and they share one conformance suite.

## Install

No version is tagged yet, so take a commit from `main`:

```sh
go get github.com/fdhoff/api-sdks/apis/mirakl/packages/go@main
```

Requires Go 1.24 or later.

## Quickstart

```go
package main

import (
	"context"
	"errors"
	"fmt"
	"log"
	"os"

	"github.com/fdhoff/api-sdks/apis/mirakl/packages/go/miraklseller"
)

func main() {
	client, err := miraklseller.NewClient(
		"https://your-operator.mirakl.net",
		miraklseller.APIKey(os.Getenv("MIRAKL_API_KEY")),
		miraklseller.WithShopID(2001),
	)
	if err != nil {
		log.Fatal(err)
	}
	ctx := context.Background()

	params := &miraklseller.OrdersListParams{OrderStateCodes: miraklseller.Ptr("WAITING_ACCEPTANCE"), Max: miraklseller.Ptr[int64](100)}
	for order, err := range client.Orders.Iter(ctx, params) {
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(*order.OrderID)
	}

	_, err = client.Offers.GetStockImport(ctx, "missing-import", nil)
	var failure *miraklseller.APIError
	if errors.Is(err, miraklseller.ErrNotFound) && errors.As(err, &failure) {
		fmt.Println(failure.Status, failure.RawBody)
	}
}
```

The base URL is the instance's root, before `/api`. Your key is read from nowhere and stored nowhere: you pass it in, and the client sends it only to that base URL.

## Imports and exports

Offer, product and stock imports, and offer, order and transaction exports, run in the background. Each start method returns an ID, and a `Wait` method polls the job's status until it ends:

```go
started, err := client.Offers.ImportStock(ctx, &miraklseller.OffersImportStockParams{
	File: miraklseller.File{Name: "stock.csv", Content: []byte("offer-sku;quantity\nsku-1;5\n")},
})
if err != nil {
	log.Fatal(err)
}
status, err := client.Offers.WaitStockImport(ctx, *started.ImportID, &miraklseller.WaitOptions{Timeout: 30 * time.Minute})
if err != nil {
	log.Fatal(err)
}
if *status.Status == "FAILED" || (status.HasErrorReport != nil && *status.HasErrorReport) {
	report, err := client.Offers.DownloadStockImportErrorReport(ctx, *started.ImportID, nil)
	// Read and close report.Body.
}
```

| Start | Wait |
| --- | --- |
| `Offers.Import` (OF01) | `Offers.WaitImport` (OF02) |
| `Offers.ImportStock` (STO01) | `Offers.WaitStockImport` (STO02) |
| `Products.Import` (P41) | `Products.WaitImport` (P42) |
| `Offers.Export` (OF52) | `Offers.WaitExport` (OF53) |
| `Orders.Export` (OR13) | `Orders.WaitExport` (OR14) |
| `Transactions.Export` (TL03) | `Transactions.WaitExport` (TL04) |

A wait polls once a minute for up to an hour unless `WaitOptions` says otherwise. Mirakl allows about one status call a minute, so a shorter interval may be rate limited, and a 429 is retried after its `Retry-After`. A job that fails returns its final status, not an error, so you can fetch its error report. At the deadline a wait returns an error matching `ErrJobTimeout`, with the last status in `APIError.Result`. Cancelling the context stops it at once. A price import (PRI01) has no wait, since its status is a list: page through `Offers.ListPriceImports` instead.

A finished export lists its files as URLs. Fetch each with `DownloadURL`:

```go
status, err := client.Offers.WaitExport(ctx, *started.TrackingID, nil)
if err != nil {
	log.Fatal(err)
}
for _, address := range status.URLs {
	file, err := client.DownloadURL(ctx, address)
	if err != nil {
		log.Fatal(err)
	}
	// Read and close file.Body.
}
```

`DownloadURL` sends your key only when the URL has the base URL's scheme, host and port. A URL on another host, such as file storage, gets no key, and neither does any request after a redirect leaves the base URL's origin. It follows up to five redirects, and logs the URL without its query, which may hold a signature.

## Configuration

`NewClient(baseURL, credentials, options...)` takes these options:

| Option | Default | Meaning |
| --- | --- | --- |
| `WithShopID` | None | The `shop_id` sent on every call that does not set its own |
| `WithUserAgent` | None | Sent as `User-Agent` |
| `WithTimeout` | 30 seconds | Deadline for each attempt, covering the whole response |
| `WithMaxRetries` | 3 | Retries after the first attempt |
| `WithRetryBaseDelay` | 500 ms | Base of the exponential backoff |
| `WithRateLimitWait` | 10 seconds | Wait after a 429 with no usable `Retry-After` |
| `WithMaxRetryWait` | 60 seconds | Longest `Retry-After` to wait for |
| `WithHTTPTransport` | `http.DefaultTransport` | An `http.RoundTripper` to use instead of the network |
| `WithLogger` | None | A `*slog.Logger` |

`APIKey(key)` is the credentials for a shop API key. To authenticate another way, pass your own `Credentials`: its `Apply` sets the headers of each attempt, retries included, and `Secrets` lists every value to keep out of logs and errors.

A `Client` is safe for concurrent use.

## Behaviour

* **Methods** are grouped by resource: `client.Account`, `client.Offers`, `client.Orders`, `client.Shipments`, `client.Products`, `client.Promotions`, `client.Returns`, `client.Threads`, `client.Invoices`, `client.Transactions` and `client.Settings`. Each method's doc comment ends with Mirakl's API code, such as OR11, so you can find it in Mirakl's docs.
* **Coverage:** the 116 current operations. The 11 deprecated ones are left out, and so are three that the spec gives only a placeholder path, since each fetches a URL an export returns: use `DownloadURL` for those.
* **Context:** every method takes a `context.Context`. Cancelling it stops the call, including any wait before a retry, and the call returns the context's error, not an `APIError`. Use it for an overall deadline; `WithTimeout` applies to each attempt.
* **Pagination:** `List` methods return one page, and `Iter` methods return an iterator for `range` over every item. Orders, offers, invoices, products, product imports and promotions page by `offset` and `max`, up to `total_count`. The others send each page's `next_page_token` back as `page_token` until there is none. Iterators start where your own `Offset` or `PageToken` says, keep your `ShopID` and filters on every page, and stop after yielding an error.
* **Retries:** 429 on every method, honouring `Retry-After`, otherwise after `WithRateLimitWait`. A `Retry-After` longer than `WithMaxRetryWait` returns `ErrRateLimited` at once, with the header in `RetryAfter`. 5xx, timeouts and connection failures on GET only, with exponential backoff. Writes are not retried after those, because a repeat could act twice.
* **Redirects** are never followed, except by `DownloadURL`. A 3xx returns `ErrAPI`, so your key stays on your base URL.
* **Errors** are `*APIError`, with `Kind`, `Status`, `RetryAfter` and `RawBody`, the body as text with your key removed. Mirakl documents no error body, so the client does not parse one. Test the kind with `errors.Is` and a sentinel such as `ErrNotFound`, `ErrPermission` or `ErrBadRequest`.
* **Logging** goes to your `slog.Logger`, and holds methods, URLs and statuses, never your key or response bodies.
* **Requests:** model and parameter fields are pointers, so a nil field is not sent. Use `Ptr` to set one, including to zero. Types are checked at compile time and nothing more.
* **Responses** are decoded tolerantly, because the spec has not been confirmed against the live API. Every field is a pointer because a required field can be missing, so check for nil. A field that does not fit its declared type stays nil and keeps its raw value in the model's `Extra` map, and so do unknown fields and nulls. An empty 204 returns nil. A body whose top level is not the declared type returns `ErrDecode`, with the body in `RawBody`.
* **Files:** imports and uploads take a `File`, with an optional name. Error reports, invoices and documents return a `*Download`; close its `Body`.

## Limits

* Model names keep the spec's, which carry the API code, such as `OR11Response200Orders` for an order in OR11's page.
* A `Wait` method sends the client's `WithShopID`, not a per-call one. Use a client for each shop to wait on another shop's job.
* Iterators do not page backward with `previous_page_token`. Call `List` with it instead.
* Only shop API keys have been tested. Mirakl may also accept other tokens; pass your own `Credentials` to try them.

## Design

See the [architecture document](https://github.com/fdhoff/api-sdks/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code. It does not cover Mirakl's spec, which is fetched at build time and not included, and grants no right to the Mirakl name.
