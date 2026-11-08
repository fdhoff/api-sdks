import assert from 'node:assert/strict';
import { generateKeyPairSync, verify, type KeyObject } from 'node:crypto';
import { test } from 'node:test';
import { inspect } from 'node:util';
import { ApiError } from 'backmarket-seller';
import {
  contentDigest,
  ED25519,
  MessageSigner,
  redact,
  Resource,
  RSA_V1_5_SHA256,
  Transport,
  type AuthRequest,
  type Credentials,
  type Operation,
} from '../dist/esm/runtime/index.js';

// The published test keys of RFC 9421, Appendix B.1.4 and B.1.1. The RSA key is re-encoded from PKCS #1 to PKCS #8.
const ED25519_KEY = `-----BEGIN PRIVATE KEY-----
MC4CAQAwBQYDK2VwBCIEIJ+DYvh6SEqVTm50DFtMDoQikTmiCqirVv9mWG9qfSnF
-----END PRIVATE KEY-----
`;
const RSA_KEY = `-----BEGIN PRIVATE KEY-----
MIIEwgIBADANBgkqhkiG9w0BAQEFAASCBKwwggSoAgEAAoIBAQCEAph22h6jLzNw
BxHzvgvxydnErMAbB3u/foA+ns+/pDaN2w8FGvBYQGd7Pp3RQMoPAZtzqfF8RcDL
mZuGBqPOvDcw4S3y4Dm3FIqhsGkoN4Es6x0koWowaZcJC8Qbth6ZzENNE/ECV4gC
BhhGNNJ39AHBVb07A0WF6SujdG2WKdXRrvmN9mCSd79iKS1K8sbfiXDbOpcENMLk
0dE5SoZOUwvg+U1lLlGLZThoI3HatQ9FwoiUTQ+4rEjhP4choWm/z6t1Xp5SA6sH
bF4jV1IUWf+ee/k6hkkQgH5Wa4qfcMJRwJlIWVA9JdJ8EOJQaHA7Dvpa5JKx/UPh
v+8ugnXTAgMBAAECggEAb8lm5JZ2hUduLnq+OAKCSODeWQ7Uqs7eet2bqeuAD0/2
po+PG4qhZoo7VwFCUTWlJan9wqdxiAPlbEQKkCdFRcbakbjN2TMJjMCHWL5zfgvq
hmgeyKsrqg1wSce97J1/Mkvn3fh6CbqnwNb6bVFDvTJS3i5FzRhKiv6rUsYm8ZAd
F4XRaYkFkeuHPl7rc+ruUTSAjC4GovxIxoDJFe0r4kbFmkiZOr40e8RZYK7T1IKr
Svzfxx5AjnlK/OZOTCq0L7wBPbMW+IxmQpFCjpI+yuoi3FlZG3LaLNrBMXQF/lLZ
UDHs77q3fAGxDWwum2hKBfdBuUQtjlqwjQlgXPsskQKBiQCyp5QmapcTcs/y1igi
MwgAqJOb2jqmw+VzwKssj0IfRRu5oDYkI4xwI2rxLJhtOqCdaUH1l9wCb9wWkDy1
hyL2bm9grwc3FCv7wVLdCjw31Enx3RTkKzAPMxh9GCEB9QbCaVaPmGnWlDMC6HBs
5cW3EodWww+HPUgG0X1jyO+CqBgctubKK7WbAnkAvSlgXQbvHzWmuUBFRHAejRh/
naQTDV3GnH4lcRHuFBFZCSLn82xQS2/7xFOqfabqq17kNcvKfzdvWpGxxJ2cILAq
0pZS6DmrZlvBU4IkK2ZHCac/XfWVZFh+PrsH/EnVkDpfcYR/iw1F40C1q5w8R6WB
Haew3SApAoGIaiodZsrWpi8HFfZfeRs8OS/0L5x6WBl3Y9btoZgsIeruc9uZ8NXT
IdxaM6FdnyNEyOYA1VH94tDYR+xEt1br1ud/dkPslLV/Aac7d7EaYc7cdkb7oC9t
6sphVg0dqE0UTDlOwBxBYMtGmQbJsFzGpmjzVgKqWqJ3B947li2U7t63HXEvKprY
2wJ4b0DzpSMb5p42dcQgOTU8Mr4S6JOEhRr/YjErMkpaXUEqvZ3jEB9HRmcRi5Gt
t4NBiBMiY6V9br8a5gjEpiAQoIUcWokBMAYjEeurU8M6JLBd3YaZVVjISaFmdtyn
wLFoQxCh6/EC1rSywwrfDpSwO29S9i8XbaapAoGIPkbARLOwU/LcZrQy9mmfcPoQ
lAuCyeu1Q9nH7PYSnbHTFzmiud4Hl8bIXU9a0/58blDoOl3PctF+b4rAEJYUpCOD
u5PFyN6uEFYRg+YQwpjBMkXk8Eb39128ctARB40Lx8caDhRdTyaEedIG3cQDXSpA
l9EOzXkzfx4bZxjAHU9mkMdJwOcMDQ==
-----END PRIVATE KEY-----
`;
const RFC_BODY = new TextEncoder().encode('{"hello": "world"}');
const COVERED = ['content-digest', '@method', '@path', '@authority'];

