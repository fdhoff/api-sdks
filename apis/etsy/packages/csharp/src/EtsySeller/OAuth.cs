using System.Globalization;
using System.Security.Cryptography;
using System.Text;
using System.Text.Json;
using System.Text.RegularExpressions;
using EtsySeller.Runtime;

namespace EtsySeller;

/// <summary>An access token and the refresh token that replaces it. Etsy prefixes both with the user's ID.</summary>
/// <param name="AccessToken">Sent as a bearer token. It lasts about an hour.</param>
/// <param name="RefreshToken">Trades for a new pair. It lasts about 90 days, and stops working once used.</param>
/// <param name="ExpiresIn">Seconds until the access token expires, when Etsy says.</param>
/// <param name="TokenType">Normally <c>Bearer</c>.</param>
public sealed record EtsyToken(string AccessToken, string RefreshToken, int? ExpiresIn = null, string TokenType = "Bearer")
{
    /// <summary>The user the token belongs to, read from its prefix.</summary>
    public long? UserId =>
        long.TryParse(AccessToken.Split('.', 2)[0], NumberStyles.None, CultureInfo.InvariantCulture, out var id) ? id : null;

    /// <summary>Leaves both tokens out, so a token can be logged safely.</summary>
    public override string ToString() => $"EtsyToken {{ UserId = {UserId}, ExpiresIn = {ExpiresIn}, TokenType = {TokenType} }}";
}

/// <summary>
/// Send the user to <see cref="Url"/>. Keep <see cref="State"/> and <see cref="CodeVerifier"/> until Etsy redirects
/// back, check that the redirect's <c>state</c> matches, then pass its <c>code</c> and this verifier to
/// <see cref="EtsyOAuth.ExchangeCodeAsync"/>.
/// </summary>
public sealed record AuthorizationRequest(Uri Url, string State, string CodeVerifier)
{
    /// <summary>Leaves the verifier out.</summary>
    public override string ToString() => $"AuthorizationRequest {{ Url = {Url}, State = {State} }}";
}

/// <summary>
/// OAuth 2 authorization code flow with PKCE, as Etsy implements it. A token this obtains is used for the client's
/// later calls, and is passed to <see cref="EtsyClientOptions.OnToken"/> for you to store.
/// </summary>
public sealed partial class EtsyOAuth
{
    /// <summary>Where users grant your app access.</summary>
    public const string AuthorizationEndpoint = "https://www.etsy.com/oauth/connect";

    internal static readonly Operation TokenOperation = new(
        "oauthToken", "POST", "/v3/public/oauth/token", "OAuth", "Token", null,
        [.. new[] { "grant_type", "client_id", "redirect_uri", "code", "code_verifier", "refresh_token" }.Select(name => new Param(name, name, ParamLocation.Urlencoded))],
        ReturnsJson: true, Security: []);

    private readonly EtsyCredentials credentials;
    private readonly Transport transport;

    internal EtsyOAuth(EtsyCredentials credentials, Transport transport)
    {
        this.credentials = credentials;
        this.transport = transport;
    }

    /// <summary>The S256 challenge for a PKCE code verifier.</summary>
    public static string CodeChallenge(string codeVerifier) =>
        Base64Url(SHA256.HashData(Encoding.ASCII.GetBytes(codeVerifier)));

