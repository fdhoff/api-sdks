#!/usr/bin/env bash
# Starts a disposable Gitea container from the pinned image, checks its version against the pinned spec, creates a
# synthetic admin, a plain user and an admin access token, and writes them to the settings file run.mjs reads.
# Everything is made for this container only. Nothing is read from or sent to any other instance.
set -euo pipefail

out="${1:?usage: bootstrap.sh <settings-file>}"
here="$(cd "$(dirname "$0")" && pwd)"
container="${GITEA_LIVE_CONTAINER:-gitea-live}"
port="${GITEA_LIVE_PORT:-3000}"
root="http://127.0.0.1:${port}"

field() { node -e 'const v = JSON.parse(require("fs").readFileSync(0, "utf8")); console.log(v[process.argv[1]] ?? "")' "$1"; }
mask() { if [ -n "${GITHUB_ACTIONS:-}" ]; then echo "::add-mask::$1"; fi; }

image="$(field image < "$here/image.json")"
tag="$(field tag < "$here/image.json")"
digest="$(field digest < "$here/image.json")"
pinned="$(field tag < "$here/../../spec/upstream/lock.json")"
if [ "v$tag" != "$pinned" ]; then
  echo "image.json names Gitea $tag, but the spec is pinned at $pinned" >&2
  exit 1
fi

docker run --detach --name "$container" --publish "127.0.0.1:${port}:3000" \
  --env GITEA__database__DB_TYPE=sqlite3 \
  --env GITEA__security__INSTALL_LOCK=true \
  --env GITEA__server__ROOT_URL=http://localhost:3000/ \
  --env GITEA__server__DISABLE_SSH=true \
  --env GITEA__service__DISABLE_REGISTRATION=true \
  "$image:$tag@$digest" > /dev/null

version_json=""
for _ in $(seq 1 90); do
  if version_json="$(curl --fail --silent "$root/api/v1/version")"; then break; fi
  sleep 2
done
if [ -z "$version_json" ]; then
  echo "Gitea did not answer /api/v1/version" >&2
  exit 1
fi
version="$(field version <<< "$version_json")"
if [ "$version" != "$tag" ]; then
  echo "The container runs Gitea $version, but the pinned tag is $tag" >&2
  exit 1
fi

admin=live-admin
user=live-user
admin_password="$(openssl rand -hex 16)"
user_password="$(openssl rand -hex 16)"
mask "$admin_password"
mask "$user_password"

create_user() {
  docker exec --user git "$container" gitea admin user create "${@:3}" \
    --username "$1" --password "$2" --email "$1@example.com" --must-change-password=false > /dev/null
}
create_user "$admin" "$admin_password" --admin
create_user "$user" "$user_password"

token_json="$(curl --fail --silent --show-error --user "$admin:$admin_password" \
  --header 'Content-Type: application/json' --data '{"name":"live-conformance","scopes":["all"]}' \
  "$root/api/v1/users/$admin/tokens")"
token="$(field sha1 <<< "$token_json")"
mask "$token"
if [ -z "$token" ]; then
  echo "Gitea returned no access token" >&2
  exit 1
fi

umask 077
printf '{"base_url":"%s","admin":"%s","admin_password":"%s","user":"%s","user_password":"%s","token":"%s"}\n' \
  "$root" "$admin" "$admin_password" "$user" "$user_password" "$token" > "$out"
echo "Gitea $version is up at $root"
