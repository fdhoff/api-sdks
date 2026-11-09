package runtime

import (
	"crypto"
	"crypto/ed25519"
	"crypto/rand"
	"crypto/rsa"
	"crypto/sha256"
	"crypto/x509"
	"encoding/base64"
	"encoding/pem"
	"errors"
	"fmt"
	"net/url"
	"regexp"
	"slices"
	"strconv"
	"strings"
	"time"
)

// Signature algorithms a [MessageSigner] can use.
const (
	AlgorithmEd25519      = "ed25519"
	AlgorithmRSAv15SHA256 = "rsa-v1_5-sha256"
)

var (
	derivedComponents = map[string]bool{"@method": true, "@target-uri": true, "@authority": true, "@scheme": true, "@request-target": true, "@path": true, "@query": true}
	fieldComponent    = regexp.MustCompile("^[a-z0-9!#$%&'*+.^_`|~-]+$")
	signatureLabel    = regexp.MustCompile(`^[a-z*][a-z0-9_.*-]*$`)
	defaultPorts      = map[string]string{"http": ":80", "https": ":443"}
)

// minSecretLine is the shortest line of a key's base64 body to redact. A shorter last line is too
// common a string.
const minSecretLine = 16

// SignerOptions configures a [MessageSigner]. Components are lowercase field names and the derived
// components @method, @target-uri, @authority, @scheme, @request-target, @path and @query.
type SignerOptions struct {
	// PrivateKey is an unencrypted PKCS #8 PEM Ed25519 or RSA private key. It is a secret.
	PrivateKey string
	Components []string
	Label      string // "sig1" when empty.
	KeyID      string // Sent as keyid when set.
	IncludeAlg bool
	Lifetime   time.Duration // Adds expires when set. Whole seconds.
	Now        func() time.Time
}

// MessageSigner signs each attempt's request with an HTTP message signature (RFC 9421): a
// Content-Digest (RFC 9530) of the body when there is one, then Signature-Input and Signature over
// the covered components, with a fresh created time. content-digest is left out of a request with
// no body. A request without content-length or host uses the body's length, 0 for a POST, PUT or
// PATCH without one, or the URL's authority, which net/http sends; any other field the request lacks
// is an error. Call Sign from Credentials.Apply.
type MessageSigner struct {
	algorithm  string
	sign       func([]byte) ([]byte, error)
	secrets    []string
	components []string
	label      string
	extra      string
	lifetime   time.Duration
	now        func() time.Time
}

// NewMessageSigner checks the options and loads the key.
func NewMessageSigner(options SignerOptions) (*MessageSigner, error) {
	for _, component := range options.Components {
		if strings.HasPrefix(component, "@") && !derivedComponents[component] || !strings.HasPrefix(component, "@") && !fieldComponent.MatchString(component) {
			return nil, fmt.Errorf("unsupported covered component %q", component)
		}
	}
	label := options.Label
	if label == "" {
		label = "sig1"
	}
	if !signatureLabel.MatchString(label) {
		return nil, errors.New("the signature label must be a lowercase key")
	}
	if options.Lifetime < 0 || options.Lifetime%time.Second != 0 {
		return nil, errors.New("the signature lifetime must be a whole number of seconds, at least 1")
	}
	algorithm, sign, err := loadSigningKey(options.PrivateKey)
	if err != nil {
		return nil, err
	}
	extra := ""
	if options.KeyID != "" {
		keyID, err := quoteParameter(options.KeyID)
		if err != nil {
			return nil, err
		}
		extra += ";keyid=" + keyID
	}
	if options.IncludeAlg {
		extra += `;alg="` + algorithm + `"`
	}
	now := options.Now
	if now == nil {
		now = time.Now
	}
	trimmed := strings.TrimSpace(options.PrivateKey)
	return &MessageSigner{
		algorithm:  algorithm,
		sign:       sign,
		secrets:    keySecrets(trimmed),
		components: append([]string(nil), options.Components...),
		label:      label,
		extra:      extra,
		lifetime:   options.Lifetime,
		now:        now,
	}, nil
}

func loadSigningKey(text string) (string, func([]byte) ([]byte, error), error) {
	block, _ := pem.Decode([]byte(text))
	if block == nil || block.Type != "PRIVATE KEY" {
		return "", nil, errors.New("the signing key must be an unencrypted PKCS #8 PEM private key")
	}
	key, err := x509.ParsePKCS8PrivateKey(block.Bytes)
	if err != nil {
		return "", nil, errors.New("the signing key is not a valid private key")
	}
	switch key := key.(type) {
	case ed25519.PrivateKey:
		return AlgorithmEd25519, func(base []byte) ([]byte, error) { return ed25519.Sign(key, base), nil }, nil
	case *rsa.PrivateKey:
		return AlgorithmRSAv15SHA256, func(base []byte) ([]byte, error) {
			digest := sha256.Sum256(base)
			return rsa.SignPKCS1v15(rand.Reader, key, crypto.SHA256, digest[:])
		}, nil
	}
	return "", nil, errors.New("the signing key must be Ed25519 or RSA")
}

