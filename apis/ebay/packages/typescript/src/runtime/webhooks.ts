export const DEFAULT_WEBHOOK_TOLERANCE_SECONDS = 300;

export type WebhookFailure = 'malformed-header' | 'too-old' | 'bad-signature';

export interface VerifyWebhookOptions {
  /** The oldest timestamp to accept, in seconds. */
  toleranceSeconds?: number;
  /** Milliseconds since the epoch. */
  now?: number;
}

const TIMESTAMP = /^[0-9]{1,12}$/;
const SIGNATURE = /^[0-9a-fA-F]{64}$/;
const MESSAGES: Record<WebhookFailure, string> = {
  'malformed-header': 'The webhook signature header is malformed',
  'too-old': 'The webhook timestamp is older than the tolerance',
  'bad-signature': 'No webhook signature matches the body',
};

/** A webhook failed verification. `reason` says why; the message never holds the secret or the body. */
export class WebhookSignatureError extends Error {
  readonly reason: WebhookFailure;

  constructor(reason: WebhookFailure) {
    super(MESSAGES[reason]);
    this.name = new.target.name;
    this.reason = reason;
  }
}

function parse(header: string | null | undefined): [string, string[]] {
  if (header == null) throw new WebhookSignatureError('malformed-header');
  let timestamp: string | undefined;
  const signatures: string[] = [];
  for (const entry of header.split(',')) {
    const trimmed = entry.replace(/^[ \t]+|[ \t]+$/g, '');
    const equals = trimmed.indexOf('=');
    if (equals < 0) throw new WebhookSignatureError('malformed-header');
    const key = trimmed.slice(0, equals);
    const value = trimmed.slice(equals + 1);
    if (key === 't') {
      if (timestamp !== undefined || !TIMESTAMP.test(value)) throw new WebhookSignatureError('malformed-header');
      timestamp = value;
    } else if (key === 'v1') {
      signatures.push(value);
    }
  }
  if (timestamp === undefined || signatures.length === 0) throw new WebhookSignatureError('malformed-header');
  return [timestamp, signatures];
}

const encode = (value: string | Uint8Array): Uint8Array<ArrayBuffer> =>
  typeof value === 'string' ? new TextEncoder().encode(value) : new Uint8Array(value);

/**
 * Checks a webhook's timestamped HMAC-SHA256 signature header, `t=<unix seconds>,v1=<hex>` signed over
 * `<t>.<raw body>`, against the raw body as received, never re-serialised. A string payload is encoded as UTF-8. Any
 * one matching `v1` value is enough, so a header may carry several while a secret rotates. Rejects with a
 * {@link WebhookSignatureError}.
 */
export async function verifyWebhook(
  payload: Uint8Array | string,
  header: string | null | undefined,
  secret: string | Uint8Array,
  options: VerifyWebhookOptions = {},
): Promise<void> {
  const tolerance = options.toleranceSeconds ?? DEFAULT_WEBHOOK_TOLERANCE_SECONDS;
  if (!(tolerance > 0)) throw new RangeError('The webhook tolerance must be positive');
  const [timestamp, signatures] = parse(header);
  const key = await crypto.subtle.importKey('raw', encode(secret), { name: 'HMAC', hash: 'SHA-256' }, false, [
    'verify',
  ]);
  const body = encode(payload);
  const prefix = new TextEncoder().encode(`${timestamp}.`);
  const message = new Uint8Array(prefix.length + body.length);
  message.set(prefix);
  message.set(body, prefix.length);
  let matched = false;
  for (const signature of signatures) {
    if (!SIGNATURE.test(signature)) continue;
    const bytes = Uint8Array.from(signature.match(/../g) ?? [], (pair) => parseInt(pair, 16));
    if (await crypto.subtle.verify('HMAC', key, bytes, message)) matched = true;
  }
  if (!matched) throw new WebhookSignatureError('bad-signature');
  if ((options.now ?? Date.now()) / 1000 - Number(timestamp) > tolerance) throw new WebhookSignatureError('too-old');
}