const upload: Operation = {
  id: 'upload',
  method: 'POST',
  path: '/files',
  resource: 'files',
  name: 'upload',
  params: [{ wire: 'file', name: 'file', location: 'form' }],
  security: [[{ scheme: 'key', scopes: [] }]],
};

const list: Operation = { ...upload, id: 'list', method: 'GET', name: 'list', params: [] };

const authRequest = (method: string, url: string, headers: Record<string, string>, body: Uint8Array): AuthRequest => ({
  method,
  url,
  headers: new Headers(headers),
  body,
  operation: upload,
});

function freshKey(): [string, KeyObject] {
  const { privateKey, publicKey } = generateKeyPairSync('ed25519');
  return [privateKey.export({ type: 'pkcs8', format: 'pem' }).toString(), publicKey];
}

class Signed implements Credentials {
  readonly signer: MessageSigner;

  constructor(signer: MessageSigner) {
    this.signer = signer;
  }

  async apply(request: AuthRequest): Promise<void> {
    request.headers.set('authorization', 'Bearer synthetic-token');
    await this.signer.sign(request);
  }

  secrets(): readonly string[] {
    return ['synthetic-token', ...this.signer.secrets()];
  }
}

class Calls extends Resource {
  run(operation: Operation, params: Record<string, unknown>): Promise<unknown> {
    return this.call(operation, undefined, params);
  }
}

interface Sent {
  url: URL;
  method: string;
  headers: Headers;
  body: Uint8Array;
}

function callsFor(credentials: Credentials, replies: Response[]) {
  const sent: Sent[] = [];
  const transport = new Transport({
    baseUrl: 'https://mock.invalid/v1',
    credentials,
    headers: { 'User-Agent': 'test' },
    toError: (context) => new ApiError(`status ${context.status}`, { status: context.status }),
    fetch: async (input, init = {}) => {
      const body = new Uint8Array(await new Response(init.body).arrayBuffer());
      sent.push({
        url: new URL(String(input)),
        method: init.method ?? 'GET',
        headers: new Headers(init.headers),
        body,
      });
      return replies.shift() as Response;
    },
    timeoutMs: 1000,
    maxRetries: 1,
    retryBaseDelayMs: 1,
    rateLimitWaitMs: 1,
    maxRetryWaitMs: 1,
  });
  return { calls: new Calls(transport), sent };
}

const json = (body: unknown, status = 200): Response =>
  new Response(JSON.stringify(body), { status, headers: { 'content-type': 'application/json' } });