func keySecrets(trimmed string) []string {
	lines := strings.Split(trimmed, "\n")
	if len(lines) < 2 {
		return []string{trimmed}
	}
	secrets := []string{trimmed}
	var body strings.Builder
	for _, line := range lines[1 : len(lines)-1] {
		line = strings.TrimSpace(line)
		body.WriteString(line)
		if len(line) >= minSecretLine {
			secrets = append(secrets, line)
		}
	}
	return slices.Compact(append(secrets, body.String()))
}

func quoteParameter(value string) (string, error) {
	for _, char := range value {
		if char < 0x20 || char > 0x7e {
			return "", errors.New("a signature parameter must be printable ASCII")
		}
	}
	return `"` + strings.NewReplacer(`\`, `\\`, `"`, `\"`).Replace(value) + `"`, nil
}

// ContentDigest is the Content-Digest value for these exact bytes.
func ContentDigest(body []byte) string {
	sum := sha256.Sum256(body)
	return "sha-256=:" + base64.StdEncoding.EncodeToString(sum[:]) + ":"
}

// Algorithm is the signature algorithm the key needs.
func (s *MessageSigner) Algorithm() string { return s.algorithm }

// Secrets returns the private key as given, as its PEM body and as each line of that body, to
// redact.
func (s *MessageSigner) Secrets() []string { return s.secrets }

// String keeps the key out of formatted output. It has a value receiver so that a dereferenced
// signer is covered too.
func (s MessageSigner) String() string { return "MessageSigner(" + s.algorithm + ", ***)" }

// GoString keeps the key out of %#v.
func (s MessageSigner) GoString() string { return s.String() }

// Sign adds the digest and signature headers to the request.
func (s *MessageSigner) Sign(request *AuthRequest) error {
	if len(request.Body) > 0 {
		request.Header.Set("Content-Digest", ContentDigest(request.Body))
	}
	target, err := url.Parse(request.URL)
	if err != nil {
		return fmt.Errorf("the request URL cannot be signed: %w", err)
	}
	created := s.now().Unix()
	var quoted, lines []string
	for _, name := range s.components {
		if name == "content-digest" && len(request.Header.Values(name)) == 0 {
			continue
		}
		value, err := componentValue(request, target, name)
		if err != nil {
			return err
		}
		quoted = append(quoted, `"`+name+`"`)
		lines = append(lines, `"`+name+`": `+value)
	}
	params := "(" + strings.Join(quoted, " ") + ");created=" + strconv.FormatInt(created, 10) + s.extra
	if s.lifetime != 0 {
		params += ";expires=" + strconv.FormatInt(created+int64(s.lifetime/time.Second), 10)
	}
	lines = append(lines, `"@signature-params": `+params)
	signature, err := s.sign([]byte(strings.Join(lines, "\n")))
	if err != nil {
		return fmt.Errorf("the request could not be signed: %w", err)
	}
	request.Header.Set("Signature-Input", s.label+"="+params)
	request.Header.Set("Signature", s.label+"=:"+base64.StdEncoding.EncodeToString(signature)+":")
	return nil
}

// contentLength is what net/http sends: the body's length, or 0 for a POST, PUT or PATCH without a body.
func contentLength(request *AuthRequest) []string {
	if len(request.Body) > 0 {
		return []string{strconv.Itoa(len(request.Body))}
	}
	if method := strings.ToUpper(request.Method); method == "POST" || method == "PUT" || method == "PATCH" {
		return []string{"0"}
	}
	return nil
}

func componentValue(request *AuthRequest, target *url.URL, name string) (string, error) {
	scheme := strings.ToLower(target.Scheme)
	authority := strings.TrimSuffix(strings.ToLower(target.Host), defaultPorts[scheme])
	if !strings.HasPrefix(name, "@") {
		values := slices.Clone(request.Header.Values(name))
		if len(values) == 0 && name == "content-length" {
			values = contentLength(request)
		}
		if len(values) == 0 && name == "host" {
			values = []string{authority}
		}
		if len(values) == 0 {
			return "", fmt.Errorf("the request has no %s field to sign", name)
		}
		for index, value := range values {
			values[index] = strings.TrimSpace(value)
		}
		return strings.Join(values, ", "), nil
	}
	path := target.EscapedPath()
	if path == "" {
		path = "/"
	}
	query := "?" + target.RawQuery
	switch name {
	case "@method":
		return strings.ToUpper(request.Method), nil
	case "@target-uri":
		return request.URL, nil
	case "@authority":
		return authority, nil
	case "@scheme":
		return scheme, nil
	case "@request-target":
		if target.RawQuery == "" {
			return path, nil
		}
		return path + query, nil
	case "@path":
		return path, nil
	default:
		return query, nil
	}
}
