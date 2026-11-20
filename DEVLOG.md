# DEVLOG — gta6-meme-x-01

Bounty: Post a GTA 6 meme on X · $500 / top 50 · deadline 2026-11-23 14:00 UTC
(22:00 CST) · entrant @yanxiaoxv · session started 2026-11-20 (after the
2026-11-19 14:00 UTC opening, so all timestamps are in-window).

## How the memes were made (authorship)

1. Base scenes generated in this session with the platform image tool —
   original parody illustration, no GTA artwork, no text baked in
   (`memes/raw/raw-{a,b,c}-*.png`).
2. `memes/build_memes.py` (written in this session, Python/PIL) typesets
   every caption in code (exact spelling, heavy stroke, sized to stay
   readable at the judge's 480px view) and draws the make.fun ghost from
   scratch as vector shapes: white ghost, thick black outline, two black
   four-point sparkle eyes, one round little hand, magenta coin with a
   white star. In every candidate the ghost is a *character in the joke*,
   not a corner sticker.
3. Two build rounds: v1 hid candidate B's wallet under the ghost and let
   candidate A's ghost cover its caption; both placements were fixed and
   re-verified by eye, plus a 480×480 shrink check on all three.

## The three candidates

### A — `memes/candidate-a-pto.png` — "47 sick days"
- Joke: I submit 47 sick days for GTA 6 launch week; my boss approves —
  he's calling in dead too. The ghost floats outside the office window,
  already in Leonida.
- Why it travels: launch-week sick lies are the most-shared GTA 6 ritual;
  every employed fan tags a coworker. Boss-twist beats the house HR-memo
  anchor on surprise.
- Weak spot: no make.fun *name* in the picture (ghost only), so the
  sell-make.fun criterion leans on the post text.

### B — `memes/candidate-b-wallet.png` — "My wallet"
- Joke: GTA 6 wants $80 + 150 GB; the wallet is empty (moths included);
  my AI agent on make.fun answers: "Relax. I win money while you wait."
- Why it travels: price + download-size pain is universal launch-week
  discourse, and the pitch *is* the punchline — the agent pays for the
  game the wallet can't.
- Weak spot: the busiest caption of the three (5 lines); empty-wallet is
  a known trope even if this combination is new.

### C — `memes/candidate-c-duo.png` — "Partner in crime" ⭐ chosen final
- Joke: Rockstar gave Jason a partner, Lucia. make.fun gave me one too —
  the ghost, leaning on the pink convertible in Leonida — and mine pays me.
- Why it travels: Jason & Lucia's duo is *the* GTA 6 fact; the parallel
  is understood in one second, the visual is pure Vice City (pink car,
  palms, art-deco Leonida), and "MINE PAYS ME" is a quotable four-word
  pitch that fits in a quote-post.
- Strengths vs the judge's order: (1) ghost is the co-protagonist, huge
  and unmissable at 480px, plus the make.fun name in the picture;
  (2) one-second joke; (3) specifically GTA 6 (Jason/Lucia, Leonida);
  (4) pitch inside the joke, not an ad line; (5) shortest caption of the
  three; (6) no house anchor or known meme uses the duo framing;
  (7) cleanest composition.

## Self-ranking (by the judge's seven criteria, in order)

1. **C — duo** — wins criteria 1, 5, 6, 7 outright; ties or wins 2–4.
2. **B — wallet** — strongest explicit pitch in-picture; loses to C on
   readability and originality.
3. **A — PTO** — funniest *workplace* angle and a safe top-50 style entry,
   but weakest in-picture branding of the three.

Chosen final: **C**, copied to `memes/final-meme.png` (byte-identical to
`candidate-c-duo.png`). A and B stay in the repo as candidates; if the user
prefers another, only the X post's picture changes — nothing else in the
entry depends on the choice.

## X post text draft (for the chosen final, main session to post)

> Rockstar gave Jason a partner in crime: Lucia.
> make.fun gave me one too — and mine pays me. 💸
>
> My AI agent enters bounties and wins real money on @makefunai while I
> wait for Leonida. This meme is its entry. Put yours to work:
> https://make.fun/bounty/gta6-meme-x-01
> <PLAYCODE — main session fills from the account's play-code endpoint>

Carries: make.fun link ✓, @makefunai tag ✓, earn-money pitch in the
meme's own voice ✓, play code (pending) ✓. Short enough for the judge's
~1,100-byte text window ✓.

## Verification done

- `node main.ts` with `MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out`:
  `out/POST.json` byte-identical to `./POST.json` (placeholder URL until
  the post is live — main session backfills, then re-runs).
- All three candidates eyeballed at full size and at 480×480: captions
  legible, ghost recognisable, nothing important cut off.
- No X posting, no login, no GitHub, no submit — frozen for main-session
  review, per dispatch.
