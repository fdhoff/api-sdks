// Conformance driver: reads cases as JSON lines and calls the public client. See the runner's README.
import { createInterface } from 'node:readline';
import { parseArgs } from 'node:util';

const { values } = parseArgs({ options: { format: { type: 'string', default: 'esm' } } });
const dist = new URL(`../dist/${values.format}/`, import.meta.url);
const { ApiError, ENVIRONMENTS, MercuryClient } = await import(new URL('index.js', dist).href);
const { OPERATIONS } = await import(new URL('resources.js', dist).href);

const FORM = ['form', 'urlencoded'];

/** Each host key's harness prefix: the key itself, or with an environment the hostname it maps the key to. */
function hosts(settings) {
  const urls = ENVIRONMENTS[settings.environment ?? 'production'];
  const path = (key, url) => (settings.environment ? new URL(url).hostname : key);
  return Object.fromEntries(
    Object.entries(urls).map(([key, url]) => [key, `${settings.base_url}/_host/${path(key, url)}`]),
  );
}

function options(settings, logs) {
  const log = (message) => logs.push(message);
  return {
    token: settings.token,
    hosts: hosts(settings),
    environment: settings.environment,
    userAgent: settings.user_agent,
    timeoutMs: settings.timeout_ms,
    maxRetries: settings.max_retries,
    retryBaseDelayMs: settings.retry_base_delay_ms,
    rateLimitWaitMs: settings.rate_limit_wait_ms,
    maxRetryWaitMs: settings.max_retry_wait_ms,
    logger: { debug: log, info: log },
  };
}

/** A form body's fields are named parameters, like query parameters. Multipart parts are files, sent as bytes. */
function args(operation, request) {
  const form = operation.params.some(({ location }) => FORM.includes(location));
  const files = Object.fromEntries(
    Object.entries(request.multipart ?? {}).map(([wire, value]) => [wire, new TextEncoder().encode(value)]),
  );
  const values = { ...request.params, ...files, ...(form ? request.body : {}) };
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
  const operation = OPERATIONS.get(request.operation);
  const resource = new MercuryClient(options(settings, logs))[operation.resource];
  if (!request.paginate) {
    const result = await resource[operation.name](...args(operation, request));
    if (!operation.returnsBinary) return result;
    return { content_type: result.contentType, base64: Buffer.from(await result.bytes()).toString('base64') };
  }
  const items = [];
  for await (const item of resource[operation.iterator](...args(operation, request))) items.push(item);
  return items;
}

function errorOutput(error) {
  const fields = { kind: error.kind, status: error.status, raw_body: error.rawBody };
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
