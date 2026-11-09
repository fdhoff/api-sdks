import { createHmac, timingSafeEqual } from 'node:crypto';
import { readFile } from 'node:fs/promises';
import { createInterface } from 'node:readline';
import { fileURLToPath } from 'node:url';
import { parse } from 'yaml';
import { applyBinary, applyHosts, returnsJson } from '../../../toolchain/pipeline/generate.mjs';
import { apiPaths } from '../../../toolchain/pipeline/paths.mjs';

const METHODS = ['get', 'put', 'post', 'delete', 'patch'];
const API_DIR = fileURLToPath(new URL('..', import.meta.url));
const DEFAULTS = { timeout_ms: 30_000, max_retries: 3, retry_base_delay_ms: 500, rate_limit_wait_ms: 10_000, max_retry_wait_ms: 60_000 };
const DEFAULT_TOLERANCE_S = 300;

const sdk = parse(await readFile(new URL('../sdk.yaml', import.meta.url), 'utf8'));

// The timestamped HMAC-SHA256 scheme of `sdk.webhooks.header`, as the runtimes check it: the signature first,
// then the age. Returns null when the signature holds, or why it does not. A tolerance that is not finite and
// positive is rejected before the header is read.
export function verifyWebhook(body, header, secret, { now = Math.floor(Date.now() / 1000), tolerance = DEFAULT_TOLERANCE_S } = {}) {
  const limit = Number(tolerance);
  if (!(Number.isFinite(limit) && limit > 0)) return 'invalid_tolerance';
  const entries = (header ?? '').split(',').map((entry) => entry.trim());
  if (entries.some((entry) => !entry.includes('='))) return 'malformed_header';
  const pairs = entries.map((entry) => [entry.slice(0, entry.indexOf('=')), entry.slice(entry.indexOf('=') + 1)]);
  const stamps = pairs.filter(([key]) => key === 't').map(([, value]) => value);
  const signatures = pairs.filter(([key]) => key === 'v1').map(([, value]) => value);
  if (stamps.length !== 1 || !/^\d{1,12}$/.test(stamps[0]) || signatures.length === 0) return 'malformed_header';
  const expected = createHmac('sha256', secret).update(`${stamps[0]}.`).update(body).digest();
  const valid = signatures.some((value) => /^[0-9a-f]{64}$/i.test(value) && timingSafeEqual(Buffer.from(value, 'hex'), expected));
  if (!valid) return 'bad_signature';
  return now - Number(stamps[0]) > limit ? 'too_old' : null;
}

let operations;

async function loadOperations() {
  const declared = applyHosts(parse(await readFile(apiPaths(API_DIR).build, 'utf8')), sdk.hosts);
  const deref = (value) => (value?.$ref ? deref(value.$ref.split('/').slice(1).reduce((node, key) => node[key], declared)) : value);
  // The media type each operation's success declares, read before applyBinary drops it.
  const accepts = new Map(
    Object.values(declared.paths).flatMap((item) =>
      METHODS.filter((method) => item[method]).map((method) => {
        const success = Object.entries(item[method].responses).find(([status]) => status.startsWith('2'));
        return [item[method].operationId, Object.keys(deref(success?.[1])?.content ?? {})[0]];
      }),
    ),
  );
  const spec = applyBinary(declared);
  return new Map(
    Object.entries(spec.paths).flatMap(([path, item]) =>
      METHODS.filter((method) => item[method]).map((method) => {
        const operation = item[method];
        const id = operation.operationId;
        const iterator = sdk.iterators[id];
        return [
          id,
          {
            method: method.toUpperCase(),
            path,
            host: operation['x-sdk-host'],
            binary: operation['x-sdk-binary-response'] === true,
            accept: accepts.get(id),
            returnsJson: returnsJson(spec, operation),
            multipart: Object.keys(deref(operation.requestBody)?.content ?? {}).includes('multipart/form-data'),
            items: iterator?.items,
            paging: iterator && { ...sdk.paging, ...iterator.paging },
            idempotencyKey: sdk.idempotency[id]?.body,
          },
        ];
      }),
    ),
  );
}

class ClientError extends Error {
  constructor(fields, retryAfter) {
    super(fields.kind);
    this.fields = fields;
    this.retryAfter = retryAfter;
  }
}

const redact = (client, text) => (client.token ? text.replaceAll(client.token, '***') : text);
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

function errorKind(status) {
  const kinds = { 400: 'bad_request', 401: 'authentication', 403: 'permission', 404: 'not_found', 409: 'conflict', 422: 'validation', 429: 'rate_limited' };
  return kinds[status] ?? (status >= 500 ? 'server' : 'api');
}

// Mercury declares no error body, so the error keeps the status and the raw text.
const toError = (client, response, text) =>
  new ClientError({ kind: errorKind(response.status), status: response.status, raw_body: redact(client, text) }, response.headers.get('retry-after'));

function decode(response, bytes, operation) {
  if (operation.binary) return { content_type: response.headers.get('content-type') ?? '', base64: bytes.toString('base64') };
  const text = bytes.toString('utf8');
  if (text === '') {
    if (operation.returnsJson && response.status !== 204) throw new ClientError({ kind: 'decode', status: response.status });
    return null;
  }
  if (!response.headers.get('content-type')?.includes('json')) return text;
  try {
    return JSON.parse(text);
  } catch {
    throw new ClientError({ kind: 'decode', status: response.status });
  }
}

const values = (value) => (Array.isArray(value) ? value : [value]);

