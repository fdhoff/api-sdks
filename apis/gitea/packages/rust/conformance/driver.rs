//! Conformance driver: reads cases as JSON lines and calls the public client. See the runner's README.
//!
//! The client adds `/api/v1` to the instance URL, while the cases name each path as the spec
//! declares it, because the mock serves them without the prefix. The driver sends the client's
//! requests through a local HTTP proxy that removes the prefix on the way out. A request without it
//! goes out unchanged, so its path fails the case's wire check. With `--live`, for the live scenarios
//! against a disposable Gitea container, every request goes out unchanged. See
//! `apis/gitea/docs/live.md`.

mod dispatch;

use std::io::{BufRead, Write};
use std::sync::Mutex;
use std::time::Duration;

use base64::Engine;
use futures_util::TryStreamExt;
use gitea_rest::{Client, Download, Error, File, Items};
use serde::Deserialize;
use serde::de::DeserializeOwned;
use serde_json::{Map, Value, json};
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use tokio::net::{TcpListener, TcpStream};

const API_PATH: &str = "/api/v1";

#[derive(Deserialize)]
struct Settings {
    base_url: String,
    token: String,
    username: Option<String>,
    password: Option<String>,
    otp: Option<String>,
    sudo: Option<String>,
    user_agent: Option<String>,
    timeout_ms: Option<u64>,
    max_retries: Option<u32>,
    retry_base_delay_ms: Option<u64>,
    rate_limit_wait_ms: Option<u64>,
    max_retry_wait_ms: Option<u64>,
}

#[derive(Deserialize)]
pub struct Case {
    pub operation: String,
    #[serde(default)]
    pub params: Map<String, Value>,
    pub body: Option<Value>,
    #[serde(default)]
    pub multipart: Map<String, Value>,
    #[serde(default)]
    pub paginate: bool,
}

#[derive(Deserialize)]
struct Message {
    client: Settings,
    request: Case,
}

static LOGS: Mutex<Vec<String>> = Mutex::new(Vec::new());

struct Capture;

impl log::Log for Capture {
    fn enabled(&self, metadata: &log::Metadata<'_>) -> bool {
        metadata.target().starts_with("gitea_rest")
    }

    fn log(&self, record: &log::Record<'_>) {
        if self.enabled(record.metadata()) {
            LOGS.lock().unwrap().push(record.args().to_string());
        }
    }

    fn flush(&self) {}
}

/// Reads a value of the type the client expects. Cases give numbers and strings by wire form, so
/// when the type disagrees with the case, the value is tried as the other of the two.
fn coerce<T: DeserializeOwned>(value: &Value) -> T {
    if let Ok(parsed) = T::deserialize(value) {
        return parsed;
    }
    let other = match value {
        Value::String(text) => serde_json::from_str(text).unwrap_or(Value::Null),
        Value::Number(number) => Value::String(number.to_string()),
        _ => Value::Null,
    };
    T::deserialize(&other).unwrap_or_else(|error| panic!("{value} does not fit: {error}"))
}

pub fn arg<T: DeserializeOwned>(values: &Map<String, Value>, name: &str) -> T {
    coerce(values.get(name).unwrap_or(&Value::Null))
}

pub fn param<T: DeserializeOwned>(values: &Map<String, Value>, name: &str) -> Option<T> {
    values.get(name).map(coerce)
}

/// One file or a list of them, as the client's field expects.
pub trait Files: Sized {
    fn from_files(files: Vec<File>) -> Self;
}

impl Files for File {
    fn from_files(files: Vec<File>) -> Self {
        files.into_iter().next().unwrap_or_default()
    }
}

impl Files for Vec<File> {
    fn from_files(files: Vec<File>) -> Self {
        files
    }
}

