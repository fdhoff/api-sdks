import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { mkdtemp, readFile, rm, stat, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { test } from 'node:test';
import { ensureGenerator, fetchWithRetry, generatorCache, readGeneratorLock } from './generator.mjs';

const JAR = Buffer.from('jar');
const LOCK = { version: '1.0.0', url: 'https://jar.invalid/generator.jar', sha256: createHash('sha256').update(JAR).digest('hex') };

async function emptyDir(t) {
  const dir = await mkdtemp(join(tmpdir(), 'generator-'));
  t.after(() => rm(dir, { recursive: true, force: true }));
  return dir;
}

// Answers each fetch with the next entry: a status code, a Response, or an Error to throw as a network failure.
const respond = (t, ...answers) =>
  t.mock.method(globalThis, 'fetch', async () => {
    const answer = answers.shift();
    if (answer instanceof Error) throw answer;
    if (answer instanceof Response) return answer;
    return answer === 200 ? new Response(JAR) : new Response('', { status: answer });
  });

const noWait = () => {
  const waits = [];
  return { waits, wait: async (ms) => waits.push(ms) };
};

test('fetchWithRetry retries throttling, server and network errors with backoff', async (t) => {
  const fetchJar = respond(t, 429, 404, 503, new TypeError('fetch failed'), 200);
  const { waits, wait } = noWait();
  const response = await fetchWithRetry(LOCK.url, { delayMs: 10, wait });
  assert.deepEqual(Buffer.from(await response.arrayBuffer()), JAR);
  assert.equal(fetchJar.mock.callCount(), 5);
  assert.deepEqual(waits, [10, 20, 40, 80]);
});

test('fetchWithRetry caps its backoff and follows Retry-After up to twice the cap', async (t) => {
  const throttled = (seconds) => new Response('', { status: 429, headers: { 'retry-after': String(seconds) } });
  respond(t, 503, 503, 503, throttled(1), throttled(30), 200);
  const { waits, wait } = noWait();
  await fetchWithRetry(LOCK.url, { delayMs: 1000, maxDelayMs: 5000, wait });
  assert.deepEqual(waits, [1000, 2000, 4000, 5000, 10000]);
});

test('fetchWithRetry gives up after its last attempt', async (t) => {
  const fetchJar = respond(t, 429, 429, 429);
  const { wait } = noWait();
  await assert.rejects(fetchWithRetry(LOCK.url, { attempts: 3, wait }), /HTTP 429/);
  assert.equal(fetchJar.mock.callCount(), 3);
});

test('fetchWithRetry does not retry a client error', async (t) => {
  const fetchJar = respond(t, 403, 200);
  const { waits, wait } = noWait();
  await assert.rejects(fetchWithRetry(LOCK.url, { wait }), /HTTP 403/);
  assert.equal(fetchJar.mock.callCount(), 1);
  assert.deepEqual(waits, []);
});

test('ensureGenerator downloads the pinned jar after a throttled attempt', async (t) => {
  const jar = join(await emptyDir(t), 'build', 'generator.jar');
  respond(t, 429, 200);
  assert.equal(await ensureGenerator(LOCK, jar, noWait()), jar);
  assert.deepEqual(await readFile(jar), JAR);
});

test('ensureGenerator serves a valid jar without the network', async (t) => {
  const jar = join(await emptyDir(t), 'generator.jar');
  await writeFile(jar, JAR);
  const fetchJar = respond(t);
  assert.equal(await ensureGenerator(LOCK, jar), jar);
  assert.equal(fetchJar.mock.callCount(), 0);
});

test('ensureGenerator rejects a download that does not match the lock', async (t) => {
  const jar = join(await emptyDir(t), 'generator.jar');
  await writeFile(jar, 'stale');
  t.mock.method(globalThis, 'fetch', async () => new Response('tampered'));
  await assert.rejects(ensureGenerator(LOCK, jar), /does not match its lock/);
  await assert.rejects(stat(jar), { code: 'ENOENT' });
});

test('the generator cache is keyed by the pinned hash', async () => {
  const lock = await readGeneratorLock();
  const { key, path } = generatorCache(lock);
  assert.equal(key, `openapi-generator-${lock.sha256}`);
  assert.match(path, new RegExp(`^toolchain/build/openapi-generator-${lock.version.replaceAll('.', '\\.')}\\.jar$`));
});
