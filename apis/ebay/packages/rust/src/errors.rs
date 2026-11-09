use std::fmt;

use serde_json::Value;

use crate::Error;
use crate::runtime::ErrorContext;

/// The class of a failed call.
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
#[non_exhaustive]
pub enum ErrorKind {
    /// HTTP 400.
    BadRequest,
    /// HTTP 401, after any new token.
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
    /// A call the client refuses before sending anything, such as a user operation with no user token.
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

/// One `name` and `value` of an [`ErrorDetail`].
#[derive(Clone, Debug, Default, PartialEq, Eq)]
#[non_exhaustive]
pub struct ErrorParameter {
    pub name: Option<String>,
    pub value: Option<String>,
}

/// One entry of an eBay error response's `errors` list. A field of the wrong type reads as `None`.
#[derive(Clone, Debug, Default, PartialEq, Eq)]
#[non_exhaustive]
pub struct ErrorDetail {
    pub error_id: Option<i64>,
    pub domain: Option<String>,
    pub subdomain: Option<String>,
    pub category: Option<String>,
    pub message: Option<String>,
    pub long_message: Option<String>,
    pub parameters: Vec<ErrorParameter>,
}

fn text(item: &Value, name: &str) -> Option<String> {
    item.get(name).and_then(Value::as_str).map(str::to_owned)
}

fn details(body: &Value) -> Vec<ErrorDetail> {
    let items = body
        .get("errors")
        .and_then(Value::as_array)
        .map(Vec::as_slice)
        .unwrap_or_default();
    items
        .iter()
        .filter(|item| item.is_object())
        .map(|item| ErrorDetail {
            error_id: item.get("errorId").and_then(Value::as_i64),
            domain: text(item, "domain"),
            subdomain: text(item, "subdomain"),
            category: text(item, "category"),
            message: text(item, "message"),
            long_message: text(item, "longMessage"),
            parameters: item
                .get("parameters")
                .and_then(Value::as_array)
                .map(Vec::as_slice)
                .unwrap_or_default()
                .iter()
                .filter(|parameter| parameter.is_object())
                .map(|parameter| ErrorParameter {
                    name: text(parameter, "name"),
                    value: text(parameter, "value"),
                })
                .collect(),
        })
        .collect()
}

/// The `errors` list of a failed call's response body, best-effort. Empty when the call had no
/// response, or its body has no such list.
pub fn error_details(error: &Error) -> Vec<ErrorDetail> {
    error
        .raw_body()
        .and_then(|text| serde_json::from_str::<Value>(text).ok())
        .map(|body| details(&body))
        .unwrap_or_default()
}

/// Maps on status first, then reads the body best-effort: the first entry of its `errors` list gives
/// the detail and the code.
pub(crate) fn to_error(context: ErrorContext) -> Error {
    let kind = error_kind(context.status);
    let first = context
        .json
        .as_ref()
        .map(details)
        .unwrap_or_default()
        .into_iter()
        .next();
    let detail = first.as_ref().and_then(|first| first.message.clone());
    let code = first
        .and_then(|first| first.error_id)
        .map(|id| id.to_string());
    let message = match &detail {
        Some(detail) => format!("HTTP {} ({kind}): {detail}", context.status),
        None => format!("HTTP {} ({kind})", context.status),
    };
    Error::new(kind, message)
        .with_status(context.status)
        .with_detail(detail)
        .with_code(code)
        .with_retry_after(context.header("retry-after"))
        .with_raw_body(Some(context.text))
}

#[cfg(test)]
mod tests {
    use reqwest::header::{HeaderMap, HeaderValue};
    use serde_json::json;

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
    fn the_first_error_gives_the_detail_and_the_code() {
        let body = json!({"errors": [
            {"errorId": 25710, "domain": "API_INVENTORY", "category": "REQUEST", "message": "Synthetic not found",
             "longMessage": "A synthetic resource was not found.", "parameters": [{"name": "sku", "value": "S-1"}]},
            {"errorId": 25001, "message": "Second"},
        ]});
        let error = to_error(context(404, Some(body)));
        assert_eq!(error.detail(), Some("Synthetic not found"));
        assert_eq!(error.code(), Some("25710"));
        assert_eq!(
            error.to_string(),
            "HTTP 404 (not_found): Synthetic not found"
        );
        assert_eq!(error.retry_after(), Some("3"));
        let details = error_details(&error);
        assert_eq!(details.len(), 2);
        assert_eq!(details[0].error_id, Some(25710));
        assert_eq!(details[0].domain.as_deref(), Some("API_INVENTORY"));
        assert_eq!(
            details[0].long_message.as_deref(),
            Some("A synthetic resource was not found.")
        );
        assert_eq!(
            details[0].parameters,
            vec![ErrorParameter {
                name: Some("sku".into()),
                value: Some("S-1".into())
            }]
        );
        assert_eq!(details[1].message.as_deref(), Some("Second"));
    }

    #[test]
    fn fields_of_the_wrong_type_read_as_none() {
        let body = json!({"errors": [{"errorId": "25710", "message": {"nested": 1}, "parameters": "none"}, "text"]});
        let error = to_error(context(400, Some(body)));
        assert_eq!(error.detail(), None);
        assert_eq!(error.code(), None);
        assert_eq!(error.to_string(), "HTTP 400 (bad_request)");
        let details = error_details(&error);
        assert_eq!(details.len(), 1);
        assert_eq!(details[0], ErrorDetail::default());
        assert!(error_details(&to_error(context(500, None))).is_empty());
        assert!(
            error_details(&to_error(context(
                400,
                Some(json!({"errors": {"errorId": 1}}))
            )))
            .is_empty()
        );
    }
}
