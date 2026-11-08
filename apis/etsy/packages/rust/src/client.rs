use std::fmt;
use std::sync::Arc;
use std::time::Duration;

use reqwest::header::{ACCEPT, HeaderMap, HeaderValue, USER_AGENT};

use crate::errors::to_error;
use crate::oauth::{EtsyCredentials, OAuth, OnToken, Token};
use crate::runtime::{Settings, Transport};

/// The API's server.
pub const BASE_URL: &str = "https://openapi.etsy.com";

/// A [`ClientBuilder`] setting that cannot work.
#[derive(Debug)]
pub struct BuildError(String);

impl fmt::Display for BuildError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.write_str(&self.0)
    }
}

impl std::error::Error for BuildError {}

fn invalid(message: &str) -> BuildError {
    BuildError(message.to_owned())
}

/// Configures a [`Client`]. Start from [`Client::builder`].
#[derive(Clone)]
pub struct ClientBuilder {
    api_key: Option<String>,
    shared_secret: Option<String>,
    access_token: Option<String>,
    refresh_token: Option<String>,
    on_token: Option<OnToken>,
    user_agent: Option<String>,
    base_url: String,
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
            api_key: None,
            shared_secret: None,
            access_token: None,
            refresh_token: None,
            on_token: None,
            user_agent: None,
            base_url: BASE_URL.to_owned(),
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
            .field("user_agent", &self.user_agent)
            .field("base_url", &self.base_url)
            .field("on_token", &self.on_token.is_some())
            .field("http_client", &self.http_client.is_some())
            .finish_non_exhaustive()
    }
}

impl ClientBuilder {
    /// Sets your app's keystring. Required.
    pub fn api_key(mut self, api_key: impl Into<String>) -> Self {
        self.api_key = Some(api_key.into());
        self
    }

    /// Sets your app's shared secret. Required. It is sent with the keystring as `x-api-key` on
    /// every call, and the client keeps it only in memory.
    pub fn shared_secret(mut self, shared_secret: impl Into<String>) -> Self {
        self.shared_secret = Some(shared_secret.into());
        self
    }

    /// Sets an OAuth access token, sent verbatim as a bearer token on the calls that need one.
    pub fn access_token(mut self, access_token: impl Into<String>) -> Self {
        self.access_token = Some(access_token.into());
        self
    }

    /// Sets a refresh token, so that the client can replace an expired access token by itself,
    /// once per call.
    pub fn refresh_token(mut self, refresh_token: impl Into<String>) -> Self {
        self.refresh_token = Some(refresh_token.into());
        self
    }

    /// Called with every new token pair, from [`OAuth::exchange_code`] and every refresh, so you
    /// can store it. The old refresh token stops working. It runs before the call that needed the
    /// refresh is retried, so keep it quick: send the token to a channel, for example.
    pub fn on_token(mut self, on_token: impl Fn(&Token) + Send + Sync + 'static) -> Self {
        self.on_token = Some(Arc::new(on_token));
        self
    }

    /// Sets the `User-Agent`. None is sent unless you set one.
    pub fn user_agent(mut self, user_agent: impl Into<String>) -> Self {
        self.user_agent = Some(user_agent.into());
        self
    }

