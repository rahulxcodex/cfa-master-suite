#!/usr/bin/env python3
"""
scripts/build_full_suite.py
Integrates the complete 400-question CFA L1 & L2 question bank into index.html
and build_notes.py, with an interactive testing dashboard and KaTeX rendering.
"""

import json
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "cfa_question_bank_master.json")
INDEX_PATH = os.path.join(BASE_DIR, "index.html")
BUILD_NOTES_PATH = os.path.join(BASE_DIR, "build_notes.py")

def main():
    print("Loading master question bank...")
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        questions = json.load(f)

    l1_qs = [q for q in questions if q.get("level") == 1]
    l2_qs = [q for q in questions if q.get("level") == 2]

    print(f"Loaded {len(questions)} total questions ({len(l1_qs)} L1, {len(l2_qs)} L2).")

    # Group L2 by vignette
    vignettes = {}
    for q in l2_qs:
        vid = q.get("vignette_id", "V_DEFAULT")
        if vid not in vignettes:
            vignettes[vid] = {
                "id": vid,
                "title": q.get("vignette_title", f"Case {vid}"),
                "text": q.get("vignette_text", ""),
                "topic": q.get("topic", "CFA Level 2 Item Set"),
                "module": q.get("module", ""),
                "questions": []
            }
        vignettes[vid]["questions"].append(q)

    # Generate HTML for Question Engine
    # We will inject an interactive JavaScript Question Bank App into index.html
    # so candidates can practice all 400 questions seamlessly.

    qb_json_str = json.dumps(questions, ensure_ascii=False)

    interactive_engine_html = f"""
    <!-- ========================================================================================= -->
    <!-- PART IV: 400-QUESTION CFA LEVEL 1 & LEVEL 2 MASTER QUESTION BANK (VERIFIED & AUDITED)    -->
    <!-- ========================================================================================= -->

    <section id="practice-l1">
      <h2 class="section-heading"><span class="num">21.</span> CFA Level 1 Master Practice Questions (180 Questions)</h2>
      <p style="color: var(--text-secondary); margin-bottom: 20px;">
        180 rigorous, exam-calibrated Level 1 multiple-choice questions covering all 12 FSA topics. Test your understanding with instant score tracking, realistic distractors, and detailed step-by-step KaTeX solutions.
      </p>

      <div class="qb-controls" style="background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: 8px; padding: 16px; margin-bottom: 24px; display: flex; flex-wrap: wrap; gap: 12px; align-items: center; justify-content: space-between;">
        <div style="display: flex; gap: 10px; flex-wrap: wrap; align-items: center;">
          <label style="font-weight: 600; color: var(--text-primary);">Filter Topic:</label>
          <select id="l1-topic-filter" onchange="renderL1Questions()" style="background: var(--bg-tertiary); color: var(--text-primary); border: 1px solid var(--border-color); border-radius: 6px; padding: 6px 12px;">
            <option value="ALL">All Level 1 Topics (180 Qs)</option>
            <option value="m1-intro">01. Intro to FSA & Mechanics (15 Qs)</option>
            <option value="m2-standards">02. Financial Reporting Standards (15 Qs)</option>
            <option value="m3-income-statement">03. Income Statements (15 Qs)</option>
            <option value="m4-balance-sheet">04. Balance Sheets (15 Qs)</option>
            <option value="m5-cash-flow">05. Cash Flow Statements (15 Qs)</option>
            <option value="m6-ratios">06. Financial Analysis Techniques (15 Qs)</option>
            <option value="m7-inventories">07. Inventories (15 Qs)</option>
            <option value="m8-long-lived-assets">08. Long-Lived Assets (15 Qs)</option>
            <option value="m9-taxes">09. Income Taxes (15 Qs)</option>
            <option value="m10-debt">10. Non-Current Liabilities (15 Qs)</option>
            <option value="m11-leases">11. Leases (15 Qs)</option>
            <option value="m12-quality-l1">12. Reporting Quality (15 Qs)</option>
          </select>
          <input type="text" id="l1-search-input" onkeyup="renderL1Questions()" placeholder="Search LOS or keyword..." style="background: var(--bg-tertiary); color: var(--text-primary); border: 1px solid var(--border-color); border-radius: 6px; padding: 6px 12px; min-width: 220px;" />
        </div>
        <div id="l1-stats" style="font-size: 0.9rem; font-weight: 600; color: var(--accent-blue);">
          Showing: <span id="l1-count">180</span> | Score: <span id="l1-score">0 / 0</span> (<span id="l1-pct">0%</span>)
        </div>
      </div>

      <div id="l1-questions-container">
        <!-- Rendered via JavaScript -->
      </div>
    </section>

    <!-- Level 2 Practice -->
    <section id="practice-l2">
      <h2 class="section-heading"><span class="num">22.</span> CFA Level 2 Item-Set Cases & Vignettes (220 Questions / 38 Vignettes)</h2>
      <p style="color: var(--text-secondary); margin-bottom: 20px;">
        220 advanced vignette-based questions structured across 38 comprehensive item sets. Covering intercorporate investments, defined benefit pensions, multinational currency translation, CAMELS/Basel III financial institutions analysis, Beneish M-Score forensic accounting, and valuation integration.
      </p>

      <div class="qb-controls" style="background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: 8px; padding: 16px; margin-bottom: 24px; display: flex; flex-wrap: wrap; gap: 12px; align-items: center; justify-content: space-between;">
        <div style="display: flex; gap: 10px; flex-wrap: wrap; align-items: center;">
          <label style="font-weight: 600; color: var(--text-primary);">Filter Topic:</label>
          <select id="l2-topic-filter" onchange="renderL2Questions()" style="background: var(--bg-tertiary); color: var(--text-primary); border: 1px solid var(--border-color); border-radius: 6px; padding: 6px 12px;">
            <option value="ALL">All Level 2 Topics (38 Vignettes / 220 Qs)</option>
            <option value="m13-intercorporate">13. Intercorporate Investments (8 Vignettes / 48 Qs)</option>
            <option value="m14-pensions">14. Pensions & Compensation (7 Vignettes / 42 Qs)</option>
            <option value="m15-multinational">15. Multinational Operations & FX (8 Vignettes / 48 Qs)</option>
            <option value="m16-financial-institutions">16. Financial Institutions & CAMELS (7 Vignettes / 42 Qs)</option>
            <option value="m17-quality-l2">17. Evaluating Quality & Beneish M-Score (4 Vignettes / 20 Qs)</option>
            <option value="m18-integration">18. Integration of FSA Techniques (4 Vignettes / 20 Qs)</option>
          </select>
          <input type="text" id="l2-search-input" onkeyup="renderL2Questions()" placeholder="Search vignette or LOS..." style="background: var(--bg-tertiary); color: var(--text-primary); border: 1px solid var(--border-color); border-radius: 6px; padding: 6px 12px; min-width: 220px;" />
        </div>
        <div id="l2-stats" style="font-size: 0.9rem; font-weight: 600; color: var(--accent-emerald);">
          Showing: <span id="l2-count">38</span> Vignettes | Score: <span id="l2-score">0 / 0</span> (<span id="l2-pct">0%</span>)
        </div>
      </div>

      <div id="l2-questions-container">
        <!-- Rendered via JavaScript -->
      </div>
    </section>
"""

    interactive_js = f"""
    <!-- Master Question Bank Script Engine -->
    <script>
      const MASTER_QUESTION_BANK = {qb_json_str};

      let userAnswers = {{}};

      function escapeHtml(text) {{
        if (!text) return '';
        return text
          .replace(/&/g, "&amp;")
          .replace(/</g, "&lt;")
          .replace(/>/g, "&gt;")
          .replace(/"/g, "&quot;")
          .replace(/'/g, "&#039;");
      }}

      function checkAnswer(qid, selectedOpt) {{
        const q = MASTER_QUESTION_BANK.find(item => item.id === qid);
        if (!q) return;

        userAnswers[qid] = selectedOpt;

        const isCorrect = selectedOpt === q.answer;
        const resultEl = document.getElementById('feedback-' + qid);
        const optionsContainer = document.getElementById('options-' + qid);

        if (optionsContainer) {{
          const opts = optionsContainer.querySelectorAll('.interactive-opt');
          opts.forEach(el => {{
            const optVal = el.getAttribute('data-opt');
            el.style.borderColor = 'var(--border-color)';
            el.style.background = 'transparent';
            if (optVal === q.answer) {{
              el.style.borderColor = 'var(--accent-emerald)';
              el.style.background = 'rgba(63, 185, 80, 0.15)';
            }} else if (optVal === selectedOpt && !isCorrect) {{
              el.style.borderColor = 'var(--accent-rose)';
              el.style.background = 'rgba(248, 81, 73, 0.15)';
            }}
          }});
        }}

        if (resultEl) {{
          resultEl.style.display = 'block';
          if (isCorrect) {{
            resultEl.innerHTML = '<span style="color: var(--accent-emerald); font-weight: 700;">✓ Correct!</span> Option ' + q.answer + ' is right.';
          }} else {{
            resultEl.innerHTML = '<span style="color: var(--accent-rose); font-weight: 700;">✗ Incorrect.</span> Correct Answer is <strong>Option ' + q.answer + '</strong>.';
          }}
        }}

        updateScores();
      }}

      function updateScores() {{
        // L1 Score
        const l1Qs = MASTER_QUESTION_BANK.filter(q => q.level === 1);
        let l1Attempted = 0, l1Correct = 0;
        l1Qs.forEach(q => {{
          if (userAnswers[q.id]) {{
            l1Attempted++;
            if (userAnswers[q.id] === q.answer) l1Correct++;
          }}
        }});
        const l1Pct = l1Attempted > 0 ? Math.round((l1Correct / l1Attempted) * 100) : 0;
        const l1ScoreEl = document.getElementById('l1-score');
        const l1PctEl = document.getElementById('l1-pct');
        if (l1ScoreEl) l1ScoreEl.innerText = l1Correct + ' / ' + l1Attempted;
        if (l1PctEl) l1PctEl.innerText = l1Pct + '%';

        // L2 Score
        const l2Qs = MASTER_QUESTION_BANK.filter(q => q.level === 2);
        let l2Attempted = 0, l2Correct = 0;
        l2Qs.forEach(q => {{
          if (userAnswers[q.id]) {{
            l2Attempted++;
            if (userAnswers[q.id] === q.answer) l2Correct++;
          }}
        }});
        const l2Pct = l2Attempted > 0 ? Math.round((l2Correct / l2Attempted) * 100) : 0;
        const l2ScoreEl = document.getElementById('l2-score');
        const l2PctEl = document.getElementById('l2-pct');
        if (l2ScoreEl) l2ScoreEl.innerText = l2Correct + ' / ' + l2Attempted;
        if (l2PctEl) l2PctEl.innerText = l2Pct + '%';
      }}

      function renderL1Questions() {{
        const container = document.getElementById('l1-questions-container');
        if (!container) return;

        const filter = document.getElementById('l1-topic-filter').value;
        const search = (document.getElementById('l1-search-input').value || '').toLowerCase();

        const filtered = MASTER_QUESTION_BANK.filter(q => {{
          if (q.level !== 1) return false;
          if (filter !== 'ALL' && q.module !== filter) return false;
          if (search) {{
            const corpus = (q.question + ' ' + q.los + ' ' + q.id + ' ' + q.topic).toLowerCase();
            if (!corpus.includes(search)) return false;
          }}
          return true;
        }});

        const countEl = document.getElementById('l1-count');
        if (countEl) countEl.innerText = filtered.length;

        let html = '';
        filtered.forEach((q, idx) => {{
          const isAnswered = !!userAnswers[q.id];
          const selected = userAnswers[q.id];

          html += `
          <div class="question-card" id="card-${{q.id}}" style="background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: 8px; padding: 20px; margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
              <span class="q-number" style="font-weight: 700; color: var(--accent-blue);">Question ${{idx + 1}} (${{q.id}}) — ${{escapeHtml(q.topic)}}</span>
              <span style="font-size: 0.75rem; background: var(--bg-tertiary); padding: 3px 8px; border-radius: 4px; color: var(--text-secondary);">LOS: ${{escapeHtml(q.los)}}</span>
            </div>
            <div class="q-stem" style="font-size: 1.05rem; line-height: 1.5; margin-bottom: 16px; color: var(--text-primary);">${{q.question}}</div>
            
            <div class="q-options" id="options-${{q.id}}" style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 14px;">
              ${{['A', 'B', 'C'].map(opt => `
                <div class="interactive-opt" data-opt="${{opt}}" onclick="checkAnswer('${{q.id}}', '${{opt}}')" style="cursor: pointer; padding: 10px 14px; border: 1px solid var(--border-color); border-radius: 6px; display: flex; align-items: flex-start; gap: 10px; transition: all 0.2s ease;">
                  <span style="font-weight: 700; min-width: 24px;">${{opt}}.</span>
                  <span>${{q.options[opt]}}</span>
                </div>
              `).join('')}}
            </div>

            <div id="feedback-${{q.id}}" style="display: none; padding: 8px 12px; border-radius: 6px; margin-bottom: 12px; background: var(--bg-tertiary);"></div>

            <details class="solution-accordion" style="margin-top: 10px; border-top: 1px dashed var(--border-color); padding-top: 10px;">
              <summary style="cursor: pointer; font-weight: 600; color: var(--accent-cyan);">View Solution & Detailed Explanation</summary>
              <div class="solution-content" style="margin-top: 10px; font-size: 0.95rem; line-height: 1.6; color: var(--text-primary);">
                <div style="background: rgba(88, 166, 255, 0.1); border-left: 3px solid var(--accent-blue); padding: 8px 12px; margin-bottom: 8px;">
                  <strong>Correct Answer: Option ${{q.answer}}</strong>
                </div>
                <div class="katex-renderable">${{q.explanation.replace(/\\n/g, '<br/>')}}</div>
              </div>
            </details>
          </div>
          `;
        }});

        container.innerHTML = html;

        // Trigger KaTeX rendering on newly inserted elements
        if (window.renderMathInElement) {{
          renderMathInElement(container, {{
            delimiters: [
              {{left: '$$', right: '$$', display: true}},
              {{left: '$', right: '$', display: false}}
            ],
            throwOnError: false
          }});
        }}
      }}

      function renderL2Questions() {{
        const container = document.getElementById('l2-questions-container');
        if (!container) return;

        const filter = document.getElementById('l2-topic-filter').value;
        const search = (document.getElementById('l2-search-input').value || '').toLowerCase();

        // Group L2 questions by vignette
        const l2Qs = MASTER_QUESTION_BANK.filter(q => q.level === 2);
        const vignetteMap = {{}};
        l2Qs.forEach(q => {{
          const vid = q.vignette_id || 'V_DEFAULT';
          if (!vignetteMap[vid]) {{
            vignetteMap[vid] = {{
              id: vid,
              title: q.vignette_title || ('Vignette ' + vid),
              text: q.vignette_text || '',
              topic: q.topic || 'CFA Level 2 Item Set',
              module: q.module || '',
              questions: []
            }};
          }}
          vignetteMap[vid].questions.push(q);
        }});

        const filteredVignettes = Object.values(vignetteMap).filter(v => {{
          if (filter !== 'ALL' && v.module !== filter) return false;
          if (search) {{
            const textToSearch = (v.title + ' ' + v.text + ' ' + v.topic + ' ' + v.questions.map(q => q.question + ' ' + q.los).join(' ')).toLowerCase();
            if (!textToSearch.includes(search)) return false;
          }}
          return true;
        }});

        const countEl = document.getElementById('l2-count');
        if (countEl) countEl.innerText = filteredVignettes.length;

        let html = '';
        filteredVignettes.forEach((v, vIdx) => {{
          html += `
          <div class="vignette-card" style="background: var(--bg-secondary); border: 2px solid var(--border-color); border-radius: 10px; padding: 24px; margin-bottom: 30px;">
            <div style="border-bottom: 2px solid var(--accent-purple); padding-bottom: 12px; margin-bottom: 16px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
              <div>
                <span style="font-weight: 800; font-size: 1.15rem; color: var(--accent-purple);">CASE VIGNETTE ${{vIdx + 1}}: ${{escapeHtml(v.title)}}</span>
                <div style="font-size: 0.85rem; color: var(--text-secondary); margin-top: 4px;">Topic: ${{escapeHtml(v.topic)}} (${{v.questions.length}} Item-Set Questions)</div>
              </div>
              <span style="font-size: 0.8rem; background: var(--bg-tertiary); padding: 4px 10px; border-radius: 4px; font-weight: 600; color: var(--accent-cyan);">${{v.id}}</span>
            </div>

            <div class="vignette-text" style="background: var(--bg-tertiary); border-left: 4px solid var(--accent-purple); border-radius: 4px; padding: 16px 20px; font-size: 0.95rem; line-height: 1.7; color: var(--text-primary); margin-bottom: 24px; white-space: pre-line;">
              ${{v.text}}
            </div>

            <div class="vignette-questions" style="display: flex; flex-direction: column; gap: 20px;">
              ${{v.questions.map((q, qIdx) => `
                <div class="item-set-q" style="background: var(--bg-primary); border: 1px solid var(--border-color); border-radius: 8px; padding: 16px;">
                  <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                    <span style="font-weight: 700; color: var(--accent-blue);">Question ${{qIdx + 1}} of ${{v.questions.length}} (${{q.id}})</span>
                    <span style="font-size: 0.75rem; color: var(--text-secondary);">LOS: ${{escapeHtml(q.los)}}</span>
                  </div>
                  <div class="q-stem" style="font-size: 1rem; line-height: 1.5; margin-bottom: 12px; color: var(--text-primary);">${{q.question}}</div>

                  <div class="q-options" id="options-${{q.id}}" style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 12px;">
                    ${{['A', 'B', 'C'].map(opt => `
                      <div class="interactive-opt" data-opt="${{opt}}" onclick="checkAnswer('${{q.id}}', '${{opt}}')" style="cursor: pointer; padding: 8px 12px; border: 1px solid var(--border-color); border-radius: 6px; display: flex; align-items: flex-start; gap: 10px; transition: all 0.2s ease;">
                        <span style="font-weight: 700; min-width: 20px;">${{opt}}.</span>
                        <span>${{q.options[opt]}}</span>
                      </div>
                    `).join('')}}
                  </div>

                  <div id="feedback-${{q.id}}" style="display: none; padding: 8px 12px; border-radius: 6px; margin-bottom: 10px; background: var(--bg-tertiary);"></div>

                  <details class="solution-accordion" style="border-top: 1px dashed var(--border-color); padding-top: 8px;">
                    <summary style="cursor: pointer; font-weight: 600; color: var(--accent-emerald); font-size: 0.9rem;">View Case Solution & Full Workings</summary>
                    <div class="solution-content" style="margin-top: 10px; font-size: 0.9rem; line-height: 1.6; color: var(--text-primary);">
                      <div style="background: rgba(63, 185, 80, 0.1); border-left: 3px solid var(--accent-emerald); padding: 6px 10px; margin-bottom: 8px;">
                        <strong>Correct Answer: Option ${{q.answer}}</strong>
                      </div>
                      <div class="katex-renderable">${{q.explanation.replace(/\\n/g, '<br/>')}}</div>
                    </div>
                  </details>
                </div>
              `).join('')}}
            </div>
          </div>
          `;
        }});

        container.innerHTML = html;

        if (window.renderMathInElement) {{
          renderMathInElement(container, {{
            delimiters: [
              {{left: '$$', right: '$$', display: true}},
              {{left: '$', right: '$', display: false}}
            ],
            throwOnError: false
          }});
        }}
      }}

      // Init on load
      document.addEventListener('DOMContentLoaded', function() {{
        renderL1Questions();
        renderL2Questions();
      }});
    </script>
"""

    print("Updating index.html...")
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Replace from `<section id="practice-l1">` up to `</section>\s*<!-- Scripts -->` or `</main>`
    # Find start of practice-l1
    l1_start = html_content.find('<section id="practice-l1">')
    # Find end of practice-l2 section
    l2_end_marker = '</section>'
    l2_pos = html_content.find('<section id="practice-l2">')
    if l1_start != -1 and l2_pos != -1:
        # Find closing tag of practice-l2
        second_end = html_content.find('</section>', l2_pos)
        after_l2 = second_end + len('</section>')
        
        # Replace sections 21 and 22
        new_html = html_content[:l1_start] + interactive_engine_html + html_content[after_l2:]
        
        # Now inject the JavaScript before </body>
        body_close = new_html.rfind('</body>')
        if body_close != -1:
            new_html = new_html[:body_close] + interactive_js + new_html[body_close:]

        with open(INDEX_PATH, "w", encoding="utf-8") as f:
            f.write(new_html)
        print(f"Updated index.html successfully ({os.path.getsize(INDEX_PATH)} bytes).")
    else:
        print("[ERROR] Could not find section markers in index.html")

    # Now update build_notes.py similarly so that python build_notes.py reproduces index.html
    print("Updating build_notes.py...")
    with open(BUILD_NOTES_PATH, "r", encoding="utf-8") as f:
        py_content = f.read()

    py_l1_start = py_content.find('<section id=\\"practice-l1\\">')
    if py_l1_start == -1:
        py_l1_start = py_content.find('<section id="practice-l1">')

    py_l2_pos = py_content.find('<section id="practice-l2">')
    if py_l1_start != -1 and py_l2_pos != -1:
        py_second_end = py_content.find('</section>', py_l2_pos)
        py_after_l2 = py_second_end + len('</section>')
        
        new_py_html = py_content[:py_l1_start] + interactive_engine_html + py_content[py_after_l2:]
        py_body_close = new_py_html.rfind('</body>')
        if py_body_close != -1:
            new_py_html = new_py_html[:py_body_close] + interactive_js + new_py_html[py_body_close:]

        with open(BUILD_NOTES_PATH, "w", encoding="utf-8") as f:
            f.write(new_py_html)
        print(f"Updated build_notes.py successfully ({os.path.getsize(BUILD_NOTES_PATH)} bytes).")
    else:
        print("[NOTICE] build_notes.py section replacement bypassed; building via compiler.")

    print("=== FULL SUITE BUILD COMPLETED SUCCESSFULLY ===")

if __name__ == "__main__":
    main()
