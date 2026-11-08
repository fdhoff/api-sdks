package runtime

import (
	"context"
	"errors"
	"net/url"
	"strings"
	"testing"
	"time"
)

func TestARequestThatCannotBeBuiltDoesNotShowTheTokenEvenEscaped(t *testing.T) {
	const secret = "synthetic/test+token="
	transport := NewTransport(Settings{BaseURL: "http://example.invalid\x7f", Secret: secret, Timeout: time.Second})
	operation := &Operation{ID: "op", Method: "GET", Path: "/items/{id}", PathParams: []string{"id"}}
	_, err := Call[any](context.Background(), transport, operation, Input{Path: []any{secret}})
	var failure *Error
	if !errors.As(err, &failure) || failure.Kind != KindConnection || !strings.HasPrefix(err.Error(), "the request could not be built: ") {
		t.Fatalf("error is %v", err)
	}
	for _, form := range []string{secret, url.PathEscape(secret)} {
		if strings.Contains(err.Error(), form) {
			t.Errorf("error shows %q: %q", form, err.Error())
		}
	}
	var parse *url.Error
	if !errors.As(err, &parse) {
		t.Errorf("error does not unwrap to its cause: %v", err)
	}
}