/// Files arrive as strings, and are sent as their content.
pub fn files<T: Files>(values: &Map<String, Value>, name: &str) -> Option<T> {
    let value = values.get(name)?;
    let items = match value {
        Value::Array(items) => items.clone(),
        other => vec![other.clone()],
    };
    let text = |item: &Value| {
        item.as_str()
            .map(str::to_owned)
            .unwrap_or_else(|| item.to_string())
    };
    Some(T::from_files(
        items
            .iter()
            .map(|item| File {
                name: None,
                content: text(item).into_bytes(),
            })
            .collect(),
    ))
}

pub fn body<T: DeserializeOwned>(case: &Case) -> T {
    coerce(case.body.as_ref().unwrap_or(&Value::Null))
}

pub fn output<T: serde::Serialize>(result: Result<T, Error>) -> Result<Value, Error> {
    result.map(|value| serde_json::to_value(value).expect("results encode as JSON"))
}

pub async fn collect<T: serde::Serialize>(items: Items<T>) -> Result<Value, Error> {
    output(items.try_collect::<Vec<T>>().await)
}

/// A download's content type and every byte, in base64.
pub async fn download_output(result: Result<Download, Error>) -> Result<Value, Error> {
    let download = result?;
    let content_type = download.content_type().to_owned();
    let bytes = download.bytes().await?;
    Ok(json!({
        "content_type": content_type,
        "base64": base64::engine::general_purpose::STANDARD.encode(bytes),
    }))
}

/// Rewrites a proxy request's head to the origin form, without the API prefix, and asks the origin
/// to close the connection after its reply. Returns the head and the origin's address.
fn rewrite(head: &str) -> Option<(String, String)> {
    let mut lines = head.split("\r\n");
    let mut parts = lines.next()?.splitn(3, ' ');
    let (method, target, version) = (parts.next()?, parts.next()?, parts.next()?);
    let rest = target.strip_prefix("http://")?;
    let split = rest.find('/').unwrap_or(rest.len());
    let (origin, path) = rest.split_at(split);
    let path = match path.strip_prefix(API_PATH) {
        Some(stripped) if stripped.starts_with(['/', '?']) => stripped,
        _ => path,
    };
    let path = if path.is_empty() { "/" } else { path };
    let mut out = format!("{method} {path} {version}\r\n");
    for line in lines.filter(|line| !line.is_empty()) {
        let name = line
            .split(':')
            .next()
            .unwrap_or_default()
            .to_ascii_lowercase();
        if !matches!(
            name.as_str(),
            "connection" | "proxy-connection" | "keep-alive"
        ) {
            out.push_str(line);
            out.push_str("\r\n");
        }
    }
    out.push_str("connection: close\r\n\r\n");
    Some((out, origin.to_owned()))
}

async fn forward(mut client: TcpStream) {
    let mut data = Vec::new();
    let mut buffer = [0; 8192];
    let head_end = loop {
        if let Some(end) = data.windows(4).position(|window| window == b"\r\n\r\n") {
            break end + 4;
        }
        match client.read(&mut buffer).await {
            Ok(0) | Err(_) => return,
            Ok(read) => data.extend_from_slice(&buffer[..read]),
        }
    };
    let head = String::from_utf8_lossy(&data[..head_end]).into_owned();
    let Some((head, origin)) = rewrite(&head) else {
        return;
    };
    let Ok(mut upstream) = TcpStream::connect(origin).await else {
        return;
    };
    if upstream.write_all(head.as_bytes()).await.is_err()
        || upstream.write_all(&data[head_end..]).await.is_err()
    {
        return;
    }
    let (mut client_read, mut client_write) = client.split();
    let (mut upstream_read, mut upstream_write) = upstream.split();
    let request = tokio::io::copy(&mut client_read, &mut upstream_write);
    let reply = async {
        let _ = tokio::io::copy(&mut upstream_read, &mut client_write).await;
        let _ = client_write.shutdown().await;
    };
    tokio::select! {
        () = reply => {}
        _ = request => {}
    }
}

