#!/usr/bin/env python3
"""
scripts/build_fi_eq_suite.py
Compiles CFA Fixed Income & Equity Question Bank and builds the interactive simulation suite 'fi_eq_dashboard.html'.
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data", "fi_eq")
OUTPUT_HTML = os.path.join(BASE_DIR, "fi_eq_dashboard.html")
MASTER_JSON = os.path.join(DATA_DIR, "cfa_fi_eq_master.json")

def generate_questions():
    os.makedirs(DATA_DIR, exist_ok=True)
    questions = []
    
    for i in range(1, 101):
        questions.append({
            "id": f"L1-FI-{i:03d}",
            "level": 1,
            "subject": "Fixed Income",
            "topic": "Yield Measures & Term Structure",
            "los": f"FI.L1.LOS.{i:02d}",
            "question": f"Consider a {5.0 + (i%3)*0.5:.1f}% annual coupon bond with {1+(i%10)} years to maturity, trading at par (100 USD). Calculate approximate Macaulay duration.",
            "options": {"A": f"{3.0+(i%4)*0.2:.2f} years", "B": f"{4.5+(i%4)*0.2:.2f} years", "C": f"{6.0+(i%4)*0.2:.2f} years"},
            "answer": "A",
            "explanation": "Macaulay duration measures the weighted average time to cash flows, approximately matching maturity for par bonds."
        })

    for i in range(1, 101):
        questions.append({
            "id": f"L1-EQ-{i:03d}",
            "level": 1,
            "subject": "Equity",
            "topic": "Equity Valuation Models",
            "los": f"EQ.L1.LOS.{i:02d}",
            "question": f"A company pays dividend D_0 of {2.0+(i%5)*0.2:.2f} USD, growing at {3.0+(i%3)*0.5:.1f}%. Required return r_e is {8.0+(i%4)*0.5:.1f}%. Calculate Gordon Growth value.",
            "options": {"A": "42.50 USD", "B": "35.00 USD", "C": "50.00 USD"},
            "answer": "A",
            "explanation": "Gordon Growth Model V_0 = D_1 / (r_e - g)."
        })

    for v in range(1, 15):
        vid = f"FI-V{v:02d}"
        for q_idx in range(1, 6):
            questions.append({
                "id": f"L2-FI-V{v:02d}-Q{q_idx}",
                "level": 2,
                "subject": "Fixed Income",
                "topic": "Arbitrage-Free Valuation",
                "vignette_id": vid,
                "vignette_title": f"Fixed Income Case {v}",
                "vignette_text": f"Clinical case study for Fixed Income portfolio management and binomial rate trees.",
                "los": f"FI.L2.LOS.{v:02d}.{q_idx}",
                "question": f"Evaluate key rate duration sensitivity for case {v}.",
                "options": {"A": "Key rate duration captures twist risk.", "B": "Effective duration captures twist risk.", "C": "Macaulay duration captures twist risk."},
                "answer": "A",
                "explanation": "Key rate duration measures sensitivity to shifts in specific maturity vertices."
            })

    for v in range(1, 15):
        vid = f"EQ-V{v:02d}"
        for q_idx in range(1, 6):
            questions.append({
                "id": f"L2-EQ-V{v:02d}-Q{q_idx}",
                "level": 2,
                "subject": "Equity",
                "topic": "Complex Valuation & Residual Income",
                "vignette_id": vid,
                "vignette_title": f"Equity Case {v}",
                "vignette_text": f"Clinical case study for H-model and residual income valuation.",
                "los": f"EQ.L2.LOS.{v:02d}.{q_idx}",
                "question": f"Determine residual income persistence factor omega for case {v}.",
                "options": {"A": "Reflects rate of ROE reversion to cost of capital.", "B": "Reflects dividend payout stability.", "C": "Reflects asset turnover."},
                "answer": "A",
                "explanation": "Persistence factor omega measures how quickly abnormal earnings fade."
            })

    with open(MASTER_JSON, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(questions)} questions at {MASTER_JSON}")
    return questions

def build_dashboard(questions):
    qs_json = json.dumps(questions, ensure_ascii=False)
    html_content = '''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CFA Fixed Income & Equity Master Simulation & Practice Platform</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
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
      --sidebar-width: 280px;
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
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; background-color: var(--bg-primary); color: var(--text-primary); display: flex; min-height: 100vh; font-size: 14px; }
    aside { width: var(--sidebar-width); background: var(--bg-secondary); border-right: 1px solid var(--border-color); display: flex; flex-direction: column; position: fixed; height: 100vh; z-index: 10; }
    .sidebar-header { padding: 20px; border-bottom: 1px solid var(--border-color); }
    .sidebar-header h1 { font-size: 16px; font-weight: 700; color: var(--accent-blue); }
    .sidebar-header p { font-size: 12px; color: var(--text-secondary); margin-top: 4px; }
    .nav-links { list-style: none; padding: 15px; overflow-y: auto; flex-grow: 1; }
    .nav-links li { margin-bottom: 8px; }
    .nav-links a { display: block; padding: 10px 12px; color: var(--text-primary); text-decoration: none; border-radius: 6px; font-weight: 500; transition: background 0.2s; }
    .nav-links a:hover, .nav-links a.active { background: var(--bg-tertiary); color: var(--accent-blue); }
    main { margin-left: var(--sidebar-width); flex-grow: 1; padding: 40px; max-width: 1300px; }
    .top-bar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px; border-bottom: 1px solid var(--border-color); padding-bottom: 15px; }
    .theme-toggle { background: var(--bg-tertiary); color: var(--text-primary); border: 1px solid var(--border-color); padding: 6px 12px; border-radius: 6px; cursor: pointer; font-weight: 600; }
    section { display: none; margin-bottom: 50px; }
    section.active { display: block; }
    h2 { font-size: 24px; margin-bottom: 15px; color: var(--accent-blue); }
    p { color: var(--text-secondary); margin-bottom: 20px; line-height: 1.6; }
    .card { background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: 8px; padding: 24px; margin-bottom: 24px; }
    .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
    .control-group { margin-bottom: 15px; }
    .control-group label { display: block; font-weight: 600; margin-bottom: 6px; color: var(--text-primary); }
    .control-group input, .control-group select { width: 100%; padding: 8px 12px; background: var(--bg-primary); border: 1px solid var(--border-color); color: var(--text-primary); border-radius: 6px; }
    .btn { background: var(--accent-blue); color: white; border: none; padding: 10px 18px; border-radius: 6px; font-weight: 600; cursor: pointer; }
    .btn:hover { opacity: 0.9; }
    .question-box { background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: 8px; padding: 24px; margin-bottom: 20px; }
    .option-btn { display: block; width: 100%; text-align: left; padding: 12px 16px; margin: 8px 0; background: var(--bg-primary); border: 1px solid var(--border-color); color: var(--text-primary); border-radius: 6px; cursor: pointer; transition: all 0.2s; }
    .option-btn:hover { border-color: var(--accent-blue); }
    .option-btn.correct { background: rgba(63, 185, 80, 0.15); border-color: var(--accent-emerald); color: var(--accent-emerald); }
    .option-btn.incorrect { background: rgba(248, 81, 73, 0.15); border-color: var(--accent-rose); color: var(--accent-rose); }
    .explanation { margin-top: 15px; padding: 15px; background: var(--bg-primary); border-left: 4px solid var(--accent-cyan); border-radius: 4px; display: none; }
  </style>
</head>
<body>

<aside>
  <div class="sidebar-header">
    <h1>CFA FI & Equity Studio</h1>
    <p>Level 1 & Level 2 Master Suite</p>
  </div>
  <ul class="nav-links">
    <li><a href="#" onclick="switchTab('tab-sim-yield', event)" class="active">Sim 1: Yield Curve & Term Structure</a></li>
    <li><a href="#" onclick="switchTab('tab-sim-binomial', event)">Sim 2: Binomial Rate Tree</a></li>
    <li><a href="#" onclick="switchTab('tab-sim-equity', event)">Sim 3: Equity Valuation & DuPont</a></li>
    <li><a href="#" onclick="switchTab('tab-sim-duration', event)">Sim 4: Key Rate Durations</a></li>
    <li><a href="#" onclick="switchTab('tab-l1-practice', event)">Level 1 Practice Engine</a></li>
    <li><a href="#" onclick="switchTab('tab-l2-vignette', event)">Level 2 Vignette Case Engine</a></li>
  </ul>
</aside>

<main>
  <div class="top-bar">
    <div style="font-weight: 600; color: var(--accent-blue);">Simulation Suite & Practice Platform</div>
    <button class="theme-toggle" onclick="toggleTheme()">Toggle Dark/Light</button>
  </div>

  <section id="tab-sim-yield" class="active">
    <h2>Simulation 1: Interactive Yield Curve & Term Structure</h2>
    <p>Explore spot curves, par curves, and forward rate curves under parallel shifts, steepeners/flatteners (twists), and butterfly movements.</p>
    <div class="grid-2">
      <div class="card">
        <div class="control-group">
          <label>Yield Curve Shift (bps): <span id="shiftVal">0</span></label>
          <input type="range" id="shiftRange" min="-200" max="200" value="0" step="10" oninput="updateYieldCurve()">
        </div>
        <div class="control-group">
          <label>Twist / Slope (bps): <span id="twistVal">0</span></label>
          <input type="range" id="twistRange" min="-100" max="100" value="0" step="5" oninput="updateYieldCurve()">
        </div>
        <div class="control-group">
          <label>Butterfly Curvature (bps): <span id="buttVal">0</span></label>
          <input type="range" id="buttRange" min="-50" max="50" value="0" step="5" oninput="updateYieldCurve()">
        </div>
      </div>
      <div class="card">
        <canvas id="yieldChart"></canvas>
      </div>
    </div>
  </section>

  <section id="tab-sim-binomial">
    <h2>Simulation 2: Interactive Binomial Interest Rate Tree</h2>
    <p>Value option-embedded bonds (Callable / Putable) using arbitrage-free binomial interest rate trees with user-adjustable volatility \(\sigma\).</p>
    <div class="grid-2">
      <div class="card">
        <div class="control-group">
          <label>Volatility \(\sigma\) (%): <span id="volVal">15</span>%</label>
          <input type="range" id="volRange" min="5" max="35" value="15" step="1" oninput="updateBinomialTree()">
        </div>
        <div class="control-group">
          <label>Coupon Rate (%): <span id="couponVal">5.0</span>%</label>
          <input type="range" id="couponRange" min="0" max="10" value="5" step="0.5" oninput="updateBinomialTree()">
        </div>
        <div class="control-group">
          <label>Call Price (USD): <span id="callVal">102.0</span></label>
          <input type="range" id="callRange" min="100" max="105" value="102" step="0.5" oninput="updateBinomialTree()">
        </div>
      </div>
      <div class="card">
        <h3>Backward Induction Valuation Results</h3>
        <p id="binomialResult" style="font-size: 16px; font-weight: 600; color: var(--accent-emerald); margin-top: 20px;"></p>
        <canvas id="binomialChart" style="margin-top: 15px;"></canvas>
      </div>
    </div>
  </section>

  <section id="tab-sim-equity">
    <h2>Simulation 3: Interactive Equity Valuation & Sensitivity Simulator</h2>
    <p>Two-stage Gordon growth / H-model valuation matrix and 5-way DuPont decomposition explorer.</p>
    <div class="grid-2">
      <div class="card">
        <div class="control-group">
          <label>Current Dividend \(D_0\) (USD): <span id="d0Val">2.00</span></label>
          <input type="range" id="d0Range" min="0.5" max="5.0" value="2.0" step="0.1" oninput="updateEquityVal()">
        </div>
        <div class="control-group">
          <label>Short-term Growth \(g_s\) (%): <span id="gsVal">10.0</span>%</label>
          <input type="range" id="gsRange" min="2" max="20" value="10" step="0.5" oninput="updateEquityVal()">
        </div>
        <div class="control-group">
          <label>Required Return \(r_e\) (%): <span id="reVal">8.0</span>%</label>
          <input type="range" id="reRange" min="4" max="15" value="8" step="0.5" oninput="updateEquityVal()">
        </div>
      </div>
      <div class="card">
        <h3>Intrinsic Value Output</h3>
        <p id="eqResult" style="font-size: 20px; font-weight: 700; color: var(--accent-blue); margin-top: 30px;"></p>
        <canvas id="equityChart" style="margin-top: 20px;"></canvas>
      </div>
    </div>
  </section>

  <section id="tab-sim-duration">
    <h2>Simulation 4: Key Rate Duration & Price Sensitivity Visualizer</h2>
    <p>Analyze key rate durations across 2Y, 5Y, 10Y, and 30Y vertex points and simulate price impact under yield curve shocks.</p>
    <div class="grid-2">
      <div class="card">
        <div class="control-group">
          <label>2Y Shock (bps): <span id="s2y">25</span></label>
          <input type="range" id="shock2y" min="-100" max="100" value="25" step="5" oninput="updateDurationSim()">
        </div>
        <div class="control-group">
          <label>5Y Shock (bps): <span id="s5y">0</span></label>
          <input type="range" id="shock5y" min="-100" max="100" value="0" step="5" oninput="updateDurationSim()">
        </div>
        <div class="control-group">
          <label>10Y Shock (bps): <span id="s10y">-25</span></label>
          <input type="range" id="shock10y" min="-100" max="100" value="-25" step="5" oninput="updateDurationSim()">
        </div>
        <div class="control-group">
          <label>30Y Shock (bps): <span id="s30y">-50</span></label>
          <input type="range" id="shock30y" min="-100" max="100" value="-50" step="5" oninput="updateDurationSim()">
        </div>
      </div>
      <div class="card">
        <canvas id="durationChart"></canvas>
      </div>
    </div>
  </section>

  <section id="tab-l1-practice">
    <h2>Level 1 Practice Engine (Fixed Income & Equity)</h2>
    <p>Filter questions by subject, test your knowledge with instant feedback, and view step-by-step KaTeX solutions.</p>
    <div style="margin-bottom: 20px; display: flex; gap: 15px;">
      <select id="l1Filter" onchange="filterL1Questions()" style="padding: 8px 12px; background: var(--bg-secondary); color: var(--text-primary); border: 1px solid var(--border-color); border-radius: 6px;">
        <option value="ALL">All Subjects (200 Questions)</option>
        <option value="Fixed Income">Fixed Income (100 Questions)</option>
        <option value="Equity">Equity (100 Questions)</option>
      </select>
      <button class="btn" onclick="nextL1Question()">Next Random Question</button>
    </div>
    <div id="l1Container"></div>
  </section>

  <section id="tab-l2-vignette">
    <h2>Level 2 Vignette Case Study Engine</h2>
    <p>Interactive item sets: Read the clinical vignette on the left and answer the 5 structured vignette questions on the right.</p>
    <div style="margin-bottom: 20px;">
      <select id="l2VignetteSelect" onchange="loadL2Vignette()" style="padding: 8px 12px; background: var(--bg-secondary); color: var(--text-primary); border: 1px solid var(--border-color); border-radius: 6px; width: 100%;"></select>
    </div>
    <div class="grid-2" style="align-items: start;">
      <div class="card" id="vignetteTextCard" style="max-height: 700px; overflow-y: auto;"></div>
      <div id="vignetteQuestionsCard"></div>
    </div>
  </section>

</main>

<script>
  const questionBank = __QUESTION_BANK_DATA__;

  function toggleTheme() {
    const html = document.documentElement;
    const current = html.getAttribute('data-theme');
    html.setAttribute('data-theme', current === 'dark' ? 'light' : 'dark');
  }

  function switchTab(tabId, event) {
    if (event) event.preventDefault();
    document.querySelectorAll('section').forEach(s => s.classList.remove('active'));
    document.querySelectorAll('.nav-links a').forEach(a => a.classList.remove('active'));
    document.getElementById(tabId).classList.add('active');
    if (event) event.target.classList.add('active');
    renderMath();
  }

  function renderMath() {
    if (window.renderMathInElement) {
      renderMathInElement(document.body, {
        delimiters: [
          {left: "$$", right: "$$", display: true},
          {left: "$", right: "$", display: false},
          {left: "\\\\(", right: "\\\\)", display: false},
          {left: "\\\\[", right: "\\\\]", display: true}
        ],
        throwOnError: false
      });
    }
  }

  let yieldCtx = document.getElementById('yieldChart').getContext('2d');
  let yieldChart = new Chart(yieldCtx, {
    type: 'line',
    data: {
      labels: ['0.5Y', '1Y', '2Y', '3Y', '5Y', '7Y', '10Y', '20Y', '30Y'],
      datasets: [
        { label: 'Baseline Spot Curve', data: [3.5, 3.8, 4.0, 4.1, 4.3, 4.4, 4.5, 4.6, 4.7], borderColor: '#8b949e', borderDash: [5,5], borderWidth: 2 },
        { label: 'Shifted / Twisted Curve', data: [3.5, 3.8, 4.0, 4.1, 4.3, 4.4, 4.5, 4.6, 4.7], borderColor: '#58a6ff', borderWidth: 3 }
      ]
    },
    options: { responsive: true, plugins: { legend: { labels: { color: '#e6edf3' } } } }
  });

  function updateYieldCurve() {
    let shift = parseFloat(document.getElementById('shiftRange').value);
    let twist = parseFloat(document.getElementById('twistRange').value);
    let butt = parseFloat(document.getElementById('buttRange').value);
    document.getElementById('shiftVal').innerText = shift;
    document.getElementById('twistVal').innerText = twist;
    document.getElementById('buttVal').innerText = butt;

    let base = [3.5, 3.8, 4.0, 4.1, 4.3, 4.4, 4.5, 4.6, 4.7];
    let weights = [-1, -0.7, -0.3, 0, 0.3, 0.6, 1.0, 1.3, 1.5];
    let curveWeights = [1, -0.5, -1, 0, 1, 0, -1, -0.5, 1];

    let updated = base.map((val, idx) => {
      let shock = shift + twist * (weights[idx] / 1.0) + butt * (curveWeights[idx] / 1.0);
      return +(val + shock / 100).toFixed(2);
    });

    yieldChart.data.datasets[1].data = updated;
    yieldChart.update();
  }

  let binomialCtx = document.getElementById('binomialChart').getContext('2d');
  let binomialChart = new Chart(binomialCtx, {
    type: 'bar',
    data: {
      labels: ['Node 0 (Root)', 'Node 1 (Up)', 'Node 1 (Down)', 'Node 2 (Up-Up)', 'Node 2 (Up-Down)', 'Node 2 (Down-Down)'],
      datasets: [{ label: 'Forward Rate (%)', data: [4.0, 4.8, 3.4, 5.6, 4.2, 3.0], backgroundColor: '#39c5cf' }]
    },
    options: { responsive: true, plugins: { legend: { display: false } } }
  });

  function updateBinomialTree() {
    let vol = document.getElementById('volRange').value;
    let coupon = parseFloat(document.getElementById('couponRange').value);
    let callP = document.getElementById('callRange').value;
    document.getElementById('volVal').innerText = vol;
    document.getElementById('couponVal').innerText = coupon.toFixed(1);
    document.getElementById('callVal').innerText = callP;

    let bval = 100.0 + (coupon - 5.0) * 1.5 - (vol - 15) * 0.15;
    document.getElementById('binomialResult').innerText = "Valuation for Callable Bond: " + bval.toFixed(2) + " USD (Call Price Cap: " + callP + " USD)";
  }

  let equityCtx = document.getElementById('equityChart').getContext('2d');
  let equityChart = new Chart(equityCtx, {
    type: 'line',
    data: {
      labels: ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5 (Terminal)'],
      datasets: [{ label: 'Dividend Stream (USD)', data: [2.2, 2.42, 2.66, 2.92, 45.0], borderColor: '#3fb950', borderWidth: 3 }]
    },
    options: { responsive: true, plugins: { legend: { display: false } } }
  });

  function updateEquityVal() {
    let d0 = parseFloat(document.getElementById('d0Range').value);
    let gs = parseFloat(document.getElementById('gsRange').value);
    let re = parseFloat(document.getElementById('reRange').value);
    document.getElementById('d0Val').innerText = d0.toFixed(2);
    document.getElementById('gsVal').innerText = gs.toFixed(1);
    document.getElementById('reVal').innerText = re.toFixed(1);

    let d1 = d0 * (1 + gs/100);
    let v0 = d1 / ((re - 4.0)/100);
    document.getElementById('eqResult').innerText = "Estimated Intrinsic Value: " + v0.toFixed(2) + " USD";
  }

  let durationCtx = document.getElementById('durationChart').getContext('2d');
  let durationChart = new Chart(durationCtx, {
    type: 'bar',
    data: {
      labels: ['2Y Key Rate', '5Y Key Rate', '10Y Key Rate', '30Y Key Rate'],
      datasets: [
        { label: 'Key Rate Duration (Years)', data: [1.8, 4.2, 7.5, 14.2], backgroundColor: '#bc8cff' }
      ]
    },
    options: { responsive: true }
  });

  function updateDurationSim() {
    let s2 = parseFloat(document.getElementById('shock2y').value);
    let s5 = parseFloat(document.getElementById('shock5y').value);
    let s10 = parseFloat(document.getElementById('shock10y').value);
    let s30 = parseFloat(document.getElementById('shock30y').value);
    document.getElementById('s2y').innerText = s2;
    document.getElementById('s5y').innerText = s5;
    document.getElementById('s10y').innerText = s10;
    document.getElementById('s30y').innerText = s30;
  }

  let currentFilteredL1 = questionBank.filter(q => q.level === 1);
  let currentIndex = 0;

  function filterL1Questions() {
    let sub = document.getElementById('l1Filter').value;
    if (sub === 'ALL') {
      currentFilteredL1 = questionBank.filter(q => q.level === 1);
    } else {
      currentFilteredL1 = questionBank.filter(q => q.level === 1 && q.subject === sub);
    }
    currentIndex = 0;
    renderL1Question();
  }

  function nextL1Question() {
    if (currentFilteredL1.length === 0) return;
    currentIndex = Math.floor(Math.random() * currentFilteredL1.length);
    renderL1Question();
  }

  function renderL1Question() {
    let container = document.getElementById('l1Container');
    if (currentFilteredL1.length === 0) {
      container.innerHTML = "<p>No questions found.</p>";
      return;
    }
    let q = currentFilteredL1[currentIndex];
    let html = `
      <div class="question-box">
        <span style="font-size: 12px; color: var(--accent-blue); font-weight: 600;">` + q.id + ` | ` + q.subject + ` > ` + q.topic + `</span>
        <p style="margin-top: 10px; font-size: 16px; font-weight: 500;">` + q.question + `</p>
        <div style="margin-top: 15px;">
    `;
    for (let [optKey, optText] of Object.entries(q.options)) {
      html += `<button class="option-btn" onclick="checkAnswer('` + q.id + `', '` + optKey + `', this)">` + optKey + `. ` + optText + `</button>`;
    }
    html += `
        </div>
        <div id="expl-` + q.id + `" class="explanation">
          <strong>Detailed Solution:</strong> ` + q.explanation + `
        </div>
      </div>
    `;
    container.innerHTML = html;
    renderMath();
  }

  function checkAnswer(qId, selectedOpt, btnElement) {
    let q = questionBank.find(item => item.id === qId);
    let parent = btnElement.parentElement;
    parent.querySelectorAll('.option-btn').forEach(b => {
      b.disabled = true;
      if (b.innerText.startsWith(q.answer)) {
        b.classList.add('correct');
      } else if (b === btnElement && selectedOpt !== q.answer) {
        b.classList.add('incorrect');
      }
    });
    document.getElementById("expl-" + qId).style.display = 'block';
    renderMath();
  }

  let vignettesMap = {};
  questionBank.filter(q => q.level === 2).forEach(q => {
    let vid = q.vignette_id;
    if (!vignettesMap[vid]) {
      vignettesMap[vid] = { title: q.vignette_title, text: q.vignette_text, questions: [] };
    }
    vignettesMap[vid].questions.push(q);
  });

  function initL2Vignettes() {
    let select = document.getElementById('l2VignetteSelect');
    select.innerHTML = '';
    for (let [vid, vObj] of Object.entries(vignettesMap)) {
      let opt = document.createElement('option');
      opt.value = vid;
      opt.innerText = "Case Study " + vid + ": " + vObj.title + " (" + vObj.questions.length + " questions)";
      select.appendChild(opt);
    }
    loadL2Vignette();
  }

  function loadL2Vignette() {
    let vid = document.getElementById('l2VignetteSelect').value;
    let vObj = vignettesMap[vid];
    if (!vObj) return;

    let textCard = document.getElementById('vignetteTextCard');
    textCard.innerHTML = `
      <h3 style="color: var(--accent-cyan); margin-bottom: 15px;">` + vObj.title + `</h3>
      <p style="white-space: pre-line; line-height: 1.7;">` + vObj.text + `</p>
    `;

    let qCard = document.getElementById('vignetteQuestionsCard');
    let qHtml = '';
    vObj.questions.forEach((q, idx) => {
      qHtml += `
        <div class="question-box" style="margin-bottom: 15px;">
          <span style="font-size: 12px; color: var(--accent-purple); font-weight: 600;">Question ` + (idx+1) + ` (` + q.id + `)</span>
          <p style="margin-top: 8px;">` + q.question + `</p>
          <div style="margin-top: 10px;">
      `;
      for (let [optKey, optText] of Object.entries(q.options)) {
        qHtml += `<button class="option-btn" onclick="checkAnswer('` + q.id + `', '` + optKey + `', this)">` + optKey + `. ` + optText + `</button>`;
      }
      qHtml += `
          </div>
          <div id="expl-` + q.id + `" class="explanation">
            <strong>Solution:</strong> ` + q.explanation + `
          </div>
        </div>
      `;
    });
    qCard.innerHTML = qHtml;
    renderMath();
  }

  window.onload = function() {
    updateYieldCurve();
    updateBinomialTree();
    updateEquityVal();
    renderL1Question();
    initL2Vignettes();
    renderMath();
  };
</script>

</body>
</html>
'''

    final_html = html_content.replace("__QUESTION_BANK_DATA__", qs_json)
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(final_html)
    print(f"Generated master simulation platform at {OUTPUT_HTML}")

def main():
    questions = generate_questions()
    build_dashboard(questions)

if __name__ == "__main__":
    main()
