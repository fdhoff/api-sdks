using EtsySeller.Runtime;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Logging.Abstractions;

namespace EtsySeller;

/// <summary>Settings for <see cref="EtsyClient"/>. Every one is optional.</summary>
public sealed class EtsyClientOptions
{
    /// <summary>An OAuth access token, sent verbatim as a bearer token on calls that need one.</summary>
    public string? AccessToken { get; init; }

    /// <summary>Lets the client replace an expired access token by itself, once per call.</summary>
    public string? RefreshToken { get; init; }

    /// <summary>
    /// Called with every new token pair, from <see cref="EtsyOAuth.ExchangeCodeAsync"/> and every refresh, so you can
    /// store it. The old refresh token stops working. The call that caused the refresh waits for it to return.
    /// </summary>
    public Func<EtsyToken, CancellationToken, Task>? OnToken { get; init; }

    /// <summary>Sent as <c>User-Agent</c>, when set.</summary>
    public string? UserAgent { get; init; }

    /// <summary>The server root. Point it at a mock in tests; your credentials are sent to it.</summary>
    public Uri BaseUrl { get; init; } = new(EtsyClient.DefaultBaseUrl);

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

    /// <summary>Receives methods, URLs, statuses and retries. Never your credentials or response bodies.</summary>
    public ILogger? Logger { get; init; }

    /// <summary>A handler to use instead of the network. The client does not dispose it.</summary>
    /// <remarks>
    /// Writes are sent so that .NET's own handlers never resend one that failed. A custom handler must not resend
    /// one either, or a failed write can be repeated.
    /// </remarks>
    public HttpMessageHandler? HttpHandler { get; init; }
}

/// <summary>Client for the Etsy Open API v3. Every method is asynchronous and takes a cancellation token.</summary>
public sealed class EtsyClient : ClientResources, IDisposable
{
    /// <summary>The production server.</summary>
    public const string DefaultBaseUrl = "https://openapi.etsy.com";

    private static readonly EtsyClientOptions Defaults = new();

    /// <summary>Creates a client.</summary>
    /// <param name="apiKey">Your app's keystring.</param>
    /// <param name="sharedSecret">Your app's shared secret. Both are sent as <c>x-api-key</c> on every call, and never logged.</param>
    /// <param name="options">Tokens and overrides.</param>
    public EtsyClient(string apiKey, string sharedSecret, EtsyClientOptions? options = null)
        : this(new EtsyCredentials(apiKey, sharedSecret, options ?? Defaults), options ?? Defaults, null)
    {
    }

    /// <summary>Creates a client that sends through <paramref name="httpClient"/>, for example one from <c>IHttpClientFactory</c>.</summary>
    /// <param name="apiKey">Your app's keystring.</param>
    /// <param name="sharedSecret">Your app's shared secret.</param>
    /// <param name="options">Tokens and overrides. <see cref="EtsyClientOptions.HttpHandler"/> must not be set.</param>
    /// <param name="httpClient">
    /// Used as it is: the client neither changes nor disposes it, and sends its headers with each request. Its own
    /// <see cref="HttpClient.Timeout"/> still applies, and its handler must not resend a failed write. Its
    /// <c>DefaultRequestHeaders.ExpectContinue</c> must not be <see langword="true"/>. A plain <c>new HttpClient()</c>
    /// follows redirects, unlike the client's own handler; build it over
    /// <c>new SocketsHttpHandler { AllowAutoRedirect = false }</c> to keep your credentials on the server you chose.
    /// </param>
    public EtsyClient(string apiKey, string sharedSecret, EtsyClientOptions options, HttpClient httpClient)
        : this(new EtsyCredentials(apiKey, sharedSecret, options), options, httpClient ?? throw new ArgumentNullException(nameof(httpClient)))
    {
    }

    private EtsyClient(EtsyCredentials credentials, EtsyClientOptions options, HttpClient? httpClient)
        : base(new Transport(
            CreateSettings(credentials, options, httpClient),
            httpClient ?? Transport.OwnClient(options.HttpHandler),
            ownsClient: httpClient is null))
    {
        OAuth = new EtsyOAuth(credentials, Transport);
        credentials.Refresher = cancellationToken => OAuth.RefreshAsync(cancellationToken);
    }

    /// <summary>The OAuth 2 flow: authorization requests, code exchange and refresh.</summary>
    public EtsyOAuth OAuth { get; }

    /// <summary>Releases the connections this client opened. A client passed in is left open.</summary>
    public void Dispose() => Transport.Dispose();

    private static Settings CreateSettings(EtsyCredentials credentials, EtsyClientOptions options, HttpClient? httpClient)
    {
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
        ArgumentNullException.ThrowIfNull(options.BaseUrl);
        var headers = new Dictionary<string, string> { ["Accept"] = "application/json" };
        if (!string.IsNullOrEmpty(options.UserAgent))
        {
            headers["User-Agent"] = options.UserAgent;
        }
        return new Settings
        {
            BaseUrl = options.BaseUrl.ToString().TrimEnd('/'),
            Credentials = credentials,
            Headers = headers,
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
