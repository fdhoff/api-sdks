use percent_encoding::{AsciiSet, NON_ALPHANUMERIC, utf8_percent_encode};
use serde::Serialize;
use serde_json::Value;

use super::model::FormValue;

/// Characters a path segment keeps as they are. Everything else is percent-encoded, `/` included.
const PATH_SEGMENT: &AsciiSet = &NON_ALPHANUMERIC.remove(b'-').remove(b'.').remove(b'_').remove(b'~');

/// Describes one API call.
#[derive(Debug)]
pub struct Operation {
    pub id: &'static str,
    pub method: &'static str,
    pub path: &'static str,
    pub query_params: &'static [&'static str],
}

/// A file to upload. `name` defaults to the form field's name.
#[derive(Clone, Debug, Default, PartialEq, Eq)]
pub struct File {
    pub name: Option<String>,
    pub content: Vec<u8>,
}

impl File {
    pub fn new(name: impl Into<String>, content: impl Into<Vec<u8>>) -> Self {
        Self { name: Some(name.into()), content: content.into() }
    }
}

#[derive(Clone, Debug)]
pub enum Part {
    Text { name: String, value: String },
    File { name: String, file: File },
}

/// A struct of query parameters or form fields.
pub trait Params {
    fn apply(&self, request: &mut Request);
}

#[derive(Clone, Debug)]
pub enum Body {
    Empty,
    Json(Vec<u8>),
    Multipart(Vec<Part>),
}

/// One call's method, path, query and body, ready to send and to resend.
#[derive(Clone, Debug)]
pub struct Request {
    pub operation: &'static Operation,
    pub path: String,
    pub query: Vec<(String, String)>,
    pub body: Body,
    /// A body that could not be encoded, reported when the request is sent.
    pub invalid: Option<String>,
}

/// The wire form of a scalar. `None` means the value is not sent.
pub fn text(value: &Value) -> Option<String> {
    match value {
        Value::Null => None,
        Value::String(text) => Some(text.clone()),
        Value::Bool(_) | Value::Number(_) => Some(value.to_string()),
        Value::Array(_) | Value::Object(_) => Some(value.to_string()),
    }
}

impl Request {
    pub fn new(operation: &'static Operation) -> Self {
        Self { operation, path: operation.path.to_owned(), query: Vec::new(), body: Body::Empty, invalid: None }
    }

    pub fn path(mut self, name: &str, value: &impl Serialize) -> Self {
        let value = serde_json::to_value(value).ok().and_then(|value| text(&value)).unwrap_or_default();
        let encoded = utf8_percent_encode(&value, PATH_SEGMENT).to_string();
        self.path = self.path.replace(&format!("{{{name}}}"), &encoded);
        self
    }

    /// Sends a JSON body, unless the value is null.
    pub fn json(mut self, body: &impl Serialize) -> Self {
        match serde_json::to_value(body) {
            Ok(Value::Null) => {}
            Ok(value) => self.body = Body::Json(value.to_string().into_bytes()),
            Err(error) => self.invalid = Some(error.to_string()),
        }
        self
    }

    pub fn params(mut self, params: &impl Params) -> Self {
        params.apply(&mut self);
        self
    }

    /// Adds a query parameter, once per item for a list. Nothing is sent for `None`.
    pub fn query(&mut self, name: &str, value: &impl Serialize) {
        let value = serde_json::to_value(value).unwrap_or(Value::Null);
        let items = match value {
            Value::Array(items) => items,
            value => vec![value],
        };
        for item in items {
            if let Some(text) = text(&item) {
                self.query.push((name.to_owned(), text));
            }
        }
    }

    /// Replaces a query parameter.
    pub fn set_query(&mut self, name: &str, value: &str) {
        self.query.retain(|(key, _)| key != name);
        self.query.push((name.to_owned(), value.to_owned()));
    }

    pub fn query_value(&self, name: &str) -> Option<&str> {
        self.query.iter().find(|(key, _)| key == name).map(|(_, value)| value.as_str())
    }

    /// Adds a multipart form field. Nothing is sent for `None`.
    pub fn form(&mut self, name: &str, value: &impl FormValue) {
        let mut parts = match std::mem::replace(&mut self.body, Body::Empty) {
            Body::Multipart(parts) => parts,
            _ => Vec::new(),
        };
        value.parts(name, &mut parts);
        if !parts.is_empty() {
            self.body = Body::Multipart(parts);
        }
    }

    pub fn url(&self, base: &str) -> String {
        if self.query.is_empty() {
            return format!("{base}{}", self.path);
        }
        let query = url::form_urlencoded::Serializer::new(String::new()).extend_pairs(&self.query).finish();
        format!("{base}{}?{query}", self.path)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    const OPERATION: Operation = Operation { id: "op", method: "GET", path: "/items/{id}", query_params: &["page"] };

    struct Query {
        page: Option<i64>,
        tags: Option<Vec<String>>,
    }

    impl Params for Query {
        fn apply(&self, request: &mut Request) {
            request.query("page", &self.page);
            request.query("tags", &self.tags);
        }
    }

    #[test]
    fn path_values_are_encoded_as_one_segment() {
        let request = Request::new(&OPERATION).path("id", &"a/b c");
        assert_eq!(request.url("https://example.test"), "https://example.test/items/a%2Fb%20c");
    }

    #[test]
    fn unset_query_values_are_not_sent_and_lists_repeat() {
        let query = Query { page: None, tags: Some(vec!["a".into(), "b".into()]) };
        let request = Request::new(&OPERATION).path("id", &1).params(&query);
        assert_eq!(request.url("http://h"), "http://h/items/1?tags=a&tags=b");
    }

    #[test]
    fn a_null_body_is_not_sent() {
        let request = Request::new(&OPERATION).json(&None::<Value>);
        assert!(matches!(request.body, Body::Empty));
    }

    #[test]
    fn form_fields_skip_none_and_keep_files() {
        let mut request = Request::new(&OPERATION);
        request.form("message", &Some("hello".to_owned()));
        request.form("missing", &None::<String>);
        request.form("files", &Some(vec![File::new("a.pdf", b"%PDF".to_vec())]));
        let Body::Multipart(parts) = request.body else { panic!("expected a multipart body") };
        assert_eq!(parts.len(), 2);
    }
}
