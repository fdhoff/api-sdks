use std::sync::{Arc, Mutex};

use base64::Engine;
use base64::engine::general_purpose::STANDARD;
use ebay_sell::finances::PayoutsListParams;
use ebay_sell::{API_SCOPE, Client, ClientBuilder, ErrorKind, Token, error_details};
use futures_util::TryStreamExt;
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use tokio::net::{TcpListener, TcpStream};

const CLIENT_ID: &str = "synthetic-client-id";
const CLIENT_SECRET: &str = "synthetic-client-secret";
const APP: &str = "synthetic-app-token";
const MINTED: &str = "synthetic-minted-app-token";
const USER: &str = "synthetic-user-token";
const NEW_USER: &str = "synthetic-user-token-2";
const REFRESH: &str = "synthetic-refresh-token";
const TOKEN_PATH: &str = "/identity/v1/oauth2/token";
const CATEGORY_TREE_PATH: &str = "/commerce/taxonomy/v1/category_tree/0";
const INVENTORY_ITEM_PATH: &str = "/sell/inventory/v1/inventory_item/SKU-1";
const PAYOUTS_PATH: &str = "/sell/finances/v1/payout";

/// One request as the server read it. `head` is lowercased.
#[derive(Clone, Debug)]
struct Sent {
    path: String,
    query: String,
    head: String,
    body: String,
}

impl Sent {
    fn header(&self, name: &str) -> Option<String> {
        let prefix = format!("{name}: ");
        self.head
            .lines()
            .find_map(|line| line.strip_prefix(&prefix))
            .map(str::to_owned)
    }

    fn form(&self) -> Vec<(String, String)> {
        url::form_urlencoded::parse(self.body.as_bytes())
            .into_owned()
            .collect()
    }

    fn bearer(&self) -> Option<String> {
        self.header("authorization")
            .and_then(|value| value.strip_prefix("bearer ").map(str::to_owned))
    }
}

type Log = Arc<Mutex<Vec<Sent>>>;

/// Serves one JSON reply per connection, picked by the request.
async fn serve(reply: impl Fn(&Sent) -> (u16, String) + Send + Sync + 'static) -> (String, Log) {
    let listener = TcpListener::bind("127.0.0.1:0").await.unwrap();
    let url = format!("http://{}", listener.local_addr().unwrap());
    let log = Log::default();
    let kept = Arc::clone(&log);
    let reply = Arc::new(reply);
    tokio::spawn(async move {
        while let Ok((stream, _)) = listener.accept().await {
            tokio::spawn(answer(stream, Arc::clone(&reply), Arc::clone(&kept)));
        }
    });
    (url, log)
}

async fn answer(
    mut stream: TcpStream,
    reply: Arc<impl Fn(&Sent) -> (u16, String) + Send + Sync + 'static>,
    log: Log,
) {
    let mut data = Vec::new();
    let mut buffer = [0; 4096];
    let head_end = loop {
        if let Some(end) = data.windows(4).position(|window| window == b"\r\n\r\n") {
            break end + 4;
        }
        match stream.read(&mut buffer).await {
            Ok(0) | Err(_) => return,
            Ok(read) => data.extend_from_slice(&buffer[..read]),
        }
    };
    let raw_head = String::from_utf8_lossy(&data[..head_end]).into_owned();
    let head = raw_head.to_lowercase();
    let length = head
        .lines()
        .find_map(|line| line.strip_prefix("content-length:"))
        .and_then(|value| value.trim().parse::<usize>().ok())
        .unwrap_or(0);
    while data.len() < head_end + length {
        match stream.read(&mut buffer).await {
            Ok(0) | Err(_) => break,
            Ok(read) => data.extend_from_slice(&buffer[..read]),
        }
    }
    let target = raw_head.split_whitespace().nth(1).unwrap_or_default();
    let (path, query) = target.split_once('?').unwrap_or((target, ""));
    let sent = Sent {
        path: path.to_owned(),
        query: query.to_owned(),
        head,
        body: String::from_utf8_lossy(&data[head_end..]).into_owned(),
    };
    log.lock().unwrap().push(sent.clone());
    let (status, body) = reply(&sent);
    let response = format!(
        "HTTP/1.1 {status} Status\r\ncontent-type: application/json\r\ncontent-length: {}\r\nconnection: close\r\n\r\n{body}",
        body.len()
    );
    let _ = stream.write_all(response.as_bytes()).await;
    let _ = stream.shutdown().await;
}

