#!/usr/bin/env python3
"""
scripts/enhance_dashboard_suite.py
Applies Anti-AI Design principles, desktop sidebar collapse, and integrates the master
solved numericals and curriculum audit sections into scripts/generate_unified_dashboard.py
and regenerates index.html.
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")
DATA_DIR = os.path.join(BASE_DIR, "data")
GEN_SCRIPT = os.path.join(SCRIPTS_DIR, "generate_unified_dashboard.py")
NUMERICALS_JSON = os.path.join(DATA_DIR, "master_solved_numericals.json")

assert os.path.exists(GEN_SCRIPT), f"Missing {GEN_SCRIPT}"
assert os.path.exists(NUMERICALS_JSON), f"Missing {NUMERICALS_JSON}"

with open(NUMERICALS_JSON, "r", encoding="utf-8") as f:
    numericals_data = json.load(f)

print(f"Loaded {len(numericals_data)} solved numericals.")

with open(GEN_SCRIPT, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Typography & Fonts
font_link = '''  <!-- Anti-AI Design: Editorial Serif, Humanist UI & Financial Monospace Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400;1,6..72,600&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">'''

if "Newsreader" not in content:
    content = content.replace("<!-- KaTeX for crisp LaTeX math rendering -->", font_link + "\n\n  <!-- KaTeX for crisp LaTeX math rendering -->")

# 2. Update CSS Variables & Design Tokens (Anti-AI Design / Financial Editorial)
old_css_root = """:root {
      --bg-primary: #0d1117;
      --bg-secondary: #161b22;
      --bg-tertiary: #21262d;
      --border-color: #30363d;
      --text-primary: #e6edf3;
      --text-secondary: #8b949e;
      --accent-blue: #58a6ff;
      --accent-cyan: #39c5cf;
      --accent-emerald: #3fb950;
      --accent-amber: #d29922;
      --accent-rose: #f85149;
      --accent-purple: #bc8cff;
      --code-bg: #1f242c;
      --sidebar-width: 290px;
    }

    [data-theme="light"] {
      --bg-primary: #ffffff;
      --bg-secondary: #f6f8fa;
      --bg-tertiary: #eaeef2;
      --border-color: #d0d7de;
      --text-primary: #1f2328;
      --text-secondary: #656d76;
      --accent-blue: #0969da;
      --accent-cyan: #0598ab;
      --accent-emerald: #1a7f37;
      --accent-amber: #9a6700;
      --accent-rose: #cf222e;
      --accent-purple: #8250df;
      --code-bg: #f3f4f6;
    }"""

new_css_root = """:root {
      /* Anti-AI Design: Disciplined Obsidian & Financial Terminal Tokens */
      --bg-primary: #090c14;
      --bg-secondary: #0f1420;
      --bg-tertiary: #171e2e;
      --border-color: #222b3e;
      --border-subtle: #1a2233;
      --text-primary: #f0f4f9;
      --text-secondary: #8a98ad;
      --text-muted: #576579;
      --accent-blue: #3b82f6;
      --accent-cyan: #0891b2;
      --accent-emerald: #10b981;
      --accent-amber: #d97706;
      --accent-rose: #ef4444;
      --accent-purple: #7c3aed;
      --code-bg: #121826;
      --sidebar-width: 285px;
      
      --font-serif: 'Newsreader', Iowan Old Style, Charter, Georgia, serif;
      --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      --font-mono: 'JetBrains Mono', SFMono-Regular, Consolas, monospace;
    }

    [data-theme="light"] {
      /* Anti-AI Design: Warm Financial Editorial Newsprint Tokens */
      --bg-primary: #fbfbfa;
      --bg-secondary: #f3f0ea;
      --bg-tertiary: #e7e3d8;
      --border-color: #d7d1c3;
      --border-subtle: #e4dec0;
      --text-primary: #14171d;
      --text-secondary: #586071;
      --text-muted: #828a99;
      --accent-blue: #1d4ed8;
      --accent-cyan: #0e7490;
      --accent-emerald: #047857;
      --accent-amber: #b45309;
      --accent-rose: #b91c1c;
      --accent-purple: #6d28d9;
      --code-bg: #ebe7de;
    }"""

if old_css_root in content:
    content = content.replace(old_css_root, new_css_root)

# 3. Update Global Body Font
old_body_font = """body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans", Helvetica, Arial, sans-serif, "Segoe UI Emoji", "Apple Color Emoji", "Noto Color Emoji";"""

