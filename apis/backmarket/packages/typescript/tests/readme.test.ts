import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { test } from 'node:test';
import * as sdk from 'backmarket-seller';

const AsyncFunction = (async () => {}).constructor as new (...args: string[]) => (...args: unknown[]) => Promise<void>;
const READMES = ['../README.md', '../../../../../README.md'];
const PAGE = { count: 1, next: null, previous: null, results: [{ order_id: 1 }] };

for (const path of READMES) {
  const text = await readFile(new URL(path, import.meta.url), 'utf8');
  const snippets = [...text.matchAll(/```ts\n(.*?)```/gs)].map((match) => match[1] as string);

  test(`${path} has a snippet`, () => assert.notEqual(snippets.length, 0));

  for (const [index, snippet] of snippets.entries()) {
    test(`${path} snippet ${index} runs`, async (t) => {
      const fetch = t.mock.method(globalThis, 'fetch', async (input: string | URL | Request) => {
        const found = String(input).includes('/orders');
        return new Response(JSON.stringify(found ? PAGE : {}), {
          status: found ? 200 : 404,
          headers: { 'content-type': 'application/json' },
        });
      });
      const lines: unknown[][] = [];
      const log = (...args: unknown[]) => void lines.push(args);
      const code = snippet.replace(/^import \{(.*)\} from 'backmarket-seller';$/m, 'const {$1} = sdk;');
      await new AsyncFunction('sdk', 'console', code)(sdk, { log });
      assert.notEqual(fetch.mock.callCount(), 0);
      assert.ok(!JSON.stringify(lines).includes('your-token'));
    });
  }
}
