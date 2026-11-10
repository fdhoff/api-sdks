// Conformance driver: reads cases as JSON lines and calls the public client. See the runner's README.
// The client adds `/api/v1` to the instance URL, while the cases name each path as the spec declares it, because the
// mock serves them without the prefix. The driver's `fetch` removes the prefix on the way out. A request without it
// goes out unchanged, so its path fails the case's wire check.
import { createInterface } from 'node:readline';
import { parseArgs } from 'node:util';

const { values } = parseArgs({ options: { format: { type: 'string', default: 'esm' } } });
const dist = new URL(`../dist/${values.format}/`, import.meta.url);
const { ApiError, GiteaClient, HttpError } = await import(new URL('index.js', dist).href);
const { API_PATH } = await import(new URL('client.js', dist).href);
const { OPERATIONS } = await import(new URL('resources.js', dist).href);

const FORM = ['form', 'urlencoded'];

function unprefixed(input, init) {
  const url = new URL(String(input));
  if (url.pathname.startsWith(`${API_PATH}/`)) url.pathname = url.pathname.slice(API_PATH.length);
  return globalThis.fetch(url, init);
}

/** A case that sets `username` uses Basic, with the one-time password unless it is null. Otherwise the token. */
function options(settings, logs) {
  const log = (message) => logs.push(message);
  const credentials =
    'username' in settings
      ? { username: settings.username, password: settings.password, otp: settings.otp ?? undefined }
      : { token: settings.token };
  return {
    baseUrl: settings.base_url,
    ...credentials,
    sudo: settings.sudo ?? undefined,
    userAgent: settings.user_agent,
    timeoutMs: settings.timeout_ms,
    maxRetries: settings.max_retries,
    retryBaseDelayMs: settings.retry_base_delay_ms,
    rateLimitWaitMs: settings.rate_limit_wait_ms,
    maxRetryWaitMs: settings.max_retry_wait_ms,
    fetch: unprefixed,
    logger: { debug: log, info: log },
  };
}

// Every multipart file part in this API is named this; the other parts are text.
const FILE_PART = 'attachment';

/** A form body's fields are named parameters, like query parameters. Multipart file parts go as bytes. */
function args(operation, request) {
  const form = operation.params.some(({ location }) => FORM.includes(location));
  const files = Object.fromEntries(
    Object.entries(request.multipart ?? {}).map(([wire, value]) => [
      wire,
      wire === FILE_PART ? new TextEncoder().encode(value) : value,
    ]),
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
  const client = new GiteaClient(options(settings, logs));
  const operation = OPERATIONS.get(request.operation);
  const resource = client[operation.resource];
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
  const message = error instanceof HttpError ? error.detail : undefined;
  const fields = { kind: error.kind, status: error.status, message, raw_body: error.rawBody };
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
