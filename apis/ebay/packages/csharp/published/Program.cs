// Smoke test of the published package, run by the published packages workflow against the mock, never the live API.
// Restored from NuGet into a clean project. Checks the version the assembly reports, then makes one call.
using System.Reflection;
using EbaySell;

var expected = Environment.GetEnvironmentVariable("SMOKE_VERSION");
var reported = typeof(EbayClient).Assembly.GetCustomAttribute<AssemblyInformationalVersionAttribute>()?.InformationalVersion.Split('+')[0];
if (reported != expected)
{
    throw new InvalidOperationException($"EbaySell reports version {reported}, not {expected}");
}

var mock = Environment.GetEnvironmentVariable("SMOKE_BASE_URL")!;
using var client = new EbayClient(new EbayClientOptions
{
    AppToken = "smoke-synthetic-app-token",
    Hosts = new Dictionary<string, string> { ["api"] = mock, ["apiz"] = mock, ["apim"] = mock },
    MarketplaceId = "EBAY_US",
});
var tree = await client.Taxonomy.CategoryTrees.GetDefaultIdAsync("EBAY_US");
if (tree.CategoryTreeId is null)
{
    throw new InvalidOperationException("The category tree has no categoryTreeId");
}
Console.WriteLine($"EbaySell {expected} on {Environment.Version}: got category tree {tree.CategoryTreeId}");
