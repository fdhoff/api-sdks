// Keeps the pinned OpenAPI Generator jar in toolchain/build/, checked against toolchain/generator/lock.json.
// No flag downloads it if absent; `--cache` prints the Actions cache `key=` and `path=` lines for $GITHUB_OUTPUT.
// Uses only Node's own modules, so it runs before `npm ci`.
import { createHash } from 'node:crypto';
import { mkdir, readFile, rm, stat, writeFile } from 'node:fs/promises';
import { setTimeout as sleep } from 'node:timers/promises';
import { dirname, join, relative } from 'node:path';
import { fileURLToPath } from 'node:url';

const TOOLCHAIN = fileURLToPath(new URL('..', import.meta.url));
const LOCK = join(TOOLCHAIN, 'generator/lock.json');
const sha256 = (bytes) => createHash('sha256').update(bytes).digest('hex');

export const readGeneratorLock = async () => JSON.parse(await readFile(LOCK, 'utf8'));

export const generatorJar = (lock) => join(TOOLCHAIN, 'build', `openapi-generator-${lock.version}.jar`);

export const generatorCache = (lock) => ({ key: `openapi-generator-${lock.sha256}`, path: relative(process.cwd(), generatorJar(lock)) });

// Maven Central throttles busy runner IPs with 429, and sometimes with a 404 for a file it serves.
const retryable = (status) => status === 404 || status === 429 || status >= 500;

// Fetches url, retrying throttling, server errors and network errors with exponential backoff.
export async function fetchWithRetry(url, { attempts = 6, delayMs = 2000, wait = sleep } = {}) {
  for (let attempt = 1; ; attempt++) {
    const result = await fetch(url).catch((error) => error);
    const status = result instanceof Response ? result.status : null;
    if (result.ok) return result;
    const failure = status === null ? result : new Error(`GET ${url}: HTTP ${status}`);
    if ((status !== null && !retryable(status)) || attempt === attempts) throw failure;
    const delay = delayMs * 2 ** (attempt - 1);
    console.error(`${failure.message}. Retrying in ${delay / 1000}s (${attempt}/${attempts - 1}).`);
    await wait(delay);
  }
}

export async function ensureGenerator(lock, jar = generatorJar(lock), options = {}) {
  if (await stat(jar).then(() => true, () => false)) {
    if (sha256(await readFile(jar)) === lock.sha256) return jar;
    await rm(jar);
  }
  const response = await fetchWithRetry(lock.url, options);
  const bytes = Buffer.from(await response.arrayBuffer());
  if (sha256(bytes) !== lock.sha256) throw new Error(`Generator from ${lock.url} does not match its lock`);
  await mkdir(dirname(jar), { recursive: true });
  await writeFile(jar, bytes);
  return jar;
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const lock = await readGeneratorLock();
  if (process.argv.includes('--cache')) {
    const { key, path } = generatorCache(lock);
    console.log(`key=${key}\npath=${path}`);
  } else {
    console.log(`Generator ready: ${await ensureGenerator(lock)}`);
  }
}
