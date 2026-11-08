//! HTTP message signatures (RFC 9421) with a `Content-Digest` (RFC 9530).

use std::fmt;
use std::time::{Duration, SystemTime, UNIX_EPOCH};

use aws_lc_rs::rand::SystemRandom;
use aws_lc_rs::signature::{Ed25519KeyPair, RSA_PKCS1_SHA256, RsaKeyPair};
use base64::Engine;
use base64::engine::general_purpose::STANDARD;
use reqwest::header::{HeaderName, HeaderValue};
use url::Url;

use super::credentials::AuthRequest;

pub const ED25519: &str = "ed25519";
pub const RSA_V1_5_SHA256: &str = "rsa-v1_5-sha256";

const DERIVED: &[&str] = &[
    "@method",
    "@target-uri",
    "@authority",
    "@scheme",
    "@request-target",
    "@path",
    "@query",
];
const PEM_BEGIN: &str = "-----BEGIN PRIVATE KEY-----";
const PEM_END: &str = "-----END PRIVATE KEY-----";
/// A shorter last line of a key's base64 body is too common a string to redact.
const MIN_SECRET_LINE: usize = 16;

/// A key, setting or request that cannot be signed.
#[derive(Debug)]
pub struct SigningError(String);

impl fmt::Display for SigningError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.write_str(&self.0)
    }
}

impl std::error::Error for SigningError {}

fn invalid(message: impl Into<String>) -> SigningError {
    SigningError(message.into())
}

/// Settings for a [`MessageSigner`]. `components` are lowercase field names and the derived
/// components `@method`, `@target-uri`, `@authority`, `@scheme`, `@request-target`, `@path` and
/// `@query`.
pub struct SignerOptions<'a> {
    pub components: &'a [&'a str],
    pub label: &'a str,
    pub key_id: Option<&'a str>,
    pub include_alg: bool,
    /// Adds `expires`, this long after `created`. Whole seconds, at least 1.
    pub lifetime: Option<Duration>,
}

impl Default for SignerOptions<'_> {
    fn default() -> Self {
        Self {
            components: &[],
            label: "sig1",
            key_id: None,
            include_alg: false,
            lifetime: None,
        }
    }
}

enum Key {
    Ed25519(Ed25519KeyPair),
    Rsa(RsaKeyPair),
}

/// Signs each attempt's request: a `Content-Digest` of the body when there is one, then
/// `Signature-Input` and `Signature` over the covered components, with a fresh `created` time.
/// `content-digest` is left out of a request with no body. A request without `content-length` or
/// `host` uses the body's length, `0` for a POST or PUT without one, or the URL's authority, which
/// reqwest sends; any other field the request lacks is an error. Call [`MessageSigner::sign`] from `Credentials::apply`.
pub struct MessageSigner {
    key: Key,
    secrets: Vec<String>,
    components: Vec<String>,
    label: String,
    extra: String,
    lifetime: Option<Duration>,
    clock: Box<dyn Fn() -> SystemTime + Send + Sync>,
}

impl fmt::Debug for MessageSigner {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "MessageSigner({}, ***)", self.algorithm())
    }
}

/// The `Content-Digest` value for these exact bytes.
pub fn content_digest(body: &[u8]) -> String {
    format!(
        "sha-256=:{}:",
        STANDARD.encode(aws_lc_rs::digest::digest(&aws_lc_rs::digest::SHA256, body))
    )
}

fn quote(value: &str) -> Result<String, SigningError> {
    if !value.bytes().all(|byte| (b' '..=b'~').contains(&byte)) {
        return Err(invalid("a signature parameter must be printable ASCII"));
    }
    Ok(format!(
        "\"{}\"",
        value.replace('\\', "\\\\").replace('"', "\\\"")
    ))
}

fn is_field(name: &str) -> bool {
    !name.is_empty()
        && name.bytes().all(|byte| {
            byte.is_ascii_lowercase() || byte.is_ascii_digit() || b"!#$%&'*+.^_`|~-".contains(&byte)
        })
}

fn is_label(label: &str) -> bool {
    let mut bytes = label.bytes();
    bytes
        .next()
        .is_some_and(|first| first.is_ascii_lowercase() || first == b'*')
        && bytes.all(|byte| {
            byte.is_ascii_lowercase() || byte.is_ascii_digit() || b"_.*-".contains(&byte)
        })
}

