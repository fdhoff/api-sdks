// Applies an API's overlay to its pinned spec, producing <api-dir>/build/openapi.yaml.
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import openapiFormat from 'openapi-format';
import { parse, stringify } from 'yaml';
import { ensureSpec } from './fetch-spec.mjs';
import { apiDirFromArgs, apiPaths } from './paths.mjs';

export async function applyOverlay(spec, overlay) {
  const { data, resultData } = await openapiFormat.openapiOverlay(spec, { overlaySet: overlay });
  if (resultData.totalActions === 0) throw new Error('Overlay has no actions');
  if (resultData.unusedActions.length > 0) {
    const targets = resultData.unusedActions.map((action) => action.target).join(', ');
    throw new Error(`Overlay actions matched nothing: ${targets}`);
  }
  return data;
}

async function build(paths) {
  const spec = parse((await ensureSpec(paths)).toString('utf8'));
  const overlay = parse(await readFile(paths.overlay, 'utf8'));
  const corrected = await applyOverlay(spec, overlay);
  await mkdir(dirname(paths.build), { recursive: true });
  await writeFile(paths.build, stringify(corrected, { lineWidth: 0, compat: 'yaml-1.1' }));
  console.log(`Built ${paths.build}`);
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  await build(apiPaths(apiDirFromArgs(process.argv)));
}
