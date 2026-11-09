package miraklseller_test

import (
	"context"
	"errors"
	"fmt"
	"io"
	"log"
	"os"
	"time"

	"github.com/fdhoff/api-sdks/apis/mirakl/packages/go/miraklseller"
)

// These examples are the README's, compiled so they stay current. They are not run.

func Example() {
	client, err := miraklseller.NewClient(
		"https://your-operator.mirakl.net",
		miraklseller.APIKey(os.Getenv("MIRAKL_API_KEY")),
		miraklseller.WithShopID(2001),
	)
	if err != nil {
		log.Fatal(err)
	}
	ctx := context.Background()

	params := &miraklseller.OrdersListParams{OrderStateCodes: miraklseller.Ptr("WAITING_ACCEPTANCE"), Max: miraklseller.Ptr[int64](100)}
	for order, err := range client.Orders.Iter(ctx, params) {
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(*order.OrderID)
	}

	_, err = client.Offers.GetStockImport(ctx, "missing-import", nil)
	var failure *miraklseller.APIError
	if errors.Is(err, miraklseller.ErrNotFound) && errors.As(err, &failure) {
		fmt.Println(failure.Status, failure.RawBody)
	}
}

func Example_stockImport() {
	client, err := miraklseller.NewClient("https://your-operator.mirakl.net", miraklseller.APIKey(os.Getenv("MIRAKL_API_KEY")))
	if err != nil {
		log.Fatal(err)
	}
	ctx := context.Background()

	started, err := client.Offers.ImportStock(ctx, &miraklseller.OffersImportStockParams{
		File: miraklseller.File{Name: "stock.csv", Content: []byte("offer-sku;quantity\nsku-1;5\n")},
	})
	if err != nil {
		log.Fatal(err)
	}
	status, err := client.Offers.WaitStockImport(ctx, *started.ImportID, &miraklseller.WaitOptions{Timeout: 30 * time.Minute})
	if err != nil {
		log.Fatal(err)
	}
	if *status.Status == "FAILED" || (status.HasErrorReport != nil && *status.HasErrorReport) {
		report, err := client.Offers.DownloadStockImportErrorReport(ctx, *started.ImportID, nil)
		if err != nil {
			log.Fatal(err)
		}
		defer report.Body.Close()
		if _, err := io.Copy(os.Stdout, report.Body); err != nil {
			log.Fatal(err)
		}
	}
}

func Example_offerExport() {
	client, err := miraklseller.NewClient("https://your-operator.mirakl.net", miraklseller.APIKey(os.Getenv("MIRAKL_API_KEY")))
	if err != nil {
		log.Fatal(err)
	}
	ctx := context.Background()

	started, err := client.Offers.Export(ctx, &miraklseller.OF52Request{ExportType: miraklseller.Ptr("application/json")}, nil)
	if err != nil {
		log.Fatal(err)
	}
	status, err := client.Offers.WaitExport(ctx, *started.TrackingID, nil)
	if err != nil {
		log.Fatal(err)
	}
	for _, address := range status.URLs {
		file, err := client.DownloadURL(ctx, address)
		if err != nil {
			log.Fatal(err)
		}
		body, err := io.ReadAll(file.Body)
		file.Body.Close()
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(len(body))
	}
}
