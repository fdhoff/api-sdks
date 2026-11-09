using System.Security.Cryptography;
using System.Text;
using System.Text.Json;
using EbaySell.Runtime;

namespace EbaySell;

/// <summary>
/// An access token and, for a user token, the refresh token that replaces it. eBay's refresh returns a new access
/// token only, so the refresh token carries over.
/// </summary>
/// <param name="AccessToken">Sent as a bearer token.</param>
/// <param name="ExpiresIn">Seconds until the access token expires, when eBay says.</param>
/// <param name="RefreshToken">Trades for a new access token. Application tokens have none.</param>
/// <param name="RefreshTokenExpiresIn">Seconds until the refresh token expires, when eBay says.</param>
/// <param name="TokenType">Normally <c>Bearer</c>.</param>
public sealed record EbayToken(string AccessToken, long? ExpiresIn = null, string? RefreshToken = null, long? RefreshTokenExpiresIn = null, string TokenType = "Bearer")
{
    /// <summary>Leaves both tokens out, so a token can be logged safely.</summary>
    public override string ToString() => $"EbayToken {{ ExpiresIn = {ExpiresIn}, RefreshTokenExpiresIn = {RefreshTokenExpiresIn}, TokenType = {TokenType} }}";
}

/// <summary>
/// Send the user to <see cref="Url"/>. Keep <see cref="State"/> until eBay redirects to your RuName's accept URL, check
/// that the redirect's <c>state</c> matches, then pass its <c>code</c> to <see cref="EbayOAuth.ExchangeCodeAsync"/>.
/// </summary>
public sealed record AuthorizationRequest(Uri Url, string State);

/// <summary>
/// OAuth 2 as eBay implements it: application tokens from the client credentials grant, and user tokens from the
/// authorization code grant, both from one token endpoint with HTTP Basic client authentication. A user token this
/// obtains is used for the client's later calls, and passed to <see cref="EbayClientOptions.OnToken"/>.
/// </summary>
public sealed class EbayOAuth
{
    /// <summary>The scope of an application token, which the public operations accept.</summary>
    public const string ApiScope = "https://api.ebay.com/oauth/api_scope";

    /// <summary>The token endpoint authenticates with the keyset alone, so it has no security and a 401 from it never triggers a refresh.</summary>
    internal static readonly Operation TokenOperation = new(
        "oauthToken", "POST", "/identity/v1/oauth2/token", "OAuth", "Token", null,
        [.. new[] { "grant_type", "code", "redirect_uri", "refresh_token", "scope" }.Select(name => new Param(name, name, ParamLocation.Urlencoded))],
        ReturnsJson: true, Security: [], Host: "api");

    private readonly EbayCredentials credentials;
    private readonly Transport transport;
    private readonly string? ruName;
    private readonly string appScope;
    private readonly string userScope;
    private readonly string environment;
    private readonly SemaphoreSlim minting = new(1, 1);
    private readonly SemaphoreSlim refreshing = new(1, 1);

    internal EbayOAuth(EbayCredentials credentials, Transport transport, EbayClientOptions options)
    {
        this.credentials = credentials;
        this.transport = transport;
        ruName = options.RuName;
        appScope = string.Join(' ', options.AppScopes);
        userScope = string.Join(' ', options.UserScopes);
        environment = options.Environment;
    }

