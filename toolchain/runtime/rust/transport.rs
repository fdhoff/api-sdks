use std::collections::{HashMap, VecDeque};
use std::fmt;
use std::io::Read;
use std::pin::Pin;
use std::sync::{Arc, PoisonError};
use std::time::{Duration, SystemTime};

use futures_core::Stream;
use reqwest::header::{ACCEPT, ACCEPT_ENCODING, CONTENT_ENCODING, CONTENT_LENGTH, CONTENT_TYPE, HeaderMap, HeaderName, HeaderValue, LOCATION};
use reqwest::{Method, StatusCode, multipart, redirect};
use serde::de::DeserializeOwned;
use serde_json::Value;

use super::credentials::{AuthRequest, Credentials, redact_with, redactions};
use super::error::{Error, ErrorContext};
use super::request::{Body, Job, Operation, Paging, Part, Request};
use crate::ErrorKind;

/// A backoff doubles per retry, and this keeps the shift in range for any retry count.
const MAX_BACKOFF_DOUBLINGS: u32 = 20;

/// The largest integer a JavaScript number holds exactly, so every runtime accepts the same numeric cursors.
const MAX_SAFE_INTEGER: f64 = 9_007_199_254_740_991.0;

/// The redirects a URL download follows, and how many it follows before giving up.
const REDIRECTS: [u16; 5] = [301, 302, 303, 307, 308];
const MAX_REDIRECTS: usize = 5;

/// What a URL download's credentials see as its operation when the caller names none.
static URL_DOWNLOAD: Operation =
    Operation { id: "downloadUrl", method: "GET", path: "", query_params: &[], returns_json: false, paging: None, security: &[] };

/// A stream of every item across all pages. It ends after yielding an error.
pub type Items<T> = Pin<Box<dyn Stream<Item = Result<T, Error>> + Send>>;

/// Configures a [`Transport`].
pub struct Settings {
    /// Where an operation with no host key is sent, without a trailing slash.
    pub base_url: String,
    /// The base URL for each host key, without a trailing slash, as `select_hosts` returns them. A
    /// request is never sent to a host that is not here.
    pub hosts: HashMap<String, String>,
    pub credentials: Arc<dyn Credentials>,
    pub headers: HeaderMap,
    /// A value for each default-able header, sent by the operations that declare it when the call
    /// gives none. Names match without regard to case.
    pub header_defaults: HashMap<String, String>,
    /// A value for each default-able query parameter, sent by the operations that declare it when the
    /// call gives none. Names match exactly.
    pub query_defaults: HashMap<String, String>,
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

/// How a job's wait method polls.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
#[allow(dead_code, reason = "an API may have no jobs")]
pub struct WaitOptions {
    /// The time between polls. Defaults to 60 seconds.
    pub interval: Duration,
    /// How long to wait for the job to end. Defaults to an hour.
    pub timeout: Duration,
}

impl Default for WaitOptions {
    fn default() -> Self {
        Self { interval: Duration::from_secs(60), timeout: Duration::from_secs(3600) }
    }
}

/// Sends requests, applying the timeout, retry and redaction rules.
pub struct Transport {
    settings: Settings,
    http: reqwest::Client,
    refreshing: tokio::sync::Mutex<()>,
    /// Counts refreshes per refresh group, so that a call whose credentials were refreshed since it
    /// sent them retries without another.
    generations: std::sync::Mutex<HashMap<&'static str, u64>>,
}

impl fmt::Debug for Transport {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("Transport").field("base_url", &self.settings.base_url).finish_non_exhaustive()
    }
}

struct Answer {
    status: u16,
    headers: HeaderMap,
    body: Vec<u8>,
}

enum Reply {
    Whole(Answer),
    Streamed(Download),
    /// Where a URL download's redirect points.
    Redirect(url::Url),
}

/// One request of a URL download: an absolute URL, sent with credentials only when `signed`.
pub(super) struct Hop<'a> {
    url: &'a url::Url,
    signed: bool,
}

/// A URL for the log, without its user, password or query, any of which may hold a secret.
fn shown(url: &url::Url) -> String {
    format!("{}{}", &url[..url::Position::BeforeUsername], &url[url::Position::BeforeHost..url::Position::AfterPath])
}

fn absolute(url: url::Url) -> Option<url::Url> {
    (matches!(url.scheme(), "http" | "https") && url.has_host()).then_some(url)
}

/// A binary response body, read as it arrives. The attempt's deadline keeps running while it is
/// read, so reading past it fails with a timeout. The body is passed on as received, and dropping
/// the download closes the connection.
#[allow(dead_code, reason = "an API may have no binary responses")]
pub struct Download {
    response: reqwest::Response,
    content_type: String,
    deadline: tokio::time::Instant,
}

#[allow(dead_code, reason = "an API may have no binary responses")]
impl Download {
    /// The response's `Content-Type`, empty if it has none.
    pub fn content_type(&self) -> &str {
        &self.content_type
    }

    /// The next part of the body, or `None` at its end.
    pub async fn chunk(&mut self) -> Result<Option<Vec<u8>>, Error> {
        match tokio::time::timeout_at(self.deadline, self.response.chunk()).await {
            Ok(chunk) => chunk.map(|chunk| chunk.map(|bytes| bytes.to_vec())).map_err(translate),
            Err(elapsed) => Err(Error::new(ErrorKind::Timeout, "the request timed out").with_source(elapsed)),
        }
    }

    /// The whole body, read into memory.
    pub async fn bytes(mut self) -> Result<Vec<u8>, Error> {
        let mut bytes = Vec::new();
        while let Some(chunk) = self.chunk().await? {
            bytes.extend_from_slice(&chunk);
        }
        Ok(bytes)
    }
}

impl fmt::Debug for Download {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("Download").field("content_type", &self.content_type).finish_non_exhaustive()
    }
}

fn is_json(headers: &HeaderMap) -> bool {
    let content_type = headers.get(CONTENT_TYPE).and_then(|value| value.to_str().ok()).unwrap_or_default();
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
        return Some(value.parse().map(Duration::from_secs).unwrap_or(Duration::MAX));
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
            let text = url::form_urlencoded::Serializer::new(String::new()).extend_pairs(fields).finish();
            return Ok((Some("application/x-www-form-urlencoded".to_owned()), text.into_bytes()));
        }
        Body::Raw { content_type, body } => return Ok((Some((*content_type).to_owned()), body.bytes().to_vec())),
        Body::Multipart(parts) => parts,
    };
    let form = form(parts)?;
    let content_type = format!("multipart/form-data; boundary={}", form.boundary());
    let mut stream = std::pin::pin!(form.into_stream());
    let mut bytes = Vec::new();
    while let Some(chunk) = futures_util::StreamExt::next(&mut stream).await {
        bytes.extend_from_slice(&chunk.map_err(translate)?);
    }
    Ok((Some(content_type), bytes))
}

fn form(parts: &[Part]) -> Result<multipart::Form, Error> {
    parts.iter().try_fold(multipart::Form::new(), |form, part| match part {
        Part::Text { name, value } => Ok(form.text(name.clone(), value.clone())),
        Part::File { name, file } => {
            let filename = file.name.clone().unwrap_or_else(|| name.clone());
            let part = multipart::Part::bytes(file.content.clone())
                .file_name(filename)
                .mime_str("application/octet-stream")
                .map_err(translate)?;
            Ok(form.part(name.clone(), part))
        }
    })
}

/// `defaults` keyed by lowercase name.
fn by_lowercase(defaults: HashMap<String, String>) -> Result<HashMap<String, String>, Error> {
    let mut clashes: Vec<&str> = defaults
        .keys()
        .filter(|name| defaults.keys().any(|other| other != *name && other.eq_ignore_ascii_case(name)))
        .map(String::as_str)
        .collect();
    if !clashes.is_empty() {
        clashes.sort_unstable();
        let message = format!("header_defaults has names that differ only by case: {}", clashes.join(", "));
        return Err(Error::new(ErrorKind::Api, message));
    }
    Ok(defaults.into_iter().map(|(name, value)| (name.to_ascii_lowercase(), value)).collect())
}

impl Transport {
    /// Builds a transport. Its own client never follows a redirect: a redirect is reported as a
    /// failure, so the token cannot be sent anywhere but the configured server. A caller's client
    /// keeps its own redirect policy. Headers are sent on each request, so either client sends them.
    /// Header defaults whose names differ only by case are an error.
    pub fn new(mut settings: Settings) -> Result<Self, Error> {
        settings.header_defaults = by_lowercase(std::mem::take(&mut settings.header_defaults))?;
        settings.headers.insert(ACCEPT_ENCODING, HeaderValue::from_static("gzip"));
        let http = match settings.http.take() {
            Some(http) => http,
            None => reqwest::Client::builder()
                .redirect(redirect::Policy::none())
                .build()
                .map_err(|error| Error::new(ErrorKind::Api, "the HTTP client cannot be built").with_source(error))?,
        };
        Ok(Self { settings, http, refreshing: tokio::sync::Mutex::new(()), generations: std::sync::Mutex::default() })
    }

