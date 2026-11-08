using System.Collections.Concurrent;
using System.Net;
using System.Text;
using System.Text.Json;
using BackMarketSeller.Runtime;
using Org.BouncyCastle.Crypto.Generators;
using Org.BouncyCastle.Crypto.Parameters;
using Org.BouncyCastle.Crypto.Signers;
using Org.BouncyCastle.Pkcs;
using Org.BouncyCastle.Security;
using Xunit;

namespace BackMarketSeller.Tests;

public sealed class SigningTests
{
    // The published test keys of RFC 9421, Appendix B.1.4 and B.1.1. The RSA key is re-encoded from PKCS #1 to PKCS #8.
    private const string Ed25519Key = """
        -----BEGIN PRIVATE KEY-----
        MC4CAQAwBQYDK2VwBCIEIJ+DYvh6SEqVTm50DFtMDoQikTmiCqirVv9mWG9qfSnF
        -----END PRIVATE KEY-----
        """;

    private const string RsaKey = """
        -----BEGIN PRIVATE KEY-----
        MIIEwgIBADANBgkqhkiG9w0BAQEFAASCBKwwggSoAgEAAoIBAQCEAph22h6jLzNw
        BxHzvgvxydnErMAbB3u/foA+ns+/pDaN2w8FGvBYQGd7Pp3RQMoPAZtzqfF8RcDL
        mZuGBqPOvDcw4S3y4Dm3FIqhsGkoN4Es6x0koWowaZcJC8Qbth6ZzENNE/ECV4gC
        BhhGNNJ39AHBVb07A0WF6SujdG2WKdXRrvmN9mCSd79iKS1K8sbfiXDbOpcENMLk
        0dE5SoZOUwvg+U1lLlGLZThoI3HatQ9FwoiUTQ+4rEjhP4choWm/z6t1Xp5SA6sH
        bF4jV1IUWf+ee/k6hkkQgH5Wa4qfcMJRwJlIWVA9JdJ8EOJQaHA7Dvpa5JKx/UPh
        v+8ugnXTAgMBAAECggEAb8lm5JZ2hUduLnq+OAKCSODeWQ7Uqs7eet2bqeuAD0/2
        po+PG4qhZoo7VwFCUTWlJan9wqdxiAPlbEQKkCdFRcbakbjN2TMJjMCHWL5zfgvq
        hmgeyKsrqg1wSce97J1/Mkvn3fh6CbqnwNb6bVFDvTJS3i5FzRhKiv6rUsYm8ZAd
        F4XRaYkFkeuHPl7rc+ruUTSAjC4GovxIxoDJFe0r4kbFmkiZOr40e8RZYK7T1IKr
        Svzfxx5AjnlK/OZOTCq0L7wBPbMW+IxmQpFCjpI+yuoi3FlZG3LaLNrBMXQF/lLZ
        UDHs77q3fAGxDWwum2hKBfdBuUQtjlqwjQlgXPsskQKBiQCyp5QmapcTcs/y1igi
        MwgAqJOb2jqmw+VzwKssj0IfRRu5oDYkI4xwI2rxLJhtOqCdaUH1l9wCb9wWkDy1
        hyL2bm9grwc3FCv7wVLdCjw31Enx3RTkKzAPMxh9GCEB9QbCaVaPmGnWlDMC6HBs
        5cW3EodWww+HPUgG0X1jyO+CqBgctubKK7WbAnkAvSlgXQbvHzWmuUBFRHAejRh/
        naQTDV3GnH4lcRHuFBFZCSLn82xQS2/7xFOqfabqq17kNcvKfzdvWpGxxJ2cILAq
        0pZS6DmrZlvBU4IkK2ZHCac/XfWVZFh+PrsH/EnVkDpfcYR/iw1F40C1q5w8R6WB
        Haew3SApAoGIaiodZsrWpi8HFfZfeRs8OS/0L5x6WBl3Y9btoZgsIeruc9uZ8NXT
        IdxaM6FdnyNEyOYA1VH94tDYR+xEt1br1ud/dkPslLV/Aac7d7EaYc7cdkb7oC9t
        6sphVg0dqE0UTDlOwBxBYMtGmQbJsFzGpmjzVgKqWqJ3B947li2U7t63HXEvKprY
        2wJ4b0DzpSMb5p42dcQgOTU8Mr4S6JOEhRr/YjErMkpaXUEqvZ3jEB9HRmcRi5Gt
        t4NBiBMiY6V9br8a5gjEpiAQoIUcWokBMAYjEeurU8M6JLBd3YaZVVjISaFmdtyn
        wLFoQxCh6/EC1rSywwrfDpSwO29S9i8XbaapAoGIPkbARLOwU/LcZrQy9mmfcPoQ
        lAuCyeu1Q9nH7PYSnbHTFzmiud4Hl8bIXU9a0/58blDoOl3PctF+b4rAEJYUpCOD
        u5PFyN6uEFYRg+YQwpjBMkXk8Eb39128ctARB40Lx8caDhRdTyaEedIG3cQDXSpA
        l9EOzXkzfx4bZxjAHU9mkMdJwOcMDQ==
        -----END PRIVATE KEY-----
        """;

