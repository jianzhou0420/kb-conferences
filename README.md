# kb-conferences — Conference Knowledge Base

Per-conference paper indexes for robotics / embodied-AI venues — CoRL, ICRA, RSS, NeurIPS, CVPR, etc. Each conference gets compact browse views (by field, by author, by track) generated from raw JSON metadata, plus a hand-curated `highlights.md` for personally-tracked papers.

This repo is the content source for the **Conferences** tab of the [docs-site-knowledge-base](https://github.com/jianzhou0420/docs-site-knowledge-base) doc-site. It is consumed as a git submodule at `docs/kb-conferences/` but stands alone as a browsable reference.

## Layout

```
<CONFERENCE><YEAR>/
├── index.md            Overview, stats, entry points
├── oral.md             Oral track — compact card list
├── poster.md           Poster track — compact card list
├── by-field.md         Cross-track grouping by topic
├── by-author.md        Cross-track index by lead author
├── highlights.md       Hand-picked papers (manual)
├── _data/              Raw JSON metadata, one file per paper
└── _scripts/           View regenerators (Python)
```

Deep methodological notes on individual papers live in topic-specific KBs (e.g. [kb-vla](https://github.com/jianzhou0420/kb-vla), [kb-vln](https://github.com/jianzhou0420/kb-vln)) and are linked back from the conference cards.

## Coverage

| Conference | Status |
|---|---|
| CoRL 2025 | scaffolding |

## License

Personal notes — no warranty. Underlying paper metadata belongs to the original authors and venues.
