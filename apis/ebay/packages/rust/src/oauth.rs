//! OAuth 2 as eBay implements it: application tokens from the client credentials grant, and user
//! tokens from the authorization code grant, both from one token endpoint with HTTP Basic client
//! authentication.

use std::collections::VecDeque;
use std::fmt;
use std::sync::{Arc, Mutex, OnceLock, PoisonError, RwLock, Weak};
use std::time::{Duration, Instant};

use base64::Engine;
use base64::engine::general_purpose::{STANDARD, URL_SAFE_NO_PAD};
use futures_core::future::BoxFuture;
use reqwest::header::{AUTHORIZATION, HeaderValue};
use serde_json::Value;

use crate::runtime::{AuthRequest, Credentials, Operation, Request, Transport};
#[cfg(feature = "signing")]
use crate::signing::Signer;
use crate::{Error, ErrorKind};

/// The scope of an application token, which the public operations accept.
pub const API_SCOPE: &str = "https://api.ebay.com/oauth/api_scope";

/// The scopes eBay's client credentials grant gives. An operation that accepts any of them takes an
/// application token, and every other operation a user token.
const APP_SCOPES: &[&str] = &[
    API_SCOPE,
    "https://api.ebay.com/oauth/api_scope/metadata.insights",
];

const AUTHORIZATION_URLS: &[(&str, &str)] = &[
    ("production", "https://auth.ebay.com/oauth2/authorize"),
    ("sandbox", "https://auth.sandbox.ebay.com/oauth2/authorize"),
];

/// An application token this close to expiry is replaced before use.
const EXPIRY_MARGIN: Duration = Duration::from_secs(60);
const REMEMBERED: usize = 16;

static TOKEN: Operation = Operation {
    id: "oauthToken",
    method: "POST",
    path: "/identity/v1/oauth2/token",
    query_params: &[],
    returns_json: true,
    paging: None,
    security: &[],
};

pub(crate) type OnToken = Arc<dyn Fn(&Token) + Send + Sync>;

/// An access token, and for a user token the refresh token that replaces it. eBay's refresh returns
/// a new access token only, so the refresh token carries over. Debug output hides both tokens.
#[derive(Clone, PartialEq, Eq)]
pub struct Token {
    pub access_token: String,
    /// Seconds until the access token expires, when the response says.
    pub expires_in: Option<i64>,
    pub refresh_token: Option<String>,
    /// Seconds until the refresh token expires, when the response says.
    pub refresh_token_expires_in: Option<i64>,
    pub token_type: String,
}

impl fmt::Debug for Token {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("Token")
            .field("access_token", &"***")
            .field("expires_in", &self.expires_in)
            .field("refresh_token", &self.refresh_token.as_ref().map(|_| "***"))
            .field("refresh_token_expires_in", &self.refresh_token_expires_in)
            .field("token_type", &self.token_type)
            .finish()
    }
}

impl Token {
    fn access(access_token: String) -> Self {
        Self {
            access_token,
            expires_in: None,
            refresh_token: None,
            refresh_token_expires_in: None,
            token_type: "Bearer".to_owned(),
        }
    }
}

/// Send the user to `url`. Keep `state` until eBay redirects to your RuName's accept URL, check
/// that the redirect's `state` matches, then pass its `code` to [`OAuth::exchange_code`].
#[derive(Clone, Debug, PartialEq, Eq)]
pub struct AuthorizationRequest {
    pub url: String,
    pub state: String,
}

fn invalid_input(message: impl Into<String>) -> Error {
    Error::new(ErrorKind::InvalidInput, message)
}

fn random_state() -> Result<String, Error> {
    let mut buffer = [0; 32];
    getrandom::fill(&mut buffer).map_err(|error| {
        Error::new(
            ErrorKind::System,
            format!("no random bytes are available: {error}"),
        )
    })?;
    Ok(URL_SAFE_NO_PAD.encode(buffer))
}

