use std::sync::{Arc, Mutex};

use etsy_seller::{
    Client, ClientBuilder, ErrorKind, File, ListingImagesUploadParams, ListingsCreateDraftParams,
    ListingsListActiveParams, ReceiptsUpdateParams, Token,
};
use futures_util::TryStreamExt;
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use tokio::net::TcpListener;

const KEY: &str = "synthetic-keystring";
const SECRET: &str = "synthetic-shared-secret";
const ACCESS: &str = "12345678.synthetic-access";
const REFRESH: &str = "12345678.synthetic-refresh";
const NEW_ACCESS: &str = "12345678.synthetic-access-2";
const NEW_REFRESH: &str = "12345678.synthetic-refresh-2";
const TOKEN_PATH: &str = "/v3/public/oauth/token";

/// One request as the server read it. `head` is lowercased.
#[derive(Clone, Debug)]
struct Sent {
    path: String,
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
}

type Log = Arc<Mutex<Vec<Sent>>>;

/// Serves one JSON reply per connection, picked by the request.
async fn serve(reply: impl Fn(&Sent) -> (u16, String) + Send + 'static) -> (String, Log) {
    let listener = TcpListener::bind("127.0.0.1:0").await.unwrap();
    let url = format!("http://{}", listener.local_addr().unwrap());
    let log = Log::default();
    let kept = Arc::clone(&log);
    tokio::spawn(async move {
        loop {
            let Ok((mut stream, _)) = listener.accept().await else {
                return;
            };
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
            let path = target.split('?').next().unwrap_or_default().to_owned();
            let sent = Sent {
                path,
                head,
                body: String::from_utf8_lossy(&data[head_end..]).into_owned(),
            };
            kept.lock().unwrap().push(sent.clone());
            let (status, body) = reply(&sent);
            let response = format!(
                "HTTP/1.1 {status} Status\r\ncontent-type: application/json\r\ncontent-length: {}\r\nconnection: close\r\n\r\n{body}",
                body.len()
            );
            let _ = stream.write_all(response.as_bytes()).await;
            let _ = stream.shutdown().await;
        }
    });
    (url, log)
}

fn builder(url: &str) -> ClientBuilder {
    Client::builder()
        .api_key(KEY)
        .shared_secret(SECRET)
        .base_url(url)
        .retry_base_delay(std::time::Duration::ZERO)
}

fn new_token() -> (u16, String) {
    let body = format!(
        r#"{{"access_token":"{NEW_ACCESS}","refresh_token":"{NEW_REFRESH}","expires_in":3600,"token_type":"Bearer"}}"#
    );
    (200, body)
}

