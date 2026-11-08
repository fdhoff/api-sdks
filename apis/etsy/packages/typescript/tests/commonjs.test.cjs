const assert = require('node:assert/strict');
const { test } = require('node:test');
const { ApiError, EtsyClient, NotFoundError } = require('etsy-seller');

test('the CommonJS build loads and works', async () => {
  const client = new EtsyClient({
    apiKey: 'synthetic-keystring',
    sharedSecret: 'synthetic-shared-secret',
    baseUrl: 'http://mock.invalid',
    fetch: async () => new Response(null, { status: 404 }),
  });
  const error = await client.shops.get(1).catch((caught) => caught);
  assert.ok(error instanceof NotFoundError);
  assert.ok(error instanceof ApiError);
  assert.equal(error.kind, 'not_found');
  const request = await client.oauth.authorizationUrl('https://example.com/callback', ['shops_r']);
  assert.match(request.url, /^https:\/\/www\.etsy\.com\/oauth\/connect\?/);
});
