from __future__ import annotations

import re
from datetime import date
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_DOCX = PROJECT_ROOT / "output" / "manuscript-draft-advisory.docx"
FINAL_DOCX = PROJECT_ROOT / "output" / "manuscript-draft-advisory.docx"


ARTICLE_SHORT_TITLE = "Exploring the Impact of the 3 Zero Movement in Bangladesh"
HEADER_RIGHT_TEXT = "DRAFT \u2014 Not for Circulation"  # emulate em dash without non-ascii literals in source

FOOTER_LEFT_TEXT = "© Minhajul Abedin, NSTU, 2026. All rights reserved."
FOOTER_RIGHT_PREFIX = "Page "

TITLE_TEXT = (
    "Exploring the Impact of the 3 Zero Movement in Bangladesh: "
    "A Pathway to Sustainable Development"
)
AUTHOR_TEXT = "Minhajul Abedin"
AFFILIATION_TEXT = (
    "Department of Applied Mathematics, "
    "Noakhali Science and Technology University, "
    "Noakhali-3814, Bangladesh"
)
LABEL_TEXT = "DRAFT VERSION \u2014 SHARED FOR ADVISORY PURPOSES ONLY"

FONT_NAME = "Times New Roman"
RED = RGBColor(0xC0, 0x00, 0x00)
NAVY = RGBColor(0x1F, 0x38, 0x64)
GRAY = RGBColor(0x80, 0x80, 0x80)
TABLE_HEADER_FILL = "D5E8F0"  # #D5E8F0


def _set_run_font(run, *, size_pt=None, bold=None, italic=None, color=None) -> None:
    run.font.name = FONT_NAME
    if size_pt is not None:
        run.font.size = Pt(size_pt)
    if bold is not None:
        run.font.bold = bool(bold)
    if italic is not None:
        run.font.italic = bool(italic)
    if color is not None:
        run.font.color.rgb = color

    # Ensure Word uses the font for all scripts.
    rfonts = run._element.xpath(".//w:rFonts")
    for rf in rfonts:
        rf.set(qn("w:ascii"), FONT_NAME)
        rf.set(qn("w:hAnsi"), FONT_NAME)
        rf.set(qn("w:eastAsia"), FONT_NAME)
        rf.set(qn("w:cs"), FONT_NAME)


def _get_or_add_tcPr(tc):
    tcPr = tc.tcPr
    if tcPr is None:
        tcPr = OxmlElement("w:tcPr")
        tc.append(tcPr)
    return tcPr


def _set_cell_shading(cell, *, fill_hex: str) -> None:
    tcPr = _get_or_add_tcPr(cell._tc)
    shd = tcPr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tcPr.append(shd)
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill_hex)


def _set_cell_borders(cell, *, top=None, bottom=None, left=None, right=None, color="000000") -> None:
    """
    Border specs: either None (meaning nil) or dict: {val, sz}
    - val: 'single' or 'nil'
    - sz: string integer for Word's border size (in eighths of a point)
    """
    tcPr = _get_or_add_tcPr(cell._tc)
    tcBorders = tcPr.find(qn("w:tcBorders"))
    if tcBorders is None:
        tcBorders = OxmlElement("w:tcBorders")
        tcPr.append(tcBorders)

    def apply_edge(edge_name: str, spec):
        el = tcBorders.find(qn(f"w:{edge_name}"))
        if el is None:
            el = OxmlElement(f"w:{edge_name}")
            tcBorders.append(el)

        if spec is None:
            el.set(qn("w:val"), "nil")
            return

        el.set(qn("w:val"), spec.get("val", "single"))
        el.set(qn("w:sz"), str(spec.get("sz", 4)))
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), color)

    apply_edge("top", top)
    apply_edge("bottom", bottom)
    apply_edge("left", left)
    apply_edge("right", right)


