use std::collections::VecDeque;
use std::fmt;
use std::io::Read;
use std::pin::Pin;
use std::sync::Arc;
use std::time::{Duration, SystemTime};

use futures_core::Stream;
use reqwest::header::{ACCEPT_ENCODING, CONTENT_ENCODING, CONTENT_TYPE, HeaderMap, HeaderValue};
use reqwest::{Method, StatusCode, multipart, redirect};
use serde::de::DeserializeOwned;
use serde_json::Value;

use super::error::{Error, ErrorContext};
use super::request::{Body, Operation, Paging, Part, Request};
use crate::ErrorKind;

const REDACTED: &str = "***";

/// A backoff doubles per retry, and this keeps the shift in range for any retry count.
const MAX_BACKOFF_DOUBLINGS: u32 = 20;

/// A stream of every item across all pages. It ends after yielding an error.
pub type Items<T> = Pin<Box<dyn Stream<Item = Result<T, Error>> + Send>>;

/// Configures a [`Transport`].
pub struct Settings {
    pub base_url: String,
    pub secret: String,
    pub headers: HeaderMap,
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

fn form(parts: &[Part]) -> multipart::Form {
    parts
        .iter()
        .fold(multipart::Form::new(), |form, part| match part {
            Part::Text { name, value } => form.text(name.clone(), value.clone()),
            Part::File { name, file } => {
                let filename = file.name.clone().unwrap_or_else(|| name.clone());
                form.part(
                    name.clone(),
                    multipart::Part::bytes(file.content.clone()).file_name(filename),
                )
            }
        })
}

impl Transport {
    /// Builds a transport. Its own client never follows a redirect: a redirect is reported as a
    /// failure, so the token cannot be sent anywhere but the configured server. A caller's client
    /// keeps its own redirect policy. Headers are sent on each request, so either client sends them.
    pub fn new(mut settings: Settings) -> Result<Self, reqwest::Error> {
        let secret = settings.secret.as_bytes();
        for value in settings.headers.values_mut() {
            if !secret.is_empty()
                && value
                    .as_bytes()
                    .windows(secret.len())
                    .any(|window| window == secret)
            {
                value.set_sensitive(true);
            }
        }
        settings
            .headers
            .insert(ACCEPT_ENCODING, HeaderValue::from_static("gzip"));
        let http = match settings.http.take() {
            Some(http) => http,
            None => reqwest::Client::builder()
                .redirect(redirect::Policy::none())
                .build()?,
        };
        Ok(Self { settings, http })
    }

    fn redact(&self, text: &str) -> String {
        if self.settings.secret.is_empty() {
            return text.to_owned();
        }
        text.replace(&self.settings.secret, REDACTED)
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

    async fn send(&self, request: &Request, method: Method) -> Result<Answer, Error> {
        let mut outgoing = self
            .http
            .request(method, request.url(&self.settings.base_url))
            .headers(self.settings.headers.clone());
        outgoing = match &request.body {
            Body::Empty => outgoing,
            Body::Json(bytes) => outgoing
                .header(CONTENT_TYPE, "application/json")
                .body(bytes.clone()),
            Body::Multipart(parts) => outgoing.multipart(form(parts)),
        };
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
    async fn attempt(&self, request: &Request, method: Method) -> Result<Answer, Error> {
        let sent = tokio::time::timeout(self.settings.timeout, self.send(request, method));
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
        let method = &request.operation.method;
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
        let mut tries = 0;
        loop {
            let url = request.url(&self.settings.base_url);
            self.log(
                log::Level::Debug,
                format_args!("request {} {method} {url}", request.operation.id),
            );
            let failure = match self.attempt(request, method.clone()).await {
                Ok(answer) => return Ok(answer),
                Err(failure) => failure,
            };
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
            if operation.returns_json {
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
            secret: String::new(),
            headers,
            to_error: |context| Error::new(ErrorKind::Api, format!("status {}", context.status)),
            timeout: Duration::from_secs(1),
            max_retries: 0,
            retry_base_delay: Duration::ZERO,
            rate_limit_wait: Duration::ZERO,
            max_retry_wait: Duration::ZERO,
            http: None,
        }
    }

    #[test]
    fn an_empty_secret_marks_no_header_sensitive() {
        let mut headers = HeaderMap::new();
        headers.insert("x-name", HeaderValue::from_static("value"));
        let transport = Transport::new(settings(headers)).unwrap();
        assert!(!transport.settings.headers["x-name"].is_sensitive());
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
    };

    fn next_url(
        operation: &'static Operation,
        query: &[(&str, &str)],
        page: Value,
        received: usize,
    ) -> Option<String> {
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
        transport
            .next_request(&request, &page, &answer, received)
            .unwrap()
            .map(|next| next.url(""))
    }

    #[test]
    fn offset_paging_advances_by_the_items_received_until_the_total() {
        let page = serde_json::json!({ "total": 5 });
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
        assert_eq!(
            next_url(
                &OFFSET_LIST,
                &[("start", "3")],
                serde_json::json!({ "total": null }),
                1
            )
            .as_deref(),
            Some("/items?start=4")
        );
        assert_eq!(
            next_url(&OFFSET_LIST, &[("start", "4")], serde_json::json!({}), 0),
            None
        );
    }

    #[test]
    fn next_link_paging_reads_the_configured_fields() {
        let page = serde_json::json!({ "more": "/items?token=b", "next": "/items?token=c" });
        assert_eq!(
            next_url(&LINKED_LIST, &[], page, 1).as_deref(),
            Some("/items?token=b")
        );
        assert_eq!(
            next_url(
                &LINKED_LIST,
                &[("token", "b")],
                serde_json::json!({ "more": null, "next": "/x?token=c" }),
                1
            ),
            None
        );
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
