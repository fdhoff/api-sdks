using System.Globalization;
using System.Security.Cryptography;
using System.Text;

namespace EbaySell;

/// <summary>Why <see cref="WebhookVerifier.Verify"/> rejected a webhook.</summary>
public enum WebhookFailure
{
    MalformedHeader,
    TooOld,
    BadSignature,
    InvalidTolerance,
}

/// <summary>A webhook failed verification, or the tolerance is invalid. The message never holds the secret or the body.</summary>
public sealed class WebhookSignatureException(WebhookFailure reason) : Exception(reason switch
{
    WebhookFailure.MalformedHeader => "The webhook signature header is malformed.",
    WebhookFailure.TooOld => "The webhook timestamp is older than the tolerance.",
    WebhookFailure.InvalidTolerance => "The webhook tolerance must be greater than zero.",
    _ => "No webhook signature matches the body.",
})
{
    public WebhookFailure Reason { get; } = reason;
}

/// <summary>
/// Checks timestamped HMAC-SHA256 webhook signatures: a header of <c>t=&lt;unix seconds&gt;,v1=&lt;hex&gt;</c>, signed
/// over <c>&lt;t&gt;.&lt;raw body&gt;</c> with the endpoint's secret.
/// </summary>
/// <remarks>A package whose API sends no signed webhooks removes this file from its build.</remarks>
public static class WebhookVerifier
{
    public static readonly TimeSpan DefaultTolerance = TimeSpan.FromMinutes(5);

    /// <summary>
    /// Checks a webhook's signature header against its raw body as received, never re-serialised. Any one matching
    /// <c>v1</c> value is enough, so a header may carry several while a secret rotates.
    /// </summary>
    /// <param name="tolerance">The oldest timestamp to accept, greater than zero, by default <see cref="DefaultTolerance"/>.</param>
    /// <param name="now">The time to check against, by default the clock.</param>
    /// <exception cref="WebhookSignatureException">The tolerance is invalid, or the header is malformed, too old or matches no signature.</exception>
    public static void Verify(ReadOnlySpan<byte> payload, string? header, string secret, TimeSpan? tolerance = null, DateTimeOffset? now = null)
    {
        var limit = tolerance ?? DefaultTolerance;
        if (limit <= TimeSpan.Zero)
        {
            throw new WebhookSignatureException(WebhookFailure.InvalidTolerance);
        }

        var (timestamp, signatures) = Parse(header);
        var message = new byte[timestamp.Length + 1 + payload.Length];
        Encoding.ASCII.GetBytes(timestamp + ".", message);
        payload.CopyTo(message.AsSpan(timestamp.Length + 1));
        var expected = HMACSHA256.HashData(Encoding.UTF8.GetBytes(secret), message);
        var matched = false;
        foreach (var signature in signatures)
        {
            if (signature.Length == 64 && signature.All(char.IsAsciiHexDigit))
            {
                matched |= CryptographicOperations.FixedTimeEquals(Convert.FromHexString(signature), expected);
            }
        }

        if (!matched)
        {
            throw new WebhookSignatureException(WebhookFailure.BadSignature);
        }

        var signed = DateTimeOffset.FromUnixTimeSeconds(long.Parse(timestamp, CultureInfo.InvariantCulture));
        if ((now ?? DateTimeOffset.UtcNow) - signed > limit)
        {
            throw new WebhookSignatureException(WebhookFailure.TooOld);
        }
    }

    private static (string Timestamp, List<string> Signatures) Parse(string? header)
    {
        if (header is null)
        {
            throw new WebhookSignatureException(WebhookFailure.MalformedHeader);
        }

        string? timestamp = null;
        var signatures = new List<string>();
        foreach (var entry in header.Split(','))
        {
            var trimmed = entry.Trim(' ', '\t');
            var equals = trimmed.IndexOf('=');
            if (equals < 0)
            {
                throw new WebhookSignatureException(WebhookFailure.MalformedHeader);
            }

            var key = trimmed[..equals];
            var value = trimmed[(equals + 1)..];
            if (key == "t")
            {
                if (timestamp is not null || value.Length is 0 or > 12 || !value.All(char.IsAsciiDigit))
                {
                    throw new WebhookSignatureException(WebhookFailure.MalformedHeader);
                }

                timestamp = value;
            }
            else if (key == "v1")
            {
                signatures.Add(value);
            }
        }

        if (timestamp is null || signatures.Count == 0)
        {
            throw new WebhookSignatureException(WebhookFailure.MalformedHeader);
        }

        return (timestamp, signatures);
    }
}