def _add_horizontal_rule(doc: Document) -> None:
    """
    Creates a 'rule-like' paragraph by setting a bottom border.
    Returns the created paragraph.
    """
    p = doc.add_paragraph("")
    pPr = p._p.find(qn("w:pPr"))
    if pPr is None:
        pPr = OxmlElement("w:pPr")
        p._p.insert(0, pPr)
    pBdr = pPr.find(qn("w:pBdr"))
    if pBdr is None:
        pBdr = OxmlElement("w:pBdr")
        pPr.append(pBdr)

    # Remove any existing bottom border
    bottom = pBdr.find(qn("w:bottom"))
    if bottom is not None:
        pBdr.remove(bottom)
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "12")  # ~1.5pt
    bottom.set(qn("w:space"), "0")
    bottom.set(qn("w:color"), "D0D0D0")
    pBdr.append(bottom)

    # Keep spacing tight around the rule.
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(6)
    return p


def _paragraph_text(doc: Document, text: str) -> str:
    # Normalize whitespace for more robust matching.
    return re.sub(r"\s+", " ", text).strip()


def _insert_title_block(doc: Document) -> None:
    # Create title block paragraphs at document end, then move them to the top in correct order.
    today = date.today()
    dt_text = f"{today.day} {today:%B} {today.year}"

    title_p = doc.add_paragraph(TITLE_TEXT)
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in title_p.runs:
        _set_run_font(run, size_pt=16, bold=True, color=NAVY)

    author_p = doc.add_paragraph(AUTHOR_TEXT)
    author_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in author_p.runs:
        _set_run_font(run, size_pt=11, italic=True)

    aff_p = doc.add_paragraph(AFFILIATION_TEXT)
    aff_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in aff_p.runs:
        _set_run_font(run, size_pt=11, italic=True)

    date_p = doc.add_paragraph(dt_text)
    date_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in date_p.runs:
        _set_run_font(run, size_pt=10, color=GRAY)

    hr1 = _add_horizontal_rule(doc)

    label_p = doc.add_paragraph(LABEL_TEXT)
    label_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in label_p.runs:
        _set_run_font(run, size_pt=11, bold=True, color=RED)

    hr2 = _add_horizontal_rule(doc)

    # Move to top of doc, in reverse order so final visual order stays correct.
    body = doc._element.body
    to_move = [title_p, author_p, aff_p, date_p, hr1, label_p, hr2]
    for p in reversed(to_move):
        body.insert(0, p._p)


def _clear_container(container) -> None:
    # Remove all existing content (paragraphs/tables) inside header/footer.
    el = container._element
    for child in list(el):
        el.remove(child)


def _remove_table_cell_borders(tbl) -> None:
    for row in tbl.rows:
        for cell in row.cells:
            _set_cell_borders(cell, top=None, bottom=None, left=None, right=None)


def _add_header_footer(section, *, is_header: bool) -> None:
    header = section.header if is_header else section.footer
    _clear_container(header)
    header.is_linked_to_previous = False

    tbl = header.add_table(rows=1, cols=2, width=Inches(6.5))
    tbl.autofit = False

    left_cell = tbl.cell(0, 0)
    right_cell = tbl.cell(0, 1)

    # Remove any table borders so it behaves like a layout container.
    _remove_table_cell_borders(tbl)

    left_cell.text = ""
    right_cell.text = ""

    left_p = left_cell.paragraphs[0]
    right_p = right_cell.paragraphs[0]
    left_p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    right_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    if is_header:
        left_run = left_p.add_run(ARTICLE_SHORT_TITLE)
        _set_run_font(left_run, size_pt=10, italic=True)

        right_run = right_p.add_run(HEADER_RIGHT_TEXT)
        _set_run_font(right_run, size_pt=10, bold=True, color=RED)
    else:
        left_run = left_p.add_run(FOOTER_LEFT_TEXT)
        _set_run_font(left_run, size_pt=9, color=GRAY)

        page_para = right_cell.paragraphs[0]
        page_para.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        prefix_run = page_para.add_run(FOOTER_RIGHT_PREFIX)
        _set_run_font(prefix_run, size_pt=9, color=GRAY)

        # Word page field: { PAGE }
        fldSimple = OxmlElement("w:fldSimple")
        fldSimple.set(qn("w:instr"), "PAGE")
        r = OxmlElement("w:r")
        rPr = OxmlElement("w:rPr")
        rFonts = OxmlElement("w:rFonts")
        rFonts.set(qn("w:ascii"), FONT_NAME)
        rFonts.set(qn("w:hAnsi"), FONT_NAME)
        rFonts.set(qn("w:eastAsia"), FONT_NAME)
        rFonts.set(qn("w:cs"), FONT_NAME)
        rPr.append(rFonts)

        # Font size in half-points in Word.
        # 9pt -> 18 half-points.
        sz = OxmlElement("w:sz")
        sz.set(qn("w:val"), "18")
        rPr.append(sz)

        color_el = OxmlElement("w:color")
        # Hex without '#'
        color_el.set(qn("w:val"), "808080")
        rPr.append(color_el)

        t = OxmlElement("w:t")
        t.text = "1"
        r.append(rPr)
        r.append(t)
        fldSimple.append(r)
        page_para._p.append(fldSimple)


