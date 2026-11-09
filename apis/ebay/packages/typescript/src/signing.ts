// Signatures for the calls eBay requires EU- and UK-domiciled sellers to sign.
import { MessageSigner } from './runtime/index.js';

export const COMPONENTS = ['content-digest', 'x-ebay-signature-key', '@method', '@path', '@authority'] as const;
const PEM_HEADER = '-----BEGIN PRIVATE KEY-----';

export interface SigningKeyOptions {
  /** The private key, as `createSigningKey` returns it or as a PKCS #8 PEM. It is a secret. */
  privateKey: string;
  /** The key's `jwe`, sent as `x-ebay-signature-key`. */
  jwe: string;
}

/** eBay returns the base64 body of the key without the PEM lines around it. */
function pem(privateKey: string): string {
  const key = privateKey.trim();
  if (key.startsWith(PEM_HEADER)) return key;
  const body = key.replace(/\s+/g, '');
  const lines = body.match(/.{1,64}/g) ?? [];
  return [PEM_HEADER, ...lines, '-----END PRIVATE KEY-----'].join('\n');
}

/**
 * A key pair from the Key Management API's `createSigningKey`. eBay returns the private key only once. Ed25519 and
 * RSA keys both work. Create one with `await SigningKey.create(...)`, which checks the key.
 */
export class SigningKey {
  readonly jwe: string;
  readonly signer: MessageSigner;

  private constructor(jwe: string, signer: MessageSigner) {
    this.jwe = jwe;
    this.signer = signer;
  }

  static async create({ privateKey, jwe }: SigningKeyOptions): Promise<SigningKey> {
    if (!jwe) throw new TypeError('jwe is required');
    return new SigningKey(jwe, await MessageSigner.create({ privateKey: pem(privateKey), components: COMPONENTS }));
  }

  /** The private key in each form to keep out of logs and errors. */
  secrets(): readonly string[] {
    return this.signer.secrets();
  }
}
