package runtime

import (
	"context"
	"crypto/ecdsa"
	"crypto/ed25519"
	"crypto/elliptic"
	"crypto/rand"
	"crypto/x509"
	"encoding/base64"
	"encoding/pem"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"slices"
	"strings"
	"sync"
	"sync/atomic"
	"testing"
	"time"
)

// The published test keys of RFC 9421, Appendix B.1.4 and B.1.1. The RSA key is re-encoded from
// PKCS #1 to PKCS #8.
const (
	rfcEd25519Key = `-----BEGIN PRIVATE KEY-----
MC4CAQAwBQYDK2VwBCIEIJ+DYvh6SEqVTm50DFtMDoQikTmiCqirVv9mWG9qfSnF
-----END PRIVATE KEY-----
`
	rfcRSAKey = `-----BEGIN PRIVATE KEY-----
MIIEwgIBADANBgkqhkiG9w0BAQEFAASCBKwwggSoAgEAAoIBAQCEAph22h6jLzNw
BxHzvgvxydnErMAbB3u/foA+ns+/pDaN2w8FGvBYQGd7Pp3RQMoPAZtzqfF8RcDL
mZuGBqPOvDcw4S3y4Dm3FIqhsGkoN4Es6x0koWowaZcJC8Qbth6ZzENNE/ECV4gC
BhhGNNJ39AHBVb07A0WF6SujdG2WKdXRrvmN9mCSd79iKS1K8sbfiXDbOpcENMLk
0dE5SoZOUwvg+U1lLlGLZThoI3HatQ9FwoiUTQ+4rEjhP4choWm/z6t1Xp5SA6sH
bF4jV1IUWf+ee/k6hkkQgH5Wa4qfcMJRwJlIWVA9JdJ8EOJQaHA7Dvpa5JKx/UPh
v+8ugnXTAgMBAAECggEAb8lm5JZ2hUduLnq+OAKCSODeWQ7Uqs7eet2bqeuAD0/2
po+PG4qhZoo7VwFCUTWlJan9wqdxiAPlbEQKkCdFRcbakbjN2TMJjMCHWL5zfgvq
hmgeyKsrqg1wSce97J1/Mkvn3fh6CbqnwNb6bVFDvTJS3i5FzRhKiv6rUsYm8ZAd
F4XRaYkFkeuHPl7rc+ruUTSAjC4GovxIxoDJFe0r4kbFmkiZOr40e8RZYK7T1IKr
Svzfxx5AjnlK/OZOTCq0L7wBPbMW+IxmQpFCjpI+yuoi3FlZG3LaLNrBMXQF/lLZ
UDHs77q3fAGxDWwum2hKBfdBuUQtjlqwjQlgXPsskQKBiQCyp5QmapcTcs/y1igi
MwgAqJOb2jqmw+VzwKssj0IfRRu5oDYkI4xwI2rxLJhtOqCdaUH1l9wCb9wWkDy1
hyL2bm9grwc3FCv7wVLdCjw31Enx3RTkKzAPMxh9GCEB9QbCaVaPmGnWlDMC6HBs
5cW3EodWww+HPUgG0X1jyO+CqBgctubKK7WbAnkAvSlgXQbvHzWmuUBFRHAejRh/
naQTDV3GnH4lcRHuFBFZCSLn82xQS2/7xFOqfabqq17kNcvKfzdvWpGxxJ2cILAq
0pZS6DmrZlvBU4IkK2ZHCac/XfWVZFh+PrsH/EnVkDpfcYR/iw1F40C1q5w8R6WB
Haew3SApAoGIaiodZsrWpi8HFfZfeRs8OS/0L5x6WBl3Y9btoZgsIeruc9uZ8NXT
IdxaM6FdnyNEyOYA1VH94tDYR+xEt1br1ud/dkPslLV/Aac7d7EaYc7cdkb7oC9t
6sphVg0dqE0UTDlOwBxBYMtGmQbJsFzGpmjzVgKqWqJ3B947li2U7t63HXEvKprY
2wJ4b0DzpSMb5p42dcQgOTU8Mr4S6JOEhRr/YjErMkpaXUEqvZ3jEB9HRmcRi5Gt
t4NBiBMiY6V9br8a5gjEpiAQoIUcWokBMAYjEeurU8M6JLBd3YaZVVjISaFmdtyn
wLFoQxCh6/EC1rSywwrfDpSwO29S9i8XbaapAoGIPkbARLOwU/LcZrQy9mmfcPoQ
lAuCyeu1Q9nH7PYSnbHTFzmiud4Hl8bIXU9a0/58blDoOl3PctF+b4rAEJYUpCOD
u5PFyN6uEFYRg+YQwpjBMkXk8Eb39128ctARB40Lx8caDhRdTyaEedIG3cQDXSpA
l9EOzXkzfx4bZxjAHU9mkMdJwOcMDQ==
-----END PRIVATE KEY-----
`
	rfcBody = `{"hello": "world"}`
)

