package mercurybanking_test

import (
	"context"
	"errors"
	"fmt"
	"io"
	"log"
	"net/http"

	"github.com/fdhoff/api-sdks/apis/mercury/packages/go/mercurybanking"
)

// These examples are the README's, compiled so they stay current. They are not run.

func newKey() string { return "a-fresh-key-you-store-with-the-payment" }

func Example() {
	client, err := mercurybanking.NewClient("secret-token:your-token")
	if err != nil {
		log.Fatal(err)
	}
	ctx := context.Background()

	for account, err := range client.Accounts.Iter(ctx, nil) {
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(*account.Name, *account.AvailableBalance)
	}

	params := &mercurybanking.TransactionsListParams{Limit: mercurybanking.Ptr[int64](100), Status: []string{"sent"}}
	for transaction, err := range client.Transactions.Iter(ctx, params) {
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(*transaction.CounterpartyName, *transaction.Amount)
	}

	_, err = client.Recipients.Get(ctx, "00000000-0000-4000-8000-000000000000")
	var failure *mercurybanking.APIError
	if errors.Is(err, mercurybanking.ErrNotFound) && errors.As(err, &failure) {
		fmt.Println(failure.Status, failure.RawBody)
	}
}

func Example_sandbox() {
	client, err := mercurybanking.NewClient("secret-token:your-sandbox-token", mercurybanking.WithEnvironment(mercurybanking.Sandbox))
	if err != nil {
		log.Fatal(err)
	}
	page, err := client.Recipients.List(context.Background(), &mercurybanking.RecipientsListParams{Limit: mercurybanking.Ptr[int64](10)})
	if err != nil {
		log.Fatal(err)
	}
	for _, recipient := range page.Recipients {
		fmt.Println(*recipient.Name)
	}
}

func Example_sendMoney() {
	client, err := mercurybanking.NewClient("secret-token:your-token")
	if err != nil {
		log.Fatal(err)
	}
	transaction, err := client.Accounts.SendMoney(context.Background(), "00000000-0000-4000-8000-000000000001", &mercurybanking.PostTransactionAPIRequest{
		RecipientID:    mercurybanking.Ptr("00000000-0000-4000-8000-000000000002"),
		Amount:         mercurybanking.Ptr(12.5),
		PaymentMethod:  mercurybanking.Ptr(mercurybanking.PostTransactionPaymentMethodAch),
		IdempotencyKey: mercurybanking.Ptr(newKey()),
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(*transaction.ID, *transaction.Status)
}

func Example_webhook() {
	secret := "your-webhook-secret"
	http.HandleFunc("/mercury", func(w http.ResponseWriter, r *http.Request) {
		body, err := io.ReadAll(r.Body)
		if err != nil {
			http.Error(w, "unreadable body", http.StatusBadRequest)
			return
		}
		if err := mercurybanking.VerifyWebhook(body, r.Header.Get(mercurybanking.SignatureHeader), secret); err != nil {
			// ErrWebhookMalformedHeader, ErrWebhookTooOld or ErrWebhookBadSignature.
			http.Error(w, "rejected", http.StatusBadRequest)
			return
		}
		w.WriteHeader(http.StatusOK)
	})
}
