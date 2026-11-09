import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { test } from 'node:test';
import { SIGNATURE_HEADER, verifyWebhook, WebhookSignatureError } from 'mercury-banking';

interface WebhookCase {
  name: string;
  header: string;
  body: string;
  now: number;
  tolerance?: number | string;
  error: string | null;
}

type Vectors = { header_name?: string; secret: string; cases: WebhookCase[] };

const read = (path: string): Vectors => JSON.parse(readFileSync(new URL(path, import.meta.url), 'utf8'));
const mercury = read('../../../conformance/webhooks/mercury-signature.json');
const shared = read('../../../../../toolchain/conformance/fixtures/webhooks/hmac-sha256.json');
const valid = mercury.cases[0]!;

test('the header is the one Mercury sends', () => {
  assert.equal(SIGNATURE_HEADER, mercury.header_name);
  assert.equal(SIGNATURE_HEADER, 'Mercury-Signature');
});

for (const [set, { secret, cases }] of [
  ['mercury', mercury],
  ['shared', shared],
] as const) {
  for (const c of cases) {
    test(`webhook vector ${set}: ${c.name}`, async () => {
      const verify = verifyWebhook(new TextEncoder().encode(c.body), c.header, secret, {
        toleranceSeconds: c.tolerance === undefined ? undefined : Number(c.tolerance),
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
}

for (const tolerance of [0, -1, Number.NaN, Number.POSITIVE_INFINITY]) {
  test(`a tolerance of ${tolerance} is rejected`, async () => {
    await assert.rejects(
      verifyWebhook(valid.body, valid.header, mercury.secret, { toleranceSeconds: tolerance, now: valid.now * 1000 }),
      { reason: 'invalid-tolerance' },
    );
  });
}

test('a missing header is malformed', async () => {
  await assert.rejects(verifyWebhook('{}', undefined, mercury.secret), { reason: 'malformed-header' });
});
