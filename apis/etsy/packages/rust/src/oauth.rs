//! OAuth 2 authorization code flow with PKCE, as Etsy implements it.

use std::fmt;
use std::sync::{Arc, Mutex, OnceLock, PoisonError, RwLock, Weak};

use base64::Engine;
use base64::engine::general_purpose::URL_SAFE_NO_PAD;
use futures_core::future::BoxFuture;
use reqwest::header::{AUTHORIZATION, HeaderValue};
use serde_json::Value;
use sha2::{Digest, Sha256};

use crate::runtime::{AuthRequest, Credentials, Operation, Request, Transport};
use crate::{Error, ErrorKind};

/// Where to send a user to grant your app access.
pub const AUTHORIZATION_URL: &str = "https://www.etsy.com/oauth/connect";

static TOKEN: Operation = Operation {
    id: "oauthToken",
    method: "POST",
    path: "/v3/public/oauth/token",
    query_params: &[],
    returns_json: true,
    paging: None,
    security: &[],
};

pub(crate) type OnToken = Arc<dyn Fn(&Token) + Send + Sync>;

/// An access token and the refresh token that replaces it. Etsy prefixes both with the user's ID.
/// Debug output hides both tokens.
#[derive(Clone, PartialEq, Eq)]
pub struct Token {
    pub access_token: String,
    pub refresh_token: String,
    /// Seconds until the access token expires, when the response says.
    pub expires_in: Option<i64>,
    pub token_type: String,
}

impl Token {
    /// The numeric user ID that prefixes the access token, when it has one.
    pub fn user_id(&self) -> Option<u64> {
        let (prefix, _) = self.access_token.split_once('.')?;
        prefix.parse().ok()
    }
}

impl fmt::Debug for Token {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("Token")
            .field("access_token", &"***")
            .field("refresh_token", &"***")
            .field("expires_in", &self.expires_in)
            .field("token_type", &self.token_type)
            .finish()
    }
}

/// Values for [`authorization_url`] to use instead of fresh random ones.
#[derive(Clone, Debug, Default, PartialEq, Eq)]
pub struct AuthorizationOptions {
    pub state: Option<String>,
    /// A PKCE code verifier: 43 to 128 letters, digits, `-`, `.`, `_` or `~`.
    pub code_verifier: Option<String>,
}

/// Send the user to `url`. Keep `state` and `code_verifier` until Etsy redirects back, check that the
/// redirect's `state` matches, then pass its `code` and this `code_verifier` to
/// [`OAuth::exchange_code`]. Debug output hides the verifier.
#[derive(Clone, PartialEq, Eq)]
pub struct AuthorizationRequest {
    pub url: String,
    pub state: String,
    pub code_verifier: String,
}

impl fmt::Debug for AuthorizationRequest {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("AuthorizationRequest")
            .field("url", &self.url)
            .field("state", &self.state)
            .field("code_verifier", &"***")
            .finish()
    }
}

/// The S256 challenge for a PKCE code verifier.
pub fn code_challenge(code_verifier: &str) -> String {
    URL_SAFE_NO_PAD.encode(Sha256::digest(code_verifier.as_bytes()))
}

fn random(bytes: usize) -> Result<String, Error> {
    let mut buffer = vec![0; bytes];
    getrandom::fill(&mut buffer).map_err(|error| {
        Error::new(
            ErrorKind::InvalidInput,
            format!("no random bytes are available: {error}"),
        )
    })?;
    Ok(URL_SAFE_NO_PAD.encode(buffer))
}

fn invalid_input(message: &str) -> Error {
    Error::new(ErrorKind::InvalidInput, message)
}

fn valid_verifier(verifier: &str) -> bool {
    (43..=128).contains(&verifier.len())
        && verifier
            .bytes()
            .all(|byte| byte.is_ascii_alphanumeric() || matches!(byte, b'-' | b'.' | b'_' | b'~'))
}