new_body_font = """body {
      font-family: var(--font-sans);"""

if old_body_font in content:
    content = content.replace(old_body_font, new_body_font)

# 4. Add Collapsible Sidebar CSS and Editorial Headings
additional_css = """
    /* Editorial Typography & Anti-AI Design Hierarchy */
    h1, h2, h3, .editorial-heading, .vignette-title, .modal-title {
      font-family: var(--font-serif);
      letter-spacing: -0.015em;
    }
    
    .stats-pills, .stat-pill, .nav-badge, .badge, .mono-data, .formula-block, pre, code {
      font-family: var(--font-mono);
      font-feature-settings: "tnum" 1, "zero" 1;
    }

    /* Desktop Collapsible Sidebar Mechanism */
    aside#appSidebar {
      transition: margin-left 0.22s cubic-bezier(0.16, 1, 0.3, 1), transform 0.22s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    body.sidebar-collapsed aside#appSidebar {
      margin-left: calc(-1 * var(--sidebar-width));
    }
    
    body.sidebar-collapsed main {
      width: 100vw;
      max-width: 100vw;
      padding-left: 55px;
      padding-right: 55px;
    }
    
    .btn-collapse-sidebar {
      background: transparent;
      border: 1px solid var(--border-color);
      color: var(--text-secondary);
      font-size: 11px;
      font-family: var(--font-mono);
      font-weight: 500;
      padding: 3px 8px;
      border-radius: 4px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      transition: all 0.15s ease;
    }
    .btn-collapse-sidebar:hover {
      background: var(--bg-tertiary);
      color: var(--text-primary);
      border-color: var(--accent-blue);
    }

    /* Solved Numericals Styling */
    .numerical-card {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: 6px;
      padding: 24px;
      margin-bottom: 24px;
      transition: border-color 0.15s ease;
    }
    .numerical-card:hover {
      border-color: var(--accent-blue);
    }
    .numerical-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 14px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--border-color);
    }
    .numerical-title {
      font-family: var(--font-serif);
      font-size: 20px;
      font-weight: 600;
      color: var(--text-primary);
    }
    .numerical-meta {
      display: flex;
      gap: 8px;
      align-items: center;
    }
    .badge-diff-easy {
      background: rgba(16, 185, 129, 0.12);
      color: var(--accent-emerald);
      border: 1px solid rgba(16, 185, 129, 0.3);
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 11px;
      font-family: var(--font-mono);
      font-weight: 600;
    }
    .badge-diff-moderate {
      background: rgba(217, 119, 6, 0.12);
      color: var(--accent-amber);
      border: 1px solid rgba(217, 119, 6, 0.3);
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 11px;
      font-family: var(--font-mono);
      font-weight: 600;
    }
    .badge-diff-difficult {
      background: rgba(239, 68, 68, 0.12);
      color: var(--accent-rose);
      border: 1px solid rgba(239, 68, 68, 0.3);
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 11px;
      font-family: var(--font-mono);
      font-weight: 600;
    }
    .numerical-section-label {
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--text-muted);
      margin-top: 14px;
      margin-bottom: 6px;
    }
    .numerical-box-problem {
      font-size: 14.5px;
      line-height: 1.65;
      color: var(--text-primary);
      margin-bottom: 12px;
    }
    .numerical-box-formula {
      background: var(--code-bg);
      border-left: 3px solid var(--accent-blue);
      padding: 12px 16px;
      font-family: var(--font-mono);
      font-size: 13px;
      line-height: 1.6;
      border-radius: 0 4px 4px 0;
      margin-bottom: 14px;
      white-space: pre-wrap;
    }
    .numerical-box-steps {
      background: var(--bg-tertiary);
      border: 1px solid var(--border-color);
      border-radius: 4px;
      padding: 16px;
      font-size: 13.5px;
      line-height: 1.65;
      margin-bottom: 14px;
      white-space: pre-wrap;
    }
    .numerical-box-answer {
      background: rgba(16, 185, 129, 0.08);
      border: 1px solid var(--accent-emerald);
      border-radius: 4px;
      padding: 12px 16px;
      font-size: 14px;
      font-weight: 600;
      color: var(--accent-emerald);
      margin-bottom: 10px;
    }
"""

