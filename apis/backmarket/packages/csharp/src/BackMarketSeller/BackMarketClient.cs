using BackMarketSeller.Runtime;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Logging.Abstractions;

namespace BackMarketSeller;

/// <summary>A marketplace region.</summary>
public enum Region
{
    AP,
    EU,
    NA,
}

/// <summary>Production or preprod servers.</summary>
public enum ServerEnvironment
{
    Production,
    Preprod,
}

/// <summary>Settings for <see cref="BackMarketClient"/>.</summary>
public sealed class BackMarketClientOptions
{
    /// <summary>Required, in the form <c>BM-{Company}-{Integration};contact@example.com</c>.</summary>
    public required string UserAgent { get; init; }

    /// <summary>Sent as <c>Accept-Language</c> on every call, for example <c>fr-fr</c>.</summary>
    public required string Locale { get; init; }

    /// <summary>The marketplace region. Set this or <see cref="BaseUrl"/>.</summary>
    public Region? Region { get; init; }

    /// <summary>Production or preprod.</summary>
    public ServerEnvironment Environment { get; init; } = ServerEnvironment.Production;

    /// <summary>A server root, for tests against a mock. Your token is sent to it.</summary>
    public Uri? BaseUrl { get; init; }

    /// <summary>Time allowed for each attempt, including reading the whole response.</summary>
    public TimeSpan Timeout { get; init; } = TimeSpan.FromSeconds(30);

    /// <summary>Retries after the first attempt.</summary>
    public int MaxRetries { get; init; } = 3;

    /// <summary>Base of the exponential backoff.</summary>
    public TimeSpan RetryBaseDelay { get; init; } = TimeSpan.FromSeconds(0.5);

    /// <summary>Wait after a 429 with no usable <c>Retry-After</c>.</summary>
    public TimeSpan RateLimitWait { get; init; } = TimeSpan.FromSeconds(10);

    /// <summary>The longest <c>Retry-After</c> to wait for. A longer one throws <see cref="RateLimitedException"/> at once.</summary>
    public TimeSpan MaxRetryWait { get; init; } = TimeSpan.FromSeconds(60);

    /// <summary>Receives methods, URLs, statuses and retries. Never your token or response bodies.</summary>
    public ILogger? Logger { get; init; }

    /// <summary>A handler to use instead of the network. The client does not dispose it.</summary>
    /// <remarks>
    /// Writes are sent so that .NET's own handlers never resend one that failed. A custom handler must not resend
    /// one either, or a failed write can be repeated.
    /// </remarks>
    public HttpMessageHandler? HttpHandler { get; init; }
}

/// <summary>Client for the Seller API. Every method is asynchronous and takes a cancellation token.</summary>
public sealed class BackMarketClient : ClientResources, IDisposable
{
    private static readonly Dictionary<(Region, ServerEnvironment), string> Servers = new()
    {
        [(Region.AP, ServerEnvironment.Production)] = "https://www.backmarket.co.jp",
        [(Region.AP, ServerEnvironment.Preprod)] = "https://preprod.backmarket.co.jp",
        [(Region.EU, ServerEnvironment.Production)] = "https://www.backmarket.fr",
        [(Region.EU, ServerEnvironment.Preprod)] = "https://preprod.backmarket.fr",
        [(Region.NA, ServerEnvironment.Production)] = "https://www.backmarket.com",
        [(Region.NA, ServerEnvironment.Preprod)] = "https://preprod.backmarket.com",
    };

    /// <summary>Creates a client.</summary>
    /// <param name="token">Your API token, sent verbatim. It is kept only by this client and never logged.</param>
    /// <param name="options">Required settings and overrides.</param>
    public BackMarketClient(string token, BackMarketClientOptions options)
        : base(new Transport(CreateSettings(token, options, null), Transport.OwnClient(options.HttpHandler), ownsClient: true))
    {
    }

    /// <summary>Creates a client that sends through <paramref name="httpClient"/>, for example one from <c>IHttpClientFactory</c>.</summary>
    /// <param name="token">Your API token, sent verbatim. It is kept only by this client and never logged.</param>
    /// <param name="options">Required settings and overrides. <see cref="BackMarketClientOptions.HttpHandler"/> must not be set.</param>
    /// <param name="httpClient">
    /// Used as it is: the client neither changes nor disposes it, and sends its headers with each request. Its own
    /// <see cref="HttpClient.Timeout"/> still applies, and its handler must not resend a failed write. Its
    /// <c>DefaultRequestHeaders.ExpectContinue</c> must not be <see langword="true"/>. A plain <c>new HttpClient()</c>
    /// follows redirects, unlike the client's own handler; build it over
    /// <c>new SocketsHttpHandler { AllowAutoRedirect = false }</c> to keep every call on the server you selected.
    /// </param>
    public BackMarketClient(string token, BackMarketClientOptions options, HttpClient httpClient)
        : this(token, options, httpClient, null)
    {
    }

    internal BackMarketClient(string token, BackMarketClientOptions options, HttpClient httpClient, ILogger? fallbackLogger)
        : base(new Transport(CreateSettings(token, options, fallbackLogger, httpClient), httpClient ?? throw new ArgumentNullException(nameof(httpClient)), ownsClient: false))
    {
    }

    /// <summary>Releases the connections this client opened. A client passed in is left open.</summary>
    public void Dispose() => Transport.Dispose();

    internal static Settings CreateSettings(string token, BackMarketClientOptions options, ILogger? fallbackLogger, HttpClient? httpClient = null)
    {
        ArgumentNullException.ThrowIfNull(options);
        if (httpClient is not null && options.HttpHandler is not null)
        {
            throw new ArgumentException("Set HttpHandler or pass an HttpClient, not both", nameof(options));
        }
        if (httpClient?.DefaultRequestHeaders.ExpectContinue == true)
        {
            throw new ArgumentException("DefaultRequestHeaders.ExpectContinue must not be true: it overrides the client's own setting and lets a failed write be resent", nameof(httpClient));
        }
        if (string.IsNullOrEmpty(token) || token.Any(char.IsControl))
        {
            throw new ArgumentException("A token is required, and must not hold control characters", nameof(token));
        }
        if (string.IsNullOrEmpty(options.UserAgent))
        {
            throw new ArgumentException("UserAgent is required; the API may refuse a request without it", nameof(options));
        }
        if (options.Region is null == options.BaseUrl is null)
        {
            throw new ArgumentException("Set exactly one of Region and BaseUrl", nameof(options));
        }
        if (options.Timeout <= TimeSpan.Zero)
        {
            throw new ArgumentOutOfRangeException(nameof(options), "Timeout must be positive");
        }
        var url = options.BaseUrl?.ToString() ?? Servers[(options.Region!.Value, options.Environment)];
        return new Settings
        {
            BaseUrl = url.TrimEnd('/'),
            Secret = token,
            Headers = new Dictionary<string, string>
            {
                ["Authorization"] = $"Basic {token}",
                ["User-Agent"] = options.UserAgent,
                ["Accept"] = "application/json",
                ["Accept-Language"] = options.Locale,
            },
            ToError = Errors.ToException,
            Logger = options.Logger ?? fallbackLogger ?? NullLogger.Instance,
            Timeout = options.Timeout,
            MaxRetries = options.MaxRetries,
            RetryBaseDelay = options.RetryBaseDelay,
            RateLimitWait = options.RateLimitWait,
            MaxRetryWait = options.MaxRetryWait,
        };
    }
}
