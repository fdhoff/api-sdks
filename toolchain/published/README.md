# Published package check

In-repository tests build each package from source. This checks what a user actually installs: missing files, wrong entry points, broken type declarations and native dependency problems show up only in the package a registry serves.

`.github/workflows/published.yml` runs it for each package as follows:

1. Starts the Prism mock from the API's built spec. The checkout serves only the mock.
2. Creates an empty project in a temporary directory outside the checkout, with fresh package caches.
3. Installs the package at the given version from its public registry: PyPI, npm, the Go module proxy, NuGet or crates.io. A registry can take minutes to serve a version it has just accepted, so for a version just released or named by hand the install retries for up to 15 minutes. `SMOKE_WAIT_SECONDS` sets the wait, which is otherwise none.
4. Checks the version the package manager installed, then runs the package's smoke program, `apis/<api>/packages/<language>/published/`, as it was at the version's release tag, so a later API change cannot break the check of an older version. A manual run with `current_program` uses the checkout's program instead, to confirm a fix to one that no longer builds. The program checks the version the package reports where it reports one, and makes one call against the mock with synthetic credentials.

| Language | Also checks |
| --- | --- |
| Python | `mypy --strict` against the installed package's type hints |
| TypeScript | `tsc` against the package's declarations, with `skipLibCheck` off, and that `require` loads it |
| Go | `go vet` |
| C# | Runs on each of .NET 10 and .NET 8 that the package targets |
| Rust | Builds against the published crate's dependencies as resolved today |

Each release workflow calls the workflow after its publish job, for the version it published. Go has no release workflow, so a Go module tag runs it. A weekly run, a manual run and a pull request that changes this check smoke the latest published version of every package; a package with no published version is skipped with a notice.

A version released before its package had a smoke program is checked with the current one, which may be written for a newer API, so its failure is a warning only. Every other failure, except on a pull request, opens an issue named after the package, version and language, with the end of the log, or comments on that issue if it is still open. Published versions are left as they are: nothing is yanked or unlisted.

No live credentials are used. A new package needs its own smoke program before its first release; `published.test.mjs` fails without one.

```sh
node toolchain/published/targets.mjs [--api <api>] [--language <language>] [--version <version>]
SMOKE_BASE_URL=http://127.0.0.1:4010 bash toolchain/published/smoke.sh <language> <package> <version> apis/<api>/packages/<language>/published
```