if "btn-collapse-sidebar" not in content:
    content = content.replace("  </style>\n</head>", additional_css + "\n  </style>\n</head>")

# 5. Update Sidebar Header with Collapse Button
old_sidebar_header = """    <div class="sidebar-header" style="display: flex; justify-content: space-between; align-items: flex-start;">
      <div>
        <h1>🎓 CFA Master Platform</h1>
        <p>Unified Exam Suite (875 Questions)</p>
      </div>
      <button class="btn-top sidebar-close-btn" onclick="closeMobileNav()" title="Close Menu">✕</button>
    </div>"""

new_sidebar_header = """    <div class="sidebar-header" style="display: flex; justify-content: space-between; align-items: flex-start;">
      <div>
        <h1 style="font-family: var(--font-serif); font-size: 19px; letter-spacing: -0.02em;">CFA Master Suite</h1>
        <p style="font-family: var(--font-mono); font-size: 11px; color: var(--text-secondary); margin-top: 3px;">1,085 Certified Questions</p>
      </div>
      <div style="display: flex; gap: 4px; align-items: center;">
        <button class="btn-collapse-sidebar" onclick="toggleDesktopSidebar()" title="Collapse Left Sidebar (Ctrl+B)">◀ Collapse</button>
        <button class="btn-top sidebar-close-btn" onclick="closeMobileNav()" title="Close Menu">✕</button>
      </div>
    </div>"""

if old_sidebar_header in content:
    content = content.replace(old_sidebar_header, new_sidebar_header)

# 6. Add Nav Links for Solved Numericals & Curriculum Audit
nav_insert_point = """      <li><a href="#overview" class="active" onclick="switchTab('overview')"><span>📊 Overview & Telemetry</span></a></li>
      <li><a href="#l1-practice" onclick="switchTab('l1-practice')"><span>📝 Level 1 Question Bank</span> <span class="nav-badge">545 Q</span></a></li>
      <li><a href="#l2-vignettes" onclick="switchTab('l2-vignettes')"><span>📑 Level 2 Case Vignettes</span> <span class="nav-badge">102 V / 540 Q</span></a></li>"""

new_nav_links = """      <li><a href="#overview" class="active" onclick="switchTab('overview')"><span>Overview & Telemetry</span></a></li>
      <li><a href="#l1-practice" onclick="switchTab('l1-practice')"><span>Level 1 Question Bank</span> <span class="nav-badge">545 Q</span></a></li>
      <li><a href="#l2-vignettes" onclick="switchTab('l2-vignettes')"><span>Level 2 Case Vignettes</span> <span class="nav-badge">102 V / 540 Q</span></a></li>
      
      <li class="nav-divider"><span>PRACTICE & WORKED SOLUTIONS</span></li>
      <li><a href="#solved-numericals" onclick="switchTab('solved-numericals')"><span>Master Solved Numericals</span> <span class="nav-badge" style="color: var(--accent-amber); border-color: var(--accent-amber);">27 Worked</span></a></li>
      <li><a href="#curriculum-audit" onclick="switchTab('curriculum-audit')"><span>Curriculum Audit & Gaps</span> <span class="nav-badge">2024–2026</span></a></li>"""

