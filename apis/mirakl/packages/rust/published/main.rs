//! Smoke test of the published crate, run by the published packages workflow against the mock, never a live instance.
//! Built in a clean package that depends on the published version from crates.io, which the workflow checks.

use std::env;
use std::error::Error;

use mirakl_seller::{AccountGetParams, Client};

#[tokio::main(flavor = "current_thread")]
async fn main() -> Result<(), Box<dyn Error>> {
    let mock = env::var("SMOKE_BASE_URL")?;
    let client = Client::builder()
        .base_url(&mock)
        .api_key("smoke-synthetic-shop-key")
        .build()?;
    let shop = client.account().get(&AccountGetParams::default()).await?;
    println!(
        "mirakl-seller {}: read shop {:?}",
        env::var("SMOKE_VERSION")?,
        shop.shop_id
    );
    Ok(())
}