fn load_key(pem: &str) -> Result<Key, SigningError> {
    let body = pem
        .trim()
        .strip_prefix(PEM_BEGIN)
        .and_then(|rest| rest.strip_suffix(PEM_END))
        .ok_or_else(|| invalid("the signing key must be an unencrypted PKCS #8 PEM private key"))?;
    let body: String = body.split_whitespace().collect();
    let der = STANDARD
        .decode(body)
        .map_err(|_| invalid("the signing key is not a valid private key"))?;
    if let Ok(key) = Ed25519KeyPair::from_pkcs8(&der) {
        return Ok(Key::Ed25519(key));
    }
    RsaKeyPair::from_pkcs8(&der)
        .map(Key::Rsa)
        .map_err(|_| invalid("the signing key must be Ed25519 or RSA"))
}

impl MessageSigner {
    /// `private_key` is an unencrypted PKCS #8 PEM Ed25519 or RSA private key. It is a secret.
    pub fn new(private_key: &str, options: SignerOptions<'_>) -> Result<Self, SigningError> {
        for component in options.components {
            let supported = if component.starts_with('@') {
                DERIVED.contains(component)
            } else {
                is_field(component)
            };
            if !supported {
                return Err(invalid(format!(
                    "unsupported covered component {component}"
                )));
            }
        }
        if !is_label(options.label) {
            return Err(invalid("the signature label must be a lowercase key"));
        }
        if options
            .lifetime
            .is_some_and(|lifetime| lifetime.subsec_nanos() != 0 || lifetime.as_secs() == 0)
        {
            return Err(invalid(
                "the signature lifetime must be a whole number of seconds, at least 1",
            ));
        }
        let key = load_key(private_key)?;
        let trimmed = private_key.trim();
        let lines: Vec<&str> = trimmed
            .lines()
            .skip(1)
            .take(trimmed.lines().count().saturating_sub(2))
            .map(str::trim)
            .collect();
        let mut secrets = vec![trimmed.to_owned(), lines.concat()];
        for line in lines
            .into_iter()
            .filter(|line| line.len() >= MIN_SECRET_LINE)
        {
            if !secrets.iter().any(|secret| secret == line) {
                secrets.push(line.to_owned());
            }
        }
        let mut signer = Self {
            key,
            secrets,
            components: options
                .components
                .iter()
                .map(|&name| name.to_owned())
                .collect(),
            label: options.label.to_owned(),
            extra: String::new(),
            lifetime: options.lifetime,
            clock: Box::new(SystemTime::now),
        };
        if let Some(key_id) = options.key_id {
            signer.extra.push_str(&format!(";keyid={}", quote(key_id)?));
        }
        if options.include_alg {
            signer
                .extra
                .push_str(&format!(";alg=\"{}\"", signer.algorithm()));
        }
        Ok(signer)
    }

    /// Reads `created` from this clock instead of the system's.
    pub fn with_clock(mut self, clock: impl Fn() -> SystemTime + Send + Sync + 'static) -> Self {
        self.clock = Box::new(clock);
        self
    }

    /// The signature algorithm the key needs.
    pub fn algorithm(&self) -> &'static str {
        match self.key {
            Key::Ed25519(_) => ED25519,
            Key::Rsa(_) => RSA_V1_5_SHA256,
        }
    }

    /// The private key as given, as its PEM body and as each line of that body, to redact.
    pub fn secrets(&self) -> Vec<String> {
        self.secrets.clone()
    }

    pub fn sign(&self, request: &mut AuthRequest) -> Result<(), SigningError> {
        if !request.body.is_empty() {
            request.headers.insert(
                HeaderName::from_static("content-digest"),
                header(content_digest(&request.body))?,
            );
        }
        let url =
            Url::parse(&request.url).map_err(|_| invalid("the request URL cannot be signed"))?;
        let created = (self.clock)()
            .duration_since(UNIX_EPOCH)
            .map_err(|_| invalid("the clock is before 1970"))?
            .as_secs();
        let mut covered = Vec::new();
        let mut lines = Vec::new();
        for name in &self.components {
            if name == "content-digest" && !request.headers.contains_key(name.as_str()) {
                continue;
            }
            lines.push(format!("\"{name}\": {}", value(request, &url, name)?));
            covered.push(format!("\"{name}\""));
        }
        let mut params = format!("({});created={created}{}", covered.join(" "), self.extra);
        if let Some(lifetime) = self.lifetime {
            params.push_str(&format!(";expires={}", created + lifetime.as_secs()));
        }
        lines.push(format!("\"@signature-params\": {params}"));
        let base = lines.join("\n");
        let signature = match &self.key {
            Key::Ed25519(key) => key.sign(base.as_bytes()).as_ref().to_vec(),
            Key::Rsa(key) => {
                let mut signature = vec![0; key.public_modulus_len()];
                key.sign(
                    &RSA_PKCS1_SHA256,
                    &SystemRandom::new(),
                    base.as_bytes(),
                    &mut signature,
                )
                .map_err(|_| invalid("the request could not be signed"))?;
                signature
            }
        };
        request.headers.insert(
            HeaderName::from_static("signature-input"),
            header(format!("{}={params}", self.label))?,
        );
        request.headers.insert(
            HeaderName::from_static("signature"),
            header(format!("{}=:{}:", self.label, STANDARD.encode(signature)))?,
        );
        Ok(())
    }
}

