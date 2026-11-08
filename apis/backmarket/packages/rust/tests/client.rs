use std::sync::atomic::{AtomicUsize, Ordering};
use std::sync::{Arc, Mutex};
use std::time::{Duration, Instant};

use backmarket_seller::models::{
    Competitor, MarketCode, Order, PostItemTransferCreateRequest, UpdateOrder,
};
use backmarket_seller::{Client, ClientBuilder, Error, ErrorKind, OrdersListParams};
use futures_util::StreamExt;
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use tokio::net::TcpListener;

const TOKEN: &str = "synthetic-token";

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

fn rate_limited(retry_after: &str) -> Reply {
    Reply {
        status: 429,
        headers: vec![("retry-after", retry_after.into())],
        body: Vec::new(),
    }
}

type Heads = Arc<Mutex<Vec<String>>>;

/// Serves one reply per connection, picked by the number of requests so far, and counts requests.
async fn serve(reply: impl Fn(usize) -> Reply + Send + 'static) -> (String, Arc<AtomicUsize>) {
    let (url, count, _) = record(reply).await;
    (url, count)
}

/// Serves like [`serve`], and also keeps each request's head, lowercased.
async fn record(
    reply: impl Fn(usize) -> Reply + Send + 'static,
) -> (String, Arc<AtomicUsize>, Heads) {
    let listener = TcpListener::bind("127.0.0.1:0").await.unwrap();
    let url = format!("http://{}", listener.local_addr().unwrap());
    let count = Arc::new(AtomicUsize::new(0));
    let seen = Arc::clone(&count);
    let heads = Heads::default();
    let kept = Arc::clone(&heads);
    tokio::spawn(async move {
        loop {
            let Ok((mut stream, _)) = listener.accept().await else {
                return;
            };
            let mut head = Vec::new();
            let mut buffer = [0; 1024];
            while !head.windows(4).any(|window| window == b"\r\n\r\n") {
                match stream.read(&mut buffer).await {
                    Ok(0) | Err(_) => break,
                    Ok(read) => head.extend_from_slice(&buffer[..read]),
                }
            }
            let text = String::from_utf8_lossy(&head).to_lowercase();
            let end = text.find("\r\n\r\n").unwrap_or(text.len());
            kept.lock().unwrap().push(text[..end].to_owned());
            let Reply {
                status,
                headers,
                body,
            } = reply(seen.fetch_add(1, Ordering::SeqCst));
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
    (url, count, heads)
}

fn builder(base_url: &str) -> ClientBuilder {
    Client::builder()
        .token(TOKEN)
        .user_agent("BM-Example-Test;test@example.com")
        .locale("en-us")
        .base_url(base_url)
        .retry_base_delay(Duration::ZERO)
}

async fn first_error(client: &Client, page: Option<i64>) -> Error {
    let params = OrdersListParams {
        page,
        ..Default::default()
    };
    let items: Vec<_> = client.orders().iter(&params).take(10).collect().await;
    let errors: Vec<_> = items.into_iter().filter_map(Result::err).collect();
    assert_eq!(errors.len(), 1, "the iteration stops at its first error");
    errors.into_iter().next().unwrap()
}

#[tokio::test]
async fn redirects_are_not_followed() {
    let (foreign, foreign_count) = serve(|_| json(200, r#"{"order_id": 1}"#)).await;
    let location = format!("{foreign}/");
    let (url, count) = serve(move |_| Reply {
        status: 302,
        headers: vec![("location", location.clone())],
        body: Vec::new(),
    })
    .await;
    let error = builder(&url)
        .build()
        .unwrap()
        .orders()
        .get(1)
        .await
        .unwrap_err();
    assert_eq!(error.status(), Some(302));
    assert_eq!(count.load(Ordering::SeqCst), 1);
    assert_eq!(foreign_count.load(Ordering::SeqCst), 0);
}

#[tokio::test]
async fn a_custom_client_follows_its_own_redirect_policy() {
    let (foreign, foreign_count, foreign_heads) = record(|_| json(200, r#"{"order_id": 1}"#)).await;
    let location = format!("{foreign}/");
    let redirect = move |_: usize| Reply {
        status: 302,
        headers: vec![("location", location.clone())],
        body: Vec::new(),
    };
    let (url, count) = serve(redirect.clone()).await;
    let order = builder(&url)
        .http_client(backmarket_seller::reqwest::Client::new())
        .build()
        .unwrap()
        .orders()
        .get(1)
        .await
        .unwrap();
    assert_eq!(order.order_id, Some(1));
    assert_eq!(count.load(Ordering::SeqCst), 1);
    assert_eq!(foreign_count.load(Ordering::SeqCst), 1);
    let head = foreign_heads.lock().unwrap()[0].clone();
    assert!(!head.contains("authorization"), "{head}");

    let (url, count) = serve(redirect).await;
    let none = backmarket_seller::reqwest::Client::builder()
        .redirect(backmarket_seller::reqwest::redirect::Policy::none())
        .build()
        .unwrap();
    let error = builder(&url)
        .http_client(none)
        .build()
        .unwrap()
        .orders()
        .get(1)
        .await
        .unwrap_err();
    assert_eq!(error.status(), Some(302));
    assert_eq!(count.load(Ordering::SeqCst), 1);
    assert_eq!(foreign_count.load(Ordering::SeqCst), 1);
}

#[tokio::test]
async fn an_empty_success_is_a_decode_error_where_the_spec_declares_json() {
    for headers in [
        vec![("content-type", "application/json".into())],
        Vec::new(),
    ] {
        let (url, _) = serve(move |_| Reply {
            status: 200,
            headers: headers.clone(),
            body: Vec::new(),
        })
        .await;
        let error = builder(&url)
            .build()
            .unwrap()
            .orders()
            .get(1)
            .await
            .unwrap_err();
        assert_eq!(error.kind(), ErrorKind::Decode);
        assert_eq!(error.status(), Some(200));
    }
}

#[tokio::test]
async fn an_empty_success_is_fine_where_the_spec_declares_no_json() {
    let (url, _) = serve(|_| Reply {
        status: 201,
        headers: Vec::new(),
        body: Vec::new(),
    })
    .await;
    let client = builder(&url).build().unwrap();
    let body = PostItemTransferCreateRequest::default();
    client.care().transfer_item(1, &body).await.unwrap();
    assert_eq!(client.care().create_refund(None).await.unwrap(), "");
}

#[tokio::test]
async fn iterator_rejects_a_next_link_that_does_not_advance() {
    let (url, count) = serve(|_| {
        json(
            200,
            r#"{"next": "https://foreign.invalid/ws/orders?page=1", "results": [{"order_id": 1}]}"#,
        )
    })
    .await;
    let error = first_error(&builder(&url).build().unwrap(), Some(1)).await;
    assert_eq!(error.kind(), ErrorKind::Decode);
    assert_eq!(count.load(Ordering::SeqCst), 1);
}

#[tokio::test]
async fn iterator_rejects_a_next_link_with_no_position() {
    let (url, count) = serve(|_| {
        json(
            200,
            r#"{"next": "https://foreign.invalid/ws/orders", "results": []}"#,
        )
    })
    .await;
    let error = first_error(&builder(&url).build().unwrap(), None).await;
    assert_eq!(error.kind(), ErrorKind::Decode);
    assert_eq!(count.load(Ordering::SeqCst), 1);
}

#[tokio::test]
async fn iterator_rejects_a_next_link_that_is_not_a_string() {
    let (url, count) = serve(|_| json(200, r#"{"next": 2, "results": []}"#)).await;
    let error = first_error(&builder(&url).build().unwrap(), None).await;
    assert_eq!(error.kind(), ErrorKind::Decode);
    assert_eq!(count.load(Ordering::SeqCst), 1);
}

#[tokio::test]
async fn iterator_rejects_a_next_link_that_is_not_a_url() {
    let (url, count) =
        serve(|_| json(200, r#"{"next": "http://[", "results": [{"order_id": 1}]}"#)).await;
    let error = first_error(&builder(&url).build().unwrap(), None).await;
    assert_eq!(error.kind(), ErrorKind::Decode);
    assert_eq!(count.load(Ordering::SeqCst), 1);
}

#[tokio::test]
async fn corrupt_compressed_429_still_honours_retry_after() {
    let (url, count) = serve(|n| match n {
        0 => Reply {
            status: 429,
            headers: vec![
                ("retry-after", "0".into()),
                ("content-encoding", "gzip".into()),
                ("content-type", "application/json".into()),
            ],
            body: b"not gzip".to_vec(),
        },
        _ => json(200, r#"{"order_id": 1}"#),
    })
    .await;
    let client = builder(&url)
        .rate_limit_wait(Duration::from_secs(60))
        .build()
        .unwrap();
    let order = tokio::time::timeout(Duration::from_secs(10), client.orders().get(1))
        .await
        .unwrap()
        .unwrap();
    assert_eq!(order.order_id, Some(1));
    assert_eq!(count.load(Ordering::SeqCst), 2);
}

#[tokio::test]
async fn the_maximum_does_not_apply_to_the_rate_limit_wait() {
    let wait = Duration::from_millis(300);
    let (url, count) = serve(|_| rate_limited("soon")).await;
    let client = builder(&url)
        .rate_limit_wait(wait)
        .max_retry_wait(Duration::from_millis(1))
        .max_retries(1)
        .build()
        .unwrap();
    let started = Instant::now();
    let error = client.orders().get(1).await.unwrap_err();
    assert_eq!(error.kind(), ErrorKind::RateLimited);
    assert!(started.elapsed() >= wait);
    assert_eq!(count.load(Ordering::SeqCst), 2);
}

#[test]
fn an_optional_reference_is_typed() {
    let competitor: Competitor = serde_json::from_str(
        r#"{"min_price": {"amount": "1.00", "currency": "EUR"}, "market": "FR"}"#,
    )
    .unwrap();
    assert_eq!(
        competitor
            .min_price
            .and_then(|price| price.amount)
            .as_deref(),
        Some("1.00")
    );
    assert_eq!(competitor.market, Some(MarketCode::Fr));
}

#[tokio::test]
async fn a_caller_supplied_http_client_still_sends_the_headers() {
    let (url, _, heads) = record(|_| json(200, r#"{"order_id": 1}"#)).await;
    let client = builder(&url)
        .http_client(backmarket_seller::reqwest::Client::new())
        .build()
        .unwrap();
    client.orders().get(1).await.unwrap();
    let head = heads.lock().unwrap()[0].clone();
    for header in [
        format!("authorization: basic {TOKEN}"),
        "user-agent: bm-example-test;test@example.com".to_owned(),
        "accept-language: en-us".to_owned(),
    ] {
        assert!(head.contains(&header), "{head}");
    }
}

#[tokio::test]
async fn an_optional_body_takes_a_reference_or_none() {
    let (url, _, heads) = record(|_| json(200, "{}")).await;
    let client = builder(&url).build().unwrap();
    let body = UpdateOrder {
        order_id: Some(1),
        ..Default::default()
    };
    client.orders().update(1, &body).await.unwrap();
    client.orders().update(1, None).await.unwrap();
    let heads = heads.lock().unwrap();
    let length = format!("content-length: {}", r#"{"order_id":1}"#.len());
    assert!(heads[0].contains(&length), "{}", heads[0]);
    assert!(
        !heads[1].contains("content-type: application/json"),
        "{}",
        heads[1]
    );
}

#[test]
fn a_date_time_is_typed_and_one_that_does_not_parse_stays_in_extra() {
    let order: Order = serde_json::from_str(
        r#"{"date_creation": "2026-01-02T03:04:05+01:00", "date_payment": "2026-01-02"}"#,
    )
    .unwrap();
    let created = order.date_creation.unwrap();
    assert_eq!(created.to_rfc3339(), "2026-01-02T03:04:05+01:00");
    assert_eq!(order.date_payment, None);
    assert_eq!(order.extra["date_payment"], "2026-01-02");
}

#[tokio::test]
async fn a_date_time_parameter_is_sent_as_rfc_3339() {
    let (url, _, heads) = record(|_| json(200, r#"{"results": []}"#)).await;
    let client = builder(&url).build().unwrap();
    let params = OrdersListParams {
        date_creation: chrono::DateTime::parse_from_rfc3339("2026-01-02T03:04:05+01:00").ok(),
        ..Default::default()
    };
    client.orders().list(&params).await.unwrap();
    let head = heads.lock().unwrap()[0].clone();
    assert!(
        head.contains("date_creation=2026-01-02t03%3a04%3a05%2b01%3a00"),
        "{head}"
    );
}
