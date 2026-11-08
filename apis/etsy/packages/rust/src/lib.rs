#![doc = include_str!("../README.md")]
#![forbid(unsafe_code)]

mod apis;
mod client;
mod errors;
pub mod models;
mod oauth;
mod resources;
mod runtime;

pub use apis::*;
/// The `chrono` this crate's date-times come from.
pub use chrono;
pub use client::{BuildError, Client, ClientBuilder};
pub use errors::ErrorKind;
pub use oauth::{
    AUTHORIZATION_URL, AuthorizationOptions, AuthorizationRequest, OAuth, Token, authorization_url,
    code_challenge,
};
/// The `reqwest` this crate is built on, for [`ClientBuilder::http_client`].
pub use reqwest;
pub use runtime::{Error, File, Items};
