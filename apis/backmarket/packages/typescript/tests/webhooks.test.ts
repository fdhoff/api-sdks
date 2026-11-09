import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { test } from 'node:test';
import { verifyWebhook, WebhookSignatureError } from '../dist/esm/runtime/index.js';

interface WebhookCase {
  name: string;
  header: string;
  body: string;
  now: number;
  tolerance?: number;
  error: string | null;
}

const vectors: { secret: string; cases: WebhookCase[] } = JSON.parse(
  readFileSync(
    new URL('../../../../../toolchain/conformance/fixtures/webhooks/hmac-sha256.json', import.meta.url),
    'utf8',
  ),
);
const { secret } = vectors;
const valid = vectors.cases[0]!;

for (const c of vectors.cases) {
  test(`webhook vector: ${c.name}`, async () => {
    const verify = verifyWebhook(new TextEncoder().encode(c.body), c.header, secret, {
      toleranceSeconds: c.tolerance,
      now: c.now * 1000,
    });
    if (c.error === null) return await verify;
    await assert.rejects(verify, (error: unknown) => {
      assert.ok(error instanceof WebhookSignatureError);
      assert.equal(error.reason, c.error?.replaceAll('_', '-'));
      assert.ok(!error.message.includes(secret) && !error.message.includes(c.body));
      return true;
    });
  });
}

test('webhook defaults to the clock and five minutes', async () => {
  await assert.rejects(verifyWebhook(valid.body, valid.header, secret), { reason: 'too-old' });
});

test('webhook takes a string body and a byte secret', async () => {
  await verifyWebhook(valid.body, valid.header, new TextEncoder().encode(secret), { now: valid.now * 1000 });
});

test('webhook without a header is malformed', async () => {
  await assert.rejects(verifyWebhook('{}', undefined, secret), { reason: 'malformed-header' });
});

test('webhook tolerance must be positive', async () => {
  await assert.rejects(verifyWebhook(valid.body, valid.header, secret, { toleranceSeconds: 0 }), RangeError);
});
