import pandas as pd
import plotly.express as px
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "mini_gene_expression.csv"
PROC_DIR = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"
SITE = ROOT / "site"

PROC_DIR.mkdir(parents=True, exist_ok=True)
REPORTS.mkdir(parents=True, exist_ok=True)
SITE.mkdir(parents=True, exist_ok=True)

# 1) ingest
df = pd.read_csv(RAW)

# 2) transform / summarize
summary = (
    df.groupby(["condition", "gene"], as_index=False)
      .agg(n=("expression", "size"),
           mean_expression=("expression", "mean"),
           sd=("expression", "std"))
)
summary_file = PROC_DIR / "summary_by_condition_gene.csv"
summary.to_csv(summary_file, index=False)

# 3) interactive viz
fig = px.violin(
    df, x="condition", y="expression", color="gene", box=True, points="all",
    title="Mini Pipeline Demo: Expression by Condition (Violin + Points)"
)
fig.update_layout(template="plotly_white")
html_out = SITE / "index.html"
fig.write_html(html_out, include_plotlyjs="cdn", full_html=True)

# 4) small markdown report
report_text = (
    f"# Mini Pipeline Demo Report\n\n"
    f"- **Input:** `{RAW}`\n"
    f"- **Rows:** {len(df)}\n"
    f"- **Output summary:** `{summary_file}`\n"
    f"- **Interactive plot:** `PipelineDemo/site/index.html`\n\n"
    f"## Grouped Statistics (first rows)\n\n{summary.head().to_markdown(index=False)}\n"
)
(REPORTS / "summary.md").write_text(report_text, encoding="utf-8")

print("Pipeline complete.")
print(f"  - {summary_file.relative_to(ROOT)}")
print(f"  - {html_out.relative_to(ROOT)}")
