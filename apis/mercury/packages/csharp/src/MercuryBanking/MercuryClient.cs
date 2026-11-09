using MercuryBanking.Runtime;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Logging.Abstractions;

namespace MercuryBanking;

/// <summary>Settings for <see cref="MercuryClient"/>. Every one is optional.</summary>
public sealed class MercuryClientOptions
{
    /// <summary>
    /// <see cref="MercuryClient.Production"/>, the default, or <see cref="MercuryClient.Sandbox"/>. Picks the hosts. A
    /// sandbox token works only in the sandbox.
    /// </summary>
    public string Environment { get; init; } = MercuryClient.Production;

    /// <summary>
    /// Your own base URL for each of the <c>api</c> and <c>vault</c> hosts, such as a mock's, instead of the
    /// environment's. Your token is sent to them.
    /// </summary>
    public IReadOnlyDictionary<string, string>? Hosts { get; init; }

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

    /// <summary>Receives methods, URLs, statuses and retries. Never your token or response bodies.</summary>
    public ILogger? Logger { get; init; }

    /// <summary>A handler to use instead of the network. The client does not dispose it.</summary>
    /// <remarks>
    /// Writes are sent so that .NET's own handlers never resend one that failed. A custom handler must not resend
    /// one either, or a failed write can be repeated.
    /// </remarks>
    public HttpMessageHandler? HttpHandler { get; init; }
}

/// <summary>
/// Client for the Mercury API. Every method is asynchronous and takes a cancellation token. A client is safe for
/// concurrent use.
/// </summary>
public sealed class MercuryClient : ClientResources, IDisposable
{
    /// <summary>The production environment, the default.</summary>
    public const string Production = "production";

    /// <summary>The sandbox environment, which holds only dummy data.</summary>
    public const string Sandbox = "sandbox";

    // Mercury documents no sandbox host for card details, so those calls go to the sandbox's own API host.
    private static readonly Dictionary<string, IReadOnlyDictionary<string, string>> HostsByEnvironment = new()
    {
        [Production] = new Dictionary<string, string> { ["api"] = "https://api.mercury.com/api/v1", ["vault"] = "https://vault-api.mercury.com/api/v1" },
        [Sandbox] = new Dictionary<string, string> { ["api"] = "https://api-sandbox.mercury.com/api/v1", ["vault"] = "https://api-sandbox.mercury.com/api/v1" },
    };

    private static readonly MercuryClientOptions Defaults = new();

    /// <summary>Creates a client.</summary>
    /// <param name="token">
    /// Your API token, sent verbatim as a bearer token; the <c>secret-token:</c> prefix is part of it. The client keeps
    /// it only in memory and never logs it.
    /// </param>
    /// <param name="options">The environment and overrides.</param>
    /// <exception cref="ArgumentException">The token is empty, or the options name an unknown environment or host.</exception>
    public MercuryClient(string token, MercuryClientOptions? options = null)
        : this(null, token, options ?? Defaults)
    {
    }

    /// <summary>Creates a client that sends through <paramref name="httpClient"/>, for example one from <c>IHttpClientFactory</c>.</summary>
    /// <param name="token">Your API token.</param>
    /// <param name="options">The environment and overrides. <see cref="MercuryClientOptions.HttpHandler"/> must not be set.</param>
    /// <param name="httpClient">
    /// Used as it is: the client neither changes nor disposes it, and sends its headers with each request. Its own
    /// <see cref="HttpClient.Timeout"/> still applies, and its handler must not resend a failed write. Its
    /// <c>DefaultRequestHeaders.ExpectContinue</c> must not be <see langword="true"/>. A plain <c>new HttpClient()</c>
    /// follows redirects, unlike the client's own handler; build it over
    /// <c>new SocketsHttpHandler { AllowAutoRedirect = false }</c> to keep your token on the hosts you chose.
    /// </param>
    public MercuryClient(string token, MercuryClientOptions options, HttpClient httpClient)
        : this(httpClient ?? throw new ArgumentNullException(nameof(httpClient)), token, options)
    {
    }

    private MercuryClient(HttpClient? httpClient, string token, MercuryClientOptions options)
        : base(new Transport(
            CreateSettings(token, options, httpClient),
            httpClient ?? Transport.OwnClient(options.HttpHandler),
            ownsClient: httpClient is null))
    {
    }

    /// <summary>
    /// The base URL of each host the API uses, by environment. <c>vault</c> serves only
    /// <see cref="Api.CardsResource.RevealAsync"/>. The result is a copy.
    /// </summary>
    public static IReadOnlyDictionary<string, IReadOnlyDictionary<string, string>> Environments =>
        HostsByEnvironment.ToDictionary(pair => pair.Key, pair => (IReadOnlyDictionary<string, string>)new Dictionary<string, string>(pair.Value));

    /// <summary>Releases the connections this client opened. A client passed in is left open.</summary>
    public void Dispose() => Transport.Dispose();

    private static Settings CreateSettings(string token, MercuryClientOptions options, HttpClient? httpClient)
    {
        ArgumentException.ThrowIfNullOrEmpty(token);
        ArgumentNullException.ThrowIfNull(options);
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
        var hosts = HostMap.Select(HostsByEnvironment, options.Environment, options.Hosts);
        var headers = new Dictionary<string, string> { ["Accept"] = "application/json" };
        if (!string.IsNullOrEmpty(options.UserAgent))
        {
            headers["User-Agent"] = options.UserAgent;
        }
        return new Settings
        {
            BaseUrl = hosts["api"],
            Hosts = hosts,
            Credentials = new StaticCredentials(new Dictionary<string, string> { ["Authorization"] = $"Bearer {token}" }, [token]),
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
