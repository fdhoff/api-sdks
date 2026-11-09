import { redact, type AuthRequest, type Credentials, type Requirement } from './credentials.js';
import { ApiConnectionError, ApiError, ApiTimeoutError, DecodeError, type ErrorContext } from './errors.js';

export type FileContent = Blob | Uint8Array;

/** A file to upload: its content, or its name and content. */
export type FileInput = FileContent | { filename: string; content: FileContent };

/** A raw request body, sent unchanged. Bytes and a Blob are retried like any body; a stream is sent once,
 * so a failure that would resend it is raised instead, and credentials see an empty body. A Node stream,
 * such as one from `fs.createReadStream`, is passed as `Readable.toWeb(stream)`; `fs.openAsBlob(path)`
 * gives a Blob that can be retried. */
export type RawBody = Uint8Array | Blob | ReadableStream<Uint8Array>;

/** A binary response. The call's deadline keeps running while `body` is read, so a timeout must cover the
 * whole transfer. Read `body` or call `bytes()` once, or cancel `body` to release the connection. The call
 * asks for no compression, but Node's fetch decodes a compressed body anyway, so `body` holds the decoded
 * bytes where the other languages pass them on as received. */
export interface Download {
  /** The response's `Content-Type`, empty if it has none. */
  readonly contentType: string;
  readonly body: ReadableStream<Uint8Array>;
  /** Reads the whole body. */
  bytes(): Promise<Uint8Array>;
}

/** `form` is a multipart part, `urlencoded` a field of a form-encoded body, and `header` a header that
 * falls back to the client's default for it. */
export interface Param {
  wire: string;
  name: string;
  location: 'path' | 'query' | 'form' | 'urlencoded' | 'header';
}

/** Pages that link to the next one. Only `params` are read from the link: it is never fetched. */
export interface NextLink {
  style: 'next_link';
  items: string;
  link: string;
  params: readonly string[];
}

/** Pages addressed by an offset, which advances by the number of items received. Iteration ends at an
 * empty page or once the offset reaches the page's `total`. */
export interface Offset {
  style: 'offset';
  items: string;
  total: string;
  offset: string;
}

export type Paging = NextLink | Offset;

export interface Operation {
  id: string;
  method: string;
  path: string;
  resource: string;
  name: string;
  /** The key of the host that serves it, in `Settings.hosts`. Without one, it goes to `baseUrl`. */
  host?: string;
  params: readonly Param[];
  hasBody?: boolean;
  returnsJson?: boolean;
  returnsText?: boolean;
  /** The success body is bytes, returned as a {@link Download}. */
  returnsBinary?: boolean;
  /** The media type of a raw request body, which the call takes as a {@link RawBody}. */
  rawBody?: string;
  iterator?: string;
  paging?: Paging;
  /** Any one of these requirements authorizes the call. */
  security?: readonly Requirement[];
}

/** Options for one call. */
export interface RequestOptions {
  /** Cancels the call, including a wait before a retry. The call rejects with the signal's reason. */
  signal?: AbortSignal;
}

/** Receives what the client logs. `console` fits. */
export interface Logger {
  debug(message: string): void;
  info(message: string): void;
}

export interface Settings {
  /** Where an operation with no host key is sent, without a trailing slash. */
  baseUrl: string;
  /** The base URL of each host key that operations name, without a trailing slash, as `selectHosts` returns them. */
  hosts?: Readonly<Record<string, string>>;
  /** Values for header parameters that an operation declares and the call leaves unset, by header name. */
  headerDefaults?: Readonly<Record<string, string>>;
  credentials: Credentials;
  headers: Record<string, string>;
  toError: (context: ErrorContext) => ApiError;
  fetch: typeof globalThis.fetch;
  logger?: Logger;
  timeoutMs: number;
  maxRetries: number;
  retryBaseDelayMs: number;
  rateLimitWaitMs: number;
  maxRetryWaitMs: number;
}

