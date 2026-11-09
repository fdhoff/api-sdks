package runtime

import (
	"encoding/json"
	"errors"
	"os"
	"strings"
	"testing"
	"time"
)

// The shared vectors, read from the repository: this file runs from internal/runtime in each Go
// package.
const webhookVectors = "../../../../../../toolchain/conformance/fixtures/webhooks/hmac-sha256.json"

type webhookCase struct {
	Name      string  `json:"name"`
	Header    string  `json:"header"`
	Body      string  `json:"body"`
	Now       int64   `json:"now"`
	Tolerance any     `json:"tolerance"`
	Error     *string `json:"error"`
}

func readWebhookVectors(t *testing.T) (string, []webhookCase) {
	t.Helper()
	raw, err := os.ReadFile(webhookVectors)
	if err != nil {
		t.Fatal(err)
	}
	var vectors struct {
		Secret string        `json:"secret"`
		Cases  []webhookCase `json:"cases"`
	}
	if err := json.Unmarshal(raw, &vectors); err != nil {
		t.Fatal(err)
	}
	return vectors.Secret, vectors.Cases
}

func TestVerifyWebhookVectors(t *testing.T) {
	secret, cases := readWebhookVectors(t)
	reasons := map[string]error{
		"malformed_header":  ErrWebhookMalformedHeader,
		"too_old":           ErrWebhookTooOld,
		"bad_signature":     ErrWebhookBadSignature,
		"invalid_tolerance": ErrWebhookInvalidTolerance,
	}
	for _, c := range cases {
		t.Run(c.Name, func(t *testing.T) {
			options := []WebhookOption{WithWebhookNow(time.Unix(c.Now, 0))}
			switch tolerance := c.Tolerance.(type) {
			case nil:
			case float64:
				options = append(options, WithWebhookTolerance(time.Duration(tolerance)*time.Second))
			default:
				t.Skip("a time.Duration cannot hold NaN or infinity")
			}
			err := VerifyWebhook([]byte(c.Body), c.Header, secret, options...)
			if c.Error == nil {
				if err != nil {
					t.Fatalf("got %v, want no error", err)
				}
				return
			}
			if !errors.Is(err, reasons[*c.Error]) {
				t.Fatalf("got %v, want %v", err, reasons[*c.Error])
			}
			if strings.Contains(err.Error(), secret) || strings.Contains(err.Error(), c.Body) {
				t.Fatalf("the error shows the secret or the body: %v", err)
			}
		})
	}
}

func TestVerifyWebhookDefaults(t *testing.T) {
	secret, cases := readWebhookVectors(t)
	c := cases[0]
	if err := VerifyWebhook([]byte(c.Body), c.Header, secret); !errors.Is(err, ErrWebhookTooOld) {
		t.Fatalf("got %v, want %v", err, ErrWebhookTooOld)
	}
}
