// Checks that the pinned URL still serves an OpenAPI document, for the spec drift job. The spec has an empty
// `info.version`, so the drift job compares content by hash, and its operation diff fails the run when
// operations are removed. Uses only Node's own modules.
import { readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';

const METHODS = ['get', 'put', 'post', 'delete', 'patch'];

// Why a response is not a spec, or null when it is one.
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
  if (!Object.values(spec.paths).some((item) => METHODS.some((method) => item?.[method]))) return 'an OpenAPI document with no operations';
  return null;
}

// Every problem found, as a sentence each. None means the URL still serves a spec.
export async function checkUpstream(lock, get = fetch) {
  let response;
  try {
    response = await get(lock.url);
  } catch (error) {
    return [`The pinned URL ${lock.url} could not be fetched: ${error.message}.`];
  }
  const problem = specProblem(response.status, await response.text());
  return problem ? [`The pinned URL ${lock.url} answered with ${problem}.`] : [];
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const lock = JSON.parse(await readFile(new URL('./upstream/lock.json', import.meta.url), 'utf8'));
  const problems = await checkUpstream(lock);
  for (const problem of problems) console.log(`::error title=Mirakl upstream spec::${problem}`);
  if (problems.length === 0) console.log(`${lock.url} still serves an OpenAPI document.`);
  process.exitCode = problems.length === 0 ? 0 : 1;
}