var signedComponents = []string{"content-digest", "@method", "@path", "@authority"}

func pkcs8PEM(t *testing.T, key any) string {
	t.Helper()
	der, err := x509.MarshalPKCS8PrivateKey(key)
	if err != nil {
		t.Fatal(err)
	}
	return string(pem.EncodeToMemory(&pem.Block{Type: "PRIVATE KEY", Bytes: der}))
}

func fixedClock(seconds int64) func() time.Time {
	return func() time.Time { return time.Unix(seconds, 0) }
}

func mustSigner(t *testing.T, options SignerOptions) *MessageSigner {
	t.Helper()
	signer, err := NewMessageSigner(options)
	if err != nil {
		t.Fatal(err)
	}
	return signer
}

// signed adds a synthetic bearer token, then signs.
type signed struct{ signer *MessageSigner }

func (c signed) Apply(_ context.Context, request *AuthRequest) error {
	request.Header.Set("Authorization", "Bearer synthetic-token")
	return c.signer.Sign(request)
}

func (c signed) Secrets() []string { return append([]string{"synthetic-token"}, c.signer.Secrets()...) }

type received struct {
	method string
	url    *url.URL
	host   string
	header http.Header
	body   []byte
}

func verifyReceived(t *testing.T, public ed25519.PublicKey, request received, components []string) {
	t.Helper()
	label, params, _ := strings.Cut(request.header.Get("Signature-Input"), "=")
	values := map[string]string{
		"content-digest": request.header.Get("Content-Digest"),
		"@method":        request.method,
		"@path":          request.url.EscapedPath(),
		"@authority":     request.host,
	}
	var base strings.Builder
	for _, name := range components {
		fmt.Fprintf(&base, "%q: %s\n", name, values[name])
	}
	base.WriteString(`"@signature-params": ` + params)
	signature, err := base64.StdEncoding.DecodeString(strings.TrimSuffix(strings.TrimPrefix(request.header.Get("Signature"), label+"=:"), ":"))
	if err != nil || !ed25519.Verify(public, []byte(base.String()), signature) {
		t.Errorf("the signature does not verify over %q", base.String())
	}
}

func TestContentDigestMatchesRFC9530(t *testing.T) {
	if got := ContentDigest([]byte(rfcBody + "\n")); got != "sha-256=:RK/0qy18MlBSVnWgjwz6lZEWjP/lF5HF9bvEF8FabDg=:" {
		t.Errorf("got %s", got)
	}
}