/// Builds the URL that asks a user to grant your app `scopes`, with a fresh state unless you pass
/// your own. `ru_name` is your app's redirect URL name, which eBay takes as `redirect_uri`.
/// `environment` is `production` or `sandbox`. Pass `prompt` `login` to make the user sign in even
/// if they already are.
pub fn authorization_url(
    client_id: &str,
    ru_name: &str,
    scopes: &[&str],
    environment: &str,
    state: Option<&str>,
    prompt: Option<&str>,
) -> Result<AuthorizationRequest, Error> {
    if scopes.is_empty() {
        return Err(invalid_input("request at least one scope"));
    }
    let Some((_, base)) = AUTHORIZATION_URLS
        .iter()
        .find(|(name, _)| *name == environment)
    else {
        let known: Vec<&str> = AUTHORIZATION_URLS.iter().map(|(name, _)| *name).collect();
        return Err(invalid_input(format!(
            "unknown environment {environment}; expected one of: {}",
            known.join(", ")
        )));
    };
    let state = match state {
        Some(state) => state.to_owned(),
        None => random_state()?,
    };
    let mut query = url::form_urlencoded::Serializer::new(String::new());
    query
        .append_pair("client_id", client_id)
        .append_pair("redirect_uri", ru_name)
        .append_pair("response_type", "code")
        .append_pair("scope", &scopes.join(" "))
        .append_pair("state", &state);
    if let Some(prompt) = prompt {
        query.append_pair("prompt", prompt);
    }
    Ok(AuthorizationRequest {
        url: format!("{base}?{}", query.finish()),
        state,
    })
}

/// eBay lists the scopes an operation accepts, any one of which is enough.
fn takes_app_token(operation: &Operation) -> bool {
    operation
        .security
        .iter()
        .flat_map(|schemes| schemes.iter())
        .flat_map(|scheme| scheme.scopes.iter())
        .any(|scope| APP_SCOPES.contains(scope))
}

fn header(text: &str) -> Result<HeaderValue, Error> {
    let mut value = HeaderValue::from_str(text)
        .map_err(|_| invalid_input("a credential cannot be sent as a header"))?;
    value.set_sensitive(true);
    Ok(value)
}

fn parse_token(reply: &Value) -> Result<Token, Error> {
    let text = |name: &str| {
        reply
            .get(name)
            .and_then(Value::as_str)
            .filter(|text| !text.is_empty())
            .map(str::to_owned)
    };
    let Some(access_token) = text("access_token") else {
        return Err(Error::new(
            ErrorKind::Decode,
            "the token response has no access token",
        ));
    };
    Ok(Token {
        access_token,
        expires_in: reply.get("expires_in").and_then(Value::as_i64),
        refresh_token: text("refresh_token"),
        refresh_token_expires_in: reply
            .get("refresh_token_expires_in")
            .and_then(Value::as_i64),
        token_type: text("token_type").unwrap_or_else(|| "Bearer".to_owned()),
    })
}

#[derive(Default)]
struct Tokens {
    app: Option<String>,
    /// When a minted application token expires. A token passed in has no known expiry.
    app_expires_at: Option<Instant>,
    user: Option<String>,
    refresh: Option<String>,
}

/// What the client was configured with, for the OAuth flows.
pub(crate) struct Config {
    pub(crate) client_id: Option<String>,
    pub(crate) client_secret: Option<String>,
    pub(crate) ru_name: Option<String>,
    pub(crate) app_token: Option<String>,
    pub(crate) user_token: Option<String>,
    pub(crate) refresh_token: Option<String>,
    pub(crate) on_token: Option<OnToken>,
    pub(crate) app_scopes: Vec<String>,
    pub(crate) user_scopes: Vec<String>,
    pub(crate) environment: String,
    #[cfg(feature = "signing")]
    pub(crate) signer: Option<Signer>,
}

/// Sends an application token on operations that accept one and a user token on the rest, then
/// signs the request when there is a signer. Mints an application token when there is none or it
/// is about to expire. After a 401, mints a new application token, or refreshes the user token
/// once when there is a refresh token.
pub(crate) struct EbayCredentials {
    client_id: Option<String>,
    client_secret: Option<String>,
    /// `Basic` and the base64 of the client ID and secret.
    basic: Option<String>,
    ru_name: Option<String>,
    app_scopes: Vec<String>,
    user_scopes: Vec<String>,
    environment: String,
    tokens: RwLock<Tokens>,
    /// Recent tokens and codes, so that none reaches a log or error.
    seen: Mutex<VecDeque<String>>,
    /// Serialises minting, so that concurrent calls share one new application token.
    minting: tokio::sync::Mutex<()>,
    /// Serialises user token requests, since a refresh may replace the refresh token.
    refreshing: tokio::sync::Mutex<()>,
    on_token: Option<OnToken>,
    #[cfg(feature = "signing")]
    signer: Option<Signer>,
    transport: OnceLock<Weak<Transport>>,
}

