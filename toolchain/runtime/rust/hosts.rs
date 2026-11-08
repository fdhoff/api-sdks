use std::collections::{BTreeSet, HashMap};

/// Named environments, each a base URL for every host key.
pub type Environments = [(&'static str, &'static [(&'static str, &'static str)])];

/// The host map for `environment`, or the caller's own `hosts`, which must name exactly the host
/// keys the environments use. Trailing slashes are removed. Empty `hosts` count as none given.
#[allow(dead_code, reason = "an API with one host defines no environments")]
pub fn select_hosts(
    environments: &Environments,
    environment: &str,
    hosts: Option<&HashMap<String, String>>,
) -> Result<HashMap<String, String>, String> {
    let trim = |url: &str| url.trim_end_matches('/').to_owned();
    if let Some(hosts) = hosts.filter(|hosts| !hosts.is_empty()) {
        let keys: BTreeSet<&str> = environments.iter().flat_map(|(_, map)| map.iter().map(|(key, _)| *key)).collect();
        let missing: Vec<&str> = keys.iter().copied().filter(|key| !hosts.contains_key(*key)).collect();
        if !missing.is_empty() {
            return Err(format!("hosts lacks keys: {}", missing.join(", ")));
        }
        let unknown: BTreeSet<&str> = hosts.keys().map(String::as_str).filter(|key| !keys.contains(key)).collect();
        if !unknown.is_empty() {
            return Err(format!("hosts has unknown keys: {}", unknown.into_iter().collect::<Vec<_>>().join(", ")));
        }
        return Ok(hosts.iter().map(|(key, url)| (key.clone(), trim(url))).collect());
    }
    match environments.iter().find(|(name, _)| *name == environment) {
        Some((_, map)) => Ok(map.iter().map(|(key, url)| ((*key).to_owned(), trim(url))).collect()),
        None => {
            let known: BTreeSet<&str> = environments.iter().map(|(name, _)| *name).collect();
            let known: Vec<&str> = known.into_iter().collect();
            Err(format!("unknown environment {environment}; expected one of: {}", known.join(", ")))
        }
    }
}

#[cfg(test)]
mod tests {
    use std::sync::Arc;
    use std::time::Duration;

    use futures_util::StreamExt;
    use reqwest::header::{HeaderMap, HeaderValue};
    use serde_json::Value;

    use super::super::credentials::tests::{Tokens, serve};
    use super::super::error::Error;
    use super::super::request::{Operation, Paging, Params, Request};
    use super::super::transport::{Settings, Transport};
    use super::*;
    use crate::ErrorKind;

    const ENVIRONMENTS: &Environments = &[
        ("production", &[("main", "https://main.example.test/"), ("files", "https://files.example.test")]),
        ("sandbox", &[("main", "https://main.sandbox.example.test"), ("files", "https://files.sandbox.example.test")]),
    ];

    const LIST_ITEMS: Operation = Operation {
        id: "list-items",
        method: "GET",
        path: "/items",
        query_params: &["offset"],
        returns_json: true,
        paging: Some(Paging::Offset { items: "results", total: "count", offset: "offset" }),
        security: &[],
    };

    const LIST_FILES: Operation = Operation { id: "list-files", path: "/files", ..LIST_ITEMS };

    struct ItemParams {
        x_tenant: Option<String>,
    }

    impl Params for ItemParams {
        fn apply(&self, request: &mut Request) {
            request.header("X-Tenant", &self.x_tenant);
        }
    }

    fn map(pairs: &[(&str, &str)]) -> HashMap<String, String> {
        pairs.iter().map(|(key, value)| ((*key).to_owned(), (*value).to_owned())).collect()
    }

    fn transport(base_url: &str, hosts: HashMap<String, String>, defaults: &[(&str, &str)], credentials: Arc<Tokens>) -> Transport {
        with_headers(base_url, hosts, defaults, credentials, HeaderMap::new())
    }

