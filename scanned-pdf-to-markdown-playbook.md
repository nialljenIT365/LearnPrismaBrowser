# Playbook: Accurate Markdown from a Scanned, Watermarked PDF

A reproducible method for turning an **image-only (scanned) PDF** — especially one
with a repeating structure (numbered items, Q&A, forms) and a **gray watermark
stamped over the text** — into a clean, searchable, correctly-segmented Markdown
file. Written to be handed to another agent. No tool/vendor names; substitute your
own document's terms where indicated.

---

## Core principles

1. **Two independent problems.** *Text quality* (are the words right?) and
   *segmentation* (is each logical unit in the right place?) are separate and can
   **trade off against each other**. Improving one pass can silently wreck the
   other. Always measure both.
2. **Program the analysis; don't read the raw dump.** Never pull the whole OCR
   output into your working context to "eyeball" it. Run **detectors** over it in a
   sandbox/subprocess and surface only the derived findings (counts, sample tokens).
   The raw bytes stay out of context.
3. **Deterministic, reviewable scripts — not ad-hoc edits.** Every transform lives
   in a script with an explicit, auditable map. This makes the whole pipeline
   re-runnable and lets a reviewer see exactly what changed.
4. **Verify every claim with a detector; iterate to zero.** After each cleanup pass,
   re-run the detectors. "Done" means the detectors return zero (minus a known
   allowlist), not "looks good".
5. **Never fabricate.** Where the scan is irreducibly garbled, leave it flagged or
   fill it **only** from an authoritative clean source — and mark that as a
   transcription/override, never as OCR.

---

## Stage 0 — Reconnaissance

- **Is the PDF actually scanned?** If it has a real text layer, skip OCR entirely and
  extract text directly. Only image-only pages need OCR.
- **Pick an OCR engine that installs cleanly** on your runtime. Note version/wheel
  constraints up front (some engines have no wheels for the newest language
  runtimes — pick an alternative that ships the same models).
- **Render pages with a PDF library in-process** (e.g. a PyMuPDF-style renderer)
  rather than depending on an external binary that may be absent.
- Record page count, DPI you'll render at, and the document's **repeating structural
  delimiter** (page footers, item headers, a "Question N" marker, a form-field
  label). You will segment on this.

## Stage 1 — Whiten the watermark *before* OCR

A light-gray watermark crossing the text is the #1 cause of **fused words**
(`NOTbeableto`) and character confusions. Remove it at the pixel level before OCR:

```python
# Render each page grayscale at a high DPI, then whiten everything lighter than a
# threshold: the pale watermark disappears, near-black body text is kept.
import io, numpy as np
from PIL import Image
THRESH = 150  # tune: just below body-text darkness, above watermark gray

def clean_page_image(pdf_page, dpi=300):
    pix  = pdf_page.render_grayscale(dpi=dpi)          # engine-specific
    arr  = np.frombuffer(pix.samples, np.uint8).reshape(pix.height, pix.width)
    arr  = np.where(arr < THRESH, arr, 255)            # drop the light watermark
    buf  = io.BytesIO(); Image.fromarray(arr).save(buf, "PNG")
    return buf.getvalue()
```

One-page A/B test to prove the threshold before running all pages:

| Variant | Typical result |
|---|---|
| plain render | `NOTbeableto returnto it.` ❌ |
| watermark whitened + higher DPI | `NOT be able to return to it.` ✅ |

## Stage 2 — Segment on the structural delimiter

Build a token stream from the OCR lines, tagging the delimiter tokens (footers /
headers / item markers). Split into logical units on the delimiter. Number/assign
each unit, tolerant of gaps.

