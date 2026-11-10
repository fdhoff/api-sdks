//! Smoke test of the published crate, run by the published packages workflow against the mock, never a live instance.
//! Built in a clean package that depends on the published version from crates.io, which the workflow checks.
//! The mock serves the spec's paths without the `/api/v1` the client adds, so requests go through a local proxy
//! that removes it.

use std::env;
use std::error::Error;
use std::io::{Read, Write};
use std::net::{TcpListener, TcpStream};
use std::thread;

use gitea_rest::Client;
use gitea_rest::reqwest::{self, Proxy};

/// Forwards one request per connection to its origin, without the prefix, and copies the reply back.
fn forward(mut client: TcpStream) -> std::io::Result<()> {
    let mut data = Vec::new();
    let mut buffer = [0; 8192];
    while !data.windows(4).any(|window| window == b"\r\n\r\n") {
        let read = client.read(&mut buffer)?;
        if read == 0 {
            return Ok(());
        }
        data.extend_from_slice(&buffer[..read]);
    }
    let head = String::from_utf8_lossy(&data).into_owned();
    let (line, rest) = head.split_once("\r\n").unwrap_or_default();
    let mut parts = line.splitn(3, ' ');
    let (method, target, version) = (
        parts.next().unwrap_or_default(),
        parts.next().unwrap_or_default(),
        parts.next().unwrap_or_default(),
    );
    let target = target.strip_prefix("http://").unwrap_or(target);
    let (origin, path) = target.split_at(target.find('/').unwrap_or(target.len()));
    let path = path.strip_prefix("/api/v1").unwrap_or(path);
    let headers: String = rest
        .split_inclusive("\r\n")
        .filter(|line| !line.to_ascii_lowercase().starts_with("connection:"))
        .collect();
    let mut upstream = TcpStream::connect(origin)?;
    write!(
        upstream,
        "{method} {path} {version}\r\nconnection: close\r\n{headers}"
    )?;
    let mut reply = Vec::new();
    upstream.read_to_end(&mut reply)?;
    client.write_all(&reply)
}

fn proxy() -> std::io::Result<String> {
    let listener = TcpListener::bind("127.0.0.1:0")?;
    let url = format!("http://{}", listener.local_addr()?);
    thread::spawn(move || {
        for stream in listener.incoming().flatten() {
            let _ = forward(stream);
        }
    });
    Ok(url)
}

#[tokio::main(flavor = "current_thread")]
async fn main() -> Result<(), Box<dyn Error>> {
    let mock = env::var("SMOKE_BASE_URL")?;
    let http = reqwest::Client::builder()
        .proxy(Proxy::http(proxy()?)?)
        .pool_max_idle_per_host(0)
        .build()?;
    let client = Client::builder()
        .base_url(&mock)
        .token("smoke-synthetic-access-token")
        .http_client(http)
        .build()?;
    let version = client.misc().get_version().await?;
    println!(
        "gitea-rest {}: read version {:?}",
        env::var("SMOKE_VERSION")?,
        version.version
    );
    Ok(())
}
