using EbaySell.Runtime;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Logging.Abstractions;

namespace EbaySell;

/// <summary>Settings for <see cref="EbayClient"/>. Pass <see cref="ClientId"/> and <see cref="ClientSecret"/>, a token, or both.</summary>
public sealed class EbayClientOptions
{
    /// <summary>Your keyset's App ID. With <see cref="ClientSecret"/>, the client mints application tokens itself and can exchange and refresh user tokens.</summary>
    public string? ClientId { get; init; }

    /// <summary>Your keyset's Cert ID. It is sent, with <see cref="ClientId"/>, only to the token endpoint, and never logged.</summary>
    public string? ClientSecret { get; init; }

    /// <summary>Your app's redirect URL name, which eBay takes as <c>redirect_uri</c> in the authorization code grant.</summary>
    public string? RuName { get; init; }

    /// <summary>An application token to use instead of minting one.</summary>
    public string? AppToken { get; init; }

    /// <summary>A user access token, sent on operations that act for a seller.</summary>
    public string? UserToken { get; init; }

    /// <summary>Lets the client replace an expired user token by itself, once per call.</summary>
    public string? RefreshToken { get; init; }

    /// <summary>
    /// Called with every new user token, from <see cref="EbayOAuth.ExchangeCodeAsync"/> and every refresh, so you can
    /// store it. It runs while the client holds its token locks, so it must not call the client: awaiting
    /// <see cref="EbayOAuth.RefreshAsync"/> from it waits forever.
    /// </summary>
    public Func<EbayToken, CancellationToken, Task>? OnToken { get; init; }

    /// <summary>The scopes of minted application tokens, at least one.</summary>
    public IReadOnlyList<string> AppScopes { get; init; } = [EbayOAuth.ApiScope];

    /// <summary>The scopes to ask for when refreshing a user token. eBay keeps the original grant's when this is empty.</summary>
    public IReadOnlyList<string> UserScopes { get; init; } = [];

    /// <summary><see cref="EbayClient.Production"/> or <see cref="EbayClient.Sandbox"/>. Picks the API hosts and the authorization URL.</summary>
    public string Environment { get; init; } = EbayClient.Production;

    /// <summary>
    /// Your own base URL for each of the <c>api</c>, <c>apiz</c> and <c>apim</c> hosts, such as a mock's, instead of the
    /// environment's. Your credentials are sent to them.
    /// </summary>
    public IReadOnlyDictionary<string, string>? Hosts { get; init; }

    /// <summary>Sent as <c>X-EBAY-C-MARKETPLACE-ID</c> on operations that take it, unless a call passes its own.</summary>
    public string? MarketplaceId { get; init; }

    /// <summary>Sent as <c>Content-Language</c> on operations that take it, unless a call passes its own.</summary>
    public string? ContentLanguage { get; init; }

    /// <summary>Signs every request, as eBay requires of EU and UK sellers on some calls.</summary>
    public EbaySigningKey? SigningKey { get; init; }

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
    /// one either, or a failed write can be repeated.
    /// </remarks>
    public HttpMessageHandler? HttpHandler { get; init; }

    /// <summary>Tells the time when application tokens expire. Tests replace it.</summary>
    internal TimeProvider Clock { get; init; } = TimeProvider.System;
}

/// <summary>
/// Client for eBay's Sell, Commerce and Developer REST APIs. Each API is a property holding that API's resources, and
/// every method is asynchronous and takes a cancellation token. A client is safe for concurrent use.
/// </summary>
public sealed class EbayClient : IDisposable
{
    /// <summary>The production environment, the default.</summary>
    public const string Production = "production";

    /// <summary>The sandbox environment.</summary>
    public const string Sandbox = "sandbox";

    private static readonly Dictionary<string, IReadOnlyDictionary<string, string>> Hosts = new()
    {
        [Production] = new Dictionary<string, string> { ["api"] = "https://api.ebay.com", ["apiz"] = "https://apiz.ebay.com", ["apim"] = "https://apim.ebay.com" },
        [Sandbox] = new Dictionary<string, string> { ["api"] = "https://api.sandbox.ebay.com", ["apiz"] = "https://apiz.sandbox.ebay.com", ["apim"] = "https://apim.sandbox.ebay.com" },
    };

    private readonly Transport transport;
    private readonly EbayCredentials credentials;

    /// <summary>Creates a client. It keeps every credential only in memory.</summary>
    /// <exception cref="ArgumentException">The options name no credentials, half a keyset, or an unknown environment or host.</exception>
    public EbayClient(EbayClientOptions options)
        : this(null, options)
    {
    }

    /// <summary>Creates a client that sends through <paramref name="httpClient"/>, for example one from <c>IHttpClientFactory</c>.</summary>
    /// <param name="options">Credentials and overrides. <see cref="EbayClientOptions.HttpHandler"/> must not be set.</param>
    /// <param name="httpClient">
    /// Used as it is: the client neither changes nor disposes it, and sends its headers with each request. Its own
    /// <see cref="HttpClient.Timeout"/> still applies, and its handler must not resend a failed write. Its
    /// <c>DefaultRequestHeaders.ExpectContinue</c> must not be <see langword="true"/>. A plain <c>new HttpClient()</c>
    /// follows redirects, unlike the client's own handler; build it over
    /// <c>new SocketsHttpHandler { AllowAutoRedirect = false }</c> to keep your credentials on the hosts you chose.
    /// </param>
    public EbayClient(EbayClientOptions options, HttpClient httpClient)
        : this(httpClient ?? throw new ArgumentNullException(nameof(httpClient)), options)
    {
    }

