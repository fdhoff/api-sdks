using GiteaRest.Runtime;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Logging.Abstractions;

namespace GiteaRest;

/// <summary>Settings for <see cref="GiteaClient"/>. Every one is optional.</summary>
public sealed class GiteaClientOptions
{
    /// <summary>A user to act as, sent as <c>Sudo</c> on every call. Needs an admin's credentials.</summary>
    public string? Sudo { get; init; }

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

    /// <summary>Receives methods, URLs, statuses and retries. Never your credentials or response bodies.</summary>
    public ILogger? Logger { get; init; }

    /// <summary>A handler to use instead of the network. The client does not dispose it.</summary>
    /// <remarks>
    /// Writes are sent so that .NET's own handlers never resend one that failed. A custom handler must not resend
    /// one either, or a failed write can be repeated. It must not follow redirects either, so that your credentials
    /// stay on your instance.
    /// </remarks>
    public HttpMessageHandler? HttpHandler { get; init; }
}

/// <summary>
/// Client for a Gitea instance's API. Unofficial. Not affiliated with, endorsed by or sponsored by the Gitea project or
/// Gitea Limited. Every method is asynchronous and takes a cancellation token. A client is safe for concurrent use.
/// </summary>
public sealed class GiteaClient : ClientResources, IDisposable
{
    private const string ApiPath = "/api/v1";

    private static readonly GiteaClientOptions Defaults = new();

    /// <summary>Creates a client.</summary>
    /// <param name="baseUrl">
    /// Your Gitea instance's URL, such as <c>https://gitea.example.com</c>, or <c>https://example.com/git</c> for an
    /// instance under a sub-path. There is no default. The client adds <c>/api/v1</c>, so leave it out. Your
    /// credentials are sent to it.
    /// </param>
    /// <param name="credentials">An access token, or a username and password. See <see cref="GiteaCredentials"/>.</param>
    /// <param name="options">Optional settings.</param>
    /// <exception cref="ArgumentException">
    /// The base URL is not an http or https URL, or already ends in <c>/api/v1</c>, or <see cref="GiteaClientOptions.Sudo"/>
    /// is empty or not a header value.
    /// </exception>
    public GiteaClient(string baseUrl, GiteaCredentials credentials, GiteaClientOptions? options = null)
        : this(null, baseUrl, credentials, options ?? Defaults)
    {
    }

    /// <summary>Creates a client that sends through <paramref name="httpClient"/>, for example one from <c>IHttpClientFactory</c>.</summary>
    /// <param name="baseUrl">Your Gitea instance's URL, without <c>/api/v1</c>.</param>
    /// <param name="credentials">An access token, or a username and password.</param>
    /// <param name="options">Optional settings. <see cref="GiteaClientOptions.HttpHandler"/> must not be set.</param>
    /// <param name="httpClient">
    /// Used as it is: the client neither changes nor disposes it, and sends its headers with each request. Its own
    /// <see cref="HttpClient.Timeout"/> still applies, and its handler must not resend a failed write. Its
    /// <c>DefaultRequestHeaders.ExpectContinue</c> must not be <see langword="true"/>. A plain <c>new HttpClient()</c>
    /// follows redirects, unlike the client's own handler; build it over
    /// <c>new SocketsHttpHandler { AllowAutoRedirect = false }</c> to keep your credentials on your instance.
    /// </param>
    public GiteaClient(string baseUrl, GiteaCredentials credentials, GiteaClientOptions options, HttpClient httpClient)
        : this(httpClient ?? throw new ArgumentNullException(nameof(httpClient)), baseUrl, credentials, options)
    {
    }

    private GiteaClient(HttpClient? httpClient, string baseUrl, GiteaCredentials credentials, GiteaClientOptions options)
        : base(new Transport(
            CreateSettings(baseUrl, credentials, options, httpClient),
            httpClient ?? Transport.OwnClient(options.HttpHandler),
            ownsClient: httpClient is null))
    {
    }

    /// <summary>Releases the connections this client opened. A client passed in is left open.</summary>
    public void Dispose() => Transport.Dispose();

    // TODO: OAuth2 bearer tokens and a custom credential provider, if users ask.
    private static Settings CreateSettings(string baseUrl, GiteaCredentials credentials, GiteaClientOptions options, HttpClient? httpClient)
    {
        ArgumentNullException.ThrowIfNull(credentials);
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
        var auth = new Dictionary<string, string> { ["Authorization"] = credentials.Authorization };
        if (credentials.Otp is { } otp)
        {
            auth["X-GITEA-OTP"] = otp;
        }
        if (options.Sudo is { } sudo)
        {
            if (sudo.Length == 0 || sudo.Any(char.IsControl))
            {
                throw new ArgumentException("Sudo must be a non-empty username", nameof(options));
            }
            auth["Sudo"] = sudo;
        }
        var headers = new Dictionary<string, string> { ["Accept"] = "application/json" };
        if (!string.IsNullOrEmpty(options.UserAgent))
        {
            headers["User-Agent"] = options.UserAgent;
        }
        return new Settings
        {
            BaseUrl = ApiUrl(baseUrl),
            Credentials = new StaticCredentials(auth, credentials.Secrets),
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

    private static string ApiUrl(string baseUrl)
    {
        if (string.IsNullOrEmpty(baseUrl))
        {
            throw new ArgumentException("The base URL is required: your Gitea instance's URL, such as https://gitea.example.com", nameof(baseUrl));
        }
        if (!Uri.TryCreate(baseUrl, UriKind.Absolute, out var parsed) || parsed.Scheme is not ("http" or "https") || parsed.Host.Length == 0)
        {
            throw new ArgumentException("The base URL must be an absolute http or https URL", nameof(baseUrl));
        }
        var root = baseUrl.TrimEnd('/');
        if (root.EndsWith(ApiPath, StringComparison.OrdinalIgnoreCase))
        {
            throw new ArgumentException($"The base URL is the instance's; leave out {ApiPath}, which the client adds", nameof(baseUrl));
        }
        return root + ApiPath;
    }
}
