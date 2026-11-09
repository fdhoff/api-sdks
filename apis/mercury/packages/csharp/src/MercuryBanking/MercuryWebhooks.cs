namespace MercuryBanking;

/// <summary>Checks that a webhook came from Mercury.</summary>
public static class MercuryWebhooks
{
    /// <summary>The request header that carries a webhook's signature.</summary>
    public const string SignatureHeader = "Mercury-Signature";

    /// <summary>
    /// Checks a webhook's <see cref="SignatureHeader"/> value against its raw body, exactly as it arrived, and the
    /// endpoint's secret. Mercury's sandbox sends no webhooks, so this is the way to test a handler. A header may carry
    /// several signatures while a secret rotates; any one that matches is enough.
    /// </summary>
    /// <param name="payload">The raw request body, never re-serialised.</param>
    /// <param name="header">The <see cref="SignatureHeader"/> value.</param>
    /// <param name="secret">The endpoint's secret.</param>
    /// <param name="tolerance">The oldest timestamp to accept, greater than zero, by default <see cref="WebhookVerifier.DefaultTolerance"/>.</param>
    /// <param name="now">The time to check against, for tests. By default the clock.</param>
    /// <exception cref="WebhookSignatureException">The tolerance is invalid, or the header is malformed, too old or matches no signature.</exception>
    public static void Verify(ReadOnlySpan<byte> payload, string? header, string secret, TimeSpan? tolerance = null, DateTimeOffset? now = null) =>
        WebhookVerifier.Verify(payload, header, secret, tolerance, now);
}
