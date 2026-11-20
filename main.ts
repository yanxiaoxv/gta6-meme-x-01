// gta6-meme-x-01 entry program (Node 22, standard library only).
//
// What this program does, and why it is so small:
//   The entry for this bounty is not a file this program creates.
//   The entry is a public post on X: its first picture is the GTA 6
//   meme built in this repository, and its text carries make.fun /
//   @makefunai plus the entrant's play code. The house reads that
//   post back from X itself, builds the judge's dossier from it,
//   and drops the dossier into /output after this program has run.
//   So the only job left for code here is faithful delivery:
//   copy this repository's POST.json, byte for byte, into /output
//   where the gate expects to find it.
//
// Local stand-ins (used outside the grader's container):
//   MAKEFUN_BOT_DIR    stands in for /bot    (the repository root)
//   MAKEFUN_OUTPUT_DIR stands in for /output (the results folder)
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const botDir = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

const sourcePath = join(botDir, 'POST.json');
const targetPath = join(outputDir, 'POST.json');

// Fail loudly on a malformed POST.json instead of copying junk:
// the gate wants a JSON object whose "url" names an X post, so a
// quick shape check here saves a wasted submission round-trip.
let parsed: unknown;
try {
  parsed = JSON.parse(readFileSync(sourcePath, 'utf8'));
} catch (err) {
  console.error(`POST.json is not readable JSON: ${(err as Error).message}`);
  process.exit(1);
}
if (
  typeof parsed !== 'object' ||
  parsed === null ||
  typeof (parsed as { url?: unknown }).url !== 'string'
) {
  console.error('POST.json must be a JSON object with a string "url" field.');
  process.exit(1);
}

mkdirSync(outputDir, { recursive: true });
copyFileSync(sourcePath, targetPath);

// Read the copy back and compare bytes: the gate parses exactly this
// file, so a silent short write would only surface as a refused entry
// after submission. Verifying here keeps both grader runs honest —
// they must produce the same bytes, and now we know they do.
const copied = readFileSync(targetPath);
if (!copied.equals(readFileSync(sourcePath))) {
  console.error('POST.json copy verification failed: bytes differ.');
  process.exit(1);
}
