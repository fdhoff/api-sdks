import { createHash, generateKeyPairSync, sign } from 'node:crypto';
import { createInterface } from 'node:readline';

const mode = process.argv[2];

// Synthetic operations for the routed mode: the host each is served from, and the header parameters it declares.
const OPERATIONS = {
  'list-items': { path: '/items', host: 'main', headers: ['X-Tenant'] },
  'list-files': { path: '/files', host: 'files', headers: [] },
};

// Each declared header takes the call's value, then the client's default in any case, or is not sent.
function declaredHeaders(operation, client, params) {
  const defaults = Object.fromEntries(Object.entries(client.header_defaults ?? {}).map(([name, value]) => [name.toLowerCase(), value]));
  const headers = {};
  for (const name of operation.headers) {
    const value = params[name] ?? defaults[name.toLowerCase()];
    if (value !== undefined) headers[name] = String(value);
  }
  return headers;
}

// Splits a call's params into query parameters and declared headers, and sends every page to the operation's host.
// The `unhosted` mode sends to the base URL instead, and `undefaulted` ignores the client's header defaults.
function routed(client, request) {
  const operation = OPERATIONS[request.operation];
  const params = { ...request.params };
  const headers = declaredHeaders(operation, mode === 'undefaulted' ? {} : client, params);
  for (const name of operation.headers) delete params[name];
  const host = mode === 'unhosted' ? '' : `/_host/${operation.host}`;
  return { url: `${client.base_url}${host}${operation.path}`, params, headers };
}

// Walks offset pages as the runtimes do: advance by the items received, stop at an empty page or the count.
// A page without a `results` list is a decode error.
async function offsetPages(client, params = {}, url = `${client.base_url}/items`, headers = {}) {
  const items = [];
  const query = { ...params };
  for (;;) {
    const search = new URLSearchParams(Object.entries(query).map(([name, value]) => [name, String(value)]));
    const response = await fetch(`${url}${search.size > 0 ? `?${search}` : ''}`, {
      headers: { ...headers, authorization: `Basic ${client.token}` },
    });
    const page = await response.json();
    if (!Array.isArray(page?.results)) return { error: { kind: 'decode' } };
    items.push(...page.results);
    const offset = Number(query.offset ?? 0) + page.results.length;
    if (page.results.length === 0 || (typeof page.count === 'number' && offset >= page.count)) return { result: items };
    query.offset = offset;
  }
}

// Synthetic operations for the cursor mode, each with the paging its cases describe.
const CURSOR_OPERATIONS = {
  'list-items': { path: '/items', items: 'results', next: 'cursor', param: 'cursor' },
  'list-events': { path: '/events', items: 'events', next: 'page.next_page', param: 'start_after' },
};

// Walks cursor pages as the runtimes do: send the value at the `next` path back as `param` until it is null,
// empty or absent, an integer as its decimal digits. A page without its items list, a value that is neither
// a string nor an integer, or a value equal to the one just sent is a decode error.
async function cursorPages(client, request) {
  const operation = CURSOR_OPERATIONS[request.operation];
  const items = [];
  const query = { ...request.params };
  for (;;) {
    const search = new URLSearchParams(Object.entries(query).map(([name, value]) => [name, String(value)]));
    const response = await fetch(`${client.base_url}${operation.path}${search.size > 0 ? `?${search}` : ''}`, {
      headers: { authorization: `Basic ${client.token}` },
    });
    const page = await response.json();
    if (!Array.isArray(page?.[operation.items])) return { error: { kind: 'decode' } };
    items.push(...page[operation.items]);
    const value = operation.next.split('.').reduce((value, key) => value?.[key], page);
    if (value === null || value === undefined || value === '') return { result: items };
    const next = Number.isSafeInteger(value) ? String(value) : value;
    if (typeof next !== 'string' || String(query[operation.param]) === next) return { error: { kind: 'decode' } };
    query[operation.param] = next;
  }
}

const { privateKey } = generateKeyPairSync('ed25519');
const digest = (bytes) => `sha-256=:${createHash('sha256').update(bytes).digest('base64')}:`;

// Signs each attempt as the runtimes' message signer does, retrying once after a rate limit. `wrong-digest`
// digests the body as it would be serialised with spaces, not the bytes sent, and `unsigned` sends a valid
// digest with no signature.
async function signedCall(client, request) {
  const wrongDigest = mode === 'wrong-digest';
  const url = new URL(`${client.base_url}/items`);
  const method = request.body === undefined ? 'GET' : 'POST';
  for (let attempt = 0; ; attempt += 1) {
    const body = request.body === undefined ? undefined : JSON.stringify(request.body);
    const headers = { authorization: `Basic ${client.token}` };
    const covered = ['@method', '@path', '@authority'];
    const lines = [`"@method": ${method}`, `"@path": ${url.pathname}`, `"@authority": ${url.host}`];
    if (body !== undefined) {
      const value = digest(wrongDigest ? JSON.stringify(request.body, null, 1) : body);
      headers['content-type'] = 'application/json';
      headers['content-digest'] = value;
      covered.unshift('content-digest');
      lines.unshift(`"content-digest": ${value}`);
    }
    const params = `(${covered.map((name) => `"${name}"`).join(' ')});created=${Math.floor(Date.now() / 1000)}`;
    lines.push(`"@signature-params": ${params}`);
    if (mode !== 'unsigned') {
      headers['signature-input'] = `sig1=${params}`;
      headers.signature = `sig1=:${sign(null, Buffer.from(lines.join('\n')), privateKey).toString('base64')}:`;
    }
    const response = await fetch(url, { method, headers, body });
    if (response.status !== 429 || attempt > 0) return { result: await response.json() };
  }
}

