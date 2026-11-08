use std::fmt;

use futures_core::future::BoxFuture;
use percent_encoding::utf8_percent_encode;
use reqwest::Method;
use reqwest::header::HeaderMap;

use super::error::Error;
use super::request::{Operation, PATH_SEGMENT};

pub(crate) const REDACTED: &str = "***";

/// A security scheme an operation names, with the scopes it needs from it. An operation lists
/// alternatives, and each alternative lists schemes that must all be satisfied.
#[derive(Debug)]
#[allow(dead_code, reason = "an API reads only what its credentials need")]
pub struct Scheme {
    pub name: &'static str,
    pub scopes: &'static [&'static str],
}

/// One attempt's request, as it will be sent. `headers` may be changed; the rest is read-only.
#[derive(Debug)]
#[allow(dead_code, reason = "an API reads only what its credentials need")]
pub struct AuthRequest {
    pub method: Method,
    pub url: String,
    pub headers: HeaderMap,
    pub body: Vec<u8>,
    pub operation: &'static Operation,
}

/// Supplies each request's credentials. `apply` runs before every attempt, retries included, so it
/// can sign the final request. `secrets` lists every value to keep out of logs and errors, and is
/// called again each time, so it may change. `refresh` runs after a 401, at most once per call and
/// once at a time per transport, and returns whether to retry. All three may run concurrently.
pub trait Credentials: Send + Sync {
    fn apply<'a>(&'a self, request: &'a mut AuthRequest) -> BoxFuture<'a, Result<(), Error>>;

    fn secrets(&self) -> Vec<String>;

    fn refresh<'a>(&'a self, _request: &'a AuthRequest) -> BoxFuture<'a, Result<bool, Error>> {
        Box::pin(async { Ok(false) })
    }
}

/// The same headers on every request.
#[allow(dead_code, reason = "an API with credentials of its own uses none")]
pub struct StaticCredentials {
    headers: HeaderMap,
    secrets: Vec<String>,
}

#[allow(dead_code, reason = "an API with credentials of its own uses none")]
impl StaticCredentials {
    pub fn new(headers: HeaderMap, secrets: Vec<String>) -> Self {
        Self { headers, secrets }
    }
}

impl fmt::Debug for StaticCredentials {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.write_str("StaticCredentials(***)")
    }
}

impl Credentials for StaticCredentials {
    fn apply<'a>(&'a self, request: &'a mut AuthRequest) -> BoxFuture<'a, Result<(), Error>> {
        request.headers.extend(self.headers.clone());
        Box::pin(async { Ok(()) })
    }

    fn secrets(&self) -> Vec<String> {
        self.secrets.clone()
    }
}

/// Each secret as written and as a path or query value encodes it, longest first so that a secret
/// containing another is removed whole.
pub(crate) fn redactions(credentials: &dyn Credentials) -> Vec<String> {
    let mut forms: Vec<String> = credentials
        .secrets()
        .into_iter()
        .filter(|secret| !secret.is_empty())
        .flat_map(|secret| {
            let path = utf8_percent_encode(&secret, PATH_SEGMENT).to_string();
            let query = url::form_urlencoded::byte_serialize(secret.as_bytes()).collect();
            [secret, path, query]
        })
        .collect();
    forms.sort_by(|a, b| b.len().cmp(&a.len()).then_with(|| a.cmp(b)));
    forms.dedup();
    forms
}

pub(crate) fn redact_with(forms: &[String], text: &str) -> String {
    forms.iter().fold(text.to_owned(), |text, form| text.replace(form.as_str(), REDACTED))
}

#[cfg(test)]
pub(crate) mod tests {
    use std::sync::atomic::{AtomicUsize, Ordering};
    use std::sync::{Arc, Mutex};
    use std::time::Duration;

    use reqwest::header::{AUTHORIZATION, HeaderValue};
    use serde_json::Value;
    use tokio::io::{AsyncReadExt, AsyncWriteExt};
    use tokio::net::TcpListener;

