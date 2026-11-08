// Package etsyseller is an unofficial client for the Etsy Open API v3. This project is unofficial
// and is not affiliated with, endorsed by, or supported by Etsy.
//
// The term 'Etsy' is a trademark of Etsy, Inc. This Application uses Etsy's API, but is not
// endorsed or certified by Etsy.
//
// It is an alpha, tested only against a mock built from the public spec, never against the live API.
//
// Every call takes a [context.Context]. Cancelling it stops the call, including any wait before a
// retry, and the call returns the context's error.
package etsyseller
