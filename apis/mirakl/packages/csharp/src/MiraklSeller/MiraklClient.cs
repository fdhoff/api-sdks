using MiraklSeller.Runtime;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Logging.Abstractions;

namespace MiraklSeller;

/// <summary>Settings for <see cref="MiraklClient"/>. Every one is optional.</summary>
public sealed class MiraklClientOptions
{
    /// <summary>
    /// The shop to act for, when your key covers several. Sent as <c>shop_id</c> on every call that leaves its own
    /// <c>shopId</c> unset.
    /// </summary>
    public long? ShopId { get; init; }

    /// <summary>Sent as <c>User-Agent</c>, when set.</summary>
    public string? UserAgent { get; init; }

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

    /// <summary>Receives methods, URLs, statuses and retries. Never your key or response bodies.</summary>
    public ILogger? Logger { get; init; }

    /// <summary>A handler to use instead of the network. The client does not dispose it.</summary>
    /// <remarks>
    /// Writes are sent so that .NET's own handlers never resend one that failed. A custom handler must not resend
    /// one either, or a failed write can be repeated. It must not follow redirects either, so that
    /// <see cref="MiraklClient.DownloadUrlAsync"/> decides where your key goes.
    /// </remarks>
    public HttpMessageHandler? HttpHandler { get; init; }
}

/// <summary>
/// Client for a Mirakl operator's seller API. Unofficial. Not affiliated with, endorsed by or sponsored by Mirakl SAS.
/// Every method is asynchronous and takes a cancellation token. A client is safe for concurrent use.
/// </summary>
public sealed class MiraklClient : ClientResources, IDisposable
{
    // What the credentials see as a URL download's requirements: the shop API key, as on every operation.
    private static readonly Scheme[][] DownloadSecurity = [[new("Shop-API-Key", [])]];

    private static readonly MiraklClientOptions Defaults = new();

    /// <summary>Creates a client.</summary>
    /// <param name="baseUrl">
    /// Your operator's Mirakl instance, such as <c>https://your-operator.mirakl.net</c>, from its seller back office.
    /// Every operator runs its own, so there is no default. Your key is sent to it.
    /// </param>
    /// <param name="apiKey">
    /// Your shop API key, sent as the whole <c>Authorization</c> header with no scheme. The client keeps it only in
    /// memory and never logs it.
    /// </param>
    /// <param name="options">Optional settings.</param>
    /// <exception cref="ArgumentException">The base URL is not an http or https URL, or the key is empty.</exception>
    public MiraklClient(string baseUrl, string apiKey, MiraklClientOptions? options = null)
        : this(null, baseUrl, apiKey, options ?? Defaults)
    {
    }

    /// <summary>Creates a client that sends through <paramref name="httpClient"/>, for example one from <c>IHttpClientFactory</c>.</summary>
    /// <param name="baseUrl">Your operator's Mirakl instance.</param>
    /// <param name="apiKey">Your shop API key.</param>
    /// <param name="options">Optional settings. <see cref="MiraklClientOptions.HttpHandler"/> must not be set.</param>
    /// <param name="httpClient">
    /// Used as it is: the client neither changes nor disposes it, and sends its headers with each request. Its own
    /// <see cref="HttpClient.Timeout"/> still applies, and its handler must not resend a failed write. Its
    /// <c>DefaultRequestHeaders.ExpectContinue</c> must not be <see langword="true"/>. A plain <c>new HttpClient()</c>
    /// follows redirects, unlike the client's own handler; build it over
    /// <c>new SocketsHttpHandler { AllowAutoRedirect = false }</c> to keep your key on your operator's instance.
    /// </param>
    public MiraklClient(string baseUrl, string apiKey, MiraklClientOptions options, HttpClient httpClient)
        : this(httpClient ?? throw new ArgumentNullException(nameof(httpClient)), baseUrl, apiKey, options)
    {
    }

    private MiraklClient(HttpClient? httpClient, string baseUrl, string apiKey, MiraklClientOptions options)
        : base(new Transport(
            CreateSettings(baseUrl, apiKey, options, httpClient),
            httpClient ?? Transport.OwnClient(options.HttpHandler),
            ownsClient: httpClient is null))
    {
    }

    /// <summary>
    /// Downloads a file from a URL an export status returned, such as the <c>Urls</c> of
    /// <see cref="Api.OffersResource.WaitForExportAsync"/>'s result. Your key goes only to the base URL's scheme, host
    /// and port, and never again once a redirect leaves them. Dispose the download.
    /// </summary>
    /// <exception cref="ArgumentException">The URL is not an absolute http or https URL. Nothing is sent.</exception>
    public Task<Download> DownloadUrlAsync(string url, CancellationToken cancellationToken = default) =>
        Transport.DownloadUrlAsync(url, DownloadSecurity, cancellationToken);

    /// <summary>Releases the connections this client opened. A client passed in is left open.</summary>
    public void Dispose() => Transport.Dispose();

    // TODO: partner OAuth2 client-credentials tokens, if users ask.
    private static Settings CreateSettings(string baseUrl, string apiKey, MiraklClientOptions options, HttpClient? httpClient)
    {
        ArgumentException.ThrowIfNullOrEmpty(baseUrl);
        ArgumentException.ThrowIfNullOrEmpty(apiKey);
        ArgumentNullException.ThrowIfNull(options);
        if (!Uri.TryCreate(baseUrl, UriKind.Absolute, out var parsed) || parsed.Scheme is not ("http" or "https") || parsed.Host.Length == 0)
        {
            throw new ArgumentException("The base URL must be an http or https URL: your operator's Mirakl instance", nameof(baseUrl));
        }
        if (httpClient is not null && options.HttpHandler is not null)
        {
            throw new ArgumentException("Set HttpHandler or pass an HttpClient, not both", nameof(options));
        }
        if (httpClient?.DefaultRequestHeaders.ExpectContinue == true)
        {
            throw new ArgumentException("DefaultRequestHeaders.ExpectContinue must not be true: it overrides the client's own setting and lets a failed write be resent", nameof(httpClient));
        }
        if (options.Timeout <= TimeSpan.Zero)
        {
            throw new ArgumentOutOfRangeException(nameof(options), "Timeout must be positive");
        }
        var headers = new Dictionary<string, string> { ["Accept"] = "application/json" };
        if (!string.IsNullOrEmpty(options.UserAgent))
        {
            headers["User-Agent"] = options.UserAgent;
        }
        var queryDefaults = new Dictionary<string, string>();
        if (options.ShopId is { } shopId)
        {
            queryDefaults["shop_id"] = shopId.ToString(System.Globalization.CultureInfo.InvariantCulture);
        }
        return new Settings
        {
            BaseUrl = baseUrl.TrimEnd('/'),
            Credentials = new StaticCredentials(new Dictionary<string, string> { ["Authorization"] = apiKey }, [apiKey]),
            Headers = headers,
            QueryDefaults = queryDefaults,
            ToError = Errors.ToException,
            Logger = options.Logger ?? NullLogger.Instance,
            Timeout = options.Timeout,
            MaxRetries = options.MaxRetries,
            RetryBaseDelay = options.RetryBaseDelay,
            RateLimitWait = options.RateLimitWait,
            MaxRetryWait = options.MaxRetryWait,
        };
    }
}