if nav_insert_point in content:
    content = content.replace(nav_insert_point, new_nav_links)

# 7. Update Top Bar to add Sidebar Toggle Button
old_top_bar_btn = """        <button class="menu-toggle-btn" id="menuToggleBtn" onclick="toggleMobileNav()" aria-label="Toggle Navigation">☰ Menu</button>"""

new_top_bar_btn = """        <button class="btn-top" id="desktopSidebarToggle" onclick="toggleDesktopSidebar()" title="Toggle Sidebar (Ctrl+B)" style="display: inline-flex; align-items: center; gap: 5px;">☰ <span>Sidebar</span></button>
        <button class="menu-toggle-btn" id="menuToggleBtn" onclick="toggleMobileNav()" aria-label="Toggle Navigation">☰ Menu</button>"""

if old_top_bar_btn in content and "desktopSidebarToggle" not in content:
    content = content.replace(old_top_bar_btn, new_top_bar_btn)

# 8. Create the HTML sections for Solved Numericals & Curriculum Audit
solved_numericals_section = r'''
    <!-- 13. MASTER SOLVED NUMERICALS & WORKED SOLUTIONS -->
    <section id="solved-numericals">
      <div class="card" style="margin-bottom: 24px; border-left: 4px solid var(--accent-amber);">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 16px;">
          <div>
            <h2 style="font-family: var(--font-serif); font-size: 26px; font-weight: 700; margin-bottom: 6px;">Master Solved Numericals & Worked Solutions</h2>
            <p style="color: var(--text-secondary); max-width: 850px; font-size: 13.5px;">
              Exhaustive step-by-step mathematical solutions graduated from Easy (Level 1 Foundational) to Moderate (Intermediate) to Difficult (Level 2 Multi-Step Item Sets) across Financial Statement Analysis, Fixed Income, Equity Investments, and Portfolio Management.
            </p>
          </div>
          <div style="text-align: right; font-family: var(--font-mono);">
            <div style="font-size: 24px; font-weight: 700; color: var(--accent-amber);" id="numericalsCountDisplay">27 Problems</div>
            <div style="font-size: 11px; color: var(--text-secondary);">100% KaTeX & Currency Verified</div>
          </div>
        </div>
      </div>

      <!-- Filter Bar -->
      <div class="filter-bar" style="margin-bottom: 20px; display: flex; flex-direction: column; gap: 12px;">
        <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
          <span style="font-family: var(--font-mono); font-size: 11px; text-transform: uppercase; color: var(--text-muted); font-weight: 700; margin-right: 4px;">Subject:</span>
          <button class="filter-btn active" id="numSubj-all" onclick="filterNumericals('all', currentNumDiff)">All Subjects</button>
          <button class="filter-btn" id="numSubj-fsa" onclick="filterNumericals('Financial Statement Analysis', currentNumDiff)">FSA (9)</button>
          <button class="filter-btn" id="numSubj-fi" onclick="filterNumericals('Fixed Income', currentNumDiff)">Fixed Income (6)</button>
          <button class="filter-btn" id="numSubj-eq" onclick="filterNumericals('Equity Investments', currentNumDiff)">Equity (6)</button>
          <button class="filter-btn" id="numSubj-pm" onclick="filterNumericals('Portfolio Management', currentNumDiff)">Portfolio Mgmt (6)</button>
        </div>
        <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
          <span style="font-family: var(--font-mono); font-size: 11px; text-transform: uppercase; color: var(--text-muted); font-weight: 700; margin-right: 4px;">Difficulty:</span>
          <button class="filter-btn active" id="numDiff-all" onclick="filterNumericals(currentNumSubj, 'all')">All Tiers</button>
          <button class="filter-btn" id="numDiff-easy" onclick="filterNumericals(currentNumSubj, 'easy')">Easy (L1)</button>
          <button class="filter-btn" id="numDiff-mod" onclick="filterNumericals(currentNumSubj, 'moderate')">Moderate</button>
          <button class="filter-btn" id="numDiff-diff" onclick="filterNumericals(currentNumSubj, 'difficult')">Difficult (L2 Vignette)</button>
          <input type="text" id="numSearchInput" placeholder="Filter by concept, formula or term (e.g. EPS, LIFO, Duration, H-Model, Perold)..." style="flex: 1 1 250px; min-width: 200px; padding: 7px 12px; background: var(--bg-tertiary); border: 1px solid var(--border-color); color: var(--text-primary); border-radius: 4px; font-size: 13px; font-family: var(--font-sans);" oninput="filterNumericals(currentNumSubj, currentNumDiff, this.value)">
        </div>
      </div>

      <!-- Container -->
      <div id="numericalsListContainer">
        <!-- Rendered via JS -->
      </div>
    </section>

    <!-- 14. CURRICULUM AUDIT & GAPS -->
    <section id="curriculum-audit">
      <div class="card" style="margin-bottom: 24px; border-left: 4px solid var(--accent-blue);">
        <h2 style="font-family: var(--font-serif); font-size: 26px; font-weight: 700; margin-bottom: 6px;">2024–2026 CFA Curriculum Completeness Audit</h2>
        <p style="color: var(--text-secondary); max-width: 900px; font-size: 13.5px; line-height: 1.6;">
          Authoritative syllabus gap analysis benchmarking this master platform against the official CFA Institute 2024–2026 curriculum and third-party preparation materials (Kaplan SchweserNotes and Wiley/UWorld).
        </p>
      </div>

      <!-- Macro 10-Topic Matrix -->
      <div class="card" style="margin-bottom: 24px;">
        <h3 style="font-family: var(--font-serif); font-size: 19px; margin-bottom: 14px;">Full 10-Topic CFA Program Scope Matrix</h3>
        <div style="overflow-x: auto;">
          <table style="width: 100%; border-collapse: collapse; font-size: 13px;">
            <thead>
              <tr style="border-bottom: 2px solid var(--border-color); text-align: left;">
                <th style="padding: 10px; font-family: var(--font-mono);">Topic Area</th>
                <th style="padding: 10px; font-family: var(--font-mono);">L1 Weight</th>
                <th style="padding: 10px; font-family: var(--font-mono);">L2 Weight</th>
                <th style="padding: 10px; font-family: var(--font-mono);">Master Suite Status</th>
                <th style="padding: 10px; font-family: var(--font-mono);">Coverage & Questions</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom: 1px solid var(--border-color); background: rgba(16, 185, 129, 0.05);">
                <td style="padding: 10px; font-weight: 600;">Financial Statement Analysis (FSA)</td>
                <td style="padding: 10px; font-family: var(--font-mono);">11%–14%</td>
                <td style="padding: 10px; font-family: var(--font-mono);">10%–15%</td>
                <td style="padding: 10px;"><span class="badge-diff-easy">COVERED</span></td>
                <td style="padding: 10px; color: var(--accent-emerald);">460 Questions (190 L1 + 270 L2)</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-color); background: rgba(16, 185, 129, 0.05);">
                <td style="padding: 10px; font-weight: 600;">Fixed Income (FI)</td>
                <td style="padding: 10px; font-family: var(--font-mono);">11%–14%</td>
                <td style="padding: 10px; font-family: var(--font-mono);">10%–15%</td>
                <td style="padding: 10px;"><span class="badge-diff-easy">COVERED</span></td>
                <td style="padding: 10px; color: var(--accent-emerald);">205 Questions (120 L1 + 85 L2)</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-color); background: rgba(16, 185, 129, 0.05);">
                <td style="padding: 10px; font-weight: 600;">Equity Investments (EQ)</td>
                <td style="padding: 10px; font-family: var(--font-mono);">11%–14%</td>
                <td style="padding: 10px; font-family: var(--font-mono);">10%–15%</td>
                <td style="padding: 10px;"><span class="badge-diff-easy">COVERED</span></td>
                <td style="padding: 10px; color: var(--accent-emerald);">210 Questions (115 L1 + 95 L2)</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-color); background: rgba(16, 185, 129, 0.05);">
                <td style="padding: 10px; font-weight: 600;">Portfolio Management (PM)</td>
                <td style="padding: 10px; font-family: var(--font-mono);">8%–12%</td>
                <td style="padding: 10px; font-family: var(--font-mono);">10%–15%</td>
                <td style="padding: 10px;"><span class="badge-diff-easy">COVERED</span></td>
                <td style="padding: 10px; color: var(--accent-emerald);">210 Questions (120 L1 + 90 L2)</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-color); opacity: 0.65;">
                <td style="padding: 10px;">Ethical & Professional Standards</td>
                <td style="padding: 10px; font-family: var(--font-mono);">15%–20%</td>
                <td style="padding: 10px; font-family: var(--font-mono);">10%–15%</td>
                <td style="padding: 10px;"><span class="badge-diff-difficult">OMITTED</span></td>
                <td style="padding: 10px;">Phase 2 Roadmap (Standards I–VII, GIPS)</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-color); opacity: 0.65;">
                <td style="padding: 10px;">Quantitative Methods</td>
                <td style="padding: 10px; font-family: var(--font-mono);">6%–9%</td>
                <td style="padding: 10px; font-family: var(--font-mono);">5%–10%</td>
                <td style="padding: 10px;"><span class="badge-diff-difficult">OMITTED</span></td>
                <td style="padding: 10px;">Phase 2 Roadmap (Time Series, Machine Learning)</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-color); opacity: 0.65;">
                <td style="padding: 10px;">Economics</td>
                <td style="padding: 10px; font-family: var(--font-mono);">6%–9%</td>
                <td style="padding: 10px; font-family: var(--font-mono);">5%–10%</td>
                <td style="padding: 10px;"><span class="badge-diff-difficult">OMITTED</span></td>
                <td style="padding: 10px;">Phase 2 Roadmap (FX Parity, Growth Economics)</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-color); opacity: 0.65;">
                <td style="padding: 10px;">Corporate Issuers</td>
                <td style="padding: 10px; font-family: var(--font-mono);">6%–9%</td>
                <td style="padding: 10px; font-family: var(--font-mono);">5%–10%</td>
                <td style="padding: 10px;"><span class="badge-diff-difficult">OMITTED</span></td>
                <td style="padding: 10px;">Phase 2 Roadmap (Capital Structure, Mergers)</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-color); opacity: 0.65;">
                <td style="padding: 10px;">Derivatives</td>
                <td style="padding: 10px; font-family: var(--font-mono);">5%–8%</td>
                <td style="padding: 10px; font-family: var(--font-mono);">5%–10%</td>
                <td style="padding: 10px;"><span class="badge-diff-difficult">OMITTED</span></td>
                <td style="padding: 10px;">Phase 2 Roadmap (Options BSM, Swaps)</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-color); opacity: 0.65;">
                <td style="padding: 10px;">Alternative Investments</td>
                <td style="padding: 10px; font-family: var(--font-mono);">7%–10%</td>
                <td style="padding: 10px; font-family: var(--font-mono);">5%–10%</td>
                <td style="padding: 10px;"><span class="badge-diff-difficult">OMITTED</span></td>
                <td style="padding: 10px;">Phase 2 Roadmap (Real Estate NAV, Private Equity)</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>
'''