type Params = Record<string, unknown>;

interface Built {
  url: string;
  headers: Record<string, string>;
  body: string | FormData | URLSearchParams | RawBody | undefined;
}

interface Encoded {
  bytes: Uint8Array;
  contentType?: string;
  /** The body is a stream, which can be sent only once. */
  streamed?: boolean;
}
const NEXT_LINK: NextLink = { style: 'next_link', items: 'results', link: 'next', params: ['page', 'cursor'] };
const HTTP_DATE = /^[A-Z][a-z]{2}, \d{2} [A-Z][a-z]{2} \d{4} \d{2}:\d{2}:\d{2} GMT$/;
const MAX_TIMER_MS = 2 ** 31 - 1;

const isObject = (value: unknown): value is Record<string, unknown> => typeof value === 'object' && value !== null;
const isContent = (value: unknown): value is FileContent => value instanceof Blob || value instanceof Uint8Array;
const formText = (value: unknown): string =>
  value instanceof Date ? value.toISOString() : isObject(value) ? JSON.stringify(value) : String(value);

function appendFile(form: FormData, wire: string, content: FileContent, filename: string): void {
  form.append(wire, content instanceof Blob ? content : new Blob([content as Uint8Array<ArrayBuffer>]), filename);
}

function appendPart(form: FormData, wire: string, value: unknown): void {
  if (Array.isArray(value)) value.forEach((item) => appendPart(form, wire, item));
  else if (value instanceof File) appendFile(form, wire, value, value.name);
  else if (isContent(value)) appendFile(form, wire, value, wire);
  else if (isObject(value) && isContent(value['content']) && typeof value['filename'] === 'string') {
    appendFile(form, wire, value['content'], value['filename']);
  } else form.append(wire, formText(value));
}

const sameName = (record: Readonly<Record<string, string>>, name: string): string[] =>
  Object.keys(record).filter((key) => key.toLowerCase() === name.toLowerCase());

/** The base URL for an operation. A host key with no URL is a configuration error, so nothing is sent. */
function baseUrlFor(settings: Settings, operation: Operation): string {
  if (!operation.host) return settings.baseUrl;
  const hosts = settings.hosts ?? {};
  if (!Object.hasOwn(hosts, operation.host)) throw new Error(`No base URL for host "${operation.host}"`);
  return hosts[operation.host]!;
}

/** `defaults` keyed by lowercase name. Two names that differ only by case are an error. */
function byLowercase(defaults: Readonly<Record<string, string>>): Map<string, string> {
  const byName = new Map<string, string>();
  const clashes = new Set<string>();
  for (const [name, value] of Object.entries(defaults)) {
    for (const other of sameName(defaults, name)) if (other !== name) clashes.add(name);
    byName.set(name.toLowerCase(), value);
  }
  if (clashes.size > 0) {
    throw new Error(`headerDefaults has names that differ only by case: ${[...clashes].sort().join(', ')}`);
  }
  return byName;
}

const trimmed = (hosts: Readonly<Record<string, string>>): Record<string, string> =>
  Object.fromEntries(Object.entries(hosts).map(([key, url]) => [key, url.replace(/\/+$/, '')]));

/** The host map for a named environment, or the caller's own, which must name exactly the keys the
 * environments use. Trailing slashes are removed from every URL. */
export function selectHosts(
  environments: Readonly<Record<string, Readonly<Record<string, string>>>>,
  environment: string,
  hosts?: Readonly<Record<string, string>>,
): Record<string, string> {
  if (hosts !== undefined && Object.keys(hosts).length > 0) {
    const keys = new Set(Object.values(environments).flatMap((map) => Object.keys(map)));
    const missing = [...keys].filter((key) => !Object.hasOwn(hosts, key)).sort();
    const unknown = Object.keys(hosts)
      .filter((key) => !keys.has(key))
      .sort();
    if (missing.length > 0) throw new Error(`hosts lacks keys: ${missing.join(', ')}`);
    if (unknown.length > 0) throw new Error(`hosts has unknown keys: ${unknown.join(', ')}`);
    return trimmed(hosts);
  }
  if (!Object.hasOwn(environments, environment)) {
    const known = Object.keys(environments).sort().join(', ');
    throw new Error(`Unknown environment "${environment}"; expected one of: ${known}`);
  }
  return trimmed(environments[environment]!);
}

