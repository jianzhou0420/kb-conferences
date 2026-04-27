"""Regenerate CoRL 2025 browse views from raw JSON metadata.

Reads paper JSONs under `_data/{Oral,Poster}/papers/*.json` and emits:
  - oral.md         (Oral track, compact card list)
  - poster.md       (Poster track, compact card list)
  - by-field.md     (cross-track grouping by topic)
  - by-author.md    (alphabetical lead-author index)

`highlights.md` and `index.md` are NOT touched — those are manual.

Usage:
    python regenerate_corl2025_views.py

Stub — implementation pending data migration. Once `_data/` is populated,
fill in `load_papers()`, `render_card()`, and the four view emitters.
"""
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
CONF_DIR = SCRIPT_DIR.parent
DATA_DIR = CONF_DIR / "_data"


def main() -> None:
    if not DATA_DIR.exists() or not any(DATA_DIR.rglob("*.json")):
        print(f"[regen] No JSON data under {DATA_DIR} — nothing to do.")
        return
    raise NotImplementedError("Implement after data migration.")


if __name__ == "__main__":
    main()
