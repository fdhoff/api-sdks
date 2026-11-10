// Checks that the pinned registry URL is still Mercury's current spec, for the spec drift job, and finds the current
// one for upstream-url.mjs. A superseded registry ID keeps answering with an old copy, so a healthy response alone
// proves nothing: the API reference must still name the pinned ID. Uses only Node's own modules.
import { readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';

// A reference page; each one names the registry ID of the spec it renders.
export const DOCS_PAGE = 'https://docs.mercury.com/reference/getaccounts';
const NAMED_ID = /"oasPublicUrl"\s*:\s*"@mercurytechnologies\/v1#([A-Za-z0-9]+)"/g;
const REGISTRY_URL = /^https:\/\/dash\.readme\.com\/api\/v1\/api-registry\/([A-Za-z0-9]+)$/;

export const registryUrl = (id) => `https://dash.readme.com/api/v1/api-registry/${id}`;

export function registryId(url) {
  const match = REGISTRY_URL.exec(url);
  if (!match) throw new Error(`lock.json url ${url} is not a ReadMe registry URL`);
  return match[1];
}

// Why a registry response is not a spec, or null when it is one.
export function specProblem(status, text) {
  if (status < 200 || status > 299) return `HTTP ${status}`;
  if (text.trim() === '') return 'an empty body';
  let spec;
  try {
    spec = JSON.parse(text);
  } catch {
    return 'a body that is not JSON';
  }
  if (typeof spec?.openapi !== 'string' || typeof spec.paths !== 'object' || spec.paths === null) return 'JSON that is not an OpenAPI document';
  return null;
}

export const namedIds = (html) => [...new Set([...html.matchAll(NAMED_ID)].map((match) => match[1]))];

// The registry URL of the one ID the API reference names.
export async function currentRegistryUrl(get = fetch) {
  const docs = await get(DOCS_PAGE);
  if (!docs.ok) throw new Error(`${DOCS_PAGE} answered HTTP ${docs.status}`);
  const ids = namedIds(await docs.text());
  if (ids.length !== 1) throw new Error(`${DOCS_PAGE} names ${ids.length === 0 ? 'no registry ID' : `registry IDs ${ids.join(', ')}`}, not one`);
  return registryUrl(ids[0]);
}

// Every problem found, as a sentence each. None means the pin is current.
export async function checkUpstream(lock, get = fetch) {
  const pinned = registryId(lock.url);
  const problems = [];
  const spec = await get(lock.url);
  const specIssue = specProblem(spec.status, await spec.text());
  if (specIssue) problems.push(`The pinned registry URL ${lock.url} answered with ${specIssue}.`);
  const docs = await get(DOCS_PAGE);
  const ids = docs.ok ? namedIds(await docs.text()) : [];
  if (!docs.ok) problems.push(`${DOCS_PAGE} answered HTTP ${docs.status}, so the pinned registry ID could not be checked.`);
  else if (ids.length === 0) problems.push(`${DOCS_PAGE} names no registry ID, so the pinned one could not be checked.`);
  else if (!ids.includes(pinned)) {
    problems.push(`The API reference names registry ID ${ids.join(', ')}, not the pinned ${pinned}. The spec drift pull request moves the pin to it.`);
  }
  return problems;
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const lock = JSON.parse(await readFile(new URL('./upstream/lock.json', import.meta.url), 'utf8'));
  const problems = await checkUpstream(lock);
  for (const problem of problems) console.log(`::error title=Mercury upstream spec::${problem}`);
  if (problems.length === 0) console.log(`The API reference still names registry ID ${registryId(lock.url)}.`);
  process.exitCode = problems.length === 0 ? 0 : 1;
}
