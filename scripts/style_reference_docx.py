from __future__ import annotations

import os
import subprocess
from datetime import date
from pathlib import Path
import shutil

from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.shared import Inches, Mm, Pt, RGBColor


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
REFERENCE_DOCX = SCRIPTS_DIR / "reference.docx"


def _set_style_rfonts(style, font_name: str) -> None:
    """
    Ensure Times New Roman is used for ascii/eastAsia/CS fonts.
    python-docx sets some font attributes, but Word may fall back without eastAsia/CS.
    """
    # rFonts live under w:rPr inside the style element.
    rfonts = style._element.xpath(".//w:rFonts")
    for rf in rfonts:
        rf.set(qn("w:ascii"), font_name)
        rf.set(qn("w:hAnsi"), font_name)
        rf.set(qn("w:eastAsia"), font_name)
        rf.set(qn("w:cs"), font_name)


def _ensure_reference_docx() -> None:
    if REFERENCE_DOCX.exists():
        return

    SCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
    pandoc = _resolve_pandoc_exe()

    # Generate a copy of pandoc's built-in default reference.docx
    subprocess.check_call(
        [
            pandoc,
            "-o",
            str(REFERENCE_DOCX),
            "--print-default-data-file",
            "reference.docx",
        ],
        cwd=str(PROJECT_ROOT),
    )


def _resolve_pandoc_exe() -> str:
    """
    Return an absolute pandoc executable path.
    winget/MSI installs may not update PATH for the current shell/tool session.
    """
    env_override = os.environ.get("PANDOC_EXE") or os.environ.get("PANDOC")
    if env_override:
        if Path(env_override).exists():
            return env_override

    which = shutil.which("pandoc")
    if which:
        return which

    candidates = []
    local_appdata = os.environ.get("LOCALAPPDATA")
    if local_appdata:
        candidates.append(Path(local_appdata) / "Programs" / "Pandoc" / "pandoc.exe")
        candidates.append(Path(local_appdata) / "Pandoc" / "pandoc.exe")

    program_files = os.environ.get("ProgramFiles")
    if program_files:
        candidates.append(Path(program_files) / "Pandoc" / "pandoc.exe")

    program_files_x86 = os.environ.get("ProgramFiles(x86)")
    if program_files_x86:
        candidates.append(Path(program_files_x86) / "Pandoc" / "pandoc.exe")

    for c in candidates:
        if c.exists():
            return str(c)

    # Last resort: let subprocess produce a nice error.
    return "pandoc"


def main() -> None:
    _ensure_reference_docx()
    doc = Document(str(REFERENCE_DOCX))

    # ---- Page setup (A4 + 1-inch margins) ----
    section = doc.sections[0]
    section.page_width = Mm(210)
    section.page_height = Mm(297)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)

    font_name = "Times New Roman"
    navy = RGBColor(0x1F, 0x38, 0x64)  # #1F3864

    # ---- Default font / body text ----
    normal = doc.styles["Normal"]
    normal.font.name = font_name
    normal.font.size = Pt(12)
    normal.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    normal.paragraph_format.line_spacing = 1.15
    normal.paragraph_format.space_after = Pt(6)
    _set_style_rfonts(normal, font_name)

    # ---- Heading 1 ----
    h1 = doc.styles["Heading 1"]
    h1.font.name = font_name
    h1.font.size = Pt(14)
    h1.font.bold = True
    h1.font.color.rgb = navy
    h1.paragraph_format.space_before = Pt(12)
    h1.paragraph_format.space_after = Pt(12)
    _set_style_rfonts(h1, font_name)

    # ---- Heading 2 ----
    h2 = doc.styles["Heading 2"]
    h2.font.name = font_name
    h2.font.size = Pt(12)
    h2.font.bold = True
    # (No color override requested; keep default black.)
    h2.paragraph_format.space_before = Pt(8)
    h2.paragraph_format.space_after = Pt(8)
    _set_style_rfonts(h2, font_name)

    # ---- Table style: booktabs-look ----
    # python-docx can create the style; border/header-row formatting is enforced again later in postprocess_docx.py.
    try:
        doc.styles["booktabs-look"]
    except KeyError:
        doc.styles.add_style("booktabs-look", WD_STYLE_TYPE.TABLE)

    doc.save(str(REFERENCE_DOCX))
    print(f"Styled reference DOCX: {REFERENCE_DOCX}")


if __name__ == "__main__":
    main()

