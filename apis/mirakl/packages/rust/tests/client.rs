use std::sync::{Arc, Mutex};
use std::time::Duration;

use futures_util::TryStreamExt;
use mirakl_seller::models::{Or13Request, Or14Response200};
use mirakl_seller::{
    AccountGetParams, Client, ClientBuilder, ErrorKind, File, OffersGetImportParams,
    OrdersListParams, OrdersStartExportParams, StockStartImportParams, WaitOptions,
};
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use tokio::net::TcpListener;

const KEY: &str = "00000000-0000-4000-8000-5e11e4000001";

struct Reply {
    status: u16,
    headers: Vec<(&'static str, String)>,
    body: Vec<u8>,
}

fn json(status: u16, body: &str) -> Reply {
    Reply {
        status,
        headers: vec![("content-type", "application/json".into())],
        body: body.into(),
    }
}

/// A request as received: the head lowercased, and the body.
#[derive(Clone)]
struct Sent {
    head: String,
    body: Vec<u8>,
}

impl Sent {
    fn line(&self, name: &str) -> Option<&str> {
        self.head
            .lines()
            .find_map(|line| line.strip_prefix(&format!("{name}: ")))
    }
}

type Log = Arc<Mutex<Vec<Sent>>>;

/// Serves one reply per connection, picked by the number of requests so far, and keeps each request.
async fn serve(reply: impl Fn(usize) -> Reply + Send + 'static) -> (String, Log) {
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
            let head = String::from_utf8_lossy(&data[..head_end]).to_lowercase();
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
            let number = {
                let mut log = kept.lock().unwrap();
                log.push(Sent {
                    head,
                    body: data[head_end..].to_vec(),
                });
                log.len() - 1
            };
            let Reply {
                status,
                headers,
                body,
            } = reply(number);
            let mut response = format!(
                "HTTP/1.1 {status} Status\r\ncontent-length: {}\r\nconnection: close\r\n",
                body.len()
            );
            for (name, value) in headers {
                response.push_str(&format!("{name}: {value}\r\n"));
            }
            response.push_str("\r\n");
            let _ = stream.write_all(response.as_bytes()).await;
            let _ = stream.write_all(&body).await;
            let _ = stream.shutdown().await;
        }
    });
    (url, log)
}

fn builder(url: &str) -> ClientBuilder {
    Client::builder()
        .base_url(url)
        .api_key(KEY)
        .retry_base_delay(Duration::ZERO)
}

fn sent(log: &Log) -> Vec<Sent> {
    log.lock().unwrap().clone()
}

fn fast() -> WaitOptions {
    WaitOptions {
        interval: Duration::ZERO,
        timeout: Duration::from_secs(5),
    }
}

