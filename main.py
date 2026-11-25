import os
from pathlib import Path


NOTE = "Inventory update: the chicken from Sunday is now a tenant. It pays no rent, but unlike you, it never leaves my door open."

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(NOTE, encoding="utf-8")
