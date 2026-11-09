use std::collections::{HashMap, VecDeque};
use std::fmt;
use std::io::Read;
use std::pin::Pin;
use std::sync::Arc;
use std::sync::atomic::{AtomicU64, Ordering};
use std::time::{Duration, SystemTime};

use futures_core::Stream;
use reqwest::header::{
    ACCEPT_ENCODING, CONTENT_ENCODING, CONTENT_LENGTH, CONTENT_TYPE, HeaderMap, HeaderName,
    HeaderValue,
};
use reqwest::{Method, StatusCode, multipart, redirect};
use serde::de::DeserializeOwned;
use serde_json::Value;

use super::credentials::{AuthRequest, Credentials, redact_with, redactions};
use super::error::{Error, ErrorContext};
use super::request::{Body, Operation, Paging, Part, Request};
use crate::ErrorKind;

/// A backoff doubles per retry, and this keeps the shift in range for any retry count.
const MAX_BACKOFF_DOUBLINGS: u32 = 20;

/// A stream of every item across all pages. It ends after yielding an error.
pub type Items<T> = Pin<Box<dyn Stream<Item = Result<T, Error>> + Send>>;

/// Configures a [`Transport`].
pub struct Settings {
    /// Where an operation with no host key is sent.
    pub base_url: String,
    /// The base URL for each host key. A request is never sent to a host that is not here.
    pub hosts: HashMap<String, String>,
    pub credentials: Arc<dyn Credentials>,
    pub headers: HeaderMap,
    /// A value for each default-able header, sent by the operations that declare it when the call
    /// gives none. Names match without regard to case.
    pub header_defaults: HashMap<String, String>,
    pub to_error: fn(ErrorContext) -> Error,
    pub timeout: Duration,
    pub max_retries: u32,
    pub retry_base_delay: Duration,
    pub rate_limit_wait: Duration,
    pub max_retry_wait: Duration,
    /// A caller's own client. Without one, the transport builds a client that never follows a
    /// redirect.
    pub http: Option<reqwest::Client>,
}

/// Sends requests, applying the timeout, retry and redaction rules.
pub struct Transport {
    settings: Settings,
    http: reqwest::Client,
    refreshing: tokio::sync::Mutex<()>,
    /// Counts refreshes, so that a call whose credentials were refreshed since it sent them retries
    /// without another.
    generation: AtomicU64,
}

impl fmt::Debug for Transport {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("Transport")
            .field("base_url", &self.settings.base_url)
            .finish_non_exhaustive()
    }
}

struct Answer {
    status: u16,
    headers: HeaderMap,
    body: Vec<u8>,
}

fn is_json(headers: &HeaderMap) -> bool {
    let content_type = headers
        .get(CONTENT_TYPE)
        .and_then(|value| value.to_str().ok())
        .unwrap_or_default();
    content_type.to_ascii_lowercase().contains("json")
}

/// Decompresses after the whole body has arrived, so that a failure here means a corrupt body and
/// never a dropped connection.
fn decompress(headers: &HeaderMap, body: Vec<u8>) -> std::io::Result<Vec<u8>> {
    let gzip = headers
        .get(CONTENT_ENCODING)
        .and_then(|value| value.to_str().ok())
        .is_some_and(|value| value.trim().eq_ignore_ascii_case("gzip"));
    if body.is_empty() || !gzip {
        return Ok(body);
    }
    let mut decoded = Vec::new();
    flate2::read::MultiGzDecoder::new(body.as_slice()).read_to_end(&mut decoded)?;
    Ok(decoded)
}

fn translate(error: reqwest::Error) -> Error {
    if error.is_timeout() {
        return Error::new(ErrorKind::Timeout, "the request timed out").with_source(error);
    }
    if error.is_builder() {
        return Error::new(ErrorKind::Api, "the request cannot be built").with_source(error);
    }
    Error::new(ErrorKind::Connection, "the connection failed").with_source(error)
}

/// Reads `Retry-After`, returning `None` when it is unusable or in the past. A number of seconds
/// too large to hold comes back as the longest duration, which then exceeds any maximum wait.
pub fn retry_after(value: Option<&str>, now: SystemTime) -> Option<Duration> {
    let value = value?.trim();
    if value.is_empty() {
        return None;
    }
    if value.bytes().all(|byte| byte.is_ascii_digit()) {
        return Some(
            value
                .parse()
                .map(Duration::from_secs)
                .unwrap_or(Duration::MAX),
        );
    }
    let when = httpdate::parse_http_date(value).ok()?;
    when.duration_since(now).ok().filter(|wait| !wait.is_zero())
}