#[tokio::test]
async fn the_key_is_the_whole_authorization_header_with_json_accepted() {
    let (url, log) = serve(|_| json(200, r#"{"shop_id": 2001}"#)).await;
    let client = builder(&url).user_agent("example/1.0").build().unwrap();
    let shop = client
        .account()
        .get(&AccountGetParams::default())
        .await
        .unwrap();
    assert_eq!(shop.shop_id, Some(2001));
    let request = &sent(&log)[0];
    assert!(
        request.head.starts_with("get /api/account "),
        "{}",
        request.head
    );
    assert_eq!(request.line("authorization"), Some(KEY));
    assert_eq!(request.line("accept"), Some("application/json"));
    assert_eq!(request.line("user-agent"), Some("example/1.0"));
}

#[tokio::test]
async fn the_shop_id_default_is_sent_unless_the_call_sets_its_own() {
    let (url, log) = serve(|_| json(200, "{}")).await;
    let client = builder(&url).shop_id(2001).build().unwrap();
    let account = client.account();
    account.get(&AccountGetParams::default()).await.unwrap();
    let own = AccountGetParams {
        shop_id: Some(2002),
    };
    account.get(&own).await.unwrap();
    builder(&url)
        .build()
        .unwrap()
        .account()
        .get(&AccountGetParams::default())
        .await
        .unwrap();
    let sent = sent(&log);
    assert!(
        sent[0].head.starts_with("get /api/account?shop_id=2001 "),
        "{}",
        sent[0].head
    );
    assert!(
        sent[1].head.starts_with("get /api/account?shop_id=2002 "),
        "{}",
        sent[1].head
    );
    assert!(
        sent[2].head.starts_with("get /api/account "),
        "{}",
        sent[2].head
    );
}

#[tokio::test]
async fn offset_iteration_keeps_the_shop_id_and_stops_at_the_total() {
    let (url, log) = serve(|number| {
        let id = number + 1;
        json(
            200,
            &format!(r#"{{"orders": [{{"order_id": "order-{id}"}}], "total_count": 2}}"#),
        )
    })
    .await;
    let client = builder(&url).shop_id(2001).build().unwrap();
    let params = OrdersListParams {
        max: Some(1),
        ..Default::default()
    };
    let orders: Vec<_> = client.orders().iter(&params).try_collect().await.unwrap();
    let ids: Vec<_> = orders.iter().map(|order| order.order_id.clone()).collect();
    assert_eq!(
        ids,
        [Some("order-1".to_owned()), Some("order-2".to_owned())]
    );
    let sent = sent(&log);
    assert_eq!(sent.len(), 2);
    for request in &sent {
        assert!(request.head.contains("shop_id=2001"), "{}", request.head);
    }
    assert!(sent[1].head.contains("offset=1"), "{}", sent[1].head);
}

#[tokio::test]
async fn a_wait_polls_until_the_job_ends_with_the_shop_id() {
    let (url, log) = serve(|number| {
        let status = if number < 2 { "RUNNING" } else { "COMPLETE" };
        json(
            200,
            &format!(r#"{{"import_id": 41, "status": "{status}"}}"#),
        )
    })
    .await;
    let client = builder(&url).shop_id(2001).build().unwrap();
    let status = client.offers().wait_for_import(41, fast()).await.unwrap();
    assert_eq!(status.status.as_deref(), Some("COMPLETE"));
    let sent = sent(&log);
    assert_eq!(sent.len(), 3);
    for request in &sent {
        assert!(
            request
                .head
                .starts_with("get /api/offers/imports/41?shop_id=2001 "),
            "{}",
            request.head
        );
    }
}

#[tokio::test]
async fn a_failed_job_returns_its_status() {
    let (url, _) = serve(|_| json(200, r#"{"status": "FAILED", "has_error_report": true}"#)).await;
    let client = builder(&url).build().unwrap();
    let status = client.offers().wait_for_import(41, fast()).await.unwrap();
    assert_eq!(status.has_error_report, Some(true));
}

#[tokio::test]
async fn a_wait_past_its_deadline_is_a_job_timeout_with_the_last_status() {
    let (url, log) = serve(|_| json(200, r#"{"status": "PENDING"}"#)).await;
    let client = builder(&url).build().unwrap();
    let options = WaitOptions {
        interval: Duration::from_millis(5),
        timeout: Duration::ZERO,
    };
    let error = client
        .orders()
        .wait_for_export("tracking-9", options)
        .await
        .unwrap_err();
    assert_eq!(error.kind(), ErrorKind::JobTimeout);
    let last: &Or14Response200 = error.job_status().unwrap();
    assert_eq!(last.status.as_deref(), Some("PENDING"));
    assert_eq!(sent(&log).len(), 1);
}

#[tokio::test]
async fn a_url_download_sends_the_key_only_to_the_base_url_origin() {
    let (other, other_log) = serve(|_| Reply {
        status: 200,
        headers: vec![("content-type", "application/json".into())],
        body: b"[]".to_vec(),
    })
    .await;
    let (url, log) = serve(|_| json(200, "[]")).await;
    let client = builder(&url).build().unwrap();
    let file = client
        .download_url(&format!("{url}/exports/1.json"))
        .await
        .unwrap();
    assert_eq!(file.bytes().await.unwrap(), b"[]");
    let file = client
        .download_url(&format!("{other}/exports/2.json?signature=synthetic"))
        .await
        .unwrap();
    assert_eq!(file.content_type(), "application/json");
    assert_eq!(sent(&log)[0].line("authorization"), Some(KEY));
    let foreign = &sent(&other_log)[0];
    assert!(
        foreign
            .head
            .starts_with("get /exports/2.json?signature=synthetic "),
        "{}",
        foreign.head
    );
    assert_eq!(foreign.line("authorization"), None);
}

#[tokio::test]
async fn a_write_is_not_retried_after_a_server_error() {
    let (url, log) = serve(|_| json(503, "unavailable")).await;
    let client = builder(&url).build().unwrap();
    let request = Or13Request::default();
    let error = client
        .orders()
        .start_export(&request, &OrdersStartExportParams::default())
        .await
        .unwrap_err();
    assert_eq!(error.kind(), ErrorKind::Server);
    assert_eq!(sent(&log).len(), 1);
}

#[tokio::test]
async fn a_get_is_retried_after_a_server_error() {
    let (url, log) = serve(|number| {
        if number == 0 {
            json(503, "unavailable")
        } else {
            json(200, r#"{"import_id": 41}"#)
        }
    })
    .await;
    let client = builder(&url).build().unwrap();
    client
        .offers()
        .get_import(41, &OffersGetImportParams::default())
        .await
        .unwrap();
    assert_eq!(sent(&log).len(), 2);
}

#[tokio::test]
async fn an_error_keeps_the_raw_body_without_the_key() {
    let body = format!("key {KEY} was refused");
    let (url, _) = serve(move |_| json(401, &body)).await;
    let client = builder(&url).build().unwrap();
    let error = client
        .account()
        .get(&AccountGetParams::default())
        .await
        .unwrap_err();
    assert_eq!(error.kind(), ErrorKind::Authentication);
    assert_eq!(error.status(), Some(401));
    let raw = error.raw_body().unwrap();
    assert!(!raw.contains(KEY), "{raw}");
    assert!(raw.ends_with("was refused"), "{raw}");
}

#[tokio::test]
async fn redirects_are_not_followed() {
    let (foreign, foreign_log) = serve(|_| json(200, "{}")).await;
    let location = format!("{foreign}/api/account");
    let (url, log) = serve(move |_| Reply {
        status: 302,
        headers: vec![("location", location.clone())],
        body: Vec::new(),
    })
    .await;
    let client = builder(&url).build().unwrap();
    let error = client
        .account()
        .get(&AccountGetParams::default())
        .await
        .unwrap_err();
    assert_eq!(error.kind(), ErrorKind::Api);
    assert_eq!(error.status(), Some(302));
    assert_eq!(sent(&log).len(), 1);
    assert!(sent(&foreign_log).is_empty());
}

#[tokio::test]
async fn an_import_sends_its_file_as_a_multipart_part() {
    let (url, log) = serve(|_| json(201, r#"{"import_id": "stock-import-1"}"#)).await;
    let client = builder(&url).build().unwrap();
    let params = StockStartImportParams {
        file: Some(File::new("stock.csv", "offer-sku;quantity\nsku-1;5\n")),
        ..Default::default()
    };
    let started = client.stock().start_import(&params).await.unwrap();
    assert_eq!(started.import_id.as_deref(), Some("stock-import-1"));
    let request = &sent(&log)[0];
    assert!(
        request
            .line("content-type")
            .is_some_and(|value| value.starts_with("multipart/form-data; boundary=")),
        "{}",
        request.head
    );
    let body = String::from_utf8_lossy(&request.body);
    assert!(
        body.contains(r#"name="file"; filename="stock.csv""#),
        "{body}"
    );
    assert!(body.contains("sku-1;5"), "{body}");
}