    private const string RfcBody = """{"hello": "world"}""";

    private static readonly string[] Covered = ["content-digest", "@method", "@path", "@authority"];

    private static readonly Operation Create = new(
        "create", "POST", "/items", "Items", "CreateAsync", null, [new("body", "body", ParamLocation.Body)], Security: [[new("key", [])]]);

    private static readonly Operation List = new("list", "GET", "/items", "Items", "ListAsync", null, [], Security: [[new("key", [])]]);

    [Fact]
    public void ContentDigestMatchesRfc9530() =>
        Assert.Equal("sha-256=:RK/0qy18MlBSVnWgjwz6lZEWjP/lF5HF9bvEF8FabDg=:", MessageSigner.ContentDigest(Encoding.UTF8.GetBytes(RfcBody + "\n")));

    [Fact]
    public void Ed25519MatchesRfc9421AppendixB26()
    {
        using var signer = new MessageSigner(
            Ed25519Key, ["date", "@method", "@path", "@authority", "content-type", "content-length"], "sig-b26", "test-key-ed25519", clock: new Clock(1618884473));
        var request = Request(
            "POST",
            "https://example.com/foo?param=Value&Pet=dog",
            new() { ["Date"] = "Tue, 20 Apr 2021 02:07:55 GMT", ["Content-Type"] = "application/json", ["Content-Length"] = "18" },
            Encoding.UTF8.GetBytes(RfcBody));

        signer.Sign(request);

        Assert.Equal(MessageSigner.Ed25519, signer.Algorithm);
        Assert.Equal(MessageSigner.ContentDigest(Encoding.UTF8.GetBytes(RfcBody)), request.Headers["content-digest"]);
        Assert.Equal(
            "sig-b26=(\"date\" \"@method\" \"@path\" \"@authority\" \"content-type\" \"content-length\");created=1618884473;keyid=\"test-key-ed25519\"",
            request.Headers["signature-input"]);
        Assert.Equal("sig-b26=:wqcAqbmYJ2ji2glfAMaRy4gruYYnx2nEFN2HN6jrnDnQCK1u02Gb04v9EDgwUPiu4A0w6vuQv5lIp5WPpBKRCw==:", request.Headers["signature"]);
    }

