import type { Uploads, Widget } from './models/index.js';
import type { Resources } from './resources.js';

export async function use(resources: Resources): Promise<[Widget, Uploads, Uploads]> {
  return [
    await resources.widgets.get('w1', { verbose: true }),
    await resources.uploads.list(),
    await resources.uploads.list({ xTenantId: 't1' }),
  ];
}
