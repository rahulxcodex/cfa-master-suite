import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data", "fi_eq")
MASTER_JSON = os.path.join(DATA_DIR, "cfa_fi_eq_master.json")
OUTPUT_HTML = os.path.join(BASE_DIR, "fi_eq_dashboard.html")
BUILD_NOTES_PY = os.path.join(BASE_DIR, "build_fi_eq_notes.py")

with open(MASTER_JSON, "r", encoding="utf-8") as f:
    questions = json.load(f)

print(f"Loaded {len(questions)} questions from {MASTER_JSON}")

# Build the complete standalone HTML dashboard
dashboard_html_template = r'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CFA Level 1 & Level 2 Master Question Bank: Fixed Income & Equity Valuation</title>
  
  <!-- KaTeX for crisp LaTeX math rendering -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
  
  <!-- Chart.js for interactive simulations -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

  <style>
    :root {
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
      --sidebar-width: 300px;
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
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif;
      background-color: var(--bg-primary);
      color: var(--text-primary);
      display: flex;
      min-height: 100vh;
      font-size: 14px;
    }

    /* Sidebar Navigation */
    aside {
      width: var(--sidebar-width);
      background: var(--bg-secondary);
      border-right: 1px solid var(--border-color);
      display: flex;
      flex-direction: column;
      position: fixed;
      height: 100vh;
      z-index: 100;
    }
    .sidebar-header {
      padding: 20px;
      border-bottom: 1px solid var(--border-color);
    }
    .sidebar-header h1 {
      font-size: 16px;
      font-weight: 700;
      color: var(--accent-blue);
      letter-spacing: -0.3px;
    }
    .sidebar-header p {
      font-size: 11px;
      color: var(--text-secondary);
      margin-top: 4px;
    }
    .nav-links {
      list-style: none;
      padding: 15px;
      overflow-y: auto;
      flex-grow: 1;
    }
    .nav-links li { margin-bottom: 6px; }
    .nav-links a {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 9px 12px;
      color: var(--text-primary);
      text-decoration: none;
      border-radius: 6px;
      font-weight: 500;
      font-size: 13px;
      transition: background 0.15s, color 0.15s;
    }
    .nav-links a:hover, .nav-links a.active {
      background: var(--bg-tertiary);
      color: var(--accent-blue);
    }
    .nav-badge {
      margin-left: auto;
      font-size: 11px;
      background: var(--bg-primary);
      padding: 2px 7px;
      border-radius: 10px;
      border: 1px solid var(--border-color);
      color: var(--text-secondary);
    }

    /* Main Container */
    main {
      margin-left: var(--sidebar-width);
      flex-grow: 1;
      padding: 35px 50px;
      max-width: 1400px;
      overflow-y: auto;
    }

    .top-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 25px;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 15px;
    }
    .top-bar h2 {
      font-size: 22px;
      font-weight: 700;
      color: var(--text-primary);
    }
    .stats-pills {
      display: flex;
      gap: 12px;
      align-items: center;
    }
    .stat-pill {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 600;
    }
    .theme-toggle {
      background: var(--bg-tertiary);
      color: var(--text-primary);
      border: 1px solid var(--border-color);
      padding: 6px 12px;
      border-radius: 6px;
      cursor: pointer;
      font-weight: 600;
      font-size: 12px;
    }

    section { display: none; }
    section.active { display: block; animation: fadeIn 0.2s ease-in-out; }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(4px); } to { opacity: 1; transform: translateY(0); } }

    /* Cards & Layout */
    .card {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 24px;
      margin-bottom: 24px;
    }
    .card-title {
      font-size: 16px;
      font-weight: 700;
      margin-bottom: 12px;
      color: var(--accent-cyan);
    }
    .grid-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
    }
    .grid-3 {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 20px;
    }
    .grid-4 {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
    }

    /* Controls & Forms */
    .control-group { margin-bottom: 14px; }
    .control-group label {
      display: block;
      font-weight: 600;
      margin-bottom: 5px;
      color: var(--text-primary);
      font-size: 13px;
    }
    .control-group input[type="range"] {
      width: 100%;
      cursor: pointer;
    }
    .control-group select, .control-group input[type="text"], .control-group input[type="number"] {
      width: 100%;
      padding: 8px 12px;
      background: var(--bg-primary);
      border: 1px solid var(--border-color);
      color: var(--text-primary);
      border-radius: 6px;
      font-size: 13px;
    }
    .btn {
      background: var(--accent-blue);
      color: #fff;
      border: none;
      padding: 9px 18px;
      border-radius: 6px;
      font-weight: 600;
      cursor: pointer;
      font-size: 13px;
      transition: opacity 0.2s;
    }
    .btn:hover { opacity: 0.9; }
    .btn-secondary {
      background: var(--bg-tertiary);
      color: var(--text-primary);
      border: 1px solid var(--border-color);
    }

    /* Question UI */
    .question-box {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 24px;
      margin-bottom: 20px;
      position: relative;
    }
    .question-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }
    .question-id-badge {
      font-size: 12px;
      font-weight: 700;
      color: var(--accent-blue);
      background: var(--bg-primary);
      padding: 3px 8px;
      border-radius: 4px;
      border: 1px solid var(--border-color);
    }
    .question-los {
      font-size: 11px;
      color: var(--text-secondary);
      max-width: 70%;
      text-align: right;
    }
    .question-text {
      font-size: 15px;
      line-height: 1.6;
      font-weight: 500;
      margin-bottom: 18px;
    }
    .options-container {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .option-btn {
      display: flex;
      align-items: center;
      width: 100%;
      text-align: left;
      padding: 12px 18px;
      background: var(--bg-primary);
      border: 1px solid var(--border-color);
      color: var(--text-primary);
      border-radius: 6px;
      cursor: pointer;
      font-size: 14px;
      line-height: 1.5;
      transition: all 0.15s ease;
    }
    .option-btn:hover:not(:disabled) {
      border-color: var(--accent-blue);
      background: var(--bg-tertiary);
    }
    .option-btn.correct {
      background: rgba(63, 185, 80, 0.15) !important;
      border-color: var(--accent-emerald) !important;
      color: var(--accent-emerald) !important;
      font-weight: 600;
    }
    .option-btn.incorrect {
      background: rgba(248, 81, 73, 0.15) !important;
      border-color: var(--accent-rose) !important;
      color: var(--accent-rose) !important;
    }

    /* Explanation & Distractor Analysis */
    .explanation-box {
      margin-top: 20px;
      padding: 20px;
      background: var(--bg-primary);
      border-left: 4px solid var(--accent-cyan);
      border-radius: 6px;
      display: none;
    }
    .explanation-title {
      font-size: 14px;
      font-weight: 700;
      color: var(--accent-cyan);
      margin-bottom: 8px;
    }
    .distractor-box {
      margin-top: 14px;
      padding: 14px;
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: 6px;
      font-size: 13px;
    }
    .distractor-title {
      font-weight: 700;
      color: var(--accent-amber);
      margin-bottom: 6px;
    }

    /* Simulation node trees */
    .tree-grid {
      display: flex;
      justify-content: space-around;
      align-items: center;
      padding: 20px 0;
      background: var(--bg-primary);
      border-radius: 8px;
      border: 1px solid var(--border-color);
    }
    .tree-col {
      display: flex;
      flex-direction: column;
      gap: 20px;
      align-items: center;
    }
    .tree-node {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      padding: 10px 14px;
      border-radius: 6px;
      text-align: center;
      min-width: 110px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    .tree-node .node-rate { font-weight: 700; color: var(--accent-blue); font-size: 13px; }
    .tree-node .node-val { font-size: 11px; color: var(--accent-emerald); margin-top: 3px; }

    /* SVG Diagrams */
    .svg-container {
      width: 100%;
      background: var(--bg-primary);
      border-radius: 8px;
      border: 1px solid var(--border-color);
      padding: 15px;
      display: flex;
      justify-content: center;
      align-items: center;
    }
  </style>
</head>
<body>

  <!-- Sidebar Navigation -->
  <aside>
    <div class="sidebar-header">
      <h1>CFA Master Platform</h1>
      <p>Fixed Income & Equity Valuation (L1 & L2)</p>
    </div>
    <ul class="nav-links">
      <li><a href="#overview" class="active" onclick="switchTab('overview')"><span>📊 Overview & Analytics</span></a></li>
      <li><a href="#l1-practice" onclick="switchTab('l1-practice')"><span>📝 Level 1 Question Bank</span> <span class="nav-badge">170 Q</span></a></li>
      <li><a href="#l2-vignettes" onclick="switchTab('l2-vignettes')"><span>📑 Level 2 Case Vignettes</span> <span class="nav-badge">170 Q</span></a></li>
      <li><a href="#sim-yield" onclick="switchTab('sim-yield')"><span>📈 Yield Curve Simulator</span></a></li>
      <li><a href="#sim-tree" onclick="switchTab('sim-tree')"><span>🌳 Binomial Tree Engine</span></a></li>
      <li><a href="#sim-equity" onclick="switchTab('sim-equity')"><span>📊 DDM & DuPont Explorer</span></a></li>
      <li><a href="#sim-duration" onclick="switchTab('sim-duration')"><span>⚡ Key Rate Duration</span></a></li>
      <li><a href="#sim-frn" onclick="switchTab('sim-frn')"><span>🔢 FRN Pricing Engine</span></a></li>
      <li><a href="#sim-ri-decay" onclick="switchTab('sim-ri-decay')"><span>📉 RI Persistence Decay</span></a></li>
      <li><a href="#sim-waterfall" onclick="switchTab('sim-waterfall')"><span>🌊 FCFF→FCFE Waterfall</span></a></li>
      <li><a href="#sim-translation" onclick="switchTab('sim-translation')"><span>💱 Currency Translation</span></a></li>
      <li><a href="#sim-prepayment" onclick="switchTab('sim-prepayment')"><span>🏠 MBS Prepayment Simulator</span></a></li>
      <li><a href="#reference-diagrams" onclick="switchTab('reference-diagrams')"><span>📐 Visual Diagrams</span></a></li>
      <li style="margin-top: 15px; border-top: 1px solid var(--border-color); padding-top: 12px;">
        <a href="index.html" style="background: rgba(210, 153, 34, 0.1); color: var(--accent-amber); font-weight: 600; border: 1px solid rgba(210, 153, 34, 0.3);">
          <span>📚 Switch to FSA Master Suite →</span>
        </a>
      </li>
    </ul>
  </aside>

  <!-- Main Content -->
  <main>
    <div class="top-bar">
      <div id="topTitle">
        <h2>Curriculum Overview & Analytics</h2>
      </div>
      <div class="stats-pills">
        <a href="index.html" class="stat-pill" style="color: var(--accent-amber); text-decoration: none; border-color: rgba(210,153,34,0.4);">📚 View FSA Suite</a>
        <div class="stat-pill" style="color: var(--accent-blue);">Total: <span id="totalQuestionsDisplay">415</span> Questions</div>
        <div class="stat-pill" style="color: var(--accent-emerald);">Score: <span id="scoreDisplay">0 / 0 (0%)</span></div>
        <button class="theme-toggle" onclick="toggleTheme()">🌓 Theme</button>
      </div>
    </div>

    <!-- 1. OVERVIEW & METRICS -->
    <section id="overview" class="active">
      <div class="grid-4" style="margin-bottom: 24px;">
        <div class="card" style="margin-bottom: 0;">
          <div style="font-size: 12px; color: var(--text-secondary); text-transform: uppercase;">L1 Fixed Income</div>
          <div style="font-size: 28px; font-weight: 700; color: var(--accent-blue); margin-top: 5px;">85 MCQs</div>
          <div style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">6 Core Learning Modules</div>
        </div>
        <div class="card" style="margin-bottom: 0;">
          <div style="font-size: 12px; color: var(--text-secondary); text-transform: uppercase;">L1 Equity Investments</div>
          <div style="font-size: 28px; font-weight: 700; color: var(--accent-cyan); margin-top: 5px;">85 MCQs</div>
          <div style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">6 Core Learning Modules</div>
        </div>
        <div class="card" style="margin-bottom: 0;">
          <div style="font-size: 12px; color: var(--text-secondary); text-transform: uppercase;">L2 Fixed Income</div>
          <div style="font-size: 28px; font-weight: 700; color: var(--accent-purple); margin-top: 5px;">85 Questions</div>
          <div style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">17 Item Sets (5 Qs each)</div>
        </div>
        <div class="card" style="margin-bottom: 0;">
          <div style="font-size: 12px; color: var(--text-secondary); text-transform: uppercase;">L2 Equity Valuation</div>
          <div style="font-size: 28px; font-weight: 700; color: var(--accent-emerald); margin-top: 5px;">85 Questions</div>
          <div style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">17 Item Sets (5 Qs each)</div>
        </div>
      </div>

      <div class="card">
        <div class="card-title">CFA Exam Curriculum & Question Distribution</div>
        <div class="grid-2">
          <div>
            <canvas id="topicDistributionChart" height="200"></canvas>
          </div>
          <div style="display: flex; flex-direction: column; justify-content: center; gap: 12px; font-size: 13px;">
            <p style="margin-bottom: 0; color: var(--text-primary);"><strong style="color: var(--accent-blue);">Fixed Income Suite:</strong> Defining elements, money market discount vs add-on yields, spot rate bootstrapping, OAS, key rate duration, negative convexity, binomial lognormal trees, Merton structural credit models, and CDS upfront/basis trading.</p>
            <p style="margin-bottom: 0; color: var(--text-primary);"><strong style="color: var(--accent-cyan);">Equity Valuation Suite:</strong> Gordon Growth, H-Model, multistage DDM, FCFF vs FCFE derivations, residual income persistence, justified multiples, guideline transactions, and private company DLOC/DLOM compounding.</p>
            <p style="margin-bottom: 0; color: var(--text-secondary);">Audited and certified by Dual Senior CFA Charterholder Subagents (Auditor Alpha & Auditor Beta) across 4 rounds of debate.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 2. LEVEL 1 PRACTICE ENGINE -->
    <section id="l1-practice">
      <div class="card" style="padding: 16px 24px; margin-bottom: 20px;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 15px;">
          <div style="display: flex; gap: 15px; align-items: center;">
            <label style="font-weight: 600; font-size: 13px;">Subject Filter:</label>
            <select id="l1SubjectFilter" onchange="filterL1Questions()" style="width: 220px; padding: 6px 10px; background: var(--bg-primary); border: 1px solid var(--border-color); color: var(--text-primary); border-radius: 6px;">
              <option value="ALL">All Subjects (170 Questions)</option>
              <option value="Fixed Income">Fixed Income Only (85 Questions)</option>
              <option value="Equity">Equity Investments Only (85 Questions)</option>
            </select>
          </div>
          <div style="display: flex; gap: 10px;">
            <button class="btn btn-secondary" onclick="prevL1Question()">← Previous</button>
            <button class="btn btn-secondary" onclick="randomL1Question()">🎲 Random</button>
            <button class="btn" onclick="nextL1Question()">Next Question →</button>
          </div>
        </div>
      </div>

      <div id="l1QuestionContainer"></div>
    </section>

    <!-- 3. LEVEL 2 VIGNETTES -->
    <section id="l2-vignettes">
      <div class="card" style="padding: 16px 24px; margin-bottom: 20px;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 15px;">
          <div style="display: flex; gap: 15px; align-items: center; flex-grow: 1;">
            <label style="font-weight: 600; font-size: 13px; white-space: nowrap;">Select Case Study:</label>
            <select id="l2VignetteSelect" onchange="loadL2Vignette()" style="padding: 7px 12px; background: var(--bg-primary); border: 1px solid var(--border-color); color: var(--text-primary); border-radius: 6px; width: 100%; max-width: 600px;">
            </select>
          </div>
          <div style="font-size: 12px; color: var(--text-secondary);">
            34 Total Case Studies (17 FI + 17 EQ)
          </div>
        </div>
      </div>

      <div class="grid-2">
        <div class="card" id="vignetteTextCard" style="height: fit-content; max-height: 80vh; overflow-y: auto;">
          <!-- Vignette Narrative will load here -->
        </div>
        <div id="vignetteQuestionsCard">
          <!-- 5 Questions will load here -->
        </div>
      </div>
    </section>

    <!-- 4. SIMULATION: YIELD CURVE -->
    <section id="sim-yield">
      <div class="card">
        <div class="card-title">Interactive Yield Curve Dynamics & Term Structure Simulator</div>
        <p style="color: var(--text-secondary); margin-bottom: 20px;">
          Simulate yield curve movements: <strong>Shift (Level)</strong>, <strong>Twist (Slope)</strong>, and <strong>Butterfly (Curvature)</strong>. Inspect the mathematical relationship between the Par Curve, Spot Rates, and Forward Rates.
        </p>
        <div class="grid-2">
          <div>
            <canvas id="yieldChart" height="230"></canvas>
          </div>
          <div>
            <div class="control-group">
              <label>Parallel Shift (Level Shift): <span id="shiftVal" style="color: var(--accent-blue);">0 bps</span></label>
              <input type="range" id="shiftRange" min="-200" max="200" value="0" step="10" oninput="updateYieldSim()">
            </div>
            <div class="control-group">
              <label>Slope Twist (Steepening / Flattening): <span id="twistVal" style="color: var(--accent-emerald);">0 bps</span></label>
              <input type="range" id="twistRange" min="-150" max="150" value="0" step="10" oninput="updateYieldSim()">
            </div>
            <div class="control-group">
              <label>Butterfly Curvature (Hump Effect): <span id="butterflyVal" style="color: var(--accent-amber);">0 bps</span></label>
              <input type="range" id="butterflyRange" min="-100" max="100" value="0" step="10" oninput="updateYieldSim()">
            </div>
            <div style="margin-top: 15px; padding: 12px; background: var(--bg-primary); border-radius: 6px; border: 1px solid var(--border-color); font-size: 12px;">
              <strong>Term Structure Formula:</strong> 
              $$\left(1 + z_2\right)^2 = \left(1 + z_1\right)\left(1 + f_{1,1}\right)$$
              Forward rate is the break-even reinvestment rate between spot maturities.
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 5. SIMULATION: BINOMIAL INTEREST RATE TREE -->
    <section id="sim-tree">
      <div class="card">
        <div class="card-title">Binomial Interest Rate Tree & Embedded Option Valuation Engine</div>
        <p style="color: var(--text-secondary); margin-bottom: 20px;">
          Interactive backward induction on a lognormal interest rate tree. Evaluate a 3-Year 6.0% annual coupon bond with an embedded Call Option exercisable at 100 USD at Year 1 and Year 2.
        </p>
        <div class="grid-2">
          <div>
            <div class="control-group">
              <label>Annual Coupon Rate (%): <span id="treeCouponVal" style="color: var(--accent-blue);">6.0%</span></label>
              <input type="range" id="treeCoupon" min="2.0" max="10.0" value="6.0" step="0.25" oninput="updateTreeSim()">
            </div>
            <div class="control-group">
              <label>Lognormal Interest Rate Volatility ($\sigma$): <span id="treeVolVal" style="color: var(--accent-cyan);">15.0%</span></label>
              <input type="range" id="treeVol" min="5.0" max="30.0" value="15.0" step="1.0" oninput="updateTreeSim()">
            </div>
            <div class="control-group">
              <label>Call Price Cap (USD): <span id="treeCallVal" style="color: var(--accent-rose);">100.00 USD</span></label>
              <input type="range" id="treeCall" min="95.0" max="105.0" value="100.0" step="0.5" oninput="updateTreeSim()">
            </div>
            <div style="margin-top: 15px; padding: 15px; background: var(--bg-primary); border-radius: 6px; border: 1px solid var(--border-color);">
              <div style="font-size: 13px; font-weight: 700; margin-bottom: 8px;">Valuation Results:</div>
              <div id="treeResults" style="font-size: 13px; line-height: 1.8;">
                <!-- Output generated here -->
              </div>
            </div>
          </div>
          <div>
            <div style="font-weight: 600; margin-bottom: 10px; font-size: 13px;">Interest Rate Tree Visualization:</div>
            <div class="tree-grid" id="treeVisualContainer">
              <!-- Tree Nodes rendered here -->
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 6. SIMULATION: EQUITY DDM & DUPONT -->
    <section id="sim-equity">
      <div class="card">
        <div class="card-title">Equity Valuation: Two-Stage DDM & DuPont 5-Factor Decomposition</div>
        <p style="color: var(--text-secondary); margin-bottom: 20px;">
          Model transitions from high-growth to sustainable growth via Gordon Growth and the H-Model, and explore the DuPont 5-way breakdown of Return on Equity (ROE).
        </p>
        <div class="grid-2">
          <div>
            <div style="font-weight: 700; color: var(--accent-emerald); margin-bottom: 12px;">H-Model Valuation Explorer</div>
            <div class="control-group">
              <label>Base Dividend ($D_0$ in USD): <span id="ddmD0Val">2.50 USD</span></label>
              <input type="range" id="ddmD0" min="0.5" max="10.0" value="2.5" step="0.25" oninput="updateEquitySim()">
            </div>
            <div class="control-group">
              <label>Short-term Growth Rate ($g_S$ %): <span id="ddmGsVal">14.0%</span></label>
              <input type="range" id="ddmGs" min="5.0" max="25.0" value="14.0" step="0.5" oninput="updateEquitySim()">
            </div>
            <div class="control-group">
              <label>Long-term Growth Rate ($g_L$ %): <span id="ddmGlVal">4.0%</span></label>
              <input type="range" id="ddmGl" min="1.0" max="7.0" value="4.0" step="0.25" oninput="updateEquitySim()">
            </div>
            <div class="control-group">
              <label>Required Return on Equity ($r_e$ %): <span id="ddmReVal">9.0%</span></label>
              <input type="range" id="ddmRe" min="6.0" max="15.0" value="9.0" step="0.25" oninput="updateEquitySim()">
            </div>
            <div class="control-group">
              <label>High Growth Half-Life ($H$ years): <span id="ddmHVal">4.0 years</span></label>
              <input type="range" id="ddmH" min="1.0" max="10.0" value="4.0" step="0.5" oninput="updateEquitySim()">
            </div>
            <div id="hModelResult" style="padding: 12px; background: var(--bg-primary); border-radius: 6px; border: 1px solid var(--border-color); font-size: 13px; font-weight: 600; color: var(--accent-emerald);">
            </div>
          </div>
          <div>
            <div style="font-weight: 700; color: var(--accent-purple); margin-bottom: 12px;">DuPont 5-Way ROE Decomposition</div>
            <div style="font-size: 12px; line-height: 1.6; margin-bottom: 15px; color: var(--text-secondary);">
              $$\text{ROE} = \left(\frac{\text{NI}}{\text{EBT}}\right) \times \left(\frac{\text{EBT}}{\text{EBIT}}\right) \times \left(\frac{\text{EBIT}}{\text{Rev}}\right) \times \left(\frac{\text{Rev}}{\text{Assets}}\right) \times \left(\frac{\text{Assets}}{\text{Equity}}\right)$$
            </div>
            <canvas id="dupontChart" height="210"></canvas>
          </div>
        </div>
      </div>
    </section>

    <!-- 7. SIMULATION: KEY RATE DURATION -->
    <section id="sim-duration">
      <div class="card">
        <div class="card-title">Key Rate Duration & Yield Curve Sensitivity Visualizer</div>
        <p style="color: var(--text-secondary); margin-bottom: 20px;">
          Examine the price sensitivity of fixed income portfolios across key maturity vertices (2Y, 5Y, 10Y, 30Y) under non-parallel yield curve shocks.
        </p>
        <div class="grid-2">
          <div>
            <canvas id="durationChart" height="230"></canvas>
          </div>
          <div>
            <div class="control-group">
              <label>2-Year Rate Shock (bps): <span id="krd2Val" style="color: var(--accent-blue);">+25 bps</span></label>
              <input type="range" id="krd2" min="-100" max="100" value="25" step="5" oninput="updateDurationSim()">
            </div>
            <div class="control-group">
              <label>5-Year Rate Shock (bps): <span id="krd5Val" style="color: var(--accent-cyan);">+15 bps</span></label>
              <input type="range" id="krd5" min="-100" max="100" value="15" step="5" oninput="updateDurationSim()">
            </div>
            <div class="control-group">
              <label>10-Year Rate Shock (bps): <span id="krd10Val" style="color: var(--accent-emerald);">0 bps</span></label>
              <input type="range" id="krd10" min="-100" max="100" value="0" step="5" oninput="updateDurationSim()">
            </div>
            <div class="control-group">
              <label>30-Year Rate Shock (bps): <span id="krd30Val" style="color: var(--accent-rose);">-30 bps</span></label>
              <input type="range" id="krd30" min="-100" max="100" value="-30" step="5" oninput="updateDurationSim()">
            </div>
            <div id="durationImpactResult" style="padding: 12px; background: var(--bg-primary); border-radius: 6px; border: 1px solid var(--border-color); font-size: 13px; font-weight: 600;">
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 7B. SIMULATION: FRN PRICING ENGINE -->
    <section id="sim-frn">
      <div class="card">
        <div class="card-title">Floating-Rate Note (FRN) Pricing & Discount Margin Engine</div>
        <p style="color: var(--text-secondary); margin-bottom: 20px;">
          Model the market price and discount margin dynamics of floating-rate notes across index rate shifts and credit risk migrations.
        </p>
        <div class="grid-2">
          <div>
            <div class="control-group">
              <label>Index Benchmark Rate (e.g. SOFR): <span id="frnIndexVal" style="color: var(--accent-blue);">4.00%</span></label>
              <input type="range" id="frnIndex" min="0.0" max="10.0" value="4.00" step="0.25" oninput="updateFrnSim()">
            </div>
            <div class="control-group">
              <label>Quoted Margin (QM in bps): <span id="frnQmVal" style="color: var(--accent-cyan);">+100 bps</span></label>
              <input type="range" id="frnQm" min="-100" max="400" value="100" step="10" oninput="updateFrnSim()">
            </div>
            <div class="control-group">
              <label>Required Discount Margin (DM in bps): <span id="frnDmVal" style="color: var(--accent-emerald);">+125 bps</span></label>
              <input type="range" id="frnDm" min="-100" max="400" value="125" step="5" oninput="updateFrnSim()">
            </div>
            <div class="control-group">
              <label>Tenor (Remaining Years): <span id="frnTenorVal" style="color: var(--accent-purple);">3 Years</span></label>
              <input type="range" id="frnTenor" min="1" max="10" value="3" step="1" oninput="updateFrnSim()">
            </div>
            <div class="control-group">
              <label>Coupon Reset Frequency:</label>
              <select id="frnFreq" onchange="updateFrnSim()" style="width: 100%; background: var(--bg-tertiary); color: var(--text-primary); border: 1px solid var(--border-color); padding: 8px 12px; border-radius: 6px;">
                <option value="4">Quarterly (4x/year)</option>
                <option value="2">Semi-Annual (2x/year)</option>
                <option value="1">Annual (1x/year)</option>
              </select>
            </div>
          </div>
          <div>
            <div style="background: var(--bg-tertiary); border: 1px solid var(--border-color); border-radius: 8px; padding: 20px;">
              <div style="font-weight: 700; color: var(--accent-blue); margin-bottom: 15px; font-size: 15px;">FRN Valuation Output & Pricing Analysis</div>
              <div id="frnResultCard" style="line-height: 1.8; font-size: 13.5px;"></div>
              <div style="margin-top: 15px; font-size: 12px; color: var(--text-secondary); border-top: 1px solid var(--border-color); padding-top: 12px;">
                $$\text{Price} = \sum_{t=1}^{N \cdot m} \frac{\frac{(\text{Index} + \text{QM})}{m} \times 100}{\left(1 + \frac{\text{Index} + \text{DM}}{m}\right)^t} + \frac{100}{\left(1 + \frac{\text{Index} + \text{DM}}{m}\right)^{N \cdot m}}$$
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 7C. SIMULATION: RESIDUAL INCOME PERSISTENCE DECAY -->
    <section id="sim-ri-decay">
      <div class="card">
        <div class="card-title">Residual Income Persistence Decay Explorer</div>
        <p style="color: var(--text-secondary); margin-bottom: 20px;">
          Analyze intrinsic equity valuation as residual income fades toward zero or normalizes over time governed by persistence factor $\omega \in [0, 1]$.
        </p>
        <div class="grid-2">
          <div>
            <canvas id="riDecayChart" height="240"></canvas>
          </div>
          <div>
            <div class="control-group">
              <label>Initial Book Value ($B_0$ in USD): <span id="riB0Val" style="color: var(--accent-blue);">50.00 USD</span></label>
              <input type="range" id="riB0" min="10" max="150" value="50" step="5" oninput="updateRiSim()">
            </div>
            <div class="control-group">
              <label>Return on Equity (ROE): <span id="riRoeVal" style="color: var(--accent-emerald);">16.0%</span></label>
              <input type="range" id="riRoe" min="5.0" max="30.0" value="16.0" step="0.5" oninput="updateRiSim()">
            </div>
            <div class="control-group">
              <label>Cost of Equity ($r$): <span id="riRVal" style="color: var(--accent-rose);">10.0%</span></label>
              <input type="range" id="riR" min="6.0" max="18.0" value="10.0" step="0.5" oninput="updateRiSim()">
            </div>
            <div class="control-group">
              <label>Persistence Factor ($\omega$): <span id="riOmegaVal" style="color: var(--accent-purple);">0.60</span></label>
              <input type="range" id="riOmega" min="0.0" max="1.0" value="0.60" step="0.05" oninput="updateRiSim()">
            </div>
            <div id="riResultBox" style="background: var(--bg-tertiary); border: 1px solid var(--border-color); border-radius: 8px; padding: 14px; margin-top: 15px; font-size: 13px;"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- 7D. SIMULATION: FCFF TO FCFE WATERFALL -->
    <section id="sim-waterfall">
      <div class="card">
        <div class="card-title">FCFF to FCFE Cash Flow Waterfall Bridge</div>
        <p style="color: var(--text-secondary); margin-bottom: 20px;">
          Interactively model the transition from Net Income to Free Cash Flow to Firm (FCFF) and Free Cash Flow to Equity (FCFE).
        </p>
        <div class="grid-2">
          <div>
            <canvas id="waterfallChart" height="260"></canvas>
          </div>
          <div>
            <div class="grid-2">
              <div class="control-group">
                <label>Net Income: <span id="wfNiVal" style="color: var(--accent-blue);">120</span></label>
                <input type="range" id="wfNi" min="20" max="300" value="120" step="10" oninput="updateWaterfallSim()">
              </div>
              <div class="control-group">
                <label>Non-Cash Charges (NCC): <span id="wfNccVal" style="color: var(--accent-cyan);">45</span></label>
                <input type="range" id="wfNcc" min="0" max="100" value="45" step="5" oninput="updateWaterfallSim()">
              </div>
              <div class="control-group">
                <label>CapEx (FCInv): <span id="wfFcinvVal" style="color: var(--accent-rose);">60</span></label>
                <input type="range" id="wfFcinv" min="10" max="150" value="60" step="5" oninput="updateWaterfallSim()">
              </div>
              <div class="control-group">
                <label>Working Capital (WCInv): <span id="wfWcinvVal" style="color: var(--accent-amber);">15</span></label>
                <input type="range" id="wfWcinv" min="-30" max="60" value="15" step="5" oninput="updateWaterfallSim()">
              </div>
              <div class="control-group">
                <label>Interest Exp (1-t): <span id="wfIntVal" style="color: var(--accent-purple);">16</span></label>
                <input type="range" id="wfInt" min="0" max="50" value="16" step="2" oninput="updateWaterfallSim()">
              </div>
              <div class="control-group">
                <label>Net Borrowing: <span id="wfNbVal" style="color: var(--accent-emerald);">20</span></label>
                <input type="range" id="wfNb" min="-50" max="100" value="20" step="5" oninput="updateWaterfallSim()">
              </div>
            </div>
            <div id="waterfallMetrics" style="background: var(--bg-tertiary); border: 1px solid var(--border-color); border-radius: 8px; padding: 14px; margin-top: 10px; font-size: 13px;"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- 7E. SIMULATION: CURRENCY TRANSLATION (TEMPORAL VS CURRENT) -->
    <section id="sim-translation">
      <div class="card">
        <div class="card-title">Multinational Currency Translation Engine (Current Rate vs. Temporal Method)</div>
        <p style="color: var(--text-secondary); margin-bottom: 20px;">
          Compare the financial statement distortions, net balance sheet exposures, and translation gains/losses under IFRS and US GAAP.
        </p>
        <div class="grid-2">
          <div>
            <div class="control-group">
              <label>Local Currency (LC) Movement vs. Reporting Currency: <span id="fxMoveVal" style="color: var(--accent-blue);">+15% (LC Appreciates)</span></label>
              <input type="range" id="fxMove" min="-30" max="30" value="15" step="5" oninput="updateTranslationSim()">
            </div>
            <div class="control-group">
              <label>Net Monetary Assets (Cash + AR - Debt - AP): <span id="fxNmaVal" style="color: var(--accent-cyan);">-40 M LC (Net Liability)</span></label>
              <input type="range" id="fxNma" min="-100" max="100" value="-40" step="10" oninput="updateTranslationSim()">
            </div>
            <div class="control-group">
              <label>Net Non-Monetary Assets (PP&E + Inventory): <span id="fxNnmaVal" style="color: var(--accent-emerald);">+120 M LC</span></label>
              <input type="range" id="fxNnma" min="20" max="250" value="120" step="10" oninput="updateTranslationSim()">
            </div>
          </div>
          <div>
            <div id="translationOutput" style="background: var(--bg-tertiary); border: 1px solid var(--border-color); border-radius: 8px; padding: 16px; font-size: 13px;"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- 7F. SIMULATION: MBS PREPAYMENT ENGINE -->
    <section id="sim-prepayment">
      <div class="card">
        <div class="card-title">MBS Prepayment Simulator & Contraction/Extension Risk</div>
        <p style="color: var(--text-secondary); margin-bottom: 20px;">
          Analyze single monthly mortality (SMM), conditional prepayment rate (CPR), and cash flow dynamics across PSA benchmark speeds.
        </p>
        <div class="grid-2">
          <div>
            <canvas id="prepaymentChart" height="250"></canvas>
          </div>
          <div>
            <div class="control-group">
              <label>PSA Benchmark Speed: <span id="psaVal" style="color: var(--accent-blue);">150% PSA</span></label>
              <input type="range" id="psaSpeed" min="25" max="350" value="150" step="25" oninput="updatePrepaymentSim()">
            </div>
            <div class="control-group">
              <label>Mortgage Seasoning (Month $t$): <span id="seasonVal" style="color: var(--accent-cyan);">Month 18</span></label>
              <input type="range" id="seasonMonth" min="1" max="60" value="18" step="1" oninput="updatePrepaymentSim()">
            </div>
            <div id="prepayResultBox" style="background: var(--bg-tertiary); border: 1px solid var(--border-color); border-radius: 8px; padding: 14px; margin-top: 15px; font-size: 13px;"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- 8. REFERENCE DIAGRAMS -->
    <section id="reference-diagrams">
      <div class="grid-2">
        <div class="card">
          <div class="card-title">Merton Structural Model: Default Boundary</div>
          <p style="color: var(--text-secondary); font-size: 12px; margin-bottom: 12px;">Equity as a call option on corporate assets with strike = face value of debt $K$.</p>
          <div class="svg-container">
            <svg width="450" height="220" viewBox="0 0 450 220">
              <!-- Axes -->
              <line x1="40" y1="180" x2="420" y2="180" stroke="var(--text-secondary)" stroke-width="2"/>
              <line x1="40" y1="20" x2="40" y2="180" stroke="var(--text-secondary)" stroke-width="2"/>
              <text x="350" y="200" fill="var(--text-secondary)" font-size="11">Time to Maturity (T)</text>
              <text x="50" y="30" fill="var(--text-secondary)" font-size="11">Asset Value V_A</text>
              <!-- Debt Threshold -->
              <line x1="40" y1="110" x2="420" y2="110" stroke="var(--accent-rose)" stroke-width="2" stroke-dasharray="4"/>
              <text x="300" y="105" fill="var(--accent-rose)" font-size="11">Default Boundary (Debt K)</text>
              <!-- Solvent Asset Path -->
              <path d="M 40 80 Q 140 50 230 70 T 420 40" fill="none" stroke="var(--accent-emerald)" stroke-width="3"/>
              <text x="425" y="45" fill="var(--accent-emerald)" font-size="11">Solvent Path</text>
              <!-- Default Path -->
              <path d="M 40 80 Q 140 100 230 130 T 360 170" fill="none" stroke="var(--accent-rose)" stroke-width="3"/>
              <text x="370" y="170" fill="var(--accent-rose)" font-size="11">Default</text>
            </svg>
          </div>
        </div>

        <div class="card">
          <div class="card-title">Bond Price-Yield Relationship: Convexity</div>
          <p style="color: var(--text-secondary); font-size: 12px; margin-bottom: 12px;">Option-free positive convexity vs Callable bond negative convexity at lower yields.</p>
          <div class="svg-container">
            <svg width="450" height="220" viewBox="0 0 450 220">
              <line x1="40" y1="180" x2="420" y2="180" stroke="var(--text-secondary)" stroke-width="2"/>
              <line x1="40" y1="20" x2="40" y2="180" stroke="var(--text-secondary)" stroke-width="2"/>
              <text x="360" y="200" fill="var(--text-secondary)" font-size="11">Yield to Maturity</text>
              <text x="50" y="30" fill="var(--text-secondary)" font-size="11">Bond Price</text>
              <!-- Call Price Line -->
              <line x1="40" y1="65" x2="420" y2="65" stroke="var(--accent-amber)" stroke-width="1.5" stroke-dasharray="3"/>
              <text x="340" y="60" fill="var(--accent-amber)" font-size="11">Call Price Cap</text>
              <!-- Option-Free Bond (Positive Convexity) -->
              <path d="M 50 35 Q 150 110 400 170" fill="none" stroke="var(--accent-blue)" stroke-width="3"/>
              <text x="280" y="130" fill="var(--accent-blue)" font-size="11">Option-Free Bond</text>
              <!-- Callable Bond (Negative Convexity) -->
              <path d="M 50 65 Q 120 65 170 85 T 400 170" fill="none" stroke="var(--accent-rose)" stroke-width="3" stroke-dasharray="6"/>
              <text x="110" y="55" fill="var(--accent-rose)" font-size="11">Callable Bond (Negative Convexity)</text>
            </svg>
          </div>
        </div>

        <div class="card">
          <div class="card-title">Porter\'s Five Forces Framework</div>
          <p style="color: var(--text-secondary); font-size: 12px; margin-bottom: 12px;">Industry competitive analysis model for equity analysts.</p>
          <div class="svg-container">
            <svg width="450" height="220" viewBox="0 0 450 220">
              <!-- Center Box -->
              <rect x="150" y="80" width="150" height="60" rx="8" fill="var(--bg-secondary)" stroke="var(--accent-blue)" stroke-width="2"/>
              <text x="225" y="105" fill="var(--text-primary)" font-size="12" font-weight="700" text-anchor="middle">Industry Rivalry</text>
              <text x="225" y="125" fill="var(--text-secondary)" font-size="10" text-anchor="middle">Existing Competitors</text>
              <!-- Top Box -->
              <rect x="150" y="10" width="150" height="45" rx="6" fill="var(--bg-secondary)" stroke="var(--accent-cyan)" stroke-width="1.5"/>
              <text x="225" y="38" fill="var(--text-primary)" font-size="11" text-anchor="middle">Threat of New Entrants</text>
              <!-- Bottom Box -->
              <rect x="150" y="165" width="150" height="45" rx="6" fill="var(--bg-secondary)" stroke="var(--accent-emerald)" stroke-width="1.5"/>
              <text x="225" y="193" fill="var(--text-primary)" font-size="11" text-anchor="middle">Threat of Substitutes</text>
              <!-- Left Box -->
              <rect x="10" y="85" width="120" height="50" rx="6" fill="var(--bg-secondary)" stroke="var(--accent-amber)" stroke-width="1.5"/>
              <text x="70" y="107" fill="var(--text-primary)" font-size="10" text-anchor="middle">Supplier Power</text>
              <text x="70" y="123" fill="var(--text-secondary)" font-size="9" text-anchor="middle">Input Pricing</text>
              <!-- Right Box -->
              <rect x="320" y="85" width="120" height="50" rx="6" fill="var(--bg-secondary)" stroke="var(--accent-purple)" stroke-width="1.5"/>
              <text x="380" y="107" fill="var(--text-primary)" font-size="10" text-anchor="middle">Buyer Power</text>
              <text x="380" y="123" fill="var(--text-secondary)" font-size="9" text-anchor="middle">Bargaining Leverage</text>
            </svg>
          </div>
        </div>

        <div class="card">
          <div class="card-title">CDS Curve Trades & Basis Arbitrage</div>
          <p style="color: var(--text-secondary); font-size: 12px; margin-bottom: 12px;">Credit curve steepening/flattening and negative/positive basis trade dynamics.</p>
          <div class="svg-container">
            <svg width="450" height="220" viewBox="0 0 450 220">
              <line x1="40" y1="180" x2="420" y2="180" stroke="var(--text-secondary)" stroke-width="2"/>
              <line x1="40" y1="20" x2="40" y2="180" stroke="var(--text-secondary)" stroke-width="2"/>
              <text x="370" y="200" fill="var(--text-secondary)" font-size="11">Maturity (Years)</text>
              <text x="50" y="30" fill="var(--text-secondary)" font-size="11">CDS Spread (bps)</text>
              <!-- Normal Upward Sloping CDS Curve -->
              <path d="M 50 140 Q 200 90 400 50" fill="none" stroke="var(--accent-cyan)" stroke-width="3"/>
              <text x="320" y="45" fill="var(--accent-cyan)" font-size="11">Normal Credit Curve</text>
              <!-- Inverted Distressed CDS Curve -->
              <path d="M 50 40 Q 200 110 400 130" fill="none" stroke="var(--accent-rose)" stroke-width="3" stroke-dasharray="4"/>
              <text x="120" y="35" fill="var(--accent-rose)" font-size="11">Inverted Curve (Default Risk)</text>
            </svg>
          </div>
        </div>
      </div>
    </section>

  </main>

  <script>
    // Embedded Question Bank Data
    const questionBank = __QUESTION_BANK_DATA__;

    // Navigation Tab Switching
    function switchTab(tabId) {
      document.querySelectorAll('section').forEach(s => s.classList.remove('active'));
      document.querySelectorAll('.nav-links a').forEach(a => a.classList.remove('active'));
      
      const targetSec = document.getElementById(tabId);
      if (targetSec) targetSec.classList.add('active');

      const activeLink = document.querySelector(`.nav-links a[href="#${tabId}"]`);
      if (activeLink) activeLink.classList.add('active');

      const titles = {
        'overview': 'Curriculum Overview & Analytics',
        'l1-practice': 'Level 1 Question Bank: Standalone Practice',
        'l2-vignettes': 'Level 2 Case Study Vignettes: Item Sets',
        'sim-yield': 'Interactive Yield Curve & Term Structure Simulator',
        'sim-tree': 'Binomial Interest Rate Tree & Embedded Option Engine',
        'sim-equity': 'Equity Valuation: Two-Stage DDM & DuPont Explorer',
        'sim-duration': 'Key Rate Duration & Sensitivity Visualizer',
        'sim-frn': 'Floating-Rate Note (FRN) Pricing & Discount Margin Engine',
        'sim-ri-decay': 'Residual Income Persistence Decay Explorer',
        'sim-waterfall': 'FCFF to FCFE Cash Flow Waterfall Bridge',
        'sim-translation': 'Multinational Currency Translation Engine (Current vs Temporal)',
        'sim-prepayment': 'MBS Prepayment Simulator & Contraction/Extension Risk',
        'reference-diagrams': 'CFA Reference Diagrams & Structural Models'
      };
      document.getElementById('topTitle').innerHTML = '<h2>' + (titles[tabId] || 'CFA Master Platform') + '</h2>';
      
      renderMath();
    }

    // Theme Toggle
    function toggleTheme() {
      const html = document.documentElement;
      const cur = html.getAttribute('data-theme');
      html.setAttribute('data-theme', cur === 'dark' ? 'light' : 'dark');
    }

    // Math Rendering helper
    function renderMath() {
      if (window.renderMathInElement) {
        renderMathInElement(document.body, {
          delimiters: [
            {left: '$$', right: '$$', display: true},
            {left: '$', right: '$', display: false}
          ],
          throwOnError: false
        });
      }
    }

    // Overview Chart
    function initOverviewChart() {
      const ctx = document.getElementById('topicDistributionChart').getContext('2d');
      new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: ['L1 Fixed Income', 'L1 Equity', 'L2 Fixed Income', 'L2 Equity'],
          datasets: [{
            data: [120, 115, 85, 95],
            backgroundColor: ['#58a6ff', '#39c5cf', '#bc8cff', '#3fb950'],
            borderColor: '#161b22',
            borderWidth: 2
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { position: 'bottom', labels: { color: '#8b949e', font: { size: 11 } } }
          }
        }
      });
    }

    // LEVEL 1 PRACTICE ENGINE
    let currentL1List = questionBank.filter(q => q.level === 1);
    let l1CurrentIdx = 0;
    let answeredQuestions = {};
    let correctCount = 0;
    let totalAnswered = 0;

    function filterL1Questions() {
      const filterVal = document.getElementById('l1SubjectFilter').value;
      if (filterVal === 'ALL') {
        currentL1List = questionBank.filter(q => q.level === 1);
      } else {
        currentL1List = questionBank.filter(q => q.level === 1 && q.subject.includes(filterVal));
      }
      l1CurrentIdx = 0;
      renderL1Question();
    }

    function nextL1Question() {
      if (currentL1List.length === 0) return;
      l1CurrentIdx = (l1CurrentIdx + 1) % currentL1List.length;
      renderL1Question();
    }

    function prevL1Question() {
      if (currentL1List.length === 0) return;
      l1CurrentIdx = (l1CurrentIdx - 1 + currentL1List.length) % currentL1List.length;
      renderL1Question();
    }

    function randomL1Question() {
      if (currentL1List.length === 0) return;
      l1CurrentIdx = Math.floor(Math.random() * currentL1List.length);
      renderL1Question();
    }

    function renderL1Question() {
      const container = document.getElementById('l1QuestionContainer');
      if (currentL1List.length === 0) {
        container.innerHTML = '<p>No questions matching criteria.</p>';
        return;
      }
      const q = currentL1List[l1CurrentIdx];
      const isAnswered = answeredQuestions[q.id];

      let optsHtml = '';
      for (const [key, val] of Object.entries(q.options)) {
        let btnClass = 'option-btn';
        if (isAnswered) {
          if (key === q.answer) btnClass += ' correct';
          else if (key === isAnswered.selected) btnClass += ' incorrect';
        }
        optsHtml += `
          <button class="${btnClass}" ${isAnswered ? 'disabled' : ''} onclick="submitL1Answer('${q.id}', '${key}', this)">
            <strong style="margin-right: 10px;">${key}.</strong> ${val}
          </button>
        `;
      }

      let distractorHtml = '';
      if (q.distractor_analysis) {
        distractorHtml += '<div class="distractor-box"><div class="distractor-title">Distractor Analysis:</div>';
        for (const [k, dText] of Object.entries(q.distractor_analysis)) {
          distractorHtml += `<div style="margin-top: 4px;"><strong>Option ${k}:</strong> ${dText}</div>`;
        }
        distractorHtml += '</div>';
      }

      container.innerHTML = `
        <div class="question-box">
          <div class="question-header">
            <span class="question-id-badge">${q.id} | ${q.subject} &gt; ${q.subtopic || q.topic}</span>
            <span class="question-los">${q.los || ''}</span>
          </div>
          <div class="question-text">${q.question}</div>
          <div class="options-container">${optsHtml}</div>
          <div id="expl-${q.id}" class="explanation-box" style="${isAnswered ? 'display: block;' : ''}">
            <div class="explanation-title">Detailed Solution & Derivation:</div>
            <div style="line-height: 1.7; font-size: 13.5px;">${q.explanation}</div>
            ${distractorHtml}
          </div>
        </div>
      `;

      renderMath();
    }

    function submitL1Answer(qId, selectedKey, btn) {
      const q = questionBank.find(item => item.id === qId);
      if (!q) return;

      const isCorrect = (selectedKey === q.answer);
      answeredQuestions[qId] = { selected: selectedKey, correct: isCorrect };

      totalAnswered++;
      if (isCorrect) correctCount++;
      updateScoreBadge();

      renderL1Question();
    }

    function updateScoreBadge() {
      const pct = totalAnswered > 0 ? Math.round((correctCount / totalAnswered) * 100) : 0;
      document.getElementById('scoreDisplay').innerText = `${correctCount} / ${totalAnswered} (${pct}%)`;
    }

    // LEVEL 2 VIGNETTE ENGINE
    let vignettesMap = {};
    function initL2Engine() {
      questionBank.filter(q => q.level === 2).forEach(q => {
        const vid = q.vignette_id || 'V_MISC';
        if (!vignettesMap[vid]) {
          vignettesMap[vid] = {
            id: vid,
            subject: q.subject,
            title: q.vignette_title || ('Case ' + vid),
            text: q.vignette_text || '',
            questions: []
          };
        }
        vignettesMap[vid].questions.push(q);
      });

      const select = document.getElementById('l2VignetteSelect');
      select.innerHTML = '';
      for (const [vid, v] of Object.entries(vignettesMap)) {
        const opt = document.createElement('option');
        opt.value = vid;
        opt.innerText = `[${v.subject}] ${vid}: ${v.title} (${v.questions.length} Questions)`;
        select.appendChild(opt);
      }

      loadL2Vignette();
    }

    function loadL2Vignette() {
      const vid = document.getElementById('l2VignetteSelect').value;
      const v = vignettesMap[vid];
      if (!v) return;

      document.getElementById('vignetteTextCard').innerHTML = `
        <div style="font-size: 11px; text-transform: uppercase; color: var(--accent-purple); font-weight: 700; margin-bottom: 6px;">Case Study Vignette: ${v.id}</div>
        <h3 style="font-size: 18px; margin-bottom: 14px; color: var(--accent-cyan);">${v.title}</h3>
        <div style="line-height: 1.75; font-size: 13.5px; white-space: pre-line; color: var(--text-primary);">${v.text}</div>
      `;

      let qHtml = '';
      v.questions.forEach((q, idx) => {
        const isAnswered = answeredQuestions[q.id];
        let optsHtml = '';
        for (const [key, val] of Object.entries(q.options)) {
          let btnClass = 'option-btn';
          if (isAnswered) {
            if (key === q.answer) btnClass += ' correct';
            else if (key === isAnswered.selected) btnClass += ' incorrect';
          }
          optsHtml += `
            <button class="${btnClass}" ${isAnswered ? 'disabled' : ''} onclick="submitL2Answer('${q.id}', '${key}', this)">
              <strong style="margin-right: 8px;">${key}.</strong> ${val}
            </button>
          `;
        }

        let distractorHtml = '';
        if (q.distractor_analysis) {
          distractorHtml += '<div class="distractor-box"><div class="distractor-title">Distractor Analysis:</div>';
          for (const [k, dText] of Object.entries(q.distractor_analysis)) {
            distractorHtml += `<div style="margin-top: 3px;"><strong>Option ${k}:</strong> ${dText}</div>`;
          }
          distractorHtml += '</div>';
        }

        qHtml += `
          <div class="question-box" style="margin-bottom: 16px;">
            <div class="question-header">
              <span class="question-id-badge">Q${idx + 1}: ${q.id}</span>
              <span class="question-los">${q.los || ''}</span>
            </div>
            <div class="question-text" style="font-size: 14px;">${q.question}</div>
            <div class="options-container">${optsHtml}</div>
            <div id="expl-${q.id}" class="explanation-box" style="${isAnswered ? 'display: block;' : ''}">
              <div class="explanation-title">Solution:</div>
              <div style="line-height: 1.65; font-size: 13px;">${q.explanation}</div>
              ${distractorHtml}
            </div>
          </div>
        `;
      });

      document.getElementById('vignetteQuestionsCard').innerHTML = qHtml;
      renderMath();
    }

    function submitL2Answer(qId, selectedKey, btn) {
      const q = questionBank.find(item => item.id === qId);
      if (!q) return;

      const isCorrect = (selectedKey === q.answer);
      answeredQuestions[qId] = { selected: selectedKey, correct: isCorrect };

      totalAnswered++;
      if (isCorrect) correctCount++;
      updateScoreBadge();

      loadL2Vignette();
    }

    // SIMULATION 1: YIELD CURVE CHART
    let yieldChart = null;
    const baseTenors = [1, 2, 3, 5, 7, 10, 20, 30];
    const baseSpot = [2.50, 2.80, 3.10, 3.60, 3.90, 4.20, 4.55, 4.70];

    function initYieldChart() {
      const ctx = document.getElementById('yieldChart').getContext('2d');
      yieldChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: ['1Y', '2Y', '3Y', '5Y', '7Y', '10Y', '20Y', '30Y'],
          datasets: [
            { label: 'Benchmark Spot Curve (%)', data: [...baseSpot], borderColor: '#58a6ff', borderWidth: 2.5, pointRadius: 4 },
            { label: 'Shifted / Shocked Curve (%)', data: [...baseSpot], borderColor: '#f85149', borderWidth: 2.5, borderDash: [5, 5], pointRadius: 4 },
            { label: 'Implied 1-Year Forward Curve (%)', data: [2.50, 3.10, 3.70, 4.35, 4.65, 4.90, 5.25, 5.00], borderColor: '#3fb950', borderWidth: 1.5, pointRadius: 2 }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: { title: { display: true, text: 'Yield (%)', color: '#8b949e' }, grid: { color: '#21262d' } },
            x: { title: { display: true, text: 'Maturity Tenor', color: '#8b949e' }, grid: { color: '#21262d' } }
          },
          plugins: { legend: { labels: { color: '#8b949e' } } }
        }
      });
    }

    function updateYieldSim() {
      const shift = parseFloat(document.getElementById('shiftRange').value);
      const twist = parseFloat(document.getElementById('twistRange').value);
      const butterfly = parseFloat(document.getElementById('butterflyRange').value);

      document.getElementById('shiftVal').innerText = (shift > 0 ? '+' : '') + shift + ' bps';
      document.getElementById('twistVal').innerText = (twist > 0 ? '+' : '') + twist + ' bps';
      document.getElementById('butterflyVal').innerText = (butterfly > 0 ? '+' : '') + butterfly + ' bps';

      const sBps = shift / 100.0;
      const tBps = twist / 100.0;
      const bBps = butterfly / 100.0;

      const shocked = baseSpot.map((r, i) => {
        // level shift + slope twist (steepening: -short, +long) + butterfly (hump at mid tenors)
        const slopeFactor = (i - 3.5) / 3.5;
        const humpf = 1.0 - Math.abs(i - 3.5) / 3.5;
        const shock = sBps + (tBps * slopeFactor) + (bBps * humpf);
        return parseFloat((r + shock).toFixed(2));
      });

      yieldChart.data.datasets[1].data = shocked;
      yieldChart.update();
    }

    // SIMULATION 2: BINOMIAL INTEREST RATE TREE
    function updateTreeSim() {
      const c = parseFloat(document.getElementById('treeCoupon').value);
      const sigma = parseFloat(document.getElementById('treeVol').value) / 100.0;
      const callP = parseFloat(document.getElementById('treeCall').value);

      document.getElementById('treeCouponVal').innerText = c.toFixed(2) + '%';
      document.getElementById('treeVolVal').innerText = (sigma * 100).toFixed(1) + '%';
      document.getElementById('treeCallVal').innerText = callP.toFixed(2) + ' USD';

      // 3-Period Lognormal Rates
      const r0 = 0.04;
      const r1_L = 0.045;
      const r1_U = r1_L * Math.exp(2 * sigma);

      const r2_LL = 0.048;
      const r2_LU = r2_LL * Math.exp(2 * sigma);
      const r2_UU = r2_LL * Math.exp(4 * sigma);

      // Par face value = 100 USD
      const par = 100.0;
      const coup = (c / 100.0) * par;

      // Year 2 Values (uncalled vs called)
      const v2_UU = Math.min((par + coup) / (1 + r2_UU), callP);
      const v2_LU = Math.min((par + coup) / (1 + r2_LU), callP);
      const v2_LL = Math.min((par + coup) / (1 + r2_LL), callP);

      // Year 1 Values
      const v1_U = Math.min((0.5 * (v2_UU + coup) + 0.5 * (v2_LU + coup)) / (1 + r1_U), callP);
      const v1_L = Math.min((0.5 * (v2_LU + coup) + 0.5 * (v2_LL + coup)) / (1 + r1_L), callP);

      // Year 0 Value
      const v0_callable = (0.5 * (v1_U + coup) + 0.5 * (v1_L + coup)) / (1 + r0);

      // Straight Bond Value (no call cap)
      const sv2_UU = (par + coup) / (1 + r2_UU);
      const sv2_LU = (par + coup) / (1 + r2_LU);
      const sv2_LL = (par + coup) / (1 + r2_LL);
      const sv1_U = (0.5 * (sv2_UU + coup) + 0.5 * (sv2_LU + coup)) / (1 + r1_U);
      const sv1_L = (0.5 * (sv2_LU + coup) + 0.5 * (sv2_LL + coup)) / (1 + r1_L);
      const v0_straight = (0.5 * (sv1_U + coup) + 0.5 * (sv1_L + coup)) / (1 + r0);

      const callOptionValue = v0_straight - v0_callable;

      document.getElementById('treeResults').innerHTML = `
        <div><strong>Straight Bond Value:</strong> ${v0_straight.toFixed(3)} USD</div>
        <div><strong>Callable Bond Value:</strong> ${v0_callable.toFixed(3)} USD</div>
        <div><strong>Embedded Call Option Value:</strong> ${callOptionValue.toFixed(3)} USD</div>
        <div style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">
          Formula: $V_{\\text{callable}} = V_{\\text{straight}} - V_{\\text{call option}}$
        </div>
      `;

      // Render Node visual
      document.getElementById('treeVisualContainer').innerHTML = `
        <div class="tree-col">
          <div style="font-size: 11px; color: var(--text-secondary); font-weight: 700;">Year 0 (Today)</div>
          <div class="tree-node">
            <div class="node-rate">${(r0*100).toFixed(2)}%</div>
            <div class="node-val">Price: ${v0_callable.toFixed(2)} USD</div>
          </div>
        </div>
        <div class="tree-col">
          <div style="font-size: 11px; color: var(--text-secondary); font-weight: 700;">Year 1</div>
          <div class="tree-node">
            <div class="node-rate">${(r1_U*100).toFixed(2)}% (Node U)</div>
            <div class="node-val">P: ${v1_U.toFixed(2)} USD</div>
          </div>
          <div class="tree-node">
            <div class="node-rate">${(r1_L*100).toFixed(2)}% (Node L)</div>
            <div class="node-val">P: ${v1_L.toFixed(2)} USD</div>
          </div>
        </div>
        <div class="tree-col">
          <div style="font-size: 11px; color: var(--text-secondary); font-weight: 700;">Year 2</div>
          <div class="tree-node">
            <div class="node-rate">${(r2_UU*100).toFixed(2)}% (UU)</div>
            <div class="node-val">P: ${v2_UU.toFixed(2)} USD</div>
          </div>
          <div class="tree-node">
            <div class="node-rate">${(r2_LU*100).toFixed(2)}% (LU)</div>
            <div class="node-val">P: ${v2_LU.toFixed(2)} USD</div>
          </div>
          <div class="tree-node">
            <div class="node-rate">${(r2_LL*100).toFixed(2)}% (LL)</div>
            <div class="node-val">P: ${v2_LL.toFixed(2)} USD</div>
          </div>
        </div>
      `;
    }

    // SIMULATION 3: EQUITY VALUATION & DUPONT
    let dupontChart = null;
    function initEquitySim() {
      const ctx = document.getElementById('dupontChart').getContext('2d');
      dupontChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ['Tax Burden (NI/EBT)', 'Interest Burden (EBT/EBIT)', 'EBIT Margin', 'Asset Turnover', 'Financial Leverage'],
          datasets: [{
            label: 'DuPont Multipliers',
            data: [0.75, 0.85, 0.18, 1.20, 1.80],
            backgroundColor: ['#58a6ff', '#39c5cf', '#3fb950', '#d29922', '#bc8cff']
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { display: false } },
          scales: { y: { grid: { color: '#21262d' } } }
        }
      });
      updateEquitySim();
    }

    function updateEquitySim() {
      const d0 = parseFloat(document.getElementById('ddmD0').value);
      const gs = parseFloat(document.getElementById('ddmGs').value) / 100.0;
      const gl = parseFloat(document.getElementById('ddmGl').value) / 100.0;
      const re = parseFloat(document.getElementById('ddmRe').value) / 100.0;
      const h = parseFloat(document.getElementById('ddmH').value);

      document.getElementById('ddmD0Val').innerText = d0.toFixed(2) + ' USD';
      document.getElementById('ddmGsVal').innerText = (gs * 100).toFixed(1) + '%';
      document.getElementById('ddmGlVal').innerText = (gl * 100).toFixed(1) + '%';
      document.getElementById('ddmReVal').innerText = (re * 100).toFixed(1) + '%';
      document.getElementById('ddmHVal').innerText = h.toFixed(1) + ' years';

      if (re <= gl) {
        document.getElementById('hModelResult').innerText = 'Invalid parameters: Required return r_e must strictly exceed long-term growth rate g_L.';
        return;
      }

      // H-Model formula
      const baseTerm = (d0 * (1 + gl)) / (re - gl);
      const excessTerm = (d0 * h * (gs - gl)) / (re - gl);
      const v0 = baseTerm + excessTerm;

      document.getElementById('hModelResult').innerHTML = `
        <div><strong>H-Model Intrinsic Value:</strong> ${v0.toFixed(2)} USD</div>
        <div style="font-size: 11px; color: var(--text-secondary); font-weight: normal; margin-top: 4px;">
          Base Component: ${baseTerm.toFixed(2)} USD | Transition Component: ${excessTerm.toFixed(2)} USD
        </div>
      `;
    }

    // SIMULATION 4: KEY RATE DURATION
    let durationChart = null;
    function initDurationSim() {
      const ctx = document.getElementById('durationChart').getContext('2d');
      durationChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ['2-Year Tenor', '5-Year Tenor', '10-Year Tenor', '30-Year Tenor'],
          datasets: [{
            label: 'Key Rate Duration (Years)',
            data: [1.8, 3.6, 6.4, 11.2],
            backgroundColor: ['#58a6ff', '#39c5cf', '#3fb950', '#f85149']
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: { title: { display: true, text: 'Duration (Years)', color: '#8b949e' }, grid: { color: '#21262d' } }
          },
          plugins: { legend: { display: false } }
        }
      });
      updateDurationSim();
    }

    function updateDurationSim() {
      const s2 = parseFloat(document.getElementById('krd2').value);
      const s5 = parseFloat(document.getElementById('krd5').value);
      const s10 = parseFloat(document.getElementById('krd10').value);
      const s30 = parseFloat(document.getElementById('krd30').value);

      document.getElementById('krd2Val').innerText = (s2 >= 0 ? '+' : '') + s2 + ' bps';
      document.getElementById('krd5Val').innerText = (s5 >= 0 ? '+' : '') + s5 + ' bps';
      document.getElementById('krd10Val').innerText = (s10 >= 0 ? '+' : '') + s10 + ' bps';
      document.getElementById('krd30Val').innerText = (s30 >= 0 ? '+' : '') + s30 + ' bps';

      // Duration weights
      const d2 = 1.8, d5 = 3.6, d10 = 6.4, d30 = 11.2;
      const effDur = d2 + d5 + d10 + d30;

      // Price percentage change: -Sum(KRD_k * delta_y_k)
      const dP2 = -d2 * (s2 / 10000.0);
      const dP5 = -d5 * (s5 / 10000.0);
      const dP10 = -d10 * (s10 / 10000.0);
      const dP30 = -d30 * (s30 / 10000.0);
      const totalPctChange = (dP2 + dP5 + dP10 + dP30) * 100.0;

      document.getElementById('durationImpactResult').innerHTML = `
        <div><strong>Total Portfolio Effective Duration:</strong> ${effDur.toFixed(2)} years</div>
        <div style="margin-top: 5px; color: ${totalPctChange >= 0 ? 'var(--accent-emerald)' : 'var(--accent-rose)'};">
          <strong>Estimated Portfolio Price Impact:</strong> ${(totalPctChange >= 0 ? '+' : '') + totalPctChange.toFixed(3)}%
        </div>
      `;
    }


    // SIMULATION 5: FRN PRICING ENGINE
    function updateFrnSim() {
      const idxRate = parseFloat(document.getElementById('frnIndex').value);
      const qmBps = parseFloat(document.getElementById('frnQm').value);
      const dmBps = parseFloat(document.getElementById('frnDm').value);
      const tenor = parseInt(document.getElementById('frnTenor').value);
      const m = parseInt(document.getElementById('frnFreq').value);

      document.getElementById('frnIndexVal').innerText = idxRate.toFixed(2) + '%';
      document.getElementById('frnQmVal').innerText = (qmBps >= 0 ? '+' : '') + qmBps + ' bps';
      document.getElementById('frnDmVal').innerText = (dmBps >= 0 ? '+' : '') + dmBps + ' bps';
      document.getElementById('frnTenorVal').innerText = tenor + ' Year' + (tenor > 1 ? 's' : '');

      const couponRate = (idxRate + qmBps / 100.0) / 100.0;
      const discountRate = (idxRate + dmBps / 100.0) / 100.0;
      const periods = tenor * m;
      const couponPerPeriod = (couponRate / m) * 100.0;
      const rPerPeriod = discountRate / m;

      let price = 0;
      for (let t = 1; t <= periods; t++) {
        price += couponPerPeriod / Math.pow(1 + rPerPeriod, t);
      }
      price += 100.0 / Math.pow(1 + rPerPeriod, periods);

      let status = '';
      let statusColor = '';
      if (Math.abs(qmBps - dmBps) < 0.1) {
        status = 'Trading at Par (100.00)';
        statusColor = 'var(--accent-blue)';
      } else if (qmBps > dmBps) {
        status = 'Trading at Premium (P > 100)';
        statusColor = 'var(--accent-emerald)';
      } else {
        status = 'Trading at Discount (P < 100)';
        statusColor = 'var(--accent-rose)';
      }

      document.getElementById('frnResultCard').innerHTML = `
        <div style="font-size: 20px; font-weight: 800; color: ${statusColor}; margin-bottom: 8px;">
          FRN Price: ${price.toFixed(3)} per 100 par
        </div>
        <div style="display: inline-block; padding: 4px 10px; border-radius: 4px; background: rgba(88, 166, 255, 0.1); color: ${statusColor}; font-weight: 700; margin-bottom: 12px;">
          ${status}
        </div>
        <div><strong>Coupon Rate (Index + QM):</strong> ${(couponRate * 100).toFixed(2)}% (${couponPerPeriod.toFixed(3)} USD / period)</div>
        <div><strong>Required Yield (Index + DM):</strong> ${(discountRate * 100).toFixed(2)}%</div>
        <div><strong>Margin Spread (QM - DM):</strong> ${(qmBps - dmBps).toFixed(0)} bps</div>
        <div style="font-size: 11px; color: var(--text-secondary); margin-top: 6px;">
          *Benchmark duration is approx. 1/(2*m) = ${(1.0 / (2 * m)).toFixed(2)} years. Price changes between reset dates are driven by changes in required credit discount margin.
        </div>
      `;
    }

    // SIMULATION 6: RESIDUAL INCOME PERSISTENCE DECAY
    let riDecayChart = null;
    function initRiSim() {
      const ctx = document.getElementById('riDecayChart').getContext('2d');
      riDecayChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5', 'Year 6', 'Year 7', 'Year 8'],
          datasets: [{
            label: 'Residual Income (USD)',
            data: [],
            backgroundColor: '#bc8cff',
            borderRadius: 4
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: { title: { display: true, text: 'Residual Income (USD)', color: '#8b949e' }, grid: { color: '#21262d' } },
            x: { grid: { color: '#21262d' } }
          },
          plugins: { legend: { display: false } }
        }
      });
      updateRiSim();
    }

    function updateRiSim() {
      const b0 = parseFloat(document.getElementById('riB0').value);
      const roe = parseFloat(document.getElementById('riRoe').value) / 100.0;
      const r = parseFloat(document.getElementById('riR').value) / 100.0;
      const omega = parseFloat(document.getElementById('riOmega').value);

      document.getElementById('riB0Val').innerText = b0.toFixed(2) + ' USD';
      document.getElementById('riRoeVal').innerText = (roe * 100).toFixed(1) + '%';
      document.getElementById('riRVal').innerText = (r * 100).toFixed(1) + '%';
      document.getElementById('riOmegaVal').innerText = omega.toFixed(2);

      const ri1 = (roe - r) * b0;
      const riStream = [];
      let pvRi = 0;

      for (let t = 1; t <= 8; t++) {
        const rit = ri1 * Math.pow(omega, t - 1);
        riStream.push(parseFloat(rit.toFixed(2)));
        pvRi += rit / Math.pow(1 + r, t);
      }

      // Continuing residual income terminal value at Year 1:
      // V0 = B0 + RI1 / (1 + r - omega)
      const v0Infinite = b0 + (ri1 / (1 + r - omega));
      const mva = v0Infinite - b0;

      if (riDecayChart) {
        riDecayChart.data.datasets[0].data = riStream;
        riDecayChart.update();
      }

      document.getElementById('riResultBox').innerHTML = `
        <div style="font-weight: 700; color: var(--accent-purple); font-size: 15px; margin-bottom: 6px;">
          Intrinsic Value ($V_0$): ${v0Infinite.toFixed(2)} USD
        </div>
        <div><strong>Initial Book Value ($B_0$):</strong> ${b0.toFixed(2)} USD</div>
        <div><strong>Economic Spread (ROE - r):</strong> ${((roe - r) * 100).toFixed(1)}%</div>
        <div><strong>Year 1 Residual Income ($RI_1$):</strong> ${ri1.toFixed(2)} USD</div>
        <div><strong>Implied Premium over Book ($V_0 - B_0$):</strong> ${mva.toFixed(2)} USD (P/B = ${(v0Infinite / b0).toFixed(2)}x)</div>
      `;
    }

    // SIMULATION 7: WATERFALL BUILDER
    let waterfallChart = null;
    function initWaterfallSim() {
      const ctx = document.getElementById('waterfallChart').getContext('2d');
      waterfallChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ['Net Income', '+ NCC', '- FCInv', '- WCInv', '= FCFF', '- Int(1-t)', '+ Net Borrow', '= FCFE'],
          datasets: [{
            label: 'Cash Flow',
            data: [],
            backgroundColor: []
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: { grid: { color: '#21262d' } },
            x: { grid: { color: '#21262d' } }
          },
          plugins: { legend: { display: false } }
        }
      });
      updateWaterfallSim();
    }

    function updateWaterfallSim() {
      const ni = parseFloat(document.getElementById('wfNi').value);
      const ncc = parseFloat(document.getElementById('wfNcc').value);
      const fcinv = parseFloat(document.getElementById('wfFcinv').value);
      const wcinv = parseFloat(document.getElementById('wfWcinv').value);
      const intNet = parseFloat(document.getElementById('wfInt').value);
      const nb = parseFloat(document.getElementById('wfNb').value);

      document.getElementById('wfNiVal').innerText = ni;
      document.getElementById('wfNccVal').innerText = ncc;
      document.getElementById('wfFcinvVal').innerText = fcinv;
      document.getElementById('wfWcinvVal').innerText = wcinv;
      document.getElementById('wfIntVal').innerText = intNet;
      document.getElementById('wfNbVal').innerText = nb;

      const fcff = ni + ncc - fcinv - wcinv + intNet;
      const fcfe = fcff - intNet + nb;

      const vals = [ni, ncc, -fcinv, -wcinv, fcff, -intNet, nb, fcfe];
      const colors = vals.map((v, i) => {
        if (i === 4) return '#39c5cf'; // FCFF
        if (i === 7) return '#3fb950'; // FCFE
        return v >= 0 ? '#58a6ff' : '#f85149';
      });

      if (waterfallChart) {
        waterfallChart.data.datasets[0].data = vals;
        waterfallChart.data.datasets[0].backgroundColor = colors;
        waterfallChart.update();
      }

      document.getElementById('waterfallMetrics').innerHTML = `
        <div style="font-weight: 700; color: var(--accent-cyan); font-size: 14px;">Free Cash Flow to Firm (FCFF): ${fcff.toFixed(1)} USD</div>
        <div style="font-weight: 700; color: var(--accent-emerald); font-size: 14px; margin-top: 4px;">Free Cash Flow to Equity (FCFE): ${fcfe.toFixed(1)} USD</div>
        <div style="font-size: 11px; color: var(--text-secondary); margin-top: 6px;">
          *FCFF is available to all providers of capital (debt + equity) and discounted at WACC. FCFE is available strictly to common shareholders and discounted at Cost of Equity ($r_e$).
        </div>
      `;
    }

    // SIMULATION 8: CURRENCY TRANSLATION
    function updateTranslationSim() {
      const fx = parseFloat(document.getElementById('fxMove').value);
      const nma = parseFloat(document.getElementById('fxNma').value);
      const nnma = parseFloat(document.getElementById('fxNnma').value);

      document.getElementById('fxMoveVal').innerText = (fx >= 0 ? '+' : '') + fx + '% (LC ' + (fx >= 0 ? 'Appreciates' : 'Depreciates') + ')';
      document.getElementById('fxNmaVal').innerText = (nma >= 0 ? '+' : '') + nma + ' M LC (' + (nma >= 0 ? 'Net Asset' : 'Net Liability') + ')';
      document.getElementById('fxNnmaVal').innerText = '+' + nnma + ' M LC';

      const netBalanceSheetExposureCurrent = nma + nnma; // All assets - all liabilities
      const netBalanceSheetExposureTemporal = nma;       // Only monetary assets - monetary liabilities

      const currentGainLoss = netBalanceSheetExposureCurrent * (fx / 100.0);
      const temporalGainLoss = netBalanceSheetExposureTemporal * (fx / 100.0);

      document.getElementById('translationOutput').innerHTML = `
        <div style="font-weight: 700; font-size: 14px; color: var(--accent-blue); margin-bottom: 10px;">Translation Methodology Comparative Matrix</div>
        <table style="width: 100%; border-collapse: collapse; font-size: 12px; margin-bottom: 12px;">
          <thead>
            <tr style="border-bottom: 1px solid var(--border-color); color: var(--text-secondary);">
              <th style="text-align: left; padding: 6px 0;">Dimension</th>
              <th style="text-align: left; padding: 6px 0;">Current Rate Method</th>
              <th style="text-align: left; padding: 6px 0;">Temporal Method</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom: 1px solid var(--border-color);">
              <td style="padding: 6px 0;">Functional Currency</td>
              <td style="color: var(--accent-cyan);">Local Currency (LC)</td>
              <td style="color: var(--accent-purple);">Parent Currency (RC)</td>
            </tr>
            <tr style="border-bottom: 1px solid var(--border-color);">
              <td style="padding: 6px 0;">Balance Sheet Exposure</td>
              <td>Net Equity: <strong>${netBalanceSheetExposureCurrent} M LC</strong></td>
              <td>Net Monetary: <strong>${netBalanceSheetExposureTemporal} M LC</strong></td>
            </tr>
            <tr style="border-bottom: 1px solid var(--border-color);">
              <td style="padding: 6px 0;">Translation Adjustment</td>
              <td style="color: ${currentGainLoss >= 0 ? 'var(--accent-emerald)' : 'var(--accent-rose)'}; font-weight: 700;">
                ${(currentGainLoss >= 0 ? '+' : '') + currentGainLoss.toFixed(1)} M (OCI / Equity CTA)
              </td>
              <td style="color: ${temporalGainLoss >= 0 ? 'var(--accent-emerald)' : 'var(--accent-rose)'}; font-weight: 700;">
                ${(temporalGainLoss >= 0 ? '+' : '') + temporalGainLoss.toFixed(1)} M (Income Statement P&L)
              </td>
            </tr>
            <tr>
              <td style="padding: 6px 0;">Inventory & Fixed Assets</td>
              <td>Current Exchange Rate</td>
              <td>Historical Exchange Rate</td>
            </tr>
          </tbody>
        </table>
        <div style="font-size: 11px; color: var(--text-secondary); line-height: 1.5;">
          *Under Current Rate, exchange gains/losses bypass Net Income and accumulate in OCI (CTA). Under Temporal, monetary imbalance hits the P&L directly, creating reported net income volatility.
        </div>
      `;
    }

    // SIMULATION 9: MBS PREPAYMENT
    let prepaymentChart = null;
    function initPrepaymentSim() {
      const ctx = document.getElementById('prepaymentChart').getContext('2d');
      prepaymentChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: Array.from({length: 30}, (_, i) => 'M' + (i + 1)),
          datasets: [
            {
              label: 'CPR (%)',
              data: [],
              borderColor: '#39c5cf',
              backgroundColor: 'rgba(57, 197, 207, 0.1)',
              fill: true,
              tension: 0.3
            },
            {
              label: 'SMM (%)',
              data: [],
              borderColor: '#f85149',
              backgroundColor: 'transparent',
              borderDash: [5, 5],
              tension: 0.3
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: { title: { display: true, text: 'Rate (%)', color: '#8b949e' }, grid: { color: '#21262d' } },
            x: { grid: { color: '#21262d' } }
          }
        }
      });
      updatePrepaymentSim();
    }

    function updatePrepaymentSim() {
      const psa = parseFloat(document.getElementById('psaSpeed').value);
      const mSel = parseInt(document.getElementById('seasonMonth').value);

      document.getElementById('psaVal').innerText = psa + '% PSA';
      document.getElementById('seasonVal').innerText = 'Month ' + mSel;

      const cprList = [];
      const smmList = [];

      for (let t = 1; t <= 30; t++) {
        let baseCpr = (t <= 30) ? (0.06 * (t / 30.0)) : 0.06;
        let cpr = baseCpr * (psa / 100.0);
        let smm = 1.0 - Math.pow(1.0 - cpr, 1.0 / 12.0);
        cprList.push((cpr * 100).toFixed(2));
        smmList.push((smm * 100).toFixed(3));
      }

      if (prepaymentChart) {
        prepaymentChart.data.datasets[0].data = cprList;
        prepaymentChart.data.datasets[1].data = smmList;
        prepaymentChart.update();
      }

      let curCpr = (mSel <= 30 ? (0.06 * (mSel / 30.0)) : 0.06) * (psa / 100.0);
      let curSmm = 1.0 - Math.pow(1.0 - curCpr, 1.0 / 12.0);

      let riskType = '';
      if (psa > 100) {
        riskType = '<span style="color: var(--accent-rose); font-weight: 700;">Contraction Risk Dominates</span> (Refinancing accelerates; prepayments shorten bond life when reinvestment rates are low).';
      } else if (psa < 100) {
        riskType = '<span style="color: var(--accent-amber); font-weight: 700;">Extension Risk Dominates</span> (Homeowners delay prepaying; bond life lengthens when interest rates are high).';
      } else {
        riskType = '<span style="color: var(--accent-emerald); font-weight: 700;">Standard Benchmark Speed (100% PSA)</span>';
      }

      document.getElementById('prepayResultBox').innerHTML = `
        <div style="font-weight: 700; color: var(--accent-blue); font-size: 14px;">Month ${mSel} Metrics (${psa}% PSA)</div>
        <div><strong>Conditional Prepayment Rate (CPR):</strong> ${(curCpr * 100).toFixed(2)}% annualized</div>
        <div><strong>Single Monthly Mortality (SMM):</strong> ${(curSmm * 100).toFixed(3)}% per month</div>
        <div style="margin-top: 8px; font-size: 12px; line-height: 1.5; border-top: 1px solid var(--border-color); padding-top: 8px;">
          ${riskType}
        </div>
      `;
    }

    // Initialization on window load
    window.addEventListener('DOMContentLoaded', () => {
      initOverviewChart();
      renderL1Question();
      initL2Engine();
      initYieldChart();
      updateTreeSim();
      initEquitySim();
      initDurationSim();
      updateFrnSim();
      initRiSim();
      initWaterfallSim();
      updateTranslationSim();
      initPrepaymentSim();
      renderMath();
    });
  </script>
