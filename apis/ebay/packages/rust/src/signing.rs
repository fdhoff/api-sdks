//! Signatures for the calls eBay requires EU- and UK-domiciled sellers to sign.

use std::fmt;

use reqwest::header::{HeaderName, HeaderValue};

use crate::runtime::{AuthRequest, MessageSigner, SignerOptions};
use crate::{Error, ErrorKind};

/// The components each signature covers, in order. `content-digest` is left out of a request with
/// no body.
pub const COMPONENTS: &[&str] = &[
    "content-digest",
    "x-ebay-signature-key",
    "@method",
    "@path",
    "@authority",
];

const PEM_BEGIN: &str = "-----BEGIN PRIVATE KEY-----";
const PEM_END: &str = "-----END PRIVATE KEY-----";
const SIGNATURE_KEY: HeaderName = HeaderName::from_static("x-ebay-signature-key");

/// A key pair from the Key Management API's `createSigningKey`: its private key, as that call
/// returns it or as a PKCS #8 PEM, and its `jwe`, which is sent as `x-ebay-signature-key`. The
/// private key is a secret, and eBay returns it only once. Debug output hides it.
#[derive(Clone)]
pub struct SigningKey {
    private_key: String,
    jwe: String,
}

impl SigningKey {
    pub fn new(private_key: impl Into<String>, jwe: impl Into<String>) -> Self {
        Self {
            private_key: private_key.into(),
            jwe: jwe.into(),
        }
    }

    /// The public key's JWE, sent as `x-ebay-signature-key`.
    pub fn jwe(&self) -> &str {
        &self.jwe
    }

    pub(crate) fn signer(&self) -> Result<Signer, String> {
        let options = SignerOptions {
            components: COMPONENTS,
            ..SignerOptions::default()
        };
        let signer = MessageSigner::new(&pem(&self.private_key), options)
            .map_err(|error| error.to_string())?;
        let mut jwe = HeaderValue::from_str(&self.jwe)
            .map_err(|_| "the signing key's jwe cannot be sent as a header")?;
        jwe.set_sensitive(true);
        let mut secrets = signer.secrets();
        secrets.push(self.private_key.trim().to_owned());
        Ok(Signer {
            signer,
            jwe,
            secrets,
        })
    }
}

impl fmt::Debug for SigningKey {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("SigningKey")
            .field("private_key", &"***")
            .field("jwe", &self.jwe)
            .finish()
    }
}

/// eBay returns the base64 body of the key without the PEM lines around it.
fn pem(private_key: &str) -> String {
    let key = private_key.trim();
    if key.starts_with(PEM_BEGIN) {
        return key.to_owned();
    }
    let body: String = key.split_whitespace().collect();
    let lines: Vec<&str> = body
        .as_bytes()
        .chunks(64)
        .map(|chunk| std::str::from_utf8(chunk).unwrap_or_default())
        .collect();
    format!("{PEM_BEGIN}\n{}\n{PEM_END}", lines.join("\n"))
}

/// Adds `x-ebay-signature-key` to each attempt's request, then signs it.
pub(crate) struct Signer {
    signer: MessageSigner,
    jwe: HeaderValue,
    secrets: Vec<String>,
}

impl Signer {
    pub(crate) fn sign(&self, request: &mut AuthRequest) -> Result<(), Error> {
        request.headers.insert(SIGNATURE_KEY, self.jwe.clone());
        self.signer.sign(request).map_err(|error| {
            Error::new(
                ErrorKind::InvalidInput,
                format!("the request cannot be signed: {error}"),
            )
        })
    }

    /// The private key in every form it may appear in.
    pub(crate) fn secrets(&self) -> &[String] {
        &self.secrets
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn a_bare_key_body_is_wrapped_as_a_pem() {
        let body = "A".repeat(100);
        let wrapped = pem(&format!("  {body}\n"));
        let lines: Vec<&str> = wrapped.lines().collect();
        assert_eq!(lines, [PEM_BEGIN, &body[..64], &body[64..], PEM_END]);
        assert_eq!(pem(&wrapped), wrapped);
    }

    #[test]
    fn debug_output_hides_the_private_key() {
        let key = SigningKey::new("synthetic-private-key", "synthetic-jwe");
        let text = format!("{key:?}");
        assert!(!text.contains("synthetic-private-key"), "{text}");
        assert!(text.contains("synthetic-jwe"));
        assert!(key.signer().is_err());
    }
}
