#!/usr/bin/env python3
"""Build docs/rsgb-sdd-n6yu-speaker-notes.html from the Markdown source.

Edit docs/rsgb-sdd-n6yu-speaker-notes.md, then run:

    python3 scripts/build_speaker_notes.py

The HTML keeps its own page shell (styles, buttons, key handling); only the
slide sections between the <main> markers are regenerated. Standard library only.

Markdown format:
    # Title                      page title
    Subtitle line                (first non-blank line after the title)
    ## 3. Slide title            a slide; "## Appendix" / "## Backup" start a divider
                                 (one plain line under a divider becomes its note)
    ### 17. Slide title          a slide under a divider
    **Takeaway:** text           gold takeaway box
    - bullet / "  - " nested     speaker notes
    **POLL:** text               red POLL tag
    **bold**, *italic*, `code`   inline formatting
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MD = ROOT / "docs" / "rsgb-sdd-n6yu-speaker-notes.md"
OUT = ROOT / "docs" / "rsgb-sdd-n6yu-speaker-notes.html"

START = '<main>\n'
END = '  <p class="keys">'


def inline(text):
    t = html.escape(text, quote=False)
    t = re.sub(r"\*\*POLL:\*\*", '<strong class="poll">POLL</strong>', t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", t)
    return t


def bullets(lines):
    """Render '- ' lines (two-space indent per level) as nested <ul>."""
    out, depth = [], -1
    for raw in lines:
        m = re.match(r"^( *)- (.*)$", raw)
        if not m:
            continue
        level = len(m.group(1)) // 2
        item = inline(m.group(2))
        if level > depth:
            out.append("<ul>\n" * (level - depth - 1) + "<ul>" if depth >= 0 else "<ul>")
            out.append("\n<li>" + item)
        elif level == depth:
            out.append("</li>\n<li>" + item)
        else:
            out.append("</li>\n" + "</ul>\n</li>\n" * (depth - level - 1) + "</ul>\n</li>\n<li>" + item)
        depth = level
    if depth >= 0:
        out.append("</li>\n" + "</ul>\n</li>\n" * depth + "</ul>")
    return "".join(out)


def build(md_text):
    title, subtitle, slides, parts = None, None, [], []
    cur = None
    for line in md_text.splitlines():
        if line.startswith("# ") and title is None:
            title = line[2:].strip()
        elif line.strip() == "---":
            continue
        elif re.match(r"^## (?!\d)", line):
            slides.append(("divider", [line[3:].strip(), ""]))
            cur = None
        elif re.match(r"^#{2,3} (\d+)\. (.*)$", line):
            m = re.match(r"^#{2,3} (\d+)\. (.*)$", line)
            cur = {"num": m.group(1), "title": m.group(2), "takeaway": "", "lines": []}
            slides.append(("slide", cur))
        elif cur is None:
            if title and subtitle is None and line.strip():
                subtitle = line.strip()
            elif slides and slides[-1][0] == "divider" and line.strip():
                slides[-1][1][1] = line.strip()  # one-line note under a divider
        elif line.startswith("**Takeaway:**"):
            cur["takeaway"] = line[len("**Takeaway:**"):].strip()
        elif line.strip():
            cur["lines"].append(line.rstrip())

    parts.append('  <div class="title"><h1>%s</h1><p>%s</p></div>' % (inline(title), inline(subtitle or "")))
    for kind, val in slides:
        if kind == "divider":
            parts.append('<h2 class="divider">%s</h2>' % inline(val[0]))
            if val[1]:
                parts.append('<p class="divnote">%s</p>' % inline(val[1]))
            continue
        notes = bullets(val["lines"])
        notes_html = '<div class="notes">%s</div>' % notes if notes else ""
        parts.append(
            '<section class="slide" id="s{n}" tabindex="-1">\n'
            '  <header><span class="num">{n}</span><h2>{t}</h2></header>\n'
            '  <p class="takeaway">{k}</p>\n'
            '  {notes}\n</section>'.format(n=val["num"], t=inline(val["title"]), k=inline(val["takeaway"]), notes=notes_html))
    return "\n".join(parts) + "\n"


def main():
    page = OUT.read_text(encoding="utf-8")
    a, b = page.index(START) + len(START), page.index(END)
    new = page[:a] + build(MD.read_text(encoding="utf-8")) + page[b:]
    OUT.write_text(new, encoding="utf-8")
    print("wrote", OUT.relative_to(ROOT))


if __name__ == "__main__":
    sys.exit(main())