fn header(text: String) -> Result<HeaderValue, SigningError> {
    HeaderValue::try_from(text)
        .map_err(|_| invalid("a signature parameter is not a valid header value"))
}

fn authority(url: &Url) -> String {
    let host = url.host_str().unwrap_or("").to_ascii_lowercase();
    url.port()
        .map_or(host.clone(), |port| format!("{host}:{port}"))
}

/// What reqwest sends: the body's length, or `0` for a POST or PUT without a body.
fn content_length(request: &AuthRequest) -> Option<String> {
    if !request.body.is_empty() {
        return Some(request.body.len().to_string());
    }
    matches!(request.method.as_str(), "POST" | "PUT").then(|| "0".to_owned())
}

fn value(request: &AuthRequest, url: &Url, name: &str) -> Result<String, SigningError> {
    if !name.starts_with('@') {
        let mut values = request
            .headers
            .get_all(name)
            .iter()
            .map(|value| value.to_str().map(str::trim))
            .collect::<Result<Vec<_>, _>>()
            .map_err(|_| invalid(format!("the {name} field is not text")))?
            .into_iter()
            .map(str::to_owned)
            .collect::<Vec<_>>();
        if values.is_empty() && name == "content-length" {
            values.extend(content_length(request));
        }
        if values.is_empty() && name == "host" {
            values.push(authority(url));
        }
        if values.is_empty() {
            return Err(invalid(format!("the request has no {name} field to sign")));
        }
        return Ok(values.join(", "));
    }
    let query = format!("?{}", url.query().unwrap_or(""));
    Ok(match name {
        "@method" => request.method.as_str().to_ascii_uppercase(),
        "@target-uri" => url.as_str().to_owned(),
        "@authority" => authority(url),
        "@scheme" => url.scheme().to_owned(),
        "@request-target" if query.len() > 1 => format!("{}{query}", url.path()),
        "@request-target" | "@path" => url.path().to_owned(),
        _ => query,
    })
}

#[cfg(test)]
mod tests {
    use std::sync::Arc;
    use std::sync::Mutex;
    use std::sync::atomic::{AtomicU64, Ordering};

    use aws_lc_rs::signature::{
        ECDSA_P256_SHA256_ASN1_SIGNING, EcdsaKeyPair, KeyPair, UnparsedPublicKey,
    };
    use futures_core::future::BoxFuture;
    use reqwest::Method;
    use reqwest::header::HeaderMap;

    use super::super::credentials::Credentials;
    use super::super::credentials::tests::{serve, transport};
    use super::super::credentials::{Scheme, redact_with, redactions};
    use super::super::error::Error;
    use super::super::request::{Operation, Request};
    use super::*;
    use crate::ErrorKind;

