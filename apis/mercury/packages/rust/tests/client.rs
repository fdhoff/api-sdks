use std::sync::{Arc, Mutex};
use std::time::Duration;

use futures_util::TryStreamExt;
use mercury_banking::models::{
    AddRecipientRequest, PostTransactionApiRequest, PostTransactionPaymentMethod,
};
use mercury_banking::{AccountsListParams, Client, ClientBuilder, ErrorKind};
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use tokio::net::TcpListener;

const TOKEN: &str = "secret-token:synthetic-token";

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

fn builder(api: &str, vault: &str) -> ClientBuilder {
    Client::builder()
        .token(TOKEN)
        .hosts([("api", api), ("vault", vault)])
        .retry_base_delay(Duration::ZERO)
}

fn sent(log: &Log) -> Vec<Sent> {
    log.lock().unwrap().clone()
}

fn payment(idempotency_key: Option<&str>) -> PostTransactionApiRequest {
    PostTransactionApiRequest {
        recipient_id: Some("00000000-0000-4000-8000-4ec100000001".to_owned()),
        amount: Some(12.5),
        payment_method: Some(PostTransactionPaymentMethod::Ach),
        idempotency_key: idempotency_key.map(str::to_owned),
        ..Default::default()
    }
}

#[tokio::test]
async fn the_token_is_sent_as_a_bearer_token_with_json_accepted() {
    let (url, log) = serve(|_| json(200, r#"{"id": "org-synthetic"}"#)).await;
    let client = builder(&url, &url)
        .user_agent("example/1.0")
        .build()
        .unwrap();
    client.organization().get().await.unwrap();
    let request = &sent(&log)[0];
    assert!(
        request.head.starts_with("get /organization "),
        "{}",
        request.head
    );
    assert_eq!(
        request.line("authorization"),
        Some(format!("bearer {TOKEN}").as_str())
    );
    assert_eq!(request.line("accept"), Some("application/json"));
    assert_eq!(request.line("user-agent"), Some("example/1.0"));
}

#[tokio::test]
async fn revealing_a_card_goes_to_the_vault_host() {
    let (api, api_log) = serve(|_| json(200, "{}")).await;
    let (vault, vault_log) = serve(|_| json(200, r#"{"pan": "4000000000000000"}"#)).await;
    let client = builder(&api, &vault).build().unwrap();
    client
        .cards()
        .reveal("00000000-0000-4000-8000-ca4d00000001")
        .await
        .unwrap();
    assert!(sent(&api_log).is_empty());
    assert_eq!(sent(&vault_log).len(), 1);
}

#[tokio::test]
async fn a_payment_with_a_key_is_retried_after_a_server_error_with_the_same_body() {
    let (url, log) = serve(|number| {
        if number == 0 {
            json(503, "")
        } else {
            json(200, r#"{"id": "00000000-0000-4000-8000-7a4000000001"}"#)
        }
    })
    .await;
    let client = builder(&url, &url).build().unwrap();
    client
        .accounts()
        .send_money(
            "00000000-0000-4000-8000-acc000000001",
            &payment(Some("synthetic-key")),
        )
        .await
        .unwrap();
    let sent = sent(&log);
    assert_eq!(sent.len(), 2);
    assert_eq!(sent[0].body, sent[1].body);
    let body: serde_json::Value = serde_json::from_slice(&sent[0].body).unwrap();
    assert_eq!(body["idempotencyKey"], "synthetic-key");
}

#[tokio::test]
async fn a_payment_without_a_key_is_not_retried() {
    let (url, log) = serve(|_| json(503, "")).await;
    let client = builder(&url, &url).build().unwrap();
    let error = client
        .accounts()
        .send_money("00000000-0000-4000-8000-acc000000001", &payment(None))
        .await
        .unwrap_err();
    assert_eq!(error.kind(), ErrorKind::Server);
    assert_eq!(sent(&log).len(), 1);
}

#[tokio::test]
async fn other_writes_are_not_retried() {
    let (url, log) = serve(|_| json(500, "")).await;
    let client = builder(&url, &url).build().unwrap();
    let recipient = AddRecipientRequest {
        name: Some("Synthetic Supplier".to_owned()),
        ..Default::default()
    };
    let error = client.recipients().create(&recipient).await.unwrap_err();
    assert_eq!(error.kind(), ErrorKind::Server);
    assert_eq!(sent(&log).len(), 1);
}

#[tokio::test]
async fn a_download_asks_for_a_pdf_and_keeps_every_byte() {
    const PDF: &[u8] = b"%PDF-1.4\n\xff\xe8\xd5\xd1\n";
    let (url, log) = serve(|_| Reply {
        status: 200,
        headers: vec![("content-type", "application/pdf".into())],
        body: PDF.to_vec(),
    })
    .await;
    let client = builder(&url, &url).build().unwrap();
    let download = client
        .statements()
        .download_pdf("00000000-0000-4000-8000-5e4000000001")
        .await
        .unwrap();
    assert_eq!(download.content_type(), "application/pdf");
    assert_eq!(download.bytes().await.unwrap(), PDF);
    assert_eq!(sent(&log)[0].line("accept"), Some("application/pdf"));
}

#[tokio::test]
async fn iteration_sends_each_next_page_back_as_start_after() {
    let (url, log) = serve(|number| match number {
        0 => json(
            200,
            r#"{"accounts": [{"id": "a1"}], "page": {"nextPage": "a1"}}"#,
        ),
        _ => json(200, r#"{"accounts": [{"id": "a2"}], "page": {}}"#),
    })
    .await;
    let client = builder(&url, &url).build().unwrap();
    let params = AccountsListParams {
        limit: Some(1),
        ..Default::default()
    };
    let accounts: Vec<_> = client.accounts().iter(&params).try_collect().await.unwrap();
    let ids: Vec<_> = accounts
        .iter()
        .map(|account| account.id.as_deref())
        .collect();
    assert_eq!(ids, [Some("a1"), Some("a2")]);
    let sent = sent(&log);
    assert!(sent[1].head.contains("start_after=a1"), "{}", sent[1].head);
    assert!(sent[1].head.contains("limit=1"), "{}", sent[1].head);
}

#[tokio::test]
async fn an_error_keeps_the_raw_body_without_the_token() {
    let body = format!("token {TOKEN} was refused");
    let (url, _) = serve(move |_| json(401, &body)).await;
    let client = builder(&url, &url).build().unwrap();
    let error = client.organization().get().await.unwrap_err();
    assert_eq!(error.kind(), ErrorKind::Authentication);
    assert_eq!(error.status(), Some(401));
    let raw = error.raw_body().unwrap();
    assert!(!raw.contains("synthetic-token"), "{raw}");
    assert!(raw.ends_with("was refused"), "{raw}");
}

#[tokio::test]
async fn redirects_are_not_followed() {
    let (foreign, foreign_log) = serve(|_| json(200, "{}")).await;
    let location = format!("{foreign}/organization");
    let (url, log) = serve(move |_| Reply {
        status: 302,
        headers: vec![("location", location.clone())],
        body: Vec::new(),
    })
    .await;
    let client = builder(&url, &url).build().unwrap();
    let error = client.organization().get().await.unwrap_err();
    assert_eq!(error.status(), Some(302));
    assert_eq!(sent(&log).len(), 1);
    assert!(sent(&foreign_log).is_empty());
}