def _fix_tables(doc: Document) -> int:
    """
    Apply booktabs-like borders (thick top/bottom, thin mid, no vertical lines) and
    header row shading.
    """
    thick = {"val": "single", "sz": 12}
    thin = {"val": "single", "sz": 4}

    fixed = 0
    for table in doc.tables:
        rows = len(table.rows)
        if rows == 0:
            continue

        # best-effort: apply named style if present (otherwise borders are still enforced)
        try:
            table.style = "booktabs-look"
        except Exception:
            pass

        for r_idx, row in enumerate(table.rows):
            for cell in row.cells:
                # Shading + bold only on the first row.
                if r_idx == 0:
                    _set_cell_shading(cell, fill_hex=TABLE_HEADER_FILL)
                    for p in cell.paragraphs:
                        for run in p.runs:
                            run.bold = True

                # Borders: top thick on header row, mid thin under header, bottom thick on last row.
                # No vertical borders. No extra internal row borders.
                top_spec = thick if r_idx == 0 else None
                bottom_spec = (
                    thick if r_idx == rows - 1 else (thin if r_idx == 0 and rows > 1 else None)
                )
                _set_cell_borders(cell, top=top_spec, bottom=bottom_spec, left=None, right=None)

        fixed += 1

    return fixed


def _collect_text(doc: Document) -> str:
    parts = []
    for p in doc.paragraphs:
        parts.append(p.text)
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    parts.append(p.text)
    return "\n".join(parts)


def main() -> None:
    if not INPUT_DOCX.exists():
        raise FileNotFoundError(f"Expected DOCX at: {INPUT_DOCX}")

    doc = Document(str(INPUT_DOCX))

    # Apply header/footer to every section.
    for section in doc.sections:
        # Ensure header/footer changes are not linked.
        section.header.is_linked_to_previous = False
        section.footer.is_linked_to_previous = False
        section.different_first_page_header_footer = False
        _add_header_footer(section, is_header=True)
        _add_header_footer(section, is_header=False)

    # Insert title block at the top (page 1 area).
    _insert_title_block(doc)

    # Fix tables.
    tables_fixed = _fix_tables(doc)

    # ---- Logging for unconverted artifacts / unresolved citations ----
    full_text = _collect_text(doc)

    unresolved = full_text.count("[?]")
    latex_artifacts = 0
    # Heuristic: literal LaTeX command remnants.
    patterns = [
        r"\\begin\{",
        r"\\end\{",
        r"\\cite\w*",
        r"\\[a-zA-Z]+",
    ]
    for pat in patterns:
        latex_artifacts += len(re.findall(pat, full_text))

    print("postprocess_docx.py results")
    print(f"- tables_fixed: {tables_fixed}")
    print(f"- unresolved_citation_placeholders ([?]): {unresolved}")
    print(f"- unconverted_latex_artifacts (heuristic): {latex_artifacts}")

    doc.save(str(FINAL_DOCX))
    print(f"Saved final DOCX: {FINAL_DOCX}")


if __name__ == "__main__":
    main()

