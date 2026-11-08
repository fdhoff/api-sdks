package ebaysell

import (
	"fmt"
	"slices"
	"testing"
)

func TestCredentialsKeepCurrentTokensAndOnlyRecentValuesForRedaction(t *testing.T) {
	credentials, err := newCredentials(options{
		clientID: "synthetic-app-id", clientSecret: "synthetic-cert-id",
		appToken: "synthetic-app-token", userToken: "synthetic-user-token", refreshToken: "synthetic-refresh-token",
	})
	if err != nil {
		t.Fatal(err)
	}
	for index := range 100 {
		credentials.remember(fmt.Sprintf("synthetic-old-%d", index))
	}
	secrets := credentials.Secrets()
	if len(secrets) >= 25 {
		t.Errorf("kept %d secrets", len(secrets))
	}
	for _, value := range []string{credentials.basic, "synthetic-cert-id", "synthetic-app-token", "synthetic-user-token", "synthetic-refresh-token", "synthetic-old-99"} {
		if !slices.Contains(secrets, value) {
			t.Errorf("%q is not redacted", value)
		}
	}
	if slices.Contains(secrets, "synthetic-old-0") {
		t.Error("kept the oldest value")
	}
}
