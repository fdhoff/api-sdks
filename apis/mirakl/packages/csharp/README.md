# MiraklSeller

Unofficial .NET client for the Mirakl seller API. Not affiliated with, endorsed by or sponsored by Mirakl SAS.

Mirakl runs marketplaces for operators, such as Best Buy. Each operator has its own Mirakl instance, and this client talks to the seller (shop) API of the one you sell on.

**Alpha.** There is no public sandbox, so it is tested only against a mock built from the public spec, never against a live instance. If you use it for real, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Before you start

* You need your operator's base URL and your own shop API key. Both come from that operator's seller back office. This package ships with neither.
* Features, roles and custom fields vary by operator. An operation your operator has not enabled fails with an error from its instance.
* Only shop API keys are supported.
* Keep the key on a server. Never ship it in a desktop or mobile app.

## How this differs from Mirakl's SDKs

Mirakl's own SDKs are for PHP (`mirakl/sdk-php-shop`, under a proprietary licence) and Java, for its customers. There is none for .NET. This package is generated from Mirakl's published OpenAPI spec, as are its siblings in other languages in [the same repository](https://github.com/fdhoff/api-sdks). Every language passes one shared conformance suite, so retries, paging, jobs, errors and redaction behave the same in each. It adds:

* typed models and async methods for all 117 current operations;
* `ListAll…Async` iterators that walk every page;
* `WaitFor…Async` methods that poll an import or export until it ends;
* `DownloadUrlAsync` for export files, which sends your key only to your operator's instance;
* your key kept out of every exception and log line.

## Install

The package is not on NuGet yet. From a clone of this repository, reference the project:

```sh
dotnet add reference path/to/apis/mirakl/packages/csharp/src/MiraklSeller/MiraklSeller.csproj
```

Requires .NET 8 or later.

## Quickstart

```csharp
using MiraklSeller;

using var client = new MiraklClient("https://your-operator.mirakl.net", "your-shop-api-key");

var shop = await client.Shop.GetAsync();
Console.WriteLine($"{shop.ShopId} {shop.ShopName}");

await foreach (var order in client.Orders.ListAllAsync(orderStateCodes: "SHIPPING"))
{
    Console.WriteLine($"{order.OrderId} {order.OrderState}");
}

try
{
    await client.Offers.GetAsync(1);
}
catch (NotFoundException error)
{
    Console.WriteLine($"{error.Status} {error.RawBody}");
}
```

Your key is read from nowhere and stored nowhere: you pass it in, and the client sends it only to the base URL.

## Shops

A key that covers several shops picks one with `shop_id`. Set it once on the client, and override it on any call:

```csharp
using MiraklSeller;

using var client = new MiraklClient("https://your-operator.mirakl.net", "your-shop-api-key", new MiraklClientOptions { ShopId = 2001 });
var own = await client.Shop.GetAsync();
var other = await client.Shop.GetAsync(shopId: 2002);
Console.WriteLine($"{own.ShopId} {other.ShopId}");
```

## Imports and exports

Imports and exports run in the background. Start one, then wait for it: a wait polls the status every minute by default, since Mirakl allows about one status call a minute, and returns the final status, whether the job completed or failed. A failed import still returns its status, so you can fetch its error report:

```csharp
using System.Text;
using MiraklSeller;

using var client = new MiraklClient("https://your-operator.mirakl.net", "your-shop-api-key");
var csv = new UploadFile("offers.csv", Encoding.UTF8.GetBytes("sku;product-id;product-id-type;price;quantity;state\n"));
var started = await client.Offers.ImportAsync(csv, importMode: "NORMAL");
var status = await client.Offers.WaitForImportAsync(started.ImportId!.Value, interval: TimeSpan.FromMinutes(1), timeout: TimeSpan.FromHours(1));
if (status.HasErrorReport == true)
{
    await using var report = await client.Offers.DownloadImportErrorReportAsync(started.ImportId.Value);
    Console.WriteLine(Encoding.UTF8.GetString(await report.ReadAllBytesAsync()));
}
Console.WriteLine(status.Status);
```

An export's status lists the URLs of its files. Fetch each with `DownloadUrlAsync`. Your key goes only to the base URL's scheme, host and port, and never again once a redirect leaves them, so files stored elsewhere are fetched without it:

```csharp
using MiraklSeller;
using MiraklSeller.Models;

using var client = new MiraklClient("https://your-operator.mirakl.net", "your-shop-api-key");
var started = await client.Offers.ExportAsync(body: new OF52Request { ExportType = "application/json" });
var status = await client.Offers.WaitForExportAsync(started.TrackingId!);
foreach (var url in status.Urls ?? [])
{
    await using var file = await client.DownloadUrlAsync(url);
    Console.WriteLine($"{file.ContentType} {(await file.ReadAllBytesAsync()).Length}");
}
```

| Starts | Waits | Status |
| --- | --- | --- |
| `Offers.ImportAsync` (OF01) | `Offers.WaitForImportAsync` | OF02 |
| `Offers.ImportStockAsync` (STO01) | `Offers.WaitForStockImportAsync` | STO02 |
| `Products.ImportAsync` (P41) | `Products.WaitForImportAsync` | P42 |
| `Offers.ExportAsync` (OF52) | `Offers.WaitForExportAsync` | OF53 |
| `Orders.ExportAsync` (OR13) | `Orders.WaitForExportAsync` | OR14 |
| `Accounting.ExportTransactionsAsync` (TL03) | `Accounting.WaitForTransactionExportAsync` | TL04 |

A wait that reaches its `timeout`, an hour by default, throws `ApiJobTimeoutException`, whose `Result` holds the last status. Cancelling its token stops it between polls. Price imports (PRI01) have no wait, because their status is a list to filter, not one import to fetch: call `Offers.ListPriceImportsAsync`.

## Configuration

`new MiraklClient(baseUrl, apiKey, options)` takes your operator's base URL, your shop API key, sent as the whole `Authorization` header with no scheme, and a `MiraklClientOptions`, whose every property is optional:

| Property | Default | Meaning |
| --- | --- | --- |
| `ShopId` | None | Sent as `shop_id` on every call that leaves its own `shopId` unset |
| `UserAgent` | None | Sent as `User-Agent` when set |
| `Timeout` | 30 seconds | Time allowed for each attempt, including reading the whole response |
| `MaxRetries` | `3` | Retries after the first attempt |
| `RetryBaseDelay` | 0.5 seconds | Base of the exponential backoff |
| `RateLimitWait` | 10 seconds | Wait after a 429 with no usable `Retry-After` |
| `MaxRetryWait` | 60 seconds | Longest `Retry-After` to wait for. A longer one throws `RateLimitedException` at once |
| `Logger` | None | An `ILogger` for methods, URLs, statuses and retries |
| `HttpHandler` | None | An `HttpMessageHandler` to use instead of the network. The client does not dispose it |

To send through an `HttpClient` of your own, such as one from `IHttpClientFactory`, pass it as the fourth argument. The client uses it as it is: it neither changes nor disposes it, and its `Timeout` still applies. Its `DefaultRequestHeaders.ExpectContinue` must not be `true`, because that would let a failed write be resent. A plain `new HttpClient()` follows redirects, unlike the client's own handler; build it over `new SocketsHttpHandler { AllowAutoRedirect = false }` so that `DownloadUrlAsync` decides where your key goes. A handler that retries must skip writes.

A client is safe for concurrent use.

## Behaviour

* **Methods** are grouped by resource: `client.Shop`, `client.Platform`, `client.Offers`, `client.Orders`, `client.Products`, `client.Shipments`, `client.Returns`, `client.Messages`, `client.Accounting`, `client.Promotions`, `client.Picklists` and `client.Users`. Each method's XML doc comment ends with Mirakl's API code, such as OR11, so you can find it in Mirakl's docs. Every method is asynchronous and takes a `CancellationToken`.
* **Not included:** the 11 deprecated operations, and the three placeholder paths for export files, which `DownloadUrlAsync` replaces.
* **Cancellation:** cancelling a call stops it, including any wait before a retry or between polls, and throws `OperationCanceledException`.
* **Pagination:** `List…Async` methods return one page and `ListAll…Async` methods return an `IAsyncEnumerable` over every item. Six operations page by `offset` and `max` up to `total_count`; the others send each page's `next_page_token` back as `page_token`. Iterators start where your own `offset` or `pageToken` says, and keep `shop_id` on every page.
* **Timeouts:** `Timeout` is the time allowed for each attempt. It throws `ApiTimeoutException`.
* **Retries:** 429 on every method, honouring `Retry-After`, otherwise after `RateLimitWait`. A `Retry-After` longer than `MaxRetryWait` throws `RateLimitedException` at once, with the header in `RetryAfter`. 5xx, timeouts and connection failures on GET only, with exponential backoff. Writes are not retried, because a repeat could act twice.
* **Redirects** are never followed by the client's own handler, except by `DownloadUrlAsync`, which drops your key once one leaves the base URL's origin.
* **Errors** derive from `ApiException`. Error responses throw an `HttpException` subclass, such as `NotFoundException` or `PermissionDeniedException`, with `Kind`, `Status`, `RetryAfter` and `RawBody`, the body as text with your key removed. Mirakl's docs define no error body, so the client does not parse one.
* **Logging** holds methods, URLs and statuses, never your key or response bodies, and leaves out the query of a `DownloadUrlAsync` URL, which may hold a signature.
* **Requests:** JSON bodies are a generated model, and a null property is not sent.
* **Responses** are read tolerantly, because the spec has not been confirmed against a live instance. Every property is nullable. A value that does not fit its property, and any field this version does not know, is kept in the model's `Extra` instead of failing the call. An empty 204 returns `null`.
* **Free-form and union values** are `object`, holding a `JsonElement`.
* **Files:** error reports, documents and invoices return a `Download`; dispose it. Uploads take `UploadFile(fileName, bytes)`.

## Limits

* Partner OAuth2 tokens are not built in, and there is no custom credential provider yet.
* Wait methods send only the job's ID and the client's `ShopId`, not a per-call `shopId`.
* Model names follow Mirakl's API codes, such as `OR11Response200Orders`, rather than names of their own.

## Testing

Every test runs against a mock built from the spec. No test uses a real key or calls a Mirakl instance.

## Design

See the [architecture document](https://github.com/fdhoff/api-sdks/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code. It does not cover Mirakl's spec, which is fetched at build time and not included, and grants no right to the Mirakl name.
