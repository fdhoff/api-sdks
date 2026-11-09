using EbaySell.Runtime;

namespace EbaySell;

/// <summary>
/// A key pair from the Key Management API's create call. eBay returns the private key only once, and it is a secret.
/// Ed25519 and RSA keys both work.
/// </summary>
/// <param name="PrivateKey">The private key, as that call returns it or as a PKCS #8 PEM.</param>
/// <param name="Jwe">The public key JWE, sent as <c>x-ebay-signature-key</c>.</param>
public sealed record EbaySigningKey(string PrivateKey, string Jwe)
{
    /// <summary>The parts of a request that eBay's signature covers. <c>content-digest</c> is left out of a request without a body.</summary>
    public static IReadOnlyList<string> SignatureComponents { get; } = ["content-digest", "x-ebay-signature-key", "@method", "@path", "@authority"];

    private const string PemHeader = "-----BEGIN PRIVATE KEY-----";

    /// <summary>Leaves the private key out.</summary>
    public override string ToString() => $"EbaySigningKey {{ Jwe = {Jwe}, PrivateKey = *** }}";

    internal MessageSigner CreateSigner()
    {
        ArgumentException.ThrowIfNullOrEmpty(PrivateKey);
        ArgumentException.ThrowIfNullOrEmpty(Jwe);
        return new MessageSigner(Pem(PrivateKey), SignatureComponents);
    }

    /// <summary>Wraps the base64 body eBay returns in the PEM lines it leaves out.</summary>
    internal static string Pem(string privateKey)
    {
        var key = privateKey.Trim();
        if (key.StartsWith(PemHeader, StringComparison.Ordinal))
        {
            return key;
        }
        var body = string.Concat(key.Where(character => !char.IsWhiteSpace(character)));
        var lines = Enumerable.Range(0, (body.Length + 63) / 64).Select(index => body.Substring(index * 64, Math.Min(64, body.Length - (index * 64))));
        return string.Join('\n', [PemHeader, .. lines, "-----END PRIVATE KEY-----"]);
    }
}
