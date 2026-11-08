//! The hand-written part of the client: everything an operation needs that the generator does
//! badly. It holds nothing specific to any one API.
//!
//! The crate must define `ErrorKind` with at least `Api`, `Timeout`, `Connection` and `Decode`.

mod credentials;
mod error;
mod model;
mod request;
mod transport;

#[allow(unused_imports, reason = "an API with static credentials implements none of its own")]
pub(crate) use credentials::{AuthRequest, Credentials};
pub(crate) use credentials::Scheme;
#[allow(unused_imports, reason = "an API with credentials of its own uses none")]
pub(crate) use credentials::StaticCredentials;
pub use error::{Error, ErrorContext};
#[allow(unused_imports, reason = "an API may declare no enumerations")]
pub(crate) use model::open_enum;
pub(crate) use model::{Fields, FormValue, text_part, tolerant_model};
pub use request::File;
pub(crate) use request::{Operation, Paging, Params, Part, Request};
pub use transport::{Items, Settings, Transport};
