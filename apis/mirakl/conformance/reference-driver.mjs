import { readFile } from 'node:fs/promises';
import { createInterface } from 'node:readline';
import { fileURLToPath } from 'node:url';
import { parse } from 'yaml';
import { applyBinary, returnsJson } from '../../../toolchain/pipeline/generate.mjs';
import { apiPaths } from '../../../toolchain/pipeline/paths.mjs';

const METHODS = ['get', 'put', 'post', 'delete', 'patch'];
const API_DIR = fileURLToPath(new URL('..', import.meta.url));
const DEFAULTS = {
  timeout_ms: 30_000,
  max_retries: 3,
  retry_base_delay_ms: 500,
  rate_limit_wait_ms: 10_000,
  max_retry_wait_ms: 60_000,
  query_defaults: {},
  poll_interval_ms: 60_000,
  poll_timeout_ms: 3_600_000,
};
const MAX_REDIRECTS = 5;

const sdk = parse(await readFile(new URL('../sdk.yaml', import.meta.url), 'utf8'));
// Each status operation to the job it reports.
const jobs = new Map(Object.values(sdk.jobs ?? {}).map((job) => [job.status, job]));

let operations;

async function loadOperations() {
  const declared = parse(await readFile(apiPaths(API_DIR).build, 'utf8'));
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
        const query = (operation.parameters ?? []).map(deref).filter((parameter) => parameter.in === 'query').map((parameter) => parameter.name);
        return [
          id,
          {
            method: method.toUpperCase(),
            path,
            binary: operation['x-sdk-binary-response'] === true,
            accept: accepts.get(id),
            returnsJson: returnsJson(spec, operation),
            multipart: Object.keys(deref(operation.requestBody)?.content ?? {}).includes('multipart/form-data'),
            defaults: (sdk.query_defaults ?? []).filter((name) => query.includes(name)),
            items: iterator?.items,
            paging: iterator && { ...sdk.paging, ...iterator.paging },
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

// The docs define no error body, so the error keeps the status and the raw text.
const toError = (client, response, text) =>
  new ClientError({ kind: errorKind(response.status), status: response.status, raw_body: redact(client, text) }, response.headers.get('retry-after'));

const binaryResult = (response, bytes) => ({ content_type: response.headers.get('content-type') ?? '', base64: bytes.toString('base64') });

function decode(response, bytes, operation) {
  if (operation.binary) return binaryResult(response, bytes);
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

function encodeBody({ body, multipart }) {
  if (multipart !== undefined) {
    const form = new FormData();
    for (const [name, value] of Object.entries(multipart)) values(value).forEach((item) => form.append(name, item));
    return { body: form };
  }
  if (body === undefined) return {};
  return { body: JSON.stringify(body), type: 'application/json' };
}

// The key goes in the Authorization header as it is, with no scheme in front.
const credentials = (client) => ({ Authorization: client.token });

function buildRequest(client, request) {
  const operation = operations.get(request.operation);
  const query = new URLSearchParams();
  let path = operation.path;
  // A client-level value fills a query parameter the call leaves unset.
  const defaults = Object.fromEntries(operation.defaults.filter((name) => client.query_defaults[name] !== undefined).map((name) => [name, client.query_defaults[name]]));
  for (const [name, value] of Object.entries({ ...defaults, ...request.params })) {
    if (path.includes(`{${name}}`)) path = path.replace(`{${name}}`, encodeURIComponent(value));
    else values(value).forEach((item) => query.append(name, String(item)));
  }
  const headers = {
    ...credentials(client),
    Accept: operation.accept ?? 'application/json',
    // fetch accepts a gzip body cut short, so ask for none.
    'Accept-Encoding': 'identity',
  };
  const { body, type } = encodeBody(request);
  if (type) headers['Content-Type'] = type;
  const search = query.size > 0 ? `?${query}` : '';
  const url = `${client.base_url}${path}${search}`;
  return { operation, url, logged: url, headers, body, retryable: operation.method === 'GET' };
}

// Logs the method, URL and size only.
async function attempt(client, built, log) {
  const { operation } = built;
  log(`-> ${operation.method} ${built.logged}`);
  let response;
  let bytes;
  try {
    response = await fetch(built.url, { method: operation.method, headers: built.headers, body: built.body, redirect: 'manual', signal: AbortSignal.timeout(client.timeout_ms) });
    bytes = Buffer.from(await response.arrayBuffer());
  } catch (error) {
    throw new ClientError({ kind: error.name === 'TimeoutError' ? 'timeout' : 'connection' });
  }
  log(`<- ${operation.method} ${response.status} (${bytes.length} bytes)`);
  return { response, bytes };
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

async function retrying(client, built, log, send) {
  for (let tries = 0; ; tries += 1) {
    try {
      return await send();
    } catch (error) {
      const delay = retryDelay(client, error, built.retryable, tries);
      if (delay === null) throw error;
      log(`retrying after ${delay}ms: ${error.fields.kind}`);
      await sleep(delay);
    }
  }
}

async function call(client, request, log) {
  const built = buildRequest(client, request);
  return retrying(client, built, log, async () => {
    const { response, bytes } = await attempt(client, built, log);
    if (!response.ok) throw toError(client, response, bytes.toString('utf8'));
    return decode(response, bytes, built.operation);
  });
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
    const next = page[paging.next];
    if (next === null || next === undefined || next === '') return items;
    if (typeof next !== 'string' || params[paging.param] === next) throw new ClientError({ kind: 'decode' });
    params[paging.param] = next;
  }
}

const field = (value, path) => path.split('.').reduce((node, key) => node?.[key], value);

// Calls the status operation at once, returns when the state is final, done or failed, and otherwise waits the
// interval, never past the deadline.
async function wait(client, request, log) {
  const job = jobs.get(request.operation);
  if (!job) throw new Error(`${request.operation} reports no job`);
  const deadline = Date.now() + client.poll_timeout_ms;
  for (;;) {
    const status = await call(client, request, log);
    if ([...job.done, ...job.failed].includes(field(status, job.state))) return status;
    const remaining = deadline - Date.now();
    if (remaining <= 0) throw new ClientError({ kind: 'job_timeout' });
    await sleep(Math.min(client.poll_interval_ms, remaining));
  }
}

// Gets a URL a response returned. The key goes only to the base URL's scheme, host and port, and never again once
// a redirect leaves it. The log leaves out the query, which may hold a signature.
async function download(client, target, log) {
  const origin = new URL(client.base_url).origin;
  const operation = { method: 'GET', binary: true };
  let url = new URL(target);
  let trusted = url.origin === origin;
  for (let hops = 0; ; hops += 1) {
    const headers = { ...(trusted ? credentials(client) : {}), 'Accept-Encoding': 'identity' };
    const built = { operation, url: url.href, logged: `${url.origin}${url.pathname}`, headers, retryable: true };
    const { response, bytes } = await retrying(client, built, log, async () => {
      const sent = await attempt(client, built, log);
      if (!sent.response.ok && !(sent.response.status >= 300 && sent.response.status < 400)) throw toError(client, sent.response, sent.bytes.toString('utf8'));
      return sent;
    });
    const location = response.headers.get('location');
    if (response.status < 300 || response.status >= 400) return binaryResult(response, bytes);
    if (!location || hops >= MAX_REDIRECTS) throw toError(client, response, bytes.toString('utf8'));
    url = new URL(location, url);
    trusted = trusted && url.origin === origin;
  }
}

function run(client, request, log) {
  if (request.download !== undefined) return download(client, request.download, log);
  if (request.wait) return wait(client, request, log);
  return (request.paginate ? paginate : call)(client, request, log);
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  operations = await loadOperations();
  for await (const line of createInterface({ input: process.stdin })) {
    const { client: settings, request } = JSON.parse(line);
    const client = { ...DEFAULTS, ...settings };
    const logs = [];
    const log = (entry) => logs.push(redact(client, entry));
    try {
      const result = await run(client, request, log);
      console.log(JSON.stringify({ result, logs }));
    } catch (error) {
      if (!(error instanceof ClientError)) throw error;
      console.log(JSON.stringify({ error: error.fields, logs }));
    }
  }
}