    /// <summary>
    /// Builds the URL that asks a user to grant the app <paramref name="scopes"/>, with a fresh state and PKCE verifier
    /// unless you pass your own.
    /// </summary>
    /// <param name="apiKey">Your app's keystring.</param>
    /// <param name="redirectUri">One of your app's registered redirect URIs.</param>
    /// <param name="scopes">Scopes such as <c>listings_r</c>; at least one.</param>
    /// <param name="state">An unguessable value to check on the redirect.</param>
    /// <param name="codeVerifier">43 to 128 unreserved characters.</param>
    public static AuthorizationRequest CreateAuthorizationRequest(
        string apiKey, string redirectUri, IEnumerable<string> scopes, string? state = null, string? codeVerifier = null)
    {
        ArgumentException.ThrowIfNullOrEmpty(apiKey);
        ArgumentException.ThrowIfNullOrEmpty(redirectUri);
        var scope = string.Join(' ', scopes ?? throw new ArgumentNullException(nameof(scopes)));
        if (scope.Length == 0)
        {
            throw new ArgumentException("Request at least one scope", nameof(scopes));
        }
        var verifier = codeVerifier ?? Base64Url(RandomNumberGenerator.GetBytes(64));
        if (!Verifier().IsMatch(verifier))
        {
            throw new ArgumentException("The code verifier must be 43 to 128 unreserved characters", nameof(codeVerifier));
        }
        state ??= Base64Url(RandomNumberGenerator.GetBytes(32));
        var query = new Dictionary<string, string>
        {
            ["response_type"] = "code",
            ["client_id"] = apiKey,
            ["redirect_uri"] = redirectUri,
            ["scope"] = scope,
            ["state"] = state,
            ["code_challenge"] = CodeChallenge(verifier),
            ["code_challenge_method"] = "S256",
        };
        var search = string.Join('&', query.Select(pair => $"{Uri.EscapeDataString(pair.Key)}={Uri.EscapeDataString(pair.Value)}"));
        return new AuthorizationRequest(new Uri($"{AuthorizationEndpoint}?{search}"), state, verifier);
    }

    /// <summary>Builds the URL that asks a user to grant this client's app <paramref name="scopes"/>. See <see cref="AuthorizationRequest"/>.</summary>
    public AuthorizationRequest CreateAuthorizationRequest(string redirectUri, IEnumerable<string> scopes, string? state = null) =>
        CreateAuthorizationRequest(credentials.ApiKey, redirectUri, scopes, state);

    /// <summary>Trades the code from Etsy's redirect for a token. <paramref name="redirectUri"/> must match the authorization request's.</summary>
    public Task<EtsyToken> ExchangeCodeAsync(string code, string codeVerifier, string redirectUri, CancellationToken cancellationToken = default)
    {
        ArgumentException.ThrowIfNullOrEmpty(code);
        ArgumentException.ThrowIfNullOrEmpty(codeVerifier);
        ArgumentException.ThrowIfNullOrEmpty(redirectUri);
        credentials.Remember(code, codeVerifier);
        return RequestAsync(["authorization_code", credentials.ApiKey, redirectUri, code, codeVerifier, null], cancellationToken);
    }

    /// <summary>Replaces the access token now. The client also does this itself after a 401.</summary>
    /// <exception cref="InvalidOperationException">There is no refresh token yet.</exception>
    public Task<EtsyToken> RefreshAsync(CancellationToken cancellationToken = default)
    {
        var refreshToken = credentials.RefreshToken
            ?? throw new InvalidOperationException("There is no refresh token: set RefreshToken, or exchange a code first");
        return RequestAsync(["refresh_token", credentials.ApiKey, null, null, null, refreshToken], cancellationToken);
    }

    private async Task<EtsyToken> RequestAsync(object?[] values, CancellationToken cancellationToken)
    {
        var reply = await transport.CallAsync<JsonElement>(TokenOperation, values, cancellationToken).ConfigureAwait(false);
        var token = Read(reply) ?? throw new ApiDecodeException("The token response has no access and refresh token") { Status = 200 };
        await credentials.StoreAsync(token, cancellationToken).ConfigureAwait(false);
        return token;
    }

    private static EtsyToken? Read(JsonElement reply)
    {
        if (reply.ValueKind != JsonValueKind.Object)
        {
            return null;
        }
        string? Text(string name) => reply.TryGetProperty(name, out var value) && value.ValueKind == JsonValueKind.String ? value.GetString() : null;

        var access = Text("access_token");
        var refresh = Text("refresh_token");
        if (string.IsNullOrEmpty(access) || string.IsNullOrEmpty(refresh))
        {
            return null;
        }
        int? expiresIn = reply.TryGetProperty("expires_in", out var expires) && expires.ValueKind == JsonValueKind.Number && expires.TryGetInt32(out var seconds) ? seconds : null;
        return new EtsyToken(access, refresh, expiresIn, Text("token_type") ?? "Bearer");
    }