/// The body's content type and bytes, encoded once so that credentials see exactly what is sent.
async fn encode(body: &Body) -> Result<(Option<String>, Vec<u8>), Error> {
    let parts = match body {
        Body::Empty => return Ok((None, Vec::new())),
        Body::Json(bytes) => return Ok((Some("application/json".to_owned()), bytes.clone())),
        Body::Form(fields) => {
            let text = url::form_urlencoded::Serializer::new(String::new())
                .extend_pairs(fields)
                .finish();
            return Ok((
                Some("application/x-www-form-urlencoded".to_owned()),
                text.into_bytes(),
            ));
        }
        Body::Multipart(parts) => parts,
    };
    let form = form(parts);
    let content_type = format!("multipart/form-data; boundary={}", form.boundary());
    let mut stream = std::pin::pin!(form.into_stream());
    let mut bytes = Vec::new();
    while let Some(chunk) = futures_util::StreamExt::next(&mut stream).await {
        bytes.extend_from_slice(&chunk.map_err(translate)?);
    }
    Ok((Some(content_type), bytes))
}

fn form(parts: &[Part]) -> multipart::Form {
    parts
        .iter()
        .fold(multipart::Form::new(), |form, part| match part {
            Part::Text { name, value } => form.text(name.clone(), value.clone()),
            Part::File { name, file } => {
                let filename = file.name.clone().unwrap_or_else(|| name.clone());
                let mut headers = HeaderMap::new();
                headers.insert(
                    CONTENT_TYPE,
                    HeaderValue::from_static("application/octet-stream"),
                );
                let part = multipart::Part::bytes(file.content.clone())
                    .file_name(filename)
                    .headers(headers);
                form.part(name.clone(), part)
            }
        })
}

/// `defaults` keyed by lowercase name.
fn by_lowercase(defaults: HashMap<String, String>) -> Result<HashMap<String, String>, Error> {
    let mut clashes: Vec<&str> = defaults
        .keys()
        .filter(|name| {
            defaults
                .keys()
                .any(|other| other != *name && other.eq_ignore_ascii_case(name))
        })
        .map(String::as_str)
        .collect();
    if !clashes.is_empty() {
        clashes.sort_unstable();
        let message = format!(
            "header_defaults has names that differ only by case: {}",
            clashes.join(", ")
        );
        return Err(Error::new(ErrorKind::Api, message));
    }
    Ok(defaults
        .into_iter()
        .map(|(name, value)| (name.to_ascii_lowercase(), value))
        .collect())
}

impl Transport {
    /// Builds a transport. Its own client never follows a redirect: a redirect is reported as a
    /// failure, so the token cannot be sent anywhere but the configured server. A caller's client
    /// keeps its own redirect policy. Headers are sent on each request, so either client sends them.
    /// Header defaults whose names differ only by case are an error.
    pub fn new(mut settings: Settings) -> Result<Self, Error> {
        settings.header_defaults = by_lowercase(std::mem::take(&mut settings.header_defaults))?;
        settings
            .headers
            .insert(ACCEPT_ENCODING, HeaderValue::from_static("gzip"));
        let http = match settings.http.take() {
            Some(http) => http,
            None => reqwest::Client::builder()
                .redirect(redirect::Policy::none())
                .build()
                .map_err(|error| {
                    Error::new(ErrorKind::Api, "the HTTP client cannot be built").with_source(error)
                })?,
        };
        Ok(Self {
            settings,
            http,
            refreshing: tokio::sync::Mutex::new(()),
            generation: AtomicU64::new(0),
        })
    }

    /// The base URL for a request's host key, or an error before anything is sent.
    fn base_url(&self, request: &Request) -> Result<&str, Error> {
        let Some(key) = request.host else {
            return Ok(&self.settings.base_url);
        };
        self.settings
            .hosts
            .get(key)
            .map(String::as_str)
            .ok_or_else(|| {
                Error::new(
                    ErrorKind::Api,
                    format!("no base URL is configured for host {key}"),
                )
            })
    }

