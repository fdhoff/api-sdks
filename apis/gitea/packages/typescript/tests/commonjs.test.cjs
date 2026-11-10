const assert = require('node:assert/strict');
const { test } = require('node:test');
const { ApiError, GiteaClient, NotFoundError } = require('gitea-rest');

test('the CommonJS build loads and works', async () => {
  const client = new GiteaClient({
    baseUrl: 'https://gitea.example.test',
    token: 'synthetic-commonjs-access-token',
    fetch: async () => new Response(JSON.stringify({ message: 'synthetic not found' }), { status: 404 }),
  });
  const error = await client.repos.get('synthetic-owner', 'missing').catch((caught) => caught);
  assert.ok(error instanceof NotFoundError);
  assert.ok(error instanceof ApiError);
  assert.equal(error.kind, 'not_found');
});
