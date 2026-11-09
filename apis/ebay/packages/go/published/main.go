// Command smoke is the published module's smoke test, run by the published packages workflow against the mock, never
// the live API. It is built in a clean module that requires the published version through the Go module proxy.
package main

import (
	"context"
	"fmt"
	"log"
	"os"
	"runtime/debug"

	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/taxonomy"
)

const module = "github.com/fdhoff/api-sdks/apis/ebay/packages/go"

func main() {
	expected := "v" + os.Getenv("SMOKE_VERSION")
	if version := moduleVersion(); version != expected {
		log.Fatalf("built with %s %q, not %s", module, version, expected)
	}
	mock := os.Getenv("SMOKE_BASE_URL")
	client, err := ebaysell.NewClient(
		ebaysell.WithAppToken("smoke-synthetic-app-token"),
		ebaysell.WithHosts(map[string]string{"api": mock, "apiz": mock, "apim": mock}),
		ebaysell.WithMarketplaceID("EBAY_US"),
	)
	if err != nil {
		log.Fatal(err)
	}
	params := &taxonomy.CategoryTreesGetDefaultIDParams{MarketplaceID: ebaysell.Ptr("EBAY_US")}
	tree, err := client.Taxonomy.CategoryTrees.GetDefaultID(context.Background(), params)
	if err != nil {
		log.Fatal(err)
	}
	if tree == nil || tree.CategoryTreeID == nil {
		log.Fatal("the category tree has no categoryTreeId")
	}
	fmt.Printf("%s %s: got category tree %s\n", module, expected, *tree.CategoryTreeID)
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
