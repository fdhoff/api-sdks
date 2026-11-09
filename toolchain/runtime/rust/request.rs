use std::collections::HashMap;
use std::fmt;
use std::sync::{Arc, Mutex};

use percent_encoding::{AsciiSet, NON_ALPHANUMERIC, utf8_percent_encode};
use serde::Serialize;
use serde::ser::{self, Error as _, Impossible};
use serde_json::Value;

use super::credentials::Scheme;
use super::model::FormValue;

/// Characters a path segment keeps as they are. Everything else is percent-encoded, `/` included.
pub(crate) const PATH_SEGMENT: &AsciiSet = &NON_ALPHANUMERIC.remove(b'-').remove(b'.').remove(b'_').remove(b'~');

/// How an iterator walks pages.
#[derive(Debug)]
pub enum Paging {
    /// Pages that link to the next one. Only `params` are read from the link: it is never fetched.
    NextLink { items: &'static str, link: &'static str, params: &'static [&'static str] },
    /// Pages addressed by an offset, which advances by the number of items received. Iteration ends
    /// at an empty page or once the offset reaches the page's `total`.
    #[allow(dead_code, reason = "an API may page only by link")]
    Offset { items: &'static str, total: &'static str, offset: &'static str },
    /// Pages that carry the next position as a value at the dotted `next` path, sent back in the `param`
    /// query parameter. Iteration ends when that value is null, empty or absent.
    #[allow(dead_code, reason = "an API may page only by link or offset")]
    Cursor { items: &'static str, next: &'static str, param: &'static str },
}

impl Paging {
    pub const DEFAULT: Self = Self::NextLink { items: "results", link: "next", params: &["page", "cursor"] };

    pub fn items(&self) -> &'static str {
        match self {
            Self::NextLink { items, .. } | Self::Offset { items, .. } | Self::Cursor { items, .. } => items,
        }
    }
}

/// How an operation reports an asynchronous job's progress. The job has ended once the string at
/// the dotted `state` path of its response is one of `done` or `failed`.
#[derive(Debug)]
#[allow(dead_code, reason = "an API may have no jobs")]
pub struct Job {
    pub state: &'static str,
    pub done: &'static [&'static str],
    pub failed: &'static [&'static str],
}

/// Describes one API call.
#[derive(Debug)]
pub struct Operation {
    pub id: &'static str,
    pub method: &'static str,
    pub path: &'static str,
    pub query_params: &'static [&'static str],
    /// Set when the spec declares a JSON success body, so an empty one is an error.
    pub returns_json: bool,
    /// How an iterator walks pages. `None` means [`Paging::DEFAULT`].
    pub paging: Option<Paging>,
    /// The spec's security requirements: any one alternative, each needing all its schemes. Empty
    /// means the operation sends no credentials, so a 401 is final.
    pub security: &'static [&'static [Scheme]],
}

impl Operation {
    pub fn paging(&self) -> &Paging {
        self.paging.as_ref().unwrap_or(&Paging::DEFAULT)
    }
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

/// A request body sent as it is: bytes, which can be resent, or a stream, which is sent once.
/// Credentials see bytes, but see a stream as an empty body, and a call never retries or refreshes
/// after sending a stream.
#[derive(Clone)]
#[allow(dead_code, reason = "an API may send no raw bodies")]
pub struct RawBody(Raw);

#[derive(Clone)]
enum Raw {
    Bytes(Vec<u8>),
    /// Shared so that a request stays cheap to clone; the first attempt takes it.
    Stream(Arc<Mutex<Option<reqwest::Body>>>),
}

#[allow(dead_code, reason = "an API may send no raw bodies")]
impl RawBody {
    /// A body that is read as it is sent, such as a file, so it is never held in memory whole.
    pub fn stream(body: impl Into<reqwest::Body>) -> Self {
        Self(Raw::Stream(Arc::new(Mutex::new(Some(body.into())))))
    }

    pub(super) fn bytes(&self) -> &[u8] {
        match &self.0 {
            Raw::Bytes(bytes) => bytes,
            Raw::Stream(_) => &[],
        }
    }

