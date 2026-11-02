import { createServer } from 'node:http';
import { setTimeout as sleep } from 'node:timers/promises';

const HOP_BY_HOP = ['host', 'connection', 'content-length', 'transfer-encoding', 'prefer'];

const expandDates = (headers) =>
  Object.fromEntries(
    Object.entries(headers).map(([name, value]) => [
      name,
      String(value).replace(/\{\{http_date\+(\d+)s\}\}/g, (_, seconds) =>
        new Date(Date.now() + Number(seconds) * 1000).toUTCString(),
      ),
    ]),
  );

async function trickle(response, payload, interval) {
  for (const byte of Buffer.from(payload)) {
    if (response.destroyed) return;
    response.write(Buffer.of(byte));
    await sleep(interval);
  }
  response.end();
}

function send(response, { status, headers = {}, body, delay_ms: delay = 0, trickle_ms: interval }) {
  const isText = typeof body === 'string';
  const payload = body === undefined ? '' : isText ? body : JSON.stringify(body);
  const defaults = body === undefined || isText ? {} : { 'content-type': 'application/json' };
  const expanded = expandDates(headers);
  const timer = setTimeout(() => {
    if (response.destroyed) return;
    response.writeHead(status, { ...defaults, ...expanded });
    if (interval === undefined) response.end(payload);
    else trickle(response, payload, interval);
  }, delay);
  timer.unref();
}

async function forward(prismUrl, prism, request, body, response) {
  const headers = Object.fromEntries(Object.entries(request.headers).filter(([name]) => !HOP_BY_HOP.includes(name)));
  if (prism.code !== undefined) headers.prefer = `code=${prism.code}`;
  const answer = await fetch(new URL(request.url, prismUrl), {
    method: request.method,
    headers,
    body: body.length > 0 ? body : undefined,
  });
  const contentType = answer.headers.get('content-type');
  response.writeHead(answer.status, contentType ? { 'content-type': contentType } : {});
  response.end(Buffer.from(await answer.arrayBuffer()));
}

export async function startHarness(prismUrl) {
  let requests = [];
  let script = null;
  let mock = {};

  const server = createServer(async (request, response) => {
    // Some HTTP stacks silently resend a GET that fails on a reused connection, which would hide a drop.
    response.setHeader('connection', 'close');
    const chunks = [];
    for await (const chunk of request) chunks.push(chunk);
    const body = Buffer.concat(chunks);
    const url = new URL(request.url, 'http://harness');
    requests.push({
      method: request.method,
      path: url.pathname,
      query: Object.fromEntries(url.searchParams),
      headers: request.headers,
      body: body.toString(),
      at: performance.now(),
    });
    if (script) {
      const next = script.shift() ?? { status: 500, body: 'script exhausted' };
      if (next.drop) request.socket.destroy();
      else send(response, next);
      return;
    }
    try {
      await forward(prismUrl, mock.prism, request, body, response);
    } catch (error) {
      send(response, { status: 500, body: `prism forward failed: ${error.message}` });
    }
  });
  await new Promise((resolve) => server.listen(0, '127.0.0.1', resolve));

  return {
    url: `http://127.0.0.1:${server.address().port}`,
    play(next) {
      requests = [];
      mock = next;
      script = next.responses ? [...next.responses] : null;
    },
    requests: () => requests,
    close: () =>
      new Promise((resolve) => {
        server.close(resolve);
        server.closeAllConnections();
      }),
  };
}
