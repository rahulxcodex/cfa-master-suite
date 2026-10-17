# CFA Master Suite — Repository Audit Report

**Audit date:** 17 October 2026  
**Repository:** https://github.com/rahulxcodex/cfa-master-suite  
**Branch reviewed:** `main`  
**Head commit reviewed:** `2c1ce3a6f0862151b29b44d1b36b4931adef9b7b`  
**Audit type:** Static repository/code/configuration review of publicly readable files. No local browser session, dependency install, performance profiling, or execution of the complete verification scripts was available in this review.

## Executive summary

The project is an ambitious static CFA study platform with a single-page dashboard, a large question bank, reference content, and interactive financial simulations. GitHub Pages deployment is configured and the latest reported deployment workflow run succeeded.

**Overall assessment: promising prototype; not yet evidence-backed as a production-grade exam-preparation product.** The largest concern is trustworthiness and consistency of the study content and validation system, followed by the large, tightly coupled HTML artifact and deployment that does not execute tests.

### Scorecard

| Area | Assessment | Why |
|---|---|---|
| Product scope | Strong | Broad question bank, reference content, and finance simulations are integrated into one experience. |
| Architecture / maintainability | Needs work | Large generated `index.html`, repeated generation scripts and multiple question-bank artifacts. |
| Automated quality gates | Weak | Current Pages workflow deploys files without running validation; verifier expectations conflict with the project state. |
| Content/data integrity | High-priority risk | Several competing question totals and master datasets; checked-in audit output is from a narrower 415-question bank. |
| Application security | Incomplete evidence | HTML is generated from question data; content insertion paths require systematic escaping and security tests. |
| Accessibility / UX | Not fully verified | CSS includes visible focus styling and responsive rules; keyboard semantics, screen-reader behavior and narrow-screen flows need live testing. |
| Deployment readiness | Partial | Pages deploy succeeds, but it is not a build/test pass and entire repository is published. |
| Documentation / open-source readiness | Weak | No root README was found; repository has no declared license in GitHub metadata. |

## Findings

### P0 — No evidence of content correctness at question level
**Severity: Critical product-trust risk; evidence is incomplete, not a claim that every answer is wrong.**

The app is marketed as a CFA Level I/II master exam preparation suite, and the internal context calls the bank “certified” and “audited.” The repository contains generated question-bank files and structural checks, but these checks primarily validate shape, counts, IDs, delimiter balance and presence of UI elements. They do not establish that every answer key, calculation, explanation, distractor or curriculum mapping is correct.

**Impact:** A structurally valid but mathematically incorrect explanation can actively teach a candidate the wrong method.

**Fix:**
1. Add deterministic numerical tests for questions with calculations (recompute each answer independently).
2. Add review metadata per question: source/curriculum objective, reviewer, review date, calculation/test status and confidence.
3. Add sampled subject-matter review and publish a transparent distinction between generated, reviewed and independently verified questions.
4. Avoid “certified” or “100% compliance” language unless backed by a defined, reproducible process.

### P1 — Stale and conflicting question totals and data sources
**Evidence:** `scripts/generate_unified_dashboard.py` header and SEO metadata still describe 875 questions, 3 subjects, 9 simulations and 84 vignettes. `.agents/CONTEXT.md` describes 1,085 questions across four subjects, 102 vignettes and 12 simulations. `scripts/verify_unified_suite.py` has a docstring saying 875 questions / 84 vignettes but asserts 1,085 questions, 545 L1, 540 L2 and 102 vignettes. `scripts/verify_final_suite.py` targets a separate 415-question FI/EQ dataset. The stored `data/fi_eq/audit_summary.json` is explicitly for 415 questions and contains many potential-currency warnings.

**Impact:** It is difficult to determine which artifacts are canonical, which tests are current, or whether the visible marketing copy matches the deployed product. “Audit passed” can refer to the wrong data generation stage.

