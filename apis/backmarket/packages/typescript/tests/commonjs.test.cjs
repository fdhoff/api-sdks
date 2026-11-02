const assert = require('node:assert/strict');
const { test } = require('node:test');
const { ApiError, BackMarketClient, NotFoundError } = require('backmarket-seller');

test('the CommonJS build loads and works', async () => {
  const client = new BackMarketClient({
    token: 'synthetic-token',
    userAgent: 'BM-Example-Test;test@example.com',
    locale: 'en-us',
    baseUrl: 'http://mock.invalid',
    fetch: async () => new Response(null, { status: 404 }),
  });
  const error = await client.orders.get(1).catch((caught) => caught);
  assert.ok(error instanceof NotFoundError);
  assert.ok(error instanceof ApiError);
  assert.equal(error.kind, 'not_found');
});