impl fmt::Debug for EbayCredentials {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.write_str("EbayCredentials(***)")
    }
}

impl EbayCredentials {
    pub(crate) fn new(config: Config) -> Result<Self, Error> {
        let basic = match (&config.client_id, &config.client_secret) {
            (Some(id), Some(secret)) => Some(format!(
                "Basic {}",
                STANDARD.encode(format!("{id}:{secret}"))
            )),
            _ => None,
        };
        for value in [&basic].into_iter().flatten() {
            header(value)?;
        }
        for token in [&config.app_token, &config.user_token]
            .into_iter()
            .flatten()
        {
            header(&format!("Bearer {token}"))?;
        }
        Ok(Self {
            client_id: config.client_id,
            client_secret: config.client_secret,
            basic,
            ru_name: config.ru_name,
            app_scopes: config.app_scopes,
            user_scopes: config.user_scopes,
            environment: config.environment,
            tokens: RwLock::new(Tokens {
                app: config.app_token,
                app_expires_at: None,
                user: config.user_token,
                refresh: config.refresh_token,
            }),
            seen: Mutex::new(VecDeque::new()),
            minting: tokio::sync::Mutex::new(()),
            refreshing: tokio::sync::Mutex::new(()),
            on_token: config.on_token,
            #[cfg(feature = "signing")]
            signer: config.signer,
            transport: OnceLock::new(),
        })
    }

    /// Lets the credentials call the token endpoint through the client's own transport.
    pub(crate) fn attach(&self, transport: &Arc<Transport>) {
        let _ = self.transport.set(Arc::downgrade(transport));
    }

    fn can_mint(&self) -> bool {
        self.basic.is_some()
    }

