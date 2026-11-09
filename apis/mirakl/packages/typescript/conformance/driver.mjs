// Conformance driver: reads cases as JSON lines and calls the public client. See the runner's README.
import { readFile } from 'node:fs/promises';
import { createInterface } from 'node:readline';
import { parseArgs } from 'node:util';
import { parse } from 'yaml';

const { values } = parseArgs({ options: { format: { type: 'string', default: 'esm' } } });
const dist = new URL(`../dist/${values.format}/`, import.meta.url);
const { ApiError, MiraklClient } = await import(new URL('index.js', dist).href);
const { OPERATIONS } = await import(new URL('resources.js', dist).href);
// The wait method of each job's status operation, which the generated operations do not name.
const names = parse(await readFile(new URL('../operations.yaml', import.meta.url), 'utf8'));

const FORM = ['form', 'urlencoded'];

function options(settings, logs) {
  const log = (message) => logs.push(message);
  return {
    baseUrl: settings.base_url,
    apiKey: settings.token,
    shopId: settings.query_defaults?.shop_id,
    userAgent: settings.user_agent,
    timeoutMs: settings.timeout_ms,
    maxRetries: settings.max_retries,
    retryBaseDelayMs: settings.retry_base_delay_ms,
    rateLimitWaitMs: settings.rate_limit_wait_ms,
    maxRetryWaitMs: settings.max_retry_wait_ms,
    logger: { debug: log, info: log },
  };
}

// Every multipart file part in this API is named one of these; the other parts are text.
const FILE_PARTS = ['file', 'files'];
const bytes = (value) => (Array.isArray(value) ? value.map(bytes) : new TextEncoder().encode(value));

/** A form body's fields are named parameters, like query parameters. Multipart file parts go as bytes. */
function args(operation, request) {
  const form = operation.params.some(({ location }) => FORM.includes(location));
  const files = Object.fromEntries(
    Object.entries(request.multipart ?? {}).map(([wire, value]) => [
      wire,
      FILE_PARTS.includes(wire) ? bytes(value) : value,
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

const binary = async (download) => ({
  content_type: download.contentType,
  base64: Buffer.from(await download.bytes()).toString('base64'),
});

async function run(message, logs) {
  const { request, client: settings } = message;
  const client = new MiraklClient(options(settings, logs));
  if (request.download !== undefined) return binary(await client.downloadUrl(request.download));
  const operation = OPERATIONS.get(request.operation);
  const resource = client[operation.resource];
  if (request.wait) {
    const path = args(operation, request).slice(
      0,
      operation.params.filter(({ location }) => location === 'path').length,
    );
    const wait = { intervalMs: settings.poll_interval_ms, timeoutMs: settings.poll_timeout_ms };
    return resource[names[operation.id].wait](...path, wait);
  }
  if (!request.paginate) {
    const result = await resource[operation.name](...args(operation, request));
    return operation.returnsBinary ? binary(result) : result;
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
