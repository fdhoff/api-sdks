//! Synthetic client for the pipeline's compile check.

use std::sync::Arc;

mod apis;
pub mod models;
mod resources;
// The fixture's operations use only part of the runtime.
#[allow(dead_code, unused_imports)]
mod runtime;

pub use apis::*;
pub use runtime::{Download, Error, File, Items, WaitOptions};

/// The kinds the runtime raises.
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
pub enum ErrorKind {
    Api,
    Timeout,
    Connection,
    Decode,
    JobTimeout,
}

pub struct Client {
    transport: Arc<runtime::Transport>,
}
