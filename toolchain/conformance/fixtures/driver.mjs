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
function routed(client, request) {
  const operation = OPERATIONS[request.operation];
  const params = { ...request.params };
  const headers = declaredHeaders(operation, client, params);
  for (const name of operation.headers) delete params[name];
  return { url: `${client.base_url}/_host/${operation.host}${operation.path}`, params, headers };
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
  if (mode === 'routed') {
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