/// Builds the URL that asks a user to grant your app `scopes`, with a fresh state and PKCE verifier
/// unless `options` gives your own. `api_key` is your app's keystring.
pub fn authorization_url(
    api_key: &str,
    redirect_uri: &str,
    scopes: &[&str],
    options: AuthorizationOptions,
) -> Result<AuthorizationRequest, Error> {
    if scopes.is_empty() {
        return Err(invalid_input("request at least one scope"));
    }
    let code_verifier = match options.code_verifier {
        Some(verifier) => verifier,
        None => random(64)?,
    };
    if !valid_verifier(&code_verifier) {
        return Err(invalid_input(
            "code_verifier must be 43 to 128 unreserved characters",
        ));
    }
    let state = match options.state {
        Some(state) => state,
        None => random(32)?,
    };
    let query = url::form_urlencoded::Serializer::new(String::new())
        .append_pair("response_type", "code")
        .append_pair("client_id", api_key)
        .append_pair("redirect_uri", redirect_uri)
        .append_pair("scope", &scopes.join(" "))
        .append_pair("state", &state)
        .append_pair("code_challenge", &code_challenge(&code_verifier))
        .append_pair("code_challenge_method", "S256")
        .finish();
    Ok(AuthorizationRequest {
        url: format!("{AUTHORIZATION_URL}?{query}"),
        state,
        code_verifier,
    })
}

fn needs(operation: &Operation, scheme: &str) -> bool {
    operation
        .security
        .iter()
        .any(|schemes| schemes.iter().any(|part| part.name == scheme))
}

fn header(text: &str) -> Result<HeaderValue, Error> {
    let mut value = HeaderValue::from_str(text)
        .map_err(|_| invalid_input("a credential cannot be sent as a header"))?;
    value.set_sensitive(true);
    Ok(value)
}

#[derive(Default)]
struct Tokens {
    access: Option<String>,
    refresh: Option<String>,
}

/// Sends `x-api-key` on every operation and the access token on those that need OAuth. After a 401 on
/// one of those, refreshes the access token once, when there is a refresh token.
pub(crate) struct EtsyCredentials {
    api_key: String,
    key_header: HeaderValue,
    shared_secret: String,
    tokens: RwLock<Tokens>,
    /// Every token and code this client has held, so that none reaches a log or error.
    seen: Mutex<Vec<String>>,
    on_token: Option<OnToken>,
    transport: OnceLock<Weak<Transport>>,
}

impl fmt::Debug for EtsyCredentials {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.write_str("EtsyCredentials(***)")
    }
}

impl EtsyCredentials {
    pub(crate) fn new(
        api_key: String,
        shared_secret: String,
        access: Option<String>,
        refresh: Option<String>,
        on_token: Option<OnToken>,
    ) -> Result<Self, Error> {
        let key_header = header(&format!("{api_key}:{shared_secret}"))?;
        if let Some(access) = &access {
            header(&format!("Bearer {access}"))?;
        }
        let seen = [&access, &refresh]
            .into_iter()
            .flatten()
            .filter(|token| !token.is_empty())
            .cloned()
            .collect();
        Ok(Self {
            api_key,
            key_header,
            shared_secret,
            tokens: RwLock::new(Tokens { access, refresh }),
            seen: Mutex::new(seen),
            on_token,
            transport: OnceLock::new(),
        })
    }

    /// Lets a refresh after a 401 call the token endpoint through the client's own transport.
    pub(crate) fn attach(&self, transport: &Arc<Transport>) {
        let _ = self.transport.set(Arc::downgrade(transport));
    }

    fn remember(&self, values: &[&str]) {
        let mut seen = self.seen.lock().unwrap_or_else(PoisonError::into_inner);
        seen.extend(
            values
                .iter()
                .filter(|value| !value.is_empty())
                .map(|value| (*value).to_owned()),
        );
    }

    fn refresh_token(&self) -> Option<String> {
        self.tokens
            .read()
            .unwrap_or_else(PoisonError::into_inner)
            .refresh
            .clone()
    }

    fn store(&self, token: Token) -> Token {
        self.remember(&[&token.access_token, &token.refresh_token]);
        {
            let mut tokens = self.tokens.write().unwrap_or_else(PoisonError::into_inner);
            tokens.access = Some(token.access_token.clone());
            tokens.refresh = Some(token.refresh_token.clone());
        }
        if let Some(on_token) = &self.on_token {
            on_token(&token);
        }
        token
    }

