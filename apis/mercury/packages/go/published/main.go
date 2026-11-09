// Command smoke is the published module's smoke test, run by the published packages workflow against the mock, never
// the live API. It is built in a clean module that requires the published version through the Go module proxy.
package main

import (
	"context"
	"fmt"
	"log"
	"os"
	"runtime/debug"

	"github.com/fdhoff/api-sdks/apis/mercury/packages/go/mercurybanking"
)

const module = "github.com/fdhoff/api-sdks/apis/mercury/packages/go"

func main() {
	expected := "v" + os.Getenv("SMOKE_VERSION")
	if version := moduleVersion(); version != expected {
		log.Fatalf("built with %s %q, not %s", module, version, expected)
	}
	mock := os.Getenv("SMOKE_BASE_URL")
	client, err := mercurybanking.NewClient(
		"secret-token:smoke-synthetic-token",
		mercurybanking.WithHosts(map[string]string{"api": mock, "vault": mock}),
	)
	if err != nil {
		log.Fatal(err)
	}
	page, err := client.Accounts.List(context.Background(), nil)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%s %s: listed %d accounts\n", module, expected, len(page.Accounts))
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