    pub(super) fn is_stream(&self) -> bool {
        matches!(self.0, Raw::Stream(_))
    }

    /// The stream to send, once. `None` for bytes, and an error for a stream already sent.
    pub(super) fn take_stream(&self) -> Result<Option<reqwest::Body>, ()> {
        match &self.0 {
            Raw::Bytes(_) => Ok(None),
            Raw::Stream(stream) => stream.lock().unwrap_or_else(|poisoned| poisoned.into_inner()).take().map(Some).ok_or(()),
        }
    }
}

impl fmt::Debug for RawBody {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match &self.0 {
            Raw::Bytes(bytes) => write!(f, "RawBody({} bytes)", bytes.len()),
            Raw::Stream(_) => f.write_str("RawBody(stream)"),
        }
    }
}

impl From<Vec<u8>> for RawBody {
    fn from(bytes: Vec<u8>) -> Self {
        Self(Raw::Bytes(bytes))
    }
}

impl From<&[u8]> for RawBody {
    fn from(bytes: &[u8]) -> Self {
        Self(Raw::Bytes(bytes.to_vec()))
    }
}

impl<const N: usize> From<&[u8; N]> for RawBody {
    fn from(bytes: &[u8; N]) -> Self {
        Self(Raw::Bytes(bytes.to_vec()))
    }
}

#[derive(Clone, Debug)]
pub enum Body {
    Empty,
    Json(Vec<u8>),
    Multipart(Vec<Part>),
    /// `application/x-www-form-urlencoded` fields, in order. A list repeats its field.
    #[allow(dead_code, reason = "an API may send no form-encoded bodies")]
    Form(Vec<(String, String)>),
    /// Sent unchanged, with the operation's declared media type.
    #[allow(dead_code, reason = "an API may send no raw bodies")]
    Raw { content_type: &'static str, body: RawBody },
}

impl Body {
    /// True for a body that cannot be sent again.
    pub(super) fn sends_once(&self) -> bool {
        matches!(self, Self::Raw { body, .. } if body.is_stream())
    }
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
    /// The operation's host key. `None` sends the request to the settings' `base_url`.
    pub host: Option<&'static str>,
    /// The JSON body field the API deduplicates this write by. `None` means the write is not idempotent.
    pub idempotency_key: Option<&'static str>,
    /// Each default-able header the operation declares, with the caller's value if it gave one.
    pub headers: Vec<(String, Option<String>)>,
    /// Each default-able query parameter the operation declares. The client's default is sent for
    /// one the call leaves unset.
    pub query_defaults: Vec<String>,
    /// Set for a download, whose body is passed on as received.
    pub(super) download: bool,
    /// The media types a download asks for in `Accept`, instead of the client's default.
    pub accept: Option<&'static str>,
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

/// A parameter as a JSON value, except that a float becomes the text Go and TypeScript send: `100.0`
/// is `100`, there is no exponent, and `NaN` and infinities are kept rather than dropped.
pub fn param_value(value: &impl Serialize) -> Value {
    value.serialize(ParamSerializer).or_else(|_| serde_json::to_value(value)).unwrap_or(Value::Null)
}

fn float_text(value: f64, text: String) -> Value {
    if value.is_infinite() {
        return Value::String(if value > 0.0 { "+Inf" } else { "-Inf" }.to_owned());
    }
    Value::String(text)
}

/// Handles scalars, options and lists. Anything else fails, and [`param_value`] falls back to JSON.
struct ParamSerializer;

struct ParamSeq(Vec<Value>);

type Unsupported = Impossible<Value, serde_json::Error>;

fn unsupported<T>() -> Result<T, serde_json::Error> {
    Err(serde_json::Error::custom("not a scalar or a list"))
}

impl ser::Serializer for ParamSerializer {
    type Ok = Value;
    type Error = serde_json::Error;
    type SerializeSeq = ParamSeq;
    type SerializeTuple = ParamSeq;
    type SerializeTupleStruct = Unsupported;
    type SerializeTupleVariant = Unsupported;
    type SerializeMap = Unsupported;
    type SerializeStruct = Unsupported;
    type SerializeStructVariant = Unsupported;

