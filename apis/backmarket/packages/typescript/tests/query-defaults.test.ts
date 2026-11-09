import assert from 'node:assert/strict';
import { test } from 'node:test';
import { ApiError } from 'backmarket-seller';
import { Resource, Transport, type Credentials, type Operation, type Settings } from '../dist/esm/runtime/index.js';

const BASE = 'http://main.invalid';

const getItem: Operation = {
  id: 'get-item',
  method: 'GET',
  path: '/items/{id}',
  resource: 'items',
  name: 'get',
  params: [
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'site', name: 'site', location: 'query', defaulted: true },
  ],
  returnsJson: true,
};

const listItems: Operation = {
  id: 'list-items',
  method: 'GET',
  path: '/items',
  resource: 'items',
  name: 'list',
  params: [
    { wire: 'site', name: 'site', location: 'query', defaulted: true },
    { wire: 'after', name: 'after', location: 'query' },
  ],
  returnsJson: true,
  paging: { style: 'cursor', items: 'results', next: 'next', param: 'after' },
};

const listFiles: Operation = {
  ...listItems,
  id: 'list-files',
  path: '/files',
  params: [{ wire: 'site', name: 'site', location: 'query' }],
};

const credentials: Credentials = {
  apply(request) {
    request.headers.set('authorization', 'Bearer synthetic');
  },
  secrets: () => [],
};

class Calls extends Resource {
  run(operation: Operation, params: Record<string, unknown> = {}): Promise<unknown> {
    return this.call(operation, undefined, params);
  }

  async all(operation: Operation, params: Record<string, unknown> = {}): Promise<unknown[]> {
    const items: unknown[] = [];
    for await (const item of this.paginate(operation, undefined, params)) items.push(item);
    return items;
  }
}

function callsWith(queryDefaults: Settings['queryDefaults'], replies: unknown[] = []) {
  const sent: string[] = [];
  const transport = new Transport({
    baseUrl: BASE,
    queryDefaults,
    credentials,
    headers: {},
    toError: (context) => new ApiError(`status ${context.status}`, { status: context.status }),
    fetch: async (input) => {
      sent.push(String(input));
      const body = replies.shift() ?? { results: [] };
      return new Response(JSON.stringify(body), { status: 200, headers: { 'content-type': 'application/json' } });
    },
    timeoutMs: 1000,
    maxRetries: 0,
    retryBaseDelayMs: 1,
    rateLimitWaitMs: 1,
    maxRetryWaitMs: 1,
  });
  return { calls: new Calls(transport), sent };
}

test('a query default is sent unless the call gives a value', async () => {
  const { calls, sent } = callsWith({ site: 'north' });
  await calls.run(getItem, { id: '1' });
  await calls.run(getItem, { id: '1', site: 'south' });
  assert.deepEqual(sent, [`${BASE}/items/1?site=north`, `${BASE}/items/1?site=south`]);
});

test('a query parameter with no default and no value is not sent', async () => {
  const { calls, sent } = callsWith(undefined);
  await calls.run(getItem, { id: '1' });
  await calls.run(getItem, { id: '1', site: null });
  assert.deepEqual(sent, [`${BASE}/items/1`, `${BASE}/items/1`]);
});

test('query default names match exactly', async () => {
  const { calls, sent } = callsWith({ Site: 'north' });
  await calls.run(getItem, { id: '1' });
  assert.deepEqual(sent, [`${BASE}/items/1`]);
});

test('a query default never reaches a parameter that does not take one', async () => {
  const { calls, sent } = callsWith({ site: 'north' });
  await calls.run(listFiles);
  assert.deepEqual(sent, [`${BASE}/files`]);
});

test('an iterator sends the query default on every page', async () => {
  const pages = [
    { results: [{ id: 'a' }], next: 'b' },
    { results: [{ id: 'b' }], next: null },
  ];
  const { calls, sent } = callsWith({ site: 'north' }, pages);
  assert.deepEqual(await calls.all(listItems), [{ id: 'a' }, { id: 'b' }]);
  assert.deepEqual(sent, [`${BASE}/items?site=north`, `${BASE}/items?site=north&after=b`]);
});
