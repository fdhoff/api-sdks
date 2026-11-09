//! Conformance driver: reads cases as JSON lines and calls the public client. See the runner's README.

mod dispatch;

use std::collections::HashMap;
use std::io::{BufRead, Write};
use std::sync::Mutex;
use std::time::Duration;

use base64::Engine;
use futures_util::TryStreamExt;
use mirakl_seller::{Client, Download, Error, File, Items, WaitOptions};
use serde::Deserialize;
use serde::de::DeserializeOwned;
use serde_json::{Map, Value, json};

#[derive(Deserialize)]
struct Settings {
    base_url: String,
    token: String,
    user_agent: Option<String>,
    timeout_ms: Option<u64>,
    max_retries: Option<u32>,
    retry_base_delay_ms: Option<u64>,
    rate_limit_wait_ms: Option<u64>,
    max_retry_wait_ms: Option<u64>,
    #[serde(default)]
    query_defaults: HashMap<String, Value>,
    poll_interval_ms: Option<u64>,
    poll_timeout_ms: Option<u64>,
}

#[derive(Deserialize)]
pub struct Case {
    /// Empty for a URL download.
    #[serde(default)]
    pub operation: String,
    #[serde(default)]
    pub params: Map<String, Value>,
    pub body: Option<Value>,
    #[serde(default)]
    pub multipart: Map<String, Value>,
    #[serde(default)]
    pub paginate: bool,
    #[serde(default)]
    pub wait: bool,
    pub download: Option<String>,
}

#[derive(Deserialize)]
struct Message {
    client: Settings,
    request: Case,
}

static LOGS: Mutex<Vec<String>> = Mutex::new(Vec::new());
static WAIT: Mutex<Option<WaitOptions>> = Mutex::new(None);

struct Capture;

impl log::Log for Capture {
    fn enabled(&self, metadata: &log::Metadata<'_>) -> bool {
        metadata.target().starts_with("mirakl_seller")
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

/// The interval and deadline the case's client sets for a wait.
pub fn wait_options() -> WaitOptions {
    WAIT.lock().unwrap().unwrap_or_default()
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

fn wait_settings(settings: &Settings) -> WaitOptions {
    let mut options = WaitOptions::default();
    if let Some(ms) = settings.poll_interval_ms {
        options.interval = Duration::from_millis(ms);
    }
    if let Some(ms) = settings.poll_timeout_ms {
        options.timeout = Duration::from_millis(ms);
    }
    options
}

async fn run(client: &Client, case: &Case) -> Result<Value, Error> {
    match &case.download {
        Some(url) => download_output(client.download_url(url).await).await,
        None => dispatch::dispatch(client, case).await,
    }
}

fn client(settings: Settings) -> Client {
    let mut builder = Client::builder()
        .base_url(&settings.base_url)
        .api_key(&settings.token);
    if let Some(shop_id) = settings.query_defaults.get("shop_id") {
        builder = builder.shop_id(coerce(shop_id));
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
    Value::Object(output)
}

fn main() {
    log::set_logger(&Capture).expect("no other logger is set");
    log::set_max_level(log::LevelFilter::Trace);
    let runtime = tokio::runtime::Builder::new_current_thread()
        .enable_all()
        .build()
        .expect("a runtime");
    let stdout = std::io::stdout();
    for line in std::io::stdin().lock().lines() {
        let message: Message =
            serde_json::from_str(&line.expect("stdin is readable")).expect("a valid message");
        LOGS.lock().unwrap().clear();
        *WAIT.lock().unwrap() = Some(wait_settings(&message.client));
        let client = client(message.client);
        let result = runtime.block_on(run(&client, &message.request));
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