    fn read(&self) -> std::sync::RwLockReadGuard<'_, Tokens> {
        self.tokens.read().unwrap_or_else(PoisonError::into_inner)
    }

    fn write(&self) -> std::sync::RwLockWriteGuard<'_, Tokens> {
        self.tokens.write().unwrap_or_else(PoisonError::into_inner)
    }

    /// Keeps values out of logs and errors from now on. Only the most recent are kept, so a
    /// long-lived client does not grow.
    fn remember(&self, values: &[&str]) {
        let mut seen = self.seen.lock().unwrap_or_else(PoisonError::into_inner);
        seen.extend(
            values
                .iter()
                .filter(|value| !value.is_empty())
                .map(|value| (*value).to_owned()),
        );
        let excess = seen.len().saturating_sub(REMEMBERED);
        seen.drain(..excess);
    }

    /// The application token, unless it is about to expire.
    fn fresh_app_token(&self) -> Option<String> {
        let tokens = self.read();
        let fresh = tokens
            .app_expires_at
            .is_none_or(|expires| Instant::now() + EXPIRY_MARGIN < expires);
        tokens.app.clone().filter(|_| fresh)
    }

    fn transport(&self) -> Result<Arc<Transport>, Error> {
        self.transport.get().and_then(Weak::upgrade).ok_or_else(|| {
            Error::new(
                ErrorKind::InvalidInput,
                "the client that made these credentials is gone",
            )
        })
    }

    async fn request_token(
        &self,
        transport: &Transport,
        fields: &[(&str, &str)],
    ) -> Result<Token, Error> {
        if self.basic.is_none() {
            return Err(invalid_input(
                "a token request needs client_id and client_secret",
            ));
        }
        let mut request = Request::new(&TOKEN).host("api");
        for (name, value) in fields {
            request.urlencoded(name, &(*value).to_owned());
        }
        let reply: Value = transport.call(request).await?;
        parse_token(&reply)
    }

    fn store_app(&self, token: Token) -> Token {
        let mut tokens = self.write();
        if let Some(old) = tokens.app.take() {
            self.remember(&[&old]);
        }
        tokens.app = Some(token.access_token.clone());
        tokens.app_expires_at = token.expires_in.map(|seconds| {
            Instant::now() + Duration::from_secs(u64::try_from(seconds).unwrap_or_default())
        });
        token
    }

    /// Keeps the refresh token when the response has none, as eBay's refresh does not return one.
    fn store_user(&self, mut token: Token) -> Token {
        let (old_user, old_refresh) = {
            let tokens = self.read();
            (tokens.user.clone(), tokens.refresh.clone())
        };
        if token.refresh_token.is_none() {
            token.refresh_token.clone_from(&old_refresh);
        }
        self.remember(&[
            old_user.as_deref().unwrap_or_default(),
            old_refresh.as_deref().unwrap_or_default(),
        ]);
        {
            let mut tokens = self.write();
            tokens.user = Some(token.access_token.clone());
            tokens.refresh.clone_from(&token.refresh_token);
        }
        if let Some(on_token) = &self.on_token {
            on_token(&token);
        }
        token
    }

    /// Mints an application token, unless the current one is fresh and is not `stale`, the token a
    /// failed request sent.
    async fn mint(
        &self,
        transport: &Transport,
        force: bool,
        stale: Option<&str>,
    ) -> Result<Token, Error> {
        let _minting = self.minting.lock().await;
        if let Some(current) = self.fresh_app_token() {
            let replaced = stale.is_some_and(|stale| stale != current);
            if replaced || (!force && stale.is_none()) {
                return Ok(Token::access(current));
            }
        }
        let scopes = self.app_scopes.join(" ");
        let token = self
            .request_token(
                transport,
                &[("grant_type", "client_credentials"), ("scope", &scopes)],
            )
            .await?;
        Ok(self.store_app(token))
    }

    /// Refreshes the user token, unless another refresh replaced `stale` while this one waited.
    async fn refresh_user(
        &self,
        transport: &Transport,
        stale: Option<&str>,
        scopes: &[&str],
    ) -> Result<Token, Error> {
        let _refreshing = self.refreshing.lock().await;
        let (current, refresh) = {
            let tokens = self.read();
            (tokens.user.clone(), tokens.refresh.clone())
        };
        if let Some(current) = current.filter(|current| stale.is_some_and(|stale| stale != current))
        {
            return Ok(Token {
                refresh_token: refresh,
                ..Token::access(current)
            });
        }
        let Some(refresh) = refresh else {
            return Err(invalid_input(
                "there is no refresh token: set refresh_token, or exchange a code first",
            ));
        };
        let scopes = if scopes.is_empty() {
            self.user_scopes.join(" ")
        } else {
            scopes.join(" ")
        };
        let mut fields = vec![
            ("grant_type", "refresh_token"),
            ("refresh_token", refresh.as_str()),
        ];
        if !scopes.is_empty() {
            fields.push(("scope", &scopes));
        }
        let token = self.request_token(transport, &fields).await?;
        Ok(self.store_user(token))
    }

    async fn token_for(&self, operation: &'static Operation) -> Result<String, Error> {
        if takes_app_token(operation) {
            let token = match self.fresh_app_token() {
                Some(token) => Some(token),
                None if self.can_mint() => Some(
                    self.mint(&*self.transport()?, false, None)
                        .await?
                        .access_token,
                ),
                None => None,
            };
            return token.or_else(|| self.read().user.clone()).ok_or_else(|| {
                invalid_input(format!(
                    "{} needs an application token: set client_id and client_secret, or app_token",
                    operation.id
                ))
            });
        }
        self.read().user.clone().ok_or_else(|| {
            invalid_input(format!(
                "{} needs a user token: set user_token, or call oauth().exchange_code first",
                operation.id
            ))
        })
    }
}

/// The bearer token a request sent.
fn sent_token(request: &AuthRequest) -> Option<&str> {
    request
        .headers
        .get(AUTHORIZATION)?
        .to_str()
        .ok()?
        .strip_prefix("Bearer ")
}