**Fix:**
- Designate one canonical source dataset and make all generated outputs consume it.
- Move totals to computed metadata (or generate a manifest) rather than maintaining hard-coded totals across README, HTML, scripts and context notes.
- Add explicit dataset version / schema version / generation commit to each audit artifact.
- Split retired legacy verifiers into an archive or update them to current data, with clearly named targets.
- In CI, fail when displayed counts differ from the dataset actually embedded in `index.html`.

### P1 — Verification script has brittle or inconsistent assumptions
**Evidence:** `scripts/verify_unified_suite.py` makes fixed-count assertions and checks only selected HTML strings for simulation and reference IDs. It does not validate DOM integrity, JavaScript syntax, calculations, accessibility, mobile usability or browser errors. The number-count comments at the top disagree with the actual assertions. The audit parser's currency checks are regex-based; the existing 415-question audit output demonstrates that it flags many dollar signs appearing in math snippets, so warning counts are not a reliable signal on their own.

**Impact:** False positives waste review time; false confidence can result if a simplistic test passes despite a real defect.

**Fix:**
- Validate schema with a formal JSON Schema or typed model and informative failure summaries.
- Check uniqueness, required fields, subject/level distribution, vignette integrity, option/answer membership and cross-references.
- Parse math delimiters with logic that understands escaped characters and inline/display blocks rather than raw dollar counts.
- Add test fixtures for legitimate USD notation, inline math, display math, escaped currency, line breaks and malformed formulas.
- Test rendered MathJax/KaTeX output in a browser, not merely source delimiter parity.

### P1 — Deployment workflow does not run checks before publishing
**Evidence:** `.github/workflows/pages.yml` checks out the repository, configures Pages, uploads the entire repository root (`path: '.'`) and deploys it. It does not install dependencies, run Python validators, run JS checks, or perform a browser smoke test. The latest reported workflow run succeeded, but its workflow only demonstrates that the deployment job completed.

**Impact:** Broken content, stale counts or a JavaScript runtime regression can be published while CI remains green.

**Fix:**
- Add a separate `quality` job that runs JSON/schema and math validation, Python syntax checks, formatting/linting, JS checks and smoke tests.
- Make Pages depend on quality checks succeeding.
- Publish a clean `dist/` folder containing only production assets.
- Use minimal workflow permissions, pin third-party actions to full commit SHAs where practical, and keep deployment isolated from test steps.

### P1 — Large monolithic, generated HTML is difficult to maintain and test
**Evidence:** Git tree lists `index.html` at about 2.62 MB, along with large generated Python files (for example `build_notes.py` is about 1.09 MB) and multiple generation/build scripts. The UI, content, data and simulation implementation are tightly coupled in the generated output.

**Impact:** Code review is noisy; small changes risk unintended replacement of unrelated content; browser parse/render cost and debugging complexity grow with the page.

**Fix:**
- Separate app shell, navigation, question engine, reference notes, and each simulation into modules/components.
- Keep question content as structured JSON loaded independently, and version it separately from rendering code.
- Have a reproducible build output assembled from source; do not edit generated files manually.
- Add a generated-file header with the exact script and data revision that produced each artifact.

### P1 — User-generated/content data is interpolated into HTML without consistently escaping every field
**Evidence:** `scripts/build_full_suite.py` builds question markup with template strings and interpolates fields such as `q.question`, `q.options[opt]`, `q.explanation`, and `v.text` into HTML. It defines `escapeHtml`, but the displayed implementation does not escape all content inserted into HTML. The current content appears to be repository-authored static JSON, so this is not proof of an exploitable remotely supplied input today; it is a dangerous maintenance boundary.

**Impact:** An accidental HTML fragment or future imported/contributed content can break layout or execute markup/script in the page. Static hosting does not remove DOM XSS risks.

**Fix:**
- Escape text for the correct output context before inserting it into HTML.
- Prefer DOM construction and `textContent` for plain text; allow rich text only through a deliberately configured sanitizer.
- Never treat a string as safe HTML solely because it came from a checked-in JSON file.
- Add tests containing `<script>`, event-handler attributes, quotes, ampersands and encoded markup to verify non-execution.

