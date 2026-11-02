import { readdir, readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { parse } from 'yaml';

const METHODS = ['get', 'put', 'post', 'delete', 'patch'];
const CASE_KEYS = ['name', 'client', 'request', 'mock', 'wire', 'expect'];
const REQUEST_KEYS = ['operation', 'params', 'body', 'multipart', 'paginate'];
const RESPONSE_KEYS = ['status', 'headers', 'body', 'delay_ms', 'drop', 'trickle_ms', 'gzip', 'cut'];
const WIRE_KEYS = ['method', 'path', 'query', 'headers', 'headers_match', 'headers_absent', 'body', 'min_delay_ms'];
const EXPECT_KEYS = ['result', 'result_keys', 'error', 'logs_required'];
const OUTCOMES = ['result', 'result_keys', 'error'];

export function operationIds(spec) {
  return new Set(
    Object.values(spec.paths).flatMap((item) =>
      METHODS.filter((method) => item[method]).map((method) => item[method].operationId),
    ),
  );
}

const unknownKeys = (value, allowed) => Object.keys(value ?? {}).filter((key) => !allowed.includes(key));

export function validateCase(item, operations) {
  const errors = [];
  const unknown = (where, value, allowed) => {
    for (const key of unknownKeys(value, allowed)) errors.push(`unknown key ${where}.${key}`);
  };

  unknown('case', item, CASE_KEYS);
  if (!/^[a-z0-9]+(-[a-z0-9]+)*$/.test(item.name ?? '')) errors.push('name must be kebab-case');

  unknown('request', item.request, REQUEST_KEYS);
  if (!operations.has(item.request?.operation)) errors.push(`unknown operation ${item.request?.operation}`);
  if (item.request?.body !== undefined && item.request?.multipart !== undefined) {
    errors.push('request needs at most one of body or multipart');
  }

  const { prism, responses } = item.mock ?? {};
  if ((prism === undefined) === (responses === undefined)) errors.push('mock needs exactly one of prism or responses');
  if (responses !== undefined && !(Array.isArray(responses) && responses.length > 0)) {
    errors.push('mock.responses must be a non-empty list');
  }
  for (const response of responses ?? []) {
    unknown('mock.responses[]', response, RESPONSE_KEYS);
    if (response.drop === undefined) {
      if (!Number.isInteger(response.status)) errors.push('mock.responses[].status must be an integer');
    } else if (response.drop !== true || Object.keys(response).length > 1) {
      errors.push('mock.responses[].drop must be true and alone');
    }
    if (response.gzip !== undefined && response.gzip !== true) errors.push('mock.responses[].gzip must be true');
    if (response.cut !== undefined && !Number.isInteger(response.cut)) errors.push('mock.responses[].cut must be an integer');
  }

  if (!(Array.isArray(item.wire) && item.wire.length > 0)) errors.push('wire must be a non-empty list');
  for (const request of item.wire ?? []) {
    unknown('wire[]', request, WIRE_KEYS);
    if (!request.method || !request.path) errors.push('wire[] needs method and path');
  }
  if (Array.isArray(responses) && Array.isArray(item.wire) && responses.length !== item.wire.length) {
    errors.push(`${responses.length} scripted responses but ${item.wire.length} wire requests`);
  }

  unknown('expect', item.expect, EXPECT_KEYS);
  if (OUTCOMES.filter((key) => item.expect?.[key] !== undefined).length !== 1) {
    errors.push(`expect needs exactly one of ${OUTCOMES.join(', ')}`);
  }
  if (item.expect?.error !== undefined && !item.expect.error?.kind) errors.push('expect.error needs a kind');

  return errors;
}

export async function loadCases(dir, operations) {
  const files = (await readdir(dir)).filter((file) => file.endsWith('.yaml')).sort();
  const cases = [];
  const errors = [];
  for (const file of files) {
    const parsed = parse(await readFile(join(dir, file), 'utf8'));
    unknownKeys(parsed, ['cases']).forEach((key) => errors.push(`${file}: unknown key ${key}`));
    for (const item of parsed?.cases ?? []) {
      if (cases.some((other) => other.name === item.name)) errors.push(`${file}: duplicate case ${item.name}`);
      errors.push(...validateCase(item, operations).map((error) => `${file}: ${item.name}: ${error}`));
      cases.push(item);
    }
  }
  if (cases.length === 0) errors.push(`no cases in ${dir}`);
  if (errors.length > 0) throw new Error(`Invalid cases:\n${errors.join('\n')}`);
  return cases;
}
