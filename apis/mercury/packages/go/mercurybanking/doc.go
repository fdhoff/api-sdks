// Package mercurybanking is an unofficial client for the Mercury API. It is not affiliated with,
// endorsed by or sponsored by Mercury Technologies, Inc. Mercury is a financial technology company,
// not a bank; its banking services are provided through partner banks.
//
// It is an alpha, tested only against a mock built from the public spec, never against the live API.
//
// Every call takes a [context.Context]. Cancelling it stops the call, including any wait before a
// retry, and the call returns the context's error.
package mercurybanking