    [Fact]
    public void RsaMatchesRfc9421Section43()
    {
        using var signer = new MessageSigner(
            RsaKey,
            ["@method", "@authority", "@path", "content-digest", "content-type", "content-length", "forwarded"],
            "proxy_sig",
            "test-key-rsa",
            includeAlg: true,
            lifetime: TimeSpan.FromMinutes(1),
            clock: new Clock(1618884480));
        // No body, so the signer keeps the RFC's own SHA-512 digest instead of adding one.
        var request = Request(
            "POST",
            "https://origin.host.internal.example/foo?param=Value&Pet=dog",
            new()
            {
                ["Content-Type"] = "application/json",
                ["Content-Length"] = "18",
                ["Forwarded"] = "for=192.0.2.123;host=example.com;proto=https",
                ["Content-Digest"] = "sha-512=:WZDPaVn/7XgHaAy8pmojAkGWoRx2UFChF41A2svX+TaPm+AbwAgBWnrIiYllu7BNNyealdVLvRwEmTHWXvJwew==:",
            },
            []);

        signer.Sign(request);

        Assert.Equal(MessageSigner.RsaV15Sha256, signer.Algorithm);
        Assert.Equal(
            "proxy_sig=(\"@method\" \"@authority\" \"@path\" \"content-digest\" \"content-type\" \"content-length\" \"forwarded\")" +
            ";created=1618884480;keyid=\"test-key-rsa\";alg=\"rsa-v1_5-sha256\";expires=1618884540",
            request.Headers["signature-input"]);
        Assert.Equal(
            "proxy_sig=:S6ZzPXSdAMOPjN/6KXfXWNO/f7V6cHm7BXYUh3YD/fRad4BCaRZxP+JH+8XY1I6+8Cy+CM5g92iHgxtRPz+MjniOaYmdkDcnL9" +
            "cCpXJleXsOckpURl49GwiyUpZ10KHgOEe11sx3G2gxI8S0jnxQB+Pu68U9vVcasqOWAEObtNKKZd8tSFu7LB5YAv0RAGhB8tmpv7sFnIm9y+7X5" +
            "kXQfi8NMaZaA8i2ZHwpBdg7a6CMfwnnrtflzvZdXAsD3LH2TwevU+/PBPv0B6NMNk93wUs/vfJvye+YuI87HU38lZHowtznbLVdp770I6VHR6Wf" +
            "gS9ddzirrswsE1w5o0LV/g==:",
            request.Headers["signature"]);
    }

    [Fact]
    public async Task EachAttemptIsSignedAgainOverItsOwnBody()
    {
        var (pem, publicKey) = FreshKey();
        var clock = new Clock(1700000000, step: 1);
        using var signer = new MessageSigner(pem, Covered, clock: clock);
        var handler = new Handler(count => count == 1
            ? new HttpResponseMessage(HttpStatusCode.TooManyRequests) { Headers = { { "Retry-After", "0" } } }
            : Ok());
        using var transport = TransportFor(new Signed(signer), handler);

        await transport.CallAsync<JsonElement>(Create, [new Dictionary<string, string> { ["name"] = "synthetic" }], TestContext.Current.CancellationToken);

        Assert.Equal(2, handler.Sent.Count);
        foreach (var (sent, index) in handler.Sent.Select((sent, index) => (sent, index)))
        {
            Assert.Equal(MessageSigner.ContentDigest(sent.Body), sent.Headers["content-digest"]);
            Assert.Equal($"""sig1=("content-digest" "@method" "@path" "@authority");created={1700000001 + index}""", sent.Headers["signature-input"]);
            Verify(publicKey, sent, Covered);
        }
    }

    [Fact]
    public async Task ARequestWithoutABodyHasNoDigest()
    {
        var (pem, publicKey) = FreshKey();
        using var signer = new MessageSigner(pem, Covered, clock: new Clock(1700000000));
        var handler = new Handler(_ => Ok());
        using var transport = TransportFor(new Signed(signer), handler);

        await transport.CallAsync<JsonElement>(List, [], TestContext.Current.CancellationToken);

        var sent = Assert.Single(handler.Sent);
        Assert.False(sent.Headers.ContainsKey("content-digest"));
        Assert.Equal("""sig1=("@method" "@path" "@authority");created=1700000000""", sent.Headers["signature-input"]);
        Verify(publicKey, sent, ["@method", "@path", "@authority"]);
    }

