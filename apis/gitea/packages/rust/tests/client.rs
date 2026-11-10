use std::sync::{Arc, Mutex};
use std::time::Duration;

use futures_util::TryStreamExt;
use gitea_rest::models::CreateIssueOption;
use gitea_rest::{Client, ClientBuilder, ContentsDownloadRawParams, ErrorKind, IssuesListParams};
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use tokio::net::TcpListener;

const TOKEN: &str = "unit-synthetic-access-token";
const PASSWORD: &str = "unit-synthetic-password";
const OTP: &str = "730194";
// base64 of `synthetic-user:unit-synthetic-password`.
const BASIC: &str = "c3ludGhldGljLXVzZXI6dW5pdC1zeW50aGV0aWMtcGFzc3dvcmQ=";

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

    fn target(&self) -> &str {
        self.head.split(' ').nth(1).unwrap_or_default()
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
        .token(TOKEN)
        .retry_base_delay(Duration::ZERO)
}

fn basic(url: &str) -> ClientBuilder {
    Client::builder()
        .base_url(url)
        .basic_auth("synthetic-user", PASSWORD)
        .retry_base_delay(Duration::ZERO)
}

fn sent(log: &Log) -> Vec<Sent> {
    log.lock().unwrap().clone()
}

#[tokio::test]
async fn the_token_goes_with_its_scheme_under_the_api_path() {
    let (url, log) = serve(|_| json(200, r#"{"id": 1, "login": "synthetic-user"}"#)).await;
    let client = builder(&url).user_agent("example/1.0").build().unwrap();
    let user = client.current_user().get().await.unwrap();
    assert_eq!(user.login.as_deref(), Some("synthetic-user"));
    let request = &sent(&log)[0];
    assert!(
        request.head.starts_with("get /api/v1/user "),
        "{}",
        request.head
    );
    assert_eq!(
        request.line("authorization"),
        Some(&*format!("token {TOKEN}"))
    );
    assert_eq!(request.line("accept"), Some("application/json"));
    assert_eq!(request.line("user-agent"), Some("example/1.0"));
    assert_eq!(request.line("x-gitea-otp"), None);
    assert_eq!(request.line("sudo"), None);
}

#[tokio::test]
async fn a_sub_path_install_keeps_its_path() {
    let (url, log) = serve(|_| json(200, r#"{"version": "28.3.0"}"#)).await;
    let client = builder(&format!("{url}/git/")).build().unwrap();
    client.misc().get_version().await.unwrap();
    assert_eq!(sent(&log)[0].target(), "/git/api/v1/version");
}

#[tokio::test]
async fn basic_auth_sends_the_one_time_password_and_sudo() {
    let (url, log) = serve(|_| json(200, r#"{"id": 2}"#)).await;
    let client = basic(&url)
        .otp(OTP)
        .sudo("synthetic-other-user")
        .build()
        .unwrap();
    client.current_user().get().await.unwrap();
    let request = &sent(&log)[0];
    assert_eq!(
        request.line("authorization"),
        Some(&*format!("basic {}", BASIC.to_lowercase()))
    );
    assert_eq!(request.line("x-gitea-otp"), Some(OTP));
    assert_eq!(request.line("sudo"), Some("synthetic-other-user"));
}

#[tokio::test]
async fn a_path_parameter_is_one_segment() {
    let (url, log) = serve(|_| Reply {
        status: 200,
        headers: vec![("content-type", "application/octet-stream".into())],
        body: b"synthetic".to_vec(),
    })
    .await;
    let client = builder(&url).build().unwrap();
    let file = client
        .contents()
        .download_raw(
            "synthetic-owner",
            "synthetic-repo",
            "docs/intro.md",
            &ContentsDownloadRawParams::default(),
        )
        .await
        .unwrap();
    assert_eq!(file.bytes().await.unwrap(), b"synthetic");
    assert_eq!(
        sent(&log)[0].target(),
        "/api/v1/repos/synthetic-owner/synthetic-repo/raw/docs%2fintro.md"
    );
}

#[tokio::test]
async fn iteration_follows_the_link_header_without_fetching_it() {
    let (other, other_log) = serve(|_| json(200, "[]")).await;
    let (url, log) = serve(move |number| {
        let mut reply = json(200, &format!(r#"[{{"number": {}}}]"#, number + 1));
        if number < 2 {
            let next = number + 2;
            reply.headers.push((
                "link",
                format!(
                    r#"<{other}/api/v1/repos/o/r/issues?limit=1&page={next}&state=open>; rel="next", <{other}/api/v1/repos/o/r/issues?limit=1&page=3>; rel="last""#
                ),
            ));
        }
        reply
    })
    .await;
    let client = builder(&url).build().unwrap();
    let params = IssuesListParams {
        state: Some("open".into()),
        limit: Some(1),
        ..Default::default()
    };
    let issues: Vec<_> = client
        .issues()
        .iter("o", "r", &params)
        .try_collect()
        .await
        .unwrap();
    let numbers: Vec<_> = issues.iter().map(|issue| issue.number).collect();
    assert_eq!(numbers, [Some(1), Some(2), Some(3)]);
    let sent = sent(&log);
    assert_eq!(sent.len(), 3);
    for (index, request) in sent.iter().enumerate() {
        let target = request.target();
        assert!(target.starts_with("/api/v1/repos/o/r/issues?"), "{target}");
        assert!(target.contains("state=open"), "{target}");
        assert!(target.contains("limit=1"), "{target}");
        if index > 0 {
            assert!(target.contains(&format!("page={}", index + 1)), "{target}");
        }
    }
    assert!(sent_is_empty(&other_log));
}

fn sent_is_empty(log: &Log) -> bool {
    log.lock().unwrap().is_empty()
}

#[tokio::test]
async fn a_link_back_to_a_page_already_sent_is_a_decode_error() {
    let (url, log) = serve(|_| {
        let mut reply = json(200, r#"[{"number": 1}]"#);
        reply.headers.push((
            "link",
            r#"<https://gitea.example.test/api/v1/repos/o/r/issues?page=2&limit=1>; rel="next""#
                .into(),
        ));
        reply
    })
    .await;
    let client = builder(&url).build().unwrap();
    let params = IssuesListParams {
        limit: Some(1),
        ..Default::default()
    };
    let error = client
        .issues()
        .iter("o", "r", &params)
        .try_collect::<Vec<_>>()
        .await
        .unwrap_err();
    assert_eq!(error.kind(), ErrorKind::Decode);
    assert_eq!(sent(&log).len(), 2);
}

#[tokio::test]
async fn a_validation_error_carries_giteas_message() {
    let (url, log) = serve(|_| {
        json(
            422,
            r#"{"message": "[Title]: Required", "url": "https://gitea.example.test/api/swagger"}"#,
        )
    })
    .await;
    let client = builder(&url).build().unwrap();
    let error = client
        .issues()
        .create("o", "r", Some(&CreateIssueOption::default()))
        .await
        .unwrap_err();
    assert_eq!(error.kind(), ErrorKind::Validation);
    assert_eq!(error.status(), Some(422));
    assert_eq!(error.detail(), Some("[Title]: Required"));
    assert_eq!(sent(&log).len(), 1, "a write is not retried");
}

#[tokio::test]
async fn an_error_holds_no_credential() {
    let body = format!("bad login {PASSWORD} {OTP} {BASIC}");
    let (url, _) = serve(move |_| json(401, &body)).await;
    let client = basic(&url).otp(OTP).build().unwrap();
    let error = client.current_user().get().await.unwrap_err();
    assert_eq!(error.kind(), ErrorKind::Authentication);
    assert_eq!(error.raw_body(), Some("bad login *** *** ***"));
    let text = format!("{error} {error:?}");
    for secret in [PASSWORD, OTP, BASIC] {
        assert!(!text.contains(secret), "{text}");
    }
}

#[tokio::test]
async fn a_get_is_retried_after_a_server_error() {
    let (url, log) = serve(|number| {
        if number == 0 {
            json(503, "unavailable")
        } else {
            json(200, r#"{"version": "28.3.0"}"#)
        }
    })
    .await;
    let client = builder(&url).build().unwrap();
    client.misc().get_version().await.unwrap();
    assert_eq!(sent(&log).len(), 2);
}

#[tokio::test]
async fn redirects_are_not_followed() {
    let (foreign, foreign_log) = serve(|_| json(200, "{}")).await;
    let location = format!("{foreign}/api/v1/user");
    let (url, log) = serve(move |_| Reply {
        status: 302,
        headers: vec![("location", location.clone())],
        body: Vec::new(),
    })
    .await;
    let client = builder(&url).build().unwrap();
    let error = client.current_user().get().await.unwrap_err();
    assert_eq!(error.kind(), ErrorKind::Api);
    assert_eq!(error.status(), Some(302));
    assert_eq!(sent(&log).len(), 1);
    assert!(sent_is_empty(&foreign_log));
}

#[tokio::test]
async fn an_attachment_is_a_multipart_part() {
    let (url, log) = serve(|_| json(201, r#"{"id": 7, "name": "notes.txt"}"#)).await;
    let client = builder(&url).build().unwrap();
    let params = gitea_rest::IssuesUploadCommentAttachmentParams {
        attachment: Some(gitea_rest::File::new("notes.txt", "synthetic notes")),
        ..Default::default()
    };
    let attachment = client
        .issues()
        .upload_comment_attachment("o", "r", 3, &params)
        .await
        .unwrap();
    assert_eq!(attachment.id, Some(7));
    let request = &sent(&log)[0];
    assert_eq!(
        request.target(),
        "/api/v1/repos/o/r/issues/comments/3/assets"
    );
    let body = String::from_utf8_lossy(&request.body);
    assert!(
        body.contains(r#"name="attachment"; filename="notes.txt""#),
        "{body}"
    );
    assert!(body.contains("synthetic notes"), "{body}");
}
