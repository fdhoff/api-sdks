package ebaysell

import (
	"strings"

	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/internal/runtime"
)

// SignatureComponents are the parts of a request that eBay's signature covers. content-digest is
// left out of a request without a body.
var SignatureComponents = []string{"content-digest", "x-ebay-signature-key", "@method", "@path", "@authority"}

const pemHeader = "-----BEGIN PRIVATE KEY-----"

// SigningKey is a key pair from the Key Management API's create call: its private key, as that call
// returns it or as a PKCS #8 PEM, and its JWE, which is sent as x-ebay-signature-key. The private key
// is a secret, and eBay returns it only once. Ed25519 and RSA keys both work. Printing a SigningKey
// hides the private key.
type SigningKey struct {
	PrivateKey string
	JWE        string
}

// String hides the private key.
func (k SigningKey) String() string { return "SigningKey{JWE: " + k.JWE + ", PrivateKey: ***}" }

// GoString hides the private key.
func (k SigningKey) GoString() string { return k.String() }

func (k SigningKey) signer() (*runtime.MessageSigner, error) {
	return runtime.NewMessageSigner(runtime.SignerOptions{PrivateKey: pem(k.PrivateKey), Components: SignatureComponents})
}

// pem wraps the base64 body eBay returns in the PEM lines it leaves out.
func pem(privateKey string) string {
	key := strings.TrimSpace(privateKey)
	if strings.HasPrefix(key, pemHeader) {
		return key
	}
	body := strings.Join(strings.Fields(key), "")
	lines := []string{pemHeader}
	for start := 0; start < len(body); start += 64 {
		lines = append(lines, body[start:min(start+64, len(body))])
	}
	return strings.Join(append(lines, "-----END PRIVATE KEY-----"), "\n")
}