    async fn request_token(
        &self,
        transport: &Transport,
        fields: &[(&str, &str)],
    ) -> Result<Token, Error> {
        let mut request = Request::new(&TOKEN);
        for (name, value) in fields {
            request.urlencoded(name, &(*value).to_owned());
        }
        let reply: Value = transport.call(request).await?;
        Ok(self.store(parse_token(&reply)?))
    }

    async fn refresh_with(&self, transport: &Transport) -> Result<Token, Error> {
        let Some(refresh_token) = self.refresh_token() else {
            return Err(invalid_input(
                "there is no refresh token: set refresh_token, or exchange a code first",
            ));
        };
        let fields = [
            ("grant_type", "refresh_token"),
            ("client_id", self.api_key.as_str()),
            ("refresh_token", &refresh_token),
        ];
        self.request_token(transport, &fields).await
    }
}

fn parse_token(reply: &Value) -> Result<Token, Error> {
    let text = |name: &str| {
        reply
            .get(name)
            .and_then(Value::as_str)
            .filter(|text| !text.is_empty())
            .map(str::to_owned)
    };
    let (Some(access_token), Some(refresh_token)) = (text("access_token"), text("refresh_token"))
    else {
        return Err(Error::new(
            ErrorKind::Decode,
            "the token response has no access and refresh token",
        ));
    };
    Ok(Token {
        access_token,
        refresh_token,
        expires_in: reply.get("expires_in").and_then(Value::as_i64),
        token_type: text("token_type").unwrap_or_else(|| "Bearer".to_owned()),
    })
}

impl Credentials for EtsyCredentials {
    fn apply<'a>(&'a self, request: &'a mut AuthRequest) -> BoxFuture<'a, Result<(), Error>> {
        let result = (|| {
            if needs(request.operation, "api_key") {
                request.headers.insert("x-api-key", self.key_header.clone());
            }
            let access = self
                .tokens
                .read()
                .unwrap_or_else(PoisonError::into_inner)
                .access
                .clone();
            if let Some(access) = access.filter(|_| needs(request.operation, "oauth2")) {
                request
                    .headers
                    .insert(AUTHORIZATION, header(&format!("Bearer {access}"))?);
            }
            Ok(())
        })();
        Box::pin(async move { result })
    }

    fn secrets(&self) -> Vec<String> {
        let seen = self.seen.lock().unwrap_or_else(PoisonError::into_inner);
        [self.api_key.clone(), self.shared_secret.clone()]
            .into_iter()
            .chain(seen.iter().cloned())
            .collect()
    }

    fn refresh<'a>(&'a self, request: &'a AuthRequest) -> BoxFuture<'a, Result<bool, Error>> {
        Box::pin(async move {
            if !needs(request.operation, "oauth2") || self.refresh_token().is_none() {
                return Ok(false);
            }
            let Some(transport) = self.transport.get().and_then(Weak::upgrade) else {
                return Ok(false);
            };
            self.refresh_with(&transport).await?;
            Ok(true)
        })
    }
}

/// OAuth 2 for a [`Client`](crate::Client), from [`Client::oauth`](crate::Client::oauth). A token it
/// obtains is used for the client's later calls, and is passed to the client's
/// [`on_token`](crate::ClientBuilder::on_token) callback for you to store.
#[derive(Clone, Debug)]
pub struct OAuth {
    credentials: Arc<EtsyCredentials>,
    transport: Arc<Transport>,
}

impl OAuth {
    pub(crate) fn new(credentials: Arc<EtsyCredentials>, transport: Arc<Transport>) -> Self {
        Self {
            credentials,
            transport,
        }
    }

    /// Builds the URL that asks a user to grant your app `scopes`. See [`AuthorizationRequest`].
    pub fn authorization_url(
        &self,
        redirect_uri: &str,
        scopes: &[&str],
        options: AuthorizationOptions,
    ) -> Result<AuthorizationRequest, Error> {
        authorization_url(&self.credentials.api_key, redirect_uri, scopes, options)
    }