    use super::super::request::{File, Request};
    use super::super::transport::{Settings, Transport};
    use super::*;
    use crate::ErrorKind;

    const KEY: &str = "synthetic-key";
    const SHARED: &str = "synthetic-shared-secret";

    static GET_ITEM: Operation = Operation {
        id: "get-item",
        method: "GET",
        path: "/items/{id}",
        query_params: &[],
        returns_json: true,
        paging: None,
        security: &[&[Scheme { name: "key", scopes: &[] }, Scheme { name: "user", scopes: &["items_r"] }]],
    };

    static UPLOAD: Operation = Operation {
        id: "upload",
        method: "POST",
        path: "/files",
        query_params: &[],
        returns_json: false,
        paging: None,
        security: &[&[Scheme { name: "key", scopes: &[] }]],
    };

    static TOKEN: Operation = Operation {
        id: "token",
        method: "POST",
        path: "/token",
        query_params: &[],
        returns_json: true,
        paging: None,
        security: &[],
    };

    pub(crate) struct Seen {
        method: Method,
        url: String,
        headers: HeaderMap,
        body: Vec<u8>,
        operation: &'static str,
    }

    /// A synthetic bearer token that changes on each refresh, beside a fixed key.
    #[derive(Default)]
    pub(crate) struct Tokens {
        version: AtomicUsize,
        refreshes: AtomicUsize,
        pub(crate) seen: Mutex<Vec<Seen>>,
    }

    impl Tokens {
        fn token(&self) -> String {
            format!("synthetic-access-{}", self.version.load(Ordering::SeqCst) + 1)
        }
    }

    impl Credentials for Tokens {
        fn apply<'a>(&'a self, request: &'a mut AuthRequest) -> BoxFuture<'a, Result<(), Error>> {
            Box::pin(async move {
                let seen = Seen {
                    method: request.method.clone(),
                    url: request.url.clone(),
                    headers: request.headers.clone(),
                    body: request.body.clone(),
                    operation: request.operation.id,
                };
                self.seen.lock().unwrap().push(seen);
                request.headers.insert("x-api-key", HeaderValue::from_str(&format!("{KEY}:{SHARED}")).unwrap());
                if request.operation.security.iter().any(|schemes| schemes.iter().any(|scheme| scheme.name == "user")) {
                    request.headers.insert(AUTHORIZATION, HeaderValue::from_str(&format!("Bearer {}", self.token())).unwrap());
                }
                Ok(())
            })
        }

        fn secrets(&self) -> Vec<String> {
            vec![KEY.to_owned(), SHARED.to_owned(), self.token(), "synthetic-refresh".to_owned()]
        }

        fn refresh<'a>(&'a self, _request: &'a AuthRequest) -> BoxFuture<'a, Result<bool, Error>> {
            Box::pin(async move {
                self.refreshes.fetch_add(1, Ordering::SeqCst);
                tokio::time::sleep(Duration::from_millis(10)).await;
                self.version.fetch_add(1, Ordering::SeqCst);
                Ok(true)
            })
        }
    }

    pub(crate) struct Sent {
        pub(crate) head: String,
        pub(crate) body: Vec<u8>,
    }

    pub(crate) type Log = Arc<Mutex<Vec<Sent>>>;

