from __future__ import annotations

import os
import re
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_HTML = PROJECT_ROOT / "output" / "paper-article-v3-google-docs.html"
OUTPUT_HTML = PROJECT_ROOT / "output" / "paper-article-v3-google-docs-copy.html"


def _filename_only(path: str) -> str:
    # Keep it simple for copy/paste readability.
    return os.path.basename(path)


def main() -> None:
    if not INPUT_HTML.exists():
        raise FileNotFoundError(f"Expected HTML at: {INPUT_HTML}")

    txt = INPUT_HTML.read_text(encoding="utf-8", errors="ignore")

    # Replace empty image placeholder spans with a visible note.
    # Example in Pandoc output:
    # <span class="image placeholder" data-original-image-src="...pdf" data-original-image-title="" width="85%"></span>
    span_pat = re.compile(
        r"<span class=\"image placeholder\"[^>]*data-original-image-src=\"(?P<src>[^\"]+)\"[^>]*></span>",
        re.IGNORECASE,
    )

    def repl(m: re.Match) -> str:
        src = m.group("src")
        fn = _filename_only(src)
        # Inline style so Google Docs paste shows the note.
        return f"<span style=\"color:#666;\">[Missing figure image: {fn}]</span>"

    out, n = span_pat.subn(repl, txt)

    if n == 0:
        print("postprocess_google_docs_html.py: no placeholders replaced (nothing to do).")
    else:
        print(f"postprocess_google_docs_html.py: replaced {n} missing-image placeholder(s).")

    OUTPUT_HTML.write_text(out, encoding="utf-8")
    print(f"Saved: {OUTPUT_HTML}")


if __name__ == "__main__":
    main()

