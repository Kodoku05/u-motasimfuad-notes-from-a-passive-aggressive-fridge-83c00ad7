import os
from pathlib import Path


NOTE = "Inventory update: Sunday's chicken is now a tenant. No rent, but unlike you, it never leaves my door open."
OUTPUT_FILE = "entry.txt"

if not NOTE.strip() or "\n" in NOTE:
    raise ValueError("NOTE must be non-empty and contain no newline characters")

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / OUTPUT_FILE).write_text(NOTE, encoding="utf-8")
