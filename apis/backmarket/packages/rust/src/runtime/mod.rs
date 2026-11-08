//! The hand-written part of the client: everything an operation needs that the generator does
//! badly. It holds nothing specific to any one API.
//!
//! The crate must define `ErrorKind` with at least `Api`, `Timeout`, `Connection` and `Decode`.

mod credentials;
mod error;
mod model;
mod request;
mod transport;

#[allow(
    unused_imports,
    reason = "an API with static credentials implements none of its own"
)]
pub(crate) use credentials::{AuthRequest, Credentials};
pub(crate) use credentials::{Scheme, StaticCredentials};
pub use error::{Error, ErrorContext};
pub(crate) use model::{Fields, FormValue, open_enum, text_part, tolerant_model};
pub use request::File;
pub(crate) use request::{Operation, Paging, Params, Part, Request};
pub use transport::{Items, Settings, Transport};
