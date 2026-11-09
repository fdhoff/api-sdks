// Prints `matrix=` for $GITHUB_OUTPUT: one {api, language, package, version} per published package to smoke test.
// Given a language and version, that API's package at that version. Given a Go module tag, that module. Otherwise
// the latest version on its registry of every package, or of those an API or language filter picks; a package
// with no published version is left out. Uses only Node's own modules, so it runs before `npm ci`.
import { readdir, readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { parseArgs } from 'node:util';

export const LANGUAGES = ['python', 'typescript', 'go', 'csharp', 'rust'];
// The smoke program each package keeps under `published/`, which smoke.sh copies into the clean project.
export const PROGRAMS = { python: 'smoke.py', typescript: 'smoke.mts', go: 'main.go', csharp: 'Program.cs', rust: 'main.rs' };
const GO_TAG = /^apis\/([a-z0-9-]+)\/packages\/go\/v(.+)$/;
// A pseudo-version names a commit, not a release: proxy.golang.org answers @latest with one for an untagged module.
const PSEUDO_VERSION = /\d{14}-[0-9a-f]{12}$/;

const first = (text, pattern) => text.match(pattern)?.[1] ?? null;

// The name a package is published under: the same lookups the release target action makes, plus Go's module path.
export async function packageName(apiDir, language) {
  const dir = join(apiDir, 'packages', language);
  const read = (file) => readFile(join(dir, file), 'utf8');
  switch (language) {
    case 'python':
      return first(await read('pyproject.toml'), /^name = "(.*)"$/m);
    case 'typescript':
      return JSON.parse(await read('package.json')).name ?? null;
    case 'go':
      return first(await read('go.mod'), /^module (\S+)$/m);
    case 'csharp': {
      for (const project of await readdir(join(dir, 'src'))) {
        const file = join('src', project, `${project}.csproj`);
        const id = first(await read(file).catch(() => ''), /<PackageId>(.*)<\/PackageId>/);
        if (id) return id;
      }
      return null;
    }
    case 'rust':
      return first(await read('Cargo.toml'), /^name = "(.*)"$/m);
    default:
      throw new Error(`Unknown language ${language}`);
  }
}

// Each API and language with a package, as CI and the release workflows find them.
export async function packages(root) {
  const found = [];
  for (const api of (await readdir(join(root, 'apis'))).sort()) {
    for (const language of LANGUAGES) {
      const files = await readdir(join(root, 'apis', api, 'packages', language)).catch(() => []);
      if (files.includes('generate.yaml')) found.push({ api, language });
    }
  }
  return found;
}

const goEscape = (path) => path.replace(/[A-Z]/g, (letter) => `!${letter.toLowerCase()}`);

function cratePath(name) {
  if (name.length <= 2) return `${name.length}/${name}`;
  if (name.length === 3) return `3/${name[0]}/${name}`;
  return `${name.slice(0, 2)}/${name.slice(2, 4)}/${name}`;
}

// Where each registry lists a package's versions.
export function registryUrl(language, name) {
  switch (language) {
    case 'python':
      return `https://pypi.org/pypi/${name}/json`;
    case 'typescript':
      return `https://registry.npmjs.org/${name}`;
    case 'go':
      return `https://proxy.golang.org/${goEscape(name)}/@latest`;
    case 'csharp':
      return `https://api.nuget.org/v3-flatcontainer/${name.toLowerCase()}/index.json`;
    case 'rust':
      return `https://index.crates.io/${cratePath(name.toLowerCase())}`;
    default:
      throw new Error(`Unknown language ${language}`);
  }
}

// The version a registry's listing says was published last, or null if it lists none. Prereleases count: every
// package is on 0.x alphas.
export function latestVersion(language, body) {
  switch (language) {
    case 'python': {
      const uploaded = Object.entries(JSON.parse(body).releases ?? {})
        .map(([version, files]) => [version, files.filter((file) => !file.yanked).map((file) => file.upload_time_iso_8601)])
        .filter(([, times]) => times.length > 0)
        .map(([version, times]) => [version, times.sort().at(-1)]);
      return uploaded.sort(([, a], [, b]) => a.localeCompare(b)).at(-1)?.[0] ?? null;
    }
    case 'typescript': {
      const { versions = {}, time = {} } = JSON.parse(body);
      const published = Object.keys(versions).filter((version) => time[version]);
      return published.sort((a, b) => time[a].localeCompare(time[b])).at(-1) ?? null;
    }
    case 'go': {
      const version = JSON.parse(body).Version ?? '';
      return version && !PSEUDO_VERSION.test(version) ? version.replace(/^v/, '') : null;
    }
    case 'csharp':
      return JSON.parse(body).versions?.at(-1) ?? null;
    case 'rust': {
      const releases = body.split('\n').filter(Boolean).map((line) => JSON.parse(line));
      return releases.filter((release) => !release.yanked).at(-1)?.vers ?? null;
    }
    default:
      throw new Error(`Unknown language ${language}`);
  }
}

async function published(language, name) {
  const response = await fetch(registryUrl(language, name), { headers: { accept: 'application/json' } });
  if ([404, 410].includes(response.status)) return null;
  if (!response.ok) throw new Error(`${registryUrl(language, name)} answered ${response.status}`);
  return latestVersion(language, await response.text());
}

export async function targets(root, { api, language, version, tag }, lookup = published) {
  const go = GO_TAG.exec(tag ?? '');
  if (!language && go) {
    language = 'go';
    [, api, version] = go;
  }
  if (version && !(api && language)) throw new Error('A version needs an API and a language');
  if (language && !LANGUAGES.includes(language)) throw new Error(`Unknown language ${language}`);
  const chosen = (await packages(root)).filter((item) => (!api || item.api === api) && (!language || item.language === language));
  if (version && chosen.length === 0) throw new Error(`apis/${api} has no ${language} package`);
  const matrix = [];
  for (const item of chosen) {
    const name = await packageName(join(root, 'apis', item.api), item.language);
    if (!name) throw new Error(`apis/${item.api}/packages/${item.language} does not declare a package name`);
    const resolved = version || (await lookup(item.language, name));
    if (resolved) matrix.push({ ...item, package: name, version: resolved });
    else console.error(`::notice title=Not published::${name} (${item.language}) has no published version.`);
  }
  return matrix;
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const { values } = parseArgs({
    options: { api: { type: 'string' }, language: { type: 'string' }, version: { type: 'string' }, tag: { type: 'string' } },
  });
  const blank = Object.fromEntries(Object.entries(values).map(([key, value]) => [key, value || undefined]));
  const root = fileURLToPath(new URL('../../', import.meta.url));
  console.log(`matrix=${JSON.stringify(await targets(root, blank))}`);
}