    // The published test keys of RFC 9421, Appendix B.1.4 and B.1.1. The RSA key is re-encoded
    // from PKCS #1 to PKCS #8.
    const ED25519_KEY: &str = "-----BEGIN PRIVATE KEY-----
MC4CAQAwBQYDK2VwBCIEIJ+DYvh6SEqVTm50DFtMDoQikTmiCqirVv9mWG9qfSnF
-----END PRIVATE KEY-----
";
    const RSA_KEY: &str = "-----BEGIN PRIVATE KEY-----
MIIEwgIBADANBgkqhkiG9w0BAQEFAASCBKwwggSoAgEAAoIBAQCEAph22h6jLzNw
BxHzvgvxydnErMAbB3u/foA+ns+/pDaN2w8FGvBYQGd7Pp3RQMoPAZtzqfF8RcDL
mZuGBqPOvDcw4S3y4Dm3FIqhsGkoN4Es6x0koWowaZcJC8Qbth6ZzENNE/ECV4gC
BhhGNNJ39AHBVb07A0WF6SujdG2WKdXRrvmN9mCSd79iKS1K8sbfiXDbOpcENMLk
0dE5SoZOUwvg+U1lLlGLZThoI3HatQ9FwoiUTQ+4rEjhP4choWm/z6t1Xp5SA6sH
bF4jV1IUWf+ee/k6hkkQgH5Wa4qfcMJRwJlIWVA9JdJ8EOJQaHA7Dvpa5JKx/UPh
v+8ugnXTAgMBAAECggEAb8lm5JZ2hUduLnq+OAKCSODeWQ7Uqs7eet2bqeuAD0/2
po+PG4qhZoo7VwFCUTWlJan9wqdxiAPlbEQKkCdFRcbakbjN2TMJjMCHWL5zfgvq
hmgeyKsrqg1wSce97J1/Mkvn3fh6CbqnwNb6bVFDvTJS3i5FzRhKiv6rUsYm8ZAd
F4XRaYkFkeuHPl7rc+ruUTSAjC4GovxIxoDJFe0r4kbFmkiZOr40e8RZYK7T1IKr
Svzfxx5AjnlK/OZOTCq0L7wBPbMW+IxmQpFCjpI+yuoi3FlZG3LaLNrBMXQF/lLZ
UDHs77q3fAGxDWwum2hKBfdBuUQtjlqwjQlgXPsskQKBiQCyp5QmapcTcs/y1igi
MwgAqJOb2jqmw+VzwKssj0IfRRu5oDYkI4xwI2rxLJhtOqCdaUH1l9wCb9wWkDy1
hyL2bm9grwc3FCv7wVLdCjw31Enx3RTkKzAPMxh9GCEB9QbCaVaPmGnWlDMC6HBs
5cW3EodWww+HPUgG0X1jyO+CqBgctubKK7WbAnkAvSlgXQbvHzWmuUBFRHAejRh/
naQTDV3GnH4lcRHuFBFZCSLn82xQS2/7xFOqfabqq17kNcvKfzdvWpGxxJ2cILAq
0pZS6DmrZlvBU4IkK2ZHCac/XfWVZFh+PrsH/EnVkDpfcYR/iw1F40C1q5w8R6WB
Haew3SApAoGIaiodZsrWpi8HFfZfeRs8OS/0L5x6WBl3Y9btoZgsIeruc9uZ8NXT
IdxaM6FdnyNEyOYA1VH94tDYR+xEt1br1ud/dkPslLV/Aac7d7EaYc7cdkb7oC9t
6sphVg0dqE0UTDlOwBxBYMtGmQbJsFzGpmjzVgKqWqJ3B947li2U7t63HXEvKprY
2wJ4b0DzpSMb5p42dcQgOTU8Mr4S6JOEhRr/YjErMkpaXUEqvZ3jEB9HRmcRi5Gt
t4NBiBMiY6V9br8a5gjEpiAQoIUcWokBMAYjEeurU8M6JLBd3YaZVVjISaFmdtyn
wLFoQxCh6/EC1rSywwrfDpSwO29S9i8XbaapAoGIPkbARLOwU/LcZrQy9mmfcPoQ
lAuCyeu1Q9nH7PYSnbHTFzmiud4Hl8bIXU9a0/58blDoOl3PctF+b4rAEJYUpCOD
u5PFyN6uEFYRg+YQwpjBMkXk8Eb39128ctARB40Lx8caDhRdTyaEedIG3cQDXSpA
l9EOzXkzfx4bZxjAHU9mkMdJwOcMDQ==
-----END PRIVATE KEY-----
";
    const RFC_BODY: &str = r#"{"hello": "world"}"#;
    const COVERED: &[&str] = &["content-digest", "@method", "@path", "@authority"];

    static CREATE: Operation = Operation {
        id: "create",
        method: "POST",
        path: "/items",
        query_params: &[],
        returns_json: true,
        paging: None,
        security: &[&[Scheme {
            name: "key",
            scopes: &[],
        }]],
    };

    static LIST: Operation = Operation {
        id: "list",
        method: "GET",
        path: "/items",
        query_params: &[],
        returns_json: true,
        paging: None,
        security: &[&[Scheme {
            name: "key",
            scopes: &[],
        }]],
    };

