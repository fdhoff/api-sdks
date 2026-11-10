use std::collections::HashMap;
use std::fmt;
use std::sync::Arc;
use std::time::Duration;

use base64::Engine;
use reqwest::header::{ACCEPT, AUTHORIZATION, HeaderMap, HeaderName, HeaderValue, USER_AGENT};

use crate::errors::to_error;
use crate::runtime::{Settings, StaticCredentials, Transport};

const API_PATH: &str = "/api/v1";
const OTP: HeaderName = HeaderName::from_static("x-gitea-otp");
const SUDO: HeaderName = HeaderName::from_static("sudo");

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

fn secret_header(value: &str, name: &str) -> Result<HeaderValue, BuildError> {
    let mut header = HeaderValue::from_str(value)
        .map_err(|_| invalid(format!("the {name} cannot be sent as a header")))?;
    header.set_sensitive(true);
    Ok(header)
}

#[derive(Clone)]
enum Login {
    Token(String),
    Basic { username: String, password: String },
}

// TODO: OAuth2 bearer tokens, if users ask.
fn credentials(
    login: Login,
    otp: Option<String>,
    sudo: Option<String>,
) -> Result<StaticCredentials, BuildError> {
    let mut headers = HeaderMap::new();
    let mut secrets = Vec::new();
    match login {
        Login::Token(token) => {
            if otp.is_some() {
                return Err(invalid(
                    "the one-time password goes only with a username and password",
                ));
            }
            headers.insert(
                AUTHORIZATION,
                secret_header(&format!("token {token}"), "token")?,
            );
            secrets.push(token);
        }
        Login::Basic { username, password } => {
            if username.is_empty() || password.is_empty() {
                return Err(invalid("the username and password must not be empty"));
            }
            let encoded =
                base64::engine::general_purpose::STANDARD.encode(format!("{username}:{password}"));
            headers.insert(
                AUTHORIZATION,
                secret_header(&format!("Basic {encoded}"), "username or password")?,
            );
            secrets.extend([password, encoded]);
        }
    }
    if let Some(otp) = otp {
        if otp.is_empty() {
            return Err(invalid("the one-time password must not be empty"));
        }
        headers.insert(OTP, secret_header(&otp, "one-time password")?);
        secrets.push(otp);
    }
    if let Some(sudo) = sudo {
        let value = HeaderValue::from_str(&sudo)
            .ok()
            .filter(|_| !sudo.is_empty())
            .ok_or_else(|| invalid("the sudo user must be a non-empty header value"))?;
        headers.insert(SUDO, value);
    }
    Ok(StaticCredentials::new(headers, secrets))
}

/// Configures a [`Client`]. Start from [`Client::builder`].
#[derive(Clone)]
pub struct ClientBuilder {
    base_url: Option<String>,
    login: Option<Login>,
    logins: usize,
    otp: Option<String>,
    sudo: Option<String>,
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
            login: None,
            logins: 0,
            otp: None,
            sudo: None,
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
            .field("sudo", &self.sudo)
            .field("user_agent", &self.user_agent)
            .field("http_client", &self.http_client.is_some())
            .finish_non_exhaustive()
    }
}

impl ClientBuilder {
    /// Sets your Gitea instance's URL, such as `https://gitea.example.com`, or
    /// `https://example.com/git` for an instance under a sub-path. Required, with no default. The
    /// client adds `/api/v1`, so leave it out. Your credentials are sent to it.
    pub fn base_url(mut self, base_url: impl Into<String>) -> Self {
        self.base_url = Some(base_url.into());
        self
    }

    /// Sets an access token, made under Settings → Applications on your instance. It is sent as
    /// `Authorization: token <token>`. Set this or [`basic_auth`](Self::basic_auth).
    pub fn token(mut self, token: impl Into<String>) -> Self {
        self.login = Some(Login::Token(token.into()));
        self.logins += 1;
        self
    }

    /// Sets a username and password, sent with Basic authentication. Set this or
    /// [`token`](Self::token).
    pub fn basic_auth(mut self, username: impl Into<String>, password: impl Into<String>) -> Self {
        self.login = Some(Login::Basic {
            username: username.into(),
            password: password.into(),
        });
        self.logins += 1;
        self
    }

    /// Sets a current one-time password, sent as `X-GITEA-OTP` with
    /// [`basic_auth`](Self::basic_auth), when your account has two-factor authentication on. It
    /// expires within a minute.
    pub fn otp(mut self, otp: impl Into<String>) -> Self {
        self.otp = Some(otp.into());
        self
    }

