const assert = require('node:assert/strict');
const { test } = require('node:test');
const { ApiError, MiraklClient, NotFoundError } = require('mirakl-seller');

test('the CommonJS build loads and works', async () => {
  const client = new MiraklClient({
    baseUrl: 'http://operator.mock.invalid',
    apiKey: 'synthetic-commonjs-shop-key',
    fetch: async () => new Response(null, { status: 404 }),
  });
  const error = await client.offers.get(1).catch((caught) => caught);
  assert.ok(error instanceof NotFoundError);
  assert.ok(error instanceof ApiError);
  assert.equal(error.kind, 'not_found');
});
