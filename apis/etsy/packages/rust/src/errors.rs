use std::fmt;

use crate::Error;
use crate::runtime::ErrorContext;

/// The class of a failed call.
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
#[non_exhaustive]
pub enum ErrorKind {
    /// HTTP 400.
    BadRequest,
    /// HTTP 401, after any refresh of the access token.
    Authentication,
    /// HTTP 403.
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
    /// Any other status, redirects included.
    Api,
    /// No response in time, after retries.
    Timeout,
    /// The connection failed or dropped before a full response, after retries.
    Connection,
    /// A success response that could not be read as the API declares it.
    Decode,
    /// A job that had not ended by the deadline. [`Error::job_status`] holds its last status.
    JobTimeout,
    /// A call the client refuses before sending anything, such as a refresh with no refresh token.
    InvalidInput,
    /// The system could not provide what the call needs, such as random bytes.
    System,
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
            Self::JobTimeout => "job_timeout",
            Self::InvalidInput => "invalid_input",
            Self::System => "system",
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

/// Maps on status first, then reads the body's `error` text best-effort.
pub(crate) fn to_error(context: ErrorContext) -> Error {
    let kind = error_kind(context.status);
    let detail = context
        .json
        .as_ref()
        .and_then(|body| body.get("error")?.as_str())
        .map(str::to_owned);
    let message = match &detail {
        Some(detail) => format!("HTTP {} ({kind}): {detail}", context.status),
        None => format!("HTTP {} ({kind})", context.status),
    };
    Error::new(kind, message)
        .with_status(context.status)
        .with_detail(detail)
        .with_retry_after(context.header("retry-after"))
        .with_raw_body(Some(context.text))
}

#[cfg(test)]
mod tests {
    use reqwest::header::{HeaderMap, HeaderValue};
    use serde_json::{Value, json};

    use super::*;

    fn context(status: u16, json: Option<Value>) -> ErrorContext {
        let mut headers = HeaderMap::new();
        headers.insert("retry-after", HeaderValue::from_static("3"));
        let text = json.as_ref().map(Value::to_string).unwrap_or_default();
        ErrorContext {
            status,
            headers,
            text,
            json,
        }
    }

    #[test]
    fn statuses_map_to_kinds() {
        let kinds = [
            (400, ErrorKind::BadRequest),
            (401, ErrorKind::Authentication),
            (403, ErrorKind::Permission),
            (404, ErrorKind::NotFound),
            (409, ErrorKind::Conflict),
            (422, ErrorKind::Validation),
            (429, ErrorKind::RateLimited),
            (503, ErrorKind::Server),
            (302, ErrorKind::Api),
            (418, ErrorKind::Api),
        ];
        for (status, kind) in kinds {
            assert_eq!(to_error(context(status, None)).kind(), kind, "{status}");
        }
    }

    #[test]
    fn the_error_text_is_the_detail() {
        let error = to_error(context(
            400,
            Some(json!({"error": "Synthetic bad request"})),
        ));
        assert_eq!(error.detail(), Some("Synthetic bad request"));
        assert_eq!(
            error.to_string(),
            "HTTP 400 (bad_request): Synthetic bad request"
        );
        assert_eq!(error.retry_after(), Some("3"));
        assert_eq!(
            to_error(context(400, Some(json!({"error": {"nested": 1}})))).detail(),
            None
        );
    }
}
