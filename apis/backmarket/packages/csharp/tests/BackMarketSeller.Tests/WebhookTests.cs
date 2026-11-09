using System.Text;
using System.Text.Json;
using Xunit;

namespace BackMarketSeller.Tests;

public sealed class WebhookTests
{
    private static readonly JsonElement Vectors = JsonDocument.Parse(File.ReadAllText(Path.Combine(AppContext.BaseDirectory, "webhooks", "hmac-sha256.json"))).RootElement;
    private static readonly string Secret = Vectors.GetProperty("secret").GetString()!;
    private static readonly JsonElement Valid = Vectors.GetProperty("cases")[0];

    public static TheoryData<string> Names() => new(Vectors.GetProperty("cases").EnumerateArray().Select(c => c.GetProperty("name").GetString()!));

    [Theory]
    [MemberData(nameof(Names))]
    public void PassesTheSharedVector(string name)
    {
        var vector = Vectors.GetProperty("cases").EnumerateArray().Single(c => c.GetProperty("name").GetString() == name);
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
        void Verify() => WebhookVerifier.Verify(Encoding.UTF8.GetBytes(body), vector.GetProperty("header").GetString(), Secret, tolerance, now);

        var error = vector.GetProperty("error");
        if (error.ValueKind == JsonValueKind.Null)
        {
            Verify();
            return;
        }

        var thrown = Assert.Throws<WebhookSignatureException>(Verify);
        Assert.Equal(error.GetString()!.Replace("_", string.Empty), thrown.Reason.ToString(), ignoreCase: true);
        Assert.DoesNotContain(Secret, thrown.Message);
        Assert.DoesNotContain(body, thrown.Message);
    }

    [Fact]
    public void DefaultsToTheClockAndFiveMinutes()
    {
        var thrown = Assert.Throws<WebhookSignatureException>(() => WebhookVerifier.Verify(Encoding.UTF8.GetBytes(Valid.GetProperty("body").GetString()!), Valid.GetProperty("header").GetString(), Secret));
        Assert.Equal(WebhookFailure.TooOld, thrown.Reason);
    }

    [Fact]
    public void AMissingHeaderIsMalformed()
    {
        var thrown = Assert.Throws<WebhookSignatureException>(() => WebhookVerifier.Verify("{}"u8, null, Secret));
        Assert.Equal(WebhookFailure.MalformedHeader, thrown.Reason);
    }
}