func TestEd25519MatchesRFC9421AppendixB26(t *testing.T) {
	signer := mustSigner(t, SignerOptions{
		PrivateKey: rfcEd25519Key,
		Components: []string{"date", "@method", "@path", "@authority", "content-type", "content-length"},
		Label:      "sig-b26",
		KeyID:      "test-key-ed25519",
		Now:        fixedClock(1618884473),
	})
	request := &AuthRequest{
		Method: "POST",
		URL:    "https://example.com/foo?param=Value&Pet=dog",
		Header: http.Header{"Date": {"Tue, 20 Apr 2021 02:07:55 GMT"}, "Content-Type": {"application/json"}, "Content-Length": {"18"}},
		Body:   []byte(rfcBody),
	}
	if err := signer.Sign(request); err != nil {
		t.Fatal(err)
	}
	if signer.Algorithm() != AlgorithmEd25519 {
		t.Errorf("algorithm %s", signer.Algorithm())
	}
	if got := request.Header.Get("Content-Digest"); got != ContentDigest([]byte(rfcBody)) {
		t.Errorf("Content-Digest %s", got)
	}
	if got := request.Header.Get("Signature-Input"); got != `sig-b26=("date" "@method" "@path" "@authority" "content-type" "content-length");created=1618884473;keyid="test-key-ed25519"` {
		t.Errorf("Signature-Input %s", got)
	}
	if got := request.Header.Get("Signature"); got != "sig-b26=:wqcAqbmYJ2ji2glfAMaRy4gruYYnx2nEFN2HN6jrnDnQCK1u02Gb04v9EDgwUPiu4A0w6vuQv5lIp5WPpBKRCw==:" {
		t.Errorf("Signature %s", got)
	}
}

func TestRSAMatchesRFC9421Section43(t *testing.T) {
	signer := mustSigner(t, SignerOptions{
		PrivateKey: rfcRSAKey,
		Components: []string{"@method", "@authority", "@path", "content-digest", "content-type", "content-length", "forwarded"},
		Label:      "proxy_sig",
		KeyID:      "test-key-rsa",
		IncludeAlg: true,
		Lifetime:   time.Minute,
		Now:        fixedClock(1618884480),
	})
	// No body, so the signer keeps the RFC's own SHA-512 digest instead of adding one.
	request := &AuthRequest{
		Method: "POST",
		URL:    "https://origin.host.internal.example/foo?param=Value&Pet=dog",
		Header: http.Header{
			"Content-Type":   {"application/json"},
			"Content-Length": {"18"},
			"Forwarded":      {"for=192.0.2.123;host=example.com;proto=https"},
			"Content-Digest": {"sha-512=:WZDPaVn/7XgHaAy8pmojAkGWoRx2UFChF41A2svX+TaPm+AbwAgBWnrIiYllu7BNNyealdVLvRwEmTHWXvJwew==:"},
		},
	}
	if err := signer.Sign(request); err != nil {
		t.Fatal(err)
	}
	if signer.Algorithm() != AlgorithmRSAv15SHA256 {
		t.Errorf("algorithm %s", signer.Algorithm())
	}
	if got := request.Header.Get("Signature-Input"); got != `proxy_sig=("@method" "@authority" "@path" "content-digest" "content-type" "content-length" "forwarded");created=1618884480;keyid="test-key-rsa";alg="rsa-v1_5-sha256";expires=1618884540` {
		t.Errorf("Signature-Input %s", got)
	}
	want := "proxy_sig=:S6ZzPXSdAMOPjN/6KXfXWNO/f7V6cHm7BXYUh3YD/fRad4BCaRZxP+JH+8XY1I6+8Cy+CM5g92iHgxtRPz+MjniOaYmdkDcnL9" +
		"cCpXJleXsOckpURl49GwiyUpZ10KHgOEe11sx3G2gxI8S0jnxQB+Pu68U9vVcasqOWAEObtNKKZd8tSFu7LB5YAv0RAGhB8tmpv7sFnIm9y+7X5" +
		"kXQfi8NMaZaA8i2ZHwpBdg7a6CMfwnnrtflzvZdXAsD3LH2TwevU+/PBPv0B6NMNk93wUs/vfJvye+YuI87HU38lZHowtznbLVdp770I6VHR6Wf" +
		"gS9ddzirrswsE1w5o0LV/g==:"
	if got := request.Header.Get("Signature"); got != want {
		t.Errorf("Signature %s", got)
	}
}