    /// Trades the code from Etsy's redirect for a token. `redirect_uri` must match the authorization
    /// URL's.
    pub async fn exchange_code(
        &self,
        code: &str,
        code_verifier: &str,
        redirect_uri: &str,
    ) -> Result<Token, Error> {
        self.credentials.remember(&[code, code_verifier]);
        let fields = [
            ("grant_type", "authorization_code"),
            ("client_id", self.credentials.api_key.as_str()),
            ("redirect_uri", redirect_uri),
            ("code", code),
            ("code_verifier", code_verifier),
        ];
        self.credentials
            .request_token(&self.transport, &fields)
            .await
    }

    /// Replaces the access token now. The client also does this itself after a 401.
    // TODO: share one refresh with an automatic refresh that is already running.
    pub async fn refresh(&self) -> Result<Token, Error> {
        self.credentials.refresh_with(&self.transport).await
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    const VERIFIER: &str = "dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk";

    #[test]
    fn the_challenge_is_the_rfc_7636_example() {
        assert_eq!(
            code_challenge(VERIFIER),
            "E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM"
        );
    }

    #[test]
    fn the_authorization_url_carries_pkce_and_state() {
        let options = AuthorizationOptions {
            state: Some("synthetic-state".into()),
            code_verifier: Some(VERIFIER.into()),
        };
        let request = authorization_url(
            "synthetic-keystring",
            "https://example.test/back",
            &["listings_r", "shops_r"],
            options,
        )
        .unwrap();
        let url = url::Url::parse(&request.url).unwrap();
        assert_eq!(url.as_str().split('?').next(), Some(AUTHORIZATION_URL));
        let query: Vec<(String, String)> = url.query_pairs().into_owned().collect();
        let expected = [
            ("response_type", "code"),
            ("client_id", "synthetic-keystring"),
            ("redirect_uri", "https://example.test/back"),
            ("scope", "listings_r shops_r"),
            ("state", "synthetic-state"),
            (
                "code_challenge",
                "E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM",
            ),
            ("code_challenge_method", "S256"),
        ];
        let expected: Vec<(String, String)> = expected
            .iter()
            .map(|(k, v)| ((*k).to_owned(), (*v).to_owned()))
            .collect();
        assert_eq!(query, expected);
        assert_eq!(request.state, "synthetic-state");
        assert!(!format!("{request:?}").contains(VERIFIER));
    }

    #[test]
    fn fresh_values_are_random_and_valid() {
        let first = authorization_url(
            "k",
            "https://example.test",
            &["email_r"],
            AuthorizationOptions::default(),
        )
        .unwrap();
        let second = authorization_url(
            "k",
            "https://example.test",
            &["email_r"],
            AuthorizationOptions::default(),
        )
        .unwrap();
        assert!(valid_verifier(&first.code_verifier));
        assert!(first.state.len() >= 32);
        assert_ne!(first.code_verifier, second.code_verifier);
        assert_ne!(first.state, second.state);
    }

    #[test]
    fn bad_input_is_refused() {
        let error = authorization_url(
            "k",
            "https://example.test",
            &[],
            AuthorizationOptions::default(),
        )
        .unwrap_err();
        assert_eq!(error.kind(), ErrorKind::InvalidInput);
        let short = AuthorizationOptions {
            code_verifier: Some("short".into()),
            ..Default::default()
        };
        assert!(authorization_url("k", "https://example.test", &["email_r"], short).is_err());
    }

    #[test]
    fn the_user_id_prefixes_the_access_token() {
        let token = Token {
            access_token: "12345678.synthetic".into(),
            refresh_token: "12345678.r".into(),
            expires_in: Some(3600),
            token_type: "Bearer".into(),
        };
        assert_eq!(token.user_id(), Some(12345678));
        assert!(!format!("{token:?}").contains("synthetic"));
        assert_eq!(
            Token {
                access_token: "synthetic".into(),
                ..token
            }
            .user_id(),
            None
        );
    }
}