### P1 — External browser dependencies have no observed resilience strategy
**Evidence:** Generated page loads KaTeX CSS/JS, auto-render and Chart.js from jsDelivr and fonts from Google Fonts. Chart.js is included without an observed version pin in the fetched generator snippet; KaTeX is pinned to 0.16.9. No fallback strategy or Content Security Policy is visible in the reviewed `vercel.json` and page template excerpts.

**Impact:** A CDN outage, blocked third-party requests, or upstream change may degrade math rendering, charts, typography or parts of the learning experience. Unpinned dependencies can introduce nondeterministic behavior.

**Fix:**
- Pin every CDN dependency to an exact version and, where practical, use SRI hashes.
- Consider vendoring critical assets for stable offline-ish learning.
- Add graceful fallbacks when math/chart libraries fail to load.
- Consider a strict Content Security Policy after testing inline scripts/styles and required hosts; deploy it as an HTTP header.
- Test behavior with third-party requests blocked.

### P2 — Security headers are incomplete and one configured header is obsolete
**Evidence:** `vercel.json` sets `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY` and `X-XSS-Protection: 1; mode=block`. The page is also deployed with GitHub Pages using a different workflow, so it is not confirmed that these Vercel settings apply to the live GitHub Pages domain.

**Impact:** The presence of a header in `vercel.json` does not demonstrate that GitHub Pages sends it. The legacy XSS header is obsolete and should not be treated as a meaningful protection against DOM injection.

**Fix:**
- Check actual response headers at the canonical live URL.
- Add the applicable security headers at the hosting layer where supported; prioritize CSP and correct output escaping.
- Remove reliance on `X-XSS-Protection`; test framing restrictions and any embed use cases.

### P2 — Root documentation is missing and repository licensing is undefined
**Evidence:** `README.md` was not found at the repository root. GitHub repo metadata reports no declared license.

**Impact:** New users cannot quickly discover the deployment URL, setup/build commands, feature map, limitations or contribution process. Without a license, reuse and redistribution terms are unclear.

**Fix:**
- Add a README with live demo link, current scope/counts, architecture, local preview, regeneration and verification commands, known limitations and data provenance.
- Choose and add a license only after deciding which code/content can be licensed, including review of any third-party-derived CFA materials.
- Add a contribution guide and security reporting instructions if the repo is open for contributions.

### P2 — Curriculum coverage is explicitly incomplete
**Evidence:** The generator contains a curriculum table marking Ethical & Professional Standards, Quantitative Methods and Economics as “OMITTED” and relegating them to a future roadmap. The project description emphasizes FSA, Fixed Income, Equity and Portfolio Management, so this can be acceptable for a focused scope, but it is not a full-syllabus CFA prep suite.

**Impact:** Users may overestimate exam readiness if the product title and marketing imply comprehensive exam coverage.

**Fix:**
- Clearly label the platform as a focused subject suite until remaining topic areas are built and reviewed.
- Add coverage dashboards by exam level, subject and learning outcome, with missing areas explicit and up to date.
- Reconcile coverage claims with the current CFA curriculum year and re-audit when curriculum changes.

### P2 — Interactive simulations need numerical, boundary and accessibility tests
**Evidence:** The generator contains custom simulation logic such as a stochastic 30-day rebalancing path and hand-coded financial chart models. The current verifier checks that element IDs/labels exist but does not test model outputs. UI code has a visible-focus style and responsive CSS, but no end-to-end keyboard or screen-reader evidence was established.

**Impact:** A chart can render successfully while showing mathematically inconsistent values. Sliders and interactive controls can also be difficult to use without a mouse.

**Fix:**
- Build unit tests from known finance examples and test boundary values, sign conventions, rates, units and rounding.
- Separate calculation functions from chart rendering and test calculations independently.
- Test every simulation at minimum, default and maximum control values.
- Use native labeled controls, keyboard-operable interactions, accessible names and live result announcements where needed.
- Run automated accessibility checks and manual keyboard/mobile review.

### P2 — SEO and metadata are stale
**Evidence:** The current generator metadata uses 875 questions / 9 simulations and three subject labels even though the project context and current page scope state 1,085 questions / 12 simulations across four subjects. `sitemap.xml` has last-modified dates from 2026-10-04 while the repository was updated on 2026-10-17.

