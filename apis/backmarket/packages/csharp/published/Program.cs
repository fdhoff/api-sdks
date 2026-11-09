// Smoke test of the published package, run by the published packages workflow against the mock, never the live API.
// Restored from NuGet into a clean project. Checks the version the assembly reports, then makes one call.
using System.Reflection;
using BackMarketSeller;

var expected = Environment.GetEnvironmentVariable("SMOKE_VERSION");
var reported = typeof(BackMarketClient).Assembly.GetCustomAttribute<AssemblyInformationalVersionAttribute>()?.InformationalVersion.Split('+')[0];
if (reported != expected)
{
    throw new InvalidOperationException($"BackMarketSeller reports version {reported}, not {expected}");
}

using var client = new BackMarketClient("smoke-synthetic-token", new BackMarketClientOptions
{
    UserAgent = "BM-Example-Smoke;smoke@example.com",
    Locale = "en-us",
    BaseUrl = new Uri(Environment.GetEnvironmentVariable("SMOKE_BASE_URL")!),
});
var order = await client.Orders.GetAsync(1);
if (order.OrderId is null)
{
    throw new InvalidOperationException("The order has no order_id");
}
Console.WriteLine($"BackMarketSeller {expected} on {Environment.Version}: got order {order.OrderId}");
