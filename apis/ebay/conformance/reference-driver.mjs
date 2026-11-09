import { createHash, generateKeyPairSync, sign } from 'node:crypto';
import { readFile } from 'node:fs/promises';
import { createInterface } from 'node:readline';
import { fileURLToPath } from 'node:url';
import { parse } from 'yaml';
import { applyHosts, returnsJson } from '../../../toolchain/pipeline/generate.mjs';
import { apiPaths } from '../../../toolchain/pipeline/paths.mjs';

const METHODS = ['get', 'put', 'post', 'delete', 'patch'];
const API_DIR = fileURLToPath(new URL('..', import.meta.url));
const DEFAULTS = { timeout_ms: 30_000, max_retries: 3, retry_base_delay_ms: 500, rate_limit_wait_ms: 10_000, max_retry_wait_ms: 60_000 };
const SECRETS = ['token', 'app_token', 'user_token'];

const sdk = parse(await readFile(new URL('../sdk.yaml', import.meta.url), 'utf8'));
const spec = applyHosts(parse(await readFile(apiPaths(API_DIR).build, 'utf8')), sdk.hosts);
const deref = (value) => (value?.$ref ? deref(value.$ref.split('/').slice(1).reduce((node, key) => node[key], spec)) : value);

// An operation takes an application token when any scope it lists is one the client credentials grant gives.
// eBay lists the scopes an operation accepts, any one of which is enough.
function takesAppToken(operation) {
  return (operation.security ?? []).some((requirement) =>
    Object.entries(requirement).some(([scheme, scopes]) => {
      const granted = Object.keys(spec.components.securitySchemes[scheme]?.flows?.clientCredentials?.scopes ?? {});
      return scopes.some((scope) => granted.includes(scope));
    }),
  );
}

const operations = new Map(
  Object.entries(spec.paths).flatMap(([path, item]) =>
    METHODS.filter((method) => item[method]).map((method) => {
      const operation = item[method];
      const parameters = [...(item.parameters ?? []), ...(operation.parameters ?? [])].map(deref);
      return [
        operation.operationId,
        {
          method: method.toUpperCase(),
          path,
          host: operation['x-sdk-host'],
          returnsJson: returnsJson(spec, operation),
          appToken: takesAppToken(operation),
          headers: new Map(parameters.filter((parameter) => parameter.in === 'header').map(({ name }) => [name.toLowerCase(), name])),
          bodyType: Object.keys(deref(operation.requestBody)?.content ?? {})[0],
          items: sdk.iterators[operation.operationId],
        },
      ];
    }),
  ),
);

// Generated per run, never stored: the cases check the signature's shape and digest, not the key.
const { privateKey } = generateKeyPairSync('ed25519');

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
  const first = parseJson(text)?.errors?.[0];
  const fields = { kind: errorKind(response.status), status: response.status, raw_body: redact(client, text) };
  if (typeof first?.message === 'string') fields.message = redact(client, first.message);
  if (Number.isInteger(first?.errorId)) fields.code = first.errorId;
  return new ClientError(fields, response.headers.get('retry-after'));
}

// 204 never has a body, though most operations that answer it also declare a JSON success.
function decode(response, text, returnsJson) {
  if (text === '') {
    if (returnsJson && response.status !== 204) throw new ClientError({ kind: 'decode', status: response.status });
    return null;
  }
  if (!response.headers.get('content-type')?.includes('json')) return text;
  const json = parseJson(text);
  if (json === undefined) throw new ClientError({ kind: 'decode', status: response.status });
  return json;
}

const values = (value) => (Array.isArray(value) ? value : [value]);

// The exact bytes sent, so the digest covers them, and their content type.
async function encodeBody(bodyType, { body, multipart }) {
  if (multipart !== undefined) {
    const form = new FormData();
    for (const [name, value] of Object.entries(multipart)) values(value).forEach((item) => form.append(name, item));
    const encoded = new Response(form);
    return { bytes: Buffer.from(await encoded.arrayBuffer()), type: encoded.headers.get('content-type') };
  }
  if (bodyType === 'application/octet-stream') return { bytes: Buffer.from(String(body)), type: bodyType };
  return { bytes: Buffer.from(JSON.stringify(body)), type: 'application/json' };
}

// Each host key goes to `<base_url>/_host/<key>`. With an environment, the key is the hostname that
// environment gives it, so a case can check the host map as well as the routing.
function hostBase(client, host) {
  if (client.environment === undefined) return `${client.base_url}/_host/${host}`;
  const url = sdk.environments[client.environment]?.[host];
  if (!url) throw new Error(`Environment ${client.environment} has no ${host} host`);
  return `${client.base_url}/_host/${new URL(url).host}`;
}