    fn header_default(&self, name: &str) -> Option<&str> {
        self.settings
            .header_defaults
            .get(&name.to_ascii_lowercase())
            .map(String::as_str)
    }

    fn redact(&self, text: &str) -> String {
        redact_with(&redactions(self.settings.credentials.as_ref()), text)
    }

    /// The request for one attempt, with the credentials applied. A header that holds a secret is
    /// marked sensitive, so that a debug print of it shows nothing.
    pub(super) async fn authorize(
        &self,
        request: &Request,
        method: Method,
        content_type: Option<&str>,
        body: Vec<u8>,
    ) -> Result<AuthRequest, Error> {
        let mut headers = self.settings.headers.clone();
        if let Some(content_type) = content_type {
            let value = HeaderValue::from_str(content_type).map_err(|error| {
                Error::new(ErrorKind::Api, "the content type is not valid").with_source(error)
            })?;
            headers.insert(CONTENT_TYPE, value);
        }
        for (name, value) in &request.headers {
            let Some(value) = value.as_deref().or_else(|| self.header_default(name)) else {
                continue;
            };
            let name = HeaderName::from_bytes(name.as_bytes()).map_err(|error| {
                Error::new(
                    ErrorKind::Api,
                    format!("the header name {name} is not valid"),
                )
                .with_source(error)
            })?;
            let value = HeaderValue::from_str(value).map_err(|error| {
                Error::new(
                    ErrorKind::Api,
                    format!("the {name} header value is not valid"),
                )
                .with_source(error)
            })?;
            headers.insert(name, value);
        }
        let url = request.url(self.base_url(request)?);
        let mut auth = AuthRequest {
            method,
            url,
            headers,
            body,
            operation: request.operation,
        };
        let credentials = self.settings.credentials.as_ref();
        credentials
            .apply(&mut auth)
            .await
            .map_err(|error| error.map_message(|text| self.redact(text)))?;
        let secrets: Vec<String> = credentials
            .secrets()
            .into_iter()
            .filter(|secret| !secret.is_empty())
            .collect();
        for value in auth.headers.values_mut() {
            let bytes = value.as_bytes();
            if secrets.iter().any(|secret| {
                bytes
                    .windows(secret.len())
                    .any(|window| window == secret.as_bytes())
            }) {
                value.set_sensitive(true);
            }
        }
        Ok(auth)
    }

    /// Lets calls waiting on a refresh share it.
    async fn refresh(&self, auth: &AuthRequest, generation: u64) -> Result<bool, Error> {
        let _refreshing = self.refreshing.lock().await;
        if self.generation.load(Ordering::Acquire) != generation {
            return Ok(true);
        }
        let refreshed = self
            .settings
            .credentials
            .refresh(auth)
            .await
            .map_err(|error| error.map_message(|text| self.redact(text)))?;
        if refreshed {
            self.generation.fetch_add(1, Ordering::AcqRel);
        }
        Ok(refreshed)
    }

    fn log(&self, level: log::Level, message: fmt::Arguments<'_>) {
        if log::log_enabled!(level) {
            log::log!(level, "{}", self.redact(&message.to_string()));
        }
    }

    fn failure(&self, answer: Answer) -> Error {
        let text = self.redact(&String::from_utf8_lossy(&answer.body));
        let json = serde_json::from_str(&text).ok();
        (self.settings.to_error)(ErrorContext {
            status: answer.status,
            headers: answer.headers,
            text,
            json,
        })
    }

    fn decode_error(&self, message: &str, answer: &Answer) -> Error {
        let text = self.redact(&String::from_utf8_lossy(&answer.body));
        Error::new(ErrorKind::Decode, message)
            .with_status(answer.status)
            .with_raw_body(Some(text))
    }

    async fn send(&self, auth: &AuthRequest) -> Result<Answer, Error> {
        let mut outgoing = self
            .http
            .request(auth.method.clone(), &auth.url)
            .headers(auth.headers.clone());
        if !auth.body.is_empty() {
            outgoing = outgoing.body(auth.body.clone());
        } else if matches!(auth.method, Method::POST | Method::PUT)
            && !auth.headers.contains_key(CONTENT_LENGTH)
        {
            // The signer signs 0 for these methods, so send it rather than rely on hyper to.
            outgoing = outgoing.header(CONTENT_LENGTH, "0");
        }
        let incoming = outgoing.send().await.map_err(translate)?;
        let status = incoming.status().as_u16();
        let headers = incoming.headers().clone();
        let body = incoming.bytes().await.map_err(translate)?.to_vec();
        Ok(Answer {
            status,
            headers,
            body,
        })
    }

