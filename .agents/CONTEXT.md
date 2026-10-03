# Project Context: Finance Workspace

- **Workspace Path**: `c:\Users\Rahul\Documents\antigravity\Finance`
- **Domain**: CFA Program Exam Prep (Level 1 & Level 2), covering Financial Statement Analysis (FSA), Fixed Income, and Equity Valuation.
- **Core Deliverables**:
  - `build_fi_eq_notes.py`: Self-contained compiler script generating the complete Fixed Income & Equity revision notes & testing simulator.
  - `fi_eq_dashboard.html`: Fully interactive CFA study dashboard (697 KB) with KaTeX math, Chart.js simulations, dark/light themes, and 340 exam questions.
  - `data/fi_eq/cfa_fi_eq_master.json`: 340 certified questions (85 L1 FI MCQs, 85 L1 Equity MCQs, 85 L2 FI across 17 vignettes, 85 L2 Equity across 17 vignettes).
  - `data/fi_eq/`: Modular dataset files (`l1_fixed_income.json`, `l1_equity.json`, `l2_fixed_income.json`, `l2_equity.json`).
  - `scripts/`: Compilation, simulation, and audit tools (`compile_master_suite.py`, `generate_full_dashboard.py`, `audit_suite.py`, `verify_final_suite.py`).
  - FSA Suite: `index.html` (1,008,541 bytes) and `build_notes.py` (400 questions).
- **Interactive Simulations**:
  - Yield Curve Shift, Twist & Butterfly Simulator.
  - Binomial Interest Rate Tree & Embedded Option Backward Induction Engine.
  - Equity Valuation: Two-Stage DDM, H-Model & DuPont 5-Way Decomposition Explorer.
  - Key Rate Duration & Sensitivity Visualizer.
  - Structural Reference Diagrams: Merton Default Model, CDS Curve Trades, Porter's 5 Forces, Negative Convexity.
- **Audit Status**: Certified by dual subagent peer audit (Auditor Alpha - Fixed Income & Quant Lead; Auditor Beta - Equity Valuation & Pedagogy Lead) across 4 formal debate rounds.
- **Rule Compliance**: Currency strictly formatted with `USD`, `EUR`, `GBP` or `\$`, KaTeX delimiters properly isolated, 0 errors, 0 warnings.
- **Content Audit (2026-10-04)**: Full CFA syllabus audit completed. 3/10 topics covered (FSA, FI, Equity) at ~89-91% module depth. 7 topics missing (Ethics, Quant, Econ, Corp Issuers, Derivatives, Alts, Portfolio Mgmt). ~1,480 total questions. 0 schema/technical errors. See `cfa_content_audit.md` artifact for full gap analysis and roadmap.
