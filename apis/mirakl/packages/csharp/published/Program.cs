// Smoke test of the published package, run by the published packages workflow against the mock, never a live instance.
// Restored from NuGet into a clean project. Checks the version the assembly reports, then makes one call.
using System.Reflection;
using MiraklSeller;

var expected = Environment.GetEnvironmentVariable("SMOKE_VERSION");
var reported = typeof(MiraklClient).Assembly.GetCustomAttribute<AssemblyInformationalVersionAttribute>()?.InformationalVersion.Split('+')[0];
if (reported != expected)
{
    throw new InvalidOperationException($"MiraklSeller reports version {reported}, not {expected}");
}

var mock = Environment.GetEnvironmentVariable("SMOKE_BASE_URL")!;
using var client = new MiraklClient(mock, "smoke-synthetic-shop-key");
var shop = await client.Shop.GetAsync();
Console.WriteLine($"MiraklSeller {expected} on {Environment.Version}: read shop {shop.ShopId}");
