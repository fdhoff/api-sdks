// Smoke test of the published package, run by the published packages workflow against the mock, never the live API.
// Restored from NuGet into a clean project. Checks the version the assembly reports, then makes one call.
using System.Reflection;
using EtsySeller;

var expected = Environment.GetEnvironmentVariable("SMOKE_VERSION");
var reported = typeof(EtsyClient).Assembly.GetCustomAttribute<AssemblyInformationalVersionAttribute>()?.InformationalVersion.Split('+')[0];
if (reported != expected)
{
    throw new InvalidOperationException($"EtsySeller reports version {reported}, not {expected}");
}

using var client = new EtsyClient("smoke-synthetic-keystring", "smoke-synthetic-shared-secret", new EtsyClientOptions
{
    BaseUrl = new Uri(Environment.GetEnvironmentVariable("SMOKE_BASE_URL")!),
});
var pong = await client.Application.PingAsync();
if (pong.ApplicationId is null)
{
    throw new InvalidOperationException("The ping has no application_id");
}
Console.WriteLine($"EtsySeller {expected} on {Environment.Version}: pinged application {pong.ApplicationId}");