    fn auth_request(
        method: Method,
        url: &str,
        headers: &[(&'static str, &str)],
        body: &[u8],
    ) -> AuthRequest {
        let mut map = HeaderMap::new();
        for (name, value) in headers {
            map.insert(
                HeaderName::from_static(name),
                HeaderValue::from_str(value).unwrap(),
            );
        }
        AuthRequest {
            method,
            url: url.to_owned(),
            headers: map,
            body: body.to_vec(),
            operation: &CREATE,
        }
    }

    fn header(request: &AuthRequest, name: &str) -> String {
        request
            .headers
            .get(name)
            .map(|value| value.to_str().unwrap().to_owned())
            .unwrap_or_default()
    }

    fn fixed(seconds: u64) -> impl Fn() -> SystemTime + Send + Sync + 'static {
        move || UNIX_EPOCH + Duration::from_secs(seconds)
    }

    fn fresh_key() -> (String, Vec<u8>) {
        let document = Ed25519KeyPair::generate_pkcs8(&SystemRandom::new()).unwrap();
        let public = Ed25519KeyPair::from_pkcs8(document.as_ref())
            .unwrap()
            .public_key()
            .as_ref()
            .to_vec();
        (
            format!(
                "{PEM_BEGIN}\n{}\n{PEM_END}\n",
                STANDARD.encode(document.as_ref())
            ),
            public,
        )
    }

    struct Seen {
        method: Method,
        url: String,
        headers: HeaderMap,
        body: Vec<u8>,
    }

    /// Adds a synthetic bearer token, signs, and keeps what it signed.
    struct Signed {
        signer: MessageSigner,
        seen: Mutex<Vec<Seen>>,
    }

    impl Credentials for Signed {
        fn apply<'a>(&'a self, request: &'a mut AuthRequest) -> BoxFuture<'a, Result<(), Error>> {
            Box::pin(async move {
                request.headers.insert(
                    "authorization",
                    HeaderValue::from_static("Bearer synthetic-token"),
                );
                self.signer
                    .sign(request)
                    .map_err(|error| Error::new(ErrorKind::Api, error.to_string()))?;
                let seen = Seen {
                    method: request.method.clone(),
                    url: request.url.clone(),
                    headers: request.headers.clone(),
                    body: request.body.clone(),
                };
                self.seen.lock().unwrap().push(seen);
                Ok(())
            })
        }

        fn secrets(&self) -> Vec<String> {
            [vec!["synthetic-token".to_owned()], self.signer.secrets()].concat()
        }
    }

    fn verify(public: &[u8], seen: &Seen, components: &[&str]) {
        let input = seen.headers["signature-input"].to_str().unwrap();
        let (label, params) = input.split_once('=').unwrap();
        let url = Url::parse(&seen.url).unwrap();
        let mut base = String::new();
        for name in components {
            let value = match *name {
                "content-digest" => seen.headers["content-digest"].to_str().unwrap().to_owned(),
                "@method" => seen.method.to_string(),
                "@path" => url.path().to_owned(),
                "content-length" => seen.body.len().to_string(),
                _ => format!("{}:{}", url.host_str().unwrap(), url.port().unwrap()),
            };
            base.push_str(&format!("\"{name}\": {value}\n"));
        }
        base.push_str(&format!("\"@signature-params\": {params}"));
        let signature = seen.headers["signature"].to_str().unwrap();
        let signature = STANDARD
            .decode(&signature[label.len() + 2..signature.len() - 1])
            .unwrap();
        UnparsedPublicKey::new(&aws_lc_rs::signature::ED25519, public)
            .verify(base.as_bytes(), &signature)
            .unwrap();
    }

    #[test]
    fn content_digest_matches_rfc_9530() {
        assert_eq!(
            content_digest(b"{\"hello\": \"world\"}\n"),
            "sha-256=:RK/0qy18MlBSVnWgjwz6lZEWjP/lF5HF9bvEF8FabDg=:"
        );
    }

    #[test]
    fn ed25519_matches_rfc_9421_appendix_b_2_6() {
        let options = SignerOptions {
            components: &[
                "date",
                "@method",
                "@path",
                "@authority",
                "content-type",
                "content-length",
            ],
            label: "sig-b26",
            key_id: Some("test-key-ed25519"),
            ..SignerOptions::default()
        };
        let signer = MessageSigner::new(ED25519_KEY, options)
            .unwrap()
            .with_clock(fixed(1618884473));
        let headers = [
            ("date", "Tue, 20 Apr 2021 02:07:55 GMT"),
            ("content-type", "application/json"),
            ("content-length", "18"),
        ];
        let mut request = auth_request(
            Method::POST,
            "https://example.com/foo?param=Value&Pet=dog",
            &headers,
            RFC_BODY.as_bytes(),
        );
        signer.sign(&mut request).unwrap();
        assert_eq!(signer.algorithm(), ED25519);
        assert_eq!(
            header(&request, "content-digest"),
            content_digest(RFC_BODY.as_bytes())
        );
        assert_eq!(
            header(&request, "signature-input"),
            r#"sig-b26=("date" "@method" "@path" "@authority" "content-type" "content-length");created=1618884473;keyid="test-key-ed25519""#
        );
        assert_eq!(
            header(&request, "signature"),
            "sig-b26=:wqcAqbmYJ2ji2glfAMaRy4gruYYnx2nEFN2HN6jrnDnQCK1u02Gb04v9EDgwUPiu4A0w6vuQv5lIp5WPpBKRCw==:"
        );
    }

    #[test]
    fn rsa_matches_rfc_9421_section_4_3() {
        let options = SignerOptions {
            components: &[
                "@method",
                "@authority",
                "@path",
                "content-digest",
                "content-type",
                "content-length",
                "forwarded",
            ],
            label: "proxy_sig",
            key_id: Some("test-key-rsa"),
            include_alg: true,
            lifetime: Some(Duration::from_secs(60)),
        };
        let signer = MessageSigner::new(RSA_KEY, options)
            .unwrap()
            .with_clock(fixed(1618884480));
        // No body, so the signer keeps the RFC's own SHA-512 digest instead of adding one.
        let headers = [
            ("content-type", "application/json"),
            ("content-length", "18"),
            ("forwarded", "for=192.0.2.123;host=example.com;proto=https"),
            (
                "content-digest",
                "sha-512=:WZDPaVn/7XgHaAy8pmojAkGWoRx2UFChF41A2svX+TaPm+AbwAgBWnrIiYllu7BNNyealdVLvRwEmTHWXvJwew==:",
            ),
        ];
        let mut request = auth_request(
            Method::POST,
            "https://origin.host.internal.example/foo?param=Value&Pet=dog",
            &headers,
            b"",
        );
        signer.sign(&mut request).unwrap();
        assert_eq!(signer.algorithm(), RSA_V1_5_SHA256);
        assert_eq!(
            header(&request, "signature-input"),
            concat!(
                r#"proxy_sig=("@method" "@authority" "@path" "content-digest" "content-type" "content-length" "forwarded")"#,
                r#";created=1618884480;keyid="test-key-rsa";alg="rsa-v1_5-sha256";expires=1618884540"#
            )
        );
        assert_eq!(
            header(&request, "signature"),
            concat!(
                "proxy_sig=:S6ZzPXSdAMOPjN/6KXfXWNO/f7V6cHm7BXYUh3YD/fRad4BCaRZxP+JH+8XY1I6+8Cy+CM5g92iHgxtRPz+MjniOaYmdkDcnL9",
                "cCpXJleXsOckpURl49GwiyUpZ10KHgOEe11sx3G2gxI8S0jnxQB+Pu68U9vVcasqOWAEObtNKKZd8tSFu7LB5YAv0RAGhB8tmpv7sFnIm9y+7X5",
                "kXQfi8NMaZaA8i2ZHwpBdg7a6CMfwnnrtflzvZdXAsD3LH2TwevU+/PBPv0B6NMNk93wUs/vfJvye+YuI87HU38lZHowtznbLVdp770I6VHR6Wf",
                "gS9ddzirrswsE1w5o0LV/g==:"
            )
        );
    }

    #[tokio::test]
    async fn each_attempt_is_signed_again_over_its_own_body() {
        let (pem, public) = fresh_key();
        let clock = Arc::new(AtomicU64::new(1700000000));
        let ticks = Arc::clone(&clock);
        let options = SignerOptions {
            components: COVERED,
            ..SignerOptions::default()
        };
        let signer = MessageSigner::new(&pem, options)
            .unwrap()
            .with_clock(move || {
                UNIX_EPOCH + Duration::from_secs(ticks.fetch_add(1, Ordering::SeqCst) + 1)
            });
        let credentials = Arc::new(Signed {
            signer,
            seen: Mutex::default(),
        });
        let (url, log) = serve(|number, _| {
            if number == 1 {
                (429, String::new())
            } else {
                (200, r#"{"id":1}"#.to_owned())
            }
        })
        .await;
        let transport = transport(&url, credentials.clone());
        let body = serde_json::json!({ "name": "synthetic" });
        transport
            .call::<serde_json::Value>(Request::new(&CREATE).json(&body))
            .await
            .unwrap();

        let seen = credentials.seen.lock().unwrap();
        let sent = log.lock().unwrap();
        assert_eq!((seen.len(), sent.len()), (2, 2));
        for (index, (seen, sent)) in seen.iter().zip(sent.iter()).enumerate() {
            assert_eq!(seen.body, sent.body);
            let digest = content_digest(&sent.body);
            assert!(
                sent.head
                    .contains(&format!("content-digest: {}\r\n", digest.to_lowercase())),
                "{}",
                sent.head
            );
            assert_eq!(header_of(seen, "content-digest"), digest);
            let input = format!(
                r#"sig1=("content-digest" "@method" "@path" "@authority");created={}"#,
                1700000001 + index
            );
            assert_eq!(header_of(seen, "signature-input"), input);
            assert!(
                sent.head.contains(&format!("signature-input: {input}\r\n")),
                "{}",
                sent.head
            );
            verify(&public, seen, COVERED);
        }
    }

    fn header_of(seen: &Seen, name: &str) -> String {
        seen.headers
            .get(name)
            .map(|value| value.to_str().unwrap().to_owned())
            .unwrap_or_default()
    }

    #[tokio::test]
    async fn a_request_without_a_body_has_no_digest() {
        let (pem, public) = fresh_key();
        let options = SignerOptions {
            components: COVERED,
            ..SignerOptions::default()
        };
        let signer = MessageSigner::new(&pem, options)
            .unwrap()
            .with_clock(fixed(1700000000));
        let credentials = Arc::new(Signed {
            signer,
            seen: Mutex::default(),
        });
        let (url, log) = serve(|_, _| (200, r#"{"id":1}"#.to_owned())).await;
        let transport = transport(&url, credentials.clone());
        transport
            .call::<serde_json::Value>(Request::new(&LIST))
            .await
            .unwrap();

        let seen = credentials.seen.lock().unwrap();
        assert!(!log.lock().unwrap()[0].head.contains("content-digest"));
        assert_eq!(
            header_of(&seen[0], "signature-input"),
            r#"sig1=("@method" "@path" "@authority");created=1700000000"#
        );
        verify(&public, &seen[0], &["@method", "@path", "@authority"]);
    }

    #[test]
    fn rejects_unsupported_keys_and_components() {
        let p256 =
            EcdsaKeyPair::generate_pkcs8(&ECDSA_P256_SHA256_ASN1_SIGNING, &SystemRandom::new())
                .unwrap();
        let p256 = format!(
            "{PEM_BEGIN}\n{}\n{PEM_END}\n",
            STANDARD.encode(p256.as_ref())
        );
        let invalid: [(&str, &[&str]); 5] = [
            (&p256, COVERED),
            ("not a key", COVERED),
            (ED25519_KEY, &["@status"]),
            (ED25519_KEY, &["Content-Type"]),
            (ED25519_KEY, &[r#""@query-param";name="Pet""#]),
        ];
        for (key, components) in invalid {
            let options = SignerOptions {
                components,
                ..SignerOptions::default()
            };
            assert!(
                MessageSigner::new(key, options).is_err(),
                "accepted {components:?}"
            );
        }
        let options = SignerOptions {
            components: &["x-missing"],
            ..SignerOptions::default()
        };
        let signer = MessageSigner::new(ED25519_KEY, options).unwrap();
        let error = signer
            .sign(&mut auth_request(
                Method::GET,
                "https://example.com/",
                &[],
                b"",
            ))
            .unwrap_err();
        assert!(error.to_string().contains("x-missing"), "{error}");
    }

    #[test]
    fn the_private_key_is_a_secret() {
        let options = SignerOptions {
            components: COVERED,
            ..SignerOptions::default()
        };
        let signer = MessageSigner::new(ED25519_KEY, options).unwrap();
        let body = "MC4CAQAwBQYDK2VwBCIEIJ+DYvh6SEqVTm50DFtMDoQikTmiCqirVv9mWG9qfSnF";
        assert!(!format!("{signer:?}").contains(body));
        let credentials = Signed {
            signer,
            seen: Mutex::default(),
        };
        let text = format!("key {} and {body}", ED25519_KEY.trim());
        assert_eq!(
            redact_with(&redactions(&credentials), &text),
            "key *** and ***"
        );
    }

    fn lifetime_signer(lifetime: Duration) -> Result<MessageSigner, SigningError> {
        let options = SignerOptions {
            components: &["@method"],
            lifetime: Some(lifetime),
            ..SignerOptions::default()
        };
        MessageSigner::new(ED25519_KEY, options)
    }

    #[test]
    fn lifetime_is_whole_seconds_of_at_least_one() {
        for lifetime in [
            Duration::ZERO,
            Duration::from_millis(500),
            Duration::from_millis(1500),
        ] {
            assert!(lifetime_signer(lifetime).is_err(), "accepted {lifetime:?}");
        }
        let signer = lifetime_signer(Duration::from_secs(1))
            .unwrap()
            .with_clock(|| UNIX_EPOCH + Duration::from_millis(1_700_000_000_900));
        let mut request = auth_request(Method::GET, "https://example.com/", &[], b"");
        signer.sign(&mut request).unwrap();
        assert_eq!(
            header(&request, "signature-input"),
            r#"sig1=("@method");created=1700000000;expires=1700000001"#
        );
    }

    #[test]
    fn a_post_or_put_without_a_body_signs_a_zero_content_length() {
        let options = SignerOptions {
            components: &["content-length"],
            ..SignerOptions::default()
        };
        let signer = MessageSigner::new(ED25519_KEY, options).unwrap();
        for method in [Method::POST, Method::PUT] {
            let mut request = auth_request(method.clone(), "https://example.com/items", &[], b"");
            let url = Url::parse(&request.url).unwrap();
            assert_eq!(
                value(&request, &url, "content-length").unwrap(),
                "0",
                "{method}"
            );
            signer.sign(&mut request).unwrap();
            assert!(!request.headers.contains_key("content-length"), "{method}");
        }
        for method in [Method::GET, Method::DELETE, Method::PATCH] {
            let mut request = auth_request(method.clone(), "https://example.com/items", &[], b"");
            let error = signer.sign(&mut request).unwrap_err();
            assert!(
                error.to_string().contains("content-length"),
                "{method}: {error}"
            );
        }
    }

    #[tokio::test]
    async fn a_post_or_put_without_a_body_sends_the_zero_content_length_it_signs() {
        static POST: Operation = Operation {
            id: "touch",
            method: "POST",
            path: "/items",
            query_params: &[],
            returns_json: false,
            paging: None,
            security: &[&[Scheme {
                name: "key",
                scopes: &[],
            }]],
        };
        static PUT: Operation = Operation {
            id: "touch",
            method: "PUT",
            path: "/items",
            query_params: &[],
            returns_json: false,
            paging: None,
            security: &[&[Scheme {
                name: "key",
                scopes: &[],
            }]],
        };
        let (pem, public) = fresh_key();
        let options = SignerOptions {
            components: &["content-length", "@method"],
            ..SignerOptions::default()
        };
        let signer = MessageSigner::new(&pem, options)
            .unwrap()
            .with_clock(fixed(1700000000));
        let credentials = Arc::new(Signed {
            signer,
            seen: Mutex::default(),
        });
        let (url, log) = serve(|_, _| (200, "{}".to_owned())).await;
        let transport = transport(&url, credentials.clone());
        for operation in [&POST, &PUT] {
            transport
                .call::<serde_json::Value>(Request::new(operation))
                .await
                .unwrap();
        }

        let seen = credentials.seen.lock().unwrap();
        let sent = log.lock().unwrap();
        assert_eq!((seen.len(), sent.len()), (2, 2));
        for (seen, sent) in seen.iter().zip(sent.iter()) {
            assert!(
                sent.head.contains("\r\ncontent-length: 0\r\n"),
                "{}",
                sent.head
            );
            verify(&public, seen, &["content-length", "@method"]);
        }
    }

    #[test]
    fn content_length_and_host_come_from_the_body_and_url_when_absent() {
        let request = auth_request(
            Method::POST,
            "https://Example.com:443/items",
            &[],
            b"synthetic",
        );
        let url = Url::parse(&request.url).unwrap();
        assert_eq!(value(&request, &url, "content-length").unwrap(), "9");
        assert_eq!(value(&request, &url, "host").unwrap(), "example.com");
        let headers = [("content-length", "18"), ("host", "proxy.example")];
        let given = auth_request(Method::POST, "https://example.com/items", &headers, b"");
        assert_eq!(value(&given, &url, "content-length").unwrap(), "18");
        assert_eq!(value(&given, &url, "host").unwrap(), "proxy.example");
        let options = SignerOptions {
            components: &["content-length", "host"],
            ..SignerOptions::default()
        };
        let signer = MessageSigner::new(ED25519_KEY, options).unwrap();
        let mut signed = auth_request(Method::POST, "https://example.com/items", &[], b"synthetic");
        signer.sign(&mut signed).unwrap();
        assert!(
            !signed.headers.contains_key("content-length") && !signed.headers.contains_key("host")
        );
        let error = signer
            .sign(&mut auth_request(
                Method::GET,
                "https://example.com/items",
                &[],
                b"",
            ))
            .unwrap_err();
        assert!(error.to_string().contains("content-length"), "{error}");
    }

    #[test]
    fn an_empty_query_is_no_query() {
        let request = auth_request(Method::GET, "https://example.com/p?", &[], b"");
        let url = Url::parse(&request.url).unwrap();
        assert_eq!(value(&request, &url, "@request-target").unwrap(), "/p");
        assert_eq!(value(&request, &url, "@query").unwrap(), "?");
    }

    #[test]
    fn each_line_of_the_key_body_is_a_secret() {
        let options = SignerOptions {
            components: COVERED,
            ..SignerOptions::default()
        };
        let credentials = Signed {
            signer: MessageSigner::new(RSA_KEY, options).unwrap(),
            seen: Mutex::default(),
        };
        let lines: Vec<&str> = RSA_KEY
            .trim()
            .lines()
            .skip(1)
            .filter(|line| !line.starts_with("-----"))
            .collect();
        let stars = vec!["***"; lines.len()].join("\r\n");
        assert_eq!(
            redact_with(&redactions(&credentials), &lines.join("\r\n")),
            stars
        );
    }
}
