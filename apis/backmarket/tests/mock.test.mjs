import assert from 'node:assert/strict';
import { spawn } from 'node:child_process';
import { after, before, test } from 'node:test';
import { fileURLToPath } from 'node:url';
import { apiPaths } from '../../../toolchain/pipeline/paths.mjs';

const PORT = 4010;
const BASE_URL = `http://127.0.0.1:${PORT}`;
const PRISM = fileURLToPath(new URL('../../../node_modules/.bin/prism', import.meta.url));
const SPEC = apiPaths(fileURLToPath(new URL('..', import.meta.url))).build;
const AUTH = { Authorization: 'Basic synthetic-test-token', Accept: 'application/json' };

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

test('an authenticated request is served', async () => {
  const response = await fetch(`${BASE_URL}/ws/orders/1`, { headers: AUTH });
  assert.equal(response.status, 200);
});

test('a missing Authorization header is refused', async () => {
  const response = await fetch(`${BASE_URL}/ws/orders/1`);
  assert.equal(response.status, 401);
});

test('the overlay secures operations upstream left open', async () => {
  const response = await fetch(`${BASE_URL}/ws/listings_bi`);
  assert.equal(response.status, 401);
});

test('a literal path wins over a templated sibling', async () => {
  const response = await fetch(`${BASE_URL}/ws/buyback/v1/orders/pending-reply`, { headers: AUTH });
  assert.equal(response.status, 200);
  assert.ok('results' in (await response.json()));
});
