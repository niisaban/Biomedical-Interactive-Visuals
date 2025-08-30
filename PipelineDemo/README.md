[![mini-pipeline](https://github.com/niisaban/Biomedical-Interactive-Visuals/actions/workflows/mini-pipeline.yml/badge.svg)](https://github.com/niisaban/Biomedical-Interactive-Visuals/actions/workflows/mini-pipeline.yml)
[**Live page →**](https://niisaban.github.io/Biomedical-Interactive-Visuals/PipelineDemo/site/)

# Mini Pipeline Demo (local → cloud)

How it works
1. Load `data/raw/mini_gene_expression.csv`
2. Compute a grouped summary: `data/processed/summary_by_condition_gene.csv`
3. Build an interactive Plotly violin plot: `site/index.html`

Run locally
```bash
pip install -r PipelineDemo/requirements.txt
python PipelineDemo/src/pipeline.py

