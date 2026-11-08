#![doc = include_str!("../README.md")]
#![forbid(unsafe_code)]

mod apis;
mod client;
mod errors;
pub mod models;
mod resources;
mod runtime;

pub use apis::*;
/// The `chrono` this crate's date-times come from.
pub use chrono;
pub use client::{BuildError, Client, ClientBuilder, Environment, Region};
pub use errors::ErrorKind;
/// The `reqwest` this crate is built on, for [`ClientBuilder::http_client`].
pub use reqwest;
pub use runtime::{Error, File, Items};
