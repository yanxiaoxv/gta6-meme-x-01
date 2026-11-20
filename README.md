# gta6-meme-x-01

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/yanxiaoxv/gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/yanxiaoxv/gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

One original GTA 6 meme, made by an AI agent and posted on X from a public account: Rockstar gave Jason a partner in crime — make.fun gave me one that pays me.

## Run it

```sh
node main.ts
```

Entry for make.fun bounty `gta6-meme-x-01` ($500, top 50 paid, deadline
2026-11-23 14:00 UTC / 22:00 CST), entrant @yanxiaoxv.

## What this is

One original GTA 6 meme, made in-session by the agent, to be posted on X
from a public account. The post itself is the entry:

- First picture = the meme (see `memes/` — the chosen final plus candidates).
- Post text carries `make.fun` / `@makefunai` and the entrant's play code,
  and tells readers, in the meme's own voice, that people and their AI
  agents earn real money in make.fun bounties.
- The picture works make.fun into the scene: its ghost mascot (white ghost,
  thick black outline, sparkle eyes, holding a magenta coin with a white
  star) as a character in the joke — never a corner sticker.

The AI judge compares posts pairwise. Ranking order: (1) make.fun visible
in the picture, (2) funny in one second to a GTA fan, (3) specifically
about GTA 6 (13-year wait, delays, launch-week sick days, price, download
size, Leonida / Vice City, Jason & Lucia), (4) sells make.fun, (5) short
and readable, (6) original, (7) clean image.

## Files

- `main.ts` — Node 22, standard library only. Copies `POST.json` to
  `/output/POST.json`. That is all it has to do; the house reads the post
  from X itself and builds the dossier.
- `POST.json` — `{"url": "https://x.com/<handle>/status/<id>"}`.
  Placeholder until the post is live; the main session backfills the real
  URL after the user approves and the post goes out. **Do not submit with
  the placeholder.**
- `memes/` — candidate memes + the chosen final, with the build script
  that assembled them (`build_memes.py`) so the making is reproducible.
- `DEVLOG.md` — the jokes, why each should travel, and the self-ranking.
- `.makefun/owner.json` — wallet claim file for this entrant.
- `LICENSE` — MIT.

## Run locally

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
# out/POST.json is then byte-for-byte ./POST.json
```

## Status

Build side only. Publishing to X and submitting are frozen until the main
session shows the memes to the user and gets a nod.

---

<sub>Entered on [make.fun](https://make.fun/?ref=5g2h0w0s&utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>
