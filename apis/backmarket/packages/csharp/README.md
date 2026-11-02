# BackMarketSeller

Unofficial .NET client for the Back Market Seller API. This project is unofficial and is not affiliated with, endorsed by, or supported by Back Market.

**Alpha, and not published yet.** It is tested only against a mock built from the public spec, never against the live API. If you use it for real, please report what you find, working or not, as a GitHub issue. Those reports are what move it past 0.x.

## Install

From a checkout of this repository, until it is published:

```sh
dotnet add reference path/to/apis/backmarket/packages/csharp/src/BackMarketSeller
```

Requires .NET 10 or later.

## Quickstart

```csharp
using BackMarketSeller;

using var client = new BackMarketClient("your-token", new BackMarketClientOptions
{
    UserAgent = "BM-YourCompany-YourIntegration;you@example.com",
    Locale = "fr-fr",
    Region = Region.EU,
});

await foreach (var order in client.Orders.ListAllAsync(pageSize: 50))
{
    Console.WriteLine(order.OrderId);
}

try
{
    await client.Listings.GetAsync("00000000-0000-4000-8000-000000000001");
}
catch (NotFoundException error)
{
    Console.WriteLine($"{error.Status} {error.RequestId}");
}
```

Your token is read from nowhere and stored nowhere: you pass it in, and the client sends it only to the server you selected.

## Configuration

`BackMarketClientOptions`:

| Property | Default | Meaning |
| --- | --- | --- |
| `UserAgent` | Required | `BM-{Company}-{Integration};contact@example.com` |
| `Locale` | Required | Sent as `Accept-Language`, for example `fr-fr` |
| `Region` | None | `Region.EU`, `Region.NA` or `Region.AP`. Set this or `BaseUrl` |
| `Environment` | `Production` | Or `ServerEnvironment.Preprod` |
| `BaseUrl` | None | A server root, for tests against a mock. Your token is sent to it |
| `Timeout` | 30 seconds | Time allowed for each attempt |
| `MaxRetries` | `3` | Retries after the first attempt |
| `RetryBaseDelay` | 0.5 seconds | Base of the exponential backoff |
| `RateLimitWait` | 10 seconds | Wait after a 429 with no usable `Retry-After` |
| `MaxRetryWait` | 60 seconds | Longest `Retry-After` to wait for. A longer one throws `RateLimitedException` at once |
| `Logger` | None | An `ILogger` for methods, URLs, statuses and retries |
| `HttpHandler` | None | An `HttpMessageHandler` to use instead of the network. The client does not dispose it |

## Behaviour

* **Methods** are grouped by resource: `Categories`, `Listings`, `Tasks`, `Orders`, `Buyback`, `Shipping`, `Care` and `Backbox`. Every method is asynchronous and takes a `CancellationToken`.
* **Pagination:** `List…Async` methods return one page and `ListAll…Async` methods return an `IAsyncEnumerable` over all of them, following `next` only for its position, against your configured server.
* **Timeouts:** `Timeout` is the time allowed for each attempt, including reading the whole response. It throws `ApiTimeoutException`. Cancelling your own token throws `OperationCanceledException` instead.
* **Retries:** 429 on every method, honouring `Retry-After` up to `MaxRetryWait`, otherwise after `RateLimitWait`. A longer `Retry-After` throws `RateLimitedException` at once, with the header in `RetryAfter`. 5xx, timeouts and connection failures on GET only, with exponential backoff, because a repeated `POST` could repeat a refund.
* **Errors** derive from `ApiException` and carry `Kind`, `Status`, `Code`, `RequestId` and `RawBody` with your token removed. `WafBlockedException` also has `CfRay`.
* **Logging** holds methods, URLs and statuses, never your token or response bodies.
* **Responses** are read tolerantly, because the spec has not been confirmed against the live API. Every property is nullable. A value that does not fit its property, and any field this version does not know, is kept in the model's `Extra` instead of failing the call, and is written back if you send the model. An empty successful body reads as an empty model.
* **Free-form and union values** are `object`, holding a `JsonElement`. Carriers are plain strings.
* **Uploads** take `UploadFile(fileName, bytes)`.

## Design

See the [architecture document](https://github.com/fdhoff/backmarket-seller-sdk/blob/main/docs/architecture.md) for the runtime contract, testing limits and the decisions behind them.

## Licence

Apache-2.0: see `LICENSE` and `NOTICE`. The licence covers only this project's own code, and grants no right to the Back Market name.
