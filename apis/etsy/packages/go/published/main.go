// Command smoke is the published module's smoke test, run by the published packages workflow against the mock, never
// the live API. It is built in a clean module that requires the published version through the Go module proxy.
package main

import (
	"context"
	"fmt"
	"log"
	"os"
	"runtime/debug"

	"github.com/fdhoff/api-sdks/apis/etsy/packages/go/etsyseller"
)

const module = "github.com/fdhoff/api-sdks/apis/etsy/packages/go"

func main() {
	expected := "v" + os.Getenv("SMOKE_VERSION")
	if version := moduleVersion(); version != expected {
		log.Fatalf("built with %s %q, not %s", module, version, expected)
	}
	client, err := etsyseller.NewClient(
		"smoke-synthetic-keystring",
		"smoke-synthetic-shared-secret",
		etsyseller.WithBaseURL(os.Getenv("SMOKE_BASE_URL")),
	)
	if err != nil {
		log.Fatal(err)
	}
	pong, err := client.Application.Ping(context.Background())
	if err != nil {
		log.Fatal(err)
	}
	if pong.ApplicationID == nil {
		log.Fatal("the ping has no application_id")
	}
	fmt.Printf("%s %s: pinged application %d\n", module, expected, *pong.ApplicationID)
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
