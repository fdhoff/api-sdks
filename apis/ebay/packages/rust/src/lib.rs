#![doc = include_str!("../README.md")]
#![forbid(unsafe_code)]

pub mod account;
pub mod account_v2;
pub mod analytics;
mod client;
pub mod developer_analytics;
mod errors;
pub mod feed;
pub mod feedback;
pub mod finances;
pub mod fulfillment;
pub mod identity;
pub mod inventory;
pub mod key_management;
pub mod marketing;
pub mod media;
pub mod message;
pub mod metadata;
pub mod negotiation;
pub mod notification;
mod oauth;
pub mod post_order;
pub mod recommendation;
mod runtime;
#[cfg(feature = "signing")]
mod signing;
pub mod stores;
pub mod taxonomy;

/// The `chrono` this crate's date-times come from.
pub use chrono;
pub use client::{BuildError, Client, ClientBuilder, ENVIRONMENTS};
pub use errors::{ErrorDetail, ErrorKind, ErrorParameter, error_details};
pub use oauth::{API_SCOPE, AuthorizationRequest, OAuth, Token, authorization_url};
/// The `reqwest` this crate is built on, for [`ClientBuilder::http_client`].
pub use reqwest;
pub use runtime::{Error, File, Items};
#[cfg(feature = "signing")]
pub use signing::{COMPONENTS, SigningKey};
