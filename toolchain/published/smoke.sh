#!/usr/bin/env bash
# Installs one published package from its public registry into an empty project outside the repository, as a user
# would, checks the version it reports, and runs the package's smoke program against the mock at SMOKE_BASE_URL.
# Usage: smoke.sh <language> <package> <version> <program-dir>. See README.md.
set -euo pipefail

if [ "$#" -ne 4 ]; then
  echo "Usage: smoke.sh <language> <package> <version> <program-dir>" >&2
  exit 2
fi
language=$1
package=$2
version=$3
program=$(cd "$4" && pwd)
templates=$(cd "$(dirname "$0")" && pwd)
: "${SMOKE_BASE_URL:?SMOKE_BASE_URL must name the mock}"
wait_seconds=${SMOKE_WAIT_SECONDS:-0}
export SMOKE_VERSION=$version

work=$(mktemp -d)
cd "$work"
echo "Smoke testing $package $version ($language) in $work"

# A registry can take minutes to serve a version it has just accepted, so the install retries until the deadline.
retry() {
  local deadline=$((SECONDS + wait_seconds))
  until "$@"; do
    if [ "$SECONDS" -ge "$deadline" ]; then
      echo "Could not install $package $version within ${wait_seconds}s." >&2
      return 1
    fi
    echo "Not installable yet; retrying in 30s." >&2
    sleep 30
  done
}

reported() {
  if [ "$1" != "$version" ]; then
    echo "The installed package reports version '$1', not $version." >&2
    exit 1
  fi
  echo "Installed $package $1."
}

case "$language" in
  python)
    python -m venv .venv
    install() { .venv/bin/python -m pip install --no-cache-dir --disable-pip-version-check --quiet "$package==$version"; }
    retry install
    reported "$(.venv/bin/python -m pip show "$package" | sed -n 's/^Version: //p')"
    .venv/bin/python -m pip install --disable-pip-version-check --quiet mypy==2.4.1
    cp "$program/smoke.py" .
    .venv/bin/python -m mypy --strict --no-incremental smoke.py
    .venv/bin/python -I smoke.py
    ;;
  typescript)
    echo '{ "private": true }' > package.json
    install() { npm install --no-audit --no-fund --prefer-online --cache "$work/.npm" "$package@$version"; }
    retry install
    reported "$(jq -r .version "node_modules/$package/package.json")"
    npm install --no-audit --no-fund --cache "$work/.npm" typescript@7.0.2 @types/node@22.20.5
    cp "$program/smoke.mts" "$templates/typescript/tsconfig.json" .
    npx tsc -p tsconfig.json
    node smoke.mts
    node -e 'if (Object.keys(require(process.argv[1])).length === 0) process.exit(1)' "$package"
    echo "Loaded $package with require."
    ;;
  go)
    export GOWORK=off GOFLAGS=-modcacherw GOMODCACHE="$work/.gomod"
    cp "$program/main.go" .
    go mod init smoke
    install() { go get "$package@v$version"; }
    retry install
    reported "$(go list -m -f '{{.Version}}' "$package" | sed 's/^v//')"
    go vet .
    go build -o smoke .
    ./smoke
    ;;
  csharp)
    export DOTNET_CLI_TELEMETRY_OPTOUT=1 DOTNET_NOLOGO=1 NUGET_PACKAGES="$work/.nuget"
    cp "$program/Program.cs" .
    id=$(echo "$package" | tr '[:upper:]' '[:lower:]')
    nuspec="https://api.nuget.org/v3-flatcontainer/$id/$(echo "$version" | tr '[:upper:]' '[:lower:]')/$id.nuspec"
    # Runs on each .NET installed here that the package targets, as its nuspec's dependency groups list them.
    install() {
      frameworks=$(curl -fsS "$nuspec" | grep -o 'targetFramework="net\(8\|10\)\.0"' | cut -d'"' -f2 | sort -u | paste -sd';' -) || return 1
      sed -e "s/{{package}}/$package/" -e "s/{{version}}/$version/" -e "s/{{frameworks}}/$frameworks/" \
        "$templates/csharp/Smoke.csproj" > Smoke.csproj
      dotnet restore --no-http-cache
    }
    retry install
    reported "$(jq -r --arg id "$package" '.libraries | keys[] | select(ascii_downcase | startswith(($id | ascii_downcase) + "/")) | split("/")[1]' obj/project.assets.json)"
    for framework in ${frameworks//;/ }; do
      dotnet run --no-restore --framework "$framework"
    done
    ;;
  rust)
    export CARGO_TERM_COLOR=never
    cargo init --name smoke --vcs none --quiet
    cp "$program/main.rs" src/main.rs
    install() { cargo add --quiet "$package@=$version" && cargo add --quiet tokio@1 --features macros,rt; }
    retry install
    reported "$(cargo metadata --format-version 1 | jq -r --arg name "$package" '.packages[] | select(.name == $name) | .version')"
    cargo run --quiet
    ;;
  *)
    echo "Unknown language $language" >&2
    exit 2
    ;;
esac
echo "$package $version ($language) passed."