/// Answers 401 until the access token is the refreshed one.
fn expiring(sent: &Sent) -> (u16, String) {
    if sent.path == TOKEN_PATH {
        return new_token();
    }
    if sent.header("authorization") != Some(format!("bearer {NEW_ACCESS}").to_lowercase()) {
        return (401, r#"{"error":"invalid_token"}"#.to_owned());
    }
    (200, r#"{"user_id":12345678,"shop_id":1}"#.to_owned())
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
async fn key_only_operations_send_no_access_token() {
    let (url, log) = serve(|_| (200, r#"{"application_id":1}"#.to_owned())).await;
    let client = builder(&url).access_token(ACCESS).build().unwrap();
    let ping = client.application().ping().await.unwrap();
    assert_eq!(ping.application_id, Some(1));
    let sent = &log.lock().unwrap()[0];
    assert_eq!(sent.header("x-api-key"), Some(format!("{KEY}:{SECRET}")));
    assert_eq!(sent.header("authorization"), None);
}

#[tokio::test]
async fn oauth_operations_send_both_headers() {
    let (url, log) = serve(|_| (200, r#"{"user_id":12345678,"shop_id":1}"#.to_owned())).await;
    let me = builder(&url)
        .access_token(ACCESS)
        .build()
        .unwrap()
        .users()
        .get_me()
        .await
        .unwrap();
    assert_eq!(me.shop_id, Some(1));
    let sent = &log.lock().unwrap()[0];
    assert_eq!(sent.header("x-api-key"), Some(format!("{KEY}:{SECRET}")));
    assert_eq!(
        sent.header("authorization"),
        Some(format!("bearer {ACCESS}"))
    );
}

#[tokio::test]
async fn form_bodies_are_url_encoded_with_repeated_fields() {
    let (url, log) = serve(|_| (201, r#"{"listing_id":1}"#.to_owned())).await;
    let client = builder(&url).access_token(ACCESS).build().unwrap();
    let params = ListingsCreateDraftParams {
        quantity: Some(1),
        title: Some("Synthetic & listing".into()),
        price: Some(1.5),
        tags: Some(vec!["a".into(), "b".into()]),
        ..Default::default()
    };
    let listing = client.listings().create_draft(1, &params).await.unwrap();
    assert_eq!(listing.listing_id, Some(1));
    let sent = &log.lock().unwrap()[0];
    assert_eq!(sent.path, "/v3/application/shops/1/listings");
    assert_eq!(
        sent.header("content-type").as_deref(),
        Some("application/x-www-form-urlencoded")
    );
    let pairs = [
        ("quantity", "1"),
        ("title", "Synthetic & listing"),
        ("price", "1.5"),
        ("tags", "a"),
        ("tags", "b"),
    ];
    let expected: Vec<(String, String)> = pairs
        .iter()
        .map(|(name, value)| ((*name).to_owned(), (*value).to_owned()))
        .collect();
    assert_eq!(sent.form(), expected);
}

#[tokio::test]
async fn query_parameters_and_form_fields_share_one_params_struct() {
    let (url, log) = serve(|_| (200, r#"{"receipt_id":2}"#.to_owned())).await;
    let client = builder(&url).access_token(ACCESS).build().unwrap();
    let params = ReceiptsUpdateParams {
        legacy: Some(false),
        was_shipped: Some(true),
        ..Default::default()
    };
    client.receipts().update(1, 2, &params).await.unwrap();
    let sent = &log.lock().unwrap()[0];
    assert!(
        sent.head
            .starts_with("put /v3/application/shops/1/receipts/2?legacy=false "),
        "{}",
        sent.head
    );
    assert_eq!(sent.body, "was_shipped=true");
}

#[tokio::test]
async fn uploads_are_multipart() {
    let (url, log) = serve(|_| (201, r#"{"listing_image_id":1}"#.to_owned())).await;
    let client = builder(&url).access_token(ACCESS).build().unwrap();
    let params = ListingImagesUploadParams {
        image: Some(File::new("a.png", b"synthetic-png".to_vec())),
        rank: Some(1),
        ..Default::default()
    };
    client.listing_images().upload(1, 2, &params).await.unwrap();
    let sent = &log.lock().unwrap()[0];
    assert!(
        sent.header("content-type")
            .unwrap()
            .starts_with("multipart/form-data; boundary=")
    );
    assert!(sent.body.contains("synthetic-png"));
    assert!(sent.body.contains("filename=\"a.png\""));
}

#[tokio::test]
async fn iterators_advance_the_offset_until_the_count() {
    let (url, log) = serve(|sent| match sent.head.contains("offset=2") {
        false => (
            200,
            r#"{"count":3,"results":[{"listing_id":1},{"listing_id":2}]}"#.to_owned(),
        ),
        true => (
            200,
            r#"{"count":3,"results":[{"listing_id":3}]}"#.to_owned(),
        ),
    })
    .await;
    let client = builder(&url).build().unwrap();
    let params = ListingsListActiveParams {
        limit: Some(2),
        ..Default::default()
    };
    let listings: Vec<_> = client
        .listings()
        .iter_active(&params)
        .try_collect()
        .await
        .unwrap();
    let ids: Vec<_> = listings.iter().map(|listing| listing.listing_id).collect();
    assert_eq!(ids, [Some(1), Some(2), Some(3)]);
    assert_eq!(log.lock().unwrap().len(), 2);
}

#[tokio::test]
async fn a_401_refreshes_once_hands_over_the_token_and_retries() {
    let (url, log) = serve(expiring).await;
    let (stored, on_token) = tokens();
    let client = builder(&url)
        .access_token(ACCESS)
        .refresh_token(REFRESH)
        .on_token(on_token)
        .build()
        .unwrap();
    let me = client.users().get_me().await.unwrap();
    assert_eq!(me.user_id, Some(12345678));

    let sent = log.lock().unwrap().clone();
    let paths: Vec<&str> = sent.iter().map(|sent| sent.path.as_str()).collect();
    assert_eq!(
        paths,
        [
            "/v3/application/users/me",
            TOKEN_PATH,
            "/v3/application/users/me"
        ]
    );
    let refresh = &sent[1];
    let pairs = [
        ("grant_type", "refresh_token"),
        ("client_id", KEY),
        ("refresh_token", REFRESH),
    ];
    let expected: Vec<(String, String)> = pairs
        .iter()
        .map(|(name, value)| ((*name).to_owned(), (*value).to_owned()))
        .collect();
    assert_eq!(refresh.form(), expected);
    assert_eq!(refresh.header("authorization"), None);

    let stored = stored.lock().unwrap();
    assert_eq!(stored.len(), 1);
    assert_eq!(
        (
            stored[0].access_token.as_str(),
            stored[0].refresh_token.as_str()
        ),
        (NEW_ACCESS, NEW_REFRESH)
    );
    assert_eq!(stored[0].expires_in, Some(3600));
}

#[tokio::test]
async fn concurrent_calls_share_one_refresh() {
    let (url, log) = serve(expiring).await;
    let client = builder(&url)
        .access_token(ACCESS)
        .refresh_token(REFRESH)
        .build()
        .unwrap();
    let users = client.users();
    let calls = (0..4).map(|_| users.get_me());
    for result in futures_util::future::join_all(calls).await {
        result.unwrap();
    }
    let refreshes = log
        .lock()
        .unwrap()
        .iter()
        .filter(|sent| sent.path == TOKEN_PATH)
        .count();
    assert_eq!(refreshes, 1);
}

#[tokio::test]
async fn an_explicit_refresh_and_a_401_share_one_token_request() {
    let (url, log) = serve(expiring).await;
    let (stored, on_token) = tokens();
    let client = builder(&url)
        .access_token(ACCESS)
        .refresh_token(REFRESH)
        .on_token(on_token)
        .build()
        .unwrap();
    let oauth = client.oauth();
    let users = client.users();
    let (token, me) = tokio::join!(oauth.refresh(), users.get_me());
    assert_eq!(token.unwrap().access_token, NEW_ACCESS);
    assert_eq!(me.unwrap().shop_id, Some(1));
    let refreshed: Vec<String> = log
        .lock()
        .unwrap()
        .iter()
        .filter(|sent| sent.path == TOKEN_PATH)
        .flat_map(Sent::form)
        .filter(|(name, _)| name == "refresh_token")
        .map(|(_, value)| value)
        .collect();
    assert_eq!(refreshed, [REFRESH]);
    assert_eq!(stored.lock().unwrap().len(), 1);
}

#[tokio::test]
async fn a_401_without_a_refresh_token_is_final() {
    let (url, log) = serve(expiring).await;
    let error = builder(&url)
        .access_token(ACCESS)
        .build()
        .unwrap()
        .users()
        .get_me()
        .await
        .unwrap_err();
    assert_eq!(error.kind(), ErrorKind::Authentication);
    assert_eq!(error.detail(), Some("invalid_token"));
    assert_eq!(log.lock().unwrap().len(), 1);
}

#[tokio::test]
async fn a_401_on_a_key_only_operation_never_refreshes() {
    let (url, log) = serve(|_| (401, r#"{"error":"invalid_api_key"}"#.to_owned())).await;
    let client = builder(&url)
        .access_token(ACCESS)
        .refresh_token(REFRESH)
        .build()
        .unwrap();
    let error = client.application().ping().await.unwrap_err();
    assert_eq!(error.kind(), ErrorKind::Authentication);
    assert_eq!(log.lock().unwrap().len(), 1);
}

#[tokio::test]
async fn a_failed_refresh_fails_the_call_once() {
    let (url, log) = serve(|sent| match sent.path == TOKEN_PATH {
        true => (400, r#"{"error":"invalid_grant"}"#.to_owned()),
        false => (401, r#"{"error":"invalid_token"}"#.to_owned()),
    })
    .await;
    let client = builder(&url)
        .access_token(ACCESS)
        .refresh_token(REFRESH)
        .build()
        .unwrap();
    let error = client.users().get_me().await.unwrap_err();
    assert_eq!(error.kind(), ErrorKind::BadRequest);
    assert_eq!(error.detail(), Some("invalid_grant"));
    assert_eq!(log.lock().unwrap().len(), 2);
}

#[tokio::test]
async fn exchanging_a_code_stores_the_token_for_later_calls() {
    let (url, log) = serve(|sent| match sent.path == TOKEN_PATH {
        true => new_token(),
        false => (200, r#"{"user_id":12345678,"shop_id":1}"#.to_owned()),
    })
    .await;
    let (stored, on_token) = tokens();
    let client = builder(&url).on_token(on_token).build().unwrap();
    let verifier = "synthetic-verifier-synthetic-verifier-synthetic";
    let token = client
        .oauth()
        .exchange_code("synthetic-code", verifier, "https://example.test/back")
        .await
        .unwrap();
    assert_eq!(token.user_id(), Some(12345678));
    client.users().get_me().await.unwrap();

    let sent = log.lock().unwrap().clone();
    let pairs = [
        ("grant_type", "authorization_code"),
        ("client_id", KEY),
        ("redirect_uri", "https://example.test/back"),
        ("code", "synthetic-code"),
        ("code_verifier", verifier),
    ];
    let expected: Vec<(String, String)> = pairs
        .iter()
        .map(|(name, value)| ((*name).to_owned(), (*value).to_owned()))
        .collect();
    assert_eq!(sent[0].form(), expected);
    assert_eq!(
        sent[1].header("authorization"),
        Some(format!("bearer {NEW_ACCESS}"))
    );
    assert_eq!(stored.lock().unwrap().len(), 1);
}

#[tokio::test]
async fn an_explicit_refresh_needs_a_refresh_token() {
    let client = builder("http://127.0.0.1:9").build().unwrap();
    assert_eq!(
        client.oauth().refresh().await.unwrap_err().kind(),
        ErrorKind::InvalidInput
    );
}

#[tokio::test]
async fn a_token_response_without_tokens_is_a_decode_error() {
    let (url, _) = serve(|_| (200, r#"{"access_token":"only-one"}"#.to_owned())).await;
    let client = builder(&url).refresh_token(REFRESH).build().unwrap();
    assert_eq!(
        client.oauth().refresh().await.unwrap_err().kind(),
        ErrorKind::Decode
    );
}

#[tokio::test]
async fn new_tokens_and_codes_are_kept_out_of_errors() {
    let (url, _) = serve(|sent| match sent.path == TOKEN_PATH {
        true => new_token(),
        false => (
            400,
            format!(r#"{{"error":"{SECRET} {NEW_ACCESS} {NEW_REFRESH} synthetic-code"}}"#),
        ),
    })
    .await;
    let client = builder(&url).build().unwrap();
    let verifier = "synthetic-verifier-synthetic-verifier-synthetic";
    client
        .oauth()
        .exchange_code("synthetic-code", verifier, "https://example.test/back")
        .await
        .unwrap();
    let error = client.users().get_me().await.unwrap_err();
    let output = format!(
        "{error} {error:?} {:?} {:?}",
        error.detail(),
        error.raw_body()
    );
    for secret in [KEY, SECRET, NEW_ACCESS, NEW_REFRESH, "synthetic-code"] {
        assert!(!output.contains(secret), "{secret} in {output}");
    }
}
