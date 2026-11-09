use std::fmt;

use crate::Error;
use crate::runtime::ErrorContext;

/// The class of a failed call.
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
#[non_exhaustive]
pub enum ErrorKind {
    /// HTTP 400.
    BadRequest,
    /// HTTP 401: the token is missing, wrong or revoked.
    Authentication,
    /// HTTP 403: the token lacks the scope, or the request did not come from an allowed IP address.
    Permission,
    /// HTTP 404.
    NotFound,
    /// HTTP 409.
    Conflict,
    /// HTTP 422.
    Validation,
    /// HTTP 429, after retries.
    RateLimited,
    /// HTTP 5xx, after retries.
    Server,
    /// Any other status.
    Api,
    /// No response in time, after retries.
    Timeout,
    /// The connection failed or dropped before a full response, after retries.
    Connection,
    /// A success response that could not be read as the API declares it.
    Decode,
}

impl ErrorKind {
    /// The kind's name, such as `not_found`.
    pub fn as_str(self) -> &'static str {
        match self {
            Self::BadRequest => "bad_request",
            Self::Authentication => "authentication",
            Self::Permission => "permission",
            Self::NotFound => "not_found",
            Self::Conflict => "conflict",
            Self::Validation => "validation",
            Self::RateLimited => "rate_limited",
            Self::Server => "server",
            Self::Api => "api",
            Self::Timeout => "timeout",
            Self::Connection => "connection",
            Self::Decode => "decode",
        }
    }
}

impl fmt::Display for ErrorKind {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.write_str(self.as_str())
    }
}

fn error_kind(status: u16) -> ErrorKind {
    match status {
        400 => ErrorKind::BadRequest,
        401 => ErrorKind::Authentication,
        403 => ErrorKind::Permission,
        404 => ErrorKind::NotFound,
        409 => ErrorKind::Conflict,
        422 => ErrorKind::Validation,
        429 => ErrorKind::RateLimited,
        500.. => ErrorKind::Server,
        _ => ErrorKind::Api,
    }
}

/// Maps on status alone. Mercury declares no error body, so the body is kept as text.
pub(crate) fn to_error(context: ErrorContext) -> Error {
    let kind = error_kind(context.status);
    Error::new(kind, format!("HTTP {} ({kind})", context.status))
        .with_status(context.status)
        .with_retry_after(context.header("retry-after"))
        .with_raw_body(Some(context.text))
}

#[cfg(test)]
mod tests {
    use reqwest::header::{HeaderMap, HeaderValue};

    use super::*;

    fn context(status: u16, text: &str) -> ErrorContext {
        let mut headers = HeaderMap::new();
        headers.insert("retry-after", HeaderValue::from_static("7"));
        ErrorContext {
            status,
            headers,
            text: text.to_owned(),
            json: None,
        }
    }

    #[test]
    fn statuses_map_to_kinds() {
        let cases = [
            (400, ErrorKind::BadRequest),
            (401, ErrorKind::Authentication),
            (403, ErrorKind::Permission),
            (404, ErrorKind::NotFound),
            (409, ErrorKind::Conflict),
            (422, ErrorKind::Validation),
            (429, ErrorKind::RateLimited),
            (503, ErrorKind::Server),
            (418, ErrorKind::Api),
        ];
        for (status, kind) in cases {
            assert_eq!(to_error(context(status, "")).kind(), kind, "{status}");
        }
    }

    #[test]
    fn the_raw_body_and_retry_after_are_kept() {
        let error = to_error(context(409, "duplicate"));
        assert_eq!(error.status(), Some(409));
        assert_eq!(error.raw_body(), Some("duplicate"));
        assert_eq!(error.retry_after(), Some("7"));
        assert_eq!(error.to_string(), "HTTP 409 (conflict)");
    }
}