    /// Serves one reply per connection, picked by the request's number and lowercased head.
    pub(crate) async fn serve(reply: impl Fn(usize, &str) -> (u16, String) + Send + 'static) -> (String, Log) {
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
                    log.push(Sent { head: head.clone(), body: data[head_end..].to_vec() });
                    log.len()
                };
                let (status, body) = reply(number, &head);
                let response = format!(
                    "HTTP/1.1 {status} Status\r\ncontent-type: application/json\r\ncontent-length: {}\r\nconnection: close\r\n\r\n{body}",
                    body.len()
                );
                let _ = stream.write_all(response.as_bytes()).await;
                let _ = stream.shutdown().await;
            }
        });
        (url, log)
    }

    pub(crate) fn transport(url: &str, credentials: Arc<dyn Credentials>) -> Transport {
        let mut headers = HeaderMap::new();
        headers.insert("user-agent", HeaderValue::from_static("test"));
        Transport::new(Settings {
            base_url: url.to_owned(),
            hosts: std::collections::HashMap::new(),
            credentials,
            headers,
            header_defaults: std::collections::HashMap::new(),
            to_error: |context| {
                Error::new(ErrorKind::Api, format!("failed: {}", context.text))
                    .with_status(context.status)
                    .with_raw_body(Some(context.text))
            },
            timeout: Duration::from_secs(5),
            max_retries: 1,
            retry_base_delay: Duration::ZERO,
            rate_limit_wait: Duration::ZERO,
            max_retry_wait: Duration::ZERO,
            http: None,
        })
        .unwrap()
    }

    fn accepts(token: &'static str) -> impl Fn(usize, &str) -> (u16, String) + Send + 'static {
        move |_, head| match head.contains(&format!("authorization: bearer {token}\r\n")) {
            true => (200, r#"{"id":1}"#.to_owned()),
            false => (401, String::new()),
        }
    }

    #[tokio::test]
    async fn apply_sees_the_final_request_on_every_attempt() {
        let credentials = Arc::new(Tokens::default());
        let (url, log) = serve(|number, _| if number == 1 { (503, String::new()) } else { (200, r#"{"id":1}"#.to_owned()) }).await;
        let transport = transport(&url, credentials.clone());
        transport.call::<Value>(Request::new(&GET_ITEM).path("id", &"a b")).await.unwrap();

        let seen = credentials.seen.lock().unwrap();
        assert_eq!(seen.len(), 2);
        let first = &seen[0];
        assert_eq!(first.method, Method::GET);
        assert_eq!(first.url, format!("{url}/items/a%20b"));
        assert_eq!(first.headers["user-agent"], "test");
        assert!(first.body.is_empty());
        assert_eq!(first.operation, "get-item");
        for sent in log.lock().unwrap().iter() {
            assert!(sent.head.contains("authorization: bearer synthetic-access-1\r\n"), "{}", sent.head);
            assert!(sent.head.contains(&format!("x-api-key: {KEY}:{SHARED}\r\n")), "{}", sent.head);
        }
    }

    #[tokio::test]
    async fn apply_gets_the_multipart_bytes_that_are_sent() {
        let credentials = Arc::new(Tokens::default());
        let (url, log) = serve(|_, _| (200, String::new())).await;
        let mut request = Request::new(&UPLOAD);
        request.form("file", &Some(vec![File::new("a.txt", b"hello".to_vec())]));
        transport(&url, credentials.clone()).call::<Value>(request).await.unwrap();

        let seen = credentials.seen.lock().unwrap();
        let sent = log.lock().unwrap();
        assert_eq!(seen[0].body, sent[0].body);
        assert!(String::from_utf8_lossy(&sent[0].body).contains("hello"));
        let content_type = seen[0].headers["content-type"].to_str().unwrap().to_lowercase();
        assert!(content_type.starts_with("multipart/form-data; boundary="));
        assert!(sent[0].head.contains(&format!("content-type: {content_type}\r\n")), "{}", sent[0].head);
        assert!(!sent[0].head.contains("authorization:"));
    }

    #[tokio::test]
    async fn a_401_refreshes_once_and_retries_once() {
        let credentials = Arc::new(Tokens::default());
        let (url, _) = serve(accepts("synthetic-access-2")).await;
        transport(&url, credentials.clone()).call::<Value>(Request::new(&GET_ITEM).path("id", &1)).await.unwrap();
        assert_eq!(credentials.refreshes.load(Ordering::SeqCst), 1);

        let stale = Arc::new(Tokens::default());
        let (url, _) = serve(accepts("never")).await;
        let error = transport(&url, stale.clone()).call::<Value>(Request::new(&GET_ITEM).path("id", &1)).await.unwrap_err();
        assert_eq!(error.status(), Some(401));
        assert_eq!(stale.refreshes.load(Ordering::SeqCst), 1);
        assert_eq!(stale.seen.lock().unwrap().len(), 2);
    }

    #[tokio::test]
    async fn a_401_is_final_when_the_credentials_cannot_refresh() {
        let (url, log) = serve(|_, _| (401, String::new())).await;
        let mut headers = HeaderMap::new();
        headers.insert(AUTHORIZATION, HeaderValue::from_static("Basic synthetic"));
        let credentials = Arc::new(StaticCredentials::new(headers, vec!["synthetic".to_owned()]));
        let error = transport(&url, credentials).call::<Value>(Request::new(&GET_ITEM).path("id", &1)).await.unwrap_err();
        assert_eq!(error.status(), Some(401));
        assert_eq!(log.lock().unwrap().len(), 1);
    }

    #[tokio::test]
    async fn a_401_never_refreshes_an_operation_that_sends_no_credentials() {
        let credentials = Arc::new(Tokens::default());
        let (url, log) = serve(|_, _| (401, String::new())).await;
        let mut request = Request::new(&TOKEN);
        request.urlencoded("grant_type", &Some("refresh_token".to_owned()));
        let error = transport(&url, credentials.clone()).call::<Value>(request).await.unwrap_err();
        assert_eq!(error.status(), Some(401));
        assert_eq!(credentials.refreshes.load(Ordering::SeqCst), 0);
        let sent = log.lock().unwrap();
        assert_eq!(sent.len(), 1);
        assert_eq!(sent[0].body, b"grant_type=refresh_token");
        assert!(sent[0].head.contains("content-type: application/x-www-form-urlencoded\r\n"), "{}", sent[0].head);
    }

    #[tokio::test]
    async fn concurrent_calls_share_one_refresh() {
        let credentials = Arc::new(Tokens::default());
        let (url, _) = serve(accepts("synthetic-access-2")).await;
        let transport = transport(&url, credentials.clone());
        let calls = (0..4).map(|id| transport.call::<Value>(Request::new(&GET_ITEM).path("id", &id)));
        for result in futures_util::future::join_all(calls).await {
            result.unwrap();
        }
        assert_eq!(credentials.refreshes.load(Ordering::SeqCst), 1);
    }

    #[tokio::test]
    async fn every_secret_is_kept_out_of_errors_and_debug_output() {
        let credentials = Arc::new(Tokens::default());
        let body = format!("bad {KEY}:{SHARED} and synthetic-access-1 and synthetic-refresh");
        let (url, _) = serve(move |_, _| (400, body.clone())).await;
        let transport = transport(&url, credentials.clone());
        let error = transport.call::<Value>(Request::new(&GET_ITEM).path("id", &SHARED)).await.unwrap_err();
        assert_eq!(error.raw_body(), Some("bad ***:*** and *** and ***"));

        let auth = transport.authorize(&Request::new(&GET_ITEM).path("id", &1), Method::GET, None, Vec::new()).await.unwrap();
        let output = format!("{error} {error:?} {auth:?}");
        for secret in credentials.secrets() {
            assert!(!output.contains(&secret), "{secret} in {output}");
        }
    }

    #[test]
    fn redaction_removes_each_secret_whole_and_encoded() {
        let credentials = StaticCredentials::new(HeaderMap::new(), vec!["a b".to_owned(), "a b/c".to_owned(), String::new()]);
        let text = "a b/c, a%20b%2Fc, a+b%2Fc and a b";
        assert_eq!(redact_with(&redactions(&credentials), text), "***, ***, *** and ***");
    }
}
