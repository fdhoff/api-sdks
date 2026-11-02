use std::fmt;

use serde_json::Value;

use crate::Error;
use crate::runtime::ErrorContext;

const BOT_CHALLENGE_CODE: &str = "bot-need-challenge";

/// The class of a failed call.
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
#[non_exhaustive]
pub enum ErrorKind {
    /// HTTP 400.
    BadRequest,
    /// HTTP 401.
    Authentication,
    /// HTTP 403 that is neither of the two below.
    Permission,
    /// HTTP 403 HTML block from the firewall. Give [`Error::cf_ray`] to your seller contact.
    WafBlocked,
    /// HTTP 403 from bot management.
    BotChallenge,
    /// HTTP 404.
    NotFound,
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
            Self::WafBlocked => "waf_blocked",
            Self::BotChallenge => "bot_challenge",
            Self::NotFound => "not_found",
            Self::Validation => "validation",
            Self::RateLimited => "rate_limited",
            Self::Server => "server",
            Self::Api => "api",
            Self::Timeout => "timeout",
            Self::Connection => "connection",
            Self::Decode => "decode",
        }
    }

    /// Whether this is any kind of 403: `Permission`, `WafBlocked` or `BotChallenge`.
    pub fn is_permission(self) -> bool {
        matches!(
            self,
            Self::Permission | Self::WafBlocked | Self::BotChallenge
        )
    }
}

impl fmt::Display for ErrorKind {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.write_str(self.as_str())
    }
}

fn text(value: Option<&Value>) -> Option<String> {
    match value? {
        Value::Null => None,
        Value::String(text) => Some(text.clone()),
        other => Some(other.to_string()),
    }
}

fn first_error_code(body: Option<&Value>) -> Option<String> {
    text(body?.get("errors")?.get(0)?.get("code"))
}

fn error_code(body: Option<&Value>) -> Option<String> {
    text(body.and_then(|body| body.get("error")?.get("code"))).or_else(|| first_error_code(body))
}

fn error_kind(context: &ErrorContext) -> ErrorKind {
    match context.status {
        403 if first_error_code(context.json.as_ref()).as_deref() == Some(BOT_CHALLENGE_CODE) => {
            ErrorKind::BotChallenge
        }
        403 if context.header("cf-ray").is_some() && context.json.is_none() => {
            ErrorKind::WafBlocked
        }
        403 => ErrorKind::Permission,
        400 => ErrorKind::BadRequest,
        401 => ErrorKind::Authentication,
        404 => ErrorKind::NotFound,
        422 => ErrorKind::Validation,
        429 => ErrorKind::RateLimited,
        500.. => ErrorKind::Server,
        _ => ErrorKind::Api,
    }
}

/// Maps on status first, then reads the body best-effort.
pub(crate) fn to_error(context: ErrorContext) -> Error {
    let kind = error_kind(&context);
    let body = context.json.as_ref();
    let code = error_code(body);
    let mut message = format!("HTTP {} ({kind})", context.status);
    if let Some(code) = &code {
        message = format!("{message}: {code}");
    }
    Error::new(kind, message)
        .with_status(context.status)
        .with_code(code)
        .with_request_id(text(body.and_then(|body| body.get("requestId"))))
        .with_retry_after(context.header("retry-after"))
        .with_cf_ray(context.header("cf-ray"))
        .with_raw_body(Some(context.text))
}

#[cfg(test)]
mod tests {
    use reqwest::header::{HeaderMap, HeaderValue};
    use serde_json::json;

    use super::*;

    fn context(status: u16, json: Option<Value>, cf_ray: bool) -> ErrorContext {
        let mut headers = HeaderMap::new();
        if cf_ray {
            headers.insert("cf-ray", HeaderValue::from_static("0000000000000000-CDG"));
        }
        let text = json.as_ref().map(Value::to_string).unwrap_or_default();
        ErrorContext {
            status,
            headers,
            text,
            json,
        }
    }

    #[test]
    fn a_403_is_split_three_ways() {
        let challenge = json!({"errors": [{"code": BOT_CHALLENGE_CODE}]});
        assert_eq!(
            to_error(context(403, Some(challenge), true)).kind(),
            ErrorKind::BotChallenge
        );
        let blocked = to_error(context(403, None, true));
        assert_eq!(blocked.kind(), ErrorKind::WafBlocked);
        assert_eq!(blocked.cf_ray(), Some("0000000000000000-CDG"));
        assert_eq!(
            to_error(context(403, Some(json!({})), true)).kind(),
            ErrorKind::Permission
        );
        assert!(blocked.kind().is_permission());
    }

    #[test]
    fn codes_come_from_either_error_shape() {
        let single = to_error(context(
            401,
            Some(json!({"error": {"code": "a"}, "requestId": "r-1"})),
            false,
        ));
        assert_eq!(
            (single.code(), single.request_id()),
            (Some("a"), Some("r-1"))
        );
        let listed = to_error(context(
            422,
            Some(json!({"errors": [{"code": "b"}]})),
            false,
        ));
        assert_eq!(
            (listed.kind(), listed.code()),
            (ErrorKind::Validation, Some("b"))
        );
    }

    #[test]
    fn unlisted_statuses_are_api_errors() {
        assert_eq!(to_error(context(413, None, false)).kind(), ErrorKind::Api);
        assert_eq!(
            to_error(context(503, None, false)).kind(),
            ErrorKind::Server
        );
    }
}