    /// One attempt, with one deadline from sending the request to reading the last byte.
    async fn attempt(&self, auth: &AuthRequest) -> Result<Answer, Error> {
        let sent = tokio::time::timeout(self.settings.timeout, self.send(auth));
        let Answer {
            status,
            headers,
            body,
        } = sent.await.map_err(|elapsed| {
            Error::new(ErrorKind::Timeout, "the request timed out").with_source(elapsed)
        })??;
        let success = StatusCode::from_u16(status).is_ok_and(|code| code.is_success());
        let body = match decompress(&headers, body) {
            Ok(body) => body,
            Err(error) if success => {
                return Err(Error::new(
                    ErrorKind::Decode,
                    "the response body cannot be decompressed",
                )
                .with_status(status)
                .with_source(error));
            }
            Err(_) => Vec::new(),
        };
        let method = &auth.method;
        self.log(
            log::Level::Debug,
            format_args!("response {method} {status} ({} bytes)", body.len()),
        );
        let answer = Answer {
            status,
            headers,
            body,
        };
        if !success {
            return Err(self.failure(answer));
        }
        Ok(answer)
    }

    fn retry_delay(&self, failure: &Error, method: &Method, tries: u32) -> Option<Duration> {
        let settings = &self.settings;
        if tries >= settings.max_retries {
            return None;
        }
        if failure.status() == Some(StatusCode::TOO_MANY_REQUESTS.as_u16()) {
            return match retry_after(failure.retry_after(), SystemTime::now()) {
                None => Some(settings.rate_limit_wait),
                Some(wait) => (wait <= settings.max_retry_wait).then_some(wait),
            };
        }
        let failed = matches!(failure.kind(), ErrorKind::Timeout | ErrorKind::Connection)
            || failure.status().is_some_and(|status| status >= 500);
        (*method == Method::GET && failed).then(|| {
            settings
                .retry_base_delay
                .saturating_mul(1 << tries.min(MAX_BACKOFF_DOUBLINGS))
        })
    }

    async fn fetch(&self, request: &Request) -> Result<Answer, Error> {
        if let Some(reason) = &request.invalid {
            return Err(Error::new(
                ErrorKind::Api,
                format!("the request body cannot be encoded: {reason}"),
            ));
        }
        let method = Method::from_bytes(request.operation.method.as_bytes()).map_err(|error| {
            Error::new(ErrorKind::Api, "the request method is not valid").with_source(error)
        })?;
        let (content_type, body) = encode(&request.body).await?;
        let mut tries = 0;
        let mut refreshed = false;
        loop {
            let generation = self.generation.load(Ordering::Acquire);
            let auth = self
                .authorize(
                    request,
                    method.clone(),
                    content_type.as_deref(),
                    body.clone(),
                )
                .await?;
            self.log(
                log::Level::Debug,
                format_args!("request {} {method} {}", request.operation.id, auth.url),
            );
            let failure = match self.attempt(&auth).await {
                Ok(answer) => return Ok(answer),
                Err(failure) => failure,
            };
            // An operation that sends no credentials, such as a token request made during a
            // refresh, has nothing to refresh.
            let secured = !request.operation.security.is_empty();
            if failure.status() == Some(StatusCode::UNAUTHORIZED.as_u16()) && !refreshed && secured
            {
                refreshed = true;
                if self.refresh(&auth, generation).await? {
                    self.log(
                        log::Level::Info,
                        format_args!("retrying after refreshing credentials"),
                    );
                    continue;
                }
            }
            let Some(delay) = self.retry_delay(&failure, &method, tries) else {
                return Err(failure);
            };
            let kind = failure.kind();
            self.log(
                log::Level::Info,
                format_args!("retrying after {delay:?}: {kind:?}"),
            );
            tokio::time::sleep(delay).await;
            tries += 1;
        }
    }