function buildRequest(
  settings: Settings,
  defaults: ReadonlyMap<string, string>,
  operation: Operation,
  body: unknown,
  params: Params,
): Built {
  const baseUrl = baseUrlFor(settings, operation);
  let path = operation.path;
  const declared: [string, string][] = [];
  const query = new URLSearchParams();
  const form = new FormData();
  const fields = new URLSearchParams();
  let hasParts = false;
  for (const { wire, name, location } of operation.params) {
    const value = params[name];
    if (location === 'header') {
      const sent = value ?? defaults.get(wire.toLowerCase());
      if (sent !== undefined && sent !== null) declared.push([wire, String(sent)]);
      continue;
    }
    if (value === undefined || value === null) {
      if (location === 'path') throw new TypeError(`${name} is required`);
      continue;
    }
    if (location === 'path') {
      path = path.replace(`{${wire}}`, encodeURIComponent(String(value)));
    } else if (location === 'query') {
      for (const item of Array.isArray(value) ? value : [value]) query.append(wire, String(item));
    } else if (location === 'urlencoded') {
      for (const item of Array.isArray(value) ? value : [value]) fields.append(wire, formText(item));
    } else {
      appendPart(form, wire, value);
      hasParts = true;
    }
  }
  const search = query.size > 0 ? `?${query}` : '';
  // fetch accepts a gzip body cut short, so ask for none.
  const headers: Record<string, string> = { 'Accept-Encoding': 'identity', ...settings.headers };
  for (const [wire, value] of declared) {
    for (const key of sameName(headers, wire)) delete headers[key];
    headers[wire] = value;
  }
  let encoded: Built['body'];
  if (operation.rawBody !== undefined) {
    if (body === undefined || body === null) throw new TypeError('body is required');
    encoded = body as RawBody;
    headers['Content-Type'] = operation.rawBody;
  } else if (hasParts) {
    encoded = form;
  } else if (fields.size > 0) {
    encoded = fields;
  } else if (body !== undefined) {
    encoded = JSON.stringify(body);
    headers['Content-Type'] = 'application/json';
  }
  return { url: `${baseUrl}${path}${search}`, headers, body: encoded };
}

/** The exact bytes to send, so that credentials can sign them. A multipart form is encoded once, with one
 * boundary. */
async function encode(body: Built['body']): Promise<Encoded> {
  if (body === undefined) return { bytes: new Uint8Array() };
  if (typeof body === 'string') return { bytes: new TextEncoder().encode(body) };
  if (body instanceof Uint8Array) return { bytes: body };
  if (body instanceof Blob) return { bytes: new Uint8Array(await body.arrayBuffer()) };
  if (body instanceof ReadableStream) return { bytes: new Uint8Array(), streamed: true };
  const draft = new Request('http://body.invalid/', { method: 'POST', body });
  return {
    bytes: new Uint8Array(await draft.arrayBuffer()),
    contentType: draft.headers.get('content-type') ?? undefined,
  };
}

function parseJson(text: string): unknown {
  try {
    return JSON.parse(text);
  } catch {
    return undefined;
  }
}

function causeCode(error: unknown): string {
  const cause = isObject(error) ? error['cause'] : undefined;
  const code = isObject(cause) ? cause['code'] : undefined;
  return typeof code === 'string' ? code : '';
}

function translate(error: unknown): ApiError {
  const name = error instanceof Error ? error.name : 'Error';
  if (name === 'TimeoutError') return new ApiTimeoutError('The request timed out');
  return new ApiConnectionError(`The connection failed: ${causeCode(error) || name}`);
}