    /// <summary>
    /// Builds the URL that asks a user to grant the app with <paramref name="clientId"/> the given scopes, with a fresh
    /// state unless you pass your own.
    /// </summary>
    /// <param name="clientId">Your keyset's App ID.</param>
    /// <param name="ruName">Your app's redirect URL name, which eBay takes as <c>redirect_uri</c>.</param>
    /// <param name="environment"><see cref="EbayClient.Production"/> or <see cref="EbayClient.Sandbox"/>.</param>
    /// <param name="scopes">At least one scope.</param>
    /// <param name="state">An unguessable value to check on the redirect.</param>
    /// <param name="prompt"><c>login</c> makes the user sign in even if they already are.</param>
    public static AuthorizationRequest CreateAuthorizationRequest(
        string clientId, string ruName, string environment, IEnumerable<string> scopes, string? state = null, string? prompt = null)
    {
        ArgumentException.ThrowIfNullOrEmpty(clientId);
        ArgumentException.ThrowIfNullOrEmpty(ruName);
        var endpoint = EbayClient.AuthorizationEndpoint(environment);
        var scope = string.Join(' ', scopes ?? throw new ArgumentNullException(nameof(scopes)));
        if (scope.Length == 0)
        {
            throw new ArgumentException("Request at least one scope", nameof(scopes));
        }
        state ??= Convert.ToBase64String(RandomNumberGenerator.GetBytes(32)).TrimEnd('=').Replace('+', '-').Replace('/', '_');
        var query = new Dictionary<string, string>
        {
            ["client_id"] = clientId,
            ["redirect_uri"] = ruName,
            ["response_type"] = "code",
            ["scope"] = scope,
            ["state"] = state,
        };
        if (!string.IsNullOrEmpty(prompt))
        {
            query["prompt"] = prompt;
        }
        var search = string.Join('&', query.Select(pair => $"{Uri.EscapeDataString(pair.Key)}={Uri.EscapeDataString(pair.Value)}"));
        return new AuthorizationRequest(new Uri($"{endpoint}?{search}"), state);
    }

    /// <summary>Builds the URL that asks a user to grant this client's app <paramref name="scopes"/>, in the client's environment.</summary>
    /// <exception cref="InvalidOperationException">The client has no <see cref="EbayClientOptions.ClientId"/> or <see cref="EbayClientOptions.RuName"/>.</exception>
    public AuthorizationRequest CreateAuthorizationRequest(IEnumerable<string> scopes, string? state = null, string? prompt = null) =>
        CreateAuthorizationRequest(UserGrant(), ruName!, environment, scopes, state, prompt);

    /// <summary>Trades the code from eBay's redirect for a user token and its refresh token.</summary>
    /// <exception cref="InvalidOperationException">The client has no keyset or <see cref="EbayClientOptions.RuName"/>.</exception>
    public Task<EbayToken> ExchangeCodeAsync(string code, CancellationToken cancellationToken = default)
    {
        ArgumentException.ThrowIfNullOrEmpty(code);
        credentials.Remember(code);
        UserGrant();
        return OneAtATimeAsync(refreshing, () => UserTokenAsync(["authorization_code", code, ruName, null, null]), cancellationToken);
    }

    /// <summary>
    /// Replaces the user token now. The client also does this itself after a 401. <paramref name="scopes"/> must be the
    /// original grant's or fewer, and default to <see cref="EbayClientOptions.UserScopes"/>. A refresh asked for while
    /// another is under way waits for it and returns its token.
    /// </summary>
    /// <exception cref="InvalidOperationException">There is no refresh token yet.</exception>
    public Task<EbayToken> RefreshAsync(IEnumerable<string>? scopes = null, CancellationToken cancellationToken = default)
    {
        var (_, before, refreshToken) = credentials.Current();
        if (string.IsNullOrEmpty(refreshToken))
        {
            throw new InvalidOperationException("There is no refresh token: set RefreshToken, or exchange a code first");
        }
        var scope = scopes is null ? userScope : string.Join(' ', scopes);
        return OneAtATimeAsync(
            refreshing,
            () =>
            {
                var (_, user, refresh) = credentials.Current();
                return !string.IsNullOrEmpty(user) && user != before
                    ? Task.FromResult(new EbayToken(user, RefreshToken: refresh))
                    : UserTokenAsync(["refresh_token", null, null, refresh, scope.Length == 0 ? null : scope]);
            },
            cancellationToken);
    }

