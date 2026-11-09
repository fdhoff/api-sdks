// Command smoke is the published module's smoke test, run by the published packages workflow against the mock, never
// the live API. It is built in a clean module that requires the published version through the Go module proxy.
package main

import (
	"context"
	"fmt"
	"log"
	"os"
	"runtime/debug"

	"github.com/fdhoff/api-sdks/apis/mirakl/packages/go/miraklseller"
)

const module = "github.com/fdhoff/api-sdks/apis/mirakl/packages/go"

func main() {
	expected := "v" + os.Getenv("SMOKE_VERSION")
	if version := moduleVersion(); version != expected {
		log.Fatalf("built with %s %q, not %s", module, version, expected)
	}
	client, err := miraklseller.NewClient(os.Getenv("SMOKE_BASE_URL"), miraklseller.APIKey("smoke-synthetic-shop-key"))
	if err != nil {
		log.Fatal(err)
	}
	account, err := client.Account.Get(context.Background(), nil)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%s %s: got shop %v\n", module, expected, account.ShopID != nil)
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
