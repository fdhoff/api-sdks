// Smoke test of the published package, run by the published packages workflow against the mock, never the live API.
// Restored from NuGet into a clean project. Checks the version the assembly reports, then makes one call.
using System.Reflection;
using MercuryBanking;

var expected = Environment.GetEnvironmentVariable("SMOKE_VERSION");
var reported = typeof(MercuryClient).Assembly.GetCustomAttribute<AssemblyInformationalVersionAttribute>()?.InformationalVersion.Split('+')[0];
if (reported != expected)
{
    throw new InvalidOperationException($"MercuryBanking reports version {reported}, not {expected}");
}

var mock = Environment.GetEnvironmentVariable("SMOKE_BASE_URL")!;
using var client = new MercuryClient("secret-token:smoke-synthetic-token", new MercuryClientOptions
{
    Hosts = new Dictionary<string, string> { ["api"] = mock, ["vault"] = mock },
});
var page = await client.Accounts.ListAsync();
if (page.Accounts is null)
{
    throw new InvalidOperationException("The page has no accounts");
}
Console.WriteLine($"MercuryBanking {expected} on {Environment.Version}: listed {page.Accounts.Count} accounts");