    fn decode<T: DeserializeOwned + Default>(
        &self,
        operation: &Operation,
        answer: &Answer,
    ) -> Result<T, Error> {
        if answer.body.is_empty() {
            if operation.returns_json && answer.status != StatusCode::NO_CONTENT.as_u16() {
                return Err(self.decode_error("the response body is empty", answer));
            }
            return Ok(T::default());
        }
        let value = if is_json(&answer.headers) {
            serde_json::from_slice(&answer.body)
                .map_err(|_| self.decode_error("the response body is not valid JSON", answer))?
        } else {
            Value::String(String::from_utf8_lossy(&answer.body).into_owned())
        };
        T::deserialize(value)
            .map_err(|_| self.decode_error("the response body does not fit its type", answer))
    }

    /// Sends one operation and decodes its response.
    pub async fn call<T: DeserializeOwned + Default>(&self, request: Request) -> Result<T, Error> {
        let answer = self.fetch(&request).await?;
        self.decode(request.operation, &answer)
    }

    /// The request for the page after this one. `None` means the last page.
    fn next_request(
        &self,
        request: &Request,
        page: &Value,
        answer: &Answer,
        received: usize,
    ) -> Result<Option<Request>, Error> {
        let items = request.operation.paging().items();
        if !page.get(items).is_some_and(Value::is_array) {
            return Err(self.decode_error(
                &format!("the {items} field of a page is not a list"),
                answer,
            ));
        }
        match request.operation.paging() {
            Paging::NextLink { link, params, .. } => {
                self.next_link(request, link, params, page, answer)
            }
            Paging::Offset { total, offset, .. } => {
                self.next_offset(request, total, offset, page, answer, received)
            }
        }
    }

    /// Reads the position out of a page's link and applies it to our own request. The link is
    /// never fetched: it could send the token to another host.
    fn next_link(
        &self,
        request: &Request,
        field: &str,
        params: &[&str],
        page: &Value,
        answer: &Answer,
    ) -> Result<Option<Request>, Error> {
        let link = match page.get(field) {
            None | Some(Value::Null) => return Ok(None),
            Some(Value::String(link)) if link.is_empty() => return Ok(None),
            Some(Value::String(link)) => link,
            Some(_) => {
                return Err(self.decode_error(&format!("the {field} link is not a string"), answer));
            }
        };
        let base = url::Url::parse("http://localhost/").expect("a valid base");
        let parsed = base.join(link).map_err(|_| {
            self.decode_error(&format!("the {field} link cannot be parsed"), answer)
        })?;
        let mut next = request.clone();
        let mut advanced = false;
        for marker in params {
            if !request.operation.query_params.contains(marker) {
                continue;
            }
            let Some((_, value)) = parsed
                .query_pairs()
                .find(|(name, value)| name == marker && !value.is_empty())
            else {
                continue;
            };
            advanced = advanced || request.query_value(marker) != Some(value.as_ref());
            next.set_query(marker, &value);
        }
        if !advanced {
            return Err(self.decode_error(
                &format!("the {field} link does not advance the iteration"),
                answer,
            ));
        }
        Ok(Some(next))
    }

    /// Moves the offset past the items received.
    fn next_offset(
        &self,
        request: &Request,
        total: &str,
        offset: &str,
        page: &Value,
        answer: &Answer,
        received: usize,
    ) -> Result<Option<Request>, Error> {
        if received == 0 {
            return Ok(None);
        }
        let start = match request.query_value(offset) {
            None => 0,
            Some(text) => text.parse::<u64>().map_err(|_| {
                self.decode_error(&format!("the {offset} parameter is not an integer"), answer)
            })?,
        };
        let position = start.saturating_add(received as u64);
        if page
            .get(total)
            .and_then(Value::as_f64)
            .is_some_and(|total| position as f64 >= total)
        {
            return Ok(None);
        }
        let mut next = request.clone();
        next.set_query(offset, &position.to_string());
        Ok(Some(next))
    }

    async fn page(&self, request: &Request) -> Result<(VecDeque<Value>, Option<Request>), Error> {
        let answer = self.fetch(request).await?;
        let page: Value = serde_json::from_slice(&answer.body).unwrap_or(Value::Null);
        if !page.is_object() {
            return Err(self.decode_error("a page is not a JSON object", &answer));
        }
        let items: VecDeque<Value> = match page.get(request.operation.paging().items()) {
            Some(Value::Array(items)) => items.iter().cloned().collect(),
            _ => VecDeque::new(),
        };
        let next = self.next_request(request, &page, &answer, items.len())?;
        Ok((items, next))
    }