    [Fact]
    public void RejectsUnsupportedKeysAndComponents()
    {
        using var p256 = System.Security.Cryptography.ECDsa.Create(System.Security.Cryptography.ECCurve.NamedCurves.nistP256);
        (string Key, string[] Components)[] invalid =
        [
            (p256.ExportPkcs8PrivateKeyPem(), Covered),
            ("not a key", Covered),
            (Ed25519Key, ["@status"]),
            (Ed25519Key, ["Content-Type"]),
            (Ed25519Key, ["\"@query-param\";name=\"Pet\""]),
        ];
        foreach (var (key, components) in invalid)
        {
            Assert.Throws<ArgumentException>(() => new MessageSigner(key, components));
        }
        using var signer = new MessageSigner(Ed25519Key, ["x-missing"]);
        var error = Assert.Throws<InvalidOperationException>(() => signer.Sign(Request("GET", "https://example.com/", [], [])));
        Assert.Contains("x-missing", error.Message, StringComparison.Ordinal);
    }

    [Fact]
    public void ThePrivateKeyIsASecret()
    {
        using var signer = new MessageSigner(Ed25519Key, Covered);
        const string Body = "MC4CAQAwBQYDK2VwBCIEIJ+DYvh6SEqVTm50DFtMDoQikTmiCqirVv9mWG9qfSnF";
        Assert.DoesNotContain(Body, signer.ToString(), StringComparison.Ordinal);
        Assert.Contains(Ed25519Key, signer.Secrets());
        Assert.Contains(Body, signer.Secrets());
    }

    [Fact]
    public void LifetimeIsWholeSecondsOfAtLeastOne()
    {
        foreach (var lifetime in new[] { TimeSpan.Zero, TimeSpan.FromSeconds(-1), TimeSpan.FromMilliseconds(500), TimeSpan.FromMilliseconds(1500) })
        {
            Assert.Throws<ArgumentException>(() => new MessageSigner(Ed25519Key, Covered, lifetime: lifetime));
        }
        using var signer = new MessageSigner(Ed25519Key, ["@method"], lifetime: TimeSpan.FromSeconds(1), clock: new Clock(1700000000));
        var request = Request("GET", "https://example.com/", [], []);

        signer.Sign(request);

        Assert.Equal("""sig1=("@method");created=1700000000;expires=1700000001""", request.Headers["signature-input"]);
    }

    [Fact]
    public void ContentLengthAndHostComeFromTheBodyAndUrlWhenAbsent()
    {
        var (pem, publicKey) = FreshKey();
        using var signer = new MessageSigner(pem, ["content-length", "host"]);
        var request = Request("POST", "https://Example.com:443/items", [], Encoding.UTF8.GetBytes("synthetic"));

        signer.Sign(request);

        Assert.False(request.Headers.ContainsKey("content-length"));
        Assert.False(request.Headers.ContainsKey("host"));
        VerifyBase(publicKey, request, ["\"content-length\": 9", "\"host\": example.com"]);
        var given = Request("POST", "https://example.com/items", new() { ["Content-Length"] = "18", ["Host"] = "proxy.example" }, []);
        signer.Sign(given);
        VerifyBase(publicKey, given, ["\"content-length\": 18", "\"host\": proxy.example"]);
        var error = Assert.Throws<InvalidOperationException>(() => signer.Sign(Request("GET", "https://example.com/items", [], [])));
        Assert.Contains("content-length", error.Message, StringComparison.Ordinal);
    }

    [Theory]
    [InlineData("POST")]
    [InlineData("PUT")]
    public void APostOrPutWithoutABodySignsAZeroContentLength(string method)
    {
        var (pem, publicKey) = FreshKey();
        using var signer = new MessageSigner(pem, ["content-length"]);
        var request = Request(method, "https://example.com/items", [], []);

        signer.Sign(request);

        Assert.False(request.Headers.ContainsKey("content-length"));
        VerifyBase(publicKey, request, ["\"content-length\": 0"]);
    }

