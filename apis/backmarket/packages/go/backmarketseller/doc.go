// Package backmarketseller is an unofficial client for the Back Market Seller API. This project is
// unofficial and is not affiliated with, endorsed by, or supported by Back Market.
//
// It is an alpha, tested only against a mock built from the public spec, never against the live API.
//
// Every call takes a [context.Context]. Cancelling it stops the call, including any wait before a
// retry, and the call returns the context's error.
package backmarketseller
