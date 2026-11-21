# harbor-cli

Command line client for the Harbor platform.

- `src/harbor_cli.py` - CLI entry point
- `hotfix/` - one manifest per hotfix branch (see `hotfix/README.md`)

Releases are cut from `main`; hotfixes are prepared on `hotfix/HB-<number>` branches and carry their
own manifest so the release desk can read the queue without merging anything.
