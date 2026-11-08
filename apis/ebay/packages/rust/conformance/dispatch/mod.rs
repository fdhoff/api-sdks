//! Routes each case to its contract's generated dispatch table.

mod account;
mod account_v2;
mod analytics;
mod developer_analytics;
mod feed;
mod feedback;
mod finances;
mod fulfillment;
mod identity;
mod inventory;
mod key_management;
mod marketing;
mod media;
mod message;
mod metadata;
mod negotiation;
mod notification;
mod recommendation;
mod stores;
mod taxonomy;

use ebay_sell::{Client, Error};
use serde_json::Value;

use crate::Case;

pub async fn dispatch(client: &Client, contract: &str, case: &Case) -> Result<Value, Error> {
    match contract {
        "sell_account_v1" => account::dispatch(client, case).await,
        "sell_account_v2" => account_v2::dispatch(client, case).await,
        "sell_analytics" => analytics::dispatch(client, case).await,
        "sell_feed" => feed::dispatch(client, case).await,
        "sell_finances" => finances::dispatch(client, case).await,
        "sell_fulfillment" => fulfillment::dispatch(client, case).await,
        "sell_inventory" => inventory::dispatch(client, case).await,
        "sell_marketing" => marketing::dispatch(client, case).await,
        "sell_metadata" => metadata::dispatch(client, case).await,
        "sell_negotiation" => negotiation::dispatch(client, case).await,
        "sell_recommendation" => recommendation::dispatch(client, case).await,
        "sell_stores" => stores::dispatch(client, case).await,
        "commerce_feedback" => feedback::dispatch(client, case).await,
        "commerce_identity" => identity::dispatch(client, case).await,
        "commerce_media" => media::dispatch(client, case).await,
        "commerce_message" => message::dispatch(client, case).await,
        "commerce_notification" => notification::dispatch(client, case).await,
        "commerce_taxonomy" => taxonomy::dispatch(client, case).await,
        "developer_analytics" => developer_analytics::dispatch(client, case).await,
        "developer_key_management" => key_management::dispatch(client, case).await,
        other => panic!("no contract {other}"),
    }
}
