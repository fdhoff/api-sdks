import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { test } from 'node:test';
import * as sdk from 'gitea-rest';

const AsyncFunction = (async () => {}).constructor as new (...args: string[]) => (...args: unknown[]) => Promise<void>;
const SECRETS = ['your-access-token', 'your-password', '123456'];
const BASE = 'https://gitea.example.com/api/v1';

function respond(url: URL): Response {
  const json = (body: unknown, status = 200) =>
    new Response(JSON.stringify(body), { status, headers: { 'content-type': 'application/json' } });
  switch (url.pathname) {
    case '/api/v1/user':
      return json({ id: 1, login: 'synthetic-user' });
    case '/api/v1/repos/your-org/your-repo/issues':
      return json([{ number: 1, title: 'Synthetic issue' }]);
    case '/api/v1/users/your-username/tokens':
      return json({ id: 7, name: 'scripts', sha1: 'synthetic-new-token' }, 201);
  }
  return json({ message: 'synthetic not found' }, 404);
}

/** A snippet's import becomes a lookup on the package. Snippets use no TypeScript-only syntax. */
const runnable = (snippet: string): string =>
  snippet.replace(/^import \{(.*)\} from 'gitea-rest';$/m, 'const {$1} = sdk;');

const text = await readFile(new URL('../README.md', import.meta.url), 'utf8');
const snippets = [...text.matchAll(/```ts\n(.*?)```/gs)].map((match) => match[1] as string);

test('the README has snippets', () => assert.ok(snippets.length >= 2));

for (const [index, snippet] of snippets.entries()) {
  test(`README snippet ${index} runs`, async (t) => {
    const fetch = t.mock.method(globalThis, 'fetch', async (input: string | URL | Request) =>
      respond(new URL(String(input))),
    );
    const lines: unknown[][] = [];
    const log = (...args: unknown[]) => void lines.push(args);
    await new AsyncFunction('sdk', 'console', runnable(snippet))(sdk, { log });
    assert.ok(fetch.mock.callCount() > 0);
    assert.ok(fetch.mock.calls.every(({ arguments: [input] }) => String(input).startsWith(`${BASE}/`)));
    assert.notEqual(lines.length, 0);
    const output = JSON.stringify(lines);
    assert.deepEqual(
      SECRETS.filter((secret) => output.includes(secret)),
      [],
    );
  });
}
