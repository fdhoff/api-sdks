//! The hand-written part of the client: everything an operation needs that the generator does
//! badly. It holds nothing specific to any one API.
//!
//! The crate must define `ErrorKind` with at least `Api`, `Timeout`, `Connection` and `Decode`. A
//! crate that signs requests has a `signing` feature that brings in `aws-lc-rs` and `base64`. A
//! crate with binary bodies re-exports `Download` and `RawBody`. A crate whose API signs its
//! webhooks has a `webhooks` feature that brings in `aws-lc-rs`, and re-exports `verify_webhook`.

mod credentials;
mod error;
mod hosts;
mod model;
mod request;
#[cfg(any(test, feature = "signing"))]
mod signing;
mod transport;
#[cfg(any(test, feature = "webhooks"))]
mod webhooks;

#[allow(unused_imports, reason = "an API with static credentials implements none of its own")]
pub(crate) use credentials::{AuthRequest, Credentials};
pub(crate) use credentials::Scheme;
#[allow(unused_imports, reason = "an API with credentials of its own uses none")]
pub(crate) use credentials::StaticCredentials;
pub use error::{Error, ErrorContext};
#[allow(unused_imports, reason = "an API with one host defines no environments")]
pub(crate) use hosts::{Environments, select_hosts};
#[allow(unused_imports, reason = "an API may declare no enumerations")]
pub(crate) use model::open_enum;
pub(crate) use model::{Fields, FormValue, text_part, tolerant_model};
pub use request::File;
#[allow(unused_imports, reason = "an API may send no raw bodies")]
pub use request::RawBody;
pub(crate) use request::{Operation, Paging, Params, Part, Request};
#[cfg(any(test, feature = "signing"))]
#[allow(unused_imports, reason = "only an API that signs requests uses it")]
pub(crate) use signing::{ED25519, MessageSigner, RSA_V1_5_SHA256, SignerOptions, SigningError, content_digest};
#[allow(unused_imports, reason = "an API may have no binary responses")]
pub use transport::Download;
pub use transport::{Items, Settings, Transport};
#[cfg(any(test, feature = "webhooks"))]
#[allow(unused_imports, reason = "only an API that signs its webhooks uses it")]
pub use webhooks::{DEFAULT_WEBHOOK_TOLERANCE, WebhookError, WebhookOptions, verify_webhook};
