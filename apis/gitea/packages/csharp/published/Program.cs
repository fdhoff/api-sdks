// Smoke test of the published package, run by the published packages workflow against the mock, never a real instance.
// Restored from NuGet into a clean project. Checks the version the assembly reports, then makes one call. The mock
// serves the spec's paths without the /api/v1 the client adds, so the handler removes it.
using System.Reflection;
using GiteaRest;

var expected = Environment.GetEnvironmentVariable("SMOKE_VERSION");
var reported = typeof(GiteaClient).Assembly.GetCustomAttribute<AssemblyInformationalVersionAttribute>()?.InformationalVersion.Split('+')[0];
if (reported != expected)
{
    throw new InvalidOperationException($"GiteaRest reports version {reported}, not {expected}");
}

var mock = Environment.GetEnvironmentVariable("SMOKE_BASE_URL")!;
using var handler = new Unprefixed();
using var client = new GiteaClient(mock, GiteaCredentials.Token("smoke-synthetic-access-token"), new GiteaClientOptions { HttpHandler = handler });
var version = await client.Misc.GetVersionAsync();
Console.WriteLine($"GiteaRest {expected} on {Environment.Version}: the mock reports version {version.VarVersion}");

internal sealed class Unprefixed() : DelegatingHandler(new SocketsHttpHandler { AllowAutoRedirect = false })
{
    protected override Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
    {
        var url = request.RequestUri!;
        if (url.AbsolutePath.StartsWith("/api/v1/", StringComparison.Ordinal))
        {
            request.RequestUri = new Uri(url.GetLeftPart(UriPartial.Authority) + url.AbsolutePath["/api/v1".Length..] + url.Query);
        }
        return base.SendAsync(request, cancellationToken);
    }
}
