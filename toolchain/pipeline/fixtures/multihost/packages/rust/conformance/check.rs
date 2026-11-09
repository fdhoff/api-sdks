//! Compiles the generated conformance dispatch against stand-ins for a driver's helpers.

// The fixture has no operation for some helpers, which real packages do use.
#[allow(unused_imports)]
mod dispatch;

use futures_util::TryStreamExt;
use multihost::{Download, Error, Items};
use serde::de::DeserializeOwned;
use serde_json::{Map, Value};

pub struct Case {
    pub operation: String,
    pub params: Map<String, Value>,
    pub body: Option<Value>,
    pub multipart: Map<String, Value>,
    pub paginate: bool,
}

fn coerce<T: DeserializeOwned>(value: &Value) -> T {
    serde_json::from_value(value.clone()).expect("case values fit the call")
}

pub fn arg<T: DeserializeOwned>(values: &Map<String, Value>, name: &str) -> T {
    coerce(values.get(name).unwrap_or(&Value::Null))
}

pub fn param<T: DeserializeOwned>(values: &Map<String, Value>, name: &str) -> Option<T> {
    values.get(name).map(coerce)
}

pub fn files<T>(_values: &Map<String, Value>, _name: &str) -> Option<T> {
    None
}

pub fn body<T: DeserializeOwned>(case: &Case) -> T {
    coerce(case.body.as_ref().unwrap_or(&Value::Null))
}

pub fn output<T: serde::Serialize>(result: Result<T, Error>) -> Result<Value, Error> {
    result.map(|value| serde_json::to_value(value).expect("results encode as JSON"))
}

pub async fn download_output(result: Result<Download, Error>) -> Result<Value, Error> {
    result.map(|download| Value::String(download.content_type().to_owned()))
}

pub async fn collect<T: serde::Serialize>(items: Items<T>) -> Result<Value, Error> {
    output(items.try_collect::<Vec<T>>().await)
}

fn main() {
    let _ = dispatch::dispatch;
}
