//! Smoke test of the published crate, run by the published packages workflow against the mock, never the live API.
//! Built in a clean package that depends on the published version from crates.io, which the workflow checks.

use std::env;
use std::error::Error;

use ebay_sell::Client;
use ebay_sell::taxonomy::CategoryTreesGetDefaultIdParams;

#[tokio::main(flavor = "current_thread")]
async fn main() -> Result<(), Box<dyn Error>> {
    let mock = env::var("SMOKE_BASE_URL")?;
    let client = Client::builder()
        .app_token("smoke-synthetic-app-token")
        .hosts([("api", &mock), ("apiz", &mock), ("apim", &mock)])
        .marketplace_id("EBAY_US")
        .build()?;
    let params = CategoryTreesGetDefaultIdParams {
        marketplace_id: Some("EBAY_US".into()),
    };
    let tree = client
        .taxonomy()
        .category_trees()
        .get_default_id(&params)
        .await?;
    let id = tree
        .and_then(|tree| tree.category_tree_id)
        .ok_or("the category tree has no categoryTreeId")?;
    println!(
        "ebay-sell {}: got category tree {id}",
        env::var("SMOKE_VERSION")?
    );
    Ok(())
}
