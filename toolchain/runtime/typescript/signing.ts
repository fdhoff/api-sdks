import type { AuthRequest } from './credentials.js';

export const ED25519 = 'ed25519';
export const RSA_V1_5_SHA256 = 'rsa-v1_5-sha256';
export type SignatureAlgorithm = typeof ED25519 | typeof RSA_V1_5_SHA256;

export interface MessageSignerOptions {
  /** An unencrypted PKCS #8 PEM Ed25519 or RSA private key. It is a secret. */
  privateKey: string;
  /** Lowercase field names, and `@method`, `@target-uri`, `@authority`, `@scheme`, `@request-target`, `@path` and `@query`. */
  components: readonly string[];
  label?: string;
  keyId?: string;
  includeAlg?: boolean;
  /** Adds `expires`, this many seconds after `created`. */
  lifetimeSeconds?: number;
  /** Milliseconds since the epoch. */
  now?: () => number;
}

type Key = Awaited<ReturnType<typeof crypto.subtle.importKey>>;
type Params = Parameters<typeof crypto.subtle.sign>[0];

const DERIVED = new Set(['@method', '@target-uri', '@authority', '@scheme', '@request-target', '@path', '@query']);
const FIELD = /^[a-z0-9!#$%&'*+.^_`|~-]+$/;
const LABEL = /^[a-z*][a-z0-9_.*-]*$/;
const ALGORITHMS: readonly [SignatureAlgorithm, Params][] = [
  [ED25519, { name: 'Ed25519' }],
  [RSA_V1_5_SHA256, { name: 'RSASSA-PKCS1-v1_5', hash: 'SHA-256' }],
];

const toBase64 = (bytes: Uint8Array): string => btoa(Array.from(bytes, (byte) => String.fromCharCode(byte)).join(''));

/** The `Content-Digest` value for these exact bytes. */
export async function contentDigest(body: Uint8Array): Promise<string> {
  const hash = await crypto.subtle.digest('SHA-256', new Uint8Array(body));
  return `sha-256=:${toBase64(new Uint8Array(hash))}:`;
}

function quote(value: string): string {
  if (!/^[\x20-\x7e]*$/.test(value)) throw new TypeError('A signature parameter must be printable ASCII');
  return `"${value.replace(/[\\"]/g, '\\$&')}"`;
}

async function importKey(pem: string): Promise<[SignatureAlgorithm, Params, Key]> {
  const lines = pem.trim().split(/\r?\n/);
  if (lines[0] !== '-----BEGIN PRIVATE KEY-----' || lines.at(-1) !== '-----END PRIVATE KEY-----') {
    throw new TypeError('The signing key must be an unencrypted PKCS #8 PEM private key');
  }
  let der: Uint8Array<ArrayBuffer>;
  try {
    der = Uint8Array.from(atob(lines.slice(1, -1).join('')), (char) => char.charCodeAt(0));
  } catch {
    throw new TypeError('The signing key is not a valid private key');
  }
  for (const [algorithm, params] of ALGORITHMS) {
    try {
      return [algorithm, params, await crypto.subtle.importKey('pkcs8', der, params, false, ['sign'])];
    } catch {
      // Not this kind of key.
    }
  }
  throw new TypeError('The signing key must be Ed25519 or RSA');
}

/**
 * Signs each attempt's request: a `Content-Digest` of the body when there is one, then `Signature-Input` and
 * `Signature` over the covered components, with a fresh `created` time. `content-digest` is left out of a request
 * with no body, and any other field the request lacks is an error.
 */
export class MessageSigner {
  readonly algorithm: SignatureAlgorithm;
  readonly #key: Key;
  readonly #params: Params;
  readonly #secrets: readonly string[];
  readonly #components: readonly string[];
  readonly #label: string;
  readonly #extra: string;
  readonly #lifetime: number | undefined;
  readonly #now: () => number;

  private constructor(options: MessageSignerOptions, [algorithm, params, key]: Awaited<ReturnType<typeof importKey>>) {
    const { privateKey, keyId, includeAlg = false } = options;
    this.algorithm = algorithm;
    this.#params = params;
    this.#key = key;
    this.#secrets = [privateKey.trim(), privateKey.trim().split(/\r?\n/).slice(1, -1).join('')];
    this.#components = [...options.components];
    this.#label = options.label ?? 'sig1';
    this.#extra = (keyId === undefined ? '' : `;keyid=${quote(keyId)}`) + (includeAlg ? `;alg="${algorithm}"` : '');
    this.#lifetime = options.lifetimeSeconds;
    this.#now = options.now ?? Date.now;
  }

  static async create(options: MessageSignerOptions): Promise<MessageSigner> {
    for (const component of options.components) {
      if (component.startsWith('@') ? !DERIVED.has(component) : !FIELD.test(component)) {
        throw new TypeError(`Unsupported covered component ${component}`);
      }
    }
    if (!LABEL.test(options.label ?? 'sig1')) throw new TypeError('The signature label must be a lowercase key');
    return new MessageSigner(options, await importKey(options.privateKey));
  }

  /** The private key as given and as its PEM body, to redact. */
  secrets(): readonly string[] {
    return this.#secrets;
  }

  async sign(request: AuthRequest): Promise<void> {
    const { headers } = request;
    if (request.body.length > 0) headers.set('content-digest', await contentDigest(request.body));
    const components = this.#components.filter((name) => name !== 'content-digest' || headers.has(name));
    const created = Math.floor(this.#now() / 1000);
    let params = `(${components.map((name) => `"${name}"`).join(' ')});created=${created}${this.#extra}`;
    if (this.#lifetime !== undefined) params += `;expires=${created + this.#lifetime}`;
    const base = [...components.map((name) => `"${name}": ${value(request, name)}`), `"@signature-params": ${params}`];
    const signature = await crypto.subtle.sign(this.#params, this.#key, new TextEncoder().encode(base.join('\n')));
    headers.set('signature-input', `${this.#label}=${params}`);
    headers.set('signature', `${this.#label}=:${toBase64(new Uint8Array(signature))}:`);
  }
}

function value(request: AuthRequest, name: string): string {
  if (!name.startsWith('@')) {
    const field = request.headers.get(name);
    if (field === null) throw new TypeError(`The request has no ${name} field to sign`);
    return field.trim();
  }
  const url = new URL(request.url);
  const derived: Record<string, string> = {
    '@method': request.method.toUpperCase(),
    '@target-uri': url.href,
    '@authority': url.host,
    '@scheme': url.protocol.slice(0, -1),
    '@request-target': url.pathname + url.search,
    '@path': url.pathname,
    '@query': url.search || '?',
  };
  return derived[name] as string;
}