main_close = '  </main>\n\n  <script>'
if main_close in content and 'id="solved-numericals"' not in content:
    content = content.replace(main_close, solved_numericals_section + '\n  </main>\n\n  <script>')

# 9. Embed Solved Numericals Data and JS functions
solved_numericals_json_escaped = json.dumps(numericals_data, ensure_ascii=False)

js_numericals_logic = """
    // Embedded Master Solved Numericals Bank
    const masterSolvedNumericals = """ + solved_numericals_json_escaped + """;

    let currentNumSubj = 'all';
    let currentNumDiff = 'all';
    let currentNumQuery = '';

    function toggleDesktopSidebar() {
      const isCollapsed = document.body.classList.toggle('sidebar-collapsed');
      localStorage.setItem('cfa_sidebar_collapsed', isCollapsed ? '1' : '0');
      const expandBtn = document.getElementById('desktopSidebarToggle');
      if (expandBtn) expandBtn.classList.toggle('active', isCollapsed);
    }

    // Initialize sidebar collapse state on startup
    if (localStorage.getItem('cfa_sidebar_collapsed') === '1') {
      document.body.classList.add('sidebar-collapsed');
    }

    // Keyboard shortcut: Ctrl+B or [ toggles sidebar
    window.addEventListener('keydown', (e) => {
      if ((e.ctrlKey && e.key.toLowerCase() === 'b') || (e.key === '[' && !['INPUT', 'TEXTAREA'].includes(e.target.tagName))) {
        e.preventDefault();
        toggleDesktopSidebar();
      }
    });

    function filterNumericals(subj, diff, query) {
      if (subj !== undefined) currentNumSubj = subj;
      if (diff !== undefined) currentNumDiff = diff;
      if (query !== undefined) currentNumQuery = query.toLowerCase().trim();

      // Update button active states
      document.querySelectorAll('#solved-numericals .filter-btn').forEach(btn => btn.classList.remove('active'));
      const subjId = currentNumSubj === 'all' ? 'numSubj-all' : 
                     currentNumSubj === 'Financial Statement Analysis' ? 'numSubj-fsa' :
                     currentNumSubj === 'Fixed Income' ? 'numSubj-fi' :
                     currentNumSubj === 'Equity Investments' ? 'numSubj-eq' : 'numSubj-pm';
      const diffId = currentNumDiff === 'all' ? 'numDiff-all' :
                     currentNumDiff === 'easy' ? 'numDiff-easy' :
                     currentNumDiff === 'moderate' ? 'numDiff-mod' : 'numDiff-diff';
      
      const sEl = document.getElementById(subjId);
      const dEl = document.getElementById(diffId);
      if (sEl) sEl.classList.add('active');
      if (dEl) dEl.classList.add('active');

      renderSolvedNumericals();
    }

    function renderSolvedNumericals() {
      const container = document.getElementById('numericalsListContainer');
      if (!container) return;

      const filtered = masterSolvedNumericals.filter(item => {
        const matchSubj = currentNumSubj === 'all' || item.subject === currentNumSubj;
        const matchDiff = currentNumDiff === 'all' || 
          (currentNumDiff === 'easy' && item.difficulty.toLowerCase().includes('easy')) ||
          (currentNumDiff === 'moderate' && item.difficulty.toLowerCase().includes('moderate')) ||
          (currentNumDiff === 'difficult' && item.difficulty.toLowerCase().includes('difficult'));
        
        let matchQuery = true;
        if (currentNumQuery) {
          const hay = (item.problem + ' ' + item.methodology + ' ' + item.steps + ' ' + item.final_answer + ' ' + item.subject).toLowerCase();
          matchQuery = hay.includes(currentNumQuery);
        }
        return matchSubj && matchDiff && matchQuery;
      });

      const countDisplay = document.getElementById('numericalsCountDisplay');
      if (countDisplay) {
        countDisplay.innerText = `${filtered.length} of ${masterSolvedNumericals.length} Problems`;
      }

      if (filtered.length === 0) {
        container.innerHTML = `
          <div class="card" style="text-align: center; padding: 40px; color: var(--text-secondary);">
            <p style="font-size: 16px;">No solved numericals match your selected filter criteria.</p>
            <button class="filter-btn" style="margin-top: 12px;" onclick="filterNumericals('all', 'all', '')">Reset Filters</button>
          </div>
        `;
        return;
      }

      container.innerHTML = filtered.map(item => {
        let diffBadge = '';
        if (item.difficulty.toLowerCase().includes('easy')) {
          diffBadge = `<span class="badge-diff-easy">Level 1: Easy / Foundational</span>`;
        } else if (item.difficulty.toLowerCase().includes('moderate')) {
          diffBadge = `<span class="badge-diff-moderate">Level 1/2: Moderate / Intermediate</span>`;
        } else {
          diffBadge = `<span class="badge-diff-difficult">Level 2: Difficult / Vignette Multi-Step</span>`;
        }

        return `
          <div class="numerical-card" id="${item.id}">
            <div class="numerical-header">
              <div>
                <div style="font-family: var(--font-mono); font-size: 11px; text-transform: uppercase; color: var(--accent-blue); font-weight: 700; margin-bottom: 3px;">${item.subject}</div>
                <div class="numerical-title">Case Problem ${item.num_code}</div>
              </div>
              <div class="numerical-meta">
                ${diffBadge}
              </div>
            </div>

            <div class="numerical-section-label">Problem Statement:</div>
            <div class="numerical-box-problem">${item.problem}</div>

            <div class="numerical-section-label">Methodology & Governing Formulas:</div>
            <div class="numerical-box-formula">${item.methodology}</div>

            <div class="numerical-section-label">Step-by-Step Calculation:</div>
            <div class="numerical-box-steps">${item.steps}</div>

            <div class="numerical-section-label">Final Verified Answer:</div>
            <div class="numerical-box-answer">${item.final_answer}</div>
          </div>
        `;
      }).join('');

      // Trigger KaTeX render if available
      if (window.renderMathInElement) {
        renderMathInElement(container, {
          delimiters: [
            {left: "$$", right: "$$", display: true},
            {left: "$", right: "$", display: false}
          ],
          throwOnError: false
        });
      }
    }
"""