    [Theory]
    [InlineData("POST")]
    [InlineData("PUT")]
    public async Task APostOrPutWithoutABodySendsTheZeroContentLengthItSigns(string method)
    {
        var (pem, publicKey) = FreshKey();
        using var signer = new MessageSigner(pem, ["content-length", "@method"], clock: new Clock(1700000000));
        await using var server = new ConnectionTests.LoopbackServer("HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: 2\r\n\r\n{}");
        var settings = new Settings
        {
            BaseUrl = server.Url.ToString().TrimEnd('/'),
            Credentials = new Signed(signer),
            Headers = new Dictionary<string, string> { ["User-Agent"] = "test" },
            ToError = context => new ApiException($"status {context.Status}") { Status = context.Status },
            Logger = Microsoft.Extensions.Logging.Abstractions.NullLogger.Instance,
            MaxRetries = 0,
        };
        using var transport = new Transport(settings, new HttpClient(), ownsClient: true);
        var operation = new Operation("touch", method, "/items", "Items", "TouchAsync", null, [], Security: [[new("key", [])]]);

        await transport.CallAsync<JsonElement>(operation, [], TestContext.Current.CancellationToken);

        var headers = Assert.Single(server.Requests).Head.Split("\r\n").Skip(1).Where(line => line.Length > 0)
            .Select(line => line.Split(':', 2))
            .ToDictionary(field => field[0], field => field[1].Trim(), StringComparer.OrdinalIgnoreCase);
        Assert.Equal("0", headers["content-length"]);
        VerifyBase(publicKey, Request(method, server.Url.ToString(), headers, []), ["\"content-length\": 0", $"\"@method\": {method}"]);
    }

    [Theory]
    [InlineData("GET")]
    [InlineData("DELETE")]
    [InlineData("PATCH")]
    public void OtherMethodsWithoutABodyHaveNoContentLengthToSign(string method)
    {
        var (pem, _) = FreshKey();
        using var signer = new MessageSigner(pem, ["content-length"]);
        var error = Assert.Throws<InvalidOperationException>(() => signer.Sign(Request(method, "https://example.com/items", [], [])));
        Assert.Contains("content-length", error.Message, StringComparison.Ordinal);
    }

    [Fact]
    public void AnEmptyQueryIsNoQuery()
    {
        var (pem, publicKey) = FreshKey();
        using var signer = new MessageSigner(pem, ["@request-target", "@query"]);
        var request = Request("GET", "https://example.com/p?", [], []);

        signer.Sign(request);

        VerifyBase(publicKey, request, ["\"@request-target\": /p", "\"@query\": ?"]);
    }

    [Fact]
    public void RejectsAFieldThatIsNotAscii()
    {
        using var signer = new MessageSigner(Ed25519Key, ["x-note"]);
        var request = Request("GET", "https://example.com/", new() { ["X-Note"] = "café" }, []);

        Assert.Throws<InvalidOperationException>(() => signer.Sign(request));
        Assert.False(request.Headers.ContainsKey("signature"));
    }

    [Fact]
    public void EachLineOfTheKeyBodyIsASecret()
    {
        using var signer = new MessageSigner(RsaKey, Covered);
        var lines = RsaKey.Trim().Split('\n')[1..^1];

        Assert.All(lines, line => Assert.Contains(line.Trim(), signer.Secrets()));
    }

    private static void VerifyBase(Ed25519PublicKeyParameters publicKey, AuthRequest request, string[] lines)
    {
        var input = request.Headers["signature-input"];
        var signatureBase = string.Join('\n', lines.Append($"\"@signature-params\": {input["sig1=".Length..]}"));
        var signature = Convert.FromBase64String(request.Headers["signature"]["sig1=:".Length..^1]);
        var verifier = new Ed25519Signer();
        verifier.Init(false, publicKey);
        var data = Encoding.ASCII.GetBytes(signatureBase);
        verifier.BlockUpdate(data, 0, data.Length);
        Assert.True(verifier.VerifySignature(signature), signatureBase);
    }

    private static AuthRequest Request(string method, string url, Dictionary<string, string> headers, byte[] body) => new()
    {
        Method = method,
        Url = new Uri(url),
        Headers = new Dictionary<string, string>(headers, StringComparer.OrdinalIgnoreCase),
        Body = body,
        Operation = Create,
    };