    /// Sets the server root, for tests against a mock. Your credentials are sent to it.
    pub fn base_url(mut self, base_url: impl Into<String>) -> Self {
        self.base_url = base_url.into();
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
    /// `reqwest::redirect::Policy::none()` to keep your credentials on the server you selected, as
    /// the default client does. Under reqwest's default policy, a 307 or 308 to the same host
    /// resends a write's body with your credentials.
    ///
    /// The client retries only GETs after a failure, but a retry policy set with
    /// `reqwest::ClientBuilder::retry` runs inside your client, below that rule, and can resend a
    /// write. Leave it unset, or limit it to GETs.
    pub fn http_client(mut self, client: reqwest::Client) -> Self {
        self.http_client = Some(client);
        self
    }

    fn server(&self) -> Result<String, BuildError> {
        let parsed = url::Url::parse(&self.base_url)
            .map_err(|_| invalid("the base URL must be absolute"))?;
        if !parsed.has_host() {
            return Err(invalid("the base URL must be absolute"));
        }
        Ok(self.base_url.trim_end_matches('/').to_owned())
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

    /// Builds the client.
    pub fn build(self) -> Result<Client, BuildError> {
        let required = |value: &Option<String>, message: &str| match value.as_deref() {
            Some(text) if !text.is_empty() => Ok(text.to_owned()),
            _ => Err(invalid(message)),
        };
        let api_key = required(&self.api_key, "the api_key is required")?;
        let shared_secret = required(&self.shared_secret, "the shared_secret is required")?;
        let credentials = Arc::new(
            EtsyCredentials::new(
                api_key,
                shared_secret,
                self.access_token.clone(),
                self.refresh_token.clone(),
                self.on_token.clone(),
            )
            .map_err(|_| invalid("the api_key, shared_secret and tokens must be printable text"))?,
        );
        let transport = Transport::new(Settings {
            base_url: self.server()?,
            headers: self.headers()?,
            credentials: credentials.clone(),
            to_error,
            timeout: self.timeout,
            max_retries: self.max_retries,
            retry_base_delay: self.retry_base_delay,
            rate_limit_wait: self.rate_limit_wait,
            max_retry_wait: self.max_retry_wait,
            http: self.http_client,
        })
        .map_err(|_| invalid("the HTTP client cannot be built"))?;
        let transport = Arc::new(transport);
        credentials.attach(&transport);
        Ok(Client {
            transport,
            credentials,
        })
    }
}

/// Calls the API. Cloning is cheap and shares the connection pool and the tokens, and a client is
/// safe to use from many tasks at once. Its operations are grouped by resource, such as
/// [`Client::listings`], and OAuth is on [`Client::oauth`].
#[derive(Clone, Debug)]
pub struct Client {
    pub(crate) transport: Arc<Transport>,
    credentials: Arc<EtsyCredentials>,
}

impl Client {
    /// Starts configuring a client. Set [`api_key`](ClientBuilder::api_key) and
    /// [`shared_secret`](ClientBuilder::shared_secret), and for OAuth operations an
    /// [`access_token`](ClientBuilder::access_token), then call [`build`](ClientBuilder::build).
    pub fn builder() -> ClientBuilder {
        ClientBuilder::default()
    }

    /// The OAuth 2 flow: the authorization URL, code exchange and refresh.
    pub fn oauth(&self) -> OAuth {
        OAuth::new(self.credentials.clone(), self.transport.clone())
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    const KEY: &str = "synthetic-keystring";
    const SECRET: &str = "synthetic-shared-secret";
    const ACCESS: &str = "12345678.synthetic-access";

    fn builder() -> ClientBuilder {
        Client::builder().api_key(KEY).shared_secret(SECRET)
    }

    #[test]
    fn the_api_key_and_shared_secret_are_required() {
        assert!(Client::builder().shared_secret(SECRET).build().is_err());
        assert!(Client::builder().api_key(KEY).build().is_err());
        assert!(builder().api_key("").build().is_err());
        assert!(builder().build().is_ok());
    }

    #[test]
    fn the_base_url_must_be_absolute() {
        assert!(builder().base_url("not a url").build().is_err());
        assert!(builder().base_url("http://127.0.0.1:4010/").build().is_ok());
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
    fn debug_output_never_shows_a_secret() {
        let builder = builder()
            .access_token(ACCESS)
            .refresh_token("12345678.synthetic-refresh");
        let client = builder.clone().build().unwrap();
        for text in [
            format!("{builder:?}"),
            format!("{client:?}"),
            format!("{:?}", client.oauth()),
        ] {
            for secret in [KEY, SECRET, ACCESS, "synthetic-refresh"] {
                assert!(!text.contains(secret), "{text}");
            }
        }
    }
}
