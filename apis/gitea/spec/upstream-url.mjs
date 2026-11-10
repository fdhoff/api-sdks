// Prints the spec URL and tag of Gitea's newest stable release, as `url=` and `tag=` lines, for the spec drift
// job to pin. Uses only Node's own modules and git.
import { newestRelease } from './check-upstream.mjs';

const { url, tag } = await newestRelease();
console.log(`url=${url}\ntag=${tag}`);
