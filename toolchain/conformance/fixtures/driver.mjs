import { createInterface } from 'node:readline';

const mode = process.argv[2];

// Walks offset pages as the runtimes do: advance by the items received, stop at an empty page or the count.
async function offsetPages(client, params = {}) {
  const items = [];
  const query = { ...params };
  for (;;) {
    const search = new URLSearchParams(Object.entries(query).map(([name, value]) => [name, String(value)]));
    const response = await fetch(`${client.base_url}/items${search.size > 0 ? `?${search}` : ''}`, {
      headers: { authorization: `Basic ${client.token}` },
    });
    const page = await response.json();
    items.push(...page.results);
    const offset = Number(query.offset ?? 0) + page.results.length;
    if (page.results.length === 0 || (typeof page.count === 'number' && offset >= page.count)) return items;
    query.offset = offset;
  }
}

for await (const line of createInterface({ input: process.stdin })) {
  const { client, request } = JSON.parse(line);
  if (mode === 'silent') {
    console.log(JSON.stringify({ result: { id: 1 }, logs: [] }));
    continue;
  }
  if (mode === 'offset') {
    console.log(JSON.stringify({ result: await offsetPages(client, request.params), logs: [] }));
    continue;
  }
  const response = await fetch(`${client.base_url}/items`, {
    headers: { authorization: `Basic ${client.token}` },
  });
  const logs = mode === 'leaky' ? [`sent ${client.token}`] : [];
  console.log(JSON.stringify({ result: await response.json(), logs }));
}
