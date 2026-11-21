# Hotfix manifests

Every `hotfix/HB-<number>` branch adds or updates `hotfix/manifest.json` at the repository root of the
branch. The file records everything the release desk needs:

| field | meaning |
| --- | --- |
| `ticket` | intake ticket id, e.g. `HB-104` |
| `title` | one line description of the fix |
| `severity` | `Critical`, `High`, `Medium` or `Low` as triaged by support |
| `area` | component the fix touches |
| `reported` | date the ticket was reported, `YYYY-MM-DD` |
| `regression_test` | `true` when the branch adds a regression test |
| `target_series` | the release series the fix was written against |
| `reporter` | who reported the ticket |

Branches that are not named `hotfix/HB-<number>` do not carry a manifest.
