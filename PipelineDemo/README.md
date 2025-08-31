# Biomedical-Interactive-Visuals

[![mini-pipeline](https://github.com/niisaban/Biomedical-Interactive-Visuals/actions/workflows/mini-pipeline.yml/badge.svg)](https://github.com/niisaban/Biomedical-Interactive-Visuals/actions/workflows/mini-pipeline.yml)
[**Live page →**](https://niisaban.github.io/Biomedical-Interactive-Visuals/PipelineDemo/site/)

Interactive biomedical data visualization demos + reproducible notebooks.

**Quick paths**
- Data (input) → `PipelineDemo/data/raw/mini_gene_expression.csv`
- Summary (output) → `PipelineDemo/data/processed/summary_by_condition_gene.csv`
- Report → `PipelineDemo/reports/summary.md`
- Interactive plot → `PipelineDemo/site/index.html`

# Mini Pipeline Demo (local → cloud)

How it works
1. Load `data/raw/mini_gene_expression.csv`
2. Compute a grouped summary: `data/processed/summary_by_condition_gene.csv`
3. Build an interactive Plotly violin plot: `site/index.html`

Run locally
```bash
pip install -r PipelineDemo/requirements.txt
python PipelineDemo/src/pipeline.py

