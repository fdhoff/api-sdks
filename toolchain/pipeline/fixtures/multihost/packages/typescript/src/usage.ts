import type { ImportStatus, Uploads, Widget } from './models/index.js';
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
