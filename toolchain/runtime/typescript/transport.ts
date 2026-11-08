import { ApiConnectionError, ApiError, ApiTimeoutError, DecodeError, type ErrorContext } from './errors.js';

export type FileContent = Blob | Uint8Array;

/** A file to upload: its content, or its name and content. */
export type FileInput = FileContent | { filename: string; content: FileContent };

export interface Param {
  wire: string;
  name: string;
  location: 'path' | 'query' | 'form';
}

export interface Operation {
  id: string;
  method: string;
  path: string;
  resource: string;
  name: string;
  params: readonly Param[];
  hasBody?: boolean;
  returnsJson?: boolean;
  iterator?: string;
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
  baseUrl: string;
  secret: string;
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
  init: RequestInit;
}

const REDACTED = '***';
const PAGE_MARKERS = ['page', 'cursor'];
const HTTP_DATE = /^[A-Z][a-z]{2}, \d{2} [A-Z][a-z]{2} \d{4} \d{2}:\d{2}:\d{2} GMT$/;
const MAX_TIMER_MS = 2 ** 31 - 1;

const isObject = (value: unknown): value is Record<string, unknown> => typeof value === 'object' && value !== null;
const isContent = (value: unknown): value is FileContent => value instanceof Blob || value instanceof Uint8Array;

function appendFile(form: FormData, wire: string, content: FileContent, filename: string): void {
  form.append(wire, content instanceof Blob ? content : new Blob([content as Uint8Array<ArrayBuffer>]), filename);
}

function appendPart(form: FormData, wire: string, value: unknown): void {
  if (Array.isArray(value)) value.forEach((item) => appendPart(form, wire, item));
  else if (value instanceof File) appendFile(form, wire, value, value.name);
  else if (isContent(value)) appendFile(form, wire, value, wire);
  else if (isObject(value) && isContent(value['content']) && typeof value['filename'] === 'string') {
    appendFile(form, wire, value['content'], value['filename']);
  } else form.append(wire, isObject(value) ? JSON.stringify(value) : String(value));
}

function buildRequest(settings: Settings, operation: Operation, body: unknown, params: Params): Built {
  let path = operation.path;
  const query = new URLSearchParams();
  const form = new FormData();
  let hasParts = false;
  for (const { wire, name, location } of operation.params) {
    const value = params[name];
    if (value === undefined || value === null) {
      if (location === 'path') throw new TypeError(`${name} is required`);
      continue;
    }
    if (location === 'path') {
      path = path.replace(`{${wire}}`, encodeURIComponent(String(value)));
    } else if (location === 'query') {
      for (const item of Array.isArray(value) ? value : [value]) query.append(wire, String(item));
    } else {
      appendPart(form, wire, value);
      hasParts = true;
    }
  }
  const search = query.size > 0 ? `?${query}` : '';
  // fetch accepts a gzip body cut short, so ask for none.
  const headers: Record<string, string> = { 'Accept-Encoding': 'identity', ...settings.headers };
  const init: RequestInit = { method: operation.method, headers, redirect: 'manual' };
  if (hasParts) {
    init.body = form;
  } else if (body !== undefined) {
    init.body = JSON.stringify(body);
    headers['Content-Type'] = 'application/json';
  }
  return { url: `${settings.baseUrl}${path}${search}`, init };
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
  const failed =
    error instanceof ApiTimeoutError || error instanceof ApiConnectionError || (error.status ?? 0) >= 500;
  return method === 'GET' && failed ? settings.retryBaseDelayMs * 2 ** tries : undefined;
}

/** Read the position out of `next` and apply it to our own request. `next` is never fetched:
 * it could send the credential to another host. */
function nextParams(operation: Operation, params: Params, page: unknown): Params | undefined {
  if (!isObject(page)) throw new DecodeError('A page is not a JSON object');
  const link = page['next'];
  if (!link) return undefined;
  let position: URLSearchParams;
  try {
    position = new URL(String(link), 'http://next.invalid').searchParams;
  } catch {
    throw new DecodeError('The `next` link is not a valid URL');
  }
  const names = operation.params.filter(({ location }) => location === 'query');
  const updated = { ...params };
  for (const { wire, name } of names) {
    const value = position.get(wire);
    if (PAGE_MARKERS.includes(wire) && value) updated[name] = value;
  }
  if (names.every(({ name }) => String(updated[name]) === String(params[name]))) {
    throw new DecodeError('The `next` link does not advance the iteration');
  }
  return updated;
}

function items(page: unknown): unknown[] {
  const results = isObject(page) ? page['results'] : undefined;
  return Array.isArray(results) ? results : [];
}

export class Transport {
  readonly #settings: Settings;

  constructor(settings: Settings) {
    this.#settings = settings;
  }

  #log(level: keyof Logger, message: string): void {
    this.#settings.logger?.[level](message.replaceAll(this.#settings.secret, REDACTED));
  }

  async #attempt({ method, returnsJson }: Operation, { url, init }: Built, signal: AbortSignal | undefined): Promise<unknown> {
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
    const text = await response.text().catch((error: unknown) => {
      signal?.throwIfAborted();
      if (!/^(Z_|ERR__ERROR)/.test(causeCode(error))) throw translate(error);
      if (!response.ok) return '';
      throw new DecodeError('The response body could not be decompressed', { status: response.status });
    });
    this.#log('debug', `<- ${method} ${response.status} (${text.length} chars)`);
    if (!response.ok) {
      const clean = text.replaceAll(settings.secret, REDACTED);
      throw settings.toError({
        status: response.status,
        headers: response.headers,
        text: clean,
        json: parseJson(clean),
      });
    }
    // TODO: an empty body where the spec declares text should read as '', as it does in the other languages.
    if (text === '') {
      if (returnsJson) throw new DecodeError('The response body is empty', { status: response.status });
      return undefined;
    }
    if (!response.headers.get('content-type')?.includes('json')) return text;
    const json = parseJson(text);
    if (json === undefined) throw new DecodeError('The response body is not valid JSON', { status: response.status });
    return json;
  }

  async fetch(operation: Operation, body: unknown, params: Params, { signal }: RequestOptions = {}): Promise<unknown> {
    const built = buildRequest(this.#settings, operation, body, params);
    for (let tries = 0; ; tries += 1) {
      try {
        return await this.#attempt(operation, built, signal);
      } catch (error) {
        if (!(error instanceof ApiError) || signal?.aborted) throw error;
        const delay = retryDelay(this.#settings, error, operation.method, tries);
        if (delay === undefined) throw error;
        this.#log('info', `retrying after ${delay}ms: ${error.kind}`);
        await sleep(delay, signal);
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
      yield* items(page) as T[];
      current = nextParams(operation, current, page);
    }
  }
}