impl Credentials for EbayCredentials {
    fn apply<'a>(&'a self, request: &'a mut AuthRequest) -> BoxFuture<'a, Result<(), Error>> {
        Box::pin(async move {
            if std::ptr::eq(request.operation, &TOKEN) {
                let basic = self.basic.as_deref().ok_or_else(|| {
                    invalid_input("a token request needs client_id and client_secret")
                })?;
                request.headers.insert(AUTHORIZATION, header(basic)?);
                return Ok(());
            }
            let token = self.token_for(request.operation).await?;
            request
                .headers
                .insert(AUTHORIZATION, header(&format!("Bearer {token}"))?);
            #[cfg(feature = "signing")]
            if let Some(signer) = &self.signer {
                signer.sign(request)?;
            }
            Ok(())
        })
    }

    fn secrets(&self) -> Vec<String> {
        let mut secrets: Vec<String> = [&self.client_secret, &self.basic]
            .into_iter()
            .flatten()
            .cloned()
            .collect();
        if let Some(basic) = &self.basic {
            secrets.push(basic.trim_start_matches("Basic ").to_owned());
        }
        {
            let tokens = self.read();
            secrets.extend(
                [&tokens.app, &tokens.user, &tokens.refresh]
                    .into_iter()
                    .flatten()
                    .cloned(),
            );
        }
        #[cfg(feature = "signing")]
        if let Some(signer) = &self.signer {
            secrets.extend(signer.secrets().iter().cloned());
        }
        secrets.extend(
            self.seen
                .lock()
                .unwrap_or_else(PoisonError::into_inner)
                .iter()
                .cloned(),
        );
        secrets.retain(|secret| !secret.is_empty());
        secrets
    }

    fn refresh<'a>(&'a self, request: &'a AuthRequest) -> BoxFuture<'a, Result<bool, Error>> {
        Box::pin(async move {
            let stale = sent_token(request);
            let has_app = self.read().app.is_some();
            if takes_app_token(request.operation) && (self.can_mint() || has_app) {
                if !self.can_mint() {
                    return Ok(false);
                }
                self.mint(&*self.transport()?, true, stale).await?;
                return Ok(true);
            }
            if self.read().refresh.is_none() {
                return Ok(false);
            }
            self.refresh_user(&*self.transport()?, stale, &[]).await?;
            Ok(true)
        })
    }
}

/// OAuth 2 for a [`Client`](crate::Client), from [`Client::oauth`](crate::Client::oauth). Tokens it
/// obtains are used for the client's later calls, and each new user token is passed to the client's
/// [`on_token`](crate::ClientBuilder::on_token) callback for you to store.
#[derive(Clone, Debug)]
pub struct OAuth {
    credentials: Arc<EbayCredentials>,
    transport: Arc<Transport>,
}

impl OAuth {
    pub(crate) fn new(credentials: Arc<EbayCredentials>, transport: Arc<Transport>) -> Self {
        Self {
            credentials,
            transport,
        }
    }

    /// Builds the URL that asks a user to grant your app `scopes`, in the client's environment. See
    /// [`AuthorizationRequest`] and [`authorization_url`].
    pub fn authorization_url(
        &self,
        scopes: &[&str],
        state: Option<&str>,
        prompt: Option<&str>,
    ) -> Result<AuthorizationRequest, Error> {
        let client_id = self.credentials.client_id.as_deref().ok_or_else(|| {
            invalid_input(
                "set client_id and client_secret on the client to use the authorization code grant",
            )
        })?;
        let ru_name = self.ru_name()?;
        authorization_url(
            client_id,
            ru_name,
            scopes,
            &self.credentials.environment,
            state,
            prompt,
        )
    }

    fn ru_name(&self) -> Result<&str, Error> {
        self.credentials.ru_name.as_deref().ok_or_else(|| {
            invalid_input("set ru_name on the client to use the authorization code grant")
        })
    }

    /// Trades the code from eBay's redirect for a user token and its refresh token.
    pub async fn exchange_code(&self, code: &str) -> Result<Token, Error> {
        self.credentials.remember(&[code]);
        let ru_name = self.ru_name()?;
        let _refreshing = self.credentials.refreshing.lock().await;
        let fields = [
            ("grant_type", "authorization_code"),
            ("code", code),
            ("redirect_uri", ru_name),
        ];
        let token = self
            .credentials
            .request_token(&self.transport, &fields)
            .await?;
        Ok(self.credentials.store_user(token))
    }

