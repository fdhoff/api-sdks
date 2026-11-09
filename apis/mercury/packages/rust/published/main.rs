//! Smoke test of the published crate, run by the published packages workflow against the mock, never the live API.
//! Built in a clean package that depends on the published version from crates.io, which the workflow checks.

use std::env;
use std::error::Error;

use mercury_banking::{AccountsListParams, Client};

#[tokio::main(flavor = "current_thread")]
async fn main() -> Result<(), Box<dyn Error>> {
    let mock = env::var("SMOKE_BASE_URL")?;
    let client = Client::builder()
        .token("secret-token:smoke-synthetic-token")
        .hosts([("api", &mock), ("vault", &mock)])
        .build()?;
    let page = client
        .accounts()
        .list(&AccountsListParams::default())
        .await?;
    let accounts = page.accounts.ok_or("the page has no accounts")?;
    println!(
        "mercury-banking {}: listed {} accounts",
        env::var("SMOKE_VERSION")?,
        accounts.len()
    );
    Ok(())
}
