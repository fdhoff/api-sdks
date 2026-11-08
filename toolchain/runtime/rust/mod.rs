//! The hand-written part of the client: everything an operation needs that the generator does
//! badly. It holds nothing specific to any one API.
//!
//! The crate must define `ErrorKind` with at least `Api`, `Timeout`, `Connection` and `Decode`. A
//! crate that signs requests has a `signing` feature that brings in `aws-lc-rs` and `base64`.

mod credentials;
mod error;
mod hosts;
mod model;
mod request;
#[cfg(any(test, feature = "signing"))]
mod signing;
mod transport;

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
pub(crate) use request::{Operation, Paging, Params, Part, Request};
#[cfg(any(test, feature = "signing"))]
#[allow(unused_imports, reason = "only an API that signs requests uses it")]
pub(crate) use signing::{ED25519, MessageSigner, RSA_V1_5_SHA256, SignerOptions, SigningError, content_digest};
pub use transport::{Items, Settings, Transport};
