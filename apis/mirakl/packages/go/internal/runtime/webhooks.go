package runtime

import (
	"crypto/hmac"
	"crypto/sha256"
	"encoding/hex"
	"errors"
	"regexp"
	"strconv"
	"strings"
	"time"
)

// DefaultWebhookTolerance is the oldest webhook timestamp [VerifyWebhook] accepts by default.
const DefaultWebhookTolerance = 5 * time.Minute

// The reasons [VerifyWebhook] fails. None of them holds the secret or the body.
var (
	ErrWebhookMalformedHeader  = errors.New("the webhook signature header is malformed")
	ErrWebhookTooOld           = errors.New("the webhook timestamp is older than the tolerance")
	ErrWebhookBadSignature     = errors.New("no webhook signature matches the body")
	ErrWebhookInvalidTolerance = errors.New("the webhook tolerance must be greater than zero")
)

var (
	webhookTimestamp = regexp.MustCompile(`^[0-9]{1,12}$`)
	webhookSignature = regexp.MustCompile(`^[0-9a-fA-F]{64}$`)
)

type webhookOptions struct {
	tolerance time.Duration
	now       time.Time
}

// WebhookOption configures [VerifyWebhook].
type WebhookOption func(*webhookOptions)

// WithWebhookTolerance sets the oldest timestamp to accept, which must be greater than zero. The
// default is [DefaultWebhookTolerance].
func WithWebhookTolerance(tolerance time.Duration) WebhookOption {
	return func(o *webhookOptions) { o.tolerance = tolerance }
}

// WithWebhookNow sets the time to check against, for tests. The default is the clock.
func WithWebhookNow(now time.Time) WebhookOption {
	return func(o *webhookOptions) { o.now = now }
}

func parseWebhookHeader(header string) (string, []string, error) {
	var timestamp string
	var signatures []string
	for _, entry := range strings.Split(header, ",") {
		key, value, found := strings.Cut(strings.Trim(entry, " \t"), "=")
		if !found {
			return "", nil, ErrWebhookMalformedHeader
		}
		switch key {
		case "t":
			if timestamp != "" || !webhookTimestamp.MatchString(value) {
				return "", nil, ErrWebhookMalformedHeader
			}
			timestamp = value
		case "v1":
			signatures = append(signatures, value)
		}
	}
	if timestamp == "" || len(signatures) == 0 {
		return "", nil, ErrWebhookMalformedHeader
	}
	return timestamp, signatures, nil
}

// VerifyWebhook checks a webhook's timestamped HMAC-SHA256 signature header, t=<unix
// seconds>,v1=<hex> signed over <t>.<raw body>, against the raw body as received, never
// re-serialised. Any one matching v1 value is enough, so a header may carry several while a secret
// rotates. It returns [ErrWebhookInvalidTolerance], [ErrWebhookMalformedHeader], [ErrWebhookTooOld]
// or [ErrWebhookBadSignature].
func VerifyWebhook(payload []byte, header, secret string, opts ...WebhookOption) error {
	options := webhookOptions{tolerance: DefaultWebhookTolerance}
	for _, option := range opts {
		option(&options)
	}
	if options.tolerance <= 0 {
		return ErrWebhookInvalidTolerance
	}
	timestamp, signatures, err := parseWebhookHeader(header)
	if err != nil {
		return err
	}
	mac := hmac.New(sha256.New, []byte(secret))
	mac.Write([]byte(timestamp + "."))
	mac.Write(payload)
	expected := mac.Sum(nil)
	matched := false
	for _, signature := range signatures {
		if webhookSignature.MatchString(signature) {
			decoded, _ := hex.DecodeString(signature)
			matched = hmac.Equal(decoded, expected) || matched
		}
	}
	if !matched {
		return ErrWebhookBadSignature
	}
	seconds, _ := strconv.ParseInt(timestamp, 10, 64)
	now := options.now
	if now.IsZero() {
		now = time.Now()
	}
	if now.Sub(time.Unix(seconds, 0)) > options.tolerance {
		return ErrWebhookTooOld
	}
	return nil
}