    /// <summary>Returns an application token with <see cref="EbayClientOptions.AppScopes"/>, minting one unless the current one is still fresh.</summary>
    /// <exception cref="InvalidOperationException">The client has no keyset.</exception>
    public Task<EbayToken> GetAppTokenAsync(CancellationToken cancellationToken = default)
    {
        if (!credentials.CanMint)
        {
            throw new InvalidOperationException("Set ClientId and ClientSecret to mint application tokens");
        }
        return OneAtATimeAsync(
            minting,
            async () =>
            {
                if (credentials.FreshAppToken() is { } current)
                {
                    return new EbayToken(current);
                }
                var token = await RequestAsync(["client_credentials", null, null, null, appScope]).ConfigureAwait(false);
                credentials.StoreApp(token);
                return token;
            },
            cancellationToken);
    }

    private string UserGrant()
    {
        if (!credentials.CanMint)
        {
            throw new InvalidOperationException("Set ClientId and ClientSecret to use the authorization code grant");
        }
        if (string.IsNullOrEmpty(ruName))
        {
            throw new InvalidOperationException("Set RuName to use the authorization code grant");
        }
        return credentials.ClientId!;
    }

    /// <summary>
    /// Sends one token request of a kind at a time. Cancelling stops the wait, not a request already sent, so a token
    /// eBay has already issued is still stored. The transport's timeout bounds the request.
    /// </summary>
    private static async Task<EbayToken> OneAtATimeAsync(SemaphoreSlim gate, Func<Task<EbayToken>> request, CancellationToken cancellationToken)
    {
        await gate.WaitAsync(cancellationToken).ConfigureAwait(false);
        Task<EbayToken> pending;
        try
        {
            pending = request();
        }
        catch
        {
            gate.Release();
            throw;
        }
        _ = pending.ContinueWith(
            done =>
            {
                _ = done.Exception;
                gate.Release();
            },
            CancellationToken.None, TaskContinuationOptions.ExecuteSynchronously, TaskScheduler.Default);
        return await pending.WaitAsync(cancellationToken).ConfigureAwait(false);
    }

    private async Task<EbayToken> UserTokenAsync(object?[] values)
    {
        var token = await RequestAsync(values).ConfigureAwait(false);
        return await credentials.StoreUserAsync(token, CancellationToken.None).ConfigureAwait(false);
    }

    private async Task<EbayToken> RequestAsync(object?[] values)
    {
        var reply = await transport.CallAsync<JsonElement>(TokenOperation, values, CancellationToken.None).ConfigureAwait(false);
        return Read(reply) ?? throw new ApiDecodeException("The token response has no access token") { Status = 200 };
    }

    private static EbayToken? Read(JsonElement reply)
    {
        if (reply.ValueKind != JsonValueKind.Object)
        {
            return null;
        }
        string? Text(string name) => reply.TryGetProperty(name, out var value) && value.ValueKind == JsonValueKind.String ? value.GetString() : null;
        long? Seconds(string name) =>
            reply.TryGetProperty(name, out var value) && value.ValueKind == JsonValueKind.Number && value.TryGetInt64(out var seconds) && seconds > 0 ? seconds : null;

        var access = Text("access_token");
        if (string.IsNullOrEmpty(access))
        {
            return null;
        }
        var refresh = Text("refresh_token");
        var type = Text("token_type");
        return new EbayToken(access, Seconds("expires_in"), string.IsNullOrEmpty(refresh) ? null : refresh, Seconds("refresh_token_expires_in"), string.IsNullOrEmpty(type) ? "Bearer" : type);
    }
}

/// <summary>
/// Sends an application token on operations that accept one and a user token on the rest, then signs the request when
/// there is a signing key. Mints an application token when there is none or it is about to expire. After a 401 it mints
/// a new application token, or refreshes the user token once when there is a refresh token.
/// </summary>
internal sealed class EbayCredentials : ICredentialProvider, IDisposable
{
    /// <summary>The scopes eBay's client credentials grant gives. An operation that accepts any of them takes an application token.</summary>
    private static readonly HashSet<string> AppScopes = [EbayOAuth.ApiScope, $"{EbayOAuth.ApiScope}/metadata.insights"];