/** Passes a download's bytes on, reporting a failure mid-body as the API error it is, or as the caller's own
 * abort reason. */
function downloadBody(
  source: ReadableStream<Uint8Array> | null,
  signal: AbortSignal | undefined,
): ReadableStream<Uint8Array> {
  if (source === null) return new ReadableStream<Uint8Array>({ start: (controller) => controller.close() });
  const reader = source.getReader();
  return new ReadableStream<Uint8Array>({
    async pull(controller) {
      try {
        const { done, value } = await reader.read();
        if (done) controller.close();
        else controller.enqueue(value);
      } catch (error) {
        controller.error(signal?.aborted ? signal.reason : translate(error));
      }
    },
    cancel: (reason) => reader.cancel(reason),
  });
}

async function readAll(stream: ReadableStream<Uint8Array>): Promise<Uint8Array> {
  const chunks: Uint8Array[] = [];
  const reader = stream.getReader();
  for (let next = await reader.read(); !next.done; next = await reader.read()) chunks.push(next.value);
  const whole = new Uint8Array(chunks.reduce((total, chunk) => total + chunk.length, 0));
  let offset = 0;
  for (const chunk of chunks) {
    whole.set(chunk, offset);
    offset += chunk.length;
  }
  return whole;
}

function download(response: Response, signal: AbortSignal | undefined): Download {
  const body = downloadBody(response.body, signal);
  return { contentType: response.headers.get('content-type') ?? '', body, bytes: () => readAll(body) };
}

function sleep(ms: number, signal: AbortSignal | undefined): Promise<void> {
  return new Promise((resolve, reject) => {
    signal?.throwIfAborted();
    const abort = () => {
      clearTimeout(timer);
      reject(signal?.reason);
    };
    const timer = setTimeout(() => {
      signal?.removeEventListener('abort', abort);
      resolve();
    }, ms);
    signal?.addEventListener('abort', abort, { once: true });
  });
}

function retryAfterMs(value: string | undefined): number | undefined {
  if (value === undefined) return undefined;
  const text = value.trim();
  if (/^\d+$/.test(text)) return Number(text) * 1000;
  if (!HTTP_DATE.test(text)) return undefined;
  const wait = Date.parse(text) - Date.now();
  return wait > 0 ? wait : undefined;
}

function retryDelay(settings: Settings, error: ApiError, method: string, tries: number): number | undefined {
  if (tries >= settings.maxRetries) return undefined;
  if (error.status === 429) {
    const after = retryAfterMs(error.retryAfter);
    if (after !== undefined && after > settings.maxRetryWaitMs) return undefined;
    const wait = after ?? settings.rateLimitWaitMs;
    return wait <= MAX_TIMER_MS ? wait : undefined;
  }
  const failed = error instanceof ApiTimeoutError || error instanceof ApiConnectionError || (error.status ?? 0) >= 500;
  return method === 'GET' && failed ? settings.retryBaseDelayMs * 2 ** tries : undefined;
}

/** Read the position out of the link and apply it to our own request. The link is never fetched:
 * it could send the credential to another host. */
function nextLink(
  operation: Operation,
  paging: NextLink,
  params: Params,
  page: Record<string, unknown>,
): Params | undefined {
  const link = page[paging.link];
  if (!link) return undefined;
  let position: URLSearchParams;
  try {
    position = new URL(String(link), 'http://next.invalid').searchParams;
  } catch {
    throw new DecodeError(`The \`${paging.link}\` link is not a valid URL`);
  }
  const names = operation.params.filter(({ location }) => location === 'query');
  const updated = { ...params };
  for (const { wire, name } of names) {
    const value = position.get(wire);
    if (paging.params.includes(wire) && value) updated[name] = value;
  }
  if (names.every(({ name }) => String(updated[name]) === String(params[name]))) {
    throw new DecodeError(`The \`${paging.link}\` link does not advance the iteration`);
  }
  return updated;
}

