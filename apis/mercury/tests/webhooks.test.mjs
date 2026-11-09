import assert from 'node:assert/strict';
import { createHmac } from 'node:crypto';
import { readFile } from 'node:fs/promises';
import { test } from 'node:test';
import { parse } from 'yaml';
import { verifyWebhook } from '../conformance/reference-driver.mjs';

const read = async (url) => JSON.parse(await readFile(new URL(url, import.meta.url), 'utf8'));
const mercury = await read('../conformance/webhooks/mercury-signature.json');
const shared = await read('../../../toolchain/conformance/fixtures/webhooks/hmac-sha256.json');
const sdk = parse(await readFile(new URL('../sdk.yaml', import.meta.url), 'utf8'));

const run = (vectors) =>
  vectors.cases
    .map((c) => ({ name: c.name, expected: c.error, actual: verifyWebhook(Buffer.from(c.body), c.header, vectors.secret, { now: c.now, tolerance: c.tolerance }) }))
    .filter(({ expected, actual }) => expected !== actual);

test('the Mercury vectors name the header sdk.yaml configures', () => {
  assert.equal(mercury.header_name, sdk.webhooks.header);
});

test('the Mercury vectors cover each outcome and sign what they claim', () => {
  assert.deepEqual([...new Set(mercury.cases.map((c) => c.error))].sort(), ['bad_signature', 'malformed_header', 'too_old', null].sort());
  for (const c of mercury.cases.filter((item) => item.error !== 'malformed_header')) {
    const entries = c.header.split(',').map((entry) => entry.trim().split('='));
    const t = entries.find(([key]) => key === 't')[1];
    const expected = createHmac('sha256', mercury.secret).update(`${t}.${c.body}`).digest('hex');
    assert.equal(entries.some(([key, value]) => key === 'v1' && value === expected), c.error !== 'bad_signature', c.name);
  }
});

test('the reference verifier passes the Mercury and the shared vectors', () => {
  assert.deepEqual(run(mercury), []);
  assert.deepEqual(run(shared), []);
});