    /// Walks every page of an operation, yielding each item.
    pub fn paginate<T: DeserializeOwned + Send + 'static>(
        transport: &Arc<Self>,
        request: Request,
    ) -> Items<T> {
        struct Walk {
            transport: Arc<Transport>,
            request: Option<Request>,
            items: VecDeque<Value>,
        }
        let walk = Walk {
            transport: Arc::clone(transport),
            request: Some(request),
            items: VecDeque::new(),
        };
        Box::pin(futures_util::stream::unfold(walk, |mut walk| async move {
            loop {
                if let Some(raw) = walk.items.pop_front() {
                    let item = T::deserialize(raw).map_err(|error| {
                        walk.request = None;
                        walk.items.clear();
                        Error::new(ErrorKind::Decode, "an item does not fit its type")
                            .with_source(error)
                    });
                    return Some((item, walk));
                }
                let request = walk.request.take()?;
                match walk.transport.page(&request).await {
                    Ok((items, next)) => {
                        walk.items = items;
                        walk.request = next;
                    }
                    Err(error) => return Some((Err(error), walk)),
                }
            }
        }))
    }
}

#[cfg(test)]
mod tests {
    use super::super::credentials::StaticCredentials;
    use super::*;

    #[test]
    fn retry_after_reads_seconds_and_dates() {
        let now = httpdate::parse_http_date("Sun, 01 Nov 2026 00:00:00 GMT").unwrap();
        assert_eq!(retry_after(Some(" 2 "), now), Some(Duration::from_secs(2)));
        assert_eq!(
            retry_after(Some("Sun, 01 Nov 2026 00:00:05 GMT"), now),
            Some(Duration::from_secs(5))
        );
        assert_eq!(
            retry_after(Some("99999999999999999999999"), now),
            Some(Duration::MAX)
        );
    }

    #[test]
    fn retry_after_ignores_past_dates_and_nonsense() {
        let now = httpdate::parse_http_date("Sun, 01 Nov 2026 00:00:00 GMT").unwrap();
        assert_eq!(
            retry_after(Some("Sat, 31 Oct 2026 23:59:59 GMT"), now),
            None
        );
        assert_eq!(retry_after(Some("-1"), now), None);
        assert_eq!(retry_after(Some("soon"), now), None);
        assert_eq!(retry_after(Some(""), now), None);
        assert_eq!(retry_after(None, now), None);
    }

    #[test]
    fn decompress_passes_plain_bodies_and_rejects_corrupt_ones() {
        let mut headers = HeaderMap::new();
        assert_eq!(decompress(&headers, b"plain".to_vec()).unwrap(), b"plain");
        headers.insert(CONTENT_ENCODING, HeaderValue::from_static("gzip"));
        assert!(decompress(&headers, b"not gzip".to_vec()).is_err());
    }

    #[test]
    fn decompress_reads_every_gzip_member() {
        let mut body = Vec::new();
        for part in [b"first ".as_slice(), b"second"] {
            let mut encoder =
                flate2::write::GzEncoder::new(Vec::new(), flate2::Compression::default());
            std::io::Write::write_all(&mut encoder, part).unwrap();
            body.extend(encoder.finish().unwrap());
        }
        let mut headers = HeaderMap::new();
        headers.insert(CONTENT_ENCODING, HeaderValue::from_static("gzip"));
        assert_eq!(decompress(&headers, body).unwrap(), b"first second");
    }

    fn settings(headers: HeaderMap) -> Settings {
        Settings {
            base_url: "http://127.0.0.1:1".to_owned(),
            hosts: HashMap::new(),
            credentials: Arc::new(StaticCredentials::new(HeaderMap::new(), Vec::new())),
            headers,
            header_defaults: HashMap::new(),
            to_error: |context| Error::new(ErrorKind::Api, format!("status {}", context.status)),
            timeout: Duration::from_secs(1),
            max_retries: 0,
            retry_base_delay: Duration::ZERO,
            rate_limit_wait: Duration::ZERO,
            max_retry_wait: Duration::ZERO,
            http: None,
        }
    }

    const OFFSET_LIST: Operation = Operation {
        id: "list-items",
        method: "GET",
        path: "/items",
        query_params: &["limit", "start"],
        returns_json: true,
        paging: Some(Paging::Offset {
            items: "data",
            total: "total",
            offset: "start",
        }),
        security: &[],
    };

