// Command smoke is the published module's smoke test, run by the published packages workflow against the mock, never
// the live API. It is built in a clean module that requires the published version through the Go module proxy.
package main

import (
	"context"
	"fmt"
	"log"
	"os"
	"runtime/debug"

	"github.com/fdhoff/api-sdks/apis/backmarket/packages/go/backmarketseller"
)

const module = "github.com/fdhoff/api-sdks/apis/backmarket/packages/go"

func main() {
	expected := "v" + os.Getenv("SMOKE_VERSION")
	if version := moduleVersion(); version != expected {
		log.Fatalf("built with %s %q, not %s", module, version, expected)
	}
	client, err := backmarketseller.NewClient(
		"smoke-synthetic-token",
		"BM-Example-Smoke;smoke@example.com",
		"en-us",
		backmarketseller.WithBaseURL(os.Getenv("SMOKE_BASE_URL")),
	)
	if err != nil {
		log.Fatal(err)
	}
	order, err := client.Orders.Get(context.Background(), 1)
	if err != nil {
		log.Fatal(err)
	}
	if order.OrderID == nil {
		log.Fatal("the order has no order_id")
	}
	fmt.Printf("%s %s: got order %d\n", module, expected, *order.OrderID)
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