fn builder(url: &str) -> ClientBuilder {
    Client::builder()
        .hosts([("api", url), ("apiz", url), ("apim", url)])
        .retry_base_delay(std::time::Duration::ZERO)
}

fn keyset(url: &str) -> ClientBuilder {
    builder(url)
        .client_id(CLIENT_ID)
        .client_secret(CLIENT_SECRET)
}

fn token(access: &str) -> (u16, String) {
    let body = format!(
        r#"{{"access_token":"{access}","expires_in":7200,"token_type":"User Access Token"}}"#
    );
    (200, body)
}

fn ok() -> (u16, String) {
    (200, r#"{"categoryTreeId":"0"}"#.to_owned())
}

fn unauthorized() -> (u16, String) {
    (
        401,
        r#"{"errors":[{"errorId":1001,"message":"Invalid access token"}]}"#.to_owned(),
    )
}

fn sent(log: &Log) -> Vec<Sent> {
    log.lock().unwrap().clone()
}

fn tokens() -> (
    Arc<Mutex<Vec<Token>>>,
    impl Fn(&Token) + Send + Sync + 'static,
) {
    let stored = Arc::new(Mutex::new(Vec::new()));
    let kept = Arc::clone(&stored);
    (stored, move |token: &Token| {
        kept.lock().unwrap().push(token.clone())
    })
}

#[tokio::test]
async fn app_operations_mint_one_application_token_with_basic_auth() {
    let (url, log) = serve(|sent| match sent.path.as_str() {
        TOKEN_PATH => token(MINTED),
        _ => ok(),
    })
    .await;
    let client = keyset(&url).user_token(USER).build().unwrap();
    let trees = client.taxonomy().category_trees();
    trees.get("0").await.unwrap();
    trees.get("0").await.unwrap();
    let sent = sent(&log);
    assert_eq!(sent.len(), 3, "{sent:?}");
    let basic = STANDARD.encode(format!("{CLIENT_ID}:{CLIENT_SECRET}"));
    assert_eq!(
        sent[0].header("authorization"),
        Some(format!("basic {basic}").to_lowercase())
    );
    let form = sent[0].form();
    assert!(form.contains(&("grant_type".to_owned(), "client_credentials".to_owned())));
    let scope = form.iter().find(|(key, _)| key == "scope").unwrap();
    assert!(
        scope.1.split(' ').any(|scope| scope == API_SCOPE),
        "{form:?}"
    );
    for call in &sent[1..] {
        assert_eq!(call.path, CATEGORY_TREE_PATH);
        assert_eq!(call.bearer(), Some(MINTED.to_lowercase()));
    }
}

#[tokio::test]
async fn user_operations_send_the_user_token() {
    let (url, log) = serve(|_| (200, r#"{"sku":"SKU-1"}"#.to_owned())).await;
    let client = keyset(&url).user_token(USER).build().unwrap();
    let item = client
        .inventory()
        .inventory_items()
        .get("SKU-1")
        .await
        .unwrap();
    assert_eq!(item.sku.as_deref(), Some("SKU-1"));
    let sent = sent(&log);
    assert_eq!(sent.len(), 1);
    assert_eq!(sent[0].path, INVENTORY_ITEM_PATH);
    assert_eq!(sent[0].bearer(), Some(USER.to_lowercase()));
}

#[tokio::test]
async fn an_app_operation_uses_a_supplied_app_token() {
    let (url, log) = serve(|_| ok()).await;
    let client = builder(&url).app_token(APP).build().unwrap();
    client.taxonomy().category_trees().get("0").await.unwrap();
    assert_eq!(sent(&log)[0].bearer(), Some(APP.to_lowercase()));
}

#[tokio::test]
async fn a_user_operation_without_a_user_token_is_refused() {
    let (url, log) = serve(|_| ok()).await;
    let client = builder(&url).app_token(APP).build().unwrap();
    let error = client
        .inventory()
        .inventory_items()
        .get("SKU-1")
        .await
        .unwrap_err();
    assert_eq!(error.kind(), ErrorKind::InvalidInput);
    assert!(sent(&log).is_empty());
}

#[tokio::test]
async fn a_401_re_mints_the_application_token_and_retries() {
    let (url, log) = serve(|sent| match sent.path.as_str() {
        TOKEN_PATH => token(MINTED),
        _ if sent.bearer() == Some(MINTED.to_lowercase()) => ok(),
        _ => unauthorized(),
    })
    .await;
    let client = keyset(&url).app_token(APP).build().unwrap();
    client.taxonomy().category_trees().get("0").await.unwrap();
    let paths: Vec<String> = sent(&log).into_iter().map(|sent| sent.path).collect();
    assert_eq!(paths, [CATEGORY_TREE_PATH, TOKEN_PATH, CATEGORY_TREE_PATH]);
}

#[tokio::test]
async fn a_401_refreshes_the_user_token_keeps_the_refresh_token_and_retries() {
    let (url, log) = serve(|sent| match sent.path.as_str() {
        TOKEN_PATH => token(NEW_USER),
        _ if sent.bearer() == Some(NEW_USER.to_lowercase()) => {
            (200, r#"{"sku":"SKU-1"}"#.to_owned())
        }
        _ => unauthorized(),
    })
    .await;
    let (stored, on_token) = tokens();
    let client = keyset(&url)
        .user_token(USER)
        .refresh_token(REFRESH)
        .on_token(on_token)
        .build()
        .unwrap();
    let items = client.inventory().inventory_items();
    items.get("SKU-1").await.unwrap();
    items.get("SKU-1").await.unwrap();
    let sent = sent(&log);
    assert_eq!(sent.len(), 4, "{sent:?}");
    let form = sent[1].form();
    assert!(form.contains(&("grant_type".to_owned(), "refresh_token".to_owned())));
    assert!(form.contains(&("refresh_token".to_owned(), REFRESH.to_owned())));
    let stored = stored.lock().unwrap();
    assert_eq!(stored.len(), 1);
    assert_eq!(stored[0].access_token, NEW_USER);
    assert_eq!(stored[0].refresh_token.as_deref(), Some(REFRESH));
}

fn token_requests(log: &Log) -> Vec<String> {
    sent(log)
        .into_iter()
        .filter(|sent| sent.path == TOKEN_PATH)
        .filter_map(|sent| {
            sent.form()
                .into_iter()
                .find(|(key, _)| key == "grant_type")
                .map(|(_, grant)| grant)
        })
        .collect()
}

#[tokio::test]
async fn concurrent_first_calls_share_one_minted_token() {
    let (url, log) = serve(|sent| match sent.path.as_str() {
        TOKEN_PATH => token(MINTED),
        _ => ok(),
    })
    .await;
    let client = keyset(&url).build().unwrap();
    let trees = client.taxonomy().category_trees();
    let calls = (0..8).map(|_| trees.get("0"));
    for result in futures_util::future::join_all(calls).await {
        result.unwrap();
    }
    assert_eq!(token_requests(&log), ["client_credentials"]);
}

#[tokio::test]
async fn concurrent_401s_share_one_refresh() {
    let (url, log) = serve(|sent| match sent.path.as_str() {
        TOKEN_PATH => token(NEW_USER),
        _ if sent.bearer() == Some(NEW_USER.to_lowercase()) => {
            (200, r#"{"sku":"SKU-1"}"#.to_owned())
        }
        _ => unauthorized(),
    })
    .await;
    let client = keyset(&url)
        .user_token(USER)
        .refresh_token(REFRESH)
        .build()
        .unwrap();
    let items = client.inventory().inventory_items();
    let calls = (0..8).map(|_| items.get("SKU-1"));
    for result in futures_util::future::join_all(calls).await {
        result.unwrap();
    }
    assert_eq!(token_requests(&log), ["refresh_token"]);
}

#[tokio::test]
async fn an_app_401_and_a_user_401_at_once_each_refresh_their_own_token() {
    let (url, log) = serve(|sent| match sent.path.as_str() {
        TOKEN_PATH if sent.body.contains("client_credentials") => token(MINTED),
        TOKEN_PATH => token(NEW_USER),
        _ if sent.bearer() == Some(MINTED.to_lowercase()) => ok(),
        _ if sent.bearer() == Some(NEW_USER.to_lowercase()) => {
            (200, r#"{"sku":"SKU-1"}"#.to_owned())
        }
        _ => unauthorized(),
    })
    .await;
    let client = keyset(&url)
        .app_token(APP)
        .user_token(USER)
        .refresh_token(REFRESH)
        .build()
        .unwrap();
    let trees = client.taxonomy().category_trees();
    let items = client.inventory().inventory_items();
    let (tree, item) = tokio::join!(trees.get("0"), items.get("SKU-1"));
    tree.unwrap();
    item.unwrap();
    let mut grants = token_requests(&log);
    grants.sort();
    assert_eq!(grants, ["client_credentials", "refresh_token"]);
}

#[tokio::test]
async fn a_401_without_a_refresh_token_is_final() {
    let (url, log) = serve(|_| unauthorized()).await;
    let client = keyset(&url).user_token(USER).build().unwrap();
    let error = client
        .inventory()
        .inventory_items()
        .get("SKU-1")
        .await
        .unwrap_err();
    assert_eq!(error.kind(), ErrorKind::Authentication);
    assert_eq!(sent(&log).len(), 1);
}

#[tokio::test]
async fn exchanging_a_code_stores_the_user_token() {
    let (url, log) = serve(|sent| match sent.path.as_str() {
        TOKEN_PATH => (
            200,
            format!(r#"{{"access_token":"{USER}","refresh_token":"{REFRESH}","token_type":"User Access Token"}}"#),
        ),
        _ => (200, r#"{"sku":"SKU-1"}"#.to_owned()),
    })
    .await;
    let client = keyset(&url).ru_name("synthetic-ru-name").build().unwrap();
    let token = client
        .oauth()
        .exchange_code("synthetic-code")
        .await
        .unwrap();
    assert_eq!(token.refresh_token.as_deref(), Some(REFRESH));
    client
        .inventory()
        .inventory_items()
        .get("SKU-1")
        .await
        .unwrap();
    let sent = sent(&log);
    let form = sent[0].form();
    assert!(form.contains(&("grant_type".to_owned(), "authorization_code".to_owned())));
    assert!(form.contains(&("code".to_owned(), "synthetic-code".to_owned())));
    assert!(form.contains(&("redirect_uri".to_owned(), "synthetic-ru-name".to_owned())));
    assert_eq!(sent[1].bearer(), Some(USER.to_lowercase()));
}

#[tokio::test]
async fn each_host_has_its_own_base_url() {
    let (url, log) = serve(|_| (200, r#"{"payouts":[]}"#.to_owned())).await;
    let client = Client::builder()
        .user_token(USER)
        .hosts([
            ("api", format!("{url}/api")),
            ("apiz", format!("{url}/apiz")),
            ("apim", format!("{url}/apim")),
        ])
        .build()
        .unwrap();
    let params = PayoutsListParams::default();
    client.finances().payouts().list(&params).await.unwrap();
    assert_eq!(sent(&log)[0].path, format!("/apiz{PAYOUTS_PATH}"));
}

#[test]
fn the_sandbox_has_its_own_hosts_and_authorization_url() {
    let client = Client::builder()
        .client_id(CLIENT_ID)
        .client_secret(CLIENT_SECRET)
        .ru_name("synthetic-ru-name")
        .environment("sandbox")
        .build()
        .unwrap();
    let request = client
        .oauth()
        .authorization_url(&[API_SCOPE], None, None)
        .unwrap();
    assert!(
        request
            .url
            .starts_with("https://auth.sandbox.ebay.com/oauth2/authorize?"),
        "{}",
        request.url
    );
    assert!(!request.state.is_empty());
    let sandbox = ebay_sell::ENVIRONMENTS
        .iter()
        .find(|(name, _)| *name == "sandbox")
        .unwrap();
    assert!(sandbox.1.contains(&("api", "https://api.sandbox.ebay.com")));
    assert!(
        Client::builder()
            .user_token(USER)
            .environment("staging")
            .build()
            .is_err()
    );
}

#[tokio::test]
async fn the_marketplace_is_a_default_each_call_may_override() {
    let (url, log) = serve(|_| (200, r#"{"payouts":[]}"#.to_owned())).await;
    let client = builder(&url)
        .user_token(USER)
        .marketplace_id("EBAY_GB")
        .build()
        .unwrap();
    let payouts = client.finances().payouts();
    payouts.list(&PayoutsListParams::default()).await.unwrap();
    let params = PayoutsListParams {
        x_ebay_c_marketplace_id: Some("EBAY_DE".to_owned()),
        ..PayoutsListParams::default()
    };
    payouts.list(&params).await.unwrap();
    let marketplaces: Vec<Option<String>> = sent(&log)
        .iter()
        .map(|sent| sent.header("x-ebay-c-marketplace-id"))
        .collect();
    assert_eq!(
        marketplaces,
        [Some("ebay_gb".to_owned()), Some("ebay_de".to_owned())]
    );
}

#[tokio::test]
async fn a_post_order_upload_sends_the_user_token_marketplace_and_a_json_file() {
    use ebay_sell::post_order::ReturnsUploadFileParams;
    use ebay_sell::post_order::models::{FilePurposeEnum, UploadFileRequest};

    let (url, log) = serve(|_| (200, r#"{"fileId":"1"}"#.to_owned())).await;
    let client = builder(&url)
        .user_token(USER)
        .marketplace_id("EBAY_GB")
        .build()
        .unwrap();
    let file = UploadFileRequest {
        data: Some("c3ludGhldGlj".to_owned()),
        file_purpose: Some(FilePurposeEnum::LabelRelated),
        ..UploadFileRequest::default()
    };
    client
        .post_order()
        .returns()
        .upload_file("5000000001", &file, &ReturnsUploadFileParams::default())
        .await
        .unwrap();
    let sent = sent(&log);
    assert_eq!(sent[0].path, "/post-order/v2/return/5000000001/file/upload");
    assert_eq!(sent[0].bearer(), Some(USER.to_lowercase()));
    assert_eq!(
        sent[0].header("x-ebay-c-marketplace-id").as_deref(),
        Some("ebay_gb")
    );
    assert_eq!(
        sent[0].header("content-type").as_deref(),
        Some("application/json")
    );
    let body: serde_json::Value = serde_json::from_str(&sent[0].body).unwrap();
    assert_eq!(
        body,
        serde_json::json!({"data": "c3ludGhldGlj", "filePurpose": "LABEL_RELATED"})
    );
}

#[tokio::test]
async fn an_empty_204_is_none() {
    let (url, _) = serve(|_| (204, String::new())).await;
    let client = builder(&url).user_token(USER).build().unwrap();
    let items = client.inventory().inventory_items();
    items.delete("SKU-1").await.unwrap();
    let item = ebay_sell::inventory::models::InventoryItem::default();
    let params = ebay_sell::inventory::InventoryItemsCreateOrReplaceParams::default();
    let created = items
        .create_or_replace("SKU-1", &item, &params)
        .await
        .unwrap();
    assert_eq!(created, None);
}

#[tokio::test]
async fn iterators_follow_the_next_link() {
    let (url, log) = serve(|sent| match sent.query.contains("offset=1") {
        false => (
            200,
            r#"{"payouts":[{"payoutId":"P-1"}],"next":"https://apiz.ebay.com/sell/finances/v1/payout?limit=1&offset=1"}"#.to_owned(),
        ),
        true => (200, r#"{"payouts":[{"payoutId":"P-2"}]}"#.to_owned()),
    })
    .await;
    let client = builder(&url).user_token(USER).build().unwrap();
    let params = PayoutsListParams {
        limit: Some("1".to_owned()),
        ..PayoutsListParams::default()
    };
    let payouts: Vec<_> = client
        .finances()
        .payouts()
        .iter(&params)
        .try_collect()
        .await
        .unwrap();
    let ids: Vec<_> = payouts
        .iter()
        .map(|payout| payout.payout_id.as_deref())
        .collect();
    assert_eq!(ids, [Some("P-1"), Some("P-2")]);
    let sent = sent(&log);
    assert_eq!(sent.len(), 2);
    assert!(sent.iter().all(|sent| sent.path == PAYOUTS_PATH));
    assert!(sent[1].query.contains("limit=1"), "{:?}", sent[1].query);
}

#[tokio::test]
async fn ebay_errors_are_typed() {
    let body = r#"{"errors":[{"errorId":25001,"domain":"API_INVENTORY","subdomain":"Selling","category":"REQUEST","message":"A synthetic failure.","longMessage":"A longer synthetic failure.","parameters":[{"name":"sku","value":"SKU-1"}]},{"errorId":25002,"message":"Another."}]}"#;
    let (url, _) = serve(move |_| (400, body.to_owned())).await;
    let client = builder(&url).user_token(USER).build().unwrap();
    let error = client
        .inventory()
        .inventory_items()
        .get("SKU-1")
        .await
        .unwrap_err();
    assert_eq!(error.kind(), ErrorKind::BadRequest);
    assert_eq!(error.status(), Some(400));
    assert_eq!(error.code(), Some("25001"));
    assert_eq!(error.detail(), Some("A synthetic failure."));
    let details = error_details(&error);
    assert_eq!(details.len(), 2);
    let first = &details[0];
    assert_eq!(first.error_id, Some(25001));
    assert_eq!(first.domain.as_deref(), Some("API_INVENTORY"));
    assert_eq!(first.category.as_deref(), Some("REQUEST"));
    assert_eq!(
        first.long_message.as_deref(),
        Some("A longer synthetic failure.")
    );
    assert_eq!(first.parameters[0].name.as_deref(), Some("sku"));
    assert_eq!(first.parameters[0].value.as_deref(), Some("SKU-1"));
    assert_eq!(details[1].error_id, Some(25002));
}

#[tokio::test]
async fn tokens_and_secrets_are_kept_out_of_errors_and_debug_output() {
    let (url, _) = serve(|sent| match sent.path.as_str() {
        TOKEN_PATH => token(MINTED),
        _ => (
            400,
            format!(r#"{{"errors":[{{"message":"{CLIENT_SECRET} {MINTED} {USER} {REFRESH}"}}]}}"#),
        ),
    })
    .await;
    let client = keyset(&url)
        .user_token(USER)
        .refresh_token(REFRESH)
        .build()
        .unwrap();
    let error = client
        .taxonomy()
        .category_trees()
        .get("0")
        .await
        .unwrap_err();
    let output = format!(
        "{error} {error:?} {:?} {:?} {client:?}",
        error.detail(),
        error.raw_body()
    );
    for secret in [CLIENT_SECRET, MINTED, USER, REFRESH] {
        assert!(!output.contains(secret), "{secret} in {output}");
    }
}

#[cfg(feature = "signing")]
mod signing {
    use aws_lc_rs::rand::SystemRandom;
    use aws_lc_rs::signature::Ed25519KeyPair;
    use ebay_sell::SigningKey;

    use super::*;

    const JWE: &str = "synthetic.jwe.value";

    fn signing_key() -> SigningKey {
        let document = Ed25519KeyPair::generate_pkcs8(&SystemRandom::new()).unwrap();
        SigningKey::new(STANDARD.encode(document.as_ref()), JWE)
    }

    #[tokio::test]
    async fn signed_calls_carry_the_key_digest_and_signature() {
        let (url, log) = serve(|sent| match sent.path.as_str() {
            TOKEN_PATH => token(MINTED),
            _ => (204, String::new()),
        })
        .await;
        let client = keyset(&url)
            .user_token(USER)
            .signing_key(signing_key())
            .build()
            .unwrap();
        let item = ebay_sell::inventory::models::InventoryItem::default();
        let params = ebay_sell::inventory::InventoryItemsCreateOrReplaceParams::default();
        client
            .inventory()
            .inventory_items()
            .create_or_replace("SKU-1", &item, &params)
            .await
            .unwrap();
        client.taxonomy().category_trees().get("0").await.unwrap();
        let sent = sent(&log);
        let put = &sent[0];
        assert_eq!(put.header("x-ebay-signature-key"), Some(JWE.to_lowercase()));
        assert!(put.header("content-digest").is_some(), "{}", put.head);
        assert!(put.header("signature").is_some(), "{}", put.head);
        let input = put.header("signature-input").unwrap();
        assert!(
            input.contains(
                r#"("content-digest" "x-ebay-signature-key" "@method" "@path" "@authority")"#
            ),
            "{input}"
        );
        let mint = sent.iter().find(|sent| sent.path == TOKEN_PATH).unwrap();
        assert!(mint.header("signature").is_none(), "{}", mint.head);
        let get = sent
            .iter()
            .find(|sent| sent.path == CATEGORY_TREE_PATH)
            .unwrap();
        let input = get.header("signature-input").unwrap();
        assert!(!input.contains("content-digest"), "{input}");
    }

    #[test]
    fn an_unreadable_key_fails_the_build() {
        let key = SigningKey::new("not a key", JWE);
        assert!(
            Client::builder()
                .user_token(USER)
                .signing_key(key)
                .build()
                .is_err()
        );
    }
}
