// Conformance driver: reads cases as JSON lines and calls the public client. See the runner's README.
import { createInterface } from 'node:readline';
import { parseArgs } from 'node:util';

const { values } = parseArgs({ options: { format: { type: 'string', default: 'esm' } } });
const dist = new URL(`../dist/${values.format}/`, import.meta.url);
const { ApiError, EtsyClient } = await import(new URL('index.js', dist).href);
const { OPERATIONS } = await import(new URL('resources.js', dist).href);

const FORM = ['form', 'urlencoded'];

function options(settings, logs) {
  const log = (message) => logs.push(message);
  return {
    apiKey: settings.api_key,
    sharedSecret: settings.shared_secret,
    accessToken: settings.token,
    baseUrl: settings.base_url,
    userAgent: settings.user_agent,
    timeoutMs: settings.timeout_ms,
    maxRetries: settings.max_retries,
    retryBaseDelayMs: settings.retry_base_delay_ms,
    rateLimitWaitMs: settings.rate_limit_wait_ms,
    maxRetryWaitMs: settings.max_retry_wait_ms,
    logger: { debug: log, info: log },
  };
}

/** A form body's fields are named parameters, like query parameters. */
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
  const operation = OPERATIONS.get(request.operation);
  const resource = new EtsyClient(options(settings, logs))[operation.resource];
  if (!request.paginate) return resource[operation.name](...args(operation, request));
  const items = [];
  for await (const item of resource[operation.iterator](...args(operation, request))) items.push(item);
  return items;
}

function errorOutput(error) {
  const fields = { kind: error.kind, status: error.status, raw_body: error.rawBody, message: error.detail };
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
