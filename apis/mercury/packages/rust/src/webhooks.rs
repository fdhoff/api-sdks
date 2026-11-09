//! Checks that a webhook came from Mercury. Mercury's sandbox sends no webhooks, so this is the way
//! to test a handler.

pub use crate::runtime::{DEFAULT_WEBHOOK_TOLERANCE, WebhookError, WebhookOptions, verify_webhook};

/// The request header that carries a webhook's signature.
pub const SIGNATURE_HEADER: &str = "Mercury-Signature";

#[cfg(test)]
mod tests {
    use std::time::{Duration, UNIX_EPOCH};

    use serde_json::Value;

    use super::*;

    fn vectors(path: &str) -> Value {
        let path = format!("{}/../../../../{path}", env!("CARGO_MANIFEST_DIR"));
        serde_json::from_str(&std::fs::read_to_string(path).unwrap()).unwrap()
    }

    fn mercury() -> Value {
        vectors("apis/mercury/conformance/webhooks/mercury-signature.json")
    }

    #[test]
    fn the_header_is_the_one_mercury_sends() {
        assert_eq!(mercury()["header_name"], SIGNATURE_HEADER);
    }

    #[test]
    fn passes_the_mercury_and_shared_vectors() {
        let shared = vectors("toolchain/conformance/fixtures/webhooks/hmac-sha256.json");
        for vectors in [mercury(), shared] {
            let secret = vectors["secret"].as_str().unwrap();
            for case in vectors["cases"].as_array().unwrap() {
                let name = case["name"].as_str().unwrap();
                let body = case["body"].as_str().unwrap();
                let tolerance = match case.get("tolerance") {
                    None => DEFAULT_WEBHOOK_TOLERANCE,
                    // A Duration cannot hold a negative value, NaN or infinity.
                    Some(seconds) => match seconds.as_u64() {
                        Some(seconds) => Duration::from_secs(seconds),
                        None => continue,
                    },
                };
                let options = WebhookOptions {
                    tolerance,
                    now: Some(UNIX_EPOCH + Duration::from_secs(case["now"].as_u64().unwrap())),
                };
                let result = verify_webhook(
                    body.as_bytes(),
                    case["header"].as_str().unwrap(),
                    secret,
                    &options,
                );
                let expected = match case["error"].as_str() {
                    None => Ok(()),
                    Some("malformed_header") => Err(WebhookError::MalformedHeader),
                    Some("too_old") => Err(WebhookError::TooOld),
                    Some("bad_signature") => Err(WebhookError::BadSignature),
                    Some("invalid_tolerance") => Err(WebhookError::InvalidTolerance),
                    Some(other) => panic!("unknown error {other}"),
                };
                assert_eq!(result, expected, "{name}");
                if let Err(error) = result {
                    let message = error.to_string();
                    assert!(
                        !message.contains(secret) && !message.contains(body),
                        "{name}"
                    );
                }
            }
        }
    }

    #[test]
    fn a_zero_tolerance_is_rejected() {
        let vectors = mercury();
        let case = &vectors["cases"][0];
        let options = WebhookOptions {
            tolerance: Duration::ZERO,
            now: None,
        };
        let result = verify_webhook(
            case["body"].as_str().unwrap().as_bytes(),
            case["header"].as_str().unwrap(),
            vectors["secret"].as_str().unwrap(),
            &options,
        );
        assert_eq!(result, Err(WebhookError::InvalidTolerance));
    }

    #[test]
    fn an_empty_header_is_malformed() {
        let result = verify_webhook(b"{}", "", "secret", &WebhookOptions::default());
        assert_eq!(result, Err(WebhookError::MalformedHeader));
    }
}
