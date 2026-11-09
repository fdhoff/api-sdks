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
	ErrWebhookMalformedHeader = errors.New("the webhook signature header is malformed")
	ErrWebhookTooOld          = errors.New("the webhook timestamp is older than the tolerance")
	ErrWebhookBadSignature    = errors.New("no webhook signature matches the body")
)

var (
	webhookTimestamp = regexp.MustCompile(`^[0-9]{1,12}$`)
	webhookSignature = regexp.MustCompile(`^[0-9a-fA-F]{64}$`)
)

// WebhookOptions configures [VerifyWebhook]. A zero Tolerance is [DefaultWebhookTolerance], and a
// zero Now is the clock.
type WebhookOptions struct {
	Tolerance time.Duration
	Now       time.Time
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
// rotates. It returns [ErrWebhookMalformedHeader], [ErrWebhookTooOld] or [ErrWebhookBadSignature].
func VerifyWebhook(payload []byte, header, secret string, options WebhookOptions) error {
	if options.Tolerance < 0 {
		return errors.New("the webhook tolerance must not be negative")
	}
	tolerance := options.Tolerance
	if tolerance == 0 {
		tolerance = DefaultWebhookTolerance
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
	now := options.Now
	if now.IsZero() {
		now = time.Now()
	}
	if now.Sub(time.Unix(seconds, 0)) > tolerance {
		return ErrWebhookTooOld
	}
	return nil
}
