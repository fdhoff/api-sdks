//! Smoke test of the published crate, run by the published packages workflow against the mock, never the live API.
//! Built in a clean package that depends on the published version from crates.io, which the workflow checks.

use std::env;
use std::error::Error;

use etsy_seller::Client;

#[tokio::main(flavor = "current_thread")]
async fn main() -> Result<(), Box<dyn Error>> {
    let client = Client::builder()
        .api_key("smoke-synthetic-keystring")
        .shared_secret("smoke-synthetic-shared-secret")
        .base_url(env::var("SMOKE_BASE_URL")?)
        .build()?;
    let pong = client.application().ping().await?;
    let id = pong
        .application_id
        .ok_or("the ping has no application_id")?;
    println!(
        "etsy-seller {}: pinged application {id}",
        env::var("SMOKE_VERSION")?
    );
    Ok(())
}
