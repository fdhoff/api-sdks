// Package gitearest is an unofficial client for the Gitea API. Not affiliated with, endorsed by or
// sponsored by the Gitea project or Gitea Limited.
//
// Every Gitea instance has its own URL, so [NewClient] always takes the instance's URL and adds
// /api/v1 itself. The API matches the pinned Gitea release named in the README.
//
// It is an alpha, tested against a mock built from the spec and a disposable Gitea container.
//
// Every call takes a [context.Context]. Cancelling it stops the call, including any wait before a
// retry, and the call returns the context's error.
package gitearest
