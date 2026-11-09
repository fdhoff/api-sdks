using System.Globalization;
using System.Security.Cryptography;
using System.Text;
using System.Text.RegularExpressions;
using Org.BouncyCastle.Asn1.EdEC;
using Org.BouncyCastle.Asn1.Pkcs;
using Org.BouncyCastle.Crypto.Parameters;
using Org.BouncyCastle.Crypto.Signers;
using Org.BouncyCastle.Security;

namespace PackageNamespace.Runtime;

/// <summary>
/// Signs each attempt's request with an HTTP message signature (RFC 9421): a <c>Content-Digest</c> (RFC 9530) of the
/// body when there is one, then <c>Signature-Input</c> and <c>Signature</c> over the covered components, with a fresh
/// <c>created</c> time. <c>content-digest</c> is left out of a request with no body. A request without
/// <c>content-length</c> or <c>host</c> uses the body's length, <c>0</c> for any method but GET without one, or the URL's
/// authority, which <see cref="Transport"/> sends; any other field the request lacks is an error, and so is a value that is not ASCII. Call <see cref="Sign"/>
/// from <see cref="ICredentialProvider.ApplyAsync"/>.
/// </summary>
/// <remarks>
/// .NET has no Ed25519, so this file needs BouncyCastle.Cryptography. A package that does not sign removes it from its
/// build, and its tests compile it with that reference.
/// </remarks>
internal sealed partial class MessageSigner : IDisposable
{
    public const string Ed25519 = "ed25519";
    public const string RsaV15Sha256 = "rsa-v1_5-sha256";

    private static readonly HashSet<string> Derived = ["@method", "@target-uri", "@authority", "@scheme", "@request-target", "@path", "@query"];

    // A shorter last line of a key's base64 body is too common a string to redact.
    private const int MinSecretLine = 16;

    private readonly RSA? rsa;
    private readonly Func<byte[], byte[]> sign;
    private readonly string[] secrets;
    private readonly string[] components;
    private readonly string label;
    private readonly string extra;
    private readonly TimeSpan? lifetime;
    private readonly TimeProvider clock;

    /// <param name="privateKey">An unencrypted PKCS #8 PEM Ed25519 or RSA private key. It is a secret.</param>
    /// <param name="components">Lowercase field names, and <c>@method</c>, <c>@target-uri</c>, <c>@authority</c>, <c>@scheme</c>, <c>@request-target</c>, <c>@path</c> and <c>@query</c>.</param>
    /// <param name="label">The signature's label in <c>Signature-Input</c> and <c>Signature</c>.</param>
    /// <param name="keyId">Adds <c>keyid</c>, when set.</param>
    /// <param name="includeAlg">Adds <c>alg</c>, the key's algorithm.</param>
    /// <param name="lifetime">Adds <c>expires</c>, this long after <c>created</c>. Whole seconds, at least 1.</param>
    /// <param name="clock">The source of <c>created</c>; the system clock by default.</param>
    public MessageSigner(
        string privateKey,
        IReadOnlyList<string> components,
        string label = "sig1",
        string? keyId = null,
        bool includeAlg = false,
        TimeSpan? lifetime = null,
        TimeProvider? clock = null)
    {
        foreach (var component in components)
        {
            if (component.StartsWith('@') ? !Derived.Contains(component) : !FieldPattern().IsMatch(component))
            {
                throw new ArgumentException($"Unsupported covered component {component}", nameof(components));
            }
        }
        if (!LabelPattern().IsMatch(label))
        {
            throw new ArgumentException("The signature label must be a lowercase key", nameof(label));
        }
        if (lifetime is { } span && (span.Ticks % TimeSpan.TicksPerSecond != 0 || span < TimeSpan.FromSeconds(1)))
        {
            throw new ArgumentException("The signature lifetime must be a whole number of seconds, at least 1", nameof(lifetime));
        }
        (Algorithm, sign, rsa) = LoadKey(privateKey);
        var trimmed = privateKey.Trim();
        var lines = trimmed.Split('\n')[1..^1].Select(line => line.Trim()).ToArray();
        secrets = [.. new[] { trimmed, string.Concat(lines) }.Concat(lines.Where(line => line.Length >= MinSecretLine)).Distinct()];
        this.components = [.. components];
        this.label = label;
        extra = (keyId is null ? "" : $";keyid={Quote(keyId)}") + (includeAlg ? $";alg=\"{Algorithm}\"" : "");
        this.lifetime = lifetime;
        this.clock = clock ?? TimeProvider.System;
    }

    public string Algorithm { get; }

    /// <summary>The private key as given, as its PEM body and as each line of that body, to redact.</summary>
    public IReadOnlyCollection<string> Secrets() => secrets;

    public override string ToString() => $"MessageSigner({Algorithm}, ***)";

    public void Dispose() => rsa?.Dispose();