func serveSigned(t *testing.T, signer *MessageSigner, statuses ...int) (*Transport, func() []received) {
	t.Helper()
	var lock sync.Mutex
	var seen []received
	transport := serveFor(t, signed{signer}, func(w http.ResponseWriter, r *http.Request) {
		body, _ := io.ReadAll(r.Body)
		lock.Lock()
		seen = append(seen, received{method: r.Method, url: r.URL, host: r.Host, header: r.Header.Clone(), body: body})
		status := statuses[len(seen)-1]
		lock.Unlock()
		if status == http.StatusTooManyRequests {
			w.Header().Set("Retry-After", "0")
		}
		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(status)
		_, _ = w.Write([]byte(`{"id":1}`))
	}, nil)
	return transport, func() []received {
		lock.Lock()
		defer lock.Unlock()
		return seen
	}
}

func TestEachAttemptIsSignedAgainOverItsOwnBody(t *testing.T) {
	public, private, _ := ed25519.GenerateKey(rand.Reader)
	var clock atomic.Int64
	clock.Store(1700000000)
	signer := mustSigner(t, SignerOptions{
		PrivateKey: pkcs8PEM(t, private),
		Components: signedComponents,
		Now:        func() time.Time { return time.Unix(clock.Add(1), 0) },
	})
	transport, seen := serveSigned(t, signer, http.StatusTooManyRequests, http.StatusOK)
	operation := &Operation{ID: "create", Method: "POST", Path: "/items", Security: []Requirement{{{Name: "key"}}}}
	if _, err := Call[any](context.Background(), transport, operation, Input{Body: map[string]string{"name": "synthetic"}}); err != nil {
		t.Fatal(err)
	}
	requests := seen()
	if len(requests) != 2 {
		t.Fatalf("sent %d requests", len(requests))
	}
	for index, request := range requests {
		if got := request.header.Get("Content-Digest"); got != ContentDigest(request.body) {
			t.Errorf("Content-Digest %s does not match the body", got)
		}
		want := fmt.Sprintf(`sig1=("content-digest" "@method" "@path" "@authority");created=%d`, 1700000001+index)
		if got := request.header.Get("Signature-Input"); got != want {
			t.Errorf("Signature-Input %s, want %s", got, want)
		}
		verifyReceived(t, public, request, signedComponents)
	}
}

func TestARequestWithoutABodyHasNoDigest(t *testing.T) {
	public, private, _ := ed25519.GenerateKey(rand.Reader)
	signer := mustSigner(t, SignerOptions{PrivateKey: pkcs8PEM(t, private), Components: signedComponents, Now: fixedClock(1700000000)})
	transport, seen := serveSigned(t, signer, http.StatusOK)
	if _, err := Call[any](context.Background(), transport, getItem, Input{Path: []any{"a"}}); err != nil {
		t.Fatal(err)
	}
	request := seen()[0]
	if request.header.Get("Content-Digest") != "" {
		t.Errorf("a request without a body has a digest")
	}
	if got := request.header.Get("Signature-Input"); got != `sig1=("@method" "@path" "@authority");created=1700000000` {
		t.Errorf("Signature-Input %s", got)
	}
	verifyReceived(t, public, request, []string{"@method", "@path", "@authority"})
}

func TestRejectsUnsupportedKeysAndComponents(t *testing.T) {
	p256, _ := ecdsa.GenerateKey(elliptic.P256(), rand.Reader)
	for _, options := range []SignerOptions{
		{PrivateKey: pkcs8PEM(t, p256), Components: signedComponents},
		{PrivateKey: "not a key", Components: signedComponents},
		{PrivateKey: rfcEd25519Key, Components: []string{"@status"}},
		{PrivateKey: rfcEd25519Key, Components: []string{"Content-Type"}},
		{PrivateKey: rfcEd25519Key, Components: []string{`"@query-param";name="Pet"`}},
	} {
		if _, err := NewMessageSigner(options); err == nil {
			t.Errorf("accepted %v", options.Components)
		}
	}
	signer := mustSigner(t, SignerOptions{PrivateKey: rfcEd25519Key, Components: []string{"x-missing"}})
	err := signer.Sign(&AuthRequest{Method: "GET", URL: "https://example.com/", Header: http.Header{}})
	if err == nil || !strings.Contains(err.Error(), "x-missing") {
		t.Errorf("got %v", err)
	}
}

