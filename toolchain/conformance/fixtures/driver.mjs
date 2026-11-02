import { createInterface } from 'node:readline';

const mode = process.argv[2];

for await (const line of createInterface({ input: process.stdin })) {
  const { client } = JSON.parse(line);
  if (mode === 'silent') {
    console.log(JSON.stringify({ result: { id: 1 }, logs: [] }));
    continue;
  }
  const response = await fetch(`${client.base_url}/items`, {
    headers: { authorization: `Basic ${client.token}` },
  });
  const logs = mode === 'leaky' ? [`sent ${client.token}`] : [];
  console.log(JSON.stringify({ result: await response.json(), logs }));
}