    /// <summary>An application token this close to expiry is replaced before use.</summary>
    private static readonly TimeSpan ExpiryMargin = TimeSpan.FromSeconds(60);

    /// <summary>How many earlier tokens and codes stay redacted besides the current ones.</summary>
    private const int Remembered = 16;

    private readonly object gate = new();
    private readonly string? clientSecret;
    private readonly string? basic;
    private readonly Func<EbayToken, CancellationToken, Task>? onToken;
    private readonly MessageSigner? signer;
    private readonly string? signatureKey;
    private readonly TimeProvider clock;
    private readonly List<string> seen = [];
    private string? appToken;
    private DateTimeOffset? appExpiresAt;
    private string? userToken;
    private string? refreshToken;

    public EbayCredentials(EbayClientOptions options)
    {
        if (string.IsNullOrEmpty(options.ClientId) != string.IsNullOrEmpty(options.ClientSecret))
        {
            throw new ArgumentException("Set ClientId and ClientSecret together", nameof(options));
        }
        if (string.IsNullOrEmpty(options.ClientId) && string.IsNullOrEmpty(options.AppToken) && string.IsNullOrEmpty(options.UserToken) && string.IsNullOrEmpty(options.RefreshToken))
        {
            throw new ArgumentException("Set ClientId and ClientSecret, or a token", nameof(options));
        }
        if ($"{options.ClientId}{options.ClientSecret}{options.AppToken}{options.UserToken}{options.RefreshToken}{options.SigningKey?.Jwe}".Any(char.IsControl))
        {
            throw new ArgumentException("Credentials must not hold control characters", nameof(options));
        }
        ClientId = string.IsNullOrEmpty(options.ClientId) ? null : options.ClientId;
        clientSecret = options.ClientSecret;
        if (ClientId is not null)
        {
            basic = Convert.ToBase64String(Encoding.UTF8.GetBytes($"{ClientId}:{clientSecret}"));
        }
        appToken = options.AppToken;
        userToken = options.UserToken;
        refreshToken = options.RefreshToken;
        onToken = options.OnToken;
        clock = options.Clock;
        if (options.SigningKey is { } key)
        {
            signer = key.CreateSigner();
            signatureKey = key.Jwe;
        }
    }

    public string? ClientId { get; }

    public bool CanMint => basic is not null;

    /// <summary>Set by the client.</summary>
    public EbayOAuth? OAuth { get; set; }

    public void Dispose() => signer?.Dispose();

    public (string? App, string? User, string? Refresh) Current()
    {
        lock (gate)
        {
            return (appToken, userToken, refreshToken);
        }
    }

    /// <summary>The application token, unless it is about to expire. A token passed in has no known expiry.</summary>
    public string? FreshAppToken()
    {
        lock (gate)
        {
            return !string.IsNullOrEmpty(appToken) && (appExpiresAt is not { } expiry || clock.GetUtcNow() < expiry - ExpiryMargin) ? appToken : null;
        }
    }

    public async ValueTask ApplyAsync(AuthRequest request, CancellationToken cancellationToken)
    {
        if (request.Operation == EbayOAuth.TokenOperation)
        {
            request.Headers["Authorization"] = $"Basic {basic ?? throw new InvalidOperationException("A token request needs ClientId and ClientSecret")}";
            return;
        }
        request.Headers["Authorization"] = $"Bearer {await TokenAsync(request.Operation, cancellationToken).ConfigureAwait(false)}";
        if (signer is not null)
        {
            request.Headers["x-ebay-signature-key"] = signatureKey!;
            signer.Sign(request);
        }
    }

    public IReadOnlyCollection<string> Secrets()
    {
        lock (gate)
        {
            var current = new[] { clientSecret, basic, appToken, userToken, refreshToken }.Where(value => !string.IsNullOrEmpty(value));
            return [.. current!, .. signer?.Secrets() ?? [], .. seen];
        }
    }