function encodeBody(operation, { body, multipart }) {
  if (multipart !== undefined) {
    const form = new FormData();
    for (const [name, value] of Object.entries(multipart)) values(value).forEach((item) => form.append(name, item));
    return { body: form };
  }
  if (body === undefined) return {};
  return { body: JSON.stringify(body), type: 'application/json' };
}

// With an environment, the host key's requests go to the hostname that environment gives it.
function hostBase(client, host) {
  if (client.environment === undefined) return `${client.base_url}/_host/${host}`;
  const url = sdk.environments[client.environment]?.[host];
  if (!url) throw new Error(`Environment ${client.environment} has no ${host} host`);
  return `${client.base_url}/_host/${new URL(url).host}`;
}

function buildRequest(client, request) {
  const operation = operations.get(request.operation);
  const query = new URLSearchParams();
  let path = operation.path;
  for (const [name, value] of Object.entries(request.params ?? {})) {
    if (path.includes(`{${name}}`)) path = path.replace(`{${name}}`, encodeURIComponent(value));
    else values(value).forEach((item) => query.append(name, String(item)));
  }
  const headers = {
    Authorization: `Bearer ${client.token}`,
    Accept: operation.accept ?? 'application/json',
    // fetch accepts a gzip body cut short, so ask for none.
    'Accept-Encoding': 'identity',
  };
  const { body, type } = encodeBody(operation, request);
  if (type) headers['Content-Type'] = type;
  const key = operation.idempotencyKey && request.body?.[operation.idempotencyKey];
  const search = query.size > 0 ? `?${query}` : '';
  return { operation, url: `${hostBase(client, operation.host)}${path}${search}`, headers, body, retryable: operation.method === 'GET' || (typeof key === 'string' && key !== '') };
}

// Logs the method, URL and size only: a body may hold card numbers.
async function attempt(client, built, log) {
  const { operation } = built;
  log(`-> ${operation.method} ${built.url}`);
  let response;
  let bytes;
  try {
    response = await fetch(built.url, { method: operation.method, headers: built.headers, body: built.body, redirect: 'manual', signal: AbortSignal.timeout(client.timeout_ms) });
    bytes = Buffer.from(await response.arrayBuffer());
  } catch (error) {
    throw new ClientError({ kind: error.name === 'TimeoutError' ? 'timeout' : 'connection' });
  }
  log(`<- ${operation.method} ${response.status} (${bytes.length} bytes)`);
  if (!response.ok) throw toError(client, response, bytes.toString('utf8'));
  return decode(response, bytes, operation);
}

function retryAfterMs(value) {
  if (/^\d+$/.test(value ?? '')) return Number(value) * 1000;
  const wait = Date.parse(value) - Date.now();
  return wait > 0 ? wait : null;
}

function retryDelay(client, error, retryable, tries) {
  if (tries >= client.max_retries) return null;
  const { kind } = error.fields;
  if (kind === 'rate_limited') {
    const wait = retryAfterMs(error.retryAfter);
    if (wait === null) return client.rate_limit_wait_ms;
    return wait <= client.max_retry_wait_ms ? wait : null;
  }
  if (retryable && ['server', 'timeout', 'connection'].includes(kind)) return client.retry_base_delay_ms * 2 ** tries;
  return null;
}

async function call(client, request, log) {
  const built = buildRequest(client, request);
  for (let tries = 0; ; tries += 1) {
    try {
      return await attempt(client, built, log);
    } catch (error) {
      const delay = retryDelay(client, error, built.retryable, tries);
      if (delay === null) throw error;
      log(`retrying after ${delay}ms: ${error.fields.kind}`);
      await sleep(delay);
    }
  }
}

// A next value is a string ID, or an integer sequence number as the treasury cursor is.
// TODO: the toolchain runtimes accept only a string; they need the integer form before any language passes.
function nextPosition(page, path) {
  const next = path.split('.').reduce((value, key) => value?.[key], page);
  if (next === null || next === undefined || next === '') return null;
  if (typeof next === 'string' || Number.isInteger(next)) return String(next);
  throw new ClientError({ kind: 'decode' });
}

async function paginate(client, request, log) {
  const { items: field, paging } = operations.get(request.operation);
  const params = { ...request.params };
  const items = [];
  for (;;) {
    const page = await call(client, { ...request, params }, log);
    if (!Array.isArray(page?.[field])) throw new ClientError({ kind: 'decode' });
    items.push(...page[field]);
    if (paging.style === 'offset') {
      const offset = Number(params[paging.offset ?? 'offset'] ?? 0) + page[field].length;
      if (page[field].length === 0 || (typeof page[paging.total] === 'number' && offset >= page[paging.total])) return items;
      params[paging.offset ?? 'offset'] = offset;
      continue;
    }
    const next = nextPosition(page, paging.next);
    if (next === null) return items;
    if (String(params[paging.param]) === next) throw new ClientError({ kind: 'decode' });
    params[paging.param] = next;
  }
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  operations = await loadOperations();
  for await (const line of createInterface({ input: process.stdin })) {
    const { client: settings, request } = JSON.parse(line);
    const client = { ...DEFAULTS, ...settings };
    const logs = [];
    const log = (entry) => logs.push(redact(client, entry));
    try {
      const result = await (request.paginate ? paginate : call)(client, request, log);
      console.log(JSON.stringify({ result, logs }));
    } catch (error) {
      if (!(error instanceof ClientError)) throw error;
      console.log(JSON.stringify({ error: error.fields, logs }));
    }
  }
}