    /// <summary>The <c>Content-Digest</c> value for these exact bytes.</summary>
    public static string ContentDigest(ReadOnlySpan<byte> body) => $"sha-256=:{Convert.ToBase64String(SHA256.HashData(body))}:";

    public void Sign(AuthRequest request)
    {
        var headers = request.Headers;
        if (!request.Body.IsEmpty)
        {
            headers["Content-Digest"] = ContentDigest(request.Body.Span);
        }
        var covered = components.Where(name => name != "content-digest" || headers.ContainsKey(name)).ToArray();
        var created = clock.GetUtcNow().ToUnixTimeSeconds();
        var parameters = $"({string.Join(' ', covered.Select(name => $"\"{name}\""))});created={created}{extra}";
        if (lifetime is { } span)
        {
            parameters += $";expires={created + (long)span.TotalSeconds}";
        }
        var lines = covered.Select(name => $"\"{name}\": {Value(request, name)}").Append($"\"@signature-params\": {parameters}");
        var signatureBase = string.Join('\n', lines);
        if (!Ascii.IsValid(signatureBase))
        {
            throw new InvalidOperationException("A covered component of the request is not ASCII");
        }
        var signature = sign(Encoding.ASCII.GetBytes(signatureBase));
        headers["Signature-Input"] = $"{label}={parameters}";
        headers["Signature"] = $"{label}=:{Convert.ToBase64String(signature)}:";
    }

    private static (string, Func<byte[], byte[]>, RSA?) LoadKey(string pem)
    {
        if (!PemEncoding.TryFind(pem, out var fields) || pem[fields.Label] != "PRIVATE KEY")
        {
            throw new ArgumentException("The signing key must be an unencrypted PKCS #8 PEM private key", nameof(pem));
        }
        PrivateKeyInfo info;
        byte[] der;
        try
        {
            der = Convert.FromBase64String(pem[fields.Base64Data]);
            info = PrivateKeyInfo.GetInstance(der);
        }
        catch (Exception)
        {
            throw new ArgumentException("The signing key is not a valid private key", nameof(pem));
        }
        var algorithm = info.PrivateKeyAlgorithm.Algorithm;
        if (algorithm.Equals(EdECObjectIdentifiers.id_Ed25519))
        {
            var key = (Ed25519PrivateKeyParameters)PrivateKeyFactory.CreateKey(info);
            return (Ed25519, data =>
            {
                var signer = new Ed25519Signer();
                signer.Init(true, key);
                signer.BlockUpdate(data, 0, data.Length);
                return signer.GenerateSignature();
            }, null);
        }
        if (algorithm.Equals(PkcsObjectIdentifiers.RsaEncryption))
        {
            var rsa = RSA.Create();
            try
            {
                rsa.ImportPkcs8PrivateKey(der, out _);
            }
            catch (CryptographicException)
            {
                rsa.Dispose();
                throw new ArgumentException("The signing key is not a valid private key", nameof(pem));
            }
            return (RsaV15Sha256, data => rsa.SignData(data, HashAlgorithmName.SHA256, RSASignaturePadding.Pkcs1), rsa);
        }
        throw new ArgumentException("The signing key must be Ed25519 or RSA", nameof(pem));
    }

    private static string Quote(string value)
    {
        if (value.Any(c => c < ' ' || c > '~'))
        {
            throw new ArgumentException("A signature parameter must be printable ASCII", nameof(value));
        }
        return $"\"{value.Replace("\\", "\\\\", StringComparison.Ordinal).Replace("\"", "\\\"", StringComparison.Ordinal)}\"";
    }

    private static string Value(AuthRequest request, string name)
    {
        var url = request.Url;
        if (!name.StartsWith('@'))
        {
            if (request.Headers.TryGetValue(name, out var value))
            {
                return value.Trim();
            }
            return name switch
            {
                "content-length" when !request.Body.IsEmpty => request.Body.Length.ToString(CultureInfo.InvariantCulture),
                "content-length" when Transport.SendsEmptyContent(request.Method) => "0",
                "host" => url.Authority.ToLowerInvariant(),
                _ => throw new InvalidOperationException($"The request has no {name} field to sign"),
            };
        }
        return name switch
        {
            "@method" => request.Method.ToUpperInvariant(),
            "@target-uri" => url.AbsoluteUri,
            "@authority" => url.Authority.ToLowerInvariant(),
            "@scheme" => url.Scheme,
            "@request-target" => url.AbsolutePath + (url.Query.Length > 1 ? url.Query : ""),
            "@path" => url.AbsolutePath,
            _ => url.Query.Length > 0 ? url.Query : "?",
        };
    }

    [GeneratedRegex(@"^[a-z0-9!#$%&'*+.^_`|~-]+\z")]
    private static partial Regex FieldPattern();

    [GeneratedRegex(@"^[a-z*][a-z0-9_.*-]*\z")]
    private static partial Regex LabelPattern();
}
