// Package ebaysell is an unofficial client for eBay's Sell, Commerce and Developer REST APIs. This
// project is unofficial. eBay is a trademark of eBay Inc. This project is not affiliated with,
// endorsed by or sponsored by eBay Inc.
//
// It is an alpha, tested only against a mock built from the public contracts, never against the
// live API.
//
// Each API is a sub-package, such as [github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/fulfillment],
// holding its models and resources, and a field of [Client], such as Client.Fulfillment.
//
// Every call takes a [context.Context]. Cancelling it stops the call, including any wait before a
// retry, and the call returns the context's error.
package ebaysell