function nextOffset(
  operation: Operation,
  paging: Offset,
  params: Params,
  page: Record<string, unknown>,
  received: number,
): Params | undefined {
  if (received === 0) return undefined;
  const param = operation.params.find(({ wire, location }) => location === 'query' && wire === paging.offset);
  if (param === undefined) throw new DecodeError(`The operation has no \`${paging.offset}\` parameter`);
  const start = String(params[param.name] ?? 0);
  if (!/^[+-]?\d+$/.test(start)) throw new DecodeError(`The \`${paging.offset}\` parameter is not an integer`);
  const position = Number(start) + received;
  const total = page[paging.total];
  if (typeof total === 'number' && position >= total) return undefined;
  return { ...params, [param.name]: position };
}

/** The parameters of the page after this one, or undefined after the last. */
function nextParams(operation: Operation, params: Params, page: unknown, received: number): Params | undefined {
  if (!isObject(page) || Array.isArray(page)) throw new DecodeError('A page is not a JSON object');
  const paging = operation.paging ?? NEXT_LINK;
  if (!Array.isArray(page[paging.items])) throw new DecodeError(`The \`${paging.items}\` field of a page is not a list`);
  return paging.style === 'offset'
    ? nextOffset(operation, paging, params, page, received)
    : nextLink(operation, paging, params, page);
}

function items(operation: Operation, page: unknown): unknown[] {
  const results = isObject(page) ? page[(operation.paging ?? NEXT_LINK).items] : undefined;
  return Array.isArray(results) ? results : [];
}

export class Transport {
  readonly #settings: Settings;
  readonly #headerDefaults: ReadonlyMap<string, string>;
  readonly #generations = new Map<string, number>();
  readonly #refreshing = new Map<string, Promise<boolean>>();
  #lastRefresh: Promise<unknown> = Promise.resolve();

  constructor(settings: Settings) {
    this.#settings = settings;
    this.#headerDefaults = byLowercase(settings.headerDefaults ?? {});
  }