    fn serialize_bool(self, value: bool) -> Result<Value, Self::Error> {
        Ok(Value::Bool(value))
    }
    fn serialize_i8(self, value: i8) -> Result<Value, Self::Error> {
        Ok(value.into())
    }
    fn serialize_i16(self, value: i16) -> Result<Value, Self::Error> {
        Ok(value.into())
    }
    fn serialize_i32(self, value: i32) -> Result<Value, Self::Error> {
        Ok(value.into())
    }
    fn serialize_i64(self, value: i64) -> Result<Value, Self::Error> {
        Ok(value.into())
    }
    fn serialize_u8(self, value: u8) -> Result<Value, Self::Error> {
        Ok(value.into())
    }
    fn serialize_u16(self, value: u16) -> Result<Value, Self::Error> {
        Ok(value.into())
    }
    fn serialize_u32(self, value: u32) -> Result<Value, Self::Error> {
        Ok(value.into())
    }
    fn serialize_u64(self, value: u64) -> Result<Value, Self::Error> {
        Ok(value.into())
    }
    fn serialize_f32(self, value: f32) -> Result<Value, Self::Error> {
        Ok(float_text(value.into(), value.to_string()))
    }
    fn serialize_f64(self, value: f64) -> Result<Value, Self::Error> {
        Ok(float_text(value, value.to_string()))
    }
    fn serialize_char(self, value: char) -> Result<Value, Self::Error> {
        Ok(Value::String(value.to_string()))
    }
    fn serialize_str(self, value: &str) -> Result<Value, Self::Error> {
        Ok(Value::String(value.to_owned()))
    }
    fn serialize_bytes(self, _: &[u8]) -> Result<Value, Self::Error> {
        unsupported()
    }
    fn serialize_none(self) -> Result<Value, Self::Error> {
        Ok(Value::Null)
    }
    fn serialize_some<T: ?Sized + Serialize>(self, value: &T) -> Result<Value, Self::Error> {
        value.serialize(self)
    }
    fn serialize_unit(self) -> Result<Value, Self::Error> {
        Ok(Value::Null)
    }
    fn serialize_unit_struct(self, _: &'static str) -> Result<Value, Self::Error> {
        Ok(Value::Null)
    }
    fn serialize_unit_variant(self, _: &'static str, _: u32, variant: &'static str) -> Result<Value, Self::Error> {
        Ok(Value::String(variant.to_owned()))
    }
    fn serialize_newtype_struct<T: ?Sized + Serialize>(self, _: &'static str, value: &T) -> Result<Value, Self::Error> {
        value.serialize(self)
    }
    fn serialize_newtype_variant<T: ?Sized + Serialize>(
        self,
        _: &'static str,
        _: u32,
        _: &'static str,
        _: &T,
    ) -> Result<Value, Self::Error> {
        unsupported()
    }
    fn serialize_seq(self, len: Option<usize>) -> Result<ParamSeq, Self::Error> {
        Ok(ParamSeq(Vec::with_capacity(len.unwrap_or(0))))
    }
    fn serialize_tuple(self, len: usize) -> Result<ParamSeq, Self::Error> {
        Ok(ParamSeq(Vec::with_capacity(len)))
    }
    fn serialize_tuple_struct(self, _: &'static str, _: usize) -> Result<Unsupported, Self::Error> {
        unsupported()
    }
    fn serialize_tuple_variant(self, _: &'static str, _: u32, _: &'static str, _: usize) -> Result<Unsupported, Self::Error> {
        unsupported()
    }
    fn serialize_map(self, _: Option<usize>) -> Result<Unsupported, Self::Error> {
        unsupported()
    }
    fn serialize_struct(self, _: &'static str, _: usize) -> Result<Unsupported, Self::Error> {
        unsupported()
    }
    fn serialize_struct_variant(self, _: &'static str, _: u32, _: &'static str, _: usize) -> Result<Unsupported, Self::Error> {
        unsupported()
    }
}

impl ser::SerializeSeq for ParamSeq {
    type Ok = Value;
    type Error = serde_json::Error;