function verifySent(publicKey: KeyObject, request: Sent, components: string[]): void {
  const input = request.headers.get('signature-input') ?? '';
  const [label] = input.split('=', 1);
  const params = input.slice(`${label}=`.length);
  const values: Record<string, string> = {
    'content-digest': request.headers.get('content-digest') ?? '',
    '@method': request.method,
    '@path': request.url.pathname,
    '@authority': request.url.host,
  };
  const base = [...components.map((name) => `"${name}": ${values[name]}`), `"@signature-params": ${params}`].join('\n');
  const signature = (request.headers.get('signature') ?? '').slice(`${label}=:`.length, -1);
  assert.ok(verify(null, Buffer.from(base), publicKey, Buffer.from(signature, 'base64')));
}

test('content digest matches RFC 9530', async () => {
  const body = new TextEncoder().encode('{"hello": "world"}\n');
  assert.equal(await contentDigest(body), 'sha-256=:RK/0qy18MlBSVnWgjwz6lZEWjP/lF5HF9bvEF8FabDg=:');
});

test('ed25519 matches RFC 9421 appendix B.2.6', async () => {
  const signer = await MessageSigner.create({
    privateKey: ED25519_KEY,
    components: ['date', '@method', '@path', '@authority', 'content-type', 'content-length'],
    label: 'sig-b26',
    keyId: 'test-key-ed25519',
    now: () => 1618884473_000,
  });
  const headers = { date: 'Tue, 20 Apr 2021 02:07:55 GMT', 'content-type': 'application/json', 'content-length': '18' };
  const request = authRequest('POST', 'https://example.com/foo?param=Value&Pet=dog', headers, RFC_BODY);
  await signer.sign(request);
  assert.equal(signer.algorithm, ED25519);
  assert.equal(request.headers.get('content-digest'), await contentDigest(RFC_BODY));
  assert.equal(
    request.headers.get('signature-input'),
    'sig-b26=("date" "@method" "@path" "@authority" "content-type" "content-length");created=1618884473;keyid="test-key-ed25519"',
  );
  assert.equal(
    request.headers.get('signature'),
    'sig-b26=:wqcAqbmYJ2ji2glfAMaRy4gruYYnx2nEFN2HN6jrnDnQCK1u02Gb04v9EDgwUPiu4A0w6vuQv5lIp5WPpBKRCw==:',
  );
});

test('rsa matches RFC 9421 section 4.3', async () => {
  const signer = await MessageSigner.create({
    privateKey: RSA_KEY,
    components: ['@method', '@authority', '@path', 'content-digest', 'content-type', 'content-length', 'forwarded'],
    label: 'proxy_sig',
    keyId: 'test-key-rsa',
    includeAlg: true,
    lifetimeSeconds: 60,
    now: () => 1618884480_000,
  });
  // No body, so the signer keeps the RFC's own SHA-512 digest instead of adding one.
  const headers = {
    'content-type': 'application/json',
    'content-length': '18',
    forwarded: 'for=192.0.2.123;host=example.com;proto=https',
    'content-digest':
      'sha-512=:WZDPaVn/7XgHaAy8pmojAkGWoRx2UFChF41A2svX+TaPm+AbwAgBWnrIiYllu7BNNyealdVLvRwEmTHWXvJwew==:',
  };
  const request = authRequest(
    'POST',
    'https://origin.host.internal.example/foo?param=Value&Pet=dog',
    headers,
    new Uint8Array(),
  );
  await signer.sign(request);
  assert.equal(signer.algorithm, RSA_V1_5_SHA256);
  assert.equal(
    request.headers.get('signature-input'),
    'proxy_sig=("@method" "@authority" "@path" "content-digest" "content-type" "content-length" "forwarded")' +
      ';created=1618884480;keyid="test-key-rsa";alg="rsa-v1_5-sha256";expires=1618884540',
  );
  assert.equal(
    request.headers.get('signature'),
    'proxy_sig=:S6ZzPXSdAMOPjN/6KXfXWNO/f7V6cHm7BXYUh3YD/fRad4BCaRZxP+JH+8XY1I6+8Cy+CM5g92iHgxtRPz+MjniOaYmdkDcnL9' +
      'cCpXJleXsOckpURl49GwiyUpZ10KHgOEe11sx3G2gxI8S0jnxQB+Pu68U9vVcasqOWAEObtNKKZd8tSFu7LB5YAv0RAGhB8tmpv7sFnIm9y+7X5' +
      'kXQfi8NMaZaA8i2ZHwpBdg7a6CMfwnnrtflzvZdXAsD3LH2TwevU+/PBPv0B6NMNk93wUs/vfJvye+YuI87HU38lZHowtznbLVdp770I6VHR6Wf' +
      'gS9ddzirrswsE1w5o0LV/g==:',
  );
});