> **Critical gotcha:** higher-DPI + watermark-whitening can *fix the text but break
> the delimiter detection* (e.g. a footer's date or number now OCRs differently), so
> units bleed into their neighbours. **You will not see this unless you measure it.**

## Stage 3 — Choose the authoritative base by *structure*, not recency

If you have two passes — say **Pass A** (clean text, scrambled structure) and
**Pass B** (noisier text, correct structure) — do **not** assume the newer/cleaner-
text pass is the deliverable. Compare them:

```python
# Per-unit length ratio between two passes flags where content sloshed around.
for n in units:
    r = len(A[n]) / max(1, len(B[n]))
    if r < 0.5: print(n, "A-too-short  (content bled OUT)")
    if r > 1.8: print(n, "A-too-fat    (swallowed a neighbour)")
    if not A[n]: print(n, "A-empty")
```

If many units diverge and one giant unit swallowed the tail, that pass's
**segmentation is untrustworthy**. **Rule: keep the pass with correct STRUCTURE as
the base and repair its TEXT** — structure is hard to reconstruct, text is easy to
clean. (In practice the noisier-but-correctly-segmented pass wins.)

## Stage 4 — Inventory the artifacts programmatically

Run these detectors over the chosen base; surface only the findings:

- **Long no-space runs:** `\b[A-Za-z]{15,}\b` → lost-space joins.
- **camelCase joins:** `[a-z][A-Z]` → e.g. `AnswerArea`.
- **Digit-adjacent joins:** alpha-only regexes miss `Word123More`; scan
  `[A-Za-z]+\d+[A-Za-z]+` separately.
- **Domain glyph confusions:** list-up the systematic misreads for *your* corpus
  (commonly capital-`I`→`l`, `rn`↔`m`, `0`↔`O`, an acronym letter dropped). Confirm
  each is safe to globally replace by **printing every occurrence's context first**.
- **Watermark crumbs:** residual fragments of the watermark string and stray
  `*.com`/domain tokens that survived.
- **Empty / very-short units, duplicate markers, out-of-order delimiters.**

### The key trick: a *self-bootstrapping* word-segmenter

To re-space joined words **without mangling proper nouns**, segment suspect tokens
using **only the words that already appear, correctly spaced, elsewhere in the same
document**. The document is its own dictionary, so product/proper names it uses are
never split into "real" English words.

```python
from collections import Counter
import re
vocab = Counter(t.lower() for t in re.findall(r"[A-Za-z]+", TEXT))
common = {w for w, c in vocab.items() if c >= 2 and len(w) >= 3} | {"a", "i",
         "to","be","it","of","in","is","an","or","by","as"}   # allow real 2-letter words

def segment(word):                      # DP: fewest pieces, each piece in `common`
    n = len(word); best = [None]*(n+1); best[0] = []
    for i in range(1, n+1):
        for j in range(max(0, i-18), i):
            piece = word[j:i]
            if best[j] is not None and piece in common:
                cand = best[j] + [piece]
                if best[i] is None or len(cand) < len(best[i]): best[i] = cand
    return best[n]
# Flag t where segment(t.lower()) splits into >=2 pieces. Exclude a small allowlist
# of real long words it wrongly splits (e.g. "datasets" -> "data sets").
```

This turns the open-ended "find all joined words" problem into a finite, reviewable
list. Run it again after each cleanup pass — it converges to zero.

## Stage 5 — Deterministic cleanup script

Order matters. Apply, in sequence, on the structural base:

1. **Whole-token crumb removal** (watermark fragments, stray `*.com`). Remove the
   token and let whitespace collapse — never partial-match inside a real word.
2. **Marker normalization** (your structural/answer markers → one canonical form).
3. **Curated joined-token map** — an **explicit dict** `{exact_token: "spaced form"}`,
   built from Stage 4's finite list. *Not* a blind segmenter at write-time: each
   entry is reviewed, so proper names are safe. Apply `\b`-anchored, longest-key-first.
4. **Verified global glyph fixes** — only the ones you confirmed have zero false
   positives, `\b`-anchored.
5. **Punctuation-adjacent joins** (`)X`→`) X`, `word(ACRONYM)`→`word (ACRONYM)`,
   possessive `s'word`→`s' word`).
6. **Line-local whitespace tidy** — collapse runs of spaces, strip space-before-
   punctuation, cap blank lines. Operate per line so you never merge across newlines.

Keep the original extraction untouched as a backup; the script reads the base and
writes a *separate* clean output, so it's idempotent and re-runnable.

## Stage 6 — Verify, and assert invariants

Re-run **all** Stage-4 detectors. Then assert structural invariants by comparing the
clean output against the base:

- unit count unchanged; **no empty units**;
- **structural/answer markers preserved** — compare *counts* base-vs-clean (they must
  match, or only increase where you intentionally normalized a fused marker);
- no unit's length changed beyond the expected crumb-removal delta (e.g. >40 chars
  flags accidental content loss);
- detectors return zero except a documented allowlist (real long words; intentionally-
  unfixable regions).

Only when all of that holds is the pass "done".

## Stage 7 — Irreducible garble (don't guess)

Some regions are corrupted in **every** pass (watermark sat directly over small
type). Do not invent text. Two honest options:

- **Leave it flagged** as-is, and note it in the file's preamble; or
- **Override from an authoritative clean source** (a clean screenshot/copy of that
  unit). Store these in a clearly-labelled `OVERRIDES = {unit_id: "clean text"}`
  block in the script, marked as **transcription, not OCR**, so it's reproducible and
  auditable. Mark any known-correct selections explicitly.

## Stage 8 — Derived outputs

Generate secondary artifacts (an index, a key, a summary) **from the cleaned file**
with a separate deterministic script, so they always reflect the latest clean source.

---

## Anti-patterns (don't)

- ❌ Read the whole OCR dump into context to skim it — slow, lossy, unreliable. Use detectors.
- ❌ Blind global find/replace without printing false-positive context first.
- ❌ A generic English word-segmenter — it shreds proper nouns. Use the document's own vocabulary.
- ❌ Trust the highest-DPI / most-recent pass blindly — verify its *structure*.
- ❌ Fabricate content for garbled regions.
- ❌ One giant manual edit — keep it in a re-runnable script with explicit maps.

## Minimal pipeline at a glance

```
render (whiten watermark) ─► OCR ─► segment on delimiter ─► [two passes? compare]
   ─► pick base by STRUCTURE ─► inventory artifacts (detectors + self-bootstrap)
   ─► deterministic cleanup (crumbs ▸ markers ▸ curated joins ▸ verified glyphs ▸ tidy)
   ─► verify to zero + assert invariants ─► override only irreducible garble
   ─► derive secondary outputs
```

## Suggested file/script layout

```
source.pdf                 # original scan (never modified)
extract_raw.py             # render+whiten+OCR+segment  -> base.md  (+ keep a backup)
cleanup.py                 # base.md -> clean.md   (curated maps, verified globals, OVERRIDES)
make_<derived>.py          # clean.md -> index / key / summary
PLAYBOOK.md                # this method
```
