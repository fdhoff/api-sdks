package etsyseller

import (
	"fmt"
	"slices"
	"testing"
)

func TestCredentialsKeepCurrentTokensAndOnlyRecentValuesForRedaction(t *testing.T) {
	credentials := newCredentials("synthetic-keystring", "synthetic-shared-secret", "12345678.synthetic-access", "12345678.synthetic-refresh", nil)
	for index := range 100 {
		credentials.remember(fmt.Sprintf("synthetic-old-%d", index))
	}
	secrets := credentials.Secrets()
	if len(secrets) >= 25 {
		t.Errorf("kept %d secrets", len(secrets))
	}
	for _, value := range []string{"synthetic-keystring", "synthetic-shared-secret", "12345678.synthetic-access", "12345678.synthetic-refresh", "synthetic-old-99"} {
		if !slices.Contains(secrets, value) {
			t.Errorf("%q is not redacted", value)
		}
	}
	if slices.Contains(secrets, "synthetic-old-0") {
		t.Error("kept the oldest value")
	}
}
