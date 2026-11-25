"""Write the 25 November 2026 front-page image to the output directory.

Standard library only. No network. The image is shipped in this
repository as entry.png (drawn during this build by
render_frontpage.py); this program copies it byte for byte, so two
runs always write identical bytes.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        raise FileNotFoundError(f"entry image missing: {source}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    # A copy must be exact: refuse a short or altered write rather
    # than leaving a corrupt image for the gate to reject.
    if target.stat().st_size != source.stat().st_size:
        raise OSError("entry.png copy size mismatch")


if __name__ == "__main__":
    main()
