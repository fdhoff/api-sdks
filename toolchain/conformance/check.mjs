import { isDeepStrictEqual } from 'node:util';

export function fill(value, vars) {
  if (typeof value === 'string') return value.replaceAll('{{token}}', vars.token);
  if (Array.isArray(value)) return value.map((item) => fill(item, vars));
  if (value !== null && typeof value === 'object') {
    return Object.fromEntries(Object.entries(value).map(([key, item]) => [key, fill(item, vars)]));
  }
  return value;
}

export function matches(expected, actual) {
  if (Array.isArray(expected)) {
    return (
      Array.isArray(actual) &&
      actual.length === expected.length &&
      expected.every((item, index) => matches(item, actual[index]))
    );
  }
  if (expected !== null && typeof expected === 'object') {
    if (actual === null || typeof actual !== 'object') return false;
    return Object.entries(expected).every(([key, item]) => matches(item, actual[key]));
  }
  return expected === actual;
}

function checkHeaders(expected, actual, label, failures) {
  for (const [name, value] of Object.entries(expected.headers ?? {})) {
    const got = actual.headers[name.toLowerCase()];
    if (got !== value) failures.push(`${label}: header ${name} is ${got}, expected ${value}`);
  }
  for (const [name, pattern] of Object.entries(expected.headers_match ?? {})) {
    const got = actual.headers[name.toLowerCase()];
    if (!new RegExp(pattern).test(got ?? '')) failures.push(`${label}: header ${name} is ${got}, expected /${pattern}/`);
  }
  for (const name of expected.headers_absent ?? []) {
    if (name.toLowerCase() in actual.headers) failures.push(`${label}: header ${name} must be absent`);
  }
}

function checkBody(expected, actual, label, failures) {
  if (expected === undefined) return;
  let got;
  try {
    got = JSON.parse(actual);
  } catch {
    failures.push(`${label}: body is not JSON: ${actual}`);
    return;
  }
  if (!isDeepStrictEqual(got, expected)) failures.push(`${label}: body is ${actual}`);
}

function checkWire(wire, requests, failures) {
  if (requests.length !== wire.length) {
    const seen = requests.map((request) => `${request.method} ${request.path}`).join(', ');
    failures.push(`sent ${requests.length} requests, expected ${wire.length}: ${seen}`);
  }
  wire.forEach((expected, index) => {
    const actual = requests[index];
    if (!actual) return;
    const label = `wire[${index}]`;
    if (actual.method !== expected.method) failures.push(`${label}: method is ${actual.method}`);
    if (actual.path !== expected.path) failures.push(`${label}: path is ${actual.path}`);
    if (!isDeepStrictEqual(actual.query, expected.query ?? {})) {
      failures.push(`${label}: query is ${JSON.stringify(actual.query)}`);
    }
    checkHeaders(expected, actual, label, failures);
    checkBody(expected.body, actual.body, label, failures);
    if (expected.min_delay_ms !== undefined) {
      const delay = actual.at - (requests[index - 1]?.at ?? actual.at);
      if (delay < expected.min_delay_ms) failures.push(`${label}: sent after ${delay}ms`);
    }
  });
}

function checkOutcome(expect, outcome, failures) {
  const shown = JSON.stringify({ result: outcome.result, error: outcome.error });
  if (expect.error !== undefined) {
    if (!matches(expect.error, outcome.error)) failures.push(`outcome is ${shown}`);
  } else if (outcome.error !== undefined) {
    failures.push(`unexpected error ${JSON.stringify(outcome.error)}`);
  } else if (expect.result_keys !== undefined) {
    const value = Array.isArray(outcome.result) ? outcome.result[0] : outcome.result;
    const missing = expect.result_keys.filter((key) => !(key in Object(value)));
    if (missing.length > 0) failures.push(`result lacks ${missing.join(', ')}: ${shown}`);
  } else if (!matches(expect.result, outcome.result)) {
    failures.push(`outcome is ${shown}`);
  }
  if (expect.logs_required && !(outcome.logs?.length > 0)) failures.push('client logged nothing');
}

export function checkCase(item, requests, outcome, token) {
  const failures = [];
  checkWire(fill(item.wire, { token }), requests, failures);
  checkOutcome(fill(item.expect, { token }), outcome, failures);
  const { result, error, logs } = outcome;
  if (JSON.stringify({ result, error, logs }).includes(token)) failures.push('token leaked into the client output');
  return failures;
}
