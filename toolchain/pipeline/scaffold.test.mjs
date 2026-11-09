import assert from 'node:assert/strict';
import { readdir, readFile } from 'node:fs/promises';
import { join, relative } from 'node:path';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';

const ROOT = fileURLToPath(new URL('../..', import.meta.url));
const FIXTURE = join(ROOT, 'toolchain/pipeline/fixtures/multihost/packages');

// Each reader returns `section:name` -> version for what a package config pins.
function cargo(text) {
  const pins = {};
  let section = '';
  for (const line of text.split('\n')) {
    const header = line.match(/^\[([^\]]+)\]/);
    if (header) section = header[1];
    const entry = line.match(/^([\w-]+)\s*=\s*(?:"([^"]+)"|\{.*?\bversion\s*=\s*"([^"]+)")/);
    if (entry && (section === 'package' ? ['edition', 'rust-version'].includes(entry[1]) : section.endsWith('dependencies'))) {
      pins[`${section}:${entry[1]}`] = entry[2] ?? entry[3];
    }
  }
  return pins;
}

function pyproject(text) {
  const pins = {};
  const python = text.match(/^requires-python\s*=\s*"([^"]+)"/m);
  if (python) pins['project:requires-python'] = python[1];
  for (const [, array, items] of text.matchAll(/^([\w-]+)\s*=\s*\[([\s\S]*?)\]/gm)) {
    for (const [, requirement] of items.matchAll(/"([^"]+)"/g)) {
      const parts = requirement.match(/^([A-Za-z0-9_.-]+)\s*([<>=!~].*)$/);
      if (parts) pins[`${array}:${parts[1].toLowerCase()}`] = parts[2];
    }
  }
  return pins;
}

function packageJson(text) {
  const json = JSON.parse(text);
  const pins = {};
  for (const field of ['dependencies', 'devDependencies']) {
    for (const [name, version] of Object.entries(json[field] ?? {})) pins[`${field}:${name}`] = version;
  }
  return pins;
}

function csproj(text) {
  const pins = {};
  const frameworks = text.match(/<TargetFrameworks?>([^<]+)</);
  if (frameworks) pins['project:TargetFrameworks'] = frameworks[1];
  for (const [, name, version] of text.matchAll(/<PackageReference Include="([^"]+)" Version="([^"]+)"/g)) pins[`package:${name}`] = version;
  return pins;
}

function goMod(text) {
  const pins = {};
  const go = text.match(/^go (\S+)/m);
  if (go) pins['go:go'] = go[1];
  for (const [, name, version] of text.matchAll(/^\s*(?:require\s+)?([\w.-]+\.[\w./-]+) (v\S+)/gm)) pins[`require:${name}`] = version;
  return pins;
}

const LANGUAGES = {
  rust: { file: 'Cargo.toml', read: cargo },
  python: { file: 'pyproject.toml', read: pyproject },
  typescript: { file: 'package.json', read: packageJson },
  csharp: { file: 'src/*/*.csproj', read: csproj },
  go: { file: 'go.mod', read: goMod },
};

async function configs(packageDir, file) {
  if (!file.includes('*')) return [join(packageDir, file)];
  const projects = await readdir(join(packageDir, 'src'), { withFileTypes: true }).catch(() => []);
  const found = [];
  for (const project of projects.filter((entry) => entry.isDirectory())) {
    const names = await readdir(join(packageDir, 'src', project.name));
    found.push(...names.filter((name) => name.endsWith('.csproj')).map((name) => join(packageDir, 'src', project.name, name)));
  }
  return found;
}

async function pinsOf(packageDir, { file, read }) {
  const merged = {};
  for (const path of await configs(packageDir, file)) {
    const text = await readFile(path, 'utf8').catch(() => null);
    if (text !== null) Object.assign(merged, read(text));
  }
  return merged;
}

test('the template fixture pins what the real packages of each language pin', async () => {
  const apis = (await readdir(join(ROOT, 'apis'), { withFileTypes: true })).filter((entry) => entry.isDirectory());
  for (const [language, reader] of Object.entries(LANGUAGES)) {
    const fixture = await pinsOf(join(FIXTURE, language), reader);
    assert.ok(Object.keys(fixture).length > 0, `${language}: the fixture pins nothing`);
    const packages = [];
    for (const api of apis) {
      const packageDir = join(ROOT, 'apis', api.name, 'packages', language);
      const pins = await pinsOf(packageDir, reader);
      if (Object.keys(pins).length > 0) packages.push({ name: relative(ROOT, packageDir), pins });
    }
    for (const [key, version] of Object.entries(fixture)) {
      const users = packages.filter(({ pins }) => key in pins);
      assert.ok(users.length > 0, `${language}: the fixture pins ${key}, which no package does`);
      for (const { name, pins } of users) {
        assert.equal(pins[key], version, `${language}: ${key} is ${version} in the fixture but ${pins[key]} in ${name}`);
      }
    }
  }
});
