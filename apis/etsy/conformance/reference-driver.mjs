import { readFile } from 'node:fs/promises';
import { createInterface } from 'node:readline';
import { fileURLToPath } from 'node:url';
import { parse } from 'yaml';
import { returnsJson } from '../../../toolchain/pipeline/generate.mjs';
import { apiPaths } from '../../../toolchain/pipeline/paths.mjs';

const METHODS = ['get', 'put', 'post', 'delete', 'patch'];
const SPEC = apiPaths(fileURLToPath(new URL('..', import.meta.url))).build;
const DEFAULTS = { timeout_ms: 30_000, max_retries: 3, retry_base_delay_ms: 500, rate_limit_wait_ms: 10_000, max_retry_wait_ms: 60_000 };
const SECRETS = ['token', 'api_key', 'shared_secret'];

const spec = parse(await readFile(SPEC, 'utf8'));
const operations = new Map(
  Object.entries(spec.paths).flatMap(([path, item]) =>
    METHODS.filter((method) => item[method]).map((method) => {
      const operation = item[method];
      const schemes = (operation.security ?? spec.security ?? []).flatMap((requirement) => Object.keys(requirement));
      return [
        operation.operationId,
        {
          method: method.toUpperCase(),
          path,
          returnsJson: returnsJson(spec, operation),
          bearer: schemes.includes('oauth2'),
          bodyType: Object.keys(operation.requestBody?.content ?? {})[0],
        },
      ];
    }),
  ),
);

class ClientError extends Error {
  constructor(fields, retryAfter) {
    super(fields.kind);
    this.fields = fields;
    this.retryAfter = retryAfter;
  }
}

function redact(client, text) {
  const secrets = SECRETS.map((name) => client[name]).filter(Boolean);
  return secrets.sort((a, b) => b.length - a.length).reduce((out, secret) => out.replaceAll(secret, '***'), text);
}

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

function parseJson(text) {
  try {
    return JSON.parse(text);
  } catch {
    return undefined;
  }
}

function errorKind(status) {
  const kinds = {
    400: 'bad_request',
    401: 'authentication',
    403: 'permission',
    404: 'not_found',
    409: 'conflict',
    422: 'validation',
    429: 'rate_limited',
  };
  return kinds[status] ?? (status >= 500 ? 'server' : 'api');
}

function toError(client, response, text) {
  const json = parseJson(text);
  const fields = { kind: errorKind(response.status), status: response.status, raw_body: redact(client, text) };
  if (typeof json?.error === 'string') fields.message = redact(client, json.error);
  return new ClientError(fields, response.headers.get('retry-after'));
}

function decode(response, text, returnsJson) {
  if (text === '') {
    if (returnsJson) throw new ClientError({ kind: 'decode', status: response.status });
    return null;
  }
  if (!response.headers.get('content-type')?.includes('json')) return text;
  const json = parseJson(text);
  if (json === undefined) throw new ClientError({ kind: 'decode', status: response.status });
  return json;
}

const values = (value) => (Array.isArray(value) ? value : [value]);

function encodeBody(bodyType, body, headers) {
  if (bodyType === 'application/x-www-form-urlencoded') {
    const form = new URLSearchParams();
    for (const [name, value] of Object.entries(body)) values(value).forEach((item) => form.append(name, item));
    return form;
  }
  if (bodyType === 'multipart/form-data') {
    const form = new FormData();
    for (const [name, value] of Object.entries(body)) values(value).forEach((item) => form.append(name, item));
    return form;
  }
  headers['Content-Type'] = 'application/json';
  return JSON.stringify(body);
}

function buildRequest(client, { operation, params = {}, body }) {
  const { method, path, returnsJson, bearer, bodyType } = operations.get(operation);
  const query = new URLSearchParams();
  let filled = path;
  for (const [name, value] of Object.entries(params)) {
    const placeholder = `{${name}}`;
    if (path.includes(placeholder)) filled = filled.replace(placeholder, encodeURIComponent(value));
    else values(value).forEach((item) => query.append(name, item));
  }
  const headers = {
    'x-api-key': `${client.api_key}:${client.shared_secret}`,
    Accept: 'application/json',
    // fetch accepts a gzip body cut short, so ask for none.
    'Accept-Encoding': 'identity',
  };
  if (bearer) headers.Authorization = `Bearer ${client.token}`;
  const init = { method, headers, redirect: 'manual' };
  if (body !== undefined) init.body = encodeBody(bodyType, body, headers);
  const search = query.size > 0 ? `?${query}` : '';
  return { url: `${client.base_url}${filled}${search}`, init, returnsJson };
}

async function attempt(client, { url, init, returnsJson }, log) {
  const auth = init.headers.Authorization ? ` Authorization: ${init.headers.Authorization}` : '';
  log(`-> ${init.method} ${url} x-api-key: ${init.headers['x-api-key']}${auth}`);
  let response;
  let text;
  try {
    response = await fetch(url, { ...init, signal: AbortSignal.timeout(client.timeout_ms) });
    text = await response.text();
  } catch (error) {
    if (!response || !error.cause?.code?.startsWith('Z_')) {
      throw new ClientError({ kind: error.name === 'TimeoutError' ? 'timeout' : 'connection' });
    }
    if (response.ok) throw new ClientError({ kind: 'decode', status: response.status });
    text = '';
  }
  log(`<- ${response.status} ${text}`);
  if (!response.ok) throw toError(client, response, text);
  return decode(response, text, returnsJson);
}

function retryAfterMs(value) {
  if (/^\d+$/.test(value)) return Number(value) * 1000;
  const wait = Date.parse(value) - Date.now();
  return wait > 0 ? wait : null;
}

function retryDelay(client, error, method, tries) {
  if (tries >= client.max_retries) return null;
  const { kind } = error.fields;
  if (kind === 'rate_limited') {
    const wait = retryAfterMs(error.retryAfter);
    if (wait === null) return client.rate_limit_wait_ms;
    return wait <= client.max_retry_wait_ms ? wait : null;
  }
  if (method === 'GET' && ['server', 'timeout', 'connection'].includes(kind)) {
    return client.retry_base_delay_ms * 2 ** tries;
  }
  return null;
}

async function call(client, request, log) {
  const built = buildRequest(client, request);
  for (let tries = 0; ; tries += 1) {
    try {
      return await attempt(client, built, log);
    } catch (error) {
      const delay = retryDelay(client, error, built.init.method, tries);
      if (delay === null) throw error;
      log(`retrying after ${delay}ms: ${error.fields.kind}`);
      await sleep(delay);
    }
  }
}

// Offset paging: advance `offset` by the items received; stop at an empty page or once it reaches `count`.
async function paginate(client, request, log) {
  const params = { ...request.params };
  const items = [];
  for (;;) {
    const page = await call(client, { ...request, params }, log);
    if (!Array.isArray(page?.results)) throw new ClientError({ kind: 'decode' });
    items.push(...page.results);
    const offset = Number(params.offset ?? 0) + page.results.length;
    if (page.results.length === 0 || (typeof page.count === 'number' && offset >= page.count)) return items;
    params.offset = offset;
  }
}

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