template_script_close = "      });\n    });\n  </script>\n</body>\n</html>\n'''"
if template_script_close in content and "masterSolvedNumericals" not in content:
    content = content.replace(template_script_close, js_numericals_logic + "\n      });\n    });\n  </script>\n</body>\n</html>\n'''")

# Update switchTab dictionary to include the 2 new tabs
old_titles_block = """        'pm-reference': 'Portfolio Management Master Reference & Formulas (8 Modules)',
        'reference-diagrams': 'Visual Frameworks & Cheat Sheets'
      };"""

new_titles_block = """        'pm-reference': 'Portfolio Management Master Reference & Formulas (8 Modules)',
        'reference-diagrams': 'Visual Frameworks & Cheat Sheets',
        'solved-numericals': 'Master Solved Numericals & Worked Solutions (27 Cases)',
        'curriculum-audit': '2024–2026 CFA Curriculum Completeness Audit & Gaps'
      };"""

if old_titles_block in content:
    content = content.replace(old_titles_block, new_titles_block)

# Ensure renderSolvedNumericals is called on switchTab
old_switch_tab_end = """      document.getElementById('topTitle').innerHTML = `<h2>${titles[tabId] || 'CFA Master Suite'}</h2>`;"""

new_switch_tab_end = """      document.getElementById('topTitle').innerHTML = `<h2>${titles[tabId] || 'CFA Master Suite'}</h2>`;
      if (tabId === 'solved-numericals') {
        renderSolvedNumericals();
      }"""

if old_switch_tab_end in content and "if (tabId === 'solved-numericals')" not in content:
    content = content.replace(old_switch_tab_end, new_switch_tab_end)

with open(GEN_SCRIPT, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully updated {GEN_SCRIPT} with Anti-AI Design tokens, sidebar collapse, and solved numericals!")
