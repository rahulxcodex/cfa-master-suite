import re
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPT_PATH = os.path.join(BASE_DIR, "scripts", "generate_full_dashboard.py")

with open(SCRIPT_PATH, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update navigation items in sidebar
nav_old = r'''      <li><a href="#sim-yield" onclick="switchTab('sim-yield')"><span>📈 Yield Curve Simulator</span></a></li>
      <li><a href="#sim-tree" onclick="switchTab('sim-tree')"><span>🌳 Binomial Tree Engine</span></a></li>
      <li><a href="#sim-equity" onclick="switchTab('sim-equity')"><span>📊 DDM & DuPont Explorer</span></a></li>
      <li><a href="#sim-duration" onclick="switchTab('sim-duration')"><span>⚡ Key Rate Duration</span></a></li>
      <li><a href="#reference-diagrams" onclick="switchTab('reference-diagrams')"><span>📐 Visual Diagrams</span></a></li>
    </ul>'''

nav_new = r'''      <li><a href="#sim-yield" onclick="switchTab('sim-yield')"><span>📈 Yield Curve Simulator</span></a></li>
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
    </ul>'''

assert nav_old in code, "Navigation snippet not found"
code = code.replace(nav_old, nav_new)

# 2. Update dynamic badges and stat-pills
old_pills = r'''      <div class="stats-pills">
        <div class="stat-pill" style="color: var(--accent-blue);">Total: 340 Questions</div>'''

new_pills = r'''      <div class="stats-pills">
        <a href="index.html" class="stat-pill" style="color: var(--accent-amber); text-decoration: none; border-color: rgba(210,153,34,0.4);">📚 View FSA Suite</a>
        <div class="stat-pill" style="color: var(--accent-blue);">Total: <span id="totalQuestionsDisplay">415</span> Questions</div>'''

assert old_pills in code, "Stats pills not found"
code = code.replace(old_pills, new_pills)

# 3. Add simulation HTML sections right before <section id="reference-diagrams">
diagram_section = r'    <!-- 8. REFERENCE DIAGRAMS -->'

simulations_html = r'''    <!-- 7B. SIMULATION: FRN PRICING ENGINE -->
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

''' + diagram_section

assert diagram_section in code, "Diagram section not found"
code = code.replace(diagram_section, simulations_html)

# 4. Update switchTab titles mapping
titles_old = r'''        'sim-yield': 'Interactive Yield Curve & Term Structure Simulator',
        'sim-tree': 'Binomial Interest Rate Tree & Embedded Option Engine',
        'sim-equity': 'Equity Valuation: Two-Stage DDM & DuPont Explorer',
        'sim-duration': 'Key Rate Duration & Sensitivity Visualizer',
        'reference-diagrams': 'CFA Reference Diagrams & Structural Models'
      };'''

titles_new = r'''        'sim-yield': 'Interactive Yield Curve & Term Structure Simulator',
        'sim-tree': 'Binomial Interest Rate Tree & Embedded Option Engine',
        'sim-equity': 'Equity Valuation: Two-Stage DDM & DuPont Explorer',
        'sim-duration': 'Key Rate Duration & Sensitivity Visualizer',
        'sim-frn': 'Floating-Rate Note (FRN) Pricing & Discount Margin Engine',
        'sim-ri-decay': 'Residual Income Persistence Decay Explorer',
        'sim-waterfall': 'FCFF to FCFE Cash Flow Waterfall Bridge',
        'sim-translation': 'Multinational Currency Translation Engine (Current vs Temporal)',
        'sim-prepayment': 'MBS Prepayment Simulator & Contraction/Extension Risk',
        'reference-diagrams': 'CFA Reference Diagrams & Structural Models'
      };'''

assert titles_old in code, "Titles dict not found"
code = code.replace(titles_old, titles_new)

# 5. Add JavaScript simulation logic and initialization before </script>
js_simulations = r'''
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
'''

init_old = r'''    // Initialization on window load
    window.addEventListener('DOMContentLoaded', () => {
      initOverviewChart();
      renderL1Question();
      initL2Engine();
      initYieldChart();
      updateTreeSim();
      initEquitySim();
      initDurationSim();
      renderMath();
    });'''

init_new = r'''    // Initialization on window load
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
    });'''

assert init_old in code, "Init on window load not found"
code = code.replace(init_old, js_simulations + "\n" + init_new)

# 6. Update question count references in code
code = code.replace("data: [85, 85, 85, 85]", "data: [120, 115, 85, 95]")
code = code.replace("<span>170 Q</span>", "<span>235 Q</span>")
code = code.replace("Total: 340 Questions", "Total: 415 Questions")

with open(SCRIPT_PATH, "w", encoding="utf-8") as f:
    f.write(code)

print(f"Successfully updated {SCRIPT_PATH}")
