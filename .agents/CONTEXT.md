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
  - `index.html`: Unified CFA Master Dashboard (2.50 MB) housing all 1,085 questions, 102 vignette item sets, 12 simulation engines, 27 master solved numerical cases, 2024-2026 curriculum audit matrix, desktop collapsible sidebar, and Anti-AI Design typography.
  - `fi_eq_dashboard.html`: Zero-latency redirect page forwarding legacy bookmarks to `index.html`.
  - `CFA_CURRICULUM_AUDIT_AND_SOLVED_NUMERICALS.md`: Exhaustive 77KB audit and multi-tier worked problems.
  - `data/master_solved_numericals.json`: Normalized dataset of 27 multi-step solved numericals.
  - `data/cfa_master_855.json`: Consolidated master question bank (1,085 questions).
  - Reference Libraries:
    - `data/fsa_reference_extracted.html`: 20-chapter accounting mechanics & formula sheet (65 KB).
    - `data/fi_reference_extracted.html`: 8-module fixed income notes & formulas (22 KB).
    - `data/eq_reference_extracted.html`: 8-module equity valuation library & models (19 KB).
    - `data/pm_reference_extracted.html`: 8-module portfolio management library, institutional matrix & worked numericals (64 KB).
  - `scripts/`:
    - `generate_unified_dashboard.py`: Unified dashboard compiler with Anti-AI Design tokens and sidebar collapse.
    - `verify_unified_suite.py`: Strict schema, KaTeX parity, and stray dollar verifier.
  - `data/cfa_jargon_dictionary.json`: Comprehensive 32-term database with intuitive definitions, KaTeX formulas, practical uses, exam traps, and worked step-by-step numericals.
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
  - **Recent Milestones**:
    - Sidebar scope fix: resolved unclosed `hashchange` listener in `scripts/generate_unified_dashboard.py` restoring global access to `toggleDesktopSidebar`, `filterNumericals`, and `renderSolvedNumericals`.
    - Mobile UI responsiveness: hid duplicate desktop sidebar toggle on screens <= 900px, isolated mobile close button, and prevented sidebar drawer offset on mobile viewports.
    - Terminology & Jargon Interactive Popover System: Architected with Gemini 4 (Argon High Thinking) via `/gemini4web`. Added 32 comprehensive CFA Level 1 & Level 2 terminologies across FSA, FI, EQ, PM with intuitive definitions, KaTeX formulas, practical uses, common pitfalls, worked step-by-step numerical examples, history stack back navigation, mobile bottom-sheet fallback, and automatic DOM tree-walker highlighting.
    - 2026–2027 CFA CBOK Curriculum Audit & 50 Inline Notes Worked Numericals: Audited all 4 portal topics against official CFA Institute CBOK (`cfainstitute.org/.../cbok`), 2026–2027 L1/L2 syllabi, and Kaplan SchweserNotes; closed subtopic gaps across FSA (Off-Balance-Sheet VIEs, Share-Based Comp, IAS 29 Hyperinflation, Sustainability/ISSB, 3-Statement Modeling), Fixed Income (Repo/Shorting, Convertibles, Vasicek/CIR/Ho-Lee/KWF term structure models, CDS Upfront/Basis, Covered Bonds, Green/SLBs, Empirical Duration), Equities (Shorting/Short Margin Call, 2027 L1 12-module Forecasting/Jurisdictions/Research Reports/Cost of Equity, EMH, Harmonic Mean, SOTP, Clean Surplus/EVA, EEM), and Portfolio Construction (Endowment Spending, 3-Asset Variance, Behavioral Biases, Economics & Investment Markets, Brinson-Fachler Attribution, VaR/CVaR, Backtesting & Simulation, Technical Analysis, Fintech/ML/DLT, ESG & 130/30 Shorting); embedded 50 inline Schweser-style Worked Numerical Examples (14 FSA, 11 FI, 11 EQ, 14 PM) directly inside Reference Notes; updated `#curriculum-audit` to official 2027 CBOK weights & simultaneous L1/L2 critique.

