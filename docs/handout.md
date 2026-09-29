# handout — Big Data Bowl x Muse Code, live (1 hour, virtual)

## the six terminals

| terminal     | dir                    | job                                            |
| ------------ | ---------------------- | ---------------------------------------------- |
| T1 glimmer   | muse-code/glimmer      | wake local box first, needs ~12GB VRAM free    |
| T2 frogger   | ~/code/frogger         | one-shot game dev, single index.html           |
| T3 deploy    | T2 dir                 | scoped sync to /not-frogger/, invalidate, curl |
| T4 squares   | ~/code/sumerian-hosts  | hostReactions.ts, additive only                |
| T5 NFL sweep | nfl-big-data-bowl-2027 | 2024 pass, 2025 pass, lasso baselines          |
| T6 watch     | ~                      | four panes green or red, own the first red     |

prompts: docs/live-demo-prompts.md. fire T1 first, fan T2-T5, T6 floats.

## links

- game: https://clouddelnorte.org/not-frogger/
- squares: https://bryanchasko.com/sumerian-squares/
- repos: chasko-labs/nfl-big-data-bowl-2027, sumerian-hosts, muse-code-pro (private)

## if a demo dies

- glimmer dark: Spark runs it, read the recorded numbers.
- SSO expired: stop, aws login, retry once.
- sweep dies: same scripts on samples/2024 plus samples/2025.
- 404 on the game url: expected until first deploy.
- VRAM held: coordinate owners pre-show, Spark covers.

backup slides 18-22 carry each of these.
