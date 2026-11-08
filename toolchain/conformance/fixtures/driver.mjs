import { createHash, generateKeyPairSync, sign } from 'node:crypto';
import { createInterface } from 'node:readline';

const mode = process.argv[2];

// Walks offset pages as the runtimes do: advance by the items received, stop at an empty page or the count.
// A page without a `results` list is a decode error.
async function offsetPages(client, params = {}) {
  const items = [];
  const query = { ...params };
  for (;;) {
    const search = new URLSearchParams(Object.entries(query).map(([name, value]) => [name, String(value)]));
    const response = await fetch(`${client.base_url}/items${search.size > 0 ? `?${search}` : ''}`, {
      headers: { authorization: `Basic ${client.token}` },
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

// Signs each attempt as the runtimes' message signer does, retrying once after a rate limit. `wrongDigest`
// digests the body as it would be serialised with spaces, not the bytes sent.
async function signedCall(client, request, wrongDigest) {
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
    headers['signature-input'] = `sig1=${params}`;
    headers.signature = `sig1=:${sign(null, Buffer.from(lines.join('\n')), privateKey).toString('base64')}:`;
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
  if (mode === 'signed' || mode === 'wrong-digest') {
    console.log(JSON.stringify({ ...(await signedCall(client, request, mode === 'wrong-digest')), logs: [] }));
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
