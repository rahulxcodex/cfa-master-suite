# Project Context: Finance Workspace (CFA Master Suite)

- **Workspace Path**: `c:\Users\Rahul\Documents\antigravity\Finance`
- **Domain**: CFA Program Exam Prep (Level 1 & Level 2), covering Financial Statement Analysis (FSA), Fixed Income, Equity Investments, and Portfolio Management.
- **Architecture**: Unified Single-Page Application (SPA) Portal at `index.html` (2.42 MB) with backward-compatibility redirect at `fi_eq_dashboard.html`.
- **Total Questions**: **1,085 Certified Questions** across 4 modules:
  - **Financial Statement Analysis**: 460 Questions (190 L1 MCQs + 270 L2 Questions across 48 vignettes)
  - **Fixed Income**: 205 Questions (120 L1 MCQs + 85 L2 Questions across 17 vignettes)
  - **Equity Investments**: 210 Questions (115 L1 MCQs + 95 L2 Questions across 19 vignettes)
  - **Portfolio Management**: 210 Questions (120 L1 MCQs + 90 L2 Questions across 18 vignettes)
  - **Level Breakdown**: 545 Level 1 MCQs, 540 Level 2 Questions across 102 distinct vignettes.
- **Core Deliverables**:
  - `index.html`: Unified CFA Master Dashboard housing all 1,085 questions, 102 vignette item sets, 12 simulation engines, 4-subject curriculum reference library with KaTeX & Chart.js, and question type calculation filters.
  - `fi_eq_dashboard.html`: Zero-latency redirect page forwarding legacy bookmarks to `index.html`.
  - `data/cfa_master_855.json`: Consolidated, normalized master JSON dataset (2.23 MB, 1,085 questions).
  - Reference Libraries:
    - `data/fsa_reference_extracted.html`: 20-chapter accounting mechanics & formula sheet (65 KB).
    - `data/fi_reference_extracted.html`: 8-module fixed income notes & formulas (22 KB).
    - `data/eq_reference_extracted.html`: 8-module equity valuation library & models (19 KB).
    - `data/pm_reference_extracted.html`: 8-module portfolio management library, institutional matrix & worked numericals (64 KB).
  - `scripts/`:
    - `compile_unified_suite.py`: Multi-source dataset compiler and validator.
    - `generate_notes_libraries.py`: Multi-subject curriculum notes compiler.
    - `generate_unified_dashboard.py`: Unified HTML dashboard generation engine.
    - `verify_unified_suite.py`: Strict schema, KaTeX parity, and stray dollar verifier.
- **Interactive Simulations (12 Total)**:
  1. Yield Curve Shift, Twist & Butterfly Simulator.
  2. Binomial Interest Rate Tree & Embedded Option Backward Induction Engine.
  3. Equity Valuation: Two-Stage DDM & DuPont Explorer.
  4. Key Rate Duration & Sensitivity Visualizer.
  5. Floating-Rate Note (FRN) Pricing & Discount Margin Engine.
  6. Residual Income Persistence Decay Explorer ($\omega \in [0, 1]$).
  7. FCFF -> FCFE Cash Flow Waterfall Bridge.
  8. Multinational Currency Translation Engine (Current Rate vs. Temporal Method).
  9. MBS Prepayment Simulator & Contraction/Extension Risk Engine.
  10. Markowitz Mean-Variance Frontier & CAL/Indifference Curve Optimizer.
  11. Grinold's Fundamental Law of Active Management ($IR = TC \times IC \times \sqrt{BR}$) & Sharpe Expansion Engine.
  12. Dynamic Rebalancing Corridors & Tolerance Band Simulation Engine.
- **Compliance & Auditing**:
  - Currency strictly formatted with `USD`, `EUR`, `GBP` or `\$`.
  - 100% KaTeX delimiter balance (0 unpaired delimiters, 0 stray dollars outside math blocks).
  - 0 schema errors across all 1,085 questions and 102 item sets.
  - 48.5% numerical calculation question density across all 4 subjects.
  - Full 4-Subject Curriculum Reference Library with 4-tab instant switcher bar.
  - Question Type filter pills ("All", "Numericals", "Theory") across L1 and L2 portals.
- **Live Deployment & Repositories**:
  - **GitHub Repository**: https://github.com/rahulxcodex/cfa-master-suite (main branch)
  - **Live Portal**: https://rahulxcodex.github.io/cfa-master-suite/

