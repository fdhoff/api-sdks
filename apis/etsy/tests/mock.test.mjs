import assert from 'node:assert/strict';
import { spawn } from 'node:child_process';
import { after, before, test } from 'node:test';
import { fileURLToPath } from 'node:url';
import { apiPaths } from '../../../toolchain/pipeline/paths.mjs';

const PORT = 4020;
const BASE_URL = `http://127.0.0.1:${PORT}`;
const PRISM = fileURLToPath(new URL('../../../node_modules/.bin/prism', import.meta.url));
const SPEC = apiPaths(fileURLToPath(new URL('..', import.meta.url))).build;
const KEY = { 'x-api-key': 'synthetic-keystring:synthetic-secret', Accept: 'application/json' };
const BEARER = { ...KEY, Authorization: 'Bearer 12345678.synthetic-token' };

let prism;

before(async () => {
  prism = spawn(PRISM, ['mock', SPEC, '--port', String(PORT)], { stdio: 'ignore' });
  for (let attempt = 0; attempt < 100; attempt += 1) {
    try {
      await fetch(BASE_URL);
      return;
    } catch {
      await new Promise((resolve) => setTimeout(resolve, 200));
    }
  }
  throw new Error('Prism did not start');
});

after(() => prism?.kill());

test('a key-only operation is served with the API key alone', async () => {
  const response = await fetch(`${BASE_URL}/v3/application/openapi-ping`, { headers: KEY });
  assert.equal(response.status, 200);
});

test('a missing API key is refused', async () => {
  const response = await fetch(`${BASE_URL}/v3/application/openapi-ping`);
  assert.equal(response.status, 401);
});

test('an OAuth operation needs the bearer token as well', async () => {
  assert.equal((await fetch(`${BASE_URL}/v3/application/users/me`, { headers: KEY })).status, 401);
  assert.equal((await fetch(`${BASE_URL}/v3/application/users/me`, { headers: BEARER })).status, 200);
});

test('any operation can answer 429 with retry-after and the rate-limit headers', async () => {
  const response = await fetch(`${BASE_URL}/v3/application/shops/1`, { headers: { ...KEY, Prefer: 'code=429' } });
  assert.equal(response.status, 429);
  for (const name of ['retry-after', 'x-limit-per-second', 'x-remaining-this-second', 'x-limit-per-day', 'x-remaining-today']) {
    assert.ok(response.headers.has(name), name);
  }
});
