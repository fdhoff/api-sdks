//! Smoke test of the published crate, run by the published packages workflow against the mock, never the live API.
//! Built in a clean package that depends on the published version from crates.io, which the workflow checks.

use std::env;
use std::error::Error;

use backmarket_seller::Client;

#[tokio::main(flavor = "current_thread")]
async fn main() -> Result<(), Box<dyn Error>> {
    let client = Client::builder()
        .token("smoke-synthetic-token")
        .user_agent("BM-Example-Smoke;smoke@example.com")
        .locale("en-us")
        .base_url(env::var("SMOKE_BASE_URL")?)
        .build()?;
    let order = client.orders().get(1).await?;
    let id = order.order_id.ok_or("the order has no order_id")?;
    println!(
        "backmarket-seller {}: got order {id}",
        env::var("SMOKE_VERSION")?
    );
    Ok(())
}
