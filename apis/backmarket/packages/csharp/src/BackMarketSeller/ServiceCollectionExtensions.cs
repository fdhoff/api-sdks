using BackMarketSeller;
using BackMarketSeller.Runtime;
using Microsoft.Extensions.Logging;

namespace Microsoft.Extensions.DependencyInjection;

/// <summary>Registers <see cref="BackMarketClient"/> with <c>IHttpClientFactory</c>.</summary>
public static class BackMarketSellerServiceCollectionExtensions
{
    /// <summary>Adds <see cref="BackMarketClient"/> as a typed client of <c>IHttpClientFactory</c>.</summary>
    /// <remarks>
    /// The factory's handler is the one the client builds by default, so writes are still never resent and redirects
    /// are not followed. Header values are redacted from the factory's logs. A handler you add to the returned builder
    /// must not resend a failed write. If <see cref="BackMarketClientOptions.Logger"/> is not set, the client logs
    /// through the registered <see cref="ILoggerFactory"/>.
    /// </remarks>
    /// <param name="services">The service collection.</param>
    /// <param name="token">Your API token, sent verbatim.</param>
    /// <param name="options">Required settings and overrides. <see cref="BackMarketClientOptions.HttpHandler"/> must not be set.</param>
    /// <returns>The builder, to add handlers or change the client further.</returns>
    public static IHttpClientBuilder AddBackMarketSeller(this IServiceCollection services, string token, BackMarketClientOptions options)
    {
        ArgumentNullException.ThrowIfNull(services);
        ArgumentNullException.ThrowIfNull(options);
        if (options.HttpHandler is not null)
        {
            throw new ArgumentException("HttpHandler cannot be used with IHttpClientFactory; configure the returned builder instead", nameof(options));
        }
        BackMarketClient.CreateSettings(token, options, null);
        return services
            .AddHttpClient(nameof(BackMarketClient))
            .ConfigurePrimaryHttpMessageHandler(Transport.CreateHandler)
            .ConfigureHttpClient(http => http.Timeout = Timeout.InfiniteTimeSpan)
            .RedactLoggedHeaders(_ => true)
            .AddTypedClient((http, provider) =>
                new BackMarketClient(token, options, http, provider.GetService<ILoggerFactory>()?.CreateLogger<BackMarketClient>()));
    }
}