func TestThePrivateKeyIsASecret(t *testing.T) {
	signer := mustSigner(t, SignerOptions{PrivateKey: rfcEd25519Key, Components: signedComponents})
	body := "MC4CAQAwBQYDK2VwBCIEIJ+DYvh6SEqVTm50DFtMDoQikTmiCqirVv9mWG9qfSnF"
	for _, shown := range []string{
		fmt.Sprint(signer),
		fmt.Sprintf("%v %+v %#v", signer, signer, signer),
		fmt.Sprintf("%v %+v %#v %s", *signer, *signer, *signer, *signer),
	} {
		if strings.Contains(shown, body) {
			t.Errorf("formatting shows the key: %s", shown)
		}
	}
	text := "key " + strings.TrimSpace(rfcEd25519Key) + " and " + body
	if got := redactWith(redactions(signed{signer}), text); got != "key *** and ***" {
		t.Errorf("redacted %q", got)
	}
}

func TestLifetimeIsWholeSecondsOfAtLeastOne(t *testing.T) {
	for _, lifetime := range []time.Duration{-time.Second, time.Millisecond, 1500 * time.Millisecond} {
		if _, err := NewMessageSigner(SignerOptions{PrivateKey: rfcEd25519Key, Components: signedComponents, Lifetime: lifetime}); err == nil {
			t.Errorf("accepted a lifetime of %v", lifetime)
		}
	}
	signer := mustSigner(t, SignerOptions{
		PrivateKey: rfcEd25519Key,
		Components: []string{"@method"},
		Lifetime:   time.Second,
		Now:        func() time.Time { return time.Unix(1700000000, 900_000_000) },
	})
	request := &AuthRequest{Method: "GET", URL: "https://example.com/", Header: http.Header{}}
	if err := signer.Sign(request); err != nil {
		t.Fatal(err)
	}
	if got := request.Header.Get("Signature-Input"); got != `sig1=("@method");created=1700000000;expires=1700000001` {
		t.Errorf("Signature-Input %s", got)
	}
}

func TestContentLengthAndHostComeFromTheBodyAndURLWhenAbsent(t *testing.T) {
	value := func(request *AuthRequest, name string) string {
		t.Helper()
		target, _ := url.Parse(request.URL)
		got, err := componentValue(request, target, name)
		if err != nil {
			t.Fatal(err)
		}
		return got
	}
	request := &AuthRequest{Method: "POST", URL: "https://Example.com:443/items", Header: http.Header{}, Body: []byte("synthetic")}
	if got := value(request, "content-length"); got != "9" {
		t.Errorf("content-length %s", got)
	}
	if got := value(request, "host"); got != "example.com" {
		t.Errorf("host %s", got)
	}
	given := &AuthRequest{Method: "POST", URL: "https://example.com/items", Header: http.Header{"Content-Length": {"18"}, "Host": {"proxy.example"}}}
	if got := value(given, "content-length") + " " + value(given, "host"); got != "18 proxy.example" {
		t.Errorf("content-length and host %s", got)
	}
	signer := mustSigner(t, SignerOptions{PrivateKey: rfcEd25519Key, Components: []string{"content-length", "host"}})
	if err := signer.Sign(request); err != nil {
		t.Fatal(err)
	}
	if request.Header.Get("Content-Length") != "" || request.Header.Get("Host") != "" {
		t.Errorf("the signer added a header the transport sends: %v", request.Header)
	}
	err := signer.Sign(&AuthRequest{Method: "GET", URL: "https://example.com/items", Header: http.Header{}})
	if err == nil || !strings.Contains(err.Error(), "content-length") {
		t.Errorf("got %v", err)
	}
}