    private static (string Pem, Ed25519PublicKeyParameters PublicKey) FreshKey()
    {
        var generator = new Ed25519KeyPairGenerator();
        generator.Init(new Ed25519KeyGenerationParameters(new SecureRandom()));
        var pair = generator.GenerateKeyPair();
        var der = PrivateKeyInfoFactory.CreatePrivateKeyInfo(pair.Private).GetEncoded();
        var pem = new string(System.Security.Cryptography.PemEncoding.Write("PRIVATE KEY", der));
        return (pem, (Ed25519PublicKeyParameters)pair.Public);
    }

    private static void Verify(Ed25519PublicKeyParameters publicKey, Sent sent, string[] components)
    {
        var input = sent.Headers["signature-input"];
        var label = input[..input.IndexOf('=', StringComparison.Ordinal)];
        var values = new Dictionary<string, string>
        {
            ["content-digest"] = sent.Headers.GetValueOrDefault("content-digest", ""),
            ["@method"] = sent.Method,
            ["@path"] = sent.Url.AbsolutePath,
            ["@authority"] = sent.Url.Authority,
        };
        var signatureBase = string.Concat(components.Select(name => $"\"{name}\": {values[name]}\n")) + $"\"@signature-params\": {input[(label.Length + 1)..]}";
        var signature = Convert.FromBase64String(sent.Headers["signature"][(label.Length + 2)..^1]);
        var verifier = new Ed25519Signer();
        verifier.Init(false, publicKey);
        var data = Encoding.ASCII.GetBytes(signatureBase);
        verifier.BlockUpdate(data, 0, data.Length);
        Assert.True(verifier.VerifySignature(signature), signatureBase);
    }

    private static Transport TransportFor(ICredentialProvider credentials, Handler handler) =>
        new(
            new Settings
            {
                BaseUrl = "https://mock.invalid/v1",
                Credentials = credentials,
                Headers = new Dictionary<string, string> { ["User-Agent"] = "test" },
                ToError = context => new ApiException($"status {context.Status}") { Status = context.Status },
                Logger = Microsoft.Extensions.Logging.Abstractions.NullLogger.Instance,
                MaxRetries = 1,
                RetryBaseDelay = TimeSpan.FromMilliseconds(1),
            },
            new HttpClient(handler),
            ownsClient: true);

    private static HttpResponseMessage Ok() => new(HttpStatusCode.OK) { Content = new StringContent("""{"id": 1}""", Encoding.UTF8, "application/json") };

    private sealed class Signed(MessageSigner signer) : ICredentialProvider
    {
        public ValueTask ApplyAsync(AuthRequest request, CancellationToken cancellationToken)
        {
            request.Headers["Authorization"] = "Bearer synthetic-token";
            signer.Sign(request);
            return ValueTask.CompletedTask;
        }

        public IReadOnlyCollection<string> Secrets() => ["synthetic-token", .. signer.Secrets()];
    }

    private sealed class Clock(long seconds, long step = 0) : TimeProvider
    {
        private long now = seconds;

        public override DateTimeOffset GetUtcNow() => DateTimeOffset.FromUnixTimeSeconds(Interlocked.Add(ref now, step));
    }

    private sealed record Sent(string Method, Uri Url, Dictionary<string, string> Headers, byte[] Body);

    private sealed class Handler(Func<int, HttpResponseMessage> respond) : HttpMessageHandler
    {
        public ConcurrentQueue<Sent> Sent { get; } = new();

        protected override async Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
        {
            var headers = request.Headers.NonValidated.ToDictionary(header => header.Key, header => header.Value.ToString(), StringComparer.OrdinalIgnoreCase);
            var body = request.Content is null ? [] : await request.Content.ReadAsByteArrayAsync(cancellationToken);
            foreach (var header in request.Content?.Headers.NonValidated.ToArray() ?? [])
            {
                headers[header.Key] = header.Value.ToString();
            }
            Sent.Enqueue(new Sent(request.Method.Method, request.RequestUri!, headers, body));
            return respond(Sent.Count);
        }
    }
}