    fn with_headers(
        base_url: &str,
        hosts: HashMap<String, String>,
        defaults: &[(&str, &str)],
        credentials: Arc<Tokens>,
        headers: HeaderMap,
    ) -> Transport {
        Transport::new(Settings {
            base_url: base_url.to_owned(),
            hosts,
            credentials,
            headers,
            header_defaults: map(defaults),
            to_error: |context| Error::new(ErrorKind::Api, format!("status {}", context.status)).with_status(context.status),
            timeout: Duration::from_secs(5),
            max_retries: 0,
            retry_base_delay: Duration::ZERO,
            rate_limit_wait: Duration::ZERO,
            max_retry_wait: Duration::ZERO,
            http: None,
        })
        .unwrap()
    }

    fn line<'a>(head: &'a str, name: &str) -> Option<&'a str> {
        head.lines().find_map(|line| line.strip_prefix(&format!("{name}: ")))
    }

    #[test]
    fn select_hosts_picks_an_environment_and_trims_slashes() {
        let hosts = select_hosts(ENVIRONMENTS, "production", None).unwrap();
        assert_eq!(hosts, map(&[("main", "https://main.example.test"), ("files", "https://files.example.test")]));
        assert_eq!(select_hosts(ENVIRONMENTS, "sandbox", Some(&HashMap::new())).unwrap()["files"], "https://files.sandbox.example.test");
    }

    #[test]
    fn select_hosts_rejects_an_unknown_environment() {
        let error = select_hosts(ENVIRONMENTS, "staging", None).unwrap_err();
        assert_eq!(error, "unknown environment staging; expected one of: production, sandbox");
    }

    #[test]
    fn select_hosts_takes_a_custom_map_that_names_every_key() {
        let custom = map(&[("main", "http://127.0.0.1:1/"), ("files", "http://127.0.0.1:2")]);
        assert_eq!(select_hosts(ENVIRONMENTS, "nowhere", Some(&custom)).unwrap()["main"], "http://127.0.0.1:1");
        let missing = select_hosts(ENVIRONMENTS, "production", Some(&map(&[("main", "http://h")]))).unwrap_err();
        assert_eq!(missing, "hosts lacks keys: files");
        let extra = map(&[("main", "http://h"), ("files", "http://h"), ("uploads", "http://h"), ("archive", "http://h")]);
        assert_eq!(select_hosts(ENVIRONMENTS, "production", Some(&extra)).unwrap_err(), "hosts has unknown keys: archive, uploads");
    }

    #[tokio::test]
    async fn each_operation_goes_to_its_host_and_pages_stay_there() {
        let (main, main_log) = serve(|_, _| (200, r#"{"results":[]}"#.to_owned())).await;
        let (files, files_log) = serve(|number, _| match number {
            1 => (200, r#"{"count":3,"results":[1,2]}"#.to_owned()),
            _ => (200, r#"{"count":3,"results":[3]}"#.to_owned()),
        })
        .await;
        let hosts = map(&[("main", &main), ("files", &format!("{files}/v1"))]);
        let transport = Arc::new(transport("http://127.0.0.1:1", hosts, &[], Arc::default()));

        transport.call::<Value>(Request::new(&LIST_ITEMS).host("main")).await.unwrap();
        let items: Vec<i64> =
            Transport::paginate::<i64>(&transport, Request::new(&LIST_FILES).host("files")).map(Result::unwrap).collect().await;
        assert_eq!(items, [1, 2, 3]);

        assert!(main_log.lock().unwrap()[0].head.starts_with("get /items http/1.1"));
        let heads: Vec<String> = files_log.lock().unwrap().iter().map(|sent| sent.head.lines().next().unwrap().to_owned()).collect();
        assert_eq!(heads, ["get /v1/files http/1.1", "get /v1/files?offset=2 http/1.1"]);
    }

    #[tokio::test]
    async fn an_operation_with_no_host_key_goes_to_the_base_url() {
        let (url, log) = serve(|_, _| (200, "{}".to_owned())).await;
        let transport = transport(&url, map(&[("main", "http://127.0.0.1:1")]), &[], Arc::default());
        transport.call::<Value>(Request::new(&LIST_ITEMS)).await.unwrap();
        assert_eq!(log.lock().unwrap().len(), 1);
    }

    #[tokio::test]
    async fn an_unknown_host_key_fails_before_credentials_or_sending() {
        let (url, log) = serve(|_, _| (200, "{}".to_owned())).await;
        let credentials = Arc::new(Tokens::default());
        let transport = transport(&url, map(&[("main", &url)]), &[], credentials.clone());
        let error = transport.call::<Value>(Request::new(&LIST_FILES).host("files")).await.unwrap_err();
        assert_eq!(error.kind(), ErrorKind::Api);
        assert!(error.to_string().contains("host files"), "{error}");
        assert!(credentials.seen.lock().unwrap().is_empty());
        assert!(log.lock().unwrap().is_empty());
    }

    #[tokio::test]
    async fn a_header_default_is_sent_unless_the_call_gives_a_value() {
        let (url, log) = serve(|_, _| (200, "{}".to_owned())).await;
        let credentials = Arc::new(Tokens::default());
        let transport = transport(&url, HashMap::new(), &[("x-TENANT", "acme")], credentials.clone());
        let call = |value: Option<&str>| Request::new(&LIST_ITEMS).params(&ItemParams { x_tenant: value.map(str::to_owned) });

        transport.call::<Value>(call(None)).await.unwrap();
        transport.call::<Value>(call(Some("other"))).await.unwrap();
        let sent = log.lock().unwrap();
        assert_eq!(line(&sent[0].head, "x-tenant"), Some("acme"));
        assert_eq!(line(&sent[1].head, "x-tenant"), Some("other"));
        assert_eq!(sent[0].head.matches("x-tenant:").count(), 1);
        assert_eq!(credentials.seen.lock().unwrap().len(), 2);
    }

    #[tokio::test]
    async fn a_header_default_reaches_only_operations_that_declare_it() {
        let (url, log) = serve(|_, _| (200, "{}".to_owned())).await;
        let transport = transport(&url, HashMap::new(), &[("X-Tenant", "acme")], Arc::default());
        transport.call::<Value>(Request::new(&LIST_FILES)).await.unwrap();
        assert_eq!(line(&log.lock().unwrap()[0].head, "x-tenant"), None);
    }

    #[tokio::test]
    async fn a_header_is_absent_with_neither_a_value_nor_a_default() {
        let (url, log) = serve(|_, _| (200, "{}".to_owned())).await;
        let transport = transport(&url, HashMap::new(), &[("X-Other", "acme")], Arc::default());
        transport.call::<Value>(Request::new(&LIST_ITEMS).params(&ItemParams { x_tenant: None })).await.unwrap();
        let head = &log.lock().unwrap()[0].head;
        assert_eq!(line(head, "x-tenant"), None);
        assert_eq!(line(head, "x-other"), None);
    }

    #[tokio::test]
    async fn a_header_value_replaces_a_client_wide_header_of_the_same_name() {
        let (url, log) = serve(|_, _| (200, "{}".to_owned())).await;
        let mut headers = HeaderMap::new();
        headers.insert("x-tenant", HeaderValue::from_static("client-wide"));
        let transport = with_headers(&url, HashMap::new(), &[("X-Tenant", "acme")], Arc::default(), headers);
        transport.call::<Value>(Request::new(&LIST_ITEMS).params(&ItemParams { x_tenant: None })).await.unwrap();
        transport.call::<Value>(Request::new(&LIST_FILES)).await.unwrap();
        let sent = log.lock().unwrap();
        assert_eq!(sent[0].head.matches("x-tenant:").count(), 1);
        assert_eq!(line(&sent[0].head, "x-tenant"), Some("acme"));
        assert_eq!(line(&sent[1].head, "x-tenant"), Some("client-wide"));
    }
}
