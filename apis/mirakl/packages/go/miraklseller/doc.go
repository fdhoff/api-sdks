// Package miraklseller is an unofficial client for the Mirakl marketplace seller API. It is not
// affiliated with, endorsed by or sponsored by Mirakl SAS.
//
// Each marketplace operator, such as Best Buy, runs its own Mirakl instance, so [NewClient] always
// takes that instance's base URL. There is no public sandbox.
//
// It is an alpha, tested only against a mock built from the public spec, never against the live API.
//
// Every call takes a [context.Context]. Cancelling it stops the call, including any wait before a
// retry or between a job's polls, and the call returns the context's error.
package miraklseller
