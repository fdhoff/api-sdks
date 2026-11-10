// Prints the registry URL the API reference names, as a `url=` line, for the spec drift job to pin. Uses only
// Node's own modules.
import { currentRegistryUrl } from './check-upstream.mjs';

console.log(`url=${await currentRegistryUrl()}`);