    public async ValueTask<bool> RefreshAsync(AuthRequest request, CancellationToken cancellationToken)
    {
        var (app, user, refresh) = Current();
        var header = request.Headers.GetValueOrDefault("Authorization");
        var sent = header?.StartsWith("Bearer ", StringComparison.Ordinal) == true ? header["Bearer ".Length..] : null;
        if (TakesAppToken(request.Operation) && (CanMint || !string.IsNullOrEmpty(app)))
        {
            if (!CanMint)
            {
                return false;
            }
            ExpireApp(sent);
            await OAuth!.GetAppTokenAsync(cancellationToken).ConfigureAwait(false);
            return true;
        }
        if (string.IsNullOrEmpty(refresh))
        {
            return false;
        }
        // Another refresh replaced the token this request sent, so retry with the new one.
        if (user != sent)
        {
            return true;
        }
        await OAuth!.RefreshAsync(cancellationToken: cancellationToken).ConfigureAwait(false);
        return true;
    }

    /// <summary>
    /// Keeps values out of logs and errors from now on, such as a code about to be exchanged. Only the most recent
    /// values are kept, so a long-lived client does not grow.
    /// </summary>
    public void Remember(params string?[] values)
    {
        lock (gate)
        {
            Keep(values);
        }
    }

    public void StoreApp(EbayToken token)
    {
        lock (gate)
        {
            Keep(appToken);
            appToken = token.AccessToken;
            appExpiresAt = token.ExpiresIn is { } seconds ? clock.GetUtcNow().AddSeconds(seconds) : null;
        }
    }

    /// <summary>Keeps the refresh token when the response has none, as eBay's refresh does not return one.</summary>
    public async Task<EbayToken> StoreUserAsync(EbayToken token, CancellationToken cancellationToken)
    {
        lock (gate)
        {
            token = token.RefreshToken is null ? token with { RefreshToken = refreshToken } : token;
            Keep(userToken, refreshToken);
            userToken = token.AccessToken;
            refreshToken = token.RefreshToken;
        }
        if (onToken is not null)
        {
            await onToken(token, cancellationToken).ConfigureAwait(false);
        }
        return token;
    }

    /// <summary>An operation accepts an application token when any scope it lists is one the client credentials grant gives.</summary>
    internal static bool TakesAppToken(Operation operation) =>
        operation.Security?.Any(requirement => requirement.Any(scheme => scheme.Scopes.Any(AppScopes.Contains))) == true;

    private async ValueTask<string> TokenAsync(Operation operation, CancellationToken cancellationToken)
    {
        var (_, user, _) = Current();
        if (!TakesAppToken(operation))
        {
            return string.IsNullOrEmpty(user)
                ? throw new InvalidOperationException($"{operation.Id} needs a user token: set UserToken, or call OAuth.ExchangeCodeAsync first")
                : user;
        }
        var token = FreshAppToken();
        if (token is null && CanMint)
        {
            token = (await OAuth!.GetAppTokenAsync(cancellationToken).ConfigureAwait(false)).AccessToken;
        }
        token ??= string.IsNullOrEmpty(user) ? null : user;
        return token ?? throw new InvalidOperationException($"{operation.Id} needs an application token: set ClientId and ClientSecret, or AppToken");
    }

    /// <summary>Makes the next call mint a new application token, unless another one already replaced <paramref name="sent"/>.</summary>
    private void ExpireApp(string? sent)
    {
        lock (gate)
        {
            if (appToken == sent)
            {
                appExpiresAt = DateTimeOffset.MinValue + ExpiryMargin;
            }
        }
    }

    private void Keep(params string?[] values)
    {
        seen.AddRange(values.Where(value => !string.IsNullOrEmpty(value))!);
        if (seen.Count > Remembered)
        {
            seen.RemoveRange(0, seen.Count - Remembered);
        }
    }
}