    const LINKED_LIST: Operation = Operation {
        id: "list-items",
        method: "GET",
        path: "/items",
        query_params: &["token"],
        returns_json: true,
        paging: Some(Paging::NextLink {
            items: "data",
            link: "more",
            params: &["token"],
        }),
        security: &[],
    };

    fn next(
        operation: &'static Operation,
        query: &[(&str, &str)],
        page: Value,
        received: usize,
    ) -> Result<Option<String>, Error> {
        let transport = Transport::new(settings(HeaderMap::new())).unwrap();
        let mut request = Request::new(operation);
        for (name, value) in query {
            request.set_query(name, value);
        }
        let answer = Answer {
            status: 200,
            headers: HeaderMap::new(),
            body: Vec::new(),
        };
        Ok(transport
            .next_request(&request, &page, &answer, received)?
            .map(|next| next.url("")))
    }

    fn next_url(
        operation: &'static Operation,
        query: &[(&str, &str)],
        page: Value,
        received: usize,
    ) -> Option<String> {
        next(operation, query, page, received).unwrap()
    }

    #[test]
    fn offset_paging_advances_by_the_items_received_until_the_total() {
        let page = serde_json::json!({ "total": 5, "data": [] });
        assert_eq!(
            next_url(&OFFSET_LIST, &[("limit", "2")], page.clone(), 2).as_deref(),
            Some("/items?limit=2&start=2")
        );
        assert_eq!(
            next_url(
                &OFFSET_LIST,
                &[("limit", "2"), ("start", "2")],
                page.clone(),
                2
            )
            .as_deref(),
            Some("/items?limit=2&start=4")
        );
        assert_eq!(
            next_url(&OFFSET_LIST, &[("limit", "2"), ("start", "4")], page, 1),
            None
        );
    }

    #[test]
    fn offset_paging_starts_at_the_callers_offset_and_stops_at_an_empty_page() {
        let page = serde_json::json!({ "total": null, "data": [] });
        assert_eq!(
            next_url(&OFFSET_LIST, &[("start", "3")], page.clone(), 1).as_deref(),
            Some("/items?start=4")
        );
        assert_eq!(next_url(&OFFSET_LIST, &[("start", "4")], page, 0), None);
    }

    #[test]
    fn offset_paging_stops_at_a_total_that_is_not_an_integer() {
        assert_eq!(
            next_url(
                &OFFSET_LIST,
                &[],
                serde_json::json!({ "total": 2.0, "data": [] }),
                2
            ),
            None
        );
    }

    #[test]
    fn offset_paging_rejects_an_offset_that_is_not_an_integer() {
        let error = next(
            &OFFSET_LIST,
            &[("start", "later")],
            serde_json::json!({ "data": [] }),
            1,
        )
        .unwrap_err();
        assert_eq!(error.kind(), ErrorKind::Decode);
        assert!(
            error
                .to_string()
                .contains("start parameter is not an integer"),
            "{error}"
        );
    }

    #[test]
    fn paging_rejects_a_page_without_an_items_list() {
        for operation in [&OFFSET_LIST, &LINKED_LIST] {
            for page in [
                serde_json::json!({ "total": 1 }),
                serde_json::json!({ "data": null }),
                serde_json::json!({ "data": {} }),
            ] {
                assert_eq!(
                    next(operation, &[], page, 0).unwrap_err().kind(),
                    ErrorKind::Decode
                );
            }
        }
    }

    #[test]
    fn next_link_paging_reads_the_configured_fields() {
        let page =
            serde_json::json!({ "data": [1], "more": "/items?token=b", "next": "/items?token=c" });
        assert_eq!(
            next_url(&LINKED_LIST, &[], page, 1).as_deref(),
            Some("/items?token=b")
        );
        let last = serde_json::json!({ "data": [1], "more": null, "next": "/x?token=c" });
        assert_eq!(next_url(&LINKED_LIST, &[("token", "b")], last, 1), None);
        assert_eq!(OFFSET_LIST.paging().items(), "data");
        assert_eq!(
            Operation {
                paging: None,
                ..LINKED_LIST
            }
            .paging()
            .items(),
            "results"
        );
    }

    #[test]
    fn a_request_that_cannot_be_built_is_not_a_connection_failure() {
        let error = reqwest::Client::new().get("not a url").build().unwrap_err();
        assert_eq!(translate(error).kind(), ErrorKind::Api);
    }
}
