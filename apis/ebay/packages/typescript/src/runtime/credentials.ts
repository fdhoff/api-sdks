import type { Operation } from './transport.js';

/** A security scheme an operation names, with the scopes it needs from it. */
export interface Scheme {
  scheme: string;
  scopes: readonly string[];
}

/** Schemes that must all be satisfied. An operation lists alternatives: any one requirement will do. */
export type Requirement = readonly Scheme[];

/** One attempt's request, as it will be sent. `headers` may be changed; the rest is read-only. */
export interface AuthRequest {
  readonly method: string;
  readonly url: string;
  readonly headers: Headers;
  readonly body: Uint8Array;
  readonly operation: Operation;
}

/**
 * Supplies each request's credentials.
 *
 * `apply` runs before every attempt, retries included, so it can sign the final request. `secrets` lists every
 * value to keep out of logs and errors, and is read again each time, so it may change. `refresh` runs after a
 * 401, at most once per call and once at a time per client, and resolves to whether to retry.
 */
export interface Credentials {
  apply(request: AuthRequest): void | Promise<void>;
  secrets(): readonly string[];
  refresh?(request: AuthRequest): boolean | Promise<boolean>;
}

/** The same headers on every request. */
export class StaticCredentials implements Credentials {
  readonly #headers: Record<string, string>;
  readonly #secrets: readonly string[];

  constructor(headers: Record<string, string>, secrets: readonly string[]) {
    this.#headers = { ...headers };
    this.#secrets = [...secrets];
  }

  apply({ headers }: AuthRequest): void {
    for (const [name, value] of Object.entries(this.#headers)) headers.set(name, value);
  }

  secrets(): readonly string[] {
    return this.#secrets;
  }
}

const REDACTED = '***';

/** Longest first, so a secret that contains another is removed whole. */
export function redact(credentials: Credentials, text: string): string {
  const secrets = [...new Set(credentials.secrets())].filter(Boolean).sort((a, b) => b.length - a.length);
  return secrets.reduce((out, secret) => out.replaceAll(secret, REDACTED), text);
}
