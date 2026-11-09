use std::collections::HashMap;
use std::fmt;
use std::sync::Arc;
use std::time::Duration;

use reqwest::header::{ACCEPT, AUTHORIZATION, HeaderMap, HeaderValue, USER_AGENT};

use crate::errors::to_error;
use crate::runtime::{Settings, StaticCredentials, Transport, select_hosts};

/// The base URL of each host the API uses, by environment. `vault` serves only
/// [`CardsApi::reveal`](crate::CardsApi::reveal). Mercury documents no sandbox host for card
/// details, so in the sandbox those calls go to its own API host.
pub const ENVIRONMENTS: &[(&str, &[(&str, &str)])] = &[
    (
        "production",
        &[
            ("api", "https://api.mercury.com/api/v1"),
            ("vault", "https://vault-api.mercury.com/api/v1"),
        ],
    ),
    (
        "sandbox",
        &[
            ("api", "https://api-sandbox.mercury.com/api/v1"),
            ("vault", "https://api-sandbox.mercury.com/api/v1"),
        ],
    ),
];

/// A [`ClientBuilder`] setting that cannot work.
#[derive(Debug)]
pub struct BuildError(String);

impl fmt::Display for BuildError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.write_str(&self.0)
    }
}

impl std::error::Error for BuildError {}

fn invalid(message: impl Into<String>) -> BuildError {
    BuildError(message.into())
}

fn credentials(token: String) -> Result<StaticCredentials, BuildError> {
    let mut authorization = HeaderValue::from_str(&format!("Bearer {token}"))
        .map_err(|_| invalid("the token cannot be sent as a header"))?;
    authorization.set_sensitive(true);
    let mut headers = HeaderMap::new();
    headers.insert(AUTHORIZATION, authorization);
    Ok(StaticCredentials::new(headers, vec![token]))
}

/// Configures a [`Client`]. Start from [`Client::builder`].
#[derive(Clone)]
pub struct ClientBuilder {
    token: Option<String>,
    environment: String,
    hosts: Option<HashMap<String, String>>,
    user_agent: Option<String>,
    timeout: Duration,
    max_retries: u32,
    retry_base_delay: Duration,
    rate_limit_wait: Duration,
    max_retry_wait: Duration,
    http_client: Option<reqwest::Client>,
}

impl Default for ClientBuilder {
    fn default() -> Self {
        Self {
            token: None,
            environment: "production".to_owned(),
            hosts: None,
            user_agent: None,
            timeout: Duration::from_secs(30),
            max_retries: 3,
            retry_base_delay: Duration::from_millis(500),
            rate_limit_wait: Duration::from_secs(10),
            max_retry_wait: Duration::from_secs(60),
            http_client: None,
        }
    }
}

impl fmt::Debug for ClientBuilder {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("ClientBuilder")
            .field("environment", &self.environment)
            .field("hosts", &self.hosts)
            .field("user_agent", &self.user_agent)
            .field("http_client", &self.http_client.is_some())
            .finish_non_exhaustive()
    }
}

impl ClientBuilder {
    /// Sets your API token. Required. It is sent verbatim as a bearer token, so keep its
    /// `secret-token:` prefix. The client keeps it only in memory and never logs it.
    pub fn token(mut self, token: impl Into<String>) -> Self {
        self.token = Some(token.into());
        self
    }

    /// Selects `production`, the default, or `sandbox`. A sandbox token works only in the sandbox.
    pub fn environment(mut self, environment: impl Into<String>) -> Self {
        self.environment = environment.into();
        self
    }

    /// Sets your own base URL for each of `api` and `vault`, such as a mock's, instead of the
    /// environment's. Your token is sent to them.
    pub fn hosts<K: Into<String>, V: Into<String>>(
        mut self,
        hosts: impl IntoIterator<Item = (K, V)>,
    ) -> Self {
        self.hosts = Some(
            hosts
                .into_iter()
                .map(|(key, url)| (key.into(), url.into()))
                .collect(),
        );
        self
    }

    /// Sets the `User-Agent`. Optional.
    pub fn user_agent(mut self, user_agent: impl Into<String>) -> Self {
        self.user_agent = Some(user_agent.into());
        self
    }

    /// Sets the deadline for each attempt, from sending the request to reading the last byte of
    /// the response. The default is 30 seconds.
    pub fn timeout(mut self, timeout: Duration) -> Self {
        self.timeout = timeout;
        self
    }

    /// Sets the retries after the first attempt. The default is 3.
    pub fn max_retries(mut self, retries: u32) -> Self {
        self.max_retries = retries;
        self
    }

    /// Sets the base of the exponential backoff. The default is 500 milliseconds.
    pub fn retry_base_delay(mut self, delay: Duration) -> Self {
        self.retry_base_delay = delay;
        self
    }

    /// Sets the wait after a 429 with no usable `Retry-After`. The default is 10 seconds.
    pub fn rate_limit_wait(mut self, wait: Duration) -> Self {
        self.rate_limit_wait = wait;
        self
    }

