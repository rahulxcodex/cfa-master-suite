# Project Context: Finance Workspace (CFA Master Suite)

- **Workspace Path**: `c:\Users\Rahul\Documents\antigravity\Finance`
- **Domain**: CFA Program Exam Prep (Level 1 & Level 2), covering Financial Statement Analysis (FSA), Fixed Income, and Equity Investments.
- **Architecture**: Unified Single-Page Application (SPA) Portal at `index.html` (1.87 MB) with backward-compatibility redirect at `fi_eq_dashboard.html`.
- **Total Questions**: **855 Certified Questions** across 3 modules:
  - **Financial Statement Analysis**: 440 Questions (190 L1 MCQs + 250 L2 Questions across 44 vignettes)
  - **Fixed Income**: 205 Questions (120 L1 MCQs + 85 L2 Questions across 17 vignettes)
  - **Equity Investments**: 210 Questions (115 L1 MCQs + 95 L2 Questions across 19 vignettes)
  - **Level Breakdown**: 425 Level 1 MCQs, 430 Level 2 Questions across 80 distinct vignettes.
- **Core Deliverables**:
  - `index.html`: Unified CFA Master Dashboard housing all 855 questions, 80 vignette item sets, 9 simulation engines, and full 20-chapter FSA reference library with KaTeX & Chart.js.
  - `fi_eq_dashboard.html`: Zero-latency redirect page forwarding legacy bookmarks to `index.html`.
  - `data/cfa_master_855.json`: Consolidated, normalized master JSON dataset (1.90 MB, 855 questions).
  - `data/fsa_reference_extracted.html`: 65 KB extracted curriculum notes and formula sheets.
  - `scripts/`:
    - `compile_unified_suite.py`: Multi-source dataset compiler and validator.
    - `extract_fsa_notes.py`: FSA reference notes extractor.
    - `generate_unified_dashboard.py`: Unified HTML dashboard generation engine.
    - `verify_unified_suite.py`: Strict schema, KaTeX parity, and stray dollar verifier.
- **Interactive Simulations (9 Total)**:
  1. Yield Curve Shift, Twist & Butterfly Simulator.
  2. Binomial Interest Rate Tree & Embedded Option Backward Induction Engine.
  3. Equity Valuation: Two-Stage DDM & DuPont Explorer.
  4. Key Rate Duration & Sensitivity Visualizer.
  5. Floating-Rate Note (FRN) Pricing & Discount Margin Engine.
  6. Residual Income Persistence Decay Explorer ($\omega \in [0, 1]$).
  7. FCFF -> FCFE Cash Flow Waterfall Bridge.
  8. Multinational Currency Translation Engine (Current Rate vs. Temporal Method).
  9. MBS Prepayment Simulator & Contraction/Extension Risk Engine.
- **Compliance & Auditing**:
  - Currency strictly formatted with `USD`, `EUR`, `GBP` or `\$`.
  - 100% KaTeX delimiter balance (0 unpaired delimiters, 0 stray dollars outside math blocks).
  - 0 schema errors across all 855 questions and 80 item sets.
  - Full 20-chapter FSA notes section restored with complete CSS class coverage and 6 interactive Chart.js visualizations.
  - Mobile drawer navigation with responsive sidebar, backdrop overlay, and hamburger toggle.
- **Live Deployment & Repositories**:
  - **GitHub Repository**: https://github.com/rahulxcodex/cfa-master-suite (main branch)
  - **Live Portal**: https://rahulxcodex.github.io/cfa-master-suite/
