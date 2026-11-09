package mercurybanking

import (
	"time"

	"github.com/fdhoff/api-sdks/apis/mercury/packages/go/internal/runtime"
)

// SignatureHeader is the request header that carries a webhook's signature.
const SignatureHeader = "Mercury-Signature"

// DefaultWebhookTolerance is the oldest webhook timestamp [VerifyWebhook] accepts by default.
const DefaultWebhookTolerance = runtime.DefaultWebhookTolerance

// The reasons [VerifyWebhook] fails, for [errors.Is]. None of them holds the secret or the body.
var (
	ErrWebhookMalformedHeader  = runtime.ErrWebhookMalformedHeader
	ErrWebhookTooOld           = runtime.ErrWebhookTooOld
	ErrWebhookBadSignature     = runtime.ErrWebhookBadSignature
	ErrWebhookInvalidTolerance = runtime.ErrWebhookInvalidTolerance
)

// WebhookOption configures [VerifyWebhook].
type WebhookOption = runtime.WebhookOption

// WithWebhookTolerance sets the oldest timestamp to accept, which must be greater than zero. The
// default is [DefaultWebhookTolerance].
func WithWebhookTolerance(tolerance time.Duration) WebhookOption {
	return runtime.WithWebhookTolerance(tolerance)
}

// WithWebhookNow sets the time to check the timestamp against, for tests. The default is the clock.
func WithWebhookNow(now time.Time) WebhookOption { return runtime.WithWebhookNow(now) }

// VerifyWebhook checks that a webhook came from Mercury. Pass the raw body exactly as it arrived,
// the value of the [SignatureHeader] header, and the endpoint's secret. Mercury's sandbox sends no
// webhooks, so this is the way to test a handler. A header may carry several signatures while a
// secret rotates; any one that matches is enough.
func VerifyWebhook(payload []byte, header, secret string, opts ...WebhookOption) error {
	return runtime.VerifyWebhook(payload, header, secret, opts...)
}
