package etsyseller_test

import (
	"context"
	"crypto/subtle"
	"errors"
	"fmt"
	"log"
	"net/url"

	"github.com/fdhoff/api-sdks/apis/etsy/packages/go/etsyseller"
)

// These examples are the README's, compiled so they stay current. They are not run.

func save(etsyseller.Token) {}

func Example() {
	client, err := etsyseller.NewClient("your-keystring", "your-shared-secret")
	if err != nil {
		log.Fatal(err)
	}
	ctx := context.Background()

	params := &etsyseller.ListingsListActiveParams{Keywords: etsyseller.Ptr("ceramic mug"), Limit: etsyseller.Ptr[int64](100)}
	for listing, err := range client.Listings.IterActive(ctx, params) {
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(*listing.ListingID, *listing.Title)
	}

	_, err = client.Shops.Get(ctx, 1)
	var failure *etsyseller.APIError
	if errors.Is(err, etsyseller.ErrNotFound) && errors.As(err, &failure) {
		fmt.Println(failure.Status, failure.Detail)
	}
}

func Example_accessToken() {
	ctx := context.Background()
	client, err := etsyseller.NewClient(
		"your-keystring",
		"your-shared-secret",
		etsyseller.WithAccessToken("12345678.your-access-token"),
		etsyseller.WithRefreshToken("12345678.your-refresh-token"),
		// Store both tokens: the old refresh token stops working.
		etsyseller.WithOnToken(func(token etsyseller.Token) { save(token) }),
	)
	if err != nil {
		log.Fatal(err)
	}
	me, err := client.Users.GetMe(ctx)
	if err != nil {
		log.Fatal(err)
	}
	for receipt, err := range client.Receipts.Iter(ctx, *me.ShopID, &etsyseller.ReceiptsListParams{WasShipped: etsyseller.Ptr(false)}) {
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(*receipt.ReceiptID)
	}
}

func ExampleOAuth() {
	ctx := context.Background()
	client, err := etsyseller.NewClient("your-keystring", "your-shared-secret")
	if err != nil {
		log.Fatal(err)
	}
	redirect, _ := url.Parse("https://example.com/callback?state=returned&code=synthetic")

	request, err := client.OAuth.AuthorizationRequest(etsyseller.AuthorizationParams{
		RedirectURI: "https://example.com/callback",
		Scopes:      []string{"listings_r", "shops_r"},
	})
	if err != nil {
		log.Fatal(err)
	}
	// Send the user to request.URL, and keep request.State and request.CodeVerifier until they return.

	returnedState, code := redirect.Query().Get("state"), redirect.Query().Get("code")
	if subtle.ConstantTimeCompare([]byte(returnedState), []byte(request.State)) != 1 {
		log.Fatal("state mismatch")
	}
	token, err := client.OAuth.ExchangeCode(ctx, code, request.CodeVerifier, "https://example.com/callback")
	if err != nil {
		log.Fatal(err)
	}
	userID, _ := token.UserID()
	fmt.Println(userID)
}
