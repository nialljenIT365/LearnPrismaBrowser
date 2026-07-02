"""Convert the born-digital PDFs in this folder to Markdown (one .md per PDF).

WHY NO OCR: per `scanned-pdf-to-markdown-playbook.md` Stage 0, the first question is
"is the PDF actually scanned?". These PDFs are NOT — every page has a real text layer
(verified ~1000-2000 chars/page). So we extract the authored text directly.

pymupdf4llm's *default* layout parser auto-runs RapidOCR on figure-heavy pages, which
injects fused, out-of-order OCR garbage from inside architecture diagrams
(e.g. "beabletologintothe", "AlAccessPermitted" = an AI->Al misread). That degrades
otherwise-perfect digital text. `use_layout(False)` selects the classic text-layer RAG
parser instead: tables + headings, NO OCR — the correct method for born-digital PDFs.

Requires: pip install pymupdf4llm   (pulls in PyMuPDF)
Run:      py -3.14 convert_pdfs_to_md.py
"""
import os, glob
import pymupdf4llm

pymupdf4llm.use_layout(False)            # text-layer parser, no OCR

FOLDER = os.path.dirname(os.path.abspath(__file__))

for pdf in sorted(glob.glob(os.path.join(FOLDER, "*.pdf"))):
    stem = os.path.splitext(os.path.basename(pdf))[0]
    out = os.path.join(FOLDER, stem + ".md")
    md = pymupdf4llm.to_markdown(pdf, ignore_images=True, show_progress=False)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(md)
    print(f"{stem}.md  ({len(md):,} chars)")

print("Done. One Markdown file written per PDF.")