    /// Sets the longest `Retry-After` to wait for. The default is 60 seconds. A longer one fails
    /// the call at once with [`ErrorKind::RateLimited`](crate::ErrorKind::RateLimited), and the
    /// header's value in [`Error::retry_after`](crate::Error::retry_after).
    pub fn max_retry_wait(mut self, wait: Duration) -> Self {
        self.max_retry_wait = wait;
        self
    }

    /// Sends requests through your own [`reqwest::Client`], for example to share its connection
    /// pool or to set a proxy or TLS roots. The client still sends its own headers and applies
    /// `timeout` and its retries. Redirects follow your client's policy: build it with
    /// `reqwest::redirect::Policy::none()` to keep your token on the hosts you selected, as the
    /// default client does.
    ///
    /// The client retries only GETs, and the four money-moving writes that carry an idempotency
    /// key, after a failure. A retry policy set with `reqwest::ClientBuilder::retry` runs inside
    /// your client, below that rule, and can resend any write. Leave it unset, or limit it to GETs.
    pub fn http_client(mut self, client: reqwest::Client) -> Self {
        self.http_client = Some(client);
        self
    }

    fn headers(&self) -> Result<HeaderMap, BuildError> {
        let mut headers = HeaderMap::new();
        headers.insert(ACCEPT, HeaderValue::from_static("application/json"));
        if let Some(user_agent) = &self.user_agent {
            let value = HeaderValue::from_str(user_agent)
                .map_err(|_| invalid("user_agent cannot be sent as a header"))?;
            headers.insert(USER_AGENT, value);
        }
        Ok(headers)
    }

    fn hosts_map(&self) -> Result<HashMap<String, String>, BuildError> {
        let hosts =
            select_hosts(ENVIRONMENTS, &self.environment, self.hosts.as_ref()).map_err(invalid)?;
        for url in hosts.values() {
            let parsed = url::Url::parse(url)
                .map_err(|_| invalid(format!("the host URL {url} must be absolute")))?;
            if !parsed.has_host() {
                return Err(invalid(format!("the host URL {url} must be absolute")));
            }
        }
        Ok(hosts)
    }

    /// Builds the client.
    pub fn build(self) -> Result<Client, BuildError> {
        let token = match self.token.clone() {
            Some(token) if !token.is_empty() => token,
            _ => return Err(invalid("the token is required")),
        };
        let hosts = self.hosts_map()?;
        let transport = Transport::new(Settings {
            base_url: hosts["api"].clone(),
            hosts,
            headers: self.headers()?,
            header_defaults: HashMap::new(),
            credentials: Arc::new(credentials(token)?),
            to_error,
            timeout: self.timeout,
            max_retries: self.max_retries,
            retry_base_delay: self.retry_base_delay,
            rate_limit_wait: self.rate_limit_wait,
            max_retry_wait: self.max_retry_wait,
            http: self.http_client,
        })
        .map_err(|error| invalid(error.to_string()))?;
        Ok(Client {
            transport: Arc::new(transport),
        })
    }
}

/// Calls the API. Cloning is cheap and shares the connection pool, and a client is safe to use
/// from many tasks at once. Its operations are grouped by resource, such as [`Client::accounts`].
#[derive(Clone, Debug)]
pub struct Client {
    pub(crate) transport: Arc<Transport>,
}

impl Client {
    /// Starts configuring a client. Set [`token`](ClientBuilder::token), then call
    /// [`build`](ClientBuilder::build).
    pub fn builder() -> ClientBuilder {
        ClientBuilder::default()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    const TOKEN: &str = "secret-token:synthetic-token";

    fn builder() -> ClientBuilder {
        Client::builder().token(TOKEN)
    }

    #[test]
    fn the_token_is_required() {
        assert!(Client::builder().build().is_err());
        assert!(builder().token("").build().is_err());
        assert!(builder().build().is_ok());
    }

    #[test]
    fn hosts_come_from_the_environment_or_the_caller() {
        assert!(builder().environment("sandbox").build().is_ok());
        let error = builder().environment("staging").build().unwrap_err();
        assert_eq!(
            error.to_string(),
            "unknown environment staging; expected one of: production, sandbox"
        );
        let mock = [
            ("api", "http://127.0.0.1:4010"),
            ("vault", "http://127.0.0.1:4010"),
        ];
        assert!(builder().hosts(mock).build().is_ok());
        let error = builder()
            .hosts([("api", "http://127.0.0.1:4010")])
            .build()
            .unwrap_err();
        assert_eq!(error.to_string(), "hosts lacks keys: vault");
        let relative = [("api", "/v1"), ("vault", "/v1")];
        assert!(builder().hosts(relative).build().is_err());
    }

    #[test]
    fn a_caller_can_supply_the_http_client() {
        assert!(
            builder()
                .http_client(reqwest::Client::new())
                .build()
                .is_ok()
        );
    }

    #[test]
    fn debug_output_never_shows_the_token() {
        let builder = builder();
        let client = builder.clone().build().unwrap();
        for text in [format!("{builder:?}"), format!("{client:?}")] {
            assert!(!text.contains("synthetic-token"), "{text}");
        }
    }
}