    private EbayClient(HttpClient? httpClient, EbayClientOptions options)
    {
        ArgumentNullException.ThrowIfNull(options);
        var settings = CreateSettings(options, httpClient, out credentials);
        transport = new Transport(settings, httpClient ?? Transport.OwnClient(options.HttpHandler), ownsClient: httpClient is null);
        OAuth = new EbayOAuth(credentials, transport, options);
        credentials.OAuth = OAuth;
        Account = new(transport);
        AccountV2 = new(transport);
        Analytics = new(transport);
        Feed = new(transport);
        Finances = new(transport);
        Fulfillment = new(transport);
        Inventory = new(transport);
        Marketing = new(transport);
        Metadata = new(transport);
        Negotiation = new(transport);
        Recommendation = new(transport);
        Stores = new(transport);
        PostOrder = new(transport);
        Feedback = new(transport);
        Identity = new(transport);
        Media = new(transport);
        Message = new(transport);
        Notification = new(transport);
        Taxonomy = new(transport);
        DeveloperAnalytics = new(transport);
        KeyManagement = new(transport);
    }

    /// <summary>The base URL of each host the APIs use, by environment. The result is a copy.</summary>
    public static IReadOnlyDictionary<string, IReadOnlyDictionary<string, string>> Environments =>
        Hosts.ToDictionary(pair => pair.Key, pair => (IReadOnlyDictionary<string, string>)new Dictionary<string, string>(pair.Value));

    /// <summary>The Account API v1.</summary>
    public global::EbaySell.Account.Resources Account { get; }

    /// <summary>The Account API v2.</summary>
    public global::EbaySell.AccountV2.Resources AccountV2 { get; }

    /// <summary>The Analytics API.</summary>
    public global::EbaySell.Analytics.Resources Analytics { get; }

    /// <summary>The Feed API.</summary>
    public global::EbaySell.Feed.Resources Feed { get; }

    /// <summary>The Finances API.</summary>
    public global::EbaySell.Finances.Resources Finances { get; }

    /// <summary>The Fulfillment API.</summary>
    public global::EbaySell.Fulfillment.Resources Fulfillment { get; }

    /// <summary>The Inventory API.</summary>
    public global::EbaySell.Inventory.Resources Inventory { get; }

    /// <summary>The Marketing API.</summary>
    public global::EbaySell.Marketing.Resources Marketing { get; }

    /// <summary>The Metadata API.</summary>
    public global::EbaySell.Metadata.Resources Metadata { get; }

    /// <summary>The Negotiation API.</summary>
    public global::EbaySell.Negotiation.Resources Negotiation { get; }

    /// <summary>The Recommendation API.</summary>
    public global::EbaySell.Recommendation.Resources Recommendation { get; }

    /// <summary>The Stores API.</summary>
    public global::EbaySell.Stores.Resources Stores { get; }

    /// <summary>The Post-Order API: cancellations, returns, item-not-received inquiries and cases.</summary>
    public global::EbaySell.PostOrder.Resources PostOrder { get; }

    /// <summary>The Feedback API.</summary>
    public global::EbaySell.Feedback.Resources Feedback { get; }

    /// <summary>The Identity API.</summary>
    public global::EbaySell.Identity.Resources Identity { get; }

    /// <summary>The Media API.</summary>
    public global::EbaySell.Media.Resources Media { get; }

    /// <summary>The Message API.</summary>
    public global::EbaySell.Message.Resources Message { get; }

    /// <summary>The Notification API.</summary>
    public global::EbaySell.Notification.Resources Notification { get; }

    /// <summary>The Taxonomy API.</summary>
    public global::EbaySell.Taxonomy.Resources Taxonomy { get; }

    /// <summary>The Developer Analytics API.</summary>
    public global::EbaySell.DeveloperAnalytics.Resources DeveloperAnalytics { get; }

    /// <summary>The Key Management API.</summary>
    public global::EbaySell.KeyManagement.Resources KeyManagement { get; }

    /// <summary>Obtains and refreshes the tokens this client sends.</summary>
    public EbayOAuth OAuth { get; }

    /// <summary>Releases the connections this client opened, and the signing key. A client passed in is left open.</summary>
    public void Dispose()
    {
        transport.Dispose();
        credentials.Dispose();
    }

    internal static string AuthorizationEndpoint(string environment) =>
        environment switch
        {
            Production => "https://auth.ebay.com/oauth2/authorize",
            Sandbox => "https://auth.sandbox.ebay.com/oauth2/authorize",
            _ => throw UnknownEnvironment(environment),
        };

    internal static ArgumentException UnknownEnvironment(string environment) =>
        new($"Unknown environment \"{environment}\"; expected one of: {Production}, {Sandbox}", nameof(environment));

    private static Settings CreateSettings(EbayClientOptions options, HttpClient? httpClient, out EbayCredentials credentials)
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
        AuthorizationEndpoint(options.Environment);
        var hosts = HostMap.Select(Hosts, options.Environment, options.Hosts);
        var defaults = new Dictionary<string, string>();
        if (!string.IsNullOrEmpty(options.MarketplaceId))
        {
            defaults["X-EBAY-C-MARKETPLACE-ID"] = options.MarketplaceId;
        }
        if (!string.IsNullOrEmpty(options.ContentLanguage))
        {
            defaults["Content-Language"] = options.ContentLanguage;
        }
        var headers = new Dictionary<string, string> { ["Accept"] = "application/json" };
        if (!string.IsNullOrEmpty(options.UserAgent))
        {
            headers["User-Agent"] = options.UserAgent;
        }
        credentials = new EbayCredentials(options);
        return new Settings
        {
            BaseUrl = hosts["api"],
            Hosts = hosts,
            HeaderDefaults = defaults,
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
