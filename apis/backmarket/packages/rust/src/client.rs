use std::collections::HashMap;
use std::fmt;
use std::sync::Arc;
use std::time::Duration;

use reqwest::header::{ACCEPT, ACCEPT_LANGUAGE, AUTHORIZATION, HeaderMap, HeaderValue, USER_AGENT};

use crate::errors::to_error;
use crate::runtime::{Settings, StaticCredentials, Transport};

/// A marketplace region.
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
#[non_exhaustive]
pub enum Region {
    Ap,
    Eu,
    Na,
}

/// Production or preprod.
#[derive(Clone, Copy, Debug, Default, PartialEq, Eq, Hash)]
#[non_exhaustive]
pub enum Environment {
    #[default]
    Production,
    Preprod,
}

fn server(region: Region, environment: Environment) -> &'static str {
    match (region, environment) {
        (Region::Ap, Environment::Production) => "https://www.backmarket.co.jp",
        (Region::Ap, Environment::Preprod) => "https://preprod.backmarket.co.jp",
        (Region::Eu, Environment::Production) => "https://www.backmarket.fr",
        (Region::Eu, Environment::Preprod) => "https://preprod.backmarket.fr",
        (Region::Na, Environment::Production) => "https://www.backmarket.com",
        (Region::Na, Environment::Preprod) => "https://preprod.backmarket.com",
    }
}

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

fn value(text: &str, name: &str) -> Result<HeaderValue, BuildError> {
    HeaderValue::from_str(text)
        .map_err(|_| BuildError(format!("{name} cannot be sent as a header")))
}

fn credentials(token: String) -> Result<StaticCredentials, BuildError> {
    let mut authorization = value(&format!("Basic {token}"), "the token")?;
    authorization.set_sensitive(true);
    let mut headers = HeaderMap::new();
    headers.insert(AUTHORIZATION, authorization);
    Ok(StaticCredentials::new(headers, vec![token]))
}

fn headers(user_agent: &str, locale: &str) -> Result<HeaderMap, BuildError> {
    let mut headers = HeaderMap::new();
    headers.insert(USER_AGENT, value(user_agent, "user_agent")?);
    headers.insert(ACCEPT, HeaderValue::from_static("application/json"));
    headers.insert(ACCEPT_LANGUAGE, value(locale, "locale")?);
    Ok(headers)
}

/// Configures a [`Client`]. Start from [`Client::builder`].
#[derive(Clone)]
pub struct ClientBuilder {
    token: Option<String>,
    user_agent: Option<String>,
    locale: Option<String>,
    region: Option<Region>,
    environment: Environment,
    base_url: Option<String>,
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
            user_agent: None,
            locale: None,
            region: None,
            environment: Environment::Production,
            base_url: None,
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
            .field("locale", &self.locale)
            .field("region", &self.region)
            .field("environment", &self.environment)
            .field("base_url", &self.base_url)
            .field("http_client", &self.http_client.is_some())
            .finish_non_exhaustive()
    }
}

impl ClientBuilder {
    /// Sets your API token. Required. It is sent verbatim, and the client keeps it only in memory.
    pub fn token(mut self, token: impl Into<String>) -> Self {
        self.token = Some(token.into());
        self
    }

    /// Sets the `User-Agent`. Required, in the form `BM-{Company}-{Integration};contact@example.com`.
    pub fn user_agent(mut self, user_agent: impl Into<String>) -> Self {
        self.user_agent = Some(user_agent.into());
        self
    }

    /// Sets the locale sent as `Accept-Language` on every call, for example `fr-fr`. Required.
    pub fn locale(mut self, locale: impl Into<String>) -> Self {
        self.locale = Some(locale.into());
        self
    }

    /// Selects the marketplace region. Set this or [`base_url`](Self::base_url).
    pub fn region(mut self, region: Region) -> Self {
        self.region = Some(region);
        self
    }

    /// Selects production, the default, or preprod.
    pub fn environment(mut self, environment: Environment) -> Self {
        self.environment = environment;
        self
    }

