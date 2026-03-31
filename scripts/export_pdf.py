from __future__ import annotations

import os
from pathlib import Path


try:
    import win32com.client  # type: ignore
except ImportError as e:
    raise SystemExit(
        "pywin32 is required for this script. Install with: pip install pywin32"
    ) from e


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DOCX_PATH = PROJECT_ROOT / "output" / "manuscript-draft-advisory.docx"
PDF_PATH = PROJECT_ROOT / "output" / "manuscript-draft-advisory-WATERMARKED.pdf"

WATERMARK_TEXT = "DRAFT"
WATERMARK_SHAPE_NAME = "DRAFT_WATERMARK"


def _file_size(path: Path) -> int:
    return path.stat().st_size if path.exists() else 0


def main() -> None:
    if not DOCX_PATH.exists():
        raise FileNotFoundError(f"Expected DOCX at: {DOCX_PATH}")

    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0

    doc = word.Documents.Open(str(DOCX_PATH))
    try:
        for section in doc.Sections:
            # wdHeaderFooterPrimary = 1
            header = section.Headers(1)

            # Remove any prior watermark to avoid duplicates on re-runs.
            try:
                for shape in list(header.Shapes):
                    if getattr(shape, "Name", "") == WATERMARK_SHAPE_NAME:
                        shape.Delete()
            except Exception:
                pass

            # Add watermark on header layer so it appears across the page.
            header.Range.Select()
            shape = header.Shapes.AddTextEffect(
                PresetTextEffect=1,  # msoTextEffect1
                Text=WATERMARK_TEXT,
                FontName="Times New Roman",
                FontSize=72,
                FontBold=True,
                FontItalic=False,
                Left=150,
                Top=200,
            )
            shape.Name = WATERMARK_SHAPE_NAME
            shape.Fill.ForeColor.RGB = 0xDDDDDD  # light gray
            try:
                # Higher transparency helps keep body text readable.
                shape.Fill.Transparency = 0.55
            except Exception:
                pass
            shape.Line.Visible = False
            shape.Rotation = 315  # 45-degree diagonal (Word uses 0..360)

    finally:
        # Export + cleanup
        doc.SaveAs(str(PDF_PATH), FileFormat=17)  # 17 = wdFormatPDF
        # Word stats: 2 == wdStatisticPages
        pages = doc.ComputeStatistics(2)
        doc.Close()
        word.Quit()

    print("export_pdf.py results")
    print(f"- DOCX path: {DOCX_PATH}")
    print(f"- PDF path: {PDF_PATH}")
    print(f"- DOCX size (bytes): {_file_size(DOCX_PATH)}")
    print(f"- PDF size (bytes): {_file_size(PDF_PATH)}")
    print(f"- PDF page count (Word stats): {pages}")


if __name__ == "__main__":
    main()

