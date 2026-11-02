import { readFile } from 'node:fs/promises';
import { createInterface } from 'node:readline';
import { fileURLToPath } from 'node:url';
import { parse } from 'yaml';
import { apiPaths } from '../../../toolchain/pipeline/paths.mjs';

const METHODS = ['get', 'put', 'post', 'delete', 'patch'];
const SPEC = apiPaths(fileURLToPath(new URL('..', import.meta.url))).build;
const DEFAULTS = { timeout_ms: 30_000, max_retries: 3, retry_base_delay_ms: 500, rate_limit_wait_ms: 10_000, max_retry_wait_ms: 60_000 };

const spec = parse(await readFile(SPEC, 'utf8'));
const operations = new Map(
  Object.entries(spec.paths).flatMap(([path, item]) =>
    METHODS.filter((method) => item[method]).map((method) => [
      item[method].operationId,
      { method: method.toUpperCase(), path },
    ]),
  ),
);

class ClientError extends Error {
  constructor(fields, retryAfter) {
    super(fields.kind);
    this.fields = fields;
    this.retryAfter = retryAfter;
  }
}

const redact = (client, text) => text.replaceAll(client.token, '***');
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

function parseJson(text) {
  try {
    return JSON.parse(text);
  } catch {
    return undefined;
  }
}

function errorKind(status, headers, json) {
  if (status === 403) {
    if (json?.errors?.[0]?.code === 'bot-need-challenge') return 'bot_challenge';
    return headers.get('cf-ray') && !json ? 'waf_blocked' : 'permission';
  }
  const kinds = { 400: 'bad_request', 401: 'authentication', 404: 'not_found', 422: 'validation', 429: 'rate_limited' };
  return kinds[status] ?? (status >= 500 ? 'server' : 'api');
}

function toError(client, response, text) {
  const json = parseJson(text);
  const fields = {
    kind: errorKind(response.status, response.headers, json),
    status: response.status,
    raw_body: redact(client, text),
  };
  const code = json?.error?.code ?? json?.errors?.[0]?.code;
  if (code !== undefined) fields.code = code;
  if (json?.requestId !== undefined) fields.request_id = json.requestId;
  if (response.headers.has('cf-ray')) fields.cf_ray = response.headers.get('cf-ray');
  return new ClientError(fields, response.headers.get('retry-after'));
}

function decode(response, text) {
  if (text === '') return null;
  if (!response.headers.get('content-type')?.includes('json')) return text;
  const json = parseJson(text);
  if (json === undefined) throw new ClientError({ kind: 'decode', status: response.status });
  return json;
}

function buildRequest(client, { operation, params = {}, body, multipart }) {
  const { method, path } = operations.get(operation);
  const query = new URLSearchParams();
  let filled = path;
  for (const [name, value] of Object.entries(params)) {
    const placeholder = `{${name}}`;
    if (path.includes(placeholder)) filled = filled.replace(placeholder, encodeURIComponent(value));
    else query.set(name, value);
  }
  const headers = {
    Authorization: `Basic ${client.token}`,
    'User-Agent': client.user_agent,
    Accept: 'application/json',
  };
  if (client.locale) headers['Accept-Language'] = client.locale;
  const init = { method, headers };
  if (multipart) {
    init.body = new FormData();
    for (const [name, value] of Object.entries(multipart)) init.body.append(name, value);
  } else if (body !== undefined) {
    init.body = JSON.stringify(body);
    headers['Content-Type'] = 'application/json';
  }
  const search = query.size > 0 ? `?${query}` : '';
  return { url: `${client.base_url}${filled}${search}`, init };
}

async function attempt(client, { url, init }, log) {
  log(`-> ${init.method} ${url} Authorization: ${init.headers.Authorization}`);
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
  return decode(response, text);
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

async function paginate(client, request, log) {
  const params = { ...request.params };
  const items = [];
  for (;;) {
    const page = await call(client, { ...request, params }, log);
    items.push(...page.results);
    if (!page.next) return items;
    if (!URL.canParse(page.next, client.base_url)) throw new ClientError({ kind: 'decode' });
    const next = new URL(page.next, client.base_url).searchParams;
    for (const name of ['page', 'cursor']) {
      if (next.has(name)) params[name] = next.get(name);
    }
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
