using System.Text;
using System.Text.Json;
using Xunit;

namespace MercuryBanking.Tests;

public sealed class WebhookTests
{
    private static readonly string[] Files = ["mercury-signature.json", "hmac-sha256.json"];

    private static JsonElement Vectors(string file) =>
        JsonDocument.Parse(File.ReadAllText(Path.Combine(AppContext.BaseDirectory, "webhooks", file))).RootElement;

    public static TheoryData<string, string> Cases()
    {
        var cases = new TheoryData<string, string>();
        foreach (var file in Files)
        {
            foreach (var vector in Vectors(file).GetProperty("cases").EnumerateArray())
            {
                cases.Add(file, vector.GetProperty("name").GetString()!);
            }
        }
        return cases;
    }

    [Theory]
    [MemberData(nameof(Cases))]
    public void PassesTheVector(string file, string name)
    {
        var vectors = Vectors(file);
        var secret = vectors.GetProperty("secret").GetString()!;
        var vector = vectors.GetProperty("cases").EnumerateArray().Single(c => c.GetProperty("name").GetString() == name);
        var body = vector.GetProperty("body").GetString()!;
        TimeSpan? tolerance = null;
        if (vector.TryGetProperty("tolerance", out var seconds))
        {
            if (seconds.ValueKind != JsonValueKind.Number)
            {
                Assert.Skip("A TimeSpan cannot hold NaN or infinity.");
            }

            tolerance = TimeSpan.FromSeconds(seconds.GetInt64());
        }

        var now = DateTimeOffset.FromUnixTimeSeconds(vector.GetProperty("now").GetInt64());
        void Verify() => MercuryWebhooks.Verify(Encoding.UTF8.GetBytes(body), vector.GetProperty("header").GetString(), secret, tolerance, now);

        var error = vector.GetProperty("error");
        if (error.ValueKind == JsonValueKind.Null)
        {
            Verify();
            return;
        }

        var thrown = Assert.Throws<WebhookSignatureException>(Verify);
        Assert.Equal(error.GetString()!.Replace("_", string.Empty), thrown.Reason.ToString(), ignoreCase: true);
        Assert.DoesNotContain(secret, thrown.Message);
        Assert.DoesNotContain(body, thrown.Message);
    }

    [Fact]
    public void TheHeaderIsMercurySignature() => Assert.Equal(MercuryWebhooks.SignatureHeader, Vectors(Files[0]).GetProperty("header_name").GetString());

    [Fact]
    public void DefaultsToTheClockAndFiveMinutes()
    {
        var vectors = Vectors(Files[0]);
        var valid = vectors.GetProperty("cases")[0];
        var thrown = Assert.Throws<WebhookSignatureException>(() => MercuryWebhooks.Verify(Encoding.UTF8.GetBytes(valid.GetProperty("body").GetString()!), valid.GetProperty("header").GetString(), vectors.GetProperty("secret").GetString()!));
        Assert.Equal(WebhookFailure.TooOld, thrown.Reason);
    }
}
