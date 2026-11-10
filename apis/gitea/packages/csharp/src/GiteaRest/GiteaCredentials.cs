using System.Text;

namespace GiteaRest;

/// <summary>
/// How the client signs in: an access token, or a username and password with an optional one-time password. The
/// client keeps them only in memory, and removes them from every exception and log line.
/// </summary>
public sealed class GiteaCredentials
{
    private GiteaCredentials(string authorization, string? otp, string[] secrets)
    {
        Authorization = authorization;
        Otp = otp;
        Secrets = secrets;
    }

    internal string Authorization { get; }

    internal string? Otp { get; }

    internal string[] Secrets { get; }

    /// <summary>An access token, made under Settings → Applications on your instance. Sent as <c>Authorization: token &lt;token&gt;</c>.</summary>
    /// <exception cref="ArgumentException">The token is empty.</exception>
    public static GiteaCredentials Token(string token)
    {
        ArgumentException.ThrowIfNullOrEmpty(token);
        return new GiteaCredentials($"token {token}", null, [token]);
    }

    /// <summary>
    /// A username and password, sent with Basic authentication. When your account has two-factor authentication on,
    /// pass the current one-time password as <paramref name="otp"/>, sent as <c>X-GITEA-OTP</c>. It expires within a
    /// minute, so this suits a short task, such as creating an access token to use from then on.
    /// </summary>
    /// <exception cref="ArgumentException">The username or password is empty, or <paramref name="otp"/> is set but empty.</exception>
    public static GiteaCredentials Basic(string username, string password, string? otp = null)
    {
        ArgumentException.ThrowIfNullOrEmpty(username);
        ArgumentException.ThrowIfNullOrEmpty(password);
        if (otp is { Length: 0 })
        {
            throw new ArgumentException("The one-time password must not be empty", nameof(otp));
        }
        var encoded = Convert.ToBase64String(Encoding.UTF8.GetBytes($"{username}:{password}"));
        string[] secrets = otp is null ? [password, encoded] : [password, encoded, otp];
        return new GiteaCredentials($"Basic {encoded}", otp, secrets);
    }

    /// <summary>Never shows the credentials.</summary>
    public override string ToString() => "GiteaCredentials(redacted)";
}
