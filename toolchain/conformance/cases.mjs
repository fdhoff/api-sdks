import { readdir, readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { parse } from 'yaml';

const METHODS = ['get', 'put', 'post', 'delete', 'patch'];
const CASE_KEYS = ['name', 'client', 'request', 'mock', 'wire', 'expect', 'steps'];
const STEP_KEYS = ['request', 'expect'];
const REQUEST_KEYS = ['operation', 'params', 'body', 'multipart', 'raw_body_base64', 'paginate', 'wait', 'download'];
const BODIES = ['body', 'multipart', 'raw_body_base64'];
// A download URL names the harness's own origin or the other one, which the runner fills in.
const DOWNLOAD_URL = /^\{\{(base_url|other_origin)\}\}\//;
const RESPONSE_KEYS = ['status', 'headers', 'body', 'body_base64', 'delay_ms', 'drop', 'trickle_ms', 'gzip', 'cut'];
const WIRE_KEYS = [
  'method',
  'host',
  'path',
  'query',
  'headers',
  'headers_match',
  'headers_absent',
  'body',
  'body_base64',
  'parts',
  'content_digest',
  'min_delay_ms',
  'cross_origin',
];
const EXPECT_KEYS = ['result', 'result_keys', 'error', 'logs_required', 'logs_exclude'];
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

  if (item.steps === undefined) {
    validateRequest(item.request, operations, '', errors);
    validateExpect(item.expect, '', errors);
  } else if (item.request !== undefined || item.expect !== undefined) {
    errors.push('a case needs either request and expect, or steps');
  } else if (!(Array.isArray(item.steps) && item.steps.length > 0)) {
    errors.push('steps must be a non-empty list');
  } else {
    item.steps.forEach((step, index) => {
      const where = `steps[${index}].`;
      for (const key of unknownKeys(step, STEP_KEYS)) errors.push(`unknown key ${where.slice(0, -1)}.${key}`);
      validateRequest(step?.request, operations, where, errors);
      validateExpect(step?.expect, where, errors);
    });
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
    for (const [name, value] of Object.entries(response.headers ?? {})) {
      const values = Array.isArray(value) ? value : [value];
      if (values.length === 0 || !values.every((item) => ['string', 'number'].includes(typeof item))) {
        errors.push(`mock.responses[].headers.${name} must be a string or a number, or a non-empty list of them`);
      }
    }
    if (response.gzip !== undefined && response.gzip !== true) errors.push('mock.responses[].gzip must be true');
    if (response.cut !== undefined && !Number.isInteger(response.cut)) errors.push('mock.responses[].cut must be an integer');
    if (response.body !== undefined && response.body_base64 !== undefined) {
      errors.push('mock.responses[] needs at most one of body or body_base64');
    }
  }

  if (!(Array.isArray(item.wire) && item.wire.length > 0)) errors.push('wire must be a non-empty list');
  for (const request of item.wire ?? []) {
    unknown('wire[]', request, WIRE_KEYS);
    if (!request.method || !request.path) errors.push('wire[] needs method and path');
    if (['body', 'body_base64', 'parts'].filter((key) => request[key] !== undefined).length > 1) {
      errors.push('wire[] needs at most one of body, body_base64 or parts');
    }
    if (![undefined, true].includes(request.content_digest)) errors.push('wire[].content_digest can only be true');
    if (![undefined, true].includes(request.cross_origin)) errors.push('wire[].cross_origin can only be true');
  }
  if (Array.isArray(responses) && Array.isArray(item.wire) && responses.length !== item.wire.length) {
    errors.push(`${responses.length} scripted responses but ${item.wire.length} wire requests`);
  }

  return errors;
}

// `where` prefixes each message with the step it is in, if any.
function validateRequest(request, operations, where, errors) {
  for (const key of unknownKeys(request, REQUEST_KEYS)) errors.push(`unknown key ${where}request.${key}`);
  if (BODIES.filter((key) => request?.[key] !== undefined).length > 1) {
    errors.push(`${where}request needs at most one of body, multipart or raw_body_base64`);
  }
  if (request?.download !== undefined) {
    if (typeof request.download !== 'string' || !DOWNLOAD_URL.test(request.download)) {
      errors.push(`${where}request.download must start with {{base_url}}/ or {{other_origin}}/`);
    }
    const others = Object.keys(request).filter((key) => key !== 'download');
    if (others.length > 0) errors.push(`${where}request.download stands alone, without ${others.join(', ')}`);
    return;
  }
  if (!operations.has(request?.operation)) errors.push(`${where}unknown operation ${request?.operation}`);
  if (request?.wait !== undefined) {
    if (request.wait !== true) errors.push(`${where}request.wait must be true`);
    if (request.paginate !== undefined || BODIES.some((key) => request[key] !== undefined)) {
      errors.push(`${where}request.wait takes only operation and params`);
    }
  }
}

function validateExpect(expect, where, errors) {
  for (const key of unknownKeys(expect, EXPECT_KEYS)) errors.push(`unknown key ${where}expect.${key}`);
  if (OUTCOMES.filter((key) => expect?.[key] !== undefined).length !== 1) {
    errors.push(`${where}expect needs exactly one of ${OUTCOMES.join(', ')}`);
  }
  if (expect?.error !== undefined && !expect.error?.kind) errors.push(`${where}expect.error needs a kind`);
  const excluded = expect?.logs_exclude;
  if (excluded !== undefined && !(Array.isArray(excluded) && excluded.length > 0 && excluded.every((value) => typeof value === 'string' && value !== ''))) {
    errors.push(`${where}expect.logs_exclude must be a non-empty list of non-empty strings`);
  }
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
