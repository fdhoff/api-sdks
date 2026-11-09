package ebaysell_test

import (
	"context"
	"crypto/subtle"
	"errors"
	"fmt"
	"log"
	"net/url"

	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/finances"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/fulfillment"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/keymanagement"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/taxonomy"
)

// These examples are the README's, compiled so they stay current. They are not run.

func save(ebaysell.Token) {}

func Example() {
	client, err := ebaysell.NewClient(ebaysell.WithClientCredentials("your-app-id", "your-cert-id"))
	if err != nil {
		log.Fatal(err)
	}
	ctx := context.Background()

	tree, err := client.Taxonomy.CategoryTrees.GetDefaultID(ctx, &taxonomy.CategoryTreesGetDefaultIDParams{MarketplaceID: ebaysell.Ptr("EBAY_US")})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(*tree.CategoryTreeID)

	_, err = client.Taxonomy.CategoryTrees.Get(ctx, "0")
	var failure *ebaysell.APIError
	if errors.Is(err, ebaysell.ErrNotFound) && errors.As(err, &failure) {
		fmt.Println(failure.Status, failure.Code, failure.Detail)
	}
}

func Example_userToken() {
	ctx := context.Background()
	client, err := ebaysell.NewClient(
		ebaysell.WithClientCredentials("your-app-id", "your-cert-id"),
		ebaysell.WithUserToken("v^1.1#your-user-token"),
		ebaysell.WithRefreshToken("v^1.1#your-refresh-token"),
		// Store the new access token. The refresh token stays the same.
		ebaysell.WithOnToken(func(token ebaysell.Token) { save(token) }),
		ebaysell.WithMarketplaceID("EBAY_US"),
	)
	if err != nil {
		log.Fatal(err)
	}
	params := &fulfillment.OrdersListParams{Filter: ebaysell.Ptr("orderfulfillmentstatus:{NOT_STARTED|IN_PROGRESS}")}
	for order, err := range client.Fulfillment.Orders.Iter(ctx, params) {
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(*order.OrderID)
	}
}

func ExampleOAuth() {
	ctx := context.Background()
	client, err := ebaysell.NewClient(
		ebaysell.WithClientCredentials("your-app-id", "your-cert-id"),
		ebaysell.WithRuName("your-ru-name"),
		ebaysell.WithOnToken(func(token ebaysell.Token) { save(token) }),
	)
	if err != nil {
		log.Fatal(err)
	}
	redirect, _ := url.Parse("https://example.com/accepted?state=returned&code=synthetic")

	request, err := client.OAuth.AuthorizationRequest(ebaysell.AuthorizationParams{
		Scopes: []string{"https://api.ebay.com/oauth/api_scope/sell.fulfillment"},
	})
	if err != nil {
		log.Fatal(err)
	}
	// Send the user to request.URL, and keep request.State until they return.

	returnedState, code := redirect.Query().Get("state"), redirect.Query().Get("code")
	if subtle.ConstantTimeCompare([]byte(returnedState), []byte(request.State)) != 1 {
		log.Fatal("state mismatch")
	}
	token, err := client.OAuth.ExchangeCode(ctx, code)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(token.ExpiresIn)
}

func ExampleSigningKey() {
	ctx := context.Background()
	keys, err := ebaysell.NewClient(ebaysell.WithClientCredentials("your-app-id", "your-cert-id"))
	if err != nil {
		log.Fatal(err)
	}
	created, err := keys.KeyManagement.SigningKeys.Create(ctx, &keymanagement.CreateSigningKeyRequest{SigningKeyCipher: ebaysell.Ptr("ED25519")})
	if err != nil {
		log.Fatal(err)
	}
	// Store *created.PrivateKey and *created.Jwe somewhere safe: eBay returns the private key only once.

	client, err := ebaysell.NewClient(
		ebaysell.WithUserToken("v^1.1#your-user-token"),
		ebaysell.WithSigningKey(ebaysell.SigningKey{PrivateKey: *created.PrivateKey, JWE: *created.Jwe}),
	)
	if err != nil {
		log.Fatal(err)
	}
	summary, err := client.Finances.SellerFunds.GetSummary(ctx, &finances.SellerFundsGetSummaryParams{MarketplaceID: ebaysell.Ptr("EBAY_GB")})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(*summary.TotalFunds.Value)
}
