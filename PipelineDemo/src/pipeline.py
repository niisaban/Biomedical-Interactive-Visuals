from pathlib import Path
import pandas as pd
import plotly.express as px

# --- Paths (relative to this file) ---
ROOT = Path(__file__).resolve().parents[1]            # PipelineDemo/
RAW = ROOT / "data" / "raw" / "mini_gene_expression.csv"
PROC_DIR = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"
SITE = ROOT / "site"

PROC_DIR.mkdir(parents=True, exist_ok=True)
REPORTS.mkdir(parents=True, exist_ok=True)
SITE.mkdir(parents=True, exist_ok=True)

# 1) Ingest
df = pd.read_csv(RAW)

# 2) Transform / summarize
summary = (
    df.groupby(["condition", "gene"], as_index=False)
      .agg(size=("expression", "size"),
           mean=("expression", "mean"),
           std=("expression", "std"))
)
summary_file = PROC_DIR / "summary_by_condition_gene.csv"
summary.to_csv(summary_file, index=False)

# 3) Interactive viz
fig = px.violin(
    df, x="condition", y="expression", color="gene",
    box=True, points="all",
    title="Mini Pipeline Demo: Expression by Condition (Violin + Points)"
)
fig.update_layout(template="plotly_white")
html_out = SITE / "index.html"
fig.write_html(html_out, include_plotlyjs="cdn", full_html=True)

# 4) Small markdown report
report_text = (
    "# Mini Pipeline Demo Report\n\n"
    f"**Input:** `{RAW.name}`\n\n"
    f"**Rows:** {len(df)}\n\n"
    f"**Output summary:** `{summary_file.relative_to(ROOT)}`\n\n"
    f"**Interactive plot:** `{html_out.relative_to(ROOT)}`\n\n"
    "## Grouped summary (first rows)\n\n"
    f"{summary.head().to_markdown(index=False)}\n"
)
(REPORTS / "summary.md").write_text(report_text, encoding="utf-8")

print("Pipeline complete.")
print(f"  summary  -> {summary_file.relative_to(ROOT)}")
print(f"  report   -> {(REPORTS / 'summary.md').relative_to(ROOT)}")
print(f"  site     -> {html_out.relative_to(ROOT)}")
