use std::collections::HashMap;
use std::fmt;
use std::sync::Arc;
use std::time::Duration;

use reqwest::header::{ACCEPT, AUTHORIZATION, HeaderMap, HeaderValue, USER_AGENT};

use crate::errors::to_error;
use crate::runtime::{Download, Error, Settings, StaticCredentials, Transport};

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

// TODO: partner OAuth2 client-credentials tokens, if users ask.
fn credentials(api_key: String) -> Result<StaticCredentials, BuildError> {
    let mut authorization = HeaderValue::from_str(&api_key)
        .map_err(|_| invalid("the API key cannot be sent as a header"))?;
    authorization.set_sensitive(true);
    let mut headers = HeaderMap::new();
    headers.insert(AUTHORIZATION, authorization);
    Ok(StaticCredentials::new(headers, vec![api_key]))
}

/// Configures a [`Client`]. Start from [`Client::builder`].
#[derive(Clone)]
pub struct ClientBuilder {
    base_url: Option<String>,
    api_key: Option<String>,
    shop_id: Option<i64>,
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
            base_url: None,
            api_key: None,
            shop_id: None,
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
            .field("base_url", &self.base_url)
            .field("shop_id", &self.shop_id)
            .field("user_agent", &self.user_agent)
            .field("http_client", &self.http_client.is_some())
            .finish_non_exhaustive()
    }
}

impl ClientBuilder {
    /// Sets your operator's Mirakl instance, such as `https://your-operator.mirakl.net`, from its
    /// seller back office. Required: every operator runs its own, so there is no default. Your key
    /// is sent to it.
    pub fn base_url(mut self, base_url: impl Into<String>) -> Self {
        self.base_url = Some(base_url.into());
        self
    }

    /// Sets your shop API key. Required. It is sent as the whole `Authorization` header, with no
    /// scheme. The client keeps it only in memory and never logs it.
    pub fn api_key(mut self, api_key: impl Into<String>) -> Self {
        self.api_key = Some(api_key.into());
        self
    }

    /// Sets the shop to act for, when your key covers several. It is sent as `shop_id` on every
    /// call that leaves its own `shop_id` unset.
    pub fn shop_id(mut self, shop_id: i64) -> Self {
        self.shop_id = Some(shop_id);
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
    /// `reqwest::redirect::Policy::none()` to keep your key on your base URL, as the default
    /// client does, and so that [`Client::download_url`] decides where your key goes.
    ///
    /// The client retries a write only after a 429. A retry policy set with
    /// `reqwest::ClientBuilder::retry` runs inside your client, below that rule, and can resend
    /// any write. Leave it unset, or limit it to GETs.
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

    fn server(&self) -> Result<String, BuildError> {
        let Some(base_url) = self.base_url.as_deref().filter(|url| !url.is_empty()) else {
            return Err(invalid(
                "the base URL is required: your operator's Mirakl instance",
            ));
        };
        let parsed = url::Url::parse(base_url)
            .map_err(|_| invalid("the base URL must be an absolute http or https URL"))?;
        if !matches!(parsed.scheme(), "http" | "https") || !parsed.has_host() {
            return Err(invalid(
                "the base URL must be an absolute http or https URL",
            ));
        }
        Ok(base_url.trim_end_matches('/').to_owned())
    }

    /// Builds the client.
    pub fn build(self) -> Result<Client, BuildError> {
        let base_url = self.server()?;
        let api_key = match self.api_key.clone() {
            Some(api_key) if !api_key.is_empty() => api_key,
            _ => return Err(invalid("the API key is required")),
        };
        let query_defaults = self
            .shop_id
            .map(|shop_id| ("shop_id".to_owned(), shop_id.to_string()))
            .into_iter()
            .collect();
        let transport = Transport::new(Settings {
            base_url,
            hosts: HashMap::new(),
            headers: self.headers()?,
            header_defaults: HashMap::new(),
            query_defaults,
            credentials: Arc::new(credentials(api_key)?),
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

/// Calls a Mirakl operator's seller API. Unofficial; not affiliated with, endorsed by or
/// sponsored by Mirakl SAS. Cloning is cheap and shares the connection pool, and a client is safe
/// to use from many tasks at once. Its operations are grouped by resource, such as
/// [`Client::orders`].
#[derive(Clone, Debug)]
pub struct Client {
    pub(crate) transport: Arc<Transport>,
}

impl Client {
    /// Starts configuring a client. Set [`base_url`](ClientBuilder::base_url) and
    /// [`api_key`](ClientBuilder::api_key), then call [`build`](ClientBuilder::build).
    pub fn builder() -> ClientBuilder {
        ClientBuilder::default()
    }

    /// Downloads a file from a URL an export's status returned, such as the `urls` of
    /// [`OrdersApi::wait_for_export`](crate::OrdersApi::wait_for_export). Your key goes only to
    /// the base URL's scheme, host and port, and never again once a redirect leaves them. Logs
    /// leave out the URL's query.
    pub async fn download_url(&self, url: &str) -> Result<Download, Error> {
        self.transport.download_url(url, None).await
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    const KEY: &str = "00000000-0000-4000-8000-5e11e4000001";

    fn builder() -> ClientBuilder {
        Client::builder()
            .base_url("https://operator.example.test")
            .api_key(KEY)
    }

    #[test]
    fn the_base_url_and_key_are_required() {
        assert!(builder().build().is_ok());
        let error = Client::builder().api_key(KEY).build().unwrap_err();
        assert_eq!(
            error.to_string(),
            "the base URL is required: your operator's Mirakl instance"
        );
        assert!(builder().base_url("").build().is_err());
        assert!(builder().api_key("").build().is_err());
        assert!(
            Client::builder()
                .base_url("https://operator.example.test")
                .build()
                .is_err()
        );
    }

    #[test]
    fn the_base_url_must_be_absolute_http() {
        for url in [
            "/api",
            "operator.example.test",
            "ftp://operator.example.test",
        ] {
            assert!(builder().base_url(url).build().is_err(), "{url}");
        }
        assert!(builder().base_url("http://127.0.0.1:4010/").build().is_ok());
    }

    #[test]
    fn a_key_that_is_not_a_header_value_is_refused() {
        assert!(builder().api_key("line\nbreak").build().is_err());
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
    fn debug_output_never_shows_the_key() {
        let builder = builder().shop_id(2001);
        let client = builder.clone().build().unwrap();
        for text in [format!("{builder:?}"), format!("{client:?}")] {
            assert!(!text.contains(KEY), "{text}");
        }
    }
}