    /// The base URL for a request's host key, or an error before anything is sent.
    fn base_url(&self, request: &Request) -> Result<&str, Error> {
        let Some(key) = request.host else { return Ok(&self.settings.base_url) };
        self.settings
            .hosts
            .get(key)
            .map(String::as_str)
            .ok_or_else(|| Error::new(ErrorKind::Api, format!("no base URL is configured for host {key}")))
    }

    fn header_default(&self, name: &str) -> Option<&str> {
        self.settings.header_defaults.get(&name.to_ascii_lowercase()).map(String::as_str)
    }

    fn redact(&self, text: &str) -> String {
        redact_with(&redactions(self.settings.credentials.as_ref()), text)
    }

    /// The request for one attempt, with the credentials applied unless it is a hop that is not
    /// signed. A header that holds a secret is marked sensitive, so that a debug print of it shows
    /// nothing.
    pub(super) async fn authorize(
        &self,
        request: &Request,
        hop: Option<&Hop<'_>>,
        method: Method,
        content_type: Option<&str>,
        body: Vec<u8>,
    ) -> Result<AuthRequest, Error> {
        let mut headers = self.settings.headers.clone();
        if request.download {
            headers.insert(ACCEPT_ENCODING, HeaderValue::from_static("identity"));
        }
        if let Some(accept) = request.accept {
            let value = HeaderValue::from_str(accept)
                .map_err(|error| Error::new(ErrorKind::Api, "the accepted media types are not valid").with_source(error))?;
            headers.insert(ACCEPT, value);
        }
        if let Some(content_type) = content_type {
            let value = HeaderValue::from_str(content_type)
                .map_err(|error| Error::new(ErrorKind::Api, "the content type is not valid").with_source(error))?;
            headers.insert(CONTENT_TYPE, value);
        }
        for (name, value) in &request.headers {
            let Some(value) = value.as_deref().or_else(|| self.header_default(name)) else { continue };
            let name = HeaderName::from_bytes(name.as_bytes())
                .map_err(|error| Error::new(ErrorKind::Api, format!("the header name {name} is not valid")).with_source(error))?;
            let value = HeaderValue::from_str(value)
                .map_err(|error| Error::new(ErrorKind::Api, format!("the {name} header value is not valid")).with_source(error))?;
            headers.insert(name, value);
        }
        let url = match hop {
            Some(hop) => hop.url.to_string(),
            None => request.url(self.base_url(request)?, &self.settings.query_defaults),
        };
        let mut auth = AuthRequest { method, url, headers, body, operation: request.operation };
        let credentials = self.settings.credentials.as_ref();
        if hop.is_none_or(|hop| hop.signed) {
            credentials.apply(&mut auth).await.map_err(|error| error.map_message(|text| self.redact(text)))?;
        }
        let secrets: Vec<String> = credentials.secrets().into_iter().filter(|secret| !secret.is_empty()).collect();
        for value in auth.headers.values_mut() {
            let bytes = value.as_bytes();
            if secrets.iter().any(|secret| bytes.windows(secret.len()).any(|window| window == secret.as_bytes())) {
                value.set_sensitive(true);
            }
        }
        Ok(auth)
    }

    fn generation(&self, group: &'static str) -> u64 {
        self.generations.lock().unwrap_or_else(PoisonError::into_inner).get(group).copied().unwrap_or_default()
    }

