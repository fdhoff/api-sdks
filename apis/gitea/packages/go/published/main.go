// Command smoke is the published module's smoke test, run by the published packages workflow against the mock, never
// a real instance. It is built in a clean module that requires the published version through the Go module proxy.
// The mock serves the spec's paths without the /api/v1 the client adds, so the transport removes it.
package main

import (
	"context"
	"fmt"
	"log"
	"net/http"
	"os"
	"runtime/debug"
	"strings"

	"github.com/fdhoff/api-sdks/apis/gitea/packages/go/gitearest"
)

const module = "github.com/fdhoff/api-sdks/apis/gitea/packages/go"

type unprefixed struct{}

func (unprefixed) RoundTrip(request *http.Request) (*http.Response, error) {
	address := *request.URL
	address.Path = strings.TrimPrefix(address.Path, gitearest.APIPath)
	address.RawPath = strings.TrimPrefix(address.RawPath, gitearest.APIPath)
	request = request.Clone(request.Context())
	request.URL = &address
	return http.DefaultTransport.RoundTrip(request)
}

func main() {
	expected := "v" + os.Getenv("SMOKE_VERSION")
	if version := moduleVersion(); version != expected {
		log.Fatalf("built with %s %q, not %s", module, version, expected)
	}
	client, err := gitearest.NewClient(os.Getenv("SMOKE_BASE_URL"), gitearest.Token("smoke-synthetic-access-token"),
		gitearest.WithHTTPTransport(unprefixed{}))
	if err != nil {
		log.Fatal(err)
	}
	version, err := client.Misc.GetVersion(context.Background())
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%s %s: got a version %v\n", module, expected, version.Version != nil)
}

// moduleVersion is the version of this module the binary was built with.
func moduleVersion() string {
	if info, ok := debug.ReadBuildInfo(); ok {
		for _, dep := range info.Deps {
			if dep.Path == module {
				return dep.Version
			}
		}
	}
	return ""
}
