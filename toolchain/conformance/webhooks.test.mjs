import assert from 'node:assert/strict';
import { createHmac } from 'node:crypto';
import { readFile } from 'node:fs/promises';
import { test } from 'node:test';

const vectors = JSON.parse(await readFile(new URL('./fixtures/webhooks/hmac-sha256.json', import.meta.url), 'utf8'));
const ERRORS = [null, 'malformed_header', 'too_old', 'bad_signature'];

test('webhook vectors have unique names and known errors', () => {
  const names = vectors.cases.map((c) => c.name);
  assert.equal(new Set(names).size, names.length);
  for (const c of vectors.cases) assert.ok(ERRORS.includes(c.error), c.name);
});

test('webhook vectors sign what they claim', () => {
  for (const c of vectors.cases.filter((c) => c.error !== 'malformed_header')) {
    const entries = c.header.split(',').map((entry) => entry.trim().split('='));
    const t = entries.find(([key]) => key === 't')[1];
    const expected = createHmac('sha256', vectors.secret).update(`${t}.${c.body}`).digest('hex');
    const matches = entries.some(([key, value]) => key === 'v1' && value.toLowerCase() === expected);
    assert.equal(matches, c.error !== 'bad_signature', c.name);
  }
});
