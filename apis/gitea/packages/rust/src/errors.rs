use std::fmt;

use crate::Error;
use crate::runtime::ErrorContext;

/// The class of a failed call.
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
#[non_exhaustive]
pub enum ErrorKind {
    /// HTTP 400.
    BadRequest,
    /// HTTP 401: the credentials are missing or wrong, or a one-time password is needed.
    Authentication,
    /// HTTP 403: the credentials do not allow the call.
    Permission,
    /// HTTP 404. Gitea also answers 404 for a private repository the credentials cannot see.
    NotFound,
    /// HTTP 409, such as for a repository or branch that already exists.
    Conflict,
    /// HTTP 422: Gitea refused the request's fields.
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
    /// A success response that could not be read as the API declares it, or a `Link` header that
    /// points back to a page already sent.
    Decode,
    /// A job that had not ended by the deadline. No Gitea operation waits on a job, so this kind
    /// never occurs; the shared runtime defines it.
    JobTimeout,
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

/// Maps on status first, then reads the `message` of Gitea's JSON error body, when it has one, into
/// [`Error::detail`].
pub(crate) fn to_error(context: ErrorContext) -> Error {
    let kind = error_kind(context.status);
    let detail = context
        .json
        .as_ref()
        .and_then(|body| body.get("message")?.as_str())
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

    fn context(status: u16, json: Option<Value>, text: &str) -> ErrorContext {
        let mut headers = HeaderMap::new();
        headers.insert("retry-after", HeaderValue::from_static("7"));
        ErrorContext {
            status,
            headers,
            text: text.to_owned(),
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
            assert_eq!(to_error(context(status, None, "")).kind(), kind, "{status}");
        }
    }

    #[test]
    fn the_message_and_raw_body_are_kept() {
        let text =
            r#"{"message":"[Title]: Required","url":"https://gitea.example.test/api/swagger"}"#;
        let body = json!({"message": "[Title]: Required", "url": "https://gitea.example.test/api/swagger"});
        let error = to_error(context(422, Some(body), text));
        assert_eq!(error.status(), Some(422));
        assert_eq!(error.detail(), Some("[Title]: Required"));
        assert_eq!(error.raw_body(), Some(text));
        assert_eq!(error.retry_after(), Some("7"));
        assert_eq!(
            error.to_string(),
            "HTTP 422 (validation): [Title]: Required"
        );
    }

    #[test]
    fn a_body_that_is_not_gitea_json_has_no_detail() {
        for json in [None, Some(json!({"message": 3})), Some(json!(["message"]))] {
            let error = to_error(context(403, json, "forbidden"));
            assert_eq!(error.detail(), None);
            assert_eq!(error.raw_body(), Some("forbidden"));
            assert_eq!(error.to_string(), "HTTP 403 (permission)");
        }
    }
}
