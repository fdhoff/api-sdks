use std::fmt;

use reqwest::header::HeaderMap;
use serde_json::Value;

use crate::ErrorKind;

type Source = Box<dyn std::error::Error + Send + Sync>;

/// The error every failed call returns. Match on [`Error::kind`].
pub struct Error {
    inner: Box<Inner>,
}

#[derive(Debug)]
struct Inner {
    kind: ErrorKind,
    message: String,
    status: Option<u16>,
    raw_body: Option<String>,
    code: Option<String>,
    detail: Option<String>,
    request_id: Option<String>,
    retry_after: Option<String>,
    cf_ray: Option<String>,
    source: Option<Source>,
}

impl Error {
    pub(crate) fn new(kind: ErrorKind, message: impl Into<String>) -> Self {
        Self {
            inner: Box::new(Inner {
                kind,
                message: message.into(),
                status: None,
                raw_body: None,
                code: None,
                detail: None,
                request_id: None,
                retry_after: None,
                cf_ray: None,
                source: None,
            }),
        }
    }

    pub(crate) fn with_status(mut self, status: u16) -> Self {
        self.inner.status = Some(status);
        self
    }

    pub(crate) fn with_raw_body(mut self, raw_body: Option<String>) -> Self {
        self.inner.raw_body = raw_body.filter(|text| !text.is_empty());
        self
    }

    #[allow(
        dead_code,
        reason = "an API whose errors carry no such field leaves it unset"
    )]
    pub(crate) fn with_code(mut self, code: Option<String>) -> Self {
        self.inner.code = code;
        self
    }

    #[allow(
        dead_code,
        reason = "an API whose errors carry no such field leaves it unset"
    )]
    pub(crate) fn with_detail(mut self, detail: Option<String>) -> Self {
        self.inner.detail = detail;
        self
    }

    #[allow(
        dead_code,
        reason = "an API whose errors carry no such field leaves it unset"
    )]
    pub(crate) fn with_request_id(mut self, request_id: Option<String>) -> Self {
        self.inner.request_id = request_id;
        self
    }

    pub(crate) fn with_retry_after(mut self, retry_after: Option<String>) -> Self {
        self.inner.retry_after = retry_after;
        self
    }

    #[allow(
        dead_code,
        reason = "an API whose errors carry no such field leaves it unset"
    )]
    pub(crate) fn with_cf_ray(mut self, cf_ray: Option<String>) -> Self {
        self.inner.cf_ray = cf_ray;
        self
    }

    pub(crate) fn map_message(mut self, map: impl FnOnce(&str) -> String) -> Self {
        self.inner.message = map(&self.inner.message);
        self
    }

    pub(crate) fn with_source(mut self, source: impl Into<Source>) -> Self {
        self.inner.source = Some(source.into());
        self
    }

    /// The class of failure.
    pub fn kind(&self) -> ErrorKind {
        self.inner.kind
    }

    /// The HTTP status, when there was a response.
    pub fn status(&self) -> Option<u16> {
        self.inner.status
    }

    /// The response body, with the token removed.
    pub fn raw_body(&self) -> Option<&str> {
        self.inner.raw_body.as_deref()
    }

    /// The error code from the response body, when it has one.
    pub fn code(&self) -> Option<&str> {
        self.inner.code.as_deref()
    }

    /// The error text from the response body, when it has one, with every secret removed.
    pub fn detail(&self) -> Option<&str> {
        self.inner.detail.as_deref()
    }

    /// The request ID from the response body, when it has one.
    pub fn request_id(&self) -> Option<&str> {
        self.inner.request_id.as_deref()
    }

    /// The `Retry-After` header, as sent.
    pub fn retry_after(&self) -> Option<&str> {
        self.inner.retry_after.as_deref()
    }

    /// The `cf-ray` header, as sent.
    pub fn cf_ray(&self) -> Option<&str> {
        self.inner.cf_ray.as_deref()
    }
}

impl fmt::Debug for Error {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        self.inner.fmt(f)
    }
}

impl fmt::Display for Error {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.write_str(&self.inner.message)
    }
}

impl std::error::Error for Error {
    fn source(&self) -> Option<&(dyn std::error::Error + 'static)> {
        self.inner.source.as_deref().map(|source| source as _)
    }
}

/// A failed response, with the token already removed from `text` and `json`.
#[derive(Debug)]
pub struct ErrorContext {
    pub status: u16,
    pub headers: HeaderMap,
    pub text: String,
    pub json: Option<Value>,
}

impl ErrorContext {
    /// A header's value, when it is present and readable.
    pub fn header(&self, name: &str) -> Option<String> {
        let value = self.headers.get(name)?.to_str().ok()?;
        Some(value.to_owned())
    }
}
