import { randomBytes } from 'node:crypto';
import { readdir, readFile } from 'node:fs/promises';
import { createServer, request as forward } from 'node:http';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { parseArgs } from 'node:util';
import { parse } from 'yaml';
import { startDriver } from '../../../../toolchain/conformance/run.mjs';

const SCENARIOS = fileURLToPath(new URL('scenarios', import.meta.url));
const LOOPBACK = ['127.0.0.1', 'localhost', '[::1]'];
const SETTINGS = ['base_url', 'admin', 'admin_password', 'user', 'user_password', 'token'];
const STEP_KEYS = ['name', 'client', 'request', 'repeat', 'save', 'expect'];
const EXPECT_KEYS = ['result', 'error', 'count', 'unique', 'requests', 'wire'];
const PLACEHOLDER = /\{\{([\w.]+)\}\}/g;

const lookup = (vars, path) => {
  const value = path.split('.').reduce((node, key) => (node === null || node === undefined ? undefined : node[key]), vars);
  if (value === undefined) throw new Error(`{{${path}}} has no value`);
  return value;
};

// A string that is one placeholder takes the value's own type, so a saved number stays a number.
export function fill(value, vars) {
  if (typeof value === 'string') {
    const whole = /^\{\{([\w.]+)\}\}$/.exec(value);
    if (whole) return lookup(vars, whole[1]);
    return value.replace(PLACEHOLDER, (_, path) => String(lookup(vars, path)));
  }
  if (Array.isArray(value)) return value.map((item) => fill(item, vars));
  if (value !== null && typeof value === 'object') {
    return Object.fromEntries(Object.entries(value).map(([key, item]) => [key, fill(item, vars)]));
  }
  return value;
}

// A subset match, as in the mock cases, where `{ $regex: pattern }` matches a string.
export function matches(expected, actual) {
  if (Array.isArray(expected)) {
    return Array.isArray(actual) && actual.length === expected.length && expected.every((item, index) => matches(item, actual[index]));
  }
  if (expected !== null && typeof expected === 'object') {
    if ('$regex' in expected) return typeof actual === 'string' && new RegExp(expected.$regex).test(actual);
    if (actual === null || typeof actual !== 'object') return false;
    return Object.entries(expected).every(([key, item]) => matches(item, actual[key]));
  }
  return expected === actual;
}

export function checkScenario(scenario, operations) {
  const problems = [];
  if (typeof scenario.scenario !== 'string') problems.push('`scenario` must name the scenario');
  if (!Array.isArray(scenario.steps) || scenario.steps.length === 0) return [...problems, '`steps` must list at least one step'];
  const names = new Set();
  for (const step of scenario.steps) {
    const label = step.name ?? '(unnamed step)';
    if (typeof step.name !== 'string') problems.push('every step needs a `name`');
    else if (names.has(step.name)) problems.push(`${label}: the name is used twice`);
    names.add(step.name);
    for (const key of Object.keys(step)) if (!STEP_KEYS.includes(key)) problems.push(`${label}: unknown key ${key}`);
    if (!operations.has(step.request?.operation)) problems.push(`${label}: no operation ${step.request?.operation}`);
    const expect = step.expect ?? {};
    for (const key of Object.keys(expect)) if (!EXPECT_KEYS.includes(key)) problems.push(`${label}: unknown expect key ${key}`);
    if (step.expect === undefined) problems.push(`${label}: no expect`);
    if ('error' in expect && Object.keys(expect).some((key) => ['result', 'count', 'unique'].includes(key))) {
      problems.push(`${label}: an expected error cannot also expect a result`);
    }
    if (step.repeat !== undefined && !(Number.isInteger(step.repeat) && step.repeat > 1)) problems.push(`${label}: repeat must be above 1`);
  }
  return problems;
}

export async function loadScenarios(dir = SCENARIOS) {
  const files = (await readdir(dir)).filter((file) => file.endsWith('.yaml')).sort();
  return Promise.all(files.map(async (file) => ({ file, ...parse(await readFile(join(dir, file), 'utf8')) })));
}

// Records each request's method, raw path and headers on the way through, so a step can count its pages.
// Response headers, `Link` included, pass back unchanged.
export async function startProxy(target) {
  const upstream = new URL(target);
  if (!LOOPBACK.includes(upstream.hostname)) throw new Error(`the live suite runs only against a local container, not ${upstream.host}`);
  let requests = [];
  const server = createServer((incoming, outgoing) => {
    const [path, search = ''] = incoming.url.split('?');
    requests.push({ method: incoming.method, path, query: Object.fromEntries(new URLSearchParams(search)), headers: incoming.headers });
    const upstreamRequest = forward(
      { hostname: upstream.hostname, port: upstream.port, method: incoming.method, path: incoming.url, headers: { ...incoming.headers, host: upstream.host } },
      (answer) => {
        outgoing.writeHead(answer.statusCode, answer.rawHeaders);
        answer.pipe(outgoing);
      },
    );
    upstreamRequest.on('error', () => outgoing.destroy());
    incoming.pipe(upstreamRequest);
  });
  await new Promise((resolve) => server.listen(0, '127.0.0.1', resolve));
  return {
    url: `http://127.0.0.1:${server.address().port}`,
    take: () => {
      const taken = requests;
      requests = [];
      return taken;
    },
    close: () =>
      new Promise((resolve) => {
        server.close(resolve);
        server.closeAllConnections();
      }),
  };
}

