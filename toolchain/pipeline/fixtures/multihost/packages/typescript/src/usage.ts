import type { Bin, ImportStatus, Part, Uploads, Widget } from './models/index.js';
import type { Resources } from './resources.js';

export async function use(resources: Resources): Promise<[Widget, Uploads, Uploads]> {
  return [
    await resources.widgets.get('w1', { verbose: true }),
    await resources.uploads.list(),
    await resources.uploads.list({ xTenantId: 't1' }),
  ];
}

export async function wait(resources: Resources, signal: AbortSignal): Promise<ImportStatus> {
  return resources.imports.wait(7, { intervalMs: 1000, timeoutMs: 60000, signal });
}

export async function iterate(resources: Resources): Promise<[Part[], Bin[]]> {
  const parts: Part[] = [];
  for await (const part of resources.parts.iter({ limit: 2 })) parts.push(part);
  const bins: Bin[] = [];
  for await (const bin of resources.bins.iter({ zone: 'a' })) bins.push(bin);
  return [parts, bins];
}
