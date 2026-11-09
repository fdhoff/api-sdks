# Changelog

This module follows semantic versioning and stays on 0.x until outside users confirm its behaviour against the live API.

## 0.1.0-alpha.1 (unreleased)

The first alpha.

* Typed client for the 116 current operations of Mirakl's seller API, generated from the public spec, with `context.Context` on every call and Mirakl's API code, such as OR11, in each method's doc comment. The 11 deprecated operations are left out.
* A base URL you supply for your operator's Mirakl instance, since there is no shared host.
* Your shop API key as the whole `Authorization` header through `APIKey`, sent only to that base URL and redacted from errors and logs, or credentials of your own through the `Credentials` interface.
* `WithShopID` sets the shop for every call, and a call's own `ShopID` wins.
* Iterators on the 21 paged operations: `offset` and `max` up to `total_count`, and `page_token` from each page's `next_page_token`.
* `Wait` methods that poll an import or export until it ends, and return its final status, done or failed. A deadline returns an error matching `ErrJobTimeout`.
* `Client.DownloadURL` fetches an export's file URL, sending the key only to the base URL's origin, never across a redirect to another one.
* Error reports, invoices and documents download as their exact bytes.
* Typed errors with the status and raw body, and retries and rate-limit handling.
