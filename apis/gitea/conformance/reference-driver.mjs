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
};

const sdk = parse(await readFile(new URL('../sdk.yaml', import.meta.url), 'utf8'));

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
        return [
          id,
          {
            method: method.toUpperCase(),
            path,
            binary: operation['x-sdk-binary-response'] === true,
            accept: accepts.get(id),
            returnsJson: returnsJson(spec, operation),
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

const basic = (client) => Buffer.from(`${client.username}:${client.password}`).toString('base64');

// Every credential the client holds, and the Basic header value that encodes the password.
function secretsOf(client) {
  const secrets = [client.token, client.password, client.otp];
  if (client.username !== undefined) secrets.push(basic(client));
  return secrets.filter((value) => typeof value === 'string' && value !== '');
}

const redact = (client, text) => secretsOf(client).reduce((redacted, secret) => redacted.replaceAll(secret, '***'), text);
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

function errorKind(status) {
  const kinds = { 400: 'bad_request', 401: 'authentication', 403: 'permission', 404: 'not_found', 409: 'conflict', 422: 'validation', 429: 'rate_limited' };
  return kinds[status] ?? (status >= 500 ? 'server' : 'api');
}

// Gitea's errors are JSON with a `message`, which the error carries beside the status and the raw text.
function toError(client, response, text) {
  let message;
  try {
    const body = JSON.parse(text);
    if (typeof body?.message === 'string') message = redact(client, body.message);
  } catch {
    // Not JSON: the raw text is all there is.
  }
  const fields = { kind: errorKind(response.status), status: response.status, raw_body: redact(client, text), ...(message === undefined ? {} : { message }) };
  return new ClientError(fields, response.headers.get('retry-after'));
}

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

// An access token goes as `Authorization: token <token>`. A username switches to Basic, which alone may carry a
// one-time password. Sudo goes with either.
function credentials(client) {
  const headers = {};
  if (client.username !== undefined) {
    headers.Authorization = `Basic ${basic(client)}`;
    if (client.otp) headers['X-GITEA-OTP'] = client.otp;
  } else {
    headers.Authorization = `token ${client.token}`;
  }
  if (client.sudo) headers.Sudo = client.sudo;
  return headers;
}

// Every path parameter is one encoded segment, so a `/` in a file path is sent as %2F.
function buildRequest(client, request) {
  const operation = operations.get(request.operation);
  const query = new URLSearchParams();
  let path = operation.path;
  for (const [name, value] of Object.entries(request.params ?? {})) {
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

// The decoded body, and the response it came from.
async function exchange(client, request, log) {
  const built = buildRequest(client, request);
  return retrying(client, built, log, async () => {
    const { response, bytes } = await attempt(client, built, log);
    if (!response.ok) throw toError(client, response, bytes.toString('utf8'));
    return { value: decode(response, bytes, built.operation), response };
  });
}

const call = async (client, request, log) => (await exchange(client, request, log)).value;

// Splits on `separator` outside <URI> and quoted strings, as an RFC 8288 Link header is read.
function splitOutside(text, separator) {
  const parts = [];
  let [start, quoted, bracketed, escaped] = [0, false, false, false];
  [...text].forEach((char, index) => {
    if (quoted) {
      if (escaped) escaped = false;
      else if (char === '\\') escaped = true;
      else if (char === '"') quoted = false;
    } else if (bracketed) bracketed = char !== '>';
    else if (char === '"') quoted = true;
    else if (char === '<') bracketed = true;
    else if (char === separator) {
      parts.push(text.slice(start, index));
      start = index + 1;
    }
  });
  return [...parts, text.slice(start)];
}

// The URI of the first link whose `rel` holds `rel`, in any case.
function linkFor(header, rel) {
  for (const entry of splitOutside(header ?? '', ',').map((part) => part.trim())) {
    const end = entry.indexOf('>');
    if (!entry.startsWith('<') || end < 0) continue;
    const param = splitOutside(entry.slice(end + 1), ';').slice(1).map((item) => item.split('=')).find(([name]) => name.trim().toLowerCase() === 'rel');
    const value = param?.slice(1).join('=').trim().replace(/^"(.*)"$/, '$1').replace(/\\(.)/g, '$1') ?? '';
    if (value.toLowerCase().split(/\s+/).includes(rel)) return entry.slice(1, end);
  }
  return undefined;
}

// Copies only the paging parameters out of each page's `next` link into our own next request. The link is never
// fetched: its host is the server's configured root URL, which can differ from the client's.
async function paginate(client, request, log) {
  const { items: field, paging } = operations.get(request.operation);
  const params = { ...request.params };
  const items = [];
  const seen = new Set();
  for (;;) {
    const position = JSON.stringify(paging.params.map((name) => (params[name] === undefined ? null : String(params[name]))));
    if (seen.has(position)) throw new ClientError({ kind: 'decode' });
    seen.add(position);
    const { value: page, response } = await exchange(client, { ...request, params }, log);
    const received = field === '$' ? page : page?.[field];
    if (!Array.isArray(received)) throw new ClientError({ kind: 'decode' });
    items.push(...received);
    const link = linkFor(response.headers.get('link'), paging.rel);
    if (link === undefined) return items;
    const next = new URL(link, 'http://next.invalid').searchParams;
    for (const name of paging.params) if (next.get(name)) params[name] = next.get(name);
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
