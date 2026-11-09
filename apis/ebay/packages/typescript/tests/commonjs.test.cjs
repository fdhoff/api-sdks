const assert = require('node:assert/strict');
const { test } = require('node:test');
const { ApiError, EbayClient, NotFoundError } = require('ebay-sell');
const { OrdersApi } = require('ebay-sell/fulfillment');

test('the CommonJS build loads and works', async () => {
  const client = new EbayClient({
    clientId: 'synthetic-app-id',
    clientSecret: 'synthetic-cert-id',
    ruName: 'synthetic-ru-name',
    userToken: 'synthetic-user-token',
    hosts: { api: 'http://mock.invalid', apiz: 'http://mock.invalid', apim: 'http://mock.invalid' },
    fetch: async () => new Response(null, { status: 404 }),
  });
  assert.ok(client.fulfillment.orders instanceof OrdersApi);
  const error = await client.fulfillment.orders.get('1').catch((caught) => caught);
  assert.ok(error instanceof NotFoundError);
  assert.ok(error instanceof ApiError);
  assert.equal(error.kind, 'not_found');
  const request = client.oauth.authorizationUrl(['https://api.ebay.com/oauth/api_scope/sell.fulfillment']);
  assert.match(request.url, /^https:\/\/auth\.ebay\.com\/oauth2\/authorize\?/);
});
