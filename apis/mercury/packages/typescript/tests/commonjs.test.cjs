const assert = require('node:assert/strict');
const { test } = require('node:test');
const { ApiError, MercuryClient, NotFoundError, SIGNATURE_HEADER } = require('mercury-banking');

test('the CommonJS build loads and works', async () => {
  const client = new MercuryClient({
    token: 'secret-token:synthetic-commonjs-token',
    hosts: { api: 'http://api.mock.invalid', vault: 'http://vault.mock.invalid' },
    fetch: async () => new Response(null, { status: 404 }),
  });
  const error = await client.recipients.get('00000000-0000-4000-8000-000000000000').catch((caught) => caught);
  assert.ok(error instanceof NotFoundError);
  assert.ok(error instanceof ApiError);
  assert.equal(error.kind, 'not_found');
  assert.equal(SIGNATURE_HEADER, 'Mercury-Signature');
});