    /// Sets a server root, for tests against a mock. Your token is sent to it.
    pub fn base_url(mut self, base_url: impl Into<String>) -> Self {
        self.base_url = Some(base_url.into());
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
    /// `reqwest::redirect::Policy::none()` to keep your token on the server you selected, as the
    /// default client does. Under reqwest's default policy, a 307 or 308 to the same host resends
    /// a write's body, token included, so a refund or other write can be repeated.
    ///
    /// The client retries only GETs after a failure, but a retry policy set with
    /// `reqwest::ClientBuilder::retry` runs inside your client, below that rule, and can resend a
    /// write. Leave it unset, or limit it to GETs.
    pub fn http_client(mut self, client: reqwest::Client) -> Self {
        self.http_client = Some(client);
        self
    }

    fn server(&self) -> Result<String, BuildError> {
        match (self.region, &self.base_url) {
            (Some(region), None) => Ok(server(region, self.environment).to_owned()),
            (None, Some(base_url)) => {
                let parsed = url::Url::parse(base_url)
                    .map_err(|_| invalid("the base URL must be absolute"))?;
                if !parsed.has_host() {
                    return Err(invalid("the base URL must be absolute"));
                }
                Ok(base_url.trim_end_matches('/').to_owned())
            }
            _ => Err(invalid("set exactly one of region and base_url")),
        }
    }

    /// Builds the client.
    pub fn build(self) -> Result<Client, BuildError> {
        let required = |value: &Option<String>, message: &str| match value.as_deref() {
            Some(text) if !text.is_empty() => Ok(text.to_owned()),
            _ => Err(invalid(message)),
        };
        let token = required(&self.token, "the token is required")?;
        let user_agent = required(
            &self.user_agent,
            "user_agent is required; the API may refuse a request without it",
        )?;
        let locale = required(&self.locale, "locale is required")?;
        let transport = Transport::new(Settings {
            base_url: self.server()?,
            hosts: HashMap::new(),
            headers: headers(&user_agent, &locale)?,
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
        .map_err(|error| invalid(&error.to_string()))?;
        Ok(Client {
            transport: Arc::new(transport),
        })
    }
}

/// Calls the API. Cloning is cheap and shares the connection pool, and a client is safe to use
/// from many tasks at once. Its operations are grouped by resource, such as [`Client::orders`].
#[derive(Clone, Debug)]
pub struct Client {
    pub(crate) transport: Arc<Transport>,
}

impl Client {
    /// Starts configuring a client. Set [`token`](ClientBuilder::token),
    /// [`user_agent`](ClientBuilder::user_agent), [`locale`](ClientBuilder::locale) and a
    /// [`region`](ClientBuilder::region), then call [`build`](ClientBuilder::build).
    pub fn builder() -> ClientBuilder {
        ClientBuilder::default()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    const TOKEN: &str = "synthetic-token";

    fn builder() -> ClientBuilder {
        Client::builder()
            .token(TOKEN)
            .user_agent("BM-Example-Test;test@example.com")
            .locale("fr-fr")
    }

    #[test]
    fn exactly_one_of_region_and_base_url() {
        assert!(builder().build().is_err());
        assert!(
            builder()
                .region(Region::Eu)
                .base_url("http://127.0.0.1")
                .build()
                .is_err()
        );
        assert!(builder().base_url("not a url").build().is_err());
        assert!(builder().region(Region::Eu).build().is_ok());
    }

    #[test]
    fn the_token_user_agent_and_locale_are_required() {
        let missing = [
            Client::builder().user_agent("ua").locale("fr-fr"),
            Client::builder().token(TOKEN).locale("fr-fr"),
            Client::builder().token(TOKEN).user_agent("ua"),
            builder().token(""),
        ];
        for builder in missing {
            assert!(builder.region(Region::Eu).build().is_err());
        }
    }

    #[test]
    fn a_caller_can_supply_the_http_client() {
        let client = builder()
            .region(Region::Eu)
            .http_client(reqwest::Client::new())
            .build();
        assert!(client.is_ok());
    }

    #[test]
    fn debug_output_never_shows_the_token() {
        let builder = builder().region(Region::Na);
        let client = builder.clone().build().unwrap();
        for text in [format!("{builder:?}"), format!("{client:?}")] {
            assert!(!text.contains(TOKEN), "{text}");
        }
    }
}