    fn serialize_element<T: ?Sized + Serialize>(&mut self, value: &T) -> Result<(), Self::Error> {
        self.0.push(value.serialize(ParamSerializer)?);
        Ok(())
    }
    fn end(self) -> Result<Value, Self::Error> {
        Ok(Value::Array(self.0))
    }
}

impl ser::SerializeTuple for ParamSeq {
    type Ok = Value;
    type Error = serde_json::Error;

    fn serialize_element<T: ?Sized + Serialize>(&mut self, value: &T) -> Result<(), Self::Error> {
        ser::SerializeSeq::serialize_element(self, value)
    }
    fn end(self) -> Result<Value, Self::Error> {
        ser::SerializeSeq::end(self)
    }
}

impl Request {
    pub fn new(operation: &'static Operation) -> Self {
        Self {
            operation,
            path: operation.path.to_owned(),
            query: Vec::new(),
            body: Body::Empty,
            invalid: None,
            host: None,
            idempotency_key: None,
            headers: Vec::new(),
            query_defaults: Vec::new(),
            download: false,
            accept: None,
        }
    }

    /// Sends the request to this host key's base URL.
    #[allow(dead_code, reason = "an API may serve every operation from one host")]
    pub fn host(mut self, key: &'static str) -> Self {
        self.host = Some(key);
        self
    }

    /// Sets the media types a download asks for in `Accept`.
    #[allow(dead_code, reason = "an API may have no binary responses")]
    pub fn accept(mut self, media_types: &'static str) -> Self {
        self.accept = Some(media_types);
        self
    }

    /// Marks a write the API deduplicates by this field of its JSON body, so a failure is retried as
    /// a GET's is whenever the body sets the field.
    #[allow(dead_code, reason = "an API may mark no write as idempotent")]
    pub fn idempotency_key(mut self, field: &'static str) -> Self {
        self.idempotency_key = Some(field);
        self
    }

    /// True when a 5xx, timeout or connection failure may be retried: the request is a GET, or a
    /// write whose JSON body sets its idempotency key to something other than null or "".
    pub(super) fn repeatable(&self) -> bool {
        if self.operation.method == "GET" {
            return true;
        }
        let (Some(field), Body::Json(bytes)) = (self.idempotency_key, &self.body) else {
            return false;
        };
        let body = serde_json::from_slice::<Value>(bytes).unwrap_or(Value::Null);
        matches!(body.get(field), Some(value) if !value.is_null() && value.as_str() != Some(""))
    }

    /// Declares a header that falls back to the client's default for it. Nothing is sent for `None`
    /// unless the client has a default.
    #[allow(dead_code, reason = "an API may name no default-able headers")]
    pub fn header(&mut self, name: &str, value: &impl Serialize) {
        let value = text(&param_value(value));
        self.headers.retain(|(key, _)| !key.eq_ignore_ascii_case(name));
        self.headers.push((name.to_owned(), value));
    }