    private static string Base64Url(byte[] bytes) => Convert.ToBase64String(bytes).TrimEnd('=').Replace('+', '-').Replace('/', '_');

    [GeneratedRegex("^[A-Za-z0-9._~-]{43,128}$")]
    private static partial Regex Verifier();
}

/// <summary>
/// Sends <c>x-api-key</c> on every operation and the access token on those that need OAuth. After a 401 on one of
/// those, refreshes the access token once, when there is a refresh token.
/// </summary>
internal sealed class EtsyCredentials : ICredentialProvider
{
    private readonly object gate = new();
    private readonly string sharedSecret;
    private readonly Func<EtsyToken, CancellationToken, Task>? onToken;
    private readonly List<string> seen = [];
    private string? accessToken;
    private string? refreshToken;

    public EtsyCredentials(string apiKey, string sharedSecret, EtsyClientOptions options)
    {
        if (string.IsNullOrEmpty(apiKey) || string.IsNullOrEmpty(sharedSecret))
        {
            throw new ArgumentException("An API key and shared secret are required");
        }
        if ($"{apiKey}{sharedSecret}{options.AccessToken}{options.RefreshToken}".Any(char.IsControl))
        {
            throw new ArgumentException("Credentials must not hold control characters");
        }
        ApiKey = apiKey;
        this.sharedSecret = sharedSecret;
        accessToken = options.AccessToken;
        refreshToken = options.RefreshToken;
        onToken = options.OnToken;
        Remember(accessToken, refreshToken);
    }

    public string ApiKey { get; }

    public string? RefreshToken
    {
        get
        {
            lock (gate)
            {
                return refreshToken;
            }
        }
    }

    /// <summary>Set by the client: replaces the token pair.</summary>
    public Func<CancellationToken, Task<EtsyToken>>? Refresher { get; set; }

    public ValueTask ApplyAsync(AuthRequest request, CancellationToken cancellationToken)
    {
        if (Needs(request.Operation, "api_key"))
        {
            request.Headers["x-api-key"] = $"{ApiKey}:{sharedSecret}";
        }
        string? access;
        lock (gate)
        {
            access = accessToken;
        }
        if (!string.IsNullOrEmpty(access) && Needs(request.Operation, "oauth2"))
        {
            request.Headers["Authorization"] = $"Bearer {access}";
        }
        return ValueTask.CompletedTask;
    }

    public IReadOnlyCollection<string> Secrets()
    {
        lock (gate)
        {
            return [ApiKey, sharedSecret, .. seen];
        }
    }

    public async ValueTask<bool> RefreshAsync(AuthRequest request, CancellationToken cancellationToken)
    {
        if (Refresher is not { } refresher || string.IsNullOrEmpty(RefreshToken) || !Needs(request.Operation, "oauth2"))
        {
            return false;
        }
        await refresher(cancellationToken).ConfigureAwait(false);
        return true;
    }

    /// <summary>Keeps values out of logs and errors from now on, such as a code about to be exchanged.</summary>
    public void Remember(params string?[] values)
    {
        lock (gate)
        {
            seen.AddRange(values.Where(value => !string.IsNullOrEmpty(value))!);
        }
    }

    public async Task StoreAsync(EtsyToken token, CancellationToken cancellationToken)
    {
        lock (gate)
        {
            seen.Add(token.AccessToken);
            seen.Add(token.RefreshToken);
            accessToken = token.AccessToken;
            refreshToken = token.RefreshToken;
        }
        if (onToken is not null)
        {
            await onToken(token, cancellationToken).ConfigureAwait(false);
        }
    }

    private static bool Needs(Operation operation, string scheme) =>
        operation.Security?.Any(requirement => requirement.Any(part => part.Name == scheme)) == true;
}