    /// Lets calls waiting on a refresh of the same group share it.
    async fn refresh(&self, auth: &AuthRequest, group: &'static str, generation: u64) -> Result<bool, Error> {
        let _refreshing = self.refreshing.lock().await;
        if self.generation(group) != generation {
            return Ok(true);
        }
        let refreshed = self
            .settings
            .credentials
            .refresh(auth)
            .await
            .map_err(|error| error.map_message(|text| self.redact(text)))?;
        if refreshed {
            *self.generations.lock().unwrap_or_else(PoisonError::into_inner).entry(group).or_default() += 1;
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
        (self.settings.to_error)(ErrorContext { status: answer.status, headers: answer.headers, text, json })
    }

    fn decode_error(&self, message: &str, answer: &Answer) -> Error {
        let text = self.redact(&String::from_utf8_lossy(&answer.body));
        Error::new(ErrorKind::Decode, message).with_status(answer.status).with_raw_body(Some(text))
    }

    async fn send(&self, auth: &AuthRequest, stream: Option<reqwest::Body>) -> Result<reqwest::Response, Error> {
        let mut outgoing = self.http.request(auth.method.clone(), &auth.url).headers(auth.headers.clone());
        if let Some(stream) = stream {
            outgoing = outgoing.body(stream);
        } else if !auth.body.is_empty() {
            outgoing = outgoing.body(auth.body.clone());
        } else if sends_empty_length(&auth.method) && !auth.headers.contains_key(CONTENT_LENGTH) {
            // The signer signs 0 for these methods, so send it rather than rely on hyper to.
            outgoing = outgoing.header(CONTENT_LENGTH, "0");
        }
        outgoing.send().await.map_err(translate)
    }

    /// Where a hop's redirect points, resolved against the hop's URL. A redirect without an http or
    /// https location is an error.
    fn redirect(&self, hop: &Hop<'_>, status: u16, headers: &HeaderMap) -> Result<url::Url, Error> {
        let Some(location) = headers.get(LOCATION) else {
            return Err(Error::new(ErrorKind::Decode, "a redirect has no Location").with_status(status));
        };
        let target = location.to_str().ok().and_then(|location| hop.url.join(location).ok()).and_then(absolute);
        target.ok_or_else(|| Error::new(ErrorKind::Decode, "a redirect's Location is not an http or https URL").with_status(status))
    }

    /// One attempt, with one deadline from sending the request to reading the last byte. A
    /// successful download is returned as soon as its headers arrive, and keeps the deadline. A
    /// hop's redirect is returned unread.
    async fn attempt(&self, auth: &AuthRequest, stream: Option<reqwest::Body>, download: bool, hop: Option<&Hop<'_>>) -> Result<Reply, Error> {
        let deadline = tokio::time::Instant::now() + self.settings.timeout;
        let timed_out = |elapsed| Error::new(ErrorKind::Timeout, "the request timed out").with_source(elapsed);
        let incoming = tokio::time::timeout_at(deadline, self.send(auth, stream)).await.map_err(timed_out)??;
        let status = incoming.status().as_u16();
        let success = incoming.status().is_success();
        let method = &auth.method;
        if let Some(hop) = hop.filter(|_| REDIRECTS.contains(&status)) {
            self.log(log::Level::Debug, format_args!("response {method} {status} (redirect)"));
            return self.redirect(hop, status, incoming.headers()).map(Reply::Redirect);
        }
        if download && success {
            self.log(log::Level::Debug, format_args!("response {method} {status} (streamed)"));
            let content_type = incoming.headers().get(CONTENT_TYPE).and_then(|value| value.to_str().ok()).unwrap_or_default().to_owned();
            return Ok(Reply::Streamed(Download { response: incoming, content_type, deadline }));
        }
        let headers = incoming.headers().clone();
        let body = tokio::time::timeout_at(deadline, incoming.bytes()).await.map_err(timed_out)?.map_err(translate)?.to_vec();
        let body = match decompress(&headers, body) {
            Ok(body) => body,
            Err(error) if success => {
                return Err(Error::new(ErrorKind::Decode, "the response body cannot be decompressed")
                    .with_status(status)
                    .with_source(error));
            }
            Err(_) => Vec::new(),
        };
        self.log(log::Level::Debug, format_args!("response {method} {status} ({} bytes)", body.len()));
        let answer = Answer { status, headers, body };
        if !success {
            return Err(self.failure(answer));
        }
        Ok(Reply::Whole(answer))
    }

    fn retry_delay(&self, failure: &Error, repeatable: bool, tries: u32) -> Option<Duration> {
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
        (repeatable && failed)
            .then(|| settings.retry_base_delay.saturating_mul(1 << tries.min(MAX_BACKOFF_DOUBLINGS)))
    }

    async fn fetch(&self, request: &Request) -> Result<Answer, Error> {
        match self.exchange(request, None).await? {
            Reply::Whole(answer) => Ok(answer),
            Reply::Streamed(_) | Reply::Redirect(_) => unreachable!("only a download streams"),
        }
    }

    /// Sends a request, retrying as the settings allow. A hop is a GET to its own URL, and is
    /// refreshed after a 401 only when it is signed.
    async fn exchange(&self, request: &Request, hop: Option<&Hop<'_>>) -> Result<Reply, Error> {
        if let Some(reason) = &request.invalid {
            return Err(Error::new(ErrorKind::Api, format!("the request cannot be encoded: {reason}")));
        }
        let method = match hop {
            Some(_) => Method::GET,
            None => Method::from_bytes(request.operation.method.as_bytes())
                .map_err(|error| Error::new(ErrorKind::Api, "the request method is not valid").with_source(error))?,
        };
        let (content_type, body) = encode(&request.body).await?;
        let signed = hop.is_none_or(|hop| hop.signed);
        let repeatable = hop.is_some() || request.repeatable();
        let mut tries = 0;
        let mut refreshed = false;
        loop {
            let group = self.settings.credentials.refresh_group(request.operation);
            let generation = self.generation(group);
            let auth = self.authorize(request, hop, method.clone(), content_type.as_deref(), body.clone()).await?;
            let url = hop.map_or_else(|| auth.url.clone(), |hop| shown(hop.url));
            self.log(log::Level::Debug, format_args!("request {} {method} {url}", request.operation.id));
            let stream = match &request.body {
                Body::Raw { body, .. } => body
                    .take_stream()
                    .map_err(|()| Error::new(ErrorKind::Api, "the request body is a stream that was already sent"))?,
                _ => None,
            };
            let failure = match self.attempt(&auth, stream, request.download, hop).await {
                Ok(reply) => return Ok(reply),
                Err(failure) => failure,
            };
            // A stream cannot be sent again, so its first failure is final.
            if request.body.sends_once() {
                return Err(failure);
            }
            // An operation that sends no credentials, such as a token request made during a
            // refresh, has nothing to refresh.
            let secured = signed && !request.operation.security.is_empty();
            if failure.status() == Some(StatusCode::UNAUTHORIZED.as_u16()) && !refreshed && secured {
                refreshed = true;
                if self.refresh(&auth, group, generation).await? {
                    self.log(log::Level::Info, format_args!("retrying after refreshing credentials"));
                    continue;
                }
            }
            let Some(delay) = self.retry_delay(&failure, repeatable, tries) else {
                return Err(failure);
            };
            let kind = failure.kind();
            self.log(log::Level::Info, format_args!("retrying after {delay:?}: {kind:?}"));
            tokio::time::sleep(delay).await;
            tries += 1;
        }
    }

    fn decode<T: DeserializeOwned + Default>(&self, operation: &Operation, answer: &Answer) -> Result<T, Error> {
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
        T::deserialize(value).map_err(|_| self.decode_error("the response body does not fit its type", answer))
    }

    /// Sends one operation and decodes its response.
    pub async fn call<T: DeserializeOwned + Default>(&self, request: Request) -> Result<T, Error> {
        let answer = self.fetch(&request).await?;
        self.decode(request.operation, &answer)
    }

    /// Sends one operation whose success body is binary, and returns it to be read as it arrives.
    #[allow(dead_code, reason = "an API may have no binary responses")]
    pub async fn download(&self, mut request: Request) -> Result<Download, Error> {
        request.download = true;
        match self.exchange(&request, None).await? {
            Reply::Streamed(download) => Ok(download),
            Reply::Whole(_) | Reply::Redirect(_) => unreachable!("a successful download streams"),
        }
    }

    /// GETs an absolute URL that a response returned, as a download, following up to five
    /// redirects. Credentials are sent only while every request so far has gone to the base URL's
    /// scheme, host and port, and never again once a redirect leaves it. `operation` is what the
    /// credentials see, for its security requirements; `None` is one with none.
    // TODO: a caller's own client that follows redirects follows them itself, past these checks,
    // and strips only the standard credential headers when it leaves the host.
    #[allow(dead_code, reason = "an API may download no URLs")]
    pub async fn download_url(&self, url: &str, operation: Option<&'static Operation>) -> Result<Download, Error> {
        let invalid = || Error::new(ErrorKind::Api, "the URL is not an absolute http or https URL");
        let mut target = url::Url::parse(url).ok().and_then(absolute).ok_or_else(invalid)?;
        let trusted = url::Url::parse(&self.settings.base_url).ok().map(|base| base.origin());
        let mut request = Request::new(operation.unwrap_or(&URL_DOWNLOAD));
        request.download = true;
        let mut signed = true;
        for _ in 0..=MAX_REDIRECTS {
            signed = signed && trusted.as_ref() == Some(&target.origin());
            match self.exchange(&request, Some(&Hop { url: &target, signed })).await? {
                Reply::Streamed(download) => return Ok(download),
                Reply::Redirect(next) => target = next,
                Reply::Whole(_) => unreachable!("a successful download streams"),
            }
        }
        Err(Error::new(ErrorKind::Decode, format!("more than {MAX_REDIRECTS} redirects")))
    }

    /// Whether a job's status says it has ended. A state that is not a string is an error.
    fn job_ended(&self, job: &Job, answer: &Answer) -> Result<bool, Error> {
        let data: Value = serde_json::from_slice(&answer.body).unwrap_or(Value::Null);
        let state = job.state.split('.').try_fold(&data, |value, key| value.get(key)).and_then(Value::as_str);
        let Some(state) = state else {
            return Err(self.decode_error(&format!("the {} state of a job is not a string", job.state), answer));
        };
        Ok(job.done.contains(&state) || job.failed.contains(&state))
    }

    /// Polls a job's status operation until the job ends, and returns its last status, done or
    /// failed. Each poll is a call, retried as any other. Once the timeout passes, the error's kind
    /// is `JobTimeout` and [`Error::job_status`] holds the last status. Dropping the future stops
    /// it, between polls included.
    #[allow(dead_code, reason = "an API may have no jobs")]
    pub async fn wait<T>(&self, job: &Job, request: Request, options: WaitOptions) -> Result<T, Error>
    where
        T: DeserializeOwned + Default + Send + Sync + 'static,
    {
        // A timeout too long to add never passes.
        let deadline = tokio::time::Instant::now().checked_add(options.timeout);
        loop {
            let answer = self.fetch(&request).await?;
            let status: T = self.decode(request.operation, &answer)?;
            if self.job_ended(job, &answer)? {
                return Ok(status);
            }
            let remaining = deadline.map(|deadline| deadline.saturating_duration_since(tokio::time::Instant::now()));
            if remaining.is_some_and(|remaining| remaining.is_zero()) {
                let message = format!("the job did not end within {:?}", options.timeout);
                return Err(Error::new(ErrorKind::JobTimeout, message).with_job_status(status));
            }
            tokio::time::sleep(remaining.map_or(options.interval, |remaining| remaining.min(options.interval))).await;
        }
    }

    /// The request for the page after this one. `None` means the last page.
    fn next_request(&self, request: &Request, page: &Value, answer: &Answer, received: usize) -> Result<Option<Request>, Error> {
        let items = request.operation.paging().items();
        if !page.get(items).is_some_and(Value::is_array) {
            return Err(self.decode_error(&format!("the {items} field of a page is not a list"), answer));
        }
        match request.operation.paging() {
            Paging::NextLink { link, params, .. } => self.next_link(request, link, params, page, answer),
            Paging::Offset { total, offset, .. } => self.next_offset(request, total, offset, page, answer, received),
            Paging::Cursor { next, param, .. } => self.next_cursor(request, next, param, page, answer),
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
            Some(_) => return Err(self.decode_error(&format!("the {field} link is not a string"), answer)),
        };
        let base = url::Url::parse("http://localhost/").expect("a valid base");
        let parsed = base.join(link).map_err(|_| self.decode_error(&format!("the {field} link cannot be parsed"), answer))?;
        let mut next = request.clone();
        let mut advanced = false;
        for marker in params {
            if !request.operation.query_params.contains(marker) {
                continue;
            }
            let Some((_, value)) = parsed.query_pairs().find(|(name, value)| name == marker && !value.is_empty()) else {
                continue;
            };
            advanced = advanced || request.query_value(marker) != Some(value.as_ref());
            next.set_query(marker, &value);
        }
        if !advanced {
            return Err(self.decode_error(&format!("the {field} link does not advance the iteration"), answer));
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
            Some(text) => text
                .parse::<u64>()
                .map_err(|_| self.decode_error(&format!("the {offset} parameter is not an integer"), answer))?,
        };
        let position = start.saturating_add(received as u64);
        if page.get(total).and_then(Value::as_f64).is_some_and(|total| position as f64 >= total) {
            return Ok(None);
        }
        let mut next = request.clone();
        next.set_query(offset, &position.to_string());
        Ok(Some(next))
    }

    /// Sends the page's next value back as the cursor parameter.
    fn next_cursor(&self, request: &Request, path: &str, param: &str, page: &Value, answer: &Answer) -> Result<Option<Request>, Error> {
        let mut value = page;
        for key in path.split('.') {
            value = match value {
                Value::Null => break,
                Value::Object(object) => object.get(key).unwrap_or(&Value::Null),
                _ => return Err(self.decode_error(&format!("the {path} value of a page is not inside an object"), answer)),
            };
        }
        let position = match value {
            Value::Null => return Ok(None),
            Value::String(position) if position.is_empty() => return Ok(None),
            Value::String(position) => Some(position.clone()),
            Value::Number(position) => position
                .as_f64()
                .filter(|whole| whole.fract() == 0.0 && whole.abs() <= MAX_SAFE_INTEGER)
                .map(|whole| (whole as i64).to_string()),
            _ => None,
        };
        let Some(position) = position else {
            return Err(self.decode_error(&format!("the {path} value of a page is not a string or an integer"), answer));
        };
        if request.query_value(param) == Some(position.as_str()) {
            return Err(self.decode_error(&format!("the {path} value does not advance the iteration"), answer));
        }
        let mut next = request.clone();
        next.set_query(param, &position);
        Ok(Some(next))
    }

    async fn page(&self, request: &Request) -> Result<(VecDeque<Value>, Option<Request>), Error> {
        let answer = self.fetch(request).await?;
        if answer.status == 204 {
            return Ok((VecDeque::new(), None));
        }
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
    pub fn paginate<T: DeserializeOwned + Send + 'static>(transport: &Arc<Self>, request: Request) -> Items<T> {
        struct Walk {
            transport: Arc<Transport>,
            request: Option<Request>,
            items: VecDeque<Value>,
        }
        let walk = Walk { transport: Arc::clone(transport), request: Some(request), items: VecDeque::new() };
        Box::pin(futures_util::stream::unfold(walk, |mut walk| async move {
            loop {
                if let Some(raw) = walk.items.pop_front() {
                    let item = T::deserialize(raw).map_err(|error| {
                        walk.request = None;
                        walk.items.clear();
                        Error::new(ErrorKind::Decode, "an item does not fit its type").with_source(error)
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

/// Whether a request with no body is sent with `Content-Length: 0`, as Go, Python and TypeScript send it.
/// The signer signs the same.
pub(super) fn sends_empty_length(method: &Method) -> bool {
    matches!(*method, Method::POST | Method::PUT | Method::PATCH)
}

#[cfg(test)]
mod tests {
    use super::super::credentials::StaticCredentials;
    use super::*;

    #[test]
    fn retry_after_reads_seconds_and_dates() {
        let now = httpdate::parse_http_date("Sun, 01 Nov 2026 00:00:00 GMT").unwrap();
        assert_eq!(retry_after(Some(" 2 "), now), Some(Duration::from_secs(2)));
        assert_eq!(retry_after(Some("Sun, 01 Nov 2026 00:00:05 GMT"), now), Some(Duration::from_secs(5)));
        assert_eq!(retry_after(Some("99999999999999999999999"), now), Some(Duration::MAX));
    }

    #[test]
    fn retry_after_ignores_past_dates_and_nonsense() {
        let now = httpdate::parse_http_date("Sun, 01 Nov 2026 00:00:00 GMT").unwrap();
        assert_eq!(retry_after(Some("Sat, 31 Oct 2026 23:59:59 GMT"), now), None);
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
            let mut encoder = flate2::write::GzEncoder::new(Vec::new(), flate2::Compression::default());
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
            query_defaults: HashMap::new(),
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
        paging: Some(Paging::Offset { items: "data", total: "total", offset: "start" }),
        security: &[],
    };

    const LINKED_LIST: Operation = Operation {
        id: "list-items",
        method: "GET",
        path: "/items",
        query_params: &["token"],
        returns_json: true,
        paging: Some(Paging::NextLink { items: "data", link: "more", params: &["token"] }),
        security: &[],
    };

    const CURSOR_LIST: Operation = Operation {
        id: "list-items",
        method: "GET",
        path: "/items",
        query_params: &["limit", "start_after"],
        returns_json: true,
        paging: Some(Paging::Cursor { items: "data", next: "page.next_page", param: "start_after" }),
        security: &[],
    };

    fn next(operation: &'static Operation, query: &[(&str, &str)], page: Value, received: usize) -> Result<Option<String>, Error> {
        let transport = Transport::new(settings(HeaderMap::new())).unwrap();
        let mut request = Request::new(operation);
        for (name, value) in query {
            request.set_query(name, value);
        }
        let answer = Answer { status: 200, headers: HeaderMap::new(), body: Vec::new() };
        Ok(transport.next_request(&request, &page, &answer, received)?.map(|next| next.url("", &HashMap::new())))
    }

    fn next_url(operation: &'static Operation, query: &[(&str, &str)], page: Value, received: usize) -> Option<String> {
        next(operation, query, page, received).unwrap()
    }

    #[test]
    fn an_empty_204_is_no_result_even_where_json_is_declared() {
        let transport = Transport::new(settings(HeaderMap::new())).unwrap();
        let empty = |status| Answer { status, headers: HeaderMap::new(), body: Vec::new() };
        assert_eq!(transport.decode::<Value>(&OFFSET_LIST, &empty(204)).unwrap(), Value::Null);
        assert!(transport.decode::<Value>(&OFFSET_LIST, &empty(200)).is_err());
    }

    #[test]
    fn offset_paging_advances_by_the_items_received_until_the_total() {
        let page = serde_json::json!({ "total": 5, "data": [] });
        assert_eq!(next_url(&OFFSET_LIST, &[("limit", "2")], page.clone(), 2).as_deref(), Some("/items?limit=2&start=2"));
        assert_eq!(next_url(&OFFSET_LIST, &[("limit", "2"), ("start", "2")], page.clone(), 2).as_deref(), Some("/items?limit=2&start=4"));
        assert_eq!(next_url(&OFFSET_LIST, &[("limit", "2"), ("start", "4")], page, 1), None);
    }

    #[test]
    fn offset_paging_starts_at_the_callers_offset_and_stops_at_an_empty_page() {
        let page = serde_json::json!({ "total": null, "data": [] });
        assert_eq!(next_url(&OFFSET_LIST, &[("start", "3")], page.clone(), 1).as_deref(), Some("/items?start=4"));
        assert_eq!(next_url(&OFFSET_LIST, &[("start", "4")], page, 0), None);
    }

    #[test]
    fn offset_paging_stops_at_a_total_that_is_not_an_integer() {
        assert_eq!(next_url(&OFFSET_LIST, &[], serde_json::json!({ "total": 2.0, "data": [] }), 2), None);
    }

    #[test]
    fn offset_paging_rejects_an_offset_that_is_not_an_integer() {
        let error = next(&OFFSET_LIST, &[("start", "later")], serde_json::json!({ "data": [] }), 1).unwrap_err();
        assert_eq!(error.kind(), ErrorKind::Decode);
        assert!(error.to_string().contains("start parameter is not an integer"), "{error}");
    }

    #[test]
    fn paging_rejects_a_page_without_an_items_list() {
        for operation in [&OFFSET_LIST, &LINKED_LIST, &CURSOR_LIST] {
            for page in [serde_json::json!({ "total": 1 }), serde_json::json!({ "data": null }), serde_json::json!({ "data": {} })] {
                assert_eq!(next(operation, &[], page, 0).unwrap_err().kind(), ErrorKind::Decode);
            }
        }
    }

    #[test]
    fn cursor_paging_sends_the_next_value_back_and_keeps_the_callers_parameters() {
        let page = serde_json::json!({ "data": [1], "page": { "next_page": "b" } });
        assert_eq!(next_url(&CURSOR_LIST, &[("limit", "2")], page.clone(), 1).as_deref(), Some("/items?limit=2&start_after=b"));
        assert_eq!(next_url(&CURSOR_LIST, &[("start_after", "a"), ("limit", "2")], page, 1).as_deref(), Some("/items?limit=2&start_after=b"));
    }

    #[test]
    fn cursor_paging_sends_an_integer_next_value_back_as_its_digits() {
        for (position, url) in [
            ("0", "/items?start_after=0"),
            ("7", "/items?start_after=7"),
            ("1.0", "/items?start_after=1"),
            ("-0", "/items?start_after=0"),
            ("9007199254740991", "/items?start_after=9007199254740991"),
        ] {
            let page = serde_json::from_str(&format!(r#"{{ "data": [1], "page": {{ "next_page": {position} }} }}"#)).unwrap();
            assert_eq!(next_url(&CURSOR_LIST, &[], page, 1).as_deref(), Some(url), "{position}");
        }
    }

    #[test]
    fn cursor_paging_stops_at_a_null_empty_or_absent_next_value() {
        for page in [
            serde_json::json!({ "data": [], "page": { "next_page": null } }),
            serde_json::json!({ "data": [], "page": { "next_page": "" } }),
            serde_json::json!({ "data": [], "page": {} }),
            serde_json::json!({ "data": [], "page": null }),
            serde_json::json!({ "data": [] }),
        ] {
            assert_eq!(next_url(&CURSOR_LIST, &[("start_after", "a")], page, 0), None);
        }
    }

    #[test]
    fn cursor_paging_rejects_a_next_value_equal_to_the_one_sent() {
        for (sent, page) in [
            ("a", serde_json::json!({ "data": [1], "page": { "next_page": "a" } })),
            ("3", serde_json::json!({ "data": [1], "page": { "next_page": 3 } })),
        ] {
            let error = next(&CURSOR_LIST, &[("start_after", sent)], page, 1).unwrap_err();
            assert_eq!(error.kind(), ErrorKind::Decode);
            assert!(error.to_string().contains("does not advance the iteration"), "{error}");
        }
    }

    #[test]
    fn cursor_paging_rejects_a_malformed_page() {
        for page in [
            serde_json::json!({ "page": { "next_page": "b" } }),
            serde_json::json!({ "data": [1], "page": { "next_page": 2.5 } }),
            serde_json::json!({ "data": [1], "page": { "next_page": 9_007_199_254_740_992_u64 } }),
            serde_json::json!({ "data": [1], "page": { "next_page": u64::MAX } }),
            serde_json::json!({ "data": [1], "page": { "next_page": i64::MIN } }),
            serde_json::json!({ "data": [1], "page": { "next_page": true } }),
            serde_json::json!({ "data": [1], "page": { "next_page": { "id": "b" } } }),
            serde_json::json!({ "data": [1], "page": "b" }),
        ] {
            assert_eq!(next(&CURSOR_LIST, &[], page, 1).unwrap_err().kind(), ErrorKind::Decode);
        }
    }

    #[test]
    fn next_link_paging_reads_the_configured_fields() {
        let page = serde_json::json!({ "data": [1], "more": "/items?token=b", "next": "/items?token=c" });
        assert_eq!(next_url(&LINKED_LIST, &[], page, 1).as_deref(), Some("/items?token=b"));
        let last = serde_json::json!({ "data": [1], "more": null, "next": "/x?token=c" });
        assert_eq!(next_url(&LINKED_LIST, &[("token", "b")], last, 1), None);
        assert_eq!(OFFSET_LIST.paging().items(), "data");
        assert_eq!(Operation { paging: None, ..LINKED_LIST }.paging().items(), "results");
    }

    #[tokio::test]
    async fn a_multipart_file_part_is_typed_and_a_text_part_is_not() {
        let file = super::super::request::File { name: Some("photo.png".to_owned()), content: b"synthetic".to_vec() };
        let parts = vec![Part::File { name: "image".to_owned(), file }, Part::Text { name: "title".to_owned(), value: "Lamp".to_owned() }];
        let (content_type, body) = encode(&Body::Multipart(parts)).await.unwrap();
        assert!(content_type.unwrap().starts_with("multipart/form-data; boundary="));
        let body = String::from_utf8(body).unwrap();
        let file = "content-disposition: form-data; name=\"image\"; filename=\"photo.png\"\r\ncontent-type: application/octet-stream\r\n\r\nsynthetic";
        assert!(body.to_lowercase().contains(file), "{body}");
        let text = "content-disposition: form-data; name=\"title\"\r\n\r\nLamp";
        assert!(body.to_lowercase().contains(&text.to_lowercase()), "{body}");
    }

    #[test]
    fn a_request_that_cannot_be_built_is_not_a_connection_failure() {
        let error = reqwest::Client::new().get("not a url").build().unwrap_err();
        assert_eq!(translate(error).kind(), ErrorKind::Api);
    }

    mod binary {
        use std::sync::Mutex;

        use futures_core::future::BoxFuture;
        use tokio::io::{AsyncReadExt, AsyncWriteExt};
        use tokio::net::TcpListener;
        use tokio::sync::Notify;

        use super::super::super::credentials::tests::{Log, Sent};
        use super::super::super::request::RawBody;
        use super::*;

        const PDF: &[u8] = &[0x25, 0x50, 0x44, 0x46, 0x00, 0xff, 0xfe, 0x80, 0x0a, 0xc3, 0x28];

        const DOWNLOAD: Operation =
            Operation { id: "download", method: "GET", path: "/files/1", query_params: &[], returns_json: false, paging: None, security: &[] };
        const UPLOAD: Operation = Operation { id: "upload", method: "PUT", ..DOWNLOAD };
        const REPORT: Operation = Operation { id: "report", path: "/report", ..DOWNLOAD };

        /// One response: its parts are written in order, and a gate holds back every part after the first.
        struct Scripted {
            status: u16,
            content_type: Option<&'static str>,
            parts: Vec<Vec<u8>>,
            gate: Option<Arc<Notify>>,
        }

        fn reply(status: u16, content_type: Option<&'static str>, body: &[u8]) -> Scripted {
            Scripted { status, content_type, parts: vec![body.to_vec()], gate: None }
        }

        async fn serve(script: impl Fn(usize) -> Scripted + Send + 'static) -> (String, Log) {
            let listener = TcpListener::bind("127.0.0.1:0").await.unwrap();
            let url = format!("http://{}", listener.local_addr().unwrap());
            let log = Log::default();
            let kept = Arc::clone(&log);
            tokio::spawn(async move {
                loop {
                    let Ok((mut stream, _)) = listener.accept().await else { return };
                    let mut data = Vec::new();
                    let mut buffer = [0; 4096];
                    let head_end = loop {
                        if let Some(end) = data.windows(4).position(|window| window == b"\r\n\r\n") {
                            break end + 4;
                        }
                        match stream.read(&mut buffer).await {
                            Ok(0) | Err(_) => return,
                            Ok(read) => data.extend_from_slice(&buffer[..read]),
                        }
                    };
                    let head = String::from_utf8_lossy(&data[..head_end]).to_lowercase();
                    let length = head
                        .lines()
                        .find_map(|line| line.strip_prefix("content-length:"))
                        .and_then(|value| value.trim().parse::<usize>().ok())
                        .unwrap_or(0);
                    while data.len() < head_end + length {
                        match stream.read(&mut buffer).await {
                            Ok(0) | Err(_) => break,
                            Ok(read) => data.extend_from_slice(&buffer[..read]),
                        }
                    }
                    let number = {
                        let mut log = kept.lock().unwrap();
                        log.push(Sent { head, body: data[head_end..].to_vec() });
                        log.len()
                    };
                    let Scripted { status, content_type, parts, gate } = script(number);
                    let length: usize = parts.iter().map(Vec::len).sum();
                    let content_type = content_type.map(|value| format!("content-type: {value}\r\n")).unwrap_or_default();
                    let head = format!("HTTP/1.1 {status} Status\r\n{content_type}content-length: {length}\r\nconnection: close\r\n\r\n");
                    tokio::spawn(async move {
                        let _ = stream.write_all(head.as_bytes()).await;
                        for (index, part) in parts.iter().enumerate() {
                            if index > 0 {
                                if let Some(gate) = &gate {
                                    gate.notified().await;
                                }
                            }
                            let _ = stream.write_all(part).await;
                            let _ = stream.flush().await;
                        }
                        let _ = stream.shutdown().await;
                    });
                }
            });
            (url, log)
        }

        /// Records the body each attempt's credentials see.
        #[derive(Default)]
        struct Recorder {
            bodies: Mutex<Vec<Vec<u8>>>,
        }

        impl Credentials for Recorder {
            fn apply<'a>(&'a self, request: &'a mut AuthRequest) -> BoxFuture<'a, Result<(), Error>> {
                self.bodies.lock().unwrap().push(request.body.clone());
                Box::pin(async { Ok(()) })
            }

            fn secrets(&self) -> Vec<String> {
                Vec::new()
            }
        }

        fn transport(url: &str, timeout: Duration, credentials: Arc<dyn Credentials>) -> Transport {
            Transport::new(Settings {
                base_url: url.to_owned(),
                credentials,
                to_error: |context| {
                    Error::new(ErrorKind::Api, format!("status {}", context.status))
                        .with_status(context.status)
                        .with_raw_body(Some(context.text))
                },
                timeout,
                max_retries: 1,
                ..settings(HeaderMap::new())
            })
            .unwrap()
        }

        fn quick(url: &str) -> Transport {
            transport(url, Duration::from_secs(5), Arc::new(Recorder::default()))
        }

        fn line<'a>(head: &'a str, name: &str) -> Option<&'a str> {
            head.lines().find_map(|line| line.strip_prefix(&format!("{name}: ")))
        }

        #[tokio::test]
        async fn a_download_returns_the_exact_bytes_and_content_type() {
            let (url, log) = serve(|_| reply(200, Some("application/pdf"), PDF)).await;
            let download = quick(&url).download(Request::new(&DOWNLOAD)).await.unwrap();
            assert_eq!(download.content_type(), "application/pdf");
            assert_eq!(download.bytes().await.unwrap(), PDF);
            assert_eq!(line(&log.lock().unwrap()[0].head, "accept-encoding"), Some("identity"));
        }

        #[tokio::test]
        async fn a_download_asks_for_its_media_types_instead_of_the_default_accept() {
            let (url, log) = serve(|_| reply(200, Some("application/pdf"), PDF)).await;
            let mut headers = HeaderMap::new();
            headers.insert(ACCEPT, HeaderValue::from_static("application/json"));
            let transport = Transport::new(Settings { base_url: url, max_retries: 0, ..settings(headers) }).unwrap();
            transport.download(Request::new(&DOWNLOAD).accept("application/pdf")).await.unwrap();
            transport.download(Request::new(&DOWNLOAD)).await.unwrap();
            let log = log.lock().unwrap();
            assert_eq!(line(&log[0].head, "accept"), Some("application/pdf"));
            assert_eq!(line(&log[1].head, "accept"), Some("application/json"));
        }

        #[tokio::test]
        async fn a_download_is_read_as_it_arrives() {
            let gate = Arc::new(Notify::new());
            let held = Arc::clone(&gate);
            let (url, _) = serve(move |_| Scripted {
                status: 200,
                content_type: Some("application/octet-stream"),
                parts: vec![b"first".to_vec(), b"second".to_vec()],
                gate: Some(Arc::clone(&held)),
            })
            .await;
            let mut download = quick(&url).download(Request::new(&DOWNLOAD)).await.unwrap();
            assert_eq!(download.chunk().await.unwrap().as_deref(), Some(b"first".as_slice()));
            gate.notify_one();
            assert_eq!(download.bytes().await.unwrap(), b"second");
        }

        #[tokio::test]
        async fn an_empty_download_is_empty_and_may_have_no_content_type() {
            let (url, _) = serve(|_| reply(200, None, b"")).await;
            let mut download = quick(&url).download(Request::new(&DOWNLOAD)).await.unwrap();
            assert_eq!(download.content_type(), "");
            assert_eq!(download.chunk().await.unwrap(), None);
        }

        #[tokio::test]
        async fn the_deadline_keeps_running_while_a_download_is_read() {
            let gate = Arc::new(Notify::new());
            let held = Arc::clone(&gate);
            let (url, _) = serve(move |_| Scripted {
                status: 200,
                content_type: None,
                parts: vec![b"first".to_vec(), b"never".to_vec()],
                gate: Some(Arc::clone(&held)),
            })
            .await;
            let transport = transport(&url, Duration::from_millis(200), Arc::new(Recorder::default()));
            let download = transport.download(Request::new(&DOWNLOAD)).await.unwrap();
            assert_eq!(download.bytes().await.unwrap_err().kind(), ErrorKind::Timeout);
        }

        #[tokio::test]
        async fn a_failed_download_is_a_typed_error_from_its_text_and_is_retried_first() {
            let (url, log) = serve(|number| match number {
                1 => reply(503, None, b""),
                _ => reply(404, Some("application/json"), br#"{"message":"not here"}"#),
            })
            .await;
            let error = quick(&url).download(Request::new(&DOWNLOAD)).await.unwrap_err();
            assert_eq!(error.status(), Some(404));
            assert_eq!(error.raw_body(), Some(r#"{"message":"not here"}"#));
            assert_eq!(log.lock().unwrap().len(), 2);
        }

        #[tokio::test]
        async fn a_byte_upload_is_sent_unchanged_seen_by_credentials_and_retried() {
            let (url, log) = serve(|number| match number {
                1 => reply(429, None, b""),
                _ => reply(200, Some("application/json"), br#"{"id":1}"#),
            })
            .await;
            let credentials = Arc::new(Recorder::default());
            let transport = transport(&url, Duration::from_secs(5), credentials.clone());
            let request = Request::new(&UPLOAD).raw("application/octet-stream", PDF);
            let result: Value = transport.call(request).await.unwrap();
            assert_eq!(result, serde_json::json!({ "id": 1 }));
            let sent = log.lock().unwrap();
            assert_eq!(sent.len(), 2);
            for attempt in sent.iter() {
                assert_eq!(attempt.body, PDF);
                assert!(attempt.head.starts_with("put /files/1 "), "{}", attempt.head);
                assert_eq!(line(&attempt.head, "content-type"), Some("application/octet-stream"));
            }
            assert_eq!(*credentials.bodies.lock().unwrap(), [PDF.to_vec(), PDF.to_vec()]);
        }

        const TRANSFER: Operation = Operation { id: "transfer", method: "POST", path: "/transfers", returns_json: true, ..DOWNLOAD };

        async fn write_attempts(request: Request) -> Vec<Vec<u8>> {
            let (url, log) = serve(|number| match number {
                1 => reply(503, None, b""),
                _ => reply(200, Some("application/json"), br#"{"id":1}"#),
            })
            .await;
            let _ = quick(&url).call::<Value>(request).await;
            log.lock().unwrap().iter().map(|sent| sent.body.clone()).collect()
        }

        #[tokio::test]
        async fn an_idempotent_write_is_retried_after_a_server_error_with_the_same_body() {
            let body = serde_json::json!({ "key": "k-1", "amount": 5 });
            let sent = write_attempts(Request::new(&TRANSFER).idempotency_key("key").json(&body)).await;
            let expected = body.to_string().into_bytes();
            assert_eq!(sent, [expected.clone(), expected]);
        }

        #[tokio::test]
        async fn a_write_is_not_retried_after_a_server_error_without_a_key() {
            let unmarked = Request::new(&TRANSFER).json(&serde_json::json!({ "key": "k-1" }));
            assert_eq!(write_attempts(unmarked).await.len(), 1);
            for body in [serde_json::json!({ "key": "" }), serde_json::json!({ "key": null }), serde_json::json!({ "amount": 5 })] {
                let request = Request::new(&TRANSFER).idempotency_key("key").json(&body);
                assert_eq!(write_attempts(request).await.len(), 1, "{body}");
            }
        }

        #[tokio::test]
        async fn a_streamed_upload_is_sent_once_and_never_resent() {
            let (url, log) = serve(|_| reply(429, None, b"")).await;
            let credentials = Arc::new(Recorder::default());
            let transport = transport(&url, Duration::from_secs(5), credentials.clone());
            let request = Request::new(&UPLOAD).raw("video/mp4", RawBody::stream(PDF.to_vec()));
            let error = transport.call::<Value>(request).await.unwrap_err();
            assert_eq!(error.status(), Some(429));
            let sent = log.lock().unwrap();
            assert_eq!(sent.len(), 1);
            assert_eq!(sent[0].body, PDF);
            assert_eq!(line(&sent[0].head, "content-type"), Some("video/mp4"));
            assert_eq!(*credentials.bodies.lock().unwrap(), [Vec::<u8>::new()]);
        }

        #[tokio::test]
        async fn an_empty_204_page_is_the_last_page() {
            let (url, log) = serve(|number| match number {
                1 => reply(200, Some("application/json"), br#"{"total":null,"data":[1,2]}"#),
                _ => reply(204, None, b""),
            })
            .await;
            let transport = Arc::new(quick(&url));
            let items: Vec<Value> = futures_util::StreamExt::collect::<Vec<_>>(Transport::paginate(&transport, Request::new(&OFFSET_LIST)))
                .await
                .into_iter()
                .collect::<Result<_, _>>()
                .unwrap();
            assert_eq!(items, [serde_json::json!(1), serde_json::json!(2)]);
            assert_eq!(log.lock().unwrap().len(), 2);

            let (url, log) = serve(|_| reply(204, None, b"")).await;
            let transport = Arc::new(quick(&url));
            let items = futures_util::StreamExt::collect::<Vec<Result<Value, Error>>>(Transport::paginate(&transport, Request::new(&OFFSET_LIST))).await;
            assert!(items.is_empty());
            assert_eq!(log.lock().unwrap().len(), 1);
        }

        #[tokio::test]
        async fn a_text_response_that_is_not_json_is_text() {
            let (url, _) = serve(|_| reply(200, Some("text/tab-separated-values"), b"id\tname\n1\tsynthetic\n")).await;
            let text: String = quick(&url).call(Request::new(&REPORT)).await.unwrap();
            assert_eq!(text, "id\tname\n1\tsynthetic\n");
        }

        #[test]
        fn a_raw_body_prints_no_content() {
            assert_eq!(format!("{:?}", RawBody::from(b"secret".as_slice())), "RawBody(6 bytes)");
            assert_eq!(format!("{:?}", RawBody::stream(b"secret".to_vec())), "RawBody(stream)");
        }
    }

    mod jobs {
        use std::net::{Ipv4Addr, SocketAddr};
        use std::sync::Mutex;
        use std::sync::atomic::{AtomicUsize, Ordering};

        use futures_core::future::BoxFuture;
        use reqwest::header::AUTHORIZATION;
        use tokio::io::{AsyncReadExt, AsyncWriteExt};
        use tokio::net::TcpListener;

        use super::super::super::credentials::Scheme;
        use super::super::super::credentials::tests::{Log, Sent};
        use super::*;

        const SECRET: &str = "synthetic-secret";
        const CSV: &str = "id;error\n1;none\n";

        const STATUS: Operation =
            Operation { id: "getImport", method: "GET", path: "/imports/{import_id}", query_params: &[], returns_json: true, paging: None, security: &[] };
        const JOB: Job = Job { state: "progress.state", done: &["COMPLETE"], failed: &["FAILED"] };
        static SECURED: Operation = Operation {
            id: "getReport",
            method: "GET",
            path: "",
            query_params: &[],
            returns_json: false,
            paging: None,
            security: &[&[Scheme { name: "key", scopes: &[] }]],
        };

        /// Sends a header on every request, and counts what it signs and refreshes.
        #[derive(Default)]
        struct Key {
            signed: Mutex<Vec<String>>,
            refreshes: AtomicUsize,
        }

        impl Credentials for Key {
            fn apply<'a>(&'a self, request: &'a mut AuthRequest) -> BoxFuture<'a, Result<(), Error>> {
                self.signed.lock().unwrap().push(request.url.clone());
                request.headers.insert(AUTHORIZATION, HeaderValue::from_static(SECRET));
                Box::pin(async { Ok(()) })
            }

            fn secrets(&self) -> Vec<String> {
                vec![SECRET.to_owned()]
            }

            fn refresh<'a>(&'a self, _request: &'a AuthRequest) -> BoxFuture<'a, Result<bool, Error>> {
                self.refreshes.fetch_add(1, Ordering::SeqCst);
                Box::pin(async { Ok(true) })
            }
        }

        /// Answers each request with the raw response the script gives for its number and lowercased head.
        async fn serve(script: impl Fn(usize, &str) -> String + Send + 'static) -> (u16, Log) {
            let listener = TcpListener::bind("127.0.0.1:0").await.unwrap();
            let port = listener.local_addr().unwrap().port();
            let log = Log::default();
            let kept = Arc::clone(&log);
            tokio::spawn(async move {
                loop {
                    let Ok((mut stream, _)) = listener.accept().await else { return };
                    let mut data = Vec::new();
                    let mut buffer = [0; 4096];
                    while !data.windows(4).any(|window| window == b"\r\n\r\n") {
                        match stream.read(&mut buffer).await {
                            Ok(0) | Err(_) => return,
                            Ok(read) => data.extend_from_slice(&buffer[..read]),
                        }
                    }
                    let head = String::from_utf8_lossy(&data).to_lowercase();
                    let number = {
                        let mut log = kept.lock().unwrap();
                        log.push(Sent { head: head.clone(), body: Vec::new() });
                        log.len()
                    };
                    let _ = stream.write_all(script(number, &head).as_bytes()).await;
                    let _ = stream.shutdown().await;
                }
            });
            (port, log)
        }

        fn response(status: u16, headers: &str, body: &str) -> String {
            format!("HTTP/1.1 {status} Status\r\n{headers}content-length: {}\r\nconnection: close\r\n\r\n{body}", body.len())
        }

        fn status(state: &str) -> String {
            response(200, "content-type: application/json\r\n", &format!(r#"{{"import_id":7,"progress":{{"state":{state}}}}}"#))
        }

        fn csv() -> String {
            response(200, "content-type: text/csv\r\n", CSV)
        }

        fn moved(location: &str) -> String {
            response(302, &format!("location: {location}\r\n"), "")
        }

        /// A transport whose base URL is `base`, with both test hosts served on this machine.
        fn transport(base: &str, credentials: Arc<Key>) -> Transport {
            let local = SocketAddr::from((Ipv4Addr::LOCALHOST, 0));
            let http = reqwest::Client::builder()
                .redirect(redirect::Policy::none())
                .resolve("api.example.test", local)
                .resolve("files.example.test", local)
                .build()
                .unwrap();
            let mut headers = HeaderMap::new();
            headers.insert("user-agent", HeaderValue::from_static("test"));
            Transport::new(Settings {
                base_url: base.to_owned(),
                credentials,
                to_error: |context| Error::new(ErrorKind::Api, format!("status {}", context.status)).with_status(context.status),
                max_retries: 2,
                http: Some(http),
                ..settings(headers)
            })
            .unwrap()
        }

        fn quick(options: (u64, u64)) -> WaitOptions {
            WaitOptions { interval: Duration::from_millis(options.0), timeout: Duration::from_millis(options.1) }
        }

        async fn wait(script: impl Fn(usize, &str) -> String + Send + 'static, options: WaitOptions) -> (Result<Value, Error>, Log) {
            let (port, log) = serve(script).await;
            let transport = transport(&format!("http://api.example.test:{port}"), Arc::default());
            (transport.wait(&JOB, Request::new(&STATUS).path("import_id", &7), options).await, log)
        }

        fn state(result: &Value) -> &str {
            result["progress"]["state"].as_str().unwrap()
        }

        fn line<'a>(head: &'a str, name: &str) -> Option<&'a str> {
            head.lines().find_map(|line| line.strip_prefix(&format!("{name}: ")))
        }

        /// The port a request was sent to, from its `Host`.
        fn port(head: &str) -> &str {
            line(head, "host").and_then(|host| host.rsplit(':').next()).unwrap()
        }

        fn signed(log: &Log) -> Vec<Option<String>> {
            log.lock().unwrap().iter().map(|sent| line(&sent.head, "authorization").map(str::to_owned)).collect()
        }

        #[test]
        fn wait_defaults_to_a_minute_between_polls_for_an_hour() {
            assert_eq!(WaitOptions::default(), quick((60_000, 3_600_000)));
        }

        #[tokio::test]
        async fn wait_polls_until_the_job_is_done_and_returns_its_last_status() {
            let states = ["\"WAITING\"", "\"RUNNING\"", "\"COMPLETE\""];
            let (result, log) = wait(move |number, _| status(states[number - 1]), quick((0, 5000))).await;
            assert_eq!(state(&result.unwrap()), "COMPLETE");
            let log = log.lock().unwrap();
            assert_eq!(log.len(), 3);
            assert!(log.iter().all(|sent| sent.head.starts_with("get /imports/7 ")));
        }

        #[tokio::test]
        async fn a_failed_job_returns_its_status_rather_than_an_error() {
            let (result, log) = wait(|number, _| status(if number == 1 { "\"RUNNING\"" } else { "\"FAILED\"" }), quick((0, 5000))).await;
            assert_eq!(state(&result.unwrap()), "FAILED");
            assert_eq!(log.lock().unwrap().len(), 2);
        }

        #[tokio::test]
        async fn a_job_that_outlasts_the_deadline_is_a_typed_timeout_with_its_last_status() {
            let (result, log) = wait(|_, _| status("\"RUNNING\""), quick((20, 50))).await;
            let error = result.unwrap_err();
            assert_eq!(error.kind(), ErrorKind::JobTimeout);
            assert_eq!(state(error.job_status::<Value>().unwrap()), "RUNNING");
            assert!(error.job_status::<String>().is_none());
            assert!(log.lock().unwrap().len() >= 2);

            let (result, log) = wait(|_, _| status("\"RUNNING\""), quick((0, 0))).await;
            assert_eq!(result.unwrap_err().kind(), ErrorKind::JobTimeout);
            assert_eq!(log.lock().unwrap().len(), 1);
        }

        #[tokio::test]
        async fn a_timeout_too_long_to_add_never_passes() {
            let options = WaitOptions { interval: Duration::ZERO, timeout: Duration::MAX };
            let (result, _) = wait(|number, _| status(if number == 1 { "\"RUNNING\"" } else { "\"COMPLETE\"" }), options).await;
            assert_eq!(state(&result.unwrap()), "COMPLETE");
        }

        #[tokio::test]
        async fn a_rate_limit_while_polling_is_retried_after_its_retry_after() {
            let (result, log) = wait(
                |number, _| match number {
                    1 => status("\"RUNNING\""),
                    2 => response(429, "retry-after: 0\r\n", ""),
                    _ => status("\"COMPLETE\""),
                },
                quick((0, 5000)),
            )
            .await;
            assert_eq!(state(&result.unwrap()), "COMPLETE");
            assert_eq!(log.lock().unwrap().len(), 3);
        }

        #[tokio::test]
        async fn a_state_that_is_not_a_string_is_a_decode_error() {
            for state in ["3", "null", "{\"name\":\"COMPLETE\"}"] {
                let (result, _) = wait(move |_, _| status(state), quick((0, 5000))).await;
                let error = result.unwrap_err();
                assert_eq!(error.kind(), ErrorKind::Decode);
                assert!(error.to_string().contains("progress.state"), "{error}");
            }
        }

        #[tokio::test]
        async fn dropping_a_wait_stops_it_without_waiting_out_the_interval() {
            let (port, log) = serve(|_, _| status("\"RUNNING\"")).await;
            let transport = transport(&format!("http://api.example.test:{port}"), Arc::default());
            let started = std::time::Instant::now();
            let waiting = transport.wait::<Value>(&JOB, Request::new(&STATUS).path("import_id", &7), WaitOptions::default());
            assert!(tokio::time::timeout(Duration::from_secs(1), waiting).await.is_err());
            assert!(started.elapsed() < Duration::from_secs(5));
            assert_eq!(log.lock().unwrap().len(), 1);
        }

        #[tokio::test]
        async fn a_download_url_on_the_base_origin_sends_credentials() {
            let (port, log) = serve(|_, _| csv()).await;
            let base = format!("http://api.example.test:{port}");
            let download = transport(&base, Arc::default()).download_url(&format!("{base}/files/report.csv?sig=abc"), None).await.unwrap();
            assert_eq!(download.content_type(), "text/csv");
            assert_eq!(download.bytes().await.unwrap(), CSV.as_bytes());
            let log = log.lock().unwrap();
            assert!(log[0].head.starts_with("get /files/report.csv?sig=abc "), "{}", log[0].head);
            assert_eq!(line(&log[0].head, "authorization"), Some(SECRET));
            assert_eq!(line(&log[0].head, "accept-encoding"), Some("identity"));
            assert_eq!(line(&log[0].head, "user-agent"), Some("test"));
        }

        #[tokio::test]
        async fn a_download_url_on_another_scheme_host_or_port_sends_no_credentials() {
            let (port, log) = serve(|_, _| csv()).await;
            let (other, other_log) = serve(|_, _| csv()).await;
            for (base, url) in [
                (format!("http://api.example.test:{port}"), format!("http://files.example.test:{port}/report.csv")),
                (format!("https://api.example.test:{port}"), format!("http://api.example.test:{port}/report.csv")),
                (format!("http://api.example.test:{other}"), format!("http://api.example.test:{port}/report.csv")),
            ] {
                let credentials = Arc::new(Key::default());
                let download = transport(&base, credentials.clone()).download_url(&url, None).await.unwrap();
                assert_eq!(download.bytes().await.unwrap(), CSV.as_bytes());
                assert!(credentials.signed.lock().unwrap().is_empty(), "{url}");
            }
            assert_eq!(signed(&log), [None, None, None]);
            assert!(other_log.lock().unwrap().is_empty());
        }

        #[tokio::test]
        async fn a_redirect_to_another_origin_drops_credentials_for_the_rest_of_the_chain() {
            let (port, log) = serve(|number, head| match number {
                1 => moved(&format!("http://files.example.test:{}/signed/1", port(head))),
                2 => moved(&format!("http://api.example.test:{}/files/final", port(head))),
                _ => csv(),
            })
            .await;
            let base = format!("http://api.example.test:{port}");
            let credentials = Arc::new(Key::default());
            let download = transport(&base, credentials.clone()).download_url(&format!("{base}/files/1"), None).await.unwrap();
            assert_eq!(download.bytes().await.unwrap(), CSV.as_bytes());
            let sent: Vec<(String, String)> = log
                .lock()
                .unwrap()
                .iter()
                .map(|sent| (sent.head.lines().next().unwrap().to_owned(), line(&sent.head, "host").unwrap().to_owned()))
                .collect();
            let expected = [("/files/1", "api"), ("/signed/1", "files"), ("/files/final", "api")]
                .map(|(path, host)| (format!("get {path} http/1.1"), format!("{host}.example.test:{port}")));
            assert_eq!(sent, expected);
            assert_eq!(signed(&log), [Some(SECRET.to_owned()), None, None]);
            assert_eq!(*credentials.signed.lock().unwrap(), [format!("{base}/files/1")]);
        }

        #[tokio::test]
        async fn a_relative_redirect_on_the_base_origin_keeps_credentials() {
            let (port, log) = serve(|number, _| if number == 1 { moved("/files/2") } else { csv() }).await;
            let base = format!("http://api.example.test:{port}");
            transport(&base, Arc::default()).download_url(&format!("{base}/files/1"), None).await.unwrap();
            assert_eq!(signed(&log), [Some(SECRET.to_owned()), Some(SECRET.to_owned())]);
            assert!(log.lock().unwrap()[1].head.starts_with("get /files/2 "));
        }

        #[tokio::test]
        async fn only_a_signed_request_refreshes_its_credentials_after_a_401() {
            let (port, log) = serve(|number, head| match number {
                1 | 3 => response(401, "", ""),
                2 => moved(&format!("http://files.example.test:{}/signed/1", port(head))),
                _ => csv(),
            })
            .await;
            let base = format!("http://api.example.test:{port}");
            let credentials = Arc::new(Key::default());
            let error = transport(&base, credentials.clone()).download_url(&format!("{base}/files/1"), Some(&SECURED)).await.unwrap_err();
            assert_eq!(error.status(), Some(401));
            assert_eq!(credentials.refreshes.load(Ordering::SeqCst), 1);
            assert_eq!(signed(&log), [Some(SECRET.to_owned()), Some(SECRET.to_owned()), None]);
        }

        #[tokio::test]
        async fn a_download_url_refuses_a_relative_or_non_http_url_before_any_request() {
            let (port, log) = serve(|_, _| csv()).await;
            let transport = transport(&format!("http://api.example.test:{port}"), Arc::default());
            for url in ["/files/1", "files/1", "ftp://api.example.test/files/1", "mailto:someone@example.test"] {
                let error = transport.download_url(url, None).await.unwrap_err();
                assert_eq!(error.kind(), ErrorKind::Api, "{url}");
                assert!(error.to_string().contains("absolute"), "{error}");
            }
            assert!(log.lock().unwrap().is_empty());
        }

        #[tokio::test]
        async fn a_download_url_stops_after_five_redirects() {
            let (port, log) = serve(|_, _| moved("/files/1")).await;
            let base = format!("http://api.example.test:{port}");
            let error = transport(&base, Arc::default()).download_url(&format!("{base}/files/1"), None).await.unwrap_err();
            assert_eq!(error.kind(), ErrorKind::Decode);
            assert!(error.to_string().contains("redirects"), "{error}");
            assert_eq!(log.lock().unwrap().len(), 6);
        }

        #[tokio::test]
        async fn a_redirect_without_an_http_location_is_a_decode_error() {
            for reply in [response(302, "", ""), moved("ftp://files.example.test/report.csv")] {
                let (port, log) = serve(move |_, _| reply.clone()).await;
                let base = format!("http://api.example.test:{port}");
                let error = transport(&base, Arc::default()).download_url(&format!("{base}/files/1"), None).await.unwrap_err();
                assert_eq!((error.kind(), error.status()), (ErrorKind::Decode, Some(302)));
                assert_eq!(log.lock().unwrap().len(), 1);
            }
        }

        #[test]
        fn a_logged_url_has_no_user_password_or_query() {
            let url = url::Url::parse("https://user:pass@files.example.test:8443/signed/1?sig=abc#part").unwrap();
            assert_eq!(shown(&url), "https://files.example.test:8443/signed/1");
        }
    }
}