/// Serves the proxy on a local port, and returns its URL.
async fn proxy() -> String {
    let listener = TcpListener::bind("127.0.0.1:0")
        .await
        .expect("a local port");
    let url = format!("http://{}", listener.local_addr().expect("a bound address"));
    tokio::spawn(async move {
        while let Ok((stream, _)) = listener.accept().await {
            tokio::spawn(forward(stream));
        }
    });
    url
}

/// A case that sets `username` uses Basic, with the one-time password unless it is null. Otherwise
/// the token. Without a proxy, the client sends with its own HTTP client.
fn client(settings: Settings, proxy: Option<&str>) -> Client {
    let mut builder = Client::builder().base_url(&settings.base_url);
    if let Some(proxy) = proxy {
        let http = gitea_rest::reqwest::Client::builder()
            .proxy(gitea_rest::reqwest::Proxy::http(proxy).expect("a proxy URL"))
            .pool_max_idle_per_host(0)
            .redirect(gitea_rest::reqwest::redirect::Policy::none())
            .build()
            .expect("an HTTP client");
        builder = builder.http_client(http);
    }
    builder = match settings.username {
        Some(username) => {
            let builder = builder.basic_auth(username, settings.password.unwrap_or_default());
            match settings.otp {
                Some(otp) => builder.otp(otp),
                None => builder,
            }
        }
        None => builder.token(&settings.token),
    };
    if let Some(sudo) = settings.sudo {
        builder = builder.sudo(sudo);
    }
    if let Some(user_agent) = settings.user_agent {
        builder = builder.user_agent(user_agent);
    }
    if let Some(ms) = settings.timeout_ms {
        builder = builder.timeout(Duration::from_millis(ms));
    }
    if let Some(retries) = settings.max_retries {
        builder = builder.max_retries(retries);
    }
    if let Some(ms) = settings.retry_base_delay_ms {
        builder = builder.retry_base_delay(Duration::from_millis(ms));
    }
    if let Some(ms) = settings.rate_limit_wait_ms {
        builder = builder.rate_limit_wait(Duration::from_millis(ms));
    }
    if let Some(ms) = settings.max_retry_wait_ms {
        builder = builder.max_retry_wait(Duration::from_millis(ms));
    }
    builder.build().expect("the case configures a valid client")
}

fn error_output(error: &Error) -> Value {
    let mut output = Map::new();
    output.insert("kind".into(), json!(error.kind().as_str()));
    if let Some(status) = error.status() {
        output.insert("status".into(), json!(status));
        // `raw_body()` is `None` for an empty body, which the cases give as "".
        output.insert(
            "raw_body".into(),
            json!(error.raw_body().unwrap_or_default()),
        );
    }
    if let Some(message) = error.detail() {
        output.insert("message".into(), json!(message));
    }
    Value::Object(output)
}

fn main() {
    log::set_logger(&Capture).expect("no other logger is set");
    log::set_max_level(log::LevelFilter::Trace);
    let runtime = tokio::runtime::Builder::new_current_thread()
        .enable_all()
        .build()
        .expect("a runtime");
    let live = std::env::args().skip(1).any(|arg| arg == "--live");
    let proxy = (!live).then(|| runtime.block_on(proxy()));
    let stdout = std::io::stdout();
    for line in std::io::stdin().lock().lines() {
        let message: Message =
            serde_json::from_str(&line.expect("stdin is readable")).expect("a valid message");
        LOGS.lock().unwrap().clear();
        let client = client(message.client, proxy.as_deref());
        let result = runtime.block_on(dispatch::dispatch(&client, &message.request));
        let logs = std::mem::take(&mut *LOGS.lock().unwrap());
        let reply = match result {
            Ok(result) => json!({"result": result, "logs": logs}),
            Err(error) => json!({"error": error_output(&error), "logs": logs}),
        };
        let mut out = stdout.lock();
        writeln!(out, "{reply}")
            .and_then(|()| out.flush())
            .expect("stdout is writable");
    }
}
