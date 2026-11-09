use std::collections::HashMap;
use std::fmt;
use std::sync::Arc;
use std::time::Duration;

use reqwest::header::{ACCEPT, HeaderMap, HeaderValue, USER_AGENT};

use crate::errors::to_error;
use crate::oauth::{API_SCOPE, Config, EbayCredentials, OAuth, OnToken, Token};
use crate::runtime::{Settings, Transport, select_hosts};
#[cfg(feature = "signing")]
use crate::signing::SigningKey;

/// The base URL of each host the APIs use, by environment.
pub const ENVIRONMENTS: &[(&str, &[(&str, &str)])] = &[
    (
        "production",
        &[
            ("api", "https://api.ebay.com"),
            ("apiz", "https://apiz.ebay.com"),
            ("apim", "https://apim.ebay.com"),
        ],
    ),
    (
        "sandbox",
        &[
            ("api", "https://api.sandbox.ebay.com"),
            ("apiz", "https://apiz.sandbox.ebay.com"),
            ("apim", "https://apim.sandbox.ebay.com"),
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

fn non_empty(value: Option<String>) -> Option<String> {
    value.filter(|text| !text.is_empty())
}

/// Configures a [`Client`]. Start from [`Client::builder`].
#[derive(Clone)]
pub struct ClientBuilder {
    client_id: Option<String>,
    client_secret: Option<String>,
    ru_name: Option<String>,
    app_token: Option<String>,
    user_token: Option<String>,
    refresh_token: Option<String>,
    on_token: Option<OnToken>,
    app_scopes: Vec<String>,
    user_scopes: Vec<String>,
    environment: String,
    hosts: Option<HashMap<String, String>>,
    marketplace_id: Option<String>,
    content_language: Option<String>,
    #[cfg(feature = "signing")]
    signing_key: Option<SigningKey>,
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
            client_id: None,
            client_secret: None,
            ru_name: None,
            app_token: None,
            user_token: None,
            refresh_token: None,
            on_token: None,
            app_scopes: vec![API_SCOPE.to_owned()],
            user_scopes: Vec::new(),
            environment: "production".to_owned(),
            hosts: None,
            marketplace_id: None,
            content_language: None,
            #[cfg(feature = "signing")]
            signing_key: None,
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
            .field("client_id", &self.client_id)
            .field("ru_name", &self.ru_name)
            .field("environment", &self.environment)
            .field("hosts", &self.hosts)
            .field("marketplace_id", &self.marketplace_id)
            .field("content_language", &self.content_language)
            .field("user_agent", &self.user_agent)
            .field("on_token", &self.on_token.is_some())
            .field("http_client", &self.http_client.is_some())
            .finish_non_exhaustive()
    }
}

impl ClientBuilder {
    /// Sets your keyset's App ID. With [`client_secret`](Self::client_secret), the client mints
    /// application tokens itself and can exchange and refresh user tokens.
    pub fn client_id(mut self, client_id: impl Into<String>) -> Self {
        self.client_id = Some(client_id.into());
        self
    }

    /// Sets your keyset's Cert ID. The client keeps it only in memory.
    pub fn client_secret(mut self, client_secret: impl Into<String>) -> Self {
        self.client_secret = Some(client_secret.into());
        self
    }

    /// Sets your app's redirect URL name, for the authorization code grant.
    pub fn ru_name(mut self, ru_name: impl Into<String>) -> Self {
        self.ru_name = Some(ru_name.into());
        self
    }

    /// Sets an application token to use instead of minting one.
    pub fn app_token(mut self, app_token: impl Into<String>) -> Self {
        self.app_token = Some(app_token.into());
        self
    }

    /// Sets a user access token, sent on operations that need a seller's consent.
    pub fn user_token(mut self, user_token: impl Into<String>) -> Self {
        self.user_token = Some(user_token.into());
        self
    }

    /// Sets a refresh token, so that the client can replace an expired user token by itself, once
    /// per call.
    pub fn refresh_token(mut self, refresh_token: impl Into<String>) -> Self {
        self.refresh_token = Some(refresh_token.into());
        self
    }

    /// Called with every new user token, from [`OAuth::exchange_code`] and every refresh, so you
    /// can store it. It runs before the call that needed the refresh is retried, so keep it quick:
    /// send the token to a channel, for example. It runs while the client holds its token locks,
    /// so it must not wait on this client: blocking on [`OAuth::refresh`] or a call from it
    /// deadlocks.
    pub fn on_token(mut self, on_token: impl Fn(&Token) + Send + Sync + 'static) -> Self {
        self.on_token = Some(Arc::new(on_token));
        self
    }

    /// Sets the scopes of minted application tokens. The default is [`API_SCOPE`]. The client
    /// fails to build without at least one.
    pub fn app_scopes<S: Into<String>>(mut self, scopes: impl IntoIterator<Item = S>) -> Self {
        self.app_scopes = scopes.into_iter().map(Into::into).collect();
        self
    }

    /// Sets the scopes to ask for when refreshing a user token. eBay keeps the original grant's
    /// when none are set.
    pub fn user_scopes<S: Into<String>>(mut self, scopes: impl IntoIterator<Item = S>) -> Self {
        self.user_scopes = scopes.into_iter().map(Into::into).collect();
        self
    }

    /// Selects `production`, the default, or `sandbox`.
    pub fn environment(mut self, environment: impl Into<String>) -> Self {
        self.environment = environment.into();
        self
    }

    /// Sets your own base URL for each of `api`, `apiz` and `apim`, such as a mock's, instead of
    /// the environment's. Your credentials are sent to them.
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

    /// Sent as `X-EBAY-C-MARKETPLACE-ID` on operations that take it, unless a call sets its own.
    pub fn marketplace_id(mut self, marketplace_id: impl Into<String>) -> Self {
        self.marketplace_id = Some(marketplace_id.into());
        self
    }

    /// Sent as `Content-Language` on operations that take it, unless a call sets its own.
    pub fn content_language(mut self, content_language: impl Into<String>) -> Self {
        self.content_language = Some(content_language.into());
        self
    }

    /// Signs every request, as eBay requires of EU and UK sellers on some calls.
    #[cfg(feature = "signing")]
    pub fn signing_key(mut self, signing_key: SigningKey) -> Self {
        self.signing_key = Some(signing_key);
        self
    }

    /// Sets the `User-Agent`. None is sent unless you set one.
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
    /// `reqwest::redirect::Policy::none()` to keep your credentials on the hosts you selected, as
    /// the default client does.
    ///
    /// The client retries only GETs after a failure, but a retry policy set with
    /// `reqwest::ClientBuilder::retry` runs inside your client, below that rule, and can resend a
    /// write. Leave it unset, or limit it to GETs.
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

    fn header_defaults(&self) -> HashMap<String, String> {
        [
            ("X-EBAY-C-MARKETPLACE-ID", &self.marketplace_id),
            ("Content-Language", &self.content_language),
        ]
        .into_iter()
        .filter_map(|(name, value)| Some((name.to_owned(), non_empty(value.clone())?)))
        .collect()
    }

    /// Builds the client.
    pub fn build(self) -> Result<Client, BuildError> {
        let client_id = non_empty(self.client_id.clone());
        let client_secret = non_empty(self.client_secret.clone());
        if client_id.is_some() != client_secret.is_some() {
            return Err(invalid("set client_id and client_secret together"));
        }
        let (app_token, user_token, refresh_token) = (
            non_empty(self.app_token.clone()),
            non_empty(self.user_token.clone()),
            non_empty(self.refresh_token.clone()),
        );
        if client_id.is_none()
            && app_token.is_none()
            && user_token.is_none()
            && refresh_token.is_none()
        {
            return Err(invalid("set client_id and client_secret, or a token"));
        }
        if self.app_scopes.iter().all(|scope| scope.trim().is_empty()) {
            return Err(invalid("app_scopes needs at least one scope"));
        }
        let hosts = self.hosts_map()?;
        let config = Config {
            client_id,
            client_secret,
            ru_name: non_empty(self.ru_name.clone()),
            app_token,
            user_token,
            refresh_token,
            on_token: self.on_token.clone(),
            app_scopes: self.app_scopes.clone(),
            user_scopes: self.user_scopes.clone(),
            environment: self.environment.clone(),
            #[cfg(feature = "signing")]
            signer: self
                .signing_key
                .as_ref()
                .map(SigningKey::signer)
                .transpose()
                .map_err(invalid)?,
        };
        let credentials = Arc::new(EbayCredentials::new(config).map_err(|_| {
            invalid("the client ID, client secret and tokens must be printable text")
        })?);
        let transport = Transport::new(Settings {
            base_url: hosts["api"].clone(),
            hosts,
            headers: self.headers()?,
            header_defaults: self.header_defaults(),
            query_defaults: HashMap::new(),
            credentials: credentials.clone(),
            to_error,
            timeout: self.timeout,
            max_retries: self.max_retries,
            retry_base_delay: self.retry_base_delay,
            rate_limit_wait: self.rate_limit_wait,
            max_retry_wait: self.max_retry_wait,
            http: self.http_client,
        })
        .map_err(|error| invalid(error.to_string()))?;
        let transport = Arc::new(transport);
        credentials.attach(&transport);
        Ok(Client {
            transport,
            credentials,
        })
    }
}

/// Calls every API in this crate. Cloning is cheap and shares the connection pool and the tokens,
/// and a client is safe to use from many tasks at once. Each API has a method, such as
/// [`Client::inventory`], whose resources hold the operations, and OAuth is on [`Client::oauth`].
#[derive(Clone, Debug)]
pub struct Client {
    transport: Arc<Transport>,
    credentials: Arc<EbayCredentials>,
}

impl Client {
    /// Starts configuring a client. Set [`client_id`](ClientBuilder::client_id) and
    /// [`client_secret`](ClientBuilder::client_secret), or a token, then call
    /// [`build`](ClientBuilder::build).
    pub fn builder() -> ClientBuilder {
        ClientBuilder::default()
    }

    /// OAuth 2: application tokens, the authorization URL, code exchange and refresh.
    pub fn oauth(&self) -> OAuth {
        OAuth::new(self.credentials.clone(), self.transport.clone())
    }

    /// The Account API v1.
    pub fn account(&self) -> crate::account::Resources {
        crate::account::Resources::new(self.transport.clone())
    }

    /// The Account API v2.
    pub fn account_v2(&self) -> crate::account_v2::Resources {
        crate::account_v2::Resources::new(self.transport.clone())
    }

    /// The Analytics API.
    pub fn analytics(&self) -> crate::analytics::Resources {
        crate::analytics::Resources::new(self.transport.clone())
    }

    /// The Feed API.
    pub fn feed(&self) -> crate::feed::Resources {
        crate::feed::Resources::new(self.transport.clone())
    }

    /// The Finances API.
    pub fn finances(&self) -> crate::finances::Resources {
        crate::finances::Resources::new(self.transport.clone())
    }

    /// The Fulfillment API.
    pub fn fulfillment(&self) -> crate::fulfillment::Resources {
        crate::fulfillment::Resources::new(self.transport.clone())
    }

    /// The Inventory API.
    pub fn inventory(&self) -> crate::inventory::Resources {
        crate::inventory::Resources::new(self.transport.clone())
    }

    /// The Marketing API.
    pub fn marketing(&self) -> crate::marketing::Resources {
        crate::marketing::Resources::new(self.transport.clone())
    }

    /// The Metadata API.
    pub fn metadata(&self) -> crate::metadata::Resources {
        crate::metadata::Resources::new(self.transport.clone())
    }

    /// The Negotiation API.
    pub fn negotiation(&self) -> crate::negotiation::Resources {
        crate::negotiation::Resources::new(self.transport.clone())
    }

    /// The Recommendation API.
    pub fn recommendation(&self) -> crate::recommendation::Resources {
        crate::recommendation::Resources::new(self.transport.clone())
    }

    /// The Stores API.
    pub fn stores(&self) -> crate::stores::Resources {
        crate::stores::Resources::new(self.transport.clone())
    }

    /// The Post-Order API: cancellations, returns, item-not-received inquiries and cases.
    pub fn post_order(&self) -> crate::post_order::Resources {
        crate::post_order::Resources::new(self.transport.clone())
    }

    /// The Feedback API.
    pub fn feedback(&self) -> crate::feedback::Resources {
        crate::feedback::Resources::new(self.transport.clone())
    }

    /// The Identity API.
    pub fn identity(&self) -> crate::identity::Resources {
        crate::identity::Resources::new(self.transport.clone())
    }

    /// The Media API.
    pub fn media(&self) -> crate::media::Resources {
        crate::media::Resources::new(self.transport.clone())
    }

    /// The Message API.
    pub fn message(&self) -> crate::message::Resources {
        crate::message::Resources::new(self.transport.clone())
    }

    /// The Notification API.
    pub fn notification(&self) -> crate::notification::Resources {
        crate::notification::Resources::new(self.transport.clone())
    }

    /// The Taxonomy API.
    pub fn taxonomy(&self) -> crate::taxonomy::Resources {
        crate::taxonomy::Resources::new(self.transport.clone())
    }

    /// The Developer Analytics API.
    pub fn developer_analytics(&self) -> crate::developer_analytics::Resources {
        crate::developer_analytics::Resources::new(self.transport.clone())
    }

    /// The Key Management API.
    pub fn key_management(&self) -> crate::key_management::Resources {
        crate::key_management::Resources::new(self.transport.clone())
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn builder() -> ClientBuilder {
        Client::builder()
            .client_id("synthetic-app-id")
            .client_secret("synthetic-cert-id")
    }

    #[test]
    fn credentials_are_required_and_the_keyset_comes_whole() {
        assert!(Client::builder().build().is_err());
        assert!(
            Client::builder()
                .client_id("synthetic-app-id")
                .build()
                .is_err()
        );
        assert!(
            Client::builder()
                .client_secret("synthetic-cert-id")
                .user_token("t")
                .build()
                .is_err()
        );
        assert!(builder().build().is_ok());
        assert!(
            Client::builder()
                .user_token("synthetic-user")
                .build()
                .is_ok()
        );
        assert!(Client::builder().app_token("synthetic-app").build().is_ok());
    }

    #[test]
    fn app_scopes_cannot_be_empty() {
        for scopes in [Vec::new(), vec![""], vec![" "]] {
            let error = builder().app_scopes(scopes).build().unwrap_err();
            assert_eq!(error.to_string(), "app_scopes needs at least one scope");
        }
        assert!(builder().app_scopes([API_SCOPE]).build().is_ok());
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
            ("api", "http://127.0.0.1:4010/"),
            ("apiz", "http://127.0.0.1:4010"),
            ("apim", "http://127.0.0.1:4010"),
        ];
        assert!(builder().hosts(mock).build().is_ok());
        assert_eq!(
            builder()
                .hosts([("api", "http://127.0.0.1:4010")])
                .build()
                .unwrap_err()
                .to_string(),
            "hosts lacks keys: apim, apiz"
        );
        let relative = [
            ("api", "/api"),
            ("apiz", "http://127.0.0.1:4010"),
            ("apim", "http://127.0.0.1:4010"),
        ];
        assert!(builder().hosts(relative).build().is_err());
    }

    #[test]
    fn empty_header_defaults_are_not_sent() {
        let builder = builder().marketplace_id("EBAY_GB").content_language("");
        assert_eq!(
            builder.header_defaults(),
            HashMap::from([("X-EBAY-C-MARKETPLACE-ID".to_owned(), "EBAY_GB".to_owned())])
        );
    }

    #[test]
    fn debug_output_never_shows_a_secret() {
        let builder = builder()
            .app_token("synthetic-minted")
            .user_token("synthetic-user")
            .refresh_token("synthetic-refresh");
        let client = builder.clone().build().unwrap();
        for text in [
            format!("{builder:?}"),
            format!("{client:?}"),
            format!("{:?}", client.oauth()),
        ] {
            for secret in [
                "synthetic-cert-id",
                "synthetic-minted",
                "synthetic-user",
                "synthetic-refresh",
            ] {
                assert!(!text.contains(secret), "{text}");
            }
        }
    }
}
