//! Verification of timestamped HMAC-SHA256 webhook signatures: a header of `t=<unix seconds>,v1=<hex>`,
//! signed over `<t>.<raw body>` with the endpoint's secret.

use std::fmt;
use std::time::{Duration, SystemTime, UNIX_EPOCH};

use aws_lc_rs::hmac;

/// The oldest webhook timestamp [`verify_webhook`] accepts by default.
pub const DEFAULT_WEBHOOK_TOLERANCE: Duration = Duration::from_secs(300);

/// Why [`verify_webhook`] rejected a webhook. None of them holds the secret or the body.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
#[non_exhaustive]
pub enum WebhookError {
    MalformedHeader,
    TooOld,
    BadSignature,
}

impl fmt::Display for WebhookError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.write_str(match self {
            Self::MalformedHeader => "the webhook signature header is malformed",
            Self::TooOld => "the webhook timestamp is older than the tolerance",
            Self::BadSignature => "no webhook signature matches the body",
        })
    }
}

impl std::error::Error for WebhookError {}

/// Settings for [`verify_webhook`]. `now` is the clock when it is `None`.
#[derive(Clone, Debug)]
pub struct WebhookOptions {
    pub tolerance: Duration,
    pub now: Option<SystemTime>,
}

impl Default for WebhookOptions {
    fn default() -> Self {
        Self { tolerance: DEFAULT_WEBHOOK_TOLERANCE, now: None }
    }
}

fn parse(header: &str) -> Result<(&str, Vec<&str>), WebhookError> {
    let mut timestamp = None;
    let mut signatures = Vec::new();
    for entry in header.split(',') {
        let (key, value) =
            entry.trim_matches([' ', '\t']).split_once('=').ok_or(WebhookError::MalformedHeader)?;
        match key {
            "t" => {
                if timestamp.is_some() || value.is_empty() || value.len() > 12 || !value.bytes().all(|byte| byte.is_ascii_digit()) {
                    return Err(WebhookError::MalformedHeader);
                }
                timestamp = Some(value);
            }
            "v1" => signatures.push(value),
            _ => {}
        }
    }
    match timestamp {
        Some(timestamp) if !signatures.is_empty() => Ok((timestamp, signatures)),
        _ => Err(WebhookError::MalformedHeader),
    }
}

fn decode_hex(value: &str) -> Option<Vec<u8>> {
    if value.len() != 64 || !value.bytes().all(|byte| byte.is_ascii_hexdigit()) {
        return None;
    }
    (0..value.len()).step_by(2).map(|at| u8::from_str_radix(&value[at..at + 2], 16).ok()).collect()
}

/// Checks a webhook's signature header against its raw body as received, never re-serialised. Any
/// one matching `v1` value is enough, so a header may carry several while a secret rotates.
///
/// # Panics
///
/// If `options.tolerance` is zero.
pub fn verify_webhook(
    payload: &[u8],
    header: &str,
    secret: impl AsRef<[u8]>,
    options: &WebhookOptions,
) -> Result<(), WebhookError> {
    assert!(!options.tolerance.is_zero(), "the webhook tolerance must be positive");
    let (timestamp, signatures) = parse(header)?;
    let key = hmac::Key::new(hmac::HMAC_SHA256, secret.as_ref());
    let mut message = Vec::with_capacity(timestamp.len() + 1 + payload.len());
    message.extend_from_slice(timestamp.as_bytes());
    message.push(b'.');
    message.extend_from_slice(payload);
    let mut matched = false;
    for signature in signatures {
        if let Some(tag) = decode_hex(signature) {
            matched |= hmac::verify(&key, &message, &tag).is_ok();
        }
    }
    if !matched {
        return Err(WebhookError::BadSignature);
    }
    let signed = UNIX_EPOCH + Duration::from_secs(timestamp.parse().map_err(|_| WebhookError::MalformedHeader)?);
    let now = options.now.unwrap_or_else(SystemTime::now);
    if now.duration_since(signed).is_ok_and(|age| age > options.tolerance) {
        return Err(WebhookError::TooOld);
    }
    Ok(())
}

#[cfg(test)]
mod tests {
    use serde_json::Value;

    use super::*;

    fn vectors() -> Value {
        // The shared vectors, read from the repository.
        let path = concat!(env!("CARGO_MANIFEST_DIR"), "/../../../../toolchain/conformance/fixtures/webhooks/hmac-sha256.json");
        serde_json::from_str(&std::fs::read_to_string(path).unwrap()).unwrap()
    }

    #[test]
    fn passes_the_shared_vectors() {
        let vectors = vectors();
        let secret = vectors["secret"].as_str().unwrap();
        for case in vectors["cases"].as_array().unwrap() {
            let name = case["name"].as_str().unwrap();
            let body = case["body"].as_str().unwrap();
            let options = WebhookOptions {
                tolerance: case["tolerance"].as_u64().map_or(DEFAULT_WEBHOOK_TOLERANCE, Duration::from_secs),
                now: Some(UNIX_EPOCH + Duration::from_secs(case["now"].as_u64().unwrap())),
            };
            let result = verify_webhook(body.as_bytes(), case["header"].as_str().unwrap(), secret, &options);
            let expected = match case["error"].as_str() {
                None => Ok(()),
                Some("malformed_header") => Err(WebhookError::MalformedHeader),
                Some("too_old") => Err(WebhookError::TooOld),
                Some("bad_signature") => Err(WebhookError::BadSignature),
                Some(other) => panic!("unknown error {other}"),
            };
            assert_eq!(result, expected, "{name}");
            if let Err(error) = result {
                let message = error.to_string();
                assert!(!message.contains(secret) && !message.contains(body), "{name}");
            }
        }
    }

    #[test]
    fn defaults_to_the_clock_and_five_minutes() {
        let vectors = vectors();
        let case = &vectors["cases"][0];
        let result = verify_webhook(
            case["body"].as_str().unwrap().as_bytes(),
            case["header"].as_str().unwrap(),
            vectors["secret"].as_str().unwrap().as_bytes(),
            &WebhookOptions::default(),
        );
        assert_eq!(result, Err(WebhookError::TooOld));
    }

    #[test]
    #[should_panic(expected = "tolerance must be positive")]
    fn the_tolerance_must_be_positive() {
        let options = WebhookOptions { tolerance: Duration::ZERO, now: None };
        let _ = verify_webhook(b"{}", "t=1,v1=00", "secret", &options);
    }
}