function checkWire(wire, requests, failures) {
  for (const request of requests) {
    if (wire.path_match !== undefined && !new RegExp(wire.path_match).test(request.path)) {
      failures.push(`sent path ${request.path}, expected /${wire.path_match}/`);
    }
    for (const [name, pattern] of Object.entries(wire.headers_match ?? {})) {
      const got = request.headers[name.toLowerCase()] ?? '';
      if (!new RegExp(pattern).test(got)) failures.push(`sent ${name}: ${got}, expected /${pattern}/`);
    }
  }
}

export function checkStep(expect, outcome, requests) {
  const failures = [];
  const shown = JSON.stringify(outcome.error ?? outcome.result)?.slice(0, 500);
  if ('error' in expect) {
    if (!matches(expect.error, outcome.error)) failures.push(`outcome is ${shown}`);
  } else if (outcome.error !== undefined) {
    failures.push(`unexpected error ${shown}`);
  } else if ('result' in expect && !matches(expect.result, outcome.result)) {
    failures.push(`result is ${shown}`);
  }
  if (expect.count !== undefined && outcome.result?.length !== expect.count) {
    failures.push(`got ${outcome.result?.length} items, expected ${expect.count}`);
  }
  if (expect.unique !== undefined && Array.isArray(outcome.result)) {
    const values = outcome.result.map((item) => item?.[expect.unique]);
    if (new Set(values).size !== values.length) failures.push(`${expect.unique} repeats: ${values.join(', ')}`);
  }
  if (expect.requests !== undefined && requests.length !== expect.requests) {
    failures.push(`sent ${requests.length} requests, expected ${expect.requests}: ${requests.map((request) => request.path).join(', ')}`);
  }
  checkWire(expect.wire ?? {}, requests, failures);
  return failures;
}

// Each step runs once, or `repeat` times with `{{i}}` counting from 1. `save` keeps a step's result for later
// steps of the same scenario as `{{<save>.<field>}}`. The client defaults to the admin's access token.
export async function runScenarios({ scenarios, settings, driver, proxy, report = () => {} }) {
  const secrets = [
    settings.token,
    settings.admin_password,
    settings.user_password,
    Buffer.from(`${settings.admin}:${settings.admin_password}`).toString('base64'),
    Buffer.from(`${settings.user}:${settings.user_password}`).toString('base64'),
  ];
  const failed = [];
  let total = 0;
  for (const scenario of scenarios) {
    const vars = { ...settings, run: randomBytes(4).toString('hex') };
    for (const step of scenario.steps) {
      for (let i = 1; i <= (step.repeat ?? 1); i += 1) {
        const label = `${scenario.scenario}: ${step.name}${step.repeat ? ` (${i})` : ''}`;
        const stepVars = { ...vars, i };
        const client = { ...fill(step.client ?? scenario.client ?? { token: '{{token}}' }, stepVars), base_url: proxy.url };
        const outcome = await driver.call({ case: label, client, request: fill(step.request, stepVars) });
        const failures = checkStep(fill(step.expect, stepVars), outcome, proxy.take());
        const output = JSON.stringify({ result: outcome.result, error: outcome.error, logs: outcome.logs });
        if (secrets.some((secret) => secret && output.includes(secret))) failures.push('a credential leaked into the client output');
        if (step.save) vars[step.save] = outcome.result;
        total += 1;
        report(label, failures);
        if (failures.length > 0) failed.push({ name: label, failures });
      }
    }
  }
  return { total, failed };
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const { values } = parseArgs({ options: { settings: { type: 'string' }, driver: { type: 'string' } } });
  if (!values.settings || !values.driver) throw new Error('Usage: run.mjs --settings <file> --driver <command>');
  const settings = JSON.parse(await readFile(values.settings, 'utf8'));
  const missing = SETTINGS.filter((name) => typeof settings[name] !== 'string' || settings[name] === '');
  if (missing.length > 0) throw new Error(`the settings file lacks ${missing.join(', ')}`);
  const proxy = await startProxy(settings.base_url);
  const driver = startDriver(values.driver);
  try {
    const { total, failed } = await runScenarios({
      scenarios: await loadScenarios(),
      settings,
      driver,
      proxy,
      report: (name, failures) => {
        console.log(`${failures.length === 0 ? 'ok  ' : 'FAIL'} ${name}`);
        failures.forEach((failure) => console.log(`     ${failure}`));
      },
    });
    console.log(`${total - failed.length} of ${total} live steps passed`);
    process.exitCode = failed.length === 0 ? 0 : 1;
  } finally {
    driver.stop();
    await proxy.close();
  }
}
