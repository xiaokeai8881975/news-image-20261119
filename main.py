"""news-image-20261119 entry: copy the image to the output directory.

Standard library only. Runs twice and writes the same bytes.
"""
import os
import shutil
from pathlib import Path

def main() -> None:
    src = Path(__file__).with_name("entry.png")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