test('each attempt is signed again over its own body', async () => {
  const [privateKey, publicKey] = freshKey();
  let clock = 1700000000_000;
  const signer = await MessageSigner.create({ privateKey, components: COVERED, now: () => (clock += 1000) });
  const replies = [new Response(null, { status: 429, headers: { 'retry-after': '0' } }), json({ id: 1 })];
  const { calls, sent } = callsFor(new Signed(signer), replies);
  assert.deepEqual(await calls.run(upload, { file: new TextEncoder().encode('synthetic') }), { id: 1 });
  assert.equal(sent.length, 2);
  for (const [index, request] of sent.entries()) {
    assert.equal(request.headers.get('content-digest'), await contentDigest(request.body));
    assert.equal(
      request.headers.get('signature-input'),
      `sig1=("content-digest" "@method" "@path" "@authority");created=${1700000001 + index}`,
    );
    verifySent(publicKey, request, COVERED);
  }
});

test('a request without a body has no digest', async () => {
  const [privateKey, publicKey] = freshKey();
  const signer = await MessageSigner.create({ privateKey, components: COVERED, now: () => 1700000000_000 });
  const { calls, sent } = callsFor(new Signed(signer), [json({ id: 1 })]);
  await calls.run(list, {});
  const [request] = sent;
  assert.ok(request);
  assert.equal(request.headers.has('content-digest'), false);
  assert.equal(request.headers.get('signature-input'), 'sig1=("@method" "@path" "@authority");created=1700000000');
  verifySent(publicKey, request, ['@method', '@path', '@authority']);
});

test('rejects unsupported keys and components', async () => {
  const p256 = generateKeyPairSync('ec', { namedCurve: 'P-256' }).privateKey.export({ type: 'pkcs8', format: 'pem' });
  const invalid: [string, string[]][] = [
    [p256.toString(), COVERED],
    ['not a key', COVERED],
    [ED25519_KEY, ['@status']],
    [ED25519_KEY, ['Content-Type']],
    [ED25519_KEY, ['"@query-param";name="Pet"']],
  ];
  for (const [privateKey, components] of invalid) {
    await assert.rejects(MessageSigner.create({ privateKey, components }), TypeError);
  }
  const signer = await MessageSigner.create({ privateKey: ED25519_KEY, components: ['x-missing'] });
  await assert.rejects(signer.sign(authRequest('GET', 'https://example.com/', {}, new Uint8Array())), /x-missing/);
});

test('the private key is a secret', async () => {
  const signer = await MessageSigner.create({ privateKey: ED25519_KEY, components: COVERED });
  const body = 'MC4CAQAwBQYDK2VwBCIEIJ+DYvh6SEqVTm50DFtMDoQikTmiCqirVv9mWG9qfSnF';
  assert.equal(inspect(signer).includes(body), false);
  assert.equal(redact(new Signed(signer), `key ${ED25519_KEY.trim()} and ${body}`), 'key *** and ***');
});