func TestAPostOrPutWithoutABodySignsAZeroContentLength(t *testing.T) {
	signer := mustSigner(t, SignerOptions{PrivateKey: rfcEd25519Key, Components: []string{"content-length"}})
	for _, method := range []string{"POST", "PUT"} {
		request := &AuthRequest{Method: method, URL: "https://example.com/items", Header: http.Header{}}
		target, _ := url.Parse(request.URL)
		if got, err := componentValue(request, target, "content-length"); err != nil || got != "0" {
			t.Errorf("%s: content-length %q, %v", method, got, err)
		}
		if err := signer.Sign(request); err != nil {
			t.Errorf("%s: %v", method, err)
		}
		if request.Header.Get("Content-Length") != "" {
			t.Errorf("%s: the signer added a header the transport sends: %v", method, request.Header)
		}
	}
	for _, method := range []string{"GET", "DELETE", "PATCH"} {
		err := signer.Sign(&AuthRequest{Method: method, URL: "https://example.com/items", Header: http.Header{}})
		if err == nil || !strings.Contains(err.Error(), "content-length") {
			t.Errorf("%s: got %v", method, err)
		}
	}
}

func TestAPostOrPutWithoutABodySendsTheZeroContentLengthItSigns(t *testing.T) {
	public, private, _ := ed25519.GenerateKey(rand.Reader)
	components := []string{"content-length", "@method"}
	signer := mustSigner(t, SignerOptions{PrivateKey: pkcs8PEM(t, private), Components: components, Now: fixedClock(1700000000)})
	for _, method := range []string{"POST", "PUT"} {
		transport, seen := serveSigned(t, signer, http.StatusOK)
		operation := &Operation{ID: "touch", Method: method, Path: "/items", Security: []Requirement{{{Name: "key"}}}}
		if _, err := Call[any](context.Background(), transport, operation, Input{}); err != nil {
			t.Fatal(err)
		}
		request := seen()[0]
		if got := request.header.Values("Content-Length"); !slices.Equal(got, []string{"0"}) {
			t.Errorf("%s: the server received Content-Length %q", method, got)
		}
		_, params, _ := strings.Cut(request.header.Get("Signature-Input"), "=")
		base := fmt.Sprintf("\"content-length\": 0\n\"@method\": %s\n\"@signature-params\": %s", method, params)
		signature, _ := base64.StdEncoding.DecodeString(strings.TrimSuffix(strings.TrimPrefix(request.header.Get("Signature"), "sig1=:"), ":"))
		if !ed25519.Verify(public, []byte(base), signature) {
			t.Errorf("%s: the signature does not verify over %q", method, base)
		}
	}
}

func TestAnEmptyQueryIsNoQuery(t *testing.T) {
	request := &AuthRequest{Method: "GET", URL: "https://example.com/p?", Header: http.Header{}}
	target, _ := url.Parse(request.URL)
	for name, want := range map[string]string{"@request-target": "/p", "@query": "?"} {
		if got, _ := componentValue(request, target, name); got != want {
			t.Errorf("%s is %q, want %q", name, got, want)
		}
	}
}

func TestEachLineOfTheKeyBodyIsASecret(t *testing.T) {
	signer := mustSigner(t, SignerOptions{PrivateKey: rfcRSAKey, Components: signedComponents})
	lines := strings.Split(strings.TrimSpace(rfcRSAKey), "\n")
	lines = lines[1 : len(lines)-1]
	stars := strings.Repeat("***\r\n", len(lines))
	if got := redactWith(redactions(signed{signer}), strings.Join(lines, "\r\n")); got != stars[:len(stars)-2] {
		t.Errorf("redacted %q", got)
	}
}
