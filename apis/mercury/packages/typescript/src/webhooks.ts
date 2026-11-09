/** Checks that a webhook came from Mercury. Mercury's sandbox sends no webhooks, so this is the way to test a
 * handler. */
export { DEFAULT_WEBHOOK_TOLERANCE_SECONDS, verifyWebhook, WebhookSignatureError } from './runtime/index.js';
export type { VerifyWebhookOptions, WebhookFailure } from './runtime/index.js';

/** The request header that carries a webhook's signature. */
export const SIGNATURE_HEADER = 'Mercury-Signature';