**Impact:** Search/social previews and sitemap freshness may misrepresent the live app.

**Fix:** Generate page metadata and sitemap from the same manifest as the site, and update counts / dates as part of the build.

### P3 — Repository hygiene and audit artifact lifecycle
**Evidence:** The repo includes `.agents/scratch/` generation scripts, but the root `.gitignore` includes `.agents/scratch/` only to prevent future additions; already committed tracked files are not removed by a gitignore rule. The tree currently includes numerous scratch builders. Older builders and verifier scripts refer to 400/415/875-question generations.

**Impact:** The root repository is harder to navigate and it becomes easier to invoke the wrong script or ship stale code/data.

**Fix:** Move one-off scratch work to local-only ignored files or an archive branch, untrack scratch material that should not be public, and place active build/test entry points in a documented Makefile or task runner. Retain artifacts only when they are reproducible and maintained.

## Security / correctness notes

- The deployment workflow is publicly readable; no secret value was established in the inspected snippets. A complete secret scan and history scan were not performed, so this is not a clean bill of health.
- I did not establish a confirmed, exploitable XSS path from a live untrusted input. The issue is an unsafe HTML-generation pattern that should be corrected before content sources expand.
- I did not execute the Python scripts against a local checkout or run the page in a real browser. No pass/fail result is claimed for JavaScript syntax, console errors, rendering, or real-world performance.
- The stored `data/fi_eq/audit_summary.json` is not evidence that the current 1,085-question page passed its current validation suite.

## Recommended remediation order

### First 1–2 days
1. Reconcile the canonical question-bank file and current counts across app, generator, tests and metadata.
2. Fix or retire the stale 415 / 875 / 1,085 verification scripts; make CI actually run the current validators.
3. Validate all question objects and compute a first-pass answer-key / numerical sanity report.
4. Escape HTML-bound content and add regression tests for unsafe markup.
5. Add a concise README with truthful current scope and local setup.

### Next week
1. Add CI gates for Python syntax, JSON schema/data integrity, JS syntax, math rendering and browser smoke tests.
2. Add baseline numerical tests for all simulation engines and sampled question solutions.
3. Break the single HTML artifact into maintainable source modules and generate `dist/` reproducibly.
4. Verify live security headers, pin dependencies, and add safe failure handling for CDN outages.
5. Add keyboard, mobile, and accessibility checks.

### Before calling it production-ready
1. Complete a documented curriculum coverage map for the exact curriculum year.
2. Independently review high-impact/high-frequency question explanations and numerical answers.
3. Run full end-to-end testing on desktop and mobile, including offline/CDN-blocked scenarios.
4. Publish only after repeatable quality checks pass against the exact commit being deployed.

## Verification evidence

- Repository: https://github.com/rahulxcodex/cfa-master-suite
- Current generator: https://github.com/rahulxcodex/cfa-master-suite/blob/main/scripts/generate_unified_dashboard.py
- Unified verifier: https://github.com/rahulxcodex/cfa-master-suite/blob/main/scripts/verify_unified_suite.py
- Legacy verifier: https://github.com/rahulxcodex/cfa-master-suite/blob/main/scripts/verify_final_suite.py
- Deployment workflow: https://github.com/rahulxcodex/cfa-master-suite/blob/main/.github/workflows/pages.yml
- Existing audit artifact: https://github.com/rahulxcodex/cfa-master-suite/blob/main/data/fi_eq/audit_summary.json
- Project context: https://github.com/rahulxcodex/cfa-master-suite/blob/main/.agents/CONTEXT.md
- Latest observed deployment workflow run: https://github.com/rahulxcodex/cfa-master-suite/actions/runs/39047865661

---

**Bottom line:** The breadth of the project is a strength, but the highest-priority work is establishing one canonical dataset and a validation pipeline that proves both structural integrity and financial correctness. A green static deployment alone should not be presented as evidence that the question bank or simulations are fully audited.
