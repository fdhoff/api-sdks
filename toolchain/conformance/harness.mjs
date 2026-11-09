import { createHash } from 'node:crypto';
import { createServer } from 'node:http';
import { setTimeout as sleep } from 'node:timers/promises';
import { gzipSync } from 'node:zlib';

const HOP_BY_HOP = ['host', 'connection', 'content-length', 'transfer-encoding', 'prefer'];

const expandDate = (value) =>
  String(value).replace(/\{\{http_date\+(\d+)s\}\}/g, (_, seconds) => new Date(Date.now() + Number(seconds) * 1000).toUTCString());

// A list of values sends the header once per value.
const expandDates = (headers) =>
  Object.fromEntries(Object.entries(headers).map(([name, value]) => [name, Array.isArray(value) ? value.map(expandDate) : expandDate(value)]));

// A server compresses only for a client that accepts it.
const acceptsGzip = (header = '') =>
  header.split(',').some((item) => {
    const [coding, ...params] = item.split(';').map((part) => part.trim().toLowerCase());
    return ['gzip', '*'].includes(coding) && !params.some((param) => /^q=0(\.0*)?$/.test(param));
  });

async function trickle(response, payload, interval) {
  for (const byte of Buffer.from(payload)) {
    if (response.destroyed) return;
    response.write(Buffer.of(byte));
    await sleep(interval);
  }
  response.end();
}

function send(response, { status, headers = {}, body, body_base64: base64, delay_ms: delay = 0, trickle_ms: interval, gzip, cut }, request) {
  const isText = typeof body === 'string';
  const text = body === undefined ? '' : isText ? body : JSON.stringify(body);
  let payload = base64 === undefined ? Buffer.from(text) : Buffer.from(base64, 'base64');
  const defaults = body === undefined || isText ? {} : { 'content-type': 'application/json' };
  if (gzip && acceptsGzip(request.headers['accept-encoding'])) {
    payload = gzipSync(payload);
    defaults['content-encoding'] = 'gzip';
  }
  if (cut !== undefined) payload = payload.subarray(0, cut);
  const expanded = expandDates(headers);
  const timer = setTimeout(() => {
    if (response.destroyed) return;
    response.writeHead(status, { ...defaults, ...expanded });
    if (interval === undefined) response.end(payload);
    else trickle(response, payload, interval);
  }, delay);
  timer.unref();
}

// A client with several hosts maps host key K to `<harness>/_host/K`. The prefix is recorded as the host
// and removed, so cases and Prism see the operation's own path.
const HOSTED = /^\/_host\/([^/]+)(\/.*)?$/;

export function unhost(pathname) {
  const hosted = HOSTED.exec(pathname);
  return hosted ? { host: decodeURIComponent(hosted[1]), path: hosted[2] ?? '/' } : { path: pathname };
}

async function forward(prismUrl, prism, request, url, body, response) {
  const headers = Object.fromEntries(Object.entries(request.headers).filter(([name]) => !HOP_BY_HOP.includes(name)));
  if (prism.code !== undefined) headers.prefer = `code=${prism.code}`;
  const answer = await fetch(new URL(`${url.pathname}${url.search}`, prismUrl), {
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

  // The second server is another origin, for URLs a client must fetch without its credentials.
  const handle = (crossOrigin) => async (request, response) => {
    // Some HTTP stacks silently resend a GET that fails on a reused connection, which would hide a drop.
    response.setHeader('connection', 'close');
    const chunks = [];
    for await (const chunk of request) chunks.push(chunk);
    const body = Buffer.concat(chunks);
    const url = new URL(request.url, 'http://harness');
    const { host, path } = unhost(url.pathname);
    url.pathname = path;
    requests.push({
      method: request.method,
      ...(host === undefined ? {} : { host }),
      ...(crossOrigin ? { cross_origin: true } : {}),
      path,
      query: Object.fromEntries(url.searchParams),
      headers: request.headers,
      body: body.toString(),
      base64: body.toString('base64'),
      sha256: createHash('sha256').update(body).digest('base64'),
      at: performance.now(),
    });
    if (script) {
      const next = script.shift() ?? { status: 500, body: 'script exhausted' };
      if (next.drop) request.socket.destroy();
      else send(response, next, request);
      return;
    }
    try {
      await forward(prismUrl, mock.prism, request, url, body, response);
    } catch (error) {
      send(response, { status: 500, body: `prism forward failed: ${error.message}` });
    }
  };
  const servers = [createServer(handle(false)), createServer(handle(true))];
  await Promise.all(servers.map((server) => new Promise((resolve) => server.listen(0, '127.0.0.1', resolve))));
  const [server, other] = servers;

  return {
    url: `http://127.0.0.1:${server.address().port}`,
    otherUrl: `http://127.0.0.1:${other.address().port}`,
    play(next) {
      requests = [];
      mock = next;
      script = next.responses ? [...next.responses] : null;
    },
    requests: () => requests,
    close: () =>
      Promise.all(
        servers.map(
          (each) =>
            new Promise((resolve) => {
              each.close(resolve);
              each.closeAllConnections();
            }),
        ),
      ),
  };
}