// Synthetic operations for the binary mode. `text` decodes every body as UTF-8 text, as a client without
// binary support would, which loses bytes that are not valid UTF-8.
async function binaryCall(client, request, text) {
  const headers = { authorization: `Basic ${client.token}` };
  if (request.operation === 'upload-file') {
    const bytes = Buffer.from(request.raw_body_base64, 'base64');
    headers['content-type'] = 'application/octet-stream';
    const body = text ? bytes.toString() : bytes;
    const response = await fetch(`${client.base_url}/upload`, { method: 'POST', headers, body });
    return { result: await response.json() };
  }
  if (request.operation === 'get-report') return { result: await (await fetch(`${client.base_url}/report`, { headers })).text() };
  const response = await fetch(`${client.base_url}/download`, { headers: { ...headers, 'accept-encoding': 'identity' } });
  if (response.status === 404) return { error: { kind: 'not_found', status: 404 } };
  const bytes = text ? Buffer.from(await response.text()) : Buffer.from(await response.arrayBuffer());
  return { result: { content_type: response.headers.get('content-type') ?? '', base64: bytes.toString('base64') } };
}

// Synthetic writes for the idempotent mode, and the body field each one is deduplicated by.
const WRITES = { 'create-transfer': { path: '/transfers', key: 'idempotency_key' }, 'create-item': { path: '/items' } };

// Retries a write after a rate limit, and after a 5xx or a dropped connection only when its key is set, sending the
// same bytes every time. `retry-writes` retries every write as a GET is, and `unretried` only after a rate limit.
async function writeCall(client, request) {
  const write = WRITES[request.operation];
  const body = JSON.stringify(request.body);
  const key = write.key === undefined ? undefined : request.body?.[write.key];
  const keyed = mode === 'retry-writes' || (mode === 'idempotent' && key !== undefined && key !== null && key !== '');
  const headers = { authorization: `Basic ${client.token}`, 'content-type': 'application/json' };
  for (let tries = 0; ; tries += 1) {
    const retry = tries < (client.max_retries ?? 0);
    let response;
    try {
      response = await fetch(`${client.base_url}${write.path}`, { method: 'POST', headers, body });
    } catch {
      if (keyed && retry) continue;
      return { error: { kind: 'connection' } };
    }
    if (response.ok) return { result: await response.json() };
    await response.arrayBuffer();
    if ((response.status === 429 || (keyed && response.status >= 500)) && retry) continue;
    const kind = response.status === 429 ? 'rate_limited' : response.status >= 500 ? 'server' : 'api';
    return { error: { kind, status: response.status } };
  }
}

for await (const line of createInterface({ input: process.stdin })) {
  const { client, request } = JSON.parse(line);
  if (mode === 'silent') {
    console.log(JSON.stringify({ result: { id: 1 }, logs: [] }));
    continue;
  }
  if (['signed', 'wrong-digest', 'unsigned'].includes(mode)) {
    console.log(JSON.stringify({ ...(await signedCall(client, request)), logs: [] }));
    continue;
  }
  if (mode === 'routed' || mode === 'unhosted' || mode === 'undefaulted') {
    const { url, params, headers } = routed(client, request);
    if (request.paginate) {
      console.log(JSON.stringify({ ...(await offsetPages(client, params, url, headers)), logs: [] }));
      continue;
    }
    const search = new URLSearchParams(Object.entries(params).map(([name, value]) => [name, String(value)]));
    const response = await fetch(`${url}${search.size > 0 ? `?${search}` : ''}`, {
      headers: { ...headers, authorization: `Basic ${client.token}` },
    });
    console.log(JSON.stringify({ result: await response.json(), logs: [] }));
    continue;
  }
  if (mode === 'binary' || mode === 'binary-as-text') {
    console.log(JSON.stringify({ ...(await binaryCall(client, request, mode === 'binary-as-text')), logs: [] }));
    continue;
  }
  if (['idempotent', 'retry-writes', 'unretried'].includes(mode)) {
    console.log(JSON.stringify({ ...(await writeCall(client, request)), logs: [] }));
    continue;
  }
  if (mode === 'cursor') {
    console.log(JSON.stringify({ ...(await cursorPages(client, request)), logs: [] }));
    continue;
  }
  if (mode === 'offset') {
    console.log(JSON.stringify({ ...(await offsetPages(client, request.params)), logs: [] }));
    continue;
  }
  const response = await fetch(`${client.base_url}/items`, {
    headers: { authorization: `Basic ${client.token}` },
  });
  const logs = mode === 'leaky' ? [`sent ${client.token}`] : [];
  console.log(JSON.stringify({ result: await response.json(), logs }));
}