    /// Replaces the user token now. The client also does this itself after a 401. `scopes` must be
    /// the original grant's or fewer; empty means the client's `user_scopes`, or without those the
    /// original grant's. A refresh asked for while another is under way waits for it and returns
    /// its token.
    pub async fn refresh(&self, scopes: &[&str]) -> Result<Token, Error> {
        let before = self.credentials.read().user.clone();
        self.credentials
            .refresh_user(&self.transport, before.as_deref(), scopes)
            .await
    }

    /// Mints an application token with the client's `app_scopes`, unless the current one is still
    /// fresh or `force` is false.
    pub async fn app_token(&self, force: bool) -> Result<Token, Error> {
        self.credentials.mint(&self.transport, force, None).await
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::runtime::Scheme;

    #[test]
    fn the_authorization_url_carries_the_ru_name_scopes_and_state() {
        let request = authorization_url(
            "synthetic-app-id",
            "synthetic-ru-name",
            &[
                API_SCOPE,
                "https://api.ebay.com/oauth/api_scope/sell.inventory",
            ],
            "sandbox",
            Some("synthetic-state"),
            Some("login"),
        )
        .unwrap();
        let url = url::Url::parse(&request.url).unwrap();
        assert_eq!(
            url.as_str().split('?').next(),
            Some("https://auth.sandbox.ebay.com/oauth2/authorize")
        );
        let query: Vec<(String, String)> = url.query_pairs().into_owned().collect();
        let expected = [
            ("client_id", "synthetic-app-id"),
            ("redirect_uri", "synthetic-ru-name"),
            ("response_type", "code"),
            (
                "scope",
                "https://api.ebay.com/oauth/api_scope https://api.ebay.com/oauth/api_scope/sell.inventory",
            ),
            ("state", "synthetic-state"),
            ("prompt", "login"),
        ];
        let expected: Vec<(String, String)> = expected
            .iter()
            .map(|(key, value)| ((*key).to_owned(), (*value).to_owned()))
            .collect();
        assert_eq!(query, expected);
        assert_eq!(request.state, "synthetic-state");
    }

    #[test]
    fn a_fresh_state_is_random() {
        let first = authorization_url("id", "ru", &[API_SCOPE], "production", None, None).unwrap();
        let second = authorization_url("id", "ru", &[API_SCOPE], "production", None, None).unwrap();
        assert!(
            first
                .url
                .starts_with("https://auth.ebay.com/oauth2/authorize?")
        );
        assert!(first.state.len() >= 32);
        assert_ne!(first.state, second.state);
        assert!(!first.url.contains("prompt"));
    }

    #[test]
    fn bad_input_is_refused() {
        let error = authorization_url("id", "ru", &[], "production", None, None).unwrap_err();
        assert_eq!(error.kind(), ErrorKind::InvalidInput);
        let error = authorization_url("id", "ru", &[API_SCOPE], "staging", None, None).unwrap_err();
        assert_eq!(
            error.to_string(),
            "unknown environment staging; expected one of: production, sandbox"
        );
    }

    #[test]
    fn operations_that_accept_an_app_scope_take_an_application_token() {
        const PUBLIC: Operation = Operation {
            id: "public",
            method: "GET",
            path: "/x",
            query_params: &[],
            returns_json: true,
            paging: None,
            security: &[&[Scheme {
                name: "api_auth",
                scopes: &[API_SCOPE],
            }]],
        };
        const SELLER: Operation = Operation {
            security: &[&[Scheme {
                name: "api_auth",
                scopes: &["https://api.ebay.com/oauth/api_scope/sell.account"],
            }]],
            ..PUBLIC
        };
        const INSIGHTS: Operation = Operation {
            security: &[&[Scheme {
                name: "api_auth",
                scopes: &["https://api.ebay.com/oauth/api_scope/metadata.insights"],
            }]],
            ..PUBLIC
        };
        assert!(takes_app_token(&PUBLIC));
        assert!(takes_app_token(&INSIGHTS));
        assert!(!takes_app_token(&SELLER));
        assert!(!takes_app_token(&TOKEN));
    }

    #[test]
    fn a_token_response_needs_an_access_token() {
        let token = parse_token(&serde_json::json!({
            "access_token": "synthetic-access", "expires_in": 7200, "token_type": "User Access Token",
            "refresh_token": "synthetic-refresh", "refresh_token_expires_in": 47304000,
        }))
        .unwrap();
        assert_eq!(token.expires_in, Some(7200));
        assert_eq!(token.refresh_token.as_deref(), Some("synthetic-refresh"));
        assert_eq!(token.refresh_token_expires_in, Some(47304000));
        assert_eq!(token.token_type, "User Access Token");
        let text = format!("{token:?}");
        assert!(
            !text.contains("synthetic-access") && !text.contains("synthetic-refresh"),
            "{text}"
        );
        let minted = parse_token(&serde_json::json!({"access_token": "a"})).unwrap();
        assert_eq!(
            (minted.refresh_token, minted.token_type.as_str()),
            (None, "Bearer")
        );
        assert_eq!(
            parse_token(&serde_json::json!({"access_token": ""}))
                .unwrap_err()
                .kind(),
            ErrorKind::Decode
        );
    }

    fn config() -> Config {
        Config {
            client_id: Some("synthetic-app-id".into()),
            client_secret: Some("synthetic-cert-id".into()),
            ru_name: None,
            app_token: None,
            user_token: Some("synthetic-user".into()),
            refresh_token: Some("synthetic-refresh".into()),
            on_token: None,
            app_scopes: vec![API_SCOPE.into()],
            user_scopes: Vec::new(),
            environment: "production".into(),
            #[cfg(feature = "signing")]
            signer: None,
        }
    }

    #[test]
    fn credentials_keep_current_tokens_and_only_recent_values_for_redaction() {
        let credentials = EbayCredentials::new(config()).unwrap();
        let old: Vec<String> = (0..100)
            .map(|index| format!("synthetic-old-{index}"))
            .collect();
        credentials.remember(&old.iter().map(String::as_str).collect::<Vec<_>>());
        let secrets = credentials.secrets();
        assert!(secrets.len() < 25);
        let basic = STANDARD.encode("synthetic-app-id:synthetic-cert-id");
        for value in [
            "synthetic-cert-id",
            &basic,
            "synthetic-user",
            "synthetic-refresh",
            "synthetic-old-99",
        ] {
            assert!(secrets.iter().any(|secret| secret == value), "{value}");
        }
        assert!(!secrets.iter().any(|secret| secret == "synthetic-old-0"));
        assert!(!secrets.iter().any(|secret| secret == "synthetic-app-id"));
    }

    #[test]
    fn a_user_token_keeps_the_refresh_token_when_the_response_has_none() {
        let seen = Arc::new(Mutex::new(Vec::new()));
        let sink = seen.clone();
        let credentials = EbayCredentials::new(Config {
            on_token: Some(Arc::new(move |token: &Token| {
                sink.lock().unwrap().push(token.clone())
            })),
            ..config()
        })
        .unwrap();
        let stored = credentials.store_user(Token::access("synthetic-user-2".into()));
        assert_eq!(stored.refresh_token.as_deref(), Some("synthetic-refresh"));
        assert_eq!(seen.lock().unwrap().as_slice(), [stored]);
        assert!(
            credentials
                .secrets()
                .iter()
                .any(|secret| secret == "synthetic-user")
        );
    }

    #[test]
    fn a_minted_token_is_replaced_before_it_expires() {
        let credentials = EbayCredentials::new(config()).unwrap();
        credentials.store_app(Token {
            expires_in: Some(30),
            ..Token::access("synthetic-app".into())
        });
        assert_eq!(credentials.fresh_app_token(), None);
        credentials.store_app(Token {
            expires_in: Some(7200),
            ..Token::access("synthetic-app-2".into())
        });
        assert_eq!(
            credentials.fresh_app_token().as_deref(),
            Some("synthetic-app-2")
        );
        assert!(
            credentials
                .secrets()
                .iter()
                .any(|secret| secret == "synthetic-app")
        );
    }
}
