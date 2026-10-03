# Project Context: Finance Workspace

- **Workspace Path**: `c:\Users\Rahul\Documents\antigravity\Finance`
- **Domain**: CFA Program Exam Prep (Level 1 & Level 2), covering Financial Statement Analysis (FSA), Fixed Income, and Equity Valuation.
- **Total Questions**: **855 Certified Questions** across 2 comprehensive interactive suites:
  - **FSA Master Suite**: 440 Questions (190 L1 MCQs + 250 L2 Questions across 50 vignettes) in `index.html` (1.09 MB).
  - **Fixed Income & Equity Suite**: 415 Questions (120 L1 FI MCQs, 115 L1 Equity MCQs, 85 L2 FI across 17 vignettes, 95 L2 Equity across 19 vignettes) in `fi_eq_dashboard.html` (828 KB).
- **Core Deliverables**:
  - `fi_eq_dashboard.html`: Fully interactive CFA study dashboard with KaTeX math, Chart.js simulations, dark/light themes, 415 exam questions, and 9 financial engines.
  - `index.html`: Complete FSA study portal with 440 questions, interactive feedback, and multi-period financial analyses.
  - `data/fi_eq/cfa_fi_eq_master.json`: 415 validated questions.
  - `data/cfa_question_bank_master.json`: 440 validated questions.
  - `data/fi_eq/`: Modular dataset files (`l1_fixed_income.json`, `l1_equity.json`, `l2_fixed_income.json`, `l2_equity.json`).
  - `scripts/`: Compilation, simulation, and audit tools (`compile_master_suite.py`, `compile_qb.py`, `generate_full_dashboard.py`, `audit_suite.py`, `verify_final_suite.py`).
- **Interactive Simulations (9 Total)**:
  1. Yield Curve Shift, Twist & Butterfly Simulator.
  2. Binomial Interest Rate Tree & Embedded Option Backward Induction Engine.
  3. Equity Valuation: Two-Stage DDM & DuPont Explorer.
  4. Key Rate Duration & Sensitivity Visualizer.
  5. Floating-Rate Note (FRN) Pricing & Discount Margin Engine.
  6. Residual Income Persistence Decay Explorer ($\omega \in [0, 1]$).
  7. FCFF → FCFE Cash Flow Waterfall Bridge.
  8. Multinational Currency Translation Engine (Current Rate vs. Temporal Method).
  9. MBS Prepayment Simulator & Contraction/Extension Risk Engine.
- **Audit & Compliance**:
  - Currency strictly formatted with `USD`, `EUR`, `GBP` or `\$`.
  - KaTeX delimiters balanced and error-free: 0 schema errors, 0 distractor errors, 0 KaTeX errors.
- **Live Deployment & Repositories**:
  - **GitHub Repository**: https://github.com/rahulxcodex/cfa-master-suite (main branch)
  - **Live GitHub Pages URL**: https://rahulxcodex.github.io/cfa-master-suite/
  - **Live Fixed Income & Equity Dashboard**: https://rahulxcodex.github.io/cfa-master-suite/fi_eq_dashboard.html
  - **Vercel Configuration**: `vercel.json` deployed to repository; production link ready for Vercel import/CLI sync.
