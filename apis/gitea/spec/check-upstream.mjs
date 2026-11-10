// Checks that the pinned release tag is still Gitea's newest stable release, for the spec drift job. Each release
// serves its spec at its own URL, which never changes, so content drift never fires: a new release is the only
// drift. Uses only Node's own modules and git.
import { execFile } from 'node:child_process';
import { readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { promisify } from 'node:util';

export const REPOSITORY = 'https://github.com/go-gitea/gitea';
const STABLE = /^v(\d+)\.(\d+)\.(\d+)$/;

export const specUrl = (tag) => `https://raw.githubusercontent.com/go-gitea/gitea/${tag}/templates/swagger/v1-openapi3.generated.json`;

// The stable `vN.N.N` tags in `git ls-remote --tags` output. Release candidates and other tags are skipped.
export function stableTags(listing) {
  return listing
    .split('\n')
    .map((line) => line.split('\t')[1]?.trim().replace(/^refs\/tags\//, '').replace(/\^\{\}$/, ''))
    .filter((tag) => STABLE.test(tag ?? ''));
}

const parts = (tag) => STABLE.exec(tag).slice(1).map(Number);

export function compareTags(a, b) {
  const [x, y] = [parts(a), parts(b)];
  return x[0] - y[0] || x[1] - y[1] || x[2] - y[2];
}

export const newestStable = (tags) => [...tags].sort(compareTags).at(-1) ?? null;

export async function listTags() {
  const { stdout } = await promisify(execFile)('git', ['ls-remote', '--tags', '--refs', REPOSITORY], { maxBuffer: 16 * 1024 * 1024 });
  return stdout;
}

// The newest stable release and its spec URL. Throws when none can be found.
export async function newestRelease(list = listTags) {
  const tag = newestStable(stableTags(await list()));
  if (!tag) throw new Error(`${REPOSITORY} lists no stable vN.N.N release tag`);
  return { tag, url: specUrl(tag) };
}

// Every problem found, as a sentence each. None means the pin is the newest stable release.
export async function checkUpstream(lock, list = listTags) {
  if (!STABLE.test(lock.tag ?? '')) return [`lock.json tag ${lock.tag} is not a stable vN.N.N release tag.`];
  if (lock.url !== specUrl(lock.tag)) return [`lock.json url ${lock.url} is not the spec URL of tag ${lock.tag}.`];
  let newest;
  try {
    newest = await newestRelease(list);
  } catch (error) {
    return [`Gitea's release tags could not be listed: ${error.message}.`];
  }
  if (compareTags(newest.tag, lock.tag) > 0) {
    return [`Gitea ${newest.tag} is newer than the pinned ${lock.tag}. The spec drift pull request moves the pin to it.`];
  }
  return [];
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const lock = JSON.parse(await readFile(new URL('./upstream/lock.json', import.meta.url), 'utf8'));
  const problems = await checkUpstream(lock);
  for (const problem of problems) console.log(`::error title=Gitea upstream spec::${problem}`);
  if (problems.length === 0) console.log(`${lock.tag} is still Gitea's newest stable release.`);
  process.exitCode = problems.length === 0 ? 0 : 1;
}
