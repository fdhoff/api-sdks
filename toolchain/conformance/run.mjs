import { spawn } from 'node:child_process';
import { readFile } from 'node:fs/promises';
import { createServer } from 'node:net';
import { join } from 'node:path';
import { createInterface } from 'node:readline';
import { fileURLToPath } from 'node:url';
import { parseArgs } from 'node:util';
import { parse } from 'yaml';
import { apiPaths } from '../pipeline/paths.mjs';
import { loadCases, operationIds } from './cases.mjs';
import { checkCase, fill } from './check.mjs';
import { startHarness } from './harness.mjs';

const PRISM = fileURLToPath(new URL('../../node_modules/.bin/prism', import.meta.url));
const SYNTHETIC_TOKEN = 'conformance-synthetic-token';
const DRIVER_TIMEOUT_MS = 30_000;

const freePort = () =>
  new Promise((resolve) => {
    const server = createServer().listen(0, '127.0.0.1', () => {
      const { port } = server.address();
      server.close(() => resolve(port));
    });
  });

async function startPrism(spec) {
  const port = await freePort();
  const url = `http://127.0.0.1:${port}`;
  const child = spawn(PRISM, ['mock', spec, '--port', String(port)], { stdio: 'ignore' });
  for (let attempt = 0; attempt < 150; attempt += 1) {
    try {
      await fetch(url);
      return { url, stop: () => child.kill() };
    } catch {
      await new Promise((resolve) => setTimeout(resolve, 200));
    }
  }
  child.kill();
  throw new Error('Prism did not start');
}

export function startDriver(command) {
  const child = spawn(command, { shell: true, stdio: ['pipe', 'pipe', 'inherit'] });
  const lines = createInterface({ input: child.stdout })[Symbol.asyncIterator]();
  return {
    async call(message) {
      child.stdin.write(`${JSON.stringify(message)}\n`);
      let timer;
      const timeout = new Promise((_, reject) => {
        timer = setTimeout(() => reject(new Error('driver did not answer')), DRIVER_TIMEOUT_MS);
      });
      const { value, done } = await Promise.race([lines.next(), timeout]).finally(() => clearTimeout(timer));
      if (done) throw new Error('driver exited');
      return JSON.parse(value);
    },
    stop: () => child.stdin.end(),
  };
}

export async function runCases({ cases, defaults, secrets = [], driver, harness, report = () => {} }) {
  const failed = [];
  for (const item of cases) {
    const client = { token: SYNTHETIC_TOKEN, ...defaults, ...item.client, base_url: harness.url };
    const vars = Object.fromEntries(['token', ...secrets].map((name) => [name, client[name]]));
    harness.play(fill(item.mock, vars));
    const outcome = await driver.call({ case: item.name, client, request: item.request });
    const failures = checkCase(item, harness.requests(), outcome, vars);
    report(item.name, failures);
    if (failures.length > 0) failed.push({ name: item.name, failures });
  }
  return failed;
}

export async function runSuite({ apiDir, driverCommand, report }) {
  const paths = apiPaths(apiDir);
  const dir = join(apiDir, 'conformance');
  const operations = operationIds(parse(await readFile(paths.build, 'utf8')));
  const cases = await loadCases(join(dir, 'cases'), operations);
  const { client: defaults, secrets = [] } = parse(await readFile(join(dir, 'defaults.yaml'), 'utf8'));
  const unset = secrets.filter((name) => typeof defaults?.[name] !== 'string' || defaults[name] === '');
  if (unset.length > 0) throw new Error(`defaults.yaml names secrets with no synthetic value: ${unset.join(', ')}`);

  const prism = await startPrism(paths.build);
  const harness = await startHarness(prism.url);
  const driver = startDriver(driverCommand);
  try {
    const failed = await runCases({ cases, defaults, secrets, driver, harness, report });
    return { total: cases.length, failed };
  } finally {
    driver.stop();
    await harness.close();
    prism.stop();
  }
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const { values, positionals } = parseArgs({ options: { driver: { type: 'string' } }, allowPositionals: true });
  if (!positionals[0] || !values.driver) throw new Error('Usage: run.mjs <api-dir> --driver <command>');
  const { total, failed } = await runSuite({
    apiDir: positionals[0],
    driverCommand: values.driver,
    report: (name, failures) => {
      console.log(`${failures.length === 0 ? 'ok  ' : 'FAIL'} ${name}`);
      failures.forEach((failure) => console.log(`     ${failure}`));
    },
  });
  console.log(`${total - failed.length} of ${total} cases passed`);
  process.exitCode = failed.length === 0 ? 0 : 1;
}