async function buildRequest(client, request) {
  const operation = operations.get(request.operation);
  const { method, path, host, returnsJson, appToken, bodyType } = operation;
  const query = new URLSearchParams();
  const headers = {
    Authorization: `Bearer ${appToken ? client.app_token : client.user_token}`,
    Accept: 'application/json',
    // fetch accepts a gzip body cut short, so ask for none.
    'Accept-Encoding': 'identity',
  };
  const given = new Map();
  let filled = path;
  for (const [name, value] of Object.entries(request.params ?? {})) {
    const placeholder = `{${name}}`;
    if (path.includes(placeholder)) filled = filled.replace(placeholder, encodeURIComponent(value));
    else if (operation.headers.has(name.toLowerCase())) given.set(name.toLowerCase(), value);
    else values(value).forEach((item) => query.append(name, item));
  }
  const defaults = new Map(Object.entries(client.header_defaults ?? {}).map(([name, value]) => [name.toLowerCase(), value]));
  for (const [lower, declared] of operation.headers) {
    const value = given.get(lower) ?? defaults.get(lower);
    if (value !== undefined) headers[declared] = String(value);
  }
  let body;
  if (request.body !== undefined || request.multipart !== undefined) {
    body = await encodeBody(bodyType, request);
    headers['Content-Type'] = body.type;
  }
  const search = query.size > 0 ? `?${query}` : '';
  return { url: `${hostBase(client, host)}${filled}${search}`, method, headers, body, returnsJson };
}

// RFC 9421 over eBay's components, with an RFC 9530 digest of the body when there is one.
function signatureHeaders(client, { url, method, body }) {
  const target = new URL(url);
  const headers = { 'x-ebay-signature-key': client.signature_key };
  const lines = [];
  if (body) {
    headers['Content-Digest'] = `sha-256=:${createHash('sha256').update(body.bytes).digest('base64')}:`;
    lines.push(`"content-digest": ${headers['Content-Digest']}`);
  }
  lines.push(`"x-ebay-signature-key": ${client.signature_key}`, `"@method": ${method}`, `"@path": ${target.pathname}`, `"@authority": ${target.host}`);
  const components = lines.map((line) => line.slice(0, line.indexOf(':'))).join(' ');
  const params = `(${components});created=${Math.floor(Date.now() / 1000)}`;
  lines.push(`"@signature-params": ${params}`);
  headers['Signature-Input'] = `sig1=${params}`;
  headers.Signature = `sig1=:${sign(null, Buffer.from(lines.join('\n')), privateKey).toString('base64')}:`;
  return headers;
}

async function attempt(client, built, log) {
  const headers = { ...built.headers, ...(client.signature_key ? signatureHeaders(client, built) : {}) };
  log(`-> ${built.method} ${built.url} Authorization: ${headers.Authorization}`);
  let response;
  let text;
  try {
    response = await fetch(built.url, {
      method: built.method,
      headers,
      body: built.body?.bytes,
      redirect: 'manual',
      signal: AbortSignal.timeout(client.timeout_ms),
    });
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
  return decode(response, text, built.returnsJson);
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
  const built = await buildRequest(client, request);
  for (let tries = 0; ; tries += 1) {
    try {
      return await attempt(client, built, log);
    } catch (error) {
      const delay = retryDelay(client, error, built.method, tries);
      if (delay === null) throw error;
      log(`retrying after ${delay}ms: ${error.fields.kind}`);
      await sleep(delay);
    }
  }
}

// next_link paging: copy the position out of `next` into our own request, never fetching the link itself.
async function paginate(client, request, log) {
  const { items: field } = operations.get(request.operation);
  const { link, params: positions } = sdk.paging;
  const params = { ...request.params };
  const items = [];
  for (;;) {
    const page = await call(client, { ...request, params }, log);
    if (page === null) return items;
    if (!Array.isArray(page?.[field])) throw new ClientError({ kind: 'decode' });
    items.push(...page[field]);
    if (!page[link]) return items;
    if (!URL.canParse(page[link], client.base_url)) throw new ClientError({ kind: 'decode' });
    const next = new URL(page[link], client.base_url).searchParams;
    const before = { ...params };
    for (const name of positions) if (next.has(name)) params[name] = next.get(name);
    if (positions.every((name) => String(params[name]) === String(before[name]))) throw new ClientError({ kind: 'decode' });
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