  #log(level: keyof Logger, message: string): void {
    this.#settings.logger?.[level](redact(this.#settings.credentials, message));
  }

  /** Calls waiting on a refresh of the same group share it, and a call whose credentials were refreshed since it
   * sent them retries without another. Refreshes run one at a time. */
  #refresh(request: AuthRequest, group: string, generation: number): Promise<boolean> {
    const { credentials } = this.#settings;
    if ((this.#generations.get(group) ?? 0) !== generation) return Promise.resolve(true);
    if (credentials.refresh === undefined) return Promise.resolve(false);
    let refreshing = this.#refreshing.get(group);
    if (refreshing === undefined) {
      refreshing = this.#lastRefresh.then(async () => {
        try {
          const refreshed = await credentials.refresh!(request);
          if (refreshed) this.#generations.set(group, generation + 1);
          return refreshed;
        } finally {
          this.#refreshing.delete(group);
        }
      });
      this.#refreshing.set(group, refreshing);
      this.#lastRefresh = refreshing.catch(() => undefined);
    }
    return refreshing;
  }

  async #attempt(
    { method, returnsJson, returnsText, returnsBinary }: Operation,
    url: string,
    init: RequestInit,
    signal: AbortSignal | undefined,
  ): Promise<unknown> {
    const settings = this.#settings;
    const { fetch } = settings;
    this.#log('debug', `-> ${method} ${url}`);
    let response: Response;
    try {
      const timeout = AbortSignal.timeout(settings.timeoutMs);
      response = await fetch(url, { ...init, signal: signal ? AbortSignal.any([signal, timeout]) : timeout });
    } catch (error) {
      signal?.throwIfAborted();
      throw translate(error);
    }
    if (returnsBinary && response.ok) {
      this.#log('debug', `<- ${method} ${response.status} (streamed)`);
      return download(response, signal);
    }
    const text = await response.text().catch((error: unknown) => {
      signal?.throwIfAborted();
      if (!/^(Z_|ERR__ERROR)/.test(causeCode(error))) throw translate(error);
      if (!response.ok) return '';
      throw new DecodeError('The response body could not be decompressed', { status: response.status });
    });
    this.#log('debug', `<- ${method} ${response.status} (${text.length} chars)`);
    if (!response.ok) {
      const clean = redact(settings.credentials, text);
      throw settings.toError({
        status: response.status,
        headers: response.headers,
        text: clean,
        json: parseJson(clean),
      });
    }
    if (text === '') {
      if (returnsJson && response.status !== 204) throw new DecodeError('The response body is empty', { status: response.status });
      return returnsText ? '' : undefined;
    }
    if (!response.headers.get('content-type')?.includes('json')) return text;
    const json = parseJson(text);
    if (json === undefined) throw new DecodeError('The response body is not valid JSON', { status: response.status });
    return json;
  }

  async fetch(operation: Operation, body: unknown, params: Params, { signal }: RequestOptions = {}): Promise<unknown> {
    signal?.throwIfAborted();
    const settings = this.#settings;
    const built = buildRequest(settings, this.#headerDefaults, operation, body, params);
    const encoded = await encode(built.body);
    let refreshed = false;
    for (let tries = 0; ;) {
      const group = settings.credentials.refreshGroup?.(operation) ?? '';
      const generation = this.#generations.get(group) ?? 0;
      const headers = new Headers(built.headers);
      if (encoded.contentType !== undefined) headers.set('Content-Type', encoded.contentType);
      const auth: AuthRequest = { method: operation.method, url: built.url, headers, body: encoded.bytes, operation };
      await settings.credentials.apply(auth);
      signal?.throwIfAborted();
      // A JSON body goes as its text, which encodes to the same bytes.
      const sent = typeof built.body === 'string' ? built.body : built.body && encoded.bytes;
      const init: RequestInit = {
        method: operation.method,
        headers,
        redirect: 'manual',
        body: (encoded.streamed ? built.body : sent) as RequestInit['body'],
        ...(encoded.streamed ? { duplex: 'half' } : {}),
      };
      try {
        return await this.#attempt(operation, built.url, init, signal);
      } catch (error) {
        signal?.throwIfAborted();
        if (!(error instanceof ApiError)) throw error;
        // A stream was consumed by the attempt, so it cannot be sent again.
        if (encoded.streamed) throw error;
        // Never for an operation that sends no credentials, such as a token request made during a refresh.
        if (error.status === 401 && !refreshed && (operation.security?.length ?? 0) > 0) {
          refreshed = true;
          if (await this.#refresh(auth, group, generation)) {
            this.#log('info', 'retrying after refreshing credentials');
            continue;
          }
        }
        const delay = retryDelay(settings, error, operation.method, tries);
        if (delay === undefined) throw error;
        this.#log('info', `retrying after ${delay}ms: ${error.kind}`);
        await sleep(delay, signal);
        tries += 1;
      }
    }
  }
}

export class Resource {
  readonly #transport: Transport;

  constructor(transport: Transport) {
    this.#transport = transport;
  }

  protected async call<T>(operation: Operation, body: unknown, params: Params, options?: RequestOptions): Promise<T> {
    return (await this.#transport.fetch(operation, body, params, options)) as T;
  }

  protected async *paginate<T>(
    operation: Operation,
    body: unknown,
    params: Params,
    options?: RequestOptions,
  ): AsyncGenerator<T, void, undefined> {
    let current: Params | undefined = params;
    while (current !== undefined) {
      const page: unknown = await this.#transport.fetch(operation, body, current, options);
      // An empty 204 is the only success without a body, and it holds no more items.
      if (page === undefined) return;
      const received = items(operation, page) as T[];
      yield* received;
      current = nextParams(operation, current, page, received.length);
    }
  }
}
