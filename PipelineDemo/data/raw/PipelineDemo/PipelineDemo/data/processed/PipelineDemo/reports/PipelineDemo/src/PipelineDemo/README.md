# Mini Pipeline Demo (local → cloud)

**Goal:** ingest a small CSV, compute grouped stats, and publish an interactive Plotly HTML to GitHub Pages.

## How it works
1. Load `data/raw/mini_gene_expression.csv`
2. Compute summary by `condition` × `gene` → `data/processed/summary_by_condition_gene.csv`
3. Generate interactive violin plot → `site/index.html` (served by GitHub Pages)

## Run locally
```bash
pip install -r PipelineDemo/requirements.txt
python PipelineDemo/src/pipeline.py

