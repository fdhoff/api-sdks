// Conformance driver: reads cases as JSON lines and calls the public client. See the runner's README.
import { generateKeyPairSync } from 'node:crypto';
import { createInterface } from 'node:readline';
import { parseArgs } from 'node:util';

const { values } = parseArgs({ options: { format: { type: 'string', default: 'esm' } } });
const dist = new URL(`../dist/${values.format}/`, import.meta.url);
const { ApiError, EbayClient, ENVIRONMENTS, HttpError, SigningKey } = await import(new URL('index.js', dist).href);

// Each contract's name in the cases, its directory and the client property that holds it.
const CONTRACTS = {
  sell_account_v1: ['account', 'account'],
  sell_account_v2: ['account-v2', 'accountV2'],
  sell_analytics: ['analytics', 'analytics'],
  sell_feed: ['feed', 'feed'],
  sell_finances: ['finances', 'finances'],
  sell_fulfillment: ['fulfillment', 'fulfillment'],
  sell_inventory: ['inventory', 'inventory'],
  sell_marketing: ['marketing', 'marketing'],
  sell_metadata: ['metadata', 'metadata'],
  sell_negotiation: ['negotiation', 'negotiation'],
  sell_recommendation: ['recommendation', 'recommendation'],
  sell_stores: ['stores', 'stores'],
  sell_post_order: ['post-order', 'postOrder'],
  commerce_feedback: ['feedback', 'feedback'],
  commerce_identity: ['identity', 'identity'],
  commerce_media: ['media', 'media'],
  commerce_message: ['message', 'message'],
  commerce_notification: ['notification', 'notification'],
  commerce_taxonomy: ['taxonomy', 'taxonomy'],
  developer_analytics: ['developer-analytics', 'developerAnalytics'],
  developer_key_management: ['key-management', 'keyManagement'],
};
const OPERATIONS = new Map();
for (const [contract, [dir, property]] of Object.entries(CONTRACTS)) {
  const { OPERATIONS: operations } = await import(new URL(`${dir}/resources.js`, dist).href);
  for (const operation of operations.values()) OPERATIONS.set(`${contract}.${operation.id}`, [property, operation]);
}
const FORM = ['form', 'urlencoded'];
// Generated per run, never stored: the cases check the signature's shape and digest, not the key.
const PRIVATE_KEY = generateKeyPairSync('ed25519').privateKey.export({ type: 'pkcs8', format: 'pem' });

/** Each host key's harness prefix: the key itself, or with an environment the hostname it maps the key to. */
function hosts(settings) {
  const urls = ENVIRONMENTS[settings.environment ?? 'production'];
  const path = (key, url) => (settings.environment ? new URL(url).hostname : key);
  return Object.fromEntries(
    Object.entries(urls).map(([key, url]) => [key, `${settings.base_url}/_host/${path(key, url)}`]),
  );
}

async function options(settings, logs) {
  const log = (message) => logs.push(message);
  const defaults = settings.header_defaults ?? {};
  const signingKey =
    settings.signature_key === undefined
      ? undefined
      : await SigningKey.create({ privateKey: PRIVATE_KEY, jwe: settings.signature_key });
  return {
    appToken: settings.app_token,
    userToken: settings.user_token,
    hosts: hosts(settings),
    environment: settings.environment,
    marketplaceId: defaults['X-EBAY-C-MARKETPLACE-ID'],
    contentLanguage: defaults['Content-Language'],
    signingKey,
    userAgent: settings.user_agent,
    timeoutMs: settings.timeout_ms,
    maxRetries: settings.max_retries,
    retryBaseDelayMs: settings.retry_base_delay_ms,
    rateLimitWaitMs: settings.rate_limit_wait_ms,
    maxRetryWaitMs: settings.max_retry_wait_ms,
    logger: { debug: log, info: log },
  };
}

/** A form body's fields are named parameters, like query and header parameters. */
function args(operation, request) {
  const form = operation.params.some(({ location }) => FORM.includes(location));
  const values = { ...request.params, ...request.multipart, ...(form ? request.body : {}) };
  const inPath = operation.params.filter(({ location }) => location === 'path');
  const named = operation.params.filter(({ location, wire }) => location !== 'path' && wire in values);
  return [
    ...inPath.map(({ wire }) => values[wire]),
    ...(operation.hasBody ? [request.body] : []),
    Object.fromEntries(named.map(({ wire, name }) => [name, values[wire]])),
  ];
}

async function run(message, logs) {
  const { request, client: settings } = message;
  const [property, operation] = OPERATIONS.get(request.operation);
  const client = new EbayClient(await options(settings, logs));
  const resource = client[property][operation.resource];
  if (!request.paginate) return resource[operation.name](...args(operation, request));
  const items = [];
  for await (const item of resource[operation.iterator](...args(operation, request))) items.push(item);
  return items;
}

function errorOutput(error) {
  const fields = {
    kind: error.kind,
    status: error.status,
    raw_body: error.rawBody,
    message: error instanceof HttpError ? error.detail : undefined,
    code: error.code,
  };
  return Object.fromEntries(Object.entries(fields).filter(([, value]) => value !== undefined));
}

for await (const line of createInterface({ input: process.stdin })) {
  const logs = [];
  try {
    const result = await run(JSON.parse(line), logs);
    console.log(JSON.stringify({ result: result ?? null, logs }));
  } catch (error) {
    if (!(error instanceof ApiError)) throw error;
    console.log(JSON.stringify({ error: errorOutput(error), logs }));
  }
}