    /// Sets a user to act as, sent as `Sudo`. Needs an admin's credentials.
    pub fn sudo(mut self, username: impl Into<String>) -> Self {
        self.sudo = Some(username.into());
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
    /// `reqwest::redirect::Policy::none()` to keep your credentials on your base URL, as the
    /// default client does.
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

    fn api_url(&self) -> Result<String, BuildError> {
        let Some(base_url) = self.base_url.as_deref().filter(|url| !url.is_empty()) else {
            return Err(invalid(
                "the base URL is required: your Gitea instance's URL, such as https://gitea.example.com",
            ));
        };
        let parsed = url::Url::parse(base_url)
            .map_err(|_| invalid("the base URL must be an absolute http or https URL"))?;
        if !matches!(parsed.scheme(), "http" | "https") || !parsed.has_host() {
            return Err(invalid(
                "the base URL must be an absolute http or https URL",
            ));
        }
        let root = base_url.trim_end_matches('/');
        if root.ends_with(API_PATH) {
            return Err(invalid(format!(
                "the base URL is the instance's; leave out {API_PATH}, which the client adds"
            )));
        }
        Ok(format!("{root}{API_PATH}"))
    }

    fn login(&self) -> Result<Login, BuildError> {
        match (&self.login, self.logins) {
            (Some(Login::Token(token)), 1) if token.is_empty() => {
                Err(invalid("the token must not be empty"))
            }
            (Some(login), 1) => Ok(login.clone()),
            _ => Err(invalid("set exactly one of token and basic_auth")),
        }
    }

    /// Builds the client.
    pub fn build(self) -> Result<Client, BuildError> {
        let base_url = self.api_url()?;
        let credentials = credentials(self.login()?, self.otp.clone(), self.sudo.clone())?;
        let transport = Transport::new(Settings {
            base_url,
            hosts: HashMap::new(),
            headers: self.headers()?,
            header_defaults: HashMap::new(),
            query_defaults: HashMap::new(),
            credentials: Arc::new(credentials),
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

/// Calls a Gitea instance's API. Unofficial; not affiliated with, endorsed by or sponsored by the
/// Gitea project or Gitea Limited. Cloning is cheap and shares the connection pool, and a client is
/// safe to use from many tasks at once. Its operations are grouped by area, such as
/// [`Client::repos`].
#[derive(Clone, Debug)]
pub struct Client {
    pub(crate) transport: Arc<Transport>,
}

impl Client {
    /// Starts configuring a client. Set [`base_url`](ClientBuilder::base_url) and either
    /// [`token`](ClientBuilder::token) or [`basic_auth`](ClientBuilder::basic_auth), then call
    /// [`build`](ClientBuilder::build).
    pub fn builder() -> ClientBuilder {
        ClientBuilder::default()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    const TOKEN: &str = "unit-synthetic-access-token";
    const PASSWORD: &str = "unit-synthetic-password";

    fn builder() -> ClientBuilder {
        Client::builder()
            .base_url("https://gitea.example.test")
            .token(TOKEN)
    }

    #[test]
    fn the_base_url_and_one_login_are_required() {
        assert!(builder().build().is_ok());
        let error = Client::builder().token(TOKEN).build().unwrap_err();
        assert!(
            error.to_string().starts_with("the base URL is required"),
            "{error}"
        );
        assert!(builder().base_url("").build().is_err());
        assert!(builder().token("").build().is_err());
        let no_login = Client::builder().base_url("https://gitea.example.test");
        assert!(no_login.clone().build().is_err());
        assert!(
            builder()
                .basic_auth("synthetic-user", PASSWORD)
                .build()
                .is_err()
        );
        assert!(builder().token(TOKEN).build().is_err());
        assert!(no_login.clone().basic_auth("", PASSWORD).build().is_err());
        assert!(no_login.basic_auth("synthetic-user", "").build().is_err());
    }

    #[test]
    fn the_client_adds_the_api_path() {
        let cases = [
            (
                "https://gitea.example.test",
                "https://gitea.example.test/api/v1",
            ),
            (
                "https://gitea.example.test/",
                "https://gitea.example.test/api/v1",
            ),
            (
                "https://example.test/git",
                "https://example.test/git/api/v1",
            ),
            (
                "http://127.0.0.1:3000/git/",
                "http://127.0.0.1:3000/git/api/v1",
            ),
        ];
        for (base, api) in cases {
            assert_eq!(builder().base_url(base).api_url().unwrap(), api, "{base}");
        }
    }

    #[test]
    fn the_base_url_must_be_the_instances() {
        for url in [
            "/api",
            "gitea.example.test",
            "ftp://gitea.example.test",
            "https://gitea.example.test/api/v1",
            "https://gitea.example.test/api/v1/",
        ] {
            assert!(builder().base_url(url).build().is_err(), "{url}");
        }
    }

    #[test]
    fn otp_goes_only_with_basic() {
        assert!(builder().otp("123456").build().is_err());
        let basic = Client::builder()
            .base_url("https://gitea.example.test")
            .basic_auth("synthetic-user", PASSWORD);
        assert!(basic.clone().otp("123456").build().is_ok());
        assert!(basic.otp("").build().is_err());
    }

    #[test]
    fn sudo_must_be_a_header_value() {
        assert!(builder().sudo("synthetic-other-user").build().is_ok());
        assert!(builder().sudo("").build().is_err());
        assert!(builder().sudo("line\nbreak").build().is_err());
    }

    #[test]
    fn a_token_that_is_not_a_header_value_is_refused() {
        assert!(builder().token("line\nbreak").build().is_err());
    }

    #[test]
    fn debug_output_never_shows_a_credential() {
        let builder = Client::builder()
            .base_url("https://gitea.example.test")
            .basic_auth("synthetic-user", PASSWORD)
            .otp("730194");
        let client = builder.clone().build().unwrap();
        for text in [format!("{builder:?}"), format!("{client:?}")] {
            for secret in [PASSWORD, "730194", "c3ludGhldGljLXVzZXI6"] {
                assert!(!text.contains(secret), "{text}");
            }
        }
    }
}