    pub fn path(mut self, name: &str, value: &impl Serialize) -> Self {
        let value = text(&param_value(value)).unwrap_or_default();
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

    /// Sends a body unchanged, as `content_type`.
    #[allow(dead_code, reason = "an API may send no raw bodies")]
    pub fn raw(mut self, content_type: &'static str, body: impl Into<RawBody>) -> Self {
        self.body = Body::Raw { content_type, body: body.into() };
        self
    }

    pub fn params(mut self, params: &impl Params) -> Self {
        params.apply(&mut self);
        self
    }

    /// Adds a query parameter, once per item for a list. Nothing is sent for `None`.
    pub fn query(&mut self, name: &str, value: &impl Serialize) {
        let items = match param_value(value) {
            Value::Array(items) => items,
            value => vec![value],
        };
        for item in items {
            if let Some(text) = text(&item) {
                self.query.push((name.to_owned(), text));
            }
        }
    }

    /// Adds a query parameter as [`Request::query`] does, falling back to the client's default for it
    /// when the call gives `None`.
    #[allow(dead_code, reason = "an API may name no default-able query parameters")]
    pub fn query_default(&mut self, name: &str, value: &impl Serialize) {
        self.query(name, value);
        self.query_defaults.push(name.to_owned());
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

    /// Adds a form-encoded field, once per item for a list. Nothing is sent for `None`.
    #[allow(dead_code, reason = "an API may send no form-encoded bodies")]
    pub fn urlencoded(&mut self, name: &str, value: &impl FormValue) {
        let mut fields = match std::mem::replace(&mut self.body, Body::Empty) {
            Body::Form(fields) => fields,
            _ => Vec::new(),
        };
        let mut parts = Vec::new();
        value.parts(name, &mut parts);
        for part in parts {
            match part {
                Part::Text { name, value } => fields.push((name, value)),
                Part::File { .. } => self.invalid = Some(format!("{name} is a file, which a form-encoded body cannot carry")),
            }
        }
        if !fields.is_empty() {
            self.body = Body::Form(fields);
        }
    }

    /// The URL, with the value in `defaults` for each default-able query parameter the call left unset.
    pub fn url(&self, base: &str, defaults: &HashMap<String, String>) -> String {
        let filled = self.query_defaults.iter().filter(|name| self.query_value(name).is_none()).filter_map(|name| defaults.get_key_value(name));
        let pairs: Vec<(&String, &String)> = self.query.iter().map(|(name, value)| (name, value)).chain(filled).collect();
        if pairs.is_empty() {
            return format!("{base}{}", self.path);
        }
        let query = url::form_urlencoded::Serializer::new(String::new()).extend_pairs(pairs).finish();
        format!("{base}{}?{query}", self.path)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    const OPERATION: Operation = Operation { id: "op", method: "GET", path: "/items/{id}", query_params: &["page"], returns_json: true, paging: None, security: &[] };

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
        assert_eq!(request.url("https://example.test", &HashMap::new()), "https://example.test/items/a%2Fb%20c");
    }

    #[test]
    fn unset_query_values_are_not_sent_and_lists_repeat() {
        let query = Query { page: None, tags: Some(vec!["a".into(), "b".into()]) };
        let request = Request::new(&OPERATION).path("id", &1).params(&query);
        assert_eq!(request.url("http://h", &HashMap::new()), "http://h/items/1?tags=a&tags=b");
    }

    #[test]
    fn floats_are_sent_as_go_and_typescript_send_them() {
        let mut request = Request::new(&OPERATION);
        for value in [100.0, 0.5, 1e16, f64::NAN, f64::INFINITY] {
            request.query("amount", &Some(value));
        }
        request.query("ratios", &vec![0.1_f32, 2.0]);
        let sent: Vec<&str> = request.query.iter().map(|(_, value)| value.as_str()).collect();
        assert_eq!(sent, ["100", "0.5", "10000000000000000", "NaN", "+Inf", "0.1", "2"]);
        let mut form = Request::new(&OPERATION);
        form.form("amount", &Some(100.0));
        let Body::Multipart(parts) = form.body else { panic!("expected a multipart body") };
        assert!(matches!(&parts[0], Part::Text { value, .. } if value == "100"));
    }

    #[test]
    fn a_null_body_is_not_sent() {
        let request = Request::new(&OPERATION).json(&None::<Value>);
        assert!(matches!(request.body, Body::Empty));
    }

    #[test]
    fn form_encoded_fields_skip_none_and_repeat_lists() {
        let mut request = Request::new(&OPERATION);
        request.urlencoded("title", &Some("a b&c".to_owned()));
        request.urlencoded("missing", &None::<String>);
        request.urlencoded("tags", &Some(vec!["x".to_owned(), "y".to_owned()]));
        request.urlencoded("price", &Some(1.5));
        let Body::Form(fields) = &request.body else { panic!("expected a form body") };
        let fields: Vec<(&str, &str)> = fields.iter().map(|(name, value)| (name.as_str(), value.as_str())).collect();
        assert_eq!(fields, [("title", "a b&c"), ("tags", "x"), ("tags", "y"), ("price", "1.5")]);
        assert!(request.invalid.is_none());
        request.urlencoded("image", &Some(File::new("a.png", b"png".to_vec())));
        assert!(request.invalid.is_some());
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