</body>
</html>
'''

# Embed json data safely
qs_json_str = json.dumps(questions, ensure_ascii=False)
html_full = dashboard_html_template.replace("__QUESTION_BANK_DATA__", qs_json_str)

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_full)

print(f"Generated complete dashboard at {OUTPUT_HTML} ({len(html_full)} bytes)")

# Also create the self-contained build_fi_eq_notes.py
compiler_code = f'''# Self-contained compiler for CFA Fixed Income & Equity Question Bank
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data", "fi_eq")
MASTER_JSON = os.path.join(DATA_DIR, "cfa_fi_eq_master.json")
OUTPUT_HTML = os.path.join(BASE_DIR, "fi_eq_dashboard.html")

def compile_suite():
    if not os.path.exists(MASTER_JSON):
        print(f"Master JSON missing at {{MASTER_JSON}}")
        return
    with open(MASTER_JSON, "r", encoding="utf-8") as f:
        questions = json.load(f)
    print(f"Compiling {{len(questions)}} questions into {{OUTPUT_HTML}}...")
    
    # Run compiler
    from scripts.generate_full_dashboard import dashboard_html_template
    html_full = dashboard_html_template.replace("__QUESTION_BANK_DATA__", json.dumps(questions, ensure_ascii=False))
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_full)
    print("Compilation successful.")

if __name__ == "__main__":
    compile_suite()
'''

with open(BUILD_NOTES_PY, "w", encoding="utf-8") as f:
    f.write(compiler_code)

print(f"Wrote compiler script to {BUILD_NOTES_PY}")
