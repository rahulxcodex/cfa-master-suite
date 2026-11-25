#!/usr/bin/env python3
"""
generate_unified_dashboard.py
Compiles the complete, unified CFA Master Study Dashboard into index.html
Housing all 2,210 questions across all 10 CBOK subjects, 183 L2 vignettes, 16 financial simulations,
63 master solved numericals, 64 jargon terms, and all 10 curriculum reference libraries (105 chapters)
with KaTeX math rendering and Chart.js telemetry.
Also writes a backward-compatibility redirect at fi_eq_dashboard.html.
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
MASTER_JSON = os.path.join(DATA_DIR, "cfa_master_855.json")
FSA_REF_HTML = os.path.join(DATA_DIR, "fsa_reference_extracted.html")
OUTPUT_INDEX = os.path.join(BASE_DIR, "index.html")
OUTPUT_FI_EQ = os.path.join(BASE_DIR, "fi_eq_dashboard.html")

dashboard_template = r'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CFA Master Study Platform: Complete CBOK I–XII Suite (L1 & L2)</title>
  
  <meta name="description" content="Unified CFA Program Level 1 & Level 2 Master Exam Preparation Suite. 2,210 audited questions across all 10 CFA CBOK courses (Ethics, Quant, Economics, FSA, Corporate Issuers, Equities, Fixed Income, Derivatives, Alternatives, Portfolio Management), with 183 case vignettes, 16 simulation engines, 63 solved numericals, and 105 curriculum chapters.">
  <link rel="canonical" href="https://rahulxcodex.github.io/cfa-master-suite/">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🎓</text></svg>">
  <meta property="og:title" content="CFA Master Study Platform (2,210 Questions, 16 Sims, All 10 CBOK Courses)">
  <meta property="og:description" content="Comprehensive CFA L1 & L2 prep platform: 2,210 questions, 183 vignettes, 16 simulations, 63 solved numericals, and 105 chapters across all CBOK courses.">
  <meta property="og:url" content="https://rahulxcodex.github.io/cfa-master-suite/">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  
    <!-- Anti-AI Design: Editorial Serif, Humanist UI & Financial Monospace Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400;1,6..72,600&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">

  <!-- KaTeX for crisp LaTeX math rendering -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
  
  <!-- Chart.js for interactive simulations & telemetry -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

  <style>
    html {
      scroll-behavior: smooth;
    }
    :focus-visible {
      outline: 2px solid var(--accent-blue);
      outline-offset: 2px;
    }
    ::-webkit-scrollbar {
      width: 8px;
      height: 8px;
    }
    ::-webkit-scrollbar-track {
      background: var(--bg-primary);
    }
    ::-webkit-scrollbar-thumb {
      background: var(--border-color);
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: var(--text-secondary);
    }
    :root {
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
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: var(--font-sans);
      background-color: var(--bg-primary);
      color: var(--text-primary);
      line-height: 1.6;
      font-size: 14px;
      display: flex;
      min-height: 100vh;
      overflow-x: hidden;
    }

    /* Sidebar Navigation */
    aside {
      width: var(--sidebar-width);
      background: var(--bg-secondary);
      border-right: 1px solid var(--border-color);
      height: 100vh;
      position: sticky;
      top: 0;
      display: flex;
      flex-direction: column;
      flex-shrink: 0;
      z-index: 100;
    }
    .sidebar-header {
      padding: 20px 18px 14px 18px;
      border-bottom: 1px solid var(--border-color);
    }
    .sidebar-header h1 {
      font-size: 17px;
      font-weight: 700;
      color: var(--accent-blue);
      letter-spacing: -0.3px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .sidebar-header p {
      font-size: 11px;
      color: var(--text-secondary);
      margin-top: 4px;
    }
    .nav-links {
      list-style: none;
      padding: 12px;
      overflow-y: auto;
      flex-grow: 1;
    }
    .nav-links li { margin-bottom: 4px; }
    .nav-links a {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 8px 12px;
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
      font-size: 10.5px;
      background: var(--bg-primary);
      padding: 2px 7px;
      border-radius: 10px;
      border: 1px solid var(--border-color);
      color: var(--text-secondary);
    }
    .nav-divider {
      padding: 12px 10px 4px 10px;
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-secondary);
    }

    /* Main Container */
    main {
      flex: 1 1 auto;
      min-width: 0;
      padding: 0 45px 35px 45px;
      max-width: 1550px;
      overflow-y: auto;
      min-height: 100vh;
    }

    .top-bar {
      position: sticky;
      top: 0;
      z-index: 50;
      background: var(--bg-primary);
      padding: 24px 0 16px 0;
      margin-bottom: 25px;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 15px;
      flex-wrap: wrap;
      backdrop-filter: blur(8px);
    }
    .top-bar h2 {
      font-size: 22px;
      font-weight: 700;
      color: var(--text-primary);
    }
    .stats-pills {
      display: flex;
      gap: 10px;
      align-items: center;
      flex-wrap: wrap;
    }
    .stat-pill {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      padding: 6px 12px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .btn-top {
      background: var(--bg-tertiary);
      color: var(--text-primary);
      border: 1px solid var(--border-color);
      padding: 6px 12px;
      border-radius: 6px;
      cursor: pointer;
      font-weight: 600;
      font-size: 12px;
      transition: background 0.15s;
    }
    .btn-top:hover {
      background: var(--border-color);
    }

    main > section { display: none; }
    main > section.active { display: block; animation: fadeIn 0.2s ease-in-out; }
    .fsa-ref-container section { display: block !important; margin-bottom: 3.5rem; scroll-margin-top: 80px; }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(4px); } to { opacity: 1; transform: translateY(0); } }

    /* Notes Library Classes & Rich Typography */
    .doc-hero {
      padding: 2.2rem 2rem;
      background: linear-gradient(135deg, rgba(88, 166, 255, 0.08), rgba(57, 197, 207, 0.04));
      border: 1px solid var(--border-color);
      border-radius: 12px;
      margin-bottom: 2.5rem;
    }
    .doc-hero h1 {
      font-size: 2.2rem;
      font-weight: 800;
      color: var(--text-primary);
      letter-spacing: -0.02em;
      margin-bottom: 0.6rem;
    }
    .doc-hero p {
      font-size: 1.02rem;
      color: var(--text-secondary);
      max-width: 850px;
      line-height: 1.6;
    }
    .meta-tags {
      display: flex;
      flex-wrap: wrap;
      gap: 0.6rem;
      margin-top: 1.2rem;
    }
    .badge {
      display: inline-block;
      padding: 0.25rem 0.65rem;
      border-radius: 20px;
      font-size: 0.75rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .badge-blue { background: rgba(88, 166, 255, 0.15); color: var(--accent-blue); border: 1px solid rgba(88, 166, 255, 0.3); }
    .badge-green { background: rgba(63, 185, 80, 0.15); color: var(--accent-emerald); border: 1px solid rgba(63, 185, 80, 0.3); }
    .badge-purple { background: rgba(188, 140, 255, 0.15); color: var(--accent-purple); border: 1px solid rgba(188, 140, 255, 0.3); }
    .badge-amber { background: rgba(210, 153, 34, 0.15); color: var(--accent-amber); border: 1px solid rgba(210, 153, 34, 0.3); }

    h2.section-heading {
      font-size: 1.6rem;
      font-weight: 700;
      color: var(--text-primary);
      border-bottom: 2px solid var(--border-color);
      padding-bottom: 0.6rem;
      margin-bottom: 1.5rem;
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }
    h2.section-heading span.num {
      color: var(--accent-blue);
      font-size: 1.25rem;
      font-weight: 800;
    }
    h3.subheading {
      font-size: 1.25rem;
      font-weight: 600;
      color: var(--text-primary);
      margin: 1.75rem 0 0.75rem;
    }

    .callout {
      padding: 1.25rem 1.5rem;
      border-radius: 8px;
      margin: 1.5rem 0;
      border-left: 4px solid var(--accent-blue);
      background: var(--bg-secondary);
      border-top: 1px solid var(--border-color);
      border-right: 1px solid var(--border-color);
      border-bottom: 1px solid var(--border-color);
    }
    .callout-tip { border-left-color: var(--accent-emerald); }
    .callout-warning { border-left-color: var(--accent-amber); }
    .callout-danger { border-left-color: var(--accent-rose); }
    .callout-info { border-left-color: var(--accent-blue); }
    .callout-title {
      font-weight: 700;
      font-size: 0.95rem;
      margin-bottom: 0.4rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .callout-tip .callout-title { color: var(--accent-emerald); }
    .callout-warning .callout-title { color: var(--accent-amber); }
    .callout-danger .callout-title { color: var(--accent-rose); }
    .callout-info .callout-title { color: var(--accent-blue); }

    .table-container, .table-wrap {
      overflow-x: auto;
      margin: 1.5rem 0;
      border: 1px solid var(--border-color);
      border-radius: 8px;
    }

    .formula-card {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 1.25rem 1.5rem;
      margin: 1.25rem 0;
      text-align: center;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .formula-title {
      font-size: 0.82rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-secondary);
      margin-bottom: 0.5rem;
      font-weight: 600;
    }

    .chart-box {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 1.5rem;
      margin: 2rem 0;
    }
    .chart-header { margin-bottom: 1rem; }
    .chart-title { font-size: 1rem; font-weight: 600; color: var(--text-primary); }
    .chart-desc { font-size: 0.82rem; color: var(--text-secondary); }
    .chart-canvas-wrap { position: relative; width: 100%; height: 320px; }

    .top-controls {
      display: flex;
      justify-content: flex-end;
      align-items: center;
      gap: 1rem;
      margin-bottom: 1.5rem;
    }
    .btn-ctrl {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      color: var(--text-primary);
      padding: 0.4rem 0.85rem;
      border-radius: 6px;
      font-size: 0.82rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: border-color 0.2s ease;
    }
    .btn-ctrl:hover {
      border-color: var(--accent-blue);
      color: var(--accent-blue);
    }

    /* Reference Subject Switcher & Anchor Offsets */
    .notes-subject-tabs {
      display: flex;
      gap: 8px;
      margin-bottom: 20px;
      flex-wrap: wrap;
    }
    .notes-tab-btn {
      padding: 7px 12px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      border: 1px solid var(--border-color);
      background: var(--bg-secondary);
      color: var(--text-secondary);
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .notes-tab-btn:hover {
      color: var(--text-primary);
      border-color: var(--accent-blue);
      background: var(--bg-tertiary);
    }
    .notes-tab-btn.active {
      color: #ffffff;
      background: var(--accent-blue);
      border-color: var(--accent-blue);
      box-shadow: 0 2px 8px rgba(88, 166, 255, 0.3);
    }
    .notes-chapter, section, [id^="m"], [id^="eth-"], [id^="qm-"], [id^="econ-"], [id^="corp-"], [id^="deriv-"], [id^="alt-"], [id^="fi-"], [id^="eq-"], [id^="pm-"], #master-gaap-ifrs, #master-formulas, #fi-formulas, #eq-formulas, #pm-formulas {
      scroll-margin-top: 85px;
    }

    /* Cards & Layout */
    .card {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 22px;
      margin-bottom: 22px;
    }
    .card-title {
      font-size: 16px;
      font-weight: 700;
      margin-bottom: 12px;
      color: var(--accent-cyan);
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .grid-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 22px;
    }
    .grid-3 {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 18px;
    }
    .grid-4 {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
    }
    .grid-5 {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 14px;
    }
    @media (max-width: 1200px) {
      .grid-5 { grid-template-columns: repeat(3, 1fr); }
    }
    @media (max-width: 768px) {
      .grid-5 { grid-template-columns: 1fr; }
    }
    .filter-pills {
      display: inline-flex;
      gap: 4px;
      background: var(--bg-tertiary);
      padding: 3px;
      border-radius: 6px;
      border: 1px solid var(--border-color);
    }
    .filter-pill {
      padding: 5px 12px;
      border-radius: 4px;
      border: none;
      background: transparent;
      color: var(--text-secondary);
      font-size: 11.5px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .filter-pill:hover {
      color: var(--text-primary);
    }
    .filter-pill.active {
      background: var(--accent-blue);
      color: #ffffff;
      box-shadow: 0 1px 4px rgba(0,0,0,0.2);
    }

    /* Controls & Forms */
    .control-group { margin-bottom: 14px; }
    .control-group label {
      display: block;
      font-weight: 600;
      margin-bottom: 5px;
      color: var(--text-primary);
      font-size: 12.5px;
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
      padding: 8px 16px;
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
    .btn-group {
      display: flex;
      gap: 8px;
      align-items: center;
      flex-wrap: wrap;
    }

    /* Question UI */
    .question-box {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 22px;
      margin-bottom: 20px;
      position: relative;
    }
    .question-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
      gap: 10px;
      flex-wrap: wrap;
    }
    .question-id-badge {
      font-size: 12px;
      font-weight: 700;
      color: var(--accent-blue);
      background: var(--bg-primary);
      padding: 4px 9px;
      border-radius: 4px;
      border: 1px solid var(--border-color);
    }
    .subject-badge {
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .badge-fsa { background: rgba(210, 153, 34, 0.15); color: var(--accent-amber); border: 1px solid rgba(210, 153, 34, 0.3); }
    .badge-fi { background: rgba(57, 197, 207, 0.15); color: var(--accent-cyan); border: 1px solid rgba(57, 197, 207, 0.3); }
    .badge-eq { background: rgba(63, 185, 80, 0.15); color: var(--accent-emerald); border: 1px solid rgba(63, 185, 80, 0.3); }
    .badge-pm { background: rgba(188, 140, 255, 0.15); color: var(--accent-purple); border: 1px solid rgba(188, 140, 255, 0.3); }
    .badge-eth { background: rgba(248, 81, 73, 0.15); color: var(--accent-rose); border: 1px solid rgba(248, 81, 73, 0.3); }
    .badge-qm { background: rgba(59, 130, 246, 0.15); color: var(--accent-blue); border: 1px solid rgba(59, 130, 246, 0.3); }
    .badge-econ { background: rgba(8, 145, 178, 0.15); color: var(--accent-cyan); border: 1px solid rgba(8, 145, 178, 0.3); }
    .badge-corp { background: rgba(217, 119, 6, 0.15); color: var(--accent-amber); border: 1px solid rgba(217, 119, 6, 0.3); }
    .badge-deriv { background: rgba(124, 58, 237, 0.15); color: var(--accent-purple); border: 1px solid rgba(124, 58, 237, 0.3); }
    .badge-alt { background: rgba(16, 185, 129, 0.15); color: var(--accent-emerald); border: 1px solid rgba(16, 185, 129, 0.3); }
    .badge-cyan { background: rgba(57, 197, 207, 0.15); color: var(--accent-cyan); border: 1px solid rgba(57, 197, 207, 0.3); }
    .badge-emerald { background: rgba(16, 185, 129, 0.15); color: var(--accent-emerald); border: 1px solid rgba(16, 185, 129, 0.3); }

    .question-los {
      font-size: 11.5px;
      color: var(--text-secondary);
      background: var(--bg-tertiary);
      border: 1px solid var(--border-color);
      border-radius: 4px;
      padding: 3px 8px;
      display: inline-block;
      max-width: 100%;
    }
    .question-text {
      font-size: 14.5px;
      line-height: 1.6;
      font-weight: 500;
      margin-bottom: 18px;
    }
    .options-container {
      display: flex;
      flex-direction: column;
      gap: 9px;
    }
    .option-btn {
      display: flex;
      align-items: center;
      width: 100%;
      text-align: left;
      padding: 11px 16px;
      background: var(--bg-primary);
      border: 1px solid var(--border-color);
      color: var(--text-primary);
      border-radius: 6px;
      cursor: pointer;
      font-size: 13.5px;
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
      margin-top: 18px;
      padding: 18px;
      background: var(--bg-primary);
      border-left: 4px solid var(--accent-cyan);
      border-radius: 6px;
      display: none;
    }
    .explanation-title {
      font-size: 13.5px;
      font-weight: 700;
      color: var(--accent-cyan);
      margin-bottom: 8px;
    }
    .distractor-box {
      margin-top: 12px;
      padding: 12px;
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: 6px;
      font-size: 12.5px;
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
      gap: 18px;
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

    /* Reference Section Styling */
    .fsa-ref-container {
      line-height: 1.7;
    }
    .fsa-ref-container h2 {
      font-size: 20px;
      color: var(--accent-blue);
      margin: 30px 0 15px 0;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 8px;
    }
    .fsa-ref-container h3 {
      font-size: 16px;
      color: var(--accent-cyan);
      margin: 20px 0 10px 0;
    }
    .fsa-ref-container p {
      margin-bottom: 14px;
    }
    .fsa-ref-container table {
      width: 100%;
      border-collapse: collapse;
      margin: 18px 0;
      font-size: 13px;
    }
    .fsa-ref-container th, .fsa-ref-container td {
      padding: 10px 14px;
      border: 1px solid var(--border-color);
      text-align: left;
    }
    .fsa-ref-container th {
      background: var(--bg-secondary);
      color: var(--accent-blue);
      font-weight: 600;
    }
    .fsa-ref-container tr:nth-child(even) {
      background: var(--bg-secondary);
    }
    .fsa-nav-bar {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-bottom: 25px;
      padding: 14px;
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: 8px;
    }
    .fsa-nav-btn {
      background: var(--bg-tertiary);
      color: var(--text-primary);
      border: 1px solid var(--border-color);
      padding: 5px 10px;
      border-radius: 4px;
      font-size: 12px;
      text-decoration: none;
      transition: background 0.15s;
    }
    .fsa-nav-btn:hover {
      background: var(--border-color);
      color: var(--accent-blue);
    }

    /* Mobile Drawer & Backdrop Navigation */
    .menu-toggle-btn {
      display: none;
      background: var(--bg-tertiary);
      color: var(--text-primary);
      border: 1px solid var(--border-color);
      padding: 6px 12px;
      border-radius: 6px;
      cursor: pointer;
      font-weight: 700;
      font-size: 13px;
      align-items: center;
      gap: 6px;
      transition: background 0.15s;
    }
    .menu-toggle-btn:hover {
      background: var(--border-color);
    }
    .sidebar-backdrop {
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(0, 0, 0, 0.65);
      backdrop-filter: blur(2px);
      z-index: 99;
    }
    .sidebar-backdrop.active {
      display: block;
    }
    .sidebar-close-btn {
      display: none;
      padding: 4px 8px;
      font-size: 11px;
      margin-top: 2px;
    }
    .l2-filter-grid {
      display: grid;
      grid-template-columns: 1.1fr 1.8fr 1.1fr;
      gap: 16px;
    }
    @media (max-width: 1000px) {
      .l2-filter-grid { grid-template-columns: 1fr; }
    }

    /* Responsive adjustments */
    @media (max-width: 900px) {
      .menu-toggle-btn { display: inline-flex; }
      .sidebar-close-btn { display: inline-flex; }
      #desktopSidebarToggle { display: none !important; }
      .btn-collapse-sidebar { display: none !important; }
      aside {
        position: fixed;
        top: 0;
        left: 0;
        bottom: 0;
        z-index: 100;
        transform: translateX(-100%);
        transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        box-shadow: 4px 0 24px rgba(0, 0, 0, 0.5);
        display: block !important;
      }
      aside.mobile-open {
        transform: translateX(0);
      }
      body.sidebar-collapsed aside#appSidebar {
        margin-left: 0 !important;
      }
      main { margin-left: 0; padding: 0 16px 25px 16px; }
      body.sidebar-collapsed main {
        margin-left: 0 !important;
        padding-left: 16px !important;
        padding-right: 16px !important;
        width: 100% !important;
        max-width: 100% !important;
      }
      .grid-4, .grid-3, .grid-2 { grid-template-columns: 1fr; }
    }

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
      width: 100%;
      max-width: 100%;
      padding-left: 55px;
      padding-right: 55px;
    }

    #desktopSidebarToggle {
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }
    #desktopSidebarToggle.active {
      background: var(--bg-primary);
      border-color: var(--accent-blue);
      color: var(--accent-blue);
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


    /* --- Interactive CFA Jargon & Terminology Popover System --- */
    .cfa-jargon-term {
      border-bottom: 1.5px dashed var(--accent-amber);
      color: inherit;
      cursor: help;
      padding: 0 2px;
      border-radius: 2px;
      transition: background 0.15s ease, color 0.15s ease, border-color 0.15s ease;
      text-decoration: none;
      display: inline;
    }
    .cfa-jargon-term:hover, .cfa-jargon-term:focus, .cfa-jargon-term.active {
      background: rgba(217, 119, 6, 0.18);
      color: #f59e0b;
      border-bottom-color: #f59e0b;
      outline: none;
    }
    .cfa-jargon-popover {
      position: fixed;
      z-index: 100000;
      width: 440px;
      max-width: calc(100vw - 32px);
      max-height: 480px;
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: 6px;
      box-shadow: 4px 4px 0px 0px rgba(0, 0, 0, 0.45);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      font-family: var(--font-sans);
      pointer-events: auto;
      opacity: 0;
      transform: translateY(4px);
      transition: opacity 0.16s ease, transform 0.16s ease;
    }
    .cfa-jargon-popover.visible {
      opacity: 1;
      transform: translateY(0);
    }
    .cfa-jargon-popover-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      padding: 12px 14px 10px 14px;
      background: var(--bg-tertiary);
      border-bottom: 1px solid var(--border-color);
      gap: 10px;
      flex-shrink: 0;
    }
    .cfa-jargon-popover-body {
      padding: 14px;
      overflow-y: auto;
      overscroll-contain: contain;
      font-size: 13px;
      line-height: 1.6;
      color: var(--text-primary);
      flex: 1 1 auto;
    }
    .cfa-jargon-section-title {
      font-family: var(--font-mono);
      font-size: 10.5px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
      margin-top: 12px;
      margin-bottom: 4px;
    }
    .cfa-jargon-section-title:first-child {
      margin-top: 0;
    }
    .cfa-jargon-formula-box {
      background: var(--code-bg);
      border-left: 3px solid var(--accent-blue);
      padding: 10px 12px;
      border-radius: 0 4px 4px 0;
      margin: 8px 0 12px 0;
      overflow-x: auto;
      font-size: 14px;
    }
    .cfa-jargon-pitfalls-box {
      background: rgba(239, 68, 68, 0.08);
      border: 1px solid rgba(239, 68, 68, 0.35);
      border-radius: 4px;
      padding: 10px 12px;
      margin: 10px 0;
      font-size: 12.5px;
      line-height: 1.55;
    }
    .cfa-jargon-numerical-box {
      background: var(--bg-tertiary);
      border: 1px solid var(--border-color);
      border-radius: 4px;
      padding: 12px;
      margin: 10px 0;
      font-size: 12.5px;
    }
    .cfa-jargon-numerical-title {
      font-weight: 700;
      color: var(--accent-amber);
      font-family: var(--font-serif);
      font-size: 14.5px;
      margin-bottom: 6px;
    }
    .cfa-jargon-result-badge {
      background: rgba(16, 185, 129, 0.12);
      border: 1px solid var(--accent-emerald);
      color: var(--accent-emerald);
      font-family: var(--font-mono);
      font-weight: 700;
      font-size: 12px;
      padding: 6px 10px;
      border-radius: 4px;
      margin-top: 8px;
    }
    .cfa-jargon-related-tag {
      display: inline-block;
      background: var(--bg-tertiary);
      border: 1px solid var(--border-color);
      color: var(--text-secondary);
      font-family: var(--font-mono);
      font-size: 11px;
      padding: 3px 7px;
      border-radius: 3px;
      margin: 2px 4px 2px 0;
      cursor: pointer;
      transition: all 0.12s ease;
    }
    .cfa-jargon-related-tag:hover {
      border-color: var(--accent-blue);
      color: var(--accent-blue);
      background: rgba(59, 130, 246, 0.1);
    }
    .cfa-jargon-backdrop {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0, 0, 0, 0.6);
      z-index: 99999;
      backdrop-filter: blur(2px);
    }

  </style>
</head>
<body>

  <!-- Backdrop overlay for mobile drawer -->
  <div class="sidebar-backdrop" id="sidebarBackdrop" onclick="closeMobileNav()"></div>

  <!-- Unified Sidebar Navigation -->
  <aside id="appSidebar">
    <div class="sidebar-header" style="display: flex; justify-content: space-between; align-items: flex-start;">
      <div>
        <h1 style="font-family: var(--font-serif); font-size: 19px; letter-spacing: -0.02em;">CFA Master Suite</h1>
        <p style="font-family: var(--font-mono); font-size: 11px; color: var(--text-secondary); margin-top: 3px;">2,210 Questions • All 10 CBOK Courses</p>
      </div>
      <div style="display: flex; gap: 4px; align-items: center;">
        <button class="btn-collapse-sidebar" onclick="toggleDesktopSidebar()" title="Collapse Left Sidebar (Ctrl+B)">◀ Collapse</button>
        <button class="btn-top sidebar-close-btn" onclick="closeMobileNav()" title="Close Menu">✕</button>
      </div>
    </div>
    <ul class="nav-links">
      <li><a href="#overview" class="active" onclick="switchTab('overview')"><span>Overview & Telemetry</span></a></li>
      <li><a href="#l1-practice" onclick="switchTab('l1-practice')"><span>Level 1 Question Bank</span> <span class="nav-badge">1,225 Q</span></a></li>
      <li><a href="#l2-vignettes" onclick="switchTab('l2-vignettes')"><span>Level 2 Case Vignettes</span> <span class="nav-badge">183 V / 985 Q</span></a></li>
      
      <li class="nav-divider"><span>PRACTICE & WORKED SOLUTIONS</span></li>
      <li><a href="#jargon-glossary" onclick="switchTab('jargon-glossary')"><span>📚 Terminology & Jargon Engine</span> <span class="nav-badge" style="color: var(--accent-amber); border-color: var(--accent-amber);">64 Master</span></a></li>
      <li><a href="#solved-numericals" onclick="switchTab('solved-numericals')"><span>Master Solved Numericals</span> <span class="nav-badge" style="color: var(--accent-amber); border-color: var(--accent-amber);">63 Worked</span></a></li>
      <li><a href="#curriculum-audit" onclick="switchTab('curriculum-audit')"><span>Curriculum Audit & Gaps</span> <span class="nav-badge">2026–2027</span></a></li>
      
      <li class="nav-divider"><span>FINANCIAL SIMULATIONS (16)</span></li>
      <li><a href="#sim-yield" onclick="switchTab('sim-yield')"><span>📈 Yield Curve Simulator</span></a></li>
      <li><a href="#sim-tree" onclick="switchTab('sim-tree')"><span>🌳 Binomial Tree Engine</span></a></li>
      <li><a href="#sim-equity" onclick="switchTab('sim-equity')"><span>📊 DDM & DuPont Explorer</span></a></li>
      <li><a href="#sim-duration" onclick="switchTab('sim-duration')"><span>⚡ Key Rate Duration</span></a></li>
      <li><a href="#sim-frn" onclick="switchTab('sim-frn')"><span>🔢 FRN Pricing Engine</span></a></li>
      <li><a href="#sim-ri-decay" onclick="switchTab('sim-ri-decay')"><span>📉 RI Persistence Decay</span></a></li>
      <li><a href="#sim-waterfall" onclick="switchTab('sim-waterfall')"><span>🌊 FCFF→FCFE Waterfall</span></a></li>
      <li><a href="#sim-translation" onclick="switchTab('sim-translation')"><span>💱 Currency Translation</span></a></li>
      <li><a href="#sim-prepayment" onclick="switchTab('sim-prepayment')"><span>🏠 MBS Prepayment Simulator</span></a></li>
      <li><a href="#sim-frontier" onclick="switchTab('sim-frontier')"><span>🎯 Markowitz Frontier & CAL</span></a></li>
      <li><a href="#sim-fundamental-law" onclick="switchTab('sim-fundamental-law')"><span>⚖️ Fundamental Law of Active Mgmt</span></a></li>
      <li><a href="#sim-rebalancing" onclick="switchTab('sim-rebalancing')"><span>📐 Dynamic Rebalancing Corridors</span></a></li>
      <li><a href="#sim-bsm" onclick="switchTab('sim-bsm')"><span>⚡ BSM & Option Greeks Lab</span></a></li>
      <li><a href="#sim-quant" onclick="switchTab('sim-quant')"><span>🎲 Quant Monte Carlo & TVM Lab</span></a></li>
      <li><a href="#sim-alts" onclick="switchTab('sim-alts')"><span>🏛️ HF Fee Waterfall & HWM Lab</span></a></li>
      <li><a href="#sim-corp" onclick="switchTab('sim-corp')"><span>🏢 WACC, Hamada & MM Optimizer</span></a></li>
      
      <li class="nav-divider"><span>CURRICULUM REFERENCE (10 CBOK)</span></li>
      <li><a href="#eth-reference" onclick="switchTab('eth-reference')"><span>⚖️ I. Ethics &amp; Standards (10 Ch + 50 Drills)</span></a></li>
      <li><a href="#qm-reference" onclick="switchTab('qm-reference')"><span>📐 II. Quantitative Methods (12 Ch)</span></a></li>
      <li><a href="#econ-reference" onclick="switchTab('econ-reference')"><span>🌍 III. Economics (10 Ch)</span></a></li>
      <li><a href="#fsa-reference" onclick="switchTab('fsa-reference')"><span>📖 IV. FSA Reference Notes (20 Ch)</span></a></li>
      <li><a href="#corp-reference" onclick="switchTab('corp-reference')"><span>🏢 V. Corporate Issuers (9 Ch)</span></a></li>
      <li><a href="#eq-reference" onclick="switchTab('eq-reference')"><span>📊 VI. Equity Valuation (8 Ch)</span></a></li>
      <li><a href="#fi-reference" onclick="switchTab('fi-reference')"><span>📈 VII. Fixed Income (8 Ch)</span></a></li>
      <li><a href="#deriv-reference" onclick="switchTab('deriv-reference')"><span>⚡ VIII. Derivatives (9 Ch)</span></a></li>
      <li><a href="#alt-reference" onclick="switchTab('alt-reference')"><span>🏛️ IX. Alternative Investments (9 Ch)</span></a></li>
      <li><a href="#pm-reference" onclick="switchTab('pm-reference')"><span>💼 X–XII. Portfolio Mgmt &amp; AA (10 Ch)</span></a></li>
      <li><a href="#reference-diagrams" onclick="switchTab('reference-diagrams')"><span>📐 Visual Frameworks</span></a></li>
    </ul>
  </aside>

  <!-- Main Content Container -->
  <main>
    <div class="top-bar">
      <div style="display: flex; align-items: center; gap: 12px;">
        <button class="btn-top" id="desktopSidebarToggle" onclick="toggleDesktopSidebar()" title="Toggle Sidebar (Ctrl+B)">☰ <span>Sidebar</span></button>
        <button class="menu-toggle-btn" id="menuToggleBtn" onclick="toggleMobileNav()" aria-label="Toggle Navigation">☰ Menu</button>
        <div id="topTitle">
          <h2>Curriculum Overview & Analytics</h2>
        </div>
      </div>
      <div class="stats-pills">
        <div class="stat-pill" style="color: var(--accent-blue);">Total: 2,210 Questions</div>
        <div class="stat-pill" style="color: var(--accent-emerald);">Score: <span id="scoreDisplay">0 / 0 (0%)</span></div>
        <button class="btn-top" onclick="resetScores()">🔄 Reset Score</button>
        <button class="btn-top" onclick="toggleTheme()">🌓 Theme</button>
      </div>
    </div>

    <!-- 1. OVERVIEW & TELEMETRY -->
    <section id="overview" class="active">
      <div class="card" style="margin-bottom: 18px; border-left: 4px solid var(--accent-blue);">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;">
          <div>
            <div style="font-size: 12px; color: var(--accent-blue); text-transform: uppercase; font-weight: 700; letter-spacing:0.05em;">Complete CFA&reg; Program CBOK I–XII Master Platform</div>
            <div style="font-size: 26px; font-weight: 700; color: var(--text-primary); margin-top: 2px;">2,210 Questions &bull; 183 L2 Vignettes &bull; 105 Chapters &bull; 16 Sims</div>
          </div>
          <div style="display:flex; gap:8px; flex-wrap:wrap;">
            <span class="badge badge-emerald">1,225 Level 1 MCQs</span>
            <span class="badge badge-purple">985 Level 2 Vignette Qs</span>
            <span class="badge badge-amber">63 Master Solved Numericals</span>
            <span class="badge badge-cyan">500 Ethics Questions &amp; Drills</span>
          </div>
        </div>
      </div>

      <div class="grid-5" style="margin-bottom: 14px;">
        <div class="card" style="margin-bottom: 0; cursor:pointer;" onclick="switchTab('eth-reference')">
          <div style="font-size: 11px; color: var(--text-secondary); text-transform: uppercase; font-weight: 700;">I. Ethics &amp; Standards</div>
          <div style="font-size: 24px; font-weight: 700; color: var(--accent-rose); margin-top: 4px;">450 Qs + 50 Drills</div>
          <div style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">270 L1 + 180 L2 (30 V) + 10 Ch</div>
        </div>
        <div class="card" style="margin-bottom: 0; cursor:pointer;" onclick="switchTab('qm-reference')">
          <div style="font-size: 11px; color: var(--text-secondary); text-transform: uppercase; font-weight: 700;">II. Quantitative Methods</div>
          <div style="font-size: 24px; font-weight: 700; color: var(--accent-blue); margin-top: 4px;">150 Qs</div>
          <div style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">90 L1 + 60 L2 (10 V) + 12 Ch</div>
        </div>
        <div class="card" style="margin-bottom: 0; cursor:pointer;" onclick="switchTab('econ-reference')">
          <div style="font-size: 11px; color: var(--text-secondary); text-transform: uppercase; font-weight: 700;">III. Economics</div>
          <div style="font-size: 24px; font-weight: 700; color: var(--accent-cyan); margin-top: 4px;">130 Qs</div>
          <div style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">80 L1 + 50 L2 (10 V) + 10 Ch</div>
        </div>
        <div class="card" style="margin-bottom: 0; cursor:pointer;" onclick="switchTab('fsa-reference')">
          <div style="font-size: 11px; color: var(--text-secondary); text-transform: uppercase; font-weight: 700;">IV. Financial Statement Analysis</div>
          <div style="font-size: 24px; font-weight: 700; color: var(--accent-amber); margin-top: 4px;">460 Qs</div>
          <div style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">190 L1 + 270 L2 (48 V) + 20 Ch</div>
        </div>
        <div class="card" style="margin-bottom: 0; cursor:pointer;" onclick="switchTab('corp-reference')">
          <div style="font-size: 11px; color: var(--text-secondary); text-transform: uppercase; font-weight: 700;">V. Corporate Issuers</div>
          <div style="font-size: 24px; font-weight: 700; color: var(--accent-amber); margin-top: 4px;">130 Qs</div>
          <div style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">80 L1 + 50 L2 (10 V) + 9 Ch</div>
        </div>
      </div>

      <div class="grid-5" style="margin-bottom: 24px;">
        <div class="card" style="margin-bottom: 0; cursor:pointer;" onclick="switchTab('eq-reference')">
          <div style="font-size: 11px; color: var(--text-secondary); text-transform: uppercase; font-weight: 700;">VI. Equity Investments</div>
          <div style="font-size: 24px; font-weight: 700; color: var(--accent-emerald); margin-top: 4px;">210 Qs</div>
          <div style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">115 L1 + 95 L2 (19 V) + 8 Ch</div>
        </div>
        <div class="card" style="margin-bottom: 0; cursor:pointer;" onclick="switchTab('fi-reference')">
          <div style="font-size: 11px; color: var(--text-secondary); text-transform: uppercase; font-weight: 700;">VII. Fixed Income</div>
          <div style="font-size: 24px; font-weight: 700; color: var(--accent-cyan); margin-top: 4px;">205 Qs</div>
          <div style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">120 L1 + 85 L2 (17 V) + 8 Ch</div>
        </div>
        <div class="card" style="margin-bottom: 0; cursor:pointer;" onclick="switchTab('deriv-reference')">
          <div style="font-size: 11px; color: var(--text-secondary); text-transform: uppercase; font-weight: 700;">VIII. Derivatives</div>
          <div style="font-size: 24px; font-weight: 700; color: var(--accent-purple); margin-top: 4px;">140 Qs</div>
          <div style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">85 L1 + 55 L2 (11 V) + 9 Ch</div>
        </div>
        <div class="card" style="margin-bottom: 0; cursor:pointer;" onclick="switchTab('alt-reference')">
          <div style="font-size: 11px; color: var(--text-secondary); text-transform: uppercase; font-weight: 700;">IX. Alternative Investments</div>
          <div style="font-size: 24px; font-weight: 700; color: var(--accent-emerald); margin-top: 4px;">125 Qs</div>
          <div style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">75 L1 + 50 L2 (10 V) + 9 Ch</div>
        </div>
        <div class="card" style="margin-bottom: 0; cursor:pointer;" onclick="switchTab('pm-reference')">
          <div style="font-size: 11px; color: var(--text-secondary); text-transform: uppercase; font-weight: 700;">X–XII. Portfolio Mgmt &amp; AA</div>
          <div style="font-size: 24px; font-weight: 700; color: var(--accent-purple); margin-top: 4px;">210 Qs</div>
          <div style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">120 L1 + 90 L2 (18 V) + 10 Ch</div>
        </div>
      </div>

      <div class="grid-2" style="margin-bottom: 24px;">
        <div class="card" style="margin-bottom: 0;">
          <div class="card-title">Curriculum Distribution & Structure</div>
          <div class="chart-canvas-wrap" style="height: 270px;">
            <canvas id="overviewChart"></canvas>
          </div>
        </div>
        <div class="card" style="margin-bottom: 0;">
          <div class="card-title">Candidate Performance Telemetry</div>
          <div class="chart-canvas-wrap" style="height: 270px;">
            <canvas id="accuracyChart"></canvas>
          </div>
        </div>
      </div>

      <div class="card">
        <div class="card-title">Quick Launch Study Portals (All 10 CBOK Subjects)</div>
        <div class="grid-3" style="margin-bottom: 12px;">
          <button class="btn" onclick="switchTab('l1-practice')">📝 Level 1 Question Bank (1,225 Q)</button>
          <button class="btn btn-secondary" onclick="switchTab('l2-vignettes')">📑 Level 2 Case Vignettes (183 V / 985 Q)</button>
          <button class="btn btn-secondary" onclick="switchTab('sim-bsm')">🔬 Financial Simulations Lab (16)</button>
        </div>
        <div class="grid-5" style="margin-bottom: 10px;">
          <button class="btn btn-secondary" onclick="switchTab('eth-reference')">⚖️ I. Ethics (500 Drills)</button>
          <button class="btn btn-secondary" onclick="switchTab('qm-reference')">📐 II. Quant Methods</button>
          <button class="btn btn-secondary" onclick="switchTab('econ-reference')">🌍 III. Economics</button>
          <button class="btn btn-secondary" onclick="switchTab('fsa-reference')">📖 IV. FSA Notes</button>
          <button class="btn btn-secondary" onclick="switchTab('corp-reference')">🏢 V. Corp Issuers</button>
        </div>
        <div class="grid-5">
          <button class="btn btn-secondary" onclick="switchTab('eq-reference')">📊 VI. Equity Valuation</button>
          <button class="btn btn-secondary" onclick="switchTab('fi-reference')">📈 VII. Fixed Income</button>
          <button class="btn btn-secondary" onclick="switchTab('deriv-reference')">⚡ VIII. Derivatives</button>
          <button class="btn btn-secondary" onclick="switchTab('alt-reference')">🏛️ IX. Alternatives</button>
          <button class="btn btn-secondary" onclick="switchTab('pm-reference')">💼 X–XII. Portfolio Mgmt</button>
        </div>
      </div>
    </section>

    <!-- 2. LEVEL 1 QUESTION BANK -->
    <section id="l1-practice">
      <div class="card">
        <div class="card-title">Level 1 Multiple-Choice Question Bank (1,225 Questions)</div>
        <div class="grid-4" style="margin-bottom: 16px;">
          <div class="control-group">
            <label>Filter Subject:</label>
            <select id="l1SubjectSelect" onchange="onL1SubjectChange()">
              <option value="ALL">All Subjects (1,225 Questions)</option>
              <option value="Ethical and Professional Standards">I. Ethical &amp; Professional Standards (270 Qs)</option>
              <option value="Quantitative Methods">II. Quantitative Methods (90 Qs)</option>
              <option value="Economics">III. Economics (80 Qs)</option>
              <option value="Financial Statement Analysis">IV. Financial Statement Analysis (190 Qs)</option>
              <option value="Corporate Issuers">V. Corporate Issuers (80 Qs)</option>
              <option value="Equity Investments">VI. Equity Investments (115 Qs)</option>
              <option value="Fixed Income">VII. Fixed Income (120 Qs)</option>
              <option value="Derivatives">VIII. Derivatives (85 Qs)</option>
              <option value="Alternative Investments">IX. Alternative Investments (75 Qs)</option>
              <option value="Portfolio Management">X. Portfolio Management (120 Qs)</option>
            </select>
          </div>
          <div class="control-group">
            <label>Filter Topic / Module:</label>
            <select id="l1TopicSelect" onchange="onL1TopicChange()">
              <option value="ALL">All Learning Modules</option>
            </select>
          </div>
          <div class="control-group">
            <label>Question Type &amp; Practice Mode:</label>
            <div class="filter-pills" style="margin-bottom: 6px;">
              <button class="filter-pill active" id="l1TypeAll" onclick="setL1TypeFilter('ALL')">All</button>
              <button class="filter-pill" id="l1TypeNum" onclick="setL1TypeFilter('NUMERICAL')">🧮 Numericals</button>
              <button class="filter-pill" id="l1TypeTheory" onclick="setL1TypeFilter('THEORY')">📖 Theory</button>
            </div>
            <div class="filter-pills">
              <button class="filter-pill active" id="l1ModeSolved" onclick="setL1PracticeMode('study')">✅ Solved / Auto-Grade</button>
              <button class="filter-pill" id="l1ModeUnsolved" onclick="setL1PracticeMode('unsolved')">🙈 Unsolved Self-Test</button>
            </div>
          </div>
          <div class="control-group">
            <label>Search Keyword / LOS:</label>
            <input type="text" id="l1SearchInput" placeholder="e.g. Standard II, BSM, WACC, GARCH, CIRP..." oninput="onL1Search()">
          </div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid var(--border-color); padding-top: 14px; flex-wrap: wrap; gap: 10px;">
          <div style="font-weight: 600; color: var(--accent-blue);" id="l1CountBadge">
            Showing Question 1 of 1,225
          </div>
          <div class="btn-group">
            <button class="btn btn-secondary" onclick="prevL1Question()">← Previous</button>
            <button class="btn btn-secondary" onclick="nextL1Question()">Next →</button>
            <button class="btn btn-secondary" onclick="randomL1Question()">🎲 Random</button>
            <button class="btn btn-secondary" id="l1ViewModeBtn" onclick="toggleL1ViewMode()">📜 Switch to Full List View</button>
          </div>
        </div>
      </div>

      <div id="l1QuestionContainer">
        <!-- Rendered dynamically -->
      </div>
    </section>

    <!-- 3. LEVEL 2 CASE VIGNETTES -->
    <section id="l2-vignettes">
      <div class="card">
        <div class="card-title">Level 2 Vignette & Item-Set Explorer (183 Vignettes / 985 Questions)</div>
        <div class="grid-4" style="margin-bottom: 16px;">
          <div class="control-group">
            <label>Filter Subject:</label>
            <select id="l2SubjectSelect" onchange="onL2SubjectChange()">
              <option value="ALL">All Subjects (183 Vignettes / 985 Qs)</option>
              <option value="Ethical and Professional Standards">I. Ethical &amp; Professional Standards (30 V / 180 Qs)</option>
              <option value="Quantitative Methods">II. Quantitative Methods (10 V / 60 Qs)</option>
              <option value="Economics">III. Economics (10 V / 50 Qs)</option>
              <option value="Financial Statement Analysis">IV. Financial Statement Analysis (48 V / 270 Qs)</option>
              <option value="Corporate Issuers">V. Corporate Issuers (10 V / 50 Qs)</option>
              <option value="Equity Investments">VI. Equity Investments (19 V / 95 Qs)</option>
              <option value="Fixed Income">VII. Fixed Income (17 V / 85 Qs)</option>
              <option value="Derivatives">VIII. Derivatives (11 V / 55 Qs)</option>
              <option value="Alternative Investments">IX. Alternative Investments (10 V / 50 Qs)</option>
              <option value="Portfolio Management">X. Portfolio Management (18 V / 90 Qs)</option>
            </select>
          </div>
          <div class="control-group">
            <label>Select Case Vignette:</label>
            <select id="l2VignetteSelect" onchange="loadL2Vignette()"></select>
          </div>
          <div class="control-group">
            <label>Question Type Filter:</label>
            <div class="filter-pills">
              <button class="filter-pill active" id="l2TypeAll" onclick="setL2TypeFilter('ALL')">All</button>
              <button class="filter-pill" id="l2TypeNum" onclick="setL2TypeFilter('NUMERICAL')">🧮 Numericals</button>
              <button class="filter-pill" id="l2TypeTheory" onclick="setL2TypeFilter('THEORY')">📖 Theory</button>
            </div>
          </div>
          <div class="control-group">
            <label>Search Vignettes / Cases:</label>
            <input type="text" id="l2SearchInput" placeholder="Search case title or concept..." oninput="onL2Search()">
          </div>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid var(--border-color); padding-top: 12px;">
          <span style="font-size: 12px; color: var(--text-secondary);" id="l2VignetteCounter">Vignette 1 of 80</span>
          <div class="btn-group">
            <button class="btn btn-secondary" onclick="prevL2Vignette()">← Previous Case</button>
            <button class="btn btn-secondary" onclick="nextL2Vignette()">Next Case →</button>
          </div>
        </div>
      </div>

      <div class="card" id="vignetteTextCard">
        <!-- Vignette Narrative will load here -->
      </div>
      <div id="vignetteQuestionsCard">
        <!-- Questions will load here -->
      </div>
    </section>

    <!-- 4. SIMULATION: YIELD CURVE -->
    <section id="sim-yield">
      <div class="card">
        <div class="card-title">📈 Interactive Yield Curve Dynamics & Term Structure Simulator</div>
        <p style="color: var(--text-secondary); margin-bottom: 20px;">
          Simulate yield curve movements: <strong>Shift (Level)</strong>, <strong>Twist (Slope)</strong>, and <strong>Butterfly (Curvature)</strong>. Inspect the mathematical relationship between the Par Curve, Spot Rates, and Forward Rates.
        </p>
        <div class="grid-2">
          <div>
            <div class="chart-canvas-wrap" style="height: 260px;">
              <canvas id="yieldChart"></canvas>
            </div>
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
        <div class="card-title">🌳 Binomial Interest Rate Tree & Embedded Option Valuation Engine</div>
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
              <div id="treeResults" style="font-size: 13px; line-height: 1.8;"></div>
            </div>
          </div>
          <div>
            <div style="font-weight: 600; margin-bottom: 10px; font-size: 13px;">Interest Rate Tree Visualization:</div>
            <div class="tree-grid" id="treeVisualContainer"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- 6. SIMULATION: EQUITY DDM & DUPONT -->
    <section id="sim-equity">
      <div class="card">
        <div class="card-title">📊 Equity Valuation: Two-Stage Dividend Discount Model & DuPont 5-Way Explorer</div>
        <p style="color: var(--text-secondary); margin-bottom: 20px;">
          Calculate intrinsic equity value using a two-stage dividend discount model and decompose Return on Equity (ROE) using the 5-stage DuPont framework.
        </p>
        <div class="grid-2">
          <div>
            <div style="font-weight: 700; margin-bottom: 12px; color: var(--accent-blue);">Two-Stage DDM Parameters:</div>
            <div class="grid-2">
              <div class="control-group">
                <label>Current Div $D_0$: <span id="d0Val">2.50 USD</span></label>
                <input type="range" id="d0Input" min="0.5" max="10" value="2.5" step="0.1" oninput="updateEquitySim()">
              </div>
              <div class="control-group">
                <label>Supernormal Growth $g_S$: <span id="gsVal">14.0%</span></label>
                <input type="range" id="gsInput" min="5" max="30" value="14" step="0.5" oninput="updateEquitySim()">
              </div>
              <div class="control-group">
                <label>High Growth Horizon $n$: <span id="nVal">5 Years</span></label>
                <input type="range" id="nInput" min="1" max="10" value="5" step="1" oninput="updateEquitySim()">
              </div>
              <div class="control-group">
                <label>Long-Term Growth $g_L$: <span id="glVal">4.0%</span></label>
                <input type="range" id="glInput" min="1" max="7" value="4" step="0.25" oninput="updateEquitySim()">
              </div>
            </div>
            <div class="control-group">
              <label>Required Return on Equity $r$: <span id="rVal">9.0%</span></label>
              <input type="range" id="rInput" min="5" max="18" value="9" step="0.25" oninput="updateEquitySim()">
            </div>
            <div style="padding: 15px; background: var(--bg-primary); border-radius: 6px; border: 1px solid var(--border-color); margin-top: 10px;">
              <div id="ddmResult" style="font-size: 14px; line-height: 1.8;"></div>
            </div>
          </div>
          <div>
            <div style="font-weight: 700; margin-bottom: 12px; color: var(--accent-emerald);">DuPont 5-Way ROE Decomposition:</div>
            <div class="chart-canvas-wrap" style="height: 220px;">
              <canvas id="dupontChart"></canvas>
            </div>
            <div id="dupontResult" style="margin-top: 12px; padding: 12px; background: var(--bg-primary); border-radius: 6px; font-size: 13px;"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- 7. SIMULATION: KEY RATE DURATION -->
    <section id="sim-duration">
      <div class="card">
        <div class="card-title">⚡ Key Rate Duration & Non-Parallel Yield Curve Sensitivity Visualizer</div>
        <p style="color: var(--text-secondary); margin-bottom: 20px;">
          Analyze how non-parallel shifts across the yield curve impact bond prices. Key rate duration measures price sensitivity to a shift in a single benchmark maturity tenor while holding other tenors constant.
        </p>
        <div class="grid-2">
          <div>
            <div class="chart-canvas-wrap" style="height: 240px;">
              <canvas id="krdChart"></canvas>
            </div>
          </div>
          <div>
            <div class="control-group">
              <label>Select Portfolio Structure:</label>
              <select id="portfolioSelect" onchange="updateDurationSim()">
                <option value="bullet">10-Year Bullet Portfolio (Concentrated at 10Y)</option>
                <option value="barbell">Barbell Portfolio (50% 2Y + 50% 30Y)</option>
                <option value="ladder">Laddered Portfolio (Equal weights 2Y, 5Y, 10Y, 30Y)</option>
              </select>
            </div>
            <div class="grid-3">
              <div class="control-group">
                <label>2Y Shock: <span id="s2Val">0 bps</span></label>
                <input type="range" id="s2" min="-100" max="100" value="0" step="10" oninput="updateDurationSim()">
              </div>
              <div class="control-group">
                <label>10Y Shock: <span id="s10Val">0 bps</span></label>
                <input type="range" id="s10" min="-100" max="100" value="0" step="10" oninput="updateDurationSim()">
              </div>
              <div class="control-group">
                <label>30Y Shock: <span id="s30Val">0 bps</span></label>
                <input type="range" id="s30" min="-100" max="100" value="0" step="10" oninput="updateDurationSim()">
              </div>
            </div>
            <div style="padding: 15px; background: var(--bg-primary); border-radius: 6px; border: 1px solid var(--border-color); margin-top: 10px;">
              <div id="krdResults" style="font-size: 13px; line-height: 1.8;"></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 8. SIMULATION: FRN PRICING -->
    <section id="sim-frn">
      <div class="card">
        <div class="card-title">🔢 Floating-Rate Note (FRN) Pricing & Discount Margin (DM) Engine</div>
        <p style="color: var(--text-secondary); margin-bottom: 20px;">
          Model Floating-Rate Note valuation on coupon reset dates. When Quoted Margin (QM) equals Discount Margin (DM), the FRN trades exactly at par (100 USD).
        </p>
        <div class="grid-2">
          <div>
            <div class="control-group">
              <label>Reference Benchmark Rate (MRR) (%): <span id="mrrVal" style="color: var(--accent-blue);">4.00%</span></label>
              <input type="range" id="mrrInput" min="1.0" max="8.0" value="4.0" step="0.25" oninput="updateFrnSim()">
            </div>
            <div class="control-group">
              <label>Quoted Margin (QM) (bps): <span id="qmVal" style="color: var(--accent-cyan);">150 bps</span></label>
              <input type="range" id="qmInput" min="0" max="400" value="150" step="10" oninput="updateFrnSim()">
            </div>
            <div class="control-group">
              <label>Discount Margin (DM / Required Margin) (bps): <span id="dmVal" style="color: var(--accent-rose);">180 bps</span></label>
              <input type="range" id="dmInput" min="0" max="400" value="180" step="10" oninput="updateFrnSim()">
            </div>
            <div class="grid-2">
              <div class="control-group">
                <label>Payment Frequency:</label>
                <select id="frnFreq" onchange="updateFrnSim()">
                  <option value="4">Quarterly (m = 4)</option>
                  <option value="2">Semiannual (m = 2)</option>
                  <option value="1">Annual (m = 1)</option>
                </select>
              </div>
              <div class="control-group">
                <label>Remaining Tenor (Years): <span id="frnTenorVal">3 Years</span></label>
                <input type="range" id="frnTenor" min="1" max="10" value="3" step="1" oninput="updateFrnSim()">
              </div>
            </div>
          </div>
          <div>
            <div style="padding: 18px; background: var(--bg-primary); border-radius: 6px; border: 1px solid var(--border-color); height: 100%; display: flex; flex-direction: column; justify-content: center;">
              <div style="font-size: 14px; font-weight: 700; color: var(--accent-cyan); margin-bottom: 12px;">FRN Valuation Output:</div>
              <div id="frnResults" style="font-size: 13.5px; line-height: 1.8;"></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 9. SIMULATION: RI PERSISTENCE DECAY -->
    <section id="sim-ri-decay">
      <div class="card">
        <div class="card-title">📉 Residual Income (RI) Persistence Decay & Continuing Value Engine</div>
        <p style="color: var(--text-secondary); margin-bottom: 20px;">
          Explore terminal residual income persistence parameter $\omega \in [0, 1]$. An $\omega = 1.0$ assumes perpetual residual income, while $\omega = 0.0$ implies immediate competitive decay to normal returns.
        </p>
        <div class="grid-2">
          <div>
            <div class="chart-canvas-wrap" style="height: 250px;">
              <canvas id="riChart"></canvas>
            </div>
          </div>
          <div>
            <div class="control-group">
              <label>Persistence Factor ($\omega$): <span id="omegaVal" style="color: var(--accent-blue);">0.60</span></label>
              <input type="range" id="omegaInput" min="0.0" max="1.0" value="0.60" step="0.05" oninput="updateRiSim()">
            </div>
            <div class="grid-2">
              <div class="control-group">
                <label>Book Value per Share ($B_0$): <span id="b0Val">40.00 USD</span></label>
                <input type="range" id="b0Input" min="10" max="100" value="40" step="5" oninput="updateRiSim()">
              </div>
              <div class="control-group">
                <label>Expected ROE (%): <span id="roeVal">18.0%</span></label>
                <input type="range" id="roeInput" min="8" max="30" value="18" step="0.5" oninput="updateRiSim()">
              </div>
            </div>
            <div class="control-group">
              <label>Cost of Equity ($r$) (%): <span id="costEqVal">10.0%</span></label>
              <input type="range" id="costEqInput" min="6" max="16" value="10" step="0.5" oninput="updateRiSim()">
            </div>
            <div style="padding: 14px; background: var(--bg-primary); border-radius: 6px; border: 1px solid var(--border-color); margin-top: 10px;">
              <div id="riResultBox" style="font-size: 13px; line-height: 1.8;"></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 10. SIMULATION: FCFF TO FCFE WATERFALL -->
    <section id="sim-waterfall">
      <div class="card">
        <div class="card-title">🌊 Free Cash Flow to Firm (FCFF) → Free Cash Flow to Equity (FCFE) Waterfall Bridge</div>
        <p style="color: var(--text-secondary); margin-bottom: 20px;">
          Interactive bridge from EBITDA down to FCFF, and subsequent bridge to FCFE through after-tax interest expense and net borrowing adjustments.
        </p>
        <div class="grid-2">
          <div>
            <div class="chart-canvas-wrap" style="height: 280px;">
              <canvas id="waterfallChart"></canvas>
            </div>
          </div>
          <div>
            <div class="grid-2">
              <div class="control-group">
                <label>EBITDA (M USD): <span id="ebitdaVal">500 M USD</span></label>
                <input type="range" id="ebitdaInput" min="200" max="1000" value="500" step="25" oninput="updateWaterfallSim()">
              </div>
              <div class="control-group">
                <label>D&A Expense (M USD): <span id="daVal">120 M USD</span></label>
                <input type="range" id="daInput" min="30" max="250" value="120" step="10" oninput="updateWaterfallSim()">
              </div>
              <div class="control-group">
                <label>CapEx (FCInv) (M USD): <span id="fcinvVal">160 M USD</span></label>
                <input type="range" id="fcinvInput" min="50" max="300" value="160" step="10" oninput="updateWaterfallSim()">
              </div>
              <div class="control-group">
                <label>$\Delta$ Working Capital (WCInv): <span id="wcinvVal">40 M USD</span></label>
                <input type="range" id="wcinvInput" min="-50" max="100" value="40" step="5" oninput="updateWaterfallSim()">
              </div>
              <div class="control-group">
                <label>Interest Expense: <span id="intVal">60 M USD</span></label>
                <input type="range" id="intInput" min="0" max="150" value="60" step="5" oninput="updateWaterfallSim()">
              </div>
              <div class="control-group">
                <label>Net Borrowing: <span id="nbVal">+50 M USD</span></label>
                <input type="range" id="nbInput" min="-100" max="150" value="50" step="10" oninput="updateWaterfallSim()">
              </div>
            </div>
            <div style="padding: 14px; background: var(--bg-primary); border-radius: 6px; border: 1px solid var(--border-color);">
              <div id="waterfallOutput" style="font-size: 13px; line-height: 1.8;"></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 11. SIMULATION: CURRENCY TRANSLATION -->
    <section id="sim-translation">
      <div class="card">
        <div class="card-title">💱 Multinational Operations: Current Rate vs. Temporal Translation Engine</div>
        <p style="color: var(--text-secondary); margin-bottom: 20px;">
          Compare the accounting impact of the <strong>Current Rate Method</strong> (LC is Functional) vs. the <strong>Temporal Method</strong> (RC/Parent is Functional) on subsidiary balance sheet exposures and translation adjustments.
        </p>
        <div class="grid-2">
          <div>
            <div class="control-group">
              <label>Net Monetary Assets (NMA) (M LC): <span id="fxNmaVal" style="color: var(--accent-blue);">+200 M LC</span></label>
              <input type="range" id="fxNma" min="-300" max="400" value="200" step="20" oninput="updateTranslationSim()">
            </div>
            <div class="control-group">
              <label>Net Non-Monetary Assets (PP&E, Inv) (M LC): <span id="fxNnmaVal" style="color: var(--accent-cyan);">+600 M LC</span></label>
              <input type="range" id="fxNnma" min="100" max="1000" value="600" step="50" oninput="updateTranslationSim()">
            </div>
            <div class="control-group">
              <label>Local Currency % Change against Parent Currency: <span id="fxChangeVal" style="color: var(--accent-rose);">-15% (Depreciation)</span></label>
              <input type="range" id="fxChange" min="-40" max="40" value="-15" step="1" oninput="updateTranslationSim()">
            </div>
          </div>
          <div>
            <div style="padding: 16px; background: var(--bg-primary); border-radius: 6px; border: 1px solid var(--border-color);">
              <div id="translationOutput"></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 12. SIMULATION: MBS PREPAYMENT -->
    <section id="sim-prepayment">
      <div class="card">
        <div class="card-title">🏠 Mortgage-Backed Securities: Prepayment Simulator & Extension / Contraction Engine</div>
        <p style="color: var(--text-secondary); margin-bottom: 20px;">
          Simulate CPR (Conditional Prepayment Rate) and SMM (Single Monthly Mortality) schedules under PSA benchmark multiples (50% to 300% PSA). Inspect how interest rate shocks create extension and contraction risk.
        </p>
        <div class="grid-2">
          <div>
            <div class="chart-canvas-wrap" style="height: 250px;">
              <canvas id="prepaymentChart"></canvas>
            </div>
          </div>
          <div>
            <div class="control-group">
              <label>PSA Speed Benchmark Multiplier: <span id="psaVal" style="color: var(--accent-blue);">150% PSA</span></label>
              <input type="range" id="psaSpeed" min="50" max="300" value="150" step="10" oninput="updatePrepaymentSim()">
            </div>
            <div class="control-group">
              <label>Seasoning Horizon (Month $t$): <span id="seasonVal" style="color: var(--accent-emerald);">Month 18</span></label>
              <input type="range" id="seasonMonth" min="1" max="30" value="18" step="1" oninput="updatePrepaymentSim()">
            </div>
            <div style="padding: 15px; background: var(--bg-primary); border-radius: 6px; border: 1px solid var(--border-color); margin-top: 15px;">
              <div id="prepayResultBox" style="font-size: 13px; line-height: 1.8;"></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 10. SIMULATION 10: MARKOWITZ MEAN-VARIANCE FRONTIER & CAL OPTIMIZER -->
    <section id="sim-frontier">
      <div class="card">
        <div class="card-title">🎯 Simulation 10: Markowitz Mean-Variance Frontier & CAL Optimizer</div>
        <p style="color: var(--text-secondary); margin-bottom: 15px;">
          Explore Modern Portfolio Theory (MPT) dynamics. Adjust expected returns, asset volatilities, and cross-asset correlation \(\rho_{1,2}\) to observe the curvature of the risky investment opportunity set, the Global Minimum Variance (GMV) portfolio, and the tangency Capital Allocation Line (CAL). Calibrate investor risk aversion \(A\) to locate optimal capital allocation \(y^*\) on the indifference curve \(U = E(R) - \frac{1}{2}A\sigma^2\).
        </p>
        <div class="grid-2">
          <div>
            <div class="control-group">
              <label>Asset 1 Expected Return \(E(R_1)\): <span id="valSim10R1" style="color: var(--accent-blue);">12.0%</span></label>
              <input type="range" id="sim10R1" min="4" max="25" step="0.5" value="12" oninput="updateFrontierSim()">
            </div>
            <div class="control-group">
              <label>Asset 1 Volatility \(\sigma_1\): <span id="valSim10Sig1" style="color: var(--accent-cyan);">20.0%</span></label>
              <input type="range" id="sim10Sig1" min="5" max="35" step="0.5" value="20" oninput="updateFrontierSim()">
            </div>
            <div class="control-group">
              <label>Asset 2 Expected Return \(E(R_2)\): <span id="valSim10R2" style="color: var(--accent-emerald);">7.0%</span></label>
              <input type="range" id="sim10R2" min="2" max="15" step="0.5" value="7" oninput="updateFrontierSim()">
            </div>
            <div class="control-group">
              <label>Asset 2 Volatility \(\sigma_2\): <span id="valSim10Sig2" style="color: var(--accent-amber);">12.0%</span></label>
              <input type="range" id="sim10Sig2" min="4" max="25" step="0.5" value="12" oninput="updateFrontierSim()">
            </div>
            <div class="control-group">
              <label>Correlation \(\rho_{1,2}\): <span id="valSim10Rho" style="color: var(--accent-purple);">0.20</span></label>
              <input type="range" id="sim10Rho" min="-100" max="100" step="5" value="20" oninput="updateFrontierSim()">
            </div>
            <div class="control-group">
              <label>Risk-Free Rate \(R_f\): <span id="valSim10Rf" style="color: var(--accent-rose);">3.50%</span></label>
              <input type="range" id="sim10Rf" min="0" max="8" step="0.25" value="3.5" oninput="updateFrontierSim()">
            </div>
            <div class="control-group">
              <label>Investor Risk Aversion (\(A\)): <span id="valSim10A" style="color: var(--text-primary);">4.0</span></label>
              <input type="range" id="sim10A" min="1" max="10" step="0.5" value="4" oninput="updateFrontierSim()">
            </div>
          </div>
          <div>
            <div class="chart-canvas-wrap" style="height: 320px;">
              <canvas id="frontierChart"></canvas>
            </div>
            <div class="callout callout-info" id="frontierMetricsBox" style="margin-top: 12px; font-size: 12.5px;">
              <!-- Populated via JS -->
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 11. SIMULATION 11: FUNDAMENTAL LAW OF ACTIVE MANAGEMENT -->
    <section id="sim-fundamental-law">
      <div class="card">
        <div class="card-title">⚖️ Simulation 11: Grinold's Fundamental Law of Active Management</div>
        <p style="color: var(--text-secondary); margin-bottom: 15px;">
          Simulate the drivers of the Information Ratio \(IR = TC \times IC \times \sqrt{BR}\) and active management performance. Examine how investment forecasting skill (\(IC\)), independent breadth of bets (\(BR\)), and real-world portfolio constraints (Transfer Coefficient \(TC \le 1.0\)) impact active return \(\alpha\) and portfolio Sharpe ratio expansion \(SR_P^2 = SR_B^2 + IR^2\).
        </p>
        <div class="grid-2">
          <div>
            <div class="control-group">
              <label>Information Coefficient (\(IC\)): <span id="valSim11Ic" style="color: var(--accent-blue);">0.080</span></label>
              <input type="range" id="sim11Ic" min="1" max="25" step="1" value="8" oninput="updateFundamentalLawSim()">
            </div>
            <div class="control-group">
              <label>Breadth (\(BR\) Independent Bets/Yr): <span id="valSim11Br" style="color: var(--accent-cyan);">100 bets</span></label>
              <input type="range" id="sim11Br" min="4" max="1000" step="10" value="100" oninput="updateFundamentalLawSim()">
            </div>
            <div class="control-group">
              <label>Transfer Coefficient (\(TC\)): <span id="valSim11Tc" style="color: var(--accent-emerald);">0.70</span></label>
              <input type="range" id="sim11Tc" min="10" max="100" step="5" value="70" oninput="updateFundamentalLawSim()">
            </div>
            <div class="control-group">
              <label>Target Active Risk / Tracking Error (\(\sigma_A\)): <span id="valSim11SigmaA" style="color: var(--accent-amber);">4.0%</span></label>
              <input type="range" id="sim11SigmaA" min="10" max="120" step="5" value="40" oninput="updateFundamentalLawSim()">
            </div>
            <div class="control-group">
              <label>Benchmark Sharpe Ratio (\(SR_B\)): <span id="valSim11SrB" style="color: var(--accent-purple);">0.40</span></label>
              <input type="range" id="sim11SrB" min="10" max="80" step="5" value="40" oninput="updateFundamentalLawSim()">
            </div>
          </div>
          <div>
            <div class="chart-canvas-wrap" style="height: 320px;">
              <canvas id="fundamentalLawChart"></canvas>
            </div>
            <div class="callout callout-tip" id="fundamentalLawMetricsBox" style="margin-top: 12px; font-size: 12.5px;">
              <!-- Populated via JS -->
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 12. SIMULATION 12: DYNAMIC REBALANCING CORRIDORS -->
    <section id="sim-rebalancing">
      <div class="card">
        <div class="card-title">📐 Simulation 12: Dynamic Rebalancing Corridors & Tolerance Bands</div>
        <p style="color: var(--text-secondary); margin-bottom: 15px;">
          Analyze the optimal corridor width for asset class rebalancing. Calculate tolerance bounds \([w^* - \Delta w, w^* + \Delta w]\) as a function of transaction costs, investor risk aversion, asset class volatility, and correlation with the portfolio. Simulate price path drift, transaction costs, and tracking error trade-offs.
        </p>
        <div class="grid-2">
          <div>
            <div class="control-group">
              <label>Target Asset Weight (\(w^*\)): <span id="valSim12Weight" style="color: var(--accent-blue);">50.0%</span></label>
              <input type="range" id="sim12Weight" min="10" max="80" step="5" value="50" oninput="updateRebalancingSim()">
            </div>
            <div class="control-group">
              <label>Transaction Costs (\(TC\) in bps): <span id="valSim12Costs" style="color: var(--accent-rose);">30 bps</span></label>
              <input type="range" id="sim12Costs" min="5" max="100" step="5" value="30" oninput="updateRebalancingSim()">
            </div>
            <div class="control-group">
              <label>Investor Risk Aversion (\(A\)): <span id="valSim12A" style="color: var(--accent-amber);">4.0</span></label>
              <input type="range" id="sim12A" min="1" max="10" step="0.5" value="4" oninput="updateRebalancingSim()">
            </div>
            <div class="control-group">
              <label>Asset Class Volatility (\(\sigma\)): <span id="valSim12Vol" style="color: var(--accent-cyan);">18.0%</span></label>
              <input type="range" id="sim12Vol" min="5" max="40" step="1" value="18" oninput="updateRebalancingSim()">
            </div>
            <div class="control-group">
              <label>Correlation with Portfolio (\(\rho\)): <span id="valSim12Corr" style="color: var(--accent-purple);">0.40</span></label>
              <input type="range" id="sim12Corr" min="-40" max="90" step="5" value="40" oninput="updateRebalancingSim()">
            </div>
            <div style="margin-top: 10px;">
              <button class="btn btn-secondary" onclick="simulateNewPath()">🎲 Re-run Random Walk Path</button>
            </div>
          </div>
          <div>
            <div class="chart-canvas-wrap" style="height: 320px;">
              <canvas id="rebalanceChart"></canvas>
            </div>
            <div class="callout callout-warning" id="rebalanceMetricsBox" style="margin-top: 12px; font-size: 12.5px;">
              <!-- Populated via JS -->
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 12B. SIMULATION 13: BLACK-SCHOLES-MERTON & OPTION GREEKS LAB -->
    <section id="sim-bsm">
      <div class="card">
        <div class="card-title">⚡ Simulation 13: Black-Scholes-Merton (BSM) &amp; Option Greeks Engine</div>
        <p style="color: var(--text-secondary); margin-bottom: 15px;">
          Compute continuous-time European Call and Put values with continuous dividend yield ($q$), verify Put-Call Parity, inspect exact $N(d_1)$/$N(d_2)$ probabilities, and track Delta, Gamma, Vega, and Theta sensitivities across underlying spot levels.
        </p>
        <div class="grid-2">
          <div>
            <div class="control-group">
              <label>Spot Price ($S_0$): <span id="valBsmS" style="color: var(--accent-blue);">100 USD</span></label>
              <input type="range" id="bsmS" min="50" max="150" step="1" value="100" oninput="updateBsmSim()">
            </div>
            <div class="control-group">
              <label>Strike Price ($K$): <span id="valBsmK" style="color: var(--accent-amber);">100 USD</span></label>
              <input type="range" id="bsmK" min="50" max="150" step="1" value="100" oninput="updateBsmSim()">
            </div>
            <div class="control-group">
              <label>Implied Volatility ($\sigma$): <span id="valBsmVol" style="color: var(--accent-purple);">24%</span></label>
              <input type="range" id="bsmVol" min="5" max="80" step="1" value="24" oninput="updateBsmSim()">
            </div>
            <div class="control-group">
              <label>Time to Expiry ($T$ yrs): <span id="valBsmT" style="color: var(--accent-cyan);">0.50 yr</span></label>
              <input type="range" id="bsmT" min="0.05" max="2.0" step="0.05" value="0.50" oninput="updateBsmSim()">
            </div>
            <div class="control-group">
              <label>Risk-Free Rate ($r$) / Div Yield ($q$): <span id="valBsmRQ" style="color: var(--accent-emerald);">r=5.0%, q=2.0%</span></label>
              <div style="display:flex; gap:10px;">
                <input type="range" id="bsmR" min="0" max="12" step="0.5" value="5.0" oninput="updateBsmSim()">
                <input type="range" id="bsmQ" min="0" max="8" step="0.5" value="2.0" oninput="updateBsmSim()">
              </div>
            </div>
          </div>
          <div>
            <div class="chart-canvas-wrap" style="height: 290px;">
              <canvas id="bsmChart"></canvas>
            </div>
            <div class="callout callout-info" id="bsmMetricsBox" style="margin-top: 12px; font-size: 12.5px;"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- 12C. SIMULATION 14: QUANTITATIVE METHODS MONTE CARLO & HYPOTHESIS LAB -->
    <section id="sim-quant">
      <div class="card">
        <div class="card-title">🎲 Simulation 14: Quant Monte Carlo GBM, Safety-First &amp; t-Test Engine</div>
        <p style="color: var(--text-secondary); margin-bottom: 15px;">
          Simulate stochastic Geometric Brownian Motion (GBM) asset price paths, inspect Roy's Safety-First shortfall ratio, and compute sample $t$-statistics across drift ($\mu$), volatility ($\sigma$), horizon ($T$), and sample size ($n$).
        </p>
        <div class="grid-2">
          <div>
            <div class="control-group">
              <label>Annual Drift ($\mu$): <span id="valQuantMu" style="color: var(--accent-emerald);">9.0%</span></label>
              <input type="range" id="quantMu" min="0" max="20" step="0.5" value="9.0" oninput="updateQuantSim()">
            </div>
            <div class="control-group">
              <label>Annual Volatility ($\sigma$): <span id="valQuantSigma" style="color: var(--accent-rose);">18.0%</span></label>
              <input type="range" id="quantSigma" min="5" max="45" step="1" value="18" oninput="updateQuantSim()">
            </div>
            <div class="control-group">
              <label>Shortfall Threshold ($R_L$): <span id="valQuantRl" style="color: var(--accent-amber);">2.0%</span></label>
              <input type="range" id="quantRl" min="-5" max="10" step="0.5" value="2.0" oninput="updateQuantSim()">
            </div>
            <div class="control-group">
              <label>Sample Size ($n$ observations): <span id="valQuantN" style="color: var(--accent-blue);">36</span></label>
              <input type="range" id="quantN" min="12" max="120" step="6" value="36" oninput="updateQuantSim()">
            </div>
            <button type="button" class="btn btn-secondary" onclick="updateQuantSim(true)">🎲 Regenerate 12 Monte Carlo Paths</button>
          </div>
          <div>
            <div class="chart-canvas-wrap" style="height: 290px;">
              <canvas id="quantChart"></canvas>
            </div>
            <div class="callout callout-info" id="quantMetricsBox" style="margin-top: 12px; font-size: 12.5px;"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- 12D. SIMULATION 15: ALTERNATIVE INVESTMENTS FEE WATERFALL & HWM ENGINE -->
    <section id="sim-alts">
      <div class="card">
        <div class="card-title">🏛️ Simulation 15: Hedge Fund Fee Waterfall, Hard/Soft Hurdle &amp; High-Water Mark</div>
        <p style="color: var(--text-secondary); margin-bottom: 15px;">
          Model GP vs. LP payout mechanics across Gross Return, Management Fee, Incentive Fee, Hard vs. Soft Hurdle structures, and High-Water Mark loss recovery hurdles on a 100M USD fund.
        </p>
        <div class="grid-2">
          <div>
            <div class="control-group">
              <label>Gross Fund Return: <span id="valAltsGross" style="color: var(--accent-emerald);">+18.0%</span></label>
              <input type="range" id="altsGross" min="-20" max="40" step="1" value="18" oninput="updateAltsSim()">
            </div>
            <div class="control-group">
              <label>Management Fee (% Ending AUM) / Incentive Fee (%): <span id="valAltsFees" style="color: var(--accent-amber);">2.0% / 20%</span></label>
              <div style="display:flex; gap:10px;">
                <input type="range" id="altsMgmt" min="0" max="3" step="0.25" value="2.0" oninput="updateAltsSim()">
                <input type="range" id="altsInc" min="0" max="30" step="5" value="20" oninput="updateAltsSim()">
              </div>
            </div>
            <div class="control-group">
              <label>Hurdle Rate (%): <span id="valAltsHurdle" style="color: var(--accent-cyan);">6.0%</span></label>
              <input type="range" id="altsHurdle" min="0" max="12" step="1" value="6" oninput="updateAltsSim()">
            </div>
            <div class="control-group">
              <label>Prior High-Water Mark (vs. 100M Current NAV): <span id="valAltsHwm" style="color: var(--accent-purple);">100M USD</span></label>
              <input type="range" id="altsHwm" min="100" max="125" step="5" value="100" oninput="updateAltsSim()">
            </div>
            <div class="control-group">
              <label>Hurdle Structure:</label>
              <select id="altsHurdleType" onchange="updateAltsSim()">
                <option value="hard">Hard Hurdle (Incentive on Excess Above Hurdle)</option>
                <option value="soft">Soft Hurdle (Incentive on Full Gain Once Cleared)</option>
              </select>
            </div>
          </div>
          <div>
            <div class="chart-canvas-wrap" style="height: 290px;">
              <canvas id="altsChart"></canvas>
            </div>
            <div class="callout callout-warning" id="altsMetricsBox" style="margin-top: 12px; font-size: 12.5px;"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- 12E. SIMULATION 16: CORPORATE ISSUERS WACC, HAMADA BETA & MM CAPITAL STRUCTURE -->
    <section id="sim-corp">
      <div class="card">
        <div class="card-title">🏢 Simulation 16: Corporate WACC, Hamada Pure-Play Beta &amp; MM Trade-Off Optimizer</div>
        <p style="color: var(--text-secondary); margin-bottom: 15px;">
          Unlever peer equity beta ($\beta_U$), relever to target $D/E$, and visualize Static Trade-Off WACC optimization balancing Modigliani-Miller tax shields ($t \cdot D$) against convex financial distress costs.
        </p>
        <div class="grid-2">
          <div>
            <div class="control-group">
              <label>Target Debt-to-Equity ($D/E$): <span id="valCorpDE" style="color: var(--accent-blue);">0.60</span></label>
              <input type="range" id="corpDE" min="0" max="2.5" step="0.1" value="0.6" oninput="updateCorpSim()">
            </div>
            <div class="control-group">
              <label>Unlevered Asset Beta ($\beta_U$): <span id="valCorpBu" style="color: var(--accent-emerald);">0.95</span></label>
              <input type="range" id="corpBu" min="0.4" max="1.6" step="0.05" value="0.95" oninput="updateCorpSim()">
            </div>
            <div class="control-group">
              <label>Marginal Tax Rate ($t$): <span id="valCorpTax" style="color: var(--accent-amber);">25%</span></label>
              <input type="range" id="corpTax" min="0" max="40" step="1" value="25" oninput="updateCorpSim()">
            </div>
            <div class="control-group">
              <label>Base Pre-Tax Debt Cost ($r_d$): <span id="valCorpRd" style="color: var(--accent-cyan);">5.5%</span></label>
              <input type="range" id="corpRd" min="3.0" max="11.0" step="0.25" value="5.5" oninput="updateCorpSim()">
            </div>
            <div class="control-group">
              <label>Distress Spread Convexity: <span id="valCorpDist" style="color: var(--accent-rose);">1.5%</span></label>
              <input type="range" id="corpDist" min="0" max="4.0" step="0.25" value="1.5" oninput="updateCorpSim()">
            </div>
          </div>
          <div>
            <div class="chart-canvas-wrap" style="height: 290px;">
              <canvas id="corpChart"></canvas>
            </div>
            <div class="callout callout-info" id="corpMetricsBox" style="margin-top: 12px; font-size: 12.5px;"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- 13A. ETHICS & PROFESSIONAL STANDARDS REFERENCE -->
    <section id="eth-reference">
      __NOTES_TABS_ETH__
      <div class="fsa-ref-container">__ETH_REFERENCE_CONTENT__</div>
    </section>

    <!-- 13B. QUANTITATIVE METHODS REFERENCE -->
    <section id="qm-reference">
      __NOTES_TABS_QM__
      <div class="fsa-ref-container">__QM_REFERENCE_CONTENT__</div>
    </section>

    <!-- 13C. ECONOMICS REFERENCE -->
    <section id="econ-reference">
      __NOTES_TABS_ECON__
      <div class="fsa-ref-container">__ECON_REFERENCE_CONTENT__</div>
    </section>

    <!-- 13D. MASTER FSA REFERENCE NOTES -->
    <section id="fsa-reference">
      __NOTES_TABS_FSA__

      <div class="card">
        <div class="card-title">📖 Comprehensive Financial Statement Analysis Reference Library</div>
        <p style="color: var(--text-secondary); margin-bottom: 16px;">
          20 Chapters of Schweser-grade notes, 14 inline worked numerical examples, Off-Balance-Sheet VIEs, Share-Based Comp, 3-Statement Modeling, Sustainability/ESG, comparative IFRS vs US GAAP matrices, and the master formula sheet.
        </p>
        <div class="fsa-nav-bar">
          <a class="fsa-nav-btn" href="#m1-intro">01. Mechanics</a>
          <a class="fsa-nav-btn" href="#m2-standards">02. Standards</a>
          <a class="fsa-nav-btn" href="#m3-income-statement">03. Income Stmt</a>
          <a class="fsa-nav-btn" href="#m4-balance-sheet">04. Balance Sheet</a>
          <a class="fsa-nav-btn" href="#m5-cash-flow">05. Cash Flow</a>
          <a class="fsa-nav-btn" href="#m6-ratios">06. Techniques & Ratios</a>
          <a class="fsa-nav-btn" href="#m7-inventories">07. Inventories</a>
          <a class="fsa-nav-btn" href="#m8-long-lived-assets">08. Long-Lived Assets</a>
          <a class="fsa-nav-btn" href="#m9-taxes">09. Taxes</a>
          <a class="fsa-nav-btn" href="#m10-debt">10. Liabilities</a>
          <a class="fsa-nav-btn" href="#m11-leases">11. Leases</a>
          <a class="fsa-nav-btn" href="#m12-quality-l1">12. Reporting Quality</a>
          <a class="fsa-nav-btn" href="#m13-intercorporate">13. Intercorporate</a>
          <a class="fsa-nav-btn" href="#m14-pensions">14. Pensions</a>
          <a class="fsa-nav-btn" href="#m15-multinational">15. Multinational FX</a>
          <a class="fsa-nav-btn" href="#m16-financial-institutions">16. Financial Inst.</a>
          <a class="fsa-nav-btn" href="#m17-quality-l2">17. Quality Evaluation</a>
          <a class="fsa-nav-btn" href="#m18-integration">18. Integration</a>
          <a class="fsa-nav-btn" href="#master-gaap-ifrs" style="color: var(--accent-amber); font-weight: 700;">GAAP vs IFRS Matrix</a>
          <a class="fsa-nav-btn" href="#master-formulas" style="color: var(--accent-emerald); font-weight: 700;">Formula Sheet</a>
        </div>
      </div>

      <div class="fsa-ref-container">
        __FSA_REFERENCE_CONTENT__
      </div>
    </section>

    <!-- 13E. CORPORATE ISSUERS REFERENCE -->
    <section id="corp-reference">
      __NOTES_TABS_CORP__
      <div class="fsa-ref-container">__CORP_REFERENCE_CONTENT__</div>
    </section>

    <!-- 14. EQUITY INVESTMENTS REFERENCE NOTES -->
    <section id="eq-reference">
      __NOTES_TABS_EQ__
      <div class="fsa-ref-container">
        __EQ_REFERENCE_CONTENT__
      </div>
    </section>

    <!-- 15. FIXED INCOME REFERENCE NOTES -->
    <section id="fi-reference">
      __NOTES_TABS_FI__
      <div class="fsa-ref-container">
        __FI_REFERENCE_CONTENT__
      </div>
    </section>

    <!-- 15B. DERIVATIVES REFERENCE -->
    <section id="deriv-reference">
      __NOTES_TABS_DERIV__
      <div class="fsa-ref-container">__DERIV_REFERENCE_CONTENT__</div>
    </section>

    <!-- 15C. ALTERNATIVE INVESTMENTS REFERENCE -->
    <section id="alt-reference">
      __NOTES_TABS_ALT__
      <div class="fsa-ref-container">__ALT_REFERENCE_CONTENT__</div>
    </section>

    <!-- 16. PORTFOLIO MANAGEMENT REFERENCE NOTES -->
    <section id="pm-reference">
      __NOTES_TABS_PM__
      <div class="fsa-ref-container">
        __PM_REFERENCE_CONTENT__
      </div>
    </section>

    <!-- 14. VISUAL DIAGRAMS & FRAMEWORKS -->
    <section id="reference-diagrams">
      <div class="grid-2">
        <div class="card">
          <div class="card-title">Merton Structural Credit Model: Default Boundary</div>
          <p style="color: var(--text-secondary); font-size: 12px; margin-bottom: 12px;">Equity as a call option on corporate assets with strike = face value of debt $K$.</p>
          <div class="svg-container">
            <svg viewBox="0 0 450 220" style="width: 100%; max-width: 450px; height: auto; display: block; margin: 0 auto;">
              <line x1="40" y1="180" x2="420" y2="180" stroke="var(--text-secondary)" stroke-width="2"/>
              <line x1="40" y1="20" x2="40" y2="180" stroke="var(--text-secondary)" stroke-width="2"/>
              <text x="350" y="200" fill="var(--text-secondary)" font-size="11">Time to Maturity (T)</text>
              <text x="50" y="30" fill="var(--text-secondary)" font-size="11">Asset Value V_A</text>
              <line x1="40" y1="110" x2="420" y2="110" stroke="var(--accent-rose)" stroke-width="2" stroke-dasharray="4"/>
              <text x="300" y="105" fill="var(--accent-rose)" font-size="11">Default Boundary (Debt K)</text>
              <path d="M 40 80 Q 140 50 230 70 T 420 40" fill="none" stroke="var(--accent-emerald)" stroke-width="3"/>
              <text x="425" y="45" fill="var(--accent-emerald)" font-size="11">Solvent Path</text>
              <path d="M 40 80 Q 140 100 230 130 T 360 170" fill="none" stroke="var(--accent-rose)" stroke-width="3"/>
              <text x="370" y="170" fill="var(--accent-rose)" font-size="11">Default</text>
            </svg>
          </div>
        </div>

        <div class="card">
          <div class="card-title">Bond Price-Yield Relationship: Convexity</div>
          <p style="color: var(--text-secondary); font-size: 12px; margin-bottom: 12px;">Option-free positive convexity vs. Callable bond negative convexity at lower yields.</p>
          <div class="svg-container">
            <svg viewBox="0 0 450 220" style="width: 100%; max-width: 450px; height: auto; display: block; margin: 0 auto;">
              <line x1="40" y1="180" x2="420" y2="180" stroke="var(--text-secondary)" stroke-width="2"/>
              <line x1="40" y1="20" x2="40" y2="180" stroke="var(--text-secondary)" stroke-width="2"/>
              <text x="360" y="200" fill="var(--text-secondary)" font-size="11">Yield to Maturity</text>
              <text x="50" y="30" fill="var(--text-secondary)" font-size="11">Bond Price</text>
              <line x1="40" y1="65" x2="420" y2="65" stroke="var(--accent-amber)" stroke-width="1.5" stroke-dasharray="3"/>
              <text x="340" y="60" fill="var(--accent-amber)" font-size="11">Call Price Cap</text>
              <path d="M 50 35 Q 150 110 400 170" fill="none" stroke="var(--accent-blue)" stroke-width="3"/>
              <text x="280" y="130" fill="var(--accent-blue)" font-size="11">Option-Free Bond</text>
              <path d="M 50 65 Q 120 65 170 85 T 400 170" fill="none" stroke="var(--accent-rose)" stroke-width="3" stroke-dasharray="6"/>
              <text x="110" y="55" fill="var(--accent-rose)" font-size="11">Callable Bond (Negative Convexity)</text>
            </svg>
          </div>
        </div>

        <div class="card">
          <div class="card-title">Porter's Five Forces Framework</div>
          <p style="color: var(--text-secondary); font-size: 12px; margin-bottom: 12px;">Industry competitive structure analysis for equity analysts.</p>
          <div class="svg-container">
            <svg viewBox="0 0 450 220" style="width: 100%; max-width: 450px; height: auto; display: block; margin: 0 auto;">
              <rect x="150" y="80" width="150" height="60" rx="8" fill="var(--bg-secondary)" stroke="var(--accent-blue)" stroke-width="2"/>
              <text x="225" y="105" fill="var(--text-primary)" font-size="12" font-weight="700" text-anchor="middle">Industry Rivalry</text>
              <text x="225" y="125" fill="var(--text-secondary)" font-size="10" text-anchor="middle">Existing Competitors</text>
              <rect x="150" y="10" width="150" height="45" rx="6" fill="var(--bg-secondary)" stroke="var(--accent-cyan)" stroke-width="1.5"/>
              <text x="225" y="38" fill="var(--text-primary)" font-size="11" text-anchor="middle">Threat of New Entrants</text>
              <rect x="150" y="165" width="150" height="45" rx="6" fill="var(--bg-secondary)" stroke="var(--accent-emerald)" stroke-width="1.5"/>
              <text x="225" y="193" fill="var(--text-primary)" font-size="11" text-anchor="middle">Threat of Substitutes</text>
              <rect x="10" y="85" width="120" height="50" rx="6" fill="var(--bg-secondary)" stroke="var(--accent-amber)" stroke-width="1.5"/>
              <text x="70" y="107" fill="var(--text-primary)" font-size="10" text-anchor="middle">Supplier Power</text>
              <text x="70" y="123" fill="var(--text-secondary)" font-size="9" text-anchor="middle">Input Pricing</text>
              <rect x="320" y="85" width="120" height="50" rx="6" fill="var(--bg-secondary)" stroke="var(--accent-purple)" stroke-width="1.5"/>
              <text x="380" y="107" fill="var(--text-primary)" font-size="10" text-anchor="middle">Buyer Power</text>
              <text x="380" y="123" fill="var(--text-secondary)" font-size="9" text-anchor="middle">Bargaining Leverage</text>
            </svg>
          </div>
        </div>

        <div class="card">
          <div class="card-title">CFA Exam Master Formula Cheatsheet</div>
          <div style="font-size: 12.5px; line-height: 1.8;">
            <div><strong>Bond Price:</strong> $$PV = \sum_{t=1}^N \frac{PMT}{(1+r)^t} + \frac{FV}{(1+r)^N}$$</div>
            <div><strong>Macaulay & Modified Duration:</strong> $$ModDur = \frac{MacDur}{1+y}, \quad \%\Delta P \approx -ModDur \times \Delta y + \frac{1}{2} Conv \times (\Delta y)^2$$</div>
            <div><strong>Two-Stage DDM:</strong> $$V_0 = \sum_{t=1}^n \frac{D_0(1+g_S)^t}{(1+r)^t} + \frac{D_0(1+g_S)^n(1+g_L)}{(r - g_L)(1+r)^n}$$</div>
            <div><strong>DuPont 5-Way:</strong> $$ROE = \frac{NI}{EBT} \times \frac{EBT}{EBIT} \times \frac{EBIT}{Rev} \times \frac{Rev}{Assets} \times \frac{Assets}{Equity}$$</div>
            <div><strong>FCFF from Net Income:</strong> $$FCFF = NI + NCC + Int(1 - T) - FCInv - WCInv$$</div>
          </div>
        </div>
      </div>
    </section>

    <!-- 12B. CFA TERMINOLOGY & MATHEMATICAL JARGON ENGINE -->
    <section id="jargon-glossary">
      <div class="card" style="margin-bottom: 24px; border-left: 4px solid var(--accent-amber);">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 16px;">
          <div>
            <h2 style="font-family: var(--font-serif); font-size: 26px; font-weight: 700; margin-bottom: 6px;">CFA Terminology & Mathematical Jargon Engine</h2>
            <p style="color: var(--text-secondary); max-width: 850px; font-size: 13.5px; line-height: 1.6;">
              Instant, deep-dive conceptual cards for essential CFA Level 1 & Level 2 financial jargon. Hover over any underlined terminology anywhere in exam questions or vignettes to reveal intuitive definitions, KaTeX formulas, practical uses, common exam traps, and complete step-by-step worked numerical examples.
            </p>
          </div>
          <div style="text-align: right; font-family: var(--font-mono);">
            <div style="font-size: 24px; font-weight: 700; color: var(--accent-amber);" id="jargonCountDisplay">64 Master Entries</div>
            <div style="font-size: 11px; color: var(--text-secondary);">Interactive Hover Cards & Worked Solutions</div>
          </div>
        </div>
      </div>

      <!-- Filter Bar -->
      <div class="filter-bar" style="margin-bottom: 20px; display: flex; flex-direction: column; gap: 12px;">
        <div style="display: flex; gap: 6px; flex-wrap: wrap; align-items: center;">
          <span style="font-family: var(--font-mono); font-size: 11px; text-transform: uppercase; color: var(--text-muted); font-weight: 700; margin-right: 4px;">Subject:</span>
          <button class="filter-btn active" id="glossSubj-all" onclick="filterJargonGlossary('all', currentGlossaryLevel)">All (64)</button>
          <button class="filter-btn" id="glossSubj-eth" onclick="filterJargonGlossary('ETH', currentGlossaryLevel)">Ethics (6)</button>
          <button class="filter-btn" id="glossSubj-qm" onclick="filterJargonGlossary('QM', currentGlossaryLevel)">Quant (6)</button>
          <button class="filter-btn" id="glossSubj-econ" onclick="filterJargonGlossary('ECON', currentGlossaryLevel)">Econ (5)</button>
          <button class="filter-btn" id="glossSubj-fsa" onclick="filterJargonGlossary('FSA', currentGlossaryLevel)">FSA (8)</button>
          <button class="filter-btn" id="glossSubj-corp" onclick="filterJargonGlossary('CORP', currentGlossaryLevel)">Corp (5)</button>
          <button class="filter-btn" id="glossSubj-eq" onclick="filterJargonGlossary('EQ', currentGlossaryLevel)">Equity (8)</button>
          <button class="filter-btn" id="glossSubj-fi" onclick="filterJargonGlossary('FI', currentGlossaryLevel)">FI (8)</button>
          <button class="filter-btn" id="glossSubj-deriv" onclick="filterJargonGlossary('DERIV', currentGlossaryLevel)">Deriv (5)</button>
          <button class="filter-btn" id="glossSubj-alt" onclick="filterJargonGlossary('ALT', currentGlossaryLevel)">Alts (5)</button>
          <button class="filter-btn" id="glossSubj-pm" onclick="filterJargonGlossary('PM', currentGlossaryLevel)">PM (8)</button>
        </div>
        <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
          <span style="font-family: var(--font-mono); font-size: 11px; text-transform: uppercase; color: var(--text-muted); font-weight: 700; margin-right: 4px;">Level:</span>
          <button class="filter-btn active" id="glossLvl-all" onclick="filterJargonGlossary(currentGlossarySubj, 'all')">All Levels</button>
          <button class="filter-btn" id="glossLvl-l1" onclick="filterJargonGlossary(currentGlossarySubj, 'L1')">Level 1</button>
          <button class="filter-btn" id="glossLvl-l2" onclick="filterJargonGlossary(currentGlossarySubj, 'L2')">Level 2</button>
          <button class="filter-btn" id="glossLvl-both" onclick="filterJargonGlossary(currentGlossarySubj, 'Both')">Both (Core)</button>
          <input type="text" id="glossarySearchInput" placeholder="Search terminologies, formulas, or acronyms (e.g. DuPont, FCFF, Duration, OAS, VaR)..." style="flex: 1 1 250px; min-width: 200px; padding: 7px 12px; background: var(--bg-tertiary); border: 1px solid var(--border-color); color: var(--text-primary); border-radius: 4px; font-size: 13px; font-family: var(--font-sans);" oninput="filterJargonGlossary(currentGlossarySubj, currentGlossaryLevel, this.value)">
        </div>
      </div>

      <!-- Container -->
      <div id="jargonGlossaryListContainer">
        <!-- Rendered via JS -->
      </div>
    </section>

    <!-- 13. MASTER SOLVED NUMERICALS & WORKED SOLUTIONS -->
    <section id="solved-numericals">
      <div class="card" style="margin-bottom: 24px; border-left: 4px solid var(--accent-amber);">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 16px;">
          <div>
            <h2 style="font-family: var(--font-serif); font-size: 26px; font-weight: 700; margin-bottom: 6px;">Master Solved Numericals & Worked Solutions</h2>
            <p style="color: var(--text-secondary); max-width: 850px; font-size: 13.5px;">
              Exhaustive step-by-step mathematical solutions graduated from Easy (Level 1 Foundational) to Moderate (Intermediate) to Difficult (Level 2 Multi-Step Item Sets) across all 10 CFA CBOK courses.
            </p>
          </div>
          <div style="text-align: right; font-family: var(--font-mono);">
            <div style="font-size: 24px; font-weight: 700; color: var(--accent-amber);" id="numericalsCountDisplay">63 Problems</div>
            <div style="font-size: 11px; color: var(--text-secondary);">100% Python-Verified KaTeX &amp; Currency</div>
          </div>
        </div>
      </div>

      <!-- Filter Bar -->
      <div class="filter-bar" style="margin-bottom: 20px; display: flex; flex-direction: column; gap: 12px;">
        <div style="display: flex; gap: 6px; flex-wrap: wrap; align-items: center;">
          <span style="font-family: var(--font-mono); font-size: 11px; text-transform: uppercase; color: var(--text-muted); font-weight: 700; margin-right: 4px;">Subject:</span>
          <button class="filter-btn active" id="numSubj-all" onclick="filterNumericals('all', currentNumDiff)">All (63)</button>
          <button class="filter-btn" id="numSubj-eth" onclick="filterNumericals('Ethical and Professional Standards', currentNumDiff)">Ethics/GIPS (6)</button>
          <button class="filter-btn" id="numSubj-qm" onclick="filterNumericals('Quantitative Methods', currentNumDiff)">Quant (6)</button>
          <button class="filter-btn" id="numSubj-econ" onclick="filterNumericals('Economics', currentNumDiff)">Econ (6)</button>
          <button class="filter-btn" id="numSubj-fsa" onclick="filterNumericals('Financial Statement Analysis', currentNumDiff)">FSA (9)</button>
          <button class="filter-btn" id="numSubj-corp" onclick="filterNumericals('Corporate Issuers', currentNumDiff)">Corp (6)</button>
          <button class="filter-btn" id="numSubj-eq" onclick="filterNumericals('Equity Investments', currentNumDiff)">Equity (6)</button>
          <button class="filter-btn" id="numSubj-fi" onclick="filterNumericals('Fixed Income', currentNumDiff)">FI (6)</button>
          <button class="filter-btn" id="numSubj-deriv" onclick="filterNumericals('Derivatives', currentNumDiff)">Deriv (6)</button>
          <button class="filter-btn" id="numSubj-alt" onclick="filterNumericals('Alternative Investments', currentNumDiff)">Alts (6)</button>
          <button class="filter-btn" id="numSubj-pm" onclick="filterNumericals('Portfolio Management', currentNumDiff)">PM (6)</button>
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
      <div class="card" style="margin-bottom: 24px; border-left: 4px solid var(--accent-emerald);">
        <h2 style="font-family: var(--font-serif); font-size: 26px; font-weight: 700; margin-bottom: 6px;">2026–2027 CFA CBOK Complete 12-Section Audit &amp; L1/L2 Master Matrix</h2>
        <p style="color: var(--text-secondary); max-width: 960px; font-size: 13.5px; line-height: 1.6;">
          100% Coverage across ALL 10 Level I/II CBOK Courses + CBOK XI (Asset Allocation) &amp; XII (Performance Measurement): <strong>2,210 Audited Q-Bank Questions</strong> (1,225 L1 MCQs + 985 L2 Questions across 183 Vignettes), <strong>105 Curriculum Modules</strong>, <strong>160+ Inline Chapter Exercises</strong> (Solved &amp; Unsolved), <strong>63 Master Solved Numericals</strong>, <strong>64 Jargon Entries</strong>, and <strong>16 Interactive Simulators</strong>.
        </p>
      </div>

      <!-- Macro 10-Topic Matrix (2027 CBOK Weights) -->
      <div class="card" style="margin-bottom: 24px;">
        <h3 style="font-family: var(--font-serif); font-size: 19px; margin-bottom: 14px;">Official 2027 CFA CBOK Complete Scope &amp; Coverage Matrix (100% Covered)</h3>
        <div class="table-container">
          <table style="width: 100%; border-collapse: collapse; font-size: 13px;">
            <thead>
              <tr style="border-bottom: 2px solid var(--border-color); text-align: left;">
                <th style="padding: 10px; font-family: var(--font-mono);">CBOK Topic Area (2027 Naming)</th>
                <th style="padding: 10px; font-family: var(--font-mono);">L1 Weight (2027)</th>
                <th style="padding: 10px; font-family: var(--font-mono);">L2 Weight (2027)</th>
                <th style="padding: 10px; font-family: var(--font-mono);">Portal Status</th>
                <th style="padding: 10px; font-family: var(--font-mono);">Embedded Questions, Notes &amp; Exercises</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom: 1px solid var(--border-color); background: rgba(16, 185, 129, 0.05);">
                <td style="padding: 10px; font-weight: 600;">I. Ethical &amp; Professional Standards</td>
                <td style="padding: 10px; font-family: var(--font-mono);">10%–15%</td>
                <td style="padding: 10px; font-family: var(--font-mono);">10%–15%</td>
                <td style="padding: 10px;"><span class="badge-diff-easy">COVERED (500)</span></td>
                <td style="padding: 10px; color: var(--accent-emerald);">270 L1 + 180 L2 (30 V) + 50 Inline Drills (25 Solved/25 Unsolved) + 10 Ch. (12th Ed. I–VII, GIPS, AMC) + 6 GIPS/Fee Cases</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-color); background: rgba(16, 185, 129, 0.05);">
                <td style="padding: 10px; font-weight: 600;">II. Quantitative Methods</td>
                <td style="padding: 10px; font-family: var(--font-mono);">11%–14%</td>
                <td style="padding: 10px; font-family: var(--font-mono);">5%–10%</td>
                <td style="padding: 10px;"><span class="badge-diff-easy">COVERED</span></td>
                <td style="padding: 10px; color: var(--accent-emerald);">90 L1 + 60 L2 (10 V) + 12 Ch. + 24 Drills (TVM, Regression, AR(1), GARCH, Backtesting, ML &amp; GenAI/LLM) + Sim Lab</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-color); background: rgba(16, 185, 129, 0.05);">
                <td style="padding: 10px; font-weight: 600;">III. Economics</td>
                <td style="padding: 10px; font-family: var(--font-mono);">6%–9%</td>
                <td style="padding: 10px; font-family: var(--font-mono);">5%–10%</td>
                <td style="padding: 10px;"><span class="badge-diff-easy">COVERED</span></td>
                <td style="padding: 10px; color: var(--accent-emerald);">80 L1 + 50 L2 (10 V) + 10 Ch. + 20 Drills (Structures, Macro Policy, FX Parity, Carry, Geopolitics, Solow Growth)</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-color); background: rgba(16, 185, 129, 0.05);">
                <td style="padding: 10px; font-weight: 600;">IV. Financial Statement Analysis (FSA)</td>
                <td style="padding: 10px; font-family: var(--font-mono);">11%–14%</td>
                <td style="padding: 10px; font-family: var(--font-mono);">10%–15%</td>
                <td style="padding: 10px;"><span class="badge-diff-easy">COVERED</span></td>
                <td style="padding: 10px; color: var(--accent-emerald);">190 L1 + 270 L2 (48 V) + 20 Ch. + 14 Inline Worked Examples (Share-Based Comp, VIEs, IAS 29, 3-Stmt Model, ESG)</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-color); background: rgba(16, 185, 129, 0.05);">
                <td style="padding: 10px; font-weight: 600;">V. Corporate Issuers (prev. Finance)</td>
                <td style="padding: 10px; font-family: var(--font-mono);">6%–9%</td>
                <td style="padding: 10px; font-family: var(--font-mono);">5%–10%</td>
                <td style="padding: 10px;"><span class="badge-diff-easy">COVERED</span></td>
                <td style="padding: 10px; color: var(--accent-emerald);">80 L1 + 50 L2 (10 V) + 9 Ch. + 20 Drills (Governance/ESG, CCC, Hamada WACC, MM I/II, Buybacks, M&amp;A) + Sim Lab</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-color); background: rgba(16, 185, 129, 0.05);">
                <td style="padding: 10px; font-weight: 600;">VI. Equities (prev. Equity Investments)</td>
                <td style="padding: 10px; font-family: var(--font-mono);">11%–14%</td>
                <td style="padding: 10px; font-family: var(--font-mono);">10%–15%</td>
                <td style="padding: 10px;"><span class="badge-diff-easy">COVERED</span></td>
                <td style="padding: 10px; color: var(--accent-emerald);">115 L1 + 95 L2 (19 V) + 8 Ch. + 11 Inline Worked Examples (2027 L1 Forecasting, Cost of Equity, Shorting, EEM, SOTP)</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-color); background: rgba(16, 185, 129, 0.05);">
                <td style="padding: 10px; font-weight: 600;">VII. Fixed Income (FI)</td>
                <td style="padding: 10px; font-family: var(--font-mono);">11%–14%</td>
                <td style="padding: 10px; font-family: var(--font-mono);">10%–15%</td>
                <td style="padding: 10px;"><span class="badge-diff-easy">COVERED</span></td>
                <td style="padding: 10px; color: var(--accent-emerald);">120 L1 + 85 L2 (17 V) + 8 Ch. + 11 Inline Worked Examples (Repo/Shorting, Convertibles, CDS, Vasicek/CIR, Green Bonds)</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-color); background: rgba(16, 185, 129, 0.05);">
                <td style="padding: 10px; font-weight: 600;">VIII. Derivatives &amp; Risk Management</td>
                <td style="padding: 10px; font-family: var(--font-mono);">6%–9%</td>
                <td style="padding: 10px; font-family: var(--font-mono);">5%–10%</td>
                <td style="padding: 10px;"><span class="badge-diff-easy">COVERED</span></td>
                <td style="padding: 10px; color: var(--accent-emerald);">85 L1 + 55 L2 (11 V) + 9 Ch. + 20 Drills (Forwards, FRAs, IRS/FX/Eq Swaps, Binomial, BSM &amp; Greeks) + BSM Sim Lab</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-color); background: rgba(16, 185, 129, 0.05);">
                <td style="padding: 10px; font-weight: 600;">IX. Alternative Investments</td>
                <td style="padding: 10px; font-family: var(--font-mono);">6%–9%</td>
                <td style="padding: 10px; font-family: var(--font-mono);">5%–10%</td>
                <td style="padding: 10px;"><span class="badge-diff-easy">COVERED</span></td>
                <td style="padding: 10px; color: var(--accent-emerald);">75 L1 + 50 L2 (10 V) + 9 Ch. + 20 Drills (HF Waterfall, PE/VC, Real Estate/REITs, Commodities, Digital Assets) + Alts Sim</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-color); background: rgba(16, 185, 129, 0.05);">
                <td style="padding: 10px; font-weight: 600;">X–XII. Portfolio Mgmt, AA &amp; Performance</td>
                <td style="padding: 10px; font-family: var(--font-mono);">8%–12%</td>
                <td style="padding: 10px; font-family: var(--font-mono);">10%–15%</td>
                <td style="padding: 10px;"><span class="badge-diff-easy">COVERED (L1–L3)</span></td>
                <td style="padding: 10px; color: var(--accent-emerald);">120 L1 + 90 L2 (18 V) + 10 Ch. (Behavioral, VaR/CVaR, Brinson-Fachler, LDI/SAA/TAA, Manager Selection, Fintech)</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Simultaneous L1 & L2 Preparation Critique -->
      <div class="card" style="margin-bottom: 24px; border-left: 4px solid var(--accent-amber);">
        <h3 style="font-family: var(--font-serif); font-size: 19px; margin-bottom: 10px;">Strategic Exam Prep Roadmap (100% CBOK Coverage + Practical Requirements)</h3>
        <ul style="font-size: 13.5px; line-height: 1.7; color: var(--text-secondary); padding-left: 20px;">
          <li><strong>100% L1 &amp; L2 Exam Footprint Achieved</strong>: Every CBOK I–XII topic is now unified in one workspace with 2,210 interactive questions (1,225 L1 + 985 L2 across 183 vignettes), 105 Reference Chapters, 160+ Chapter Exercises, and 63 Python-verified Master Solved Numericals.</li>
          <li><strong>Ethics Mastery Strategy (500 Exercises)</strong>: Ethics acts as CFA Institute's borderline pass/fail tiebreaker. Use the Unsolved Self-Test Mode inside Ethics Reference &amp; Question Bank to drill all 450 Q-Bank scenarios + 50 chapter exercises until accuracy exceeds 85%.</li>
          <li><strong>Mandatory Official CFA Requirements Outside Any Study Suite</strong>: Complete at least one official <strong>Practical Skills Module (PSM)</strong> per level in the CFA Learning Ecosystem (scores are withheld without PSM completion) and practice timed computer-based mocks with a physical <strong>BA II Plus / HP 12C</strong> calculator.</li>
        </ul>
      </div>
    </section>

  <!-- Jargon Popover & Mobile Backdrop Portal -->
  <div id="cfaJargonBackdrop" class="cfa-jargon-backdrop" style="display: none;" onclick="closeJargonPopover()"></div>
  <div id="cfaJargonPopover" class="cfa-jargon-popover" style="display: none;" onmouseenter="cancelJargonClose()" onmouseleave="handleJargonPopoverLeave()">
    <div class="cfa-jargon-popover-header" id="cfaJargonPopoverHeader"></div>
    <div class="cfa-jargon-popover-body" id="cfaJargonPopoverBody"></div>
  </div>

  </main>

  <script>
    // Embedded Master Question Bank (875 Questions)
    const questionBank = __QUESTION_BANK_DATA__;

    // State
    let answeredQuestions = JSON.parse(localStorage.getItem('cfa_answered_qs') || '{}');
    let totalAnswered = Object.keys(answeredQuestions).length;
    let correctCount = Object.values(answeredQuestions).filter(a => a.correct).length;

    let currentL1List = [];
    let l1CurrentIdx = 0;
    let l1ViewMode = 'card'; // 'card' or 'list'

    let vignettesMap = {};
    let currentL2VignetteId = '';

    // Mobile Navigation Controls
    function toggleMobileNav() {
      const sidebar = document.getElementById('appSidebar');
      const backdrop = document.getElementById('sidebarBackdrop');
      if (sidebar) sidebar.classList.toggle('mobile-open');
      if (backdrop) backdrop.classList.toggle('active');
    }

    function closeMobileNav() {
      const sidebar = document.getElementById('appSidebar');
      const backdrop = document.getElementById('sidebarBackdrop');
      if (sidebar) sidebar.classList.remove('mobile-open');
      if (backdrop) backdrop.classList.remove('active');
    }

    // Tab Navigation
    function switchTab(tabId) {
      closeMobileNav();
      document.querySelectorAll('main > section').forEach(s => s.classList.remove('active'));
      const activeSec = document.getElementById(tabId);
      if (activeSec) activeSec.classList.add('active');

      document.querySelectorAll('.nav-links a').forEach(a => {
        a.classList.toggle('active', a.getAttribute('href') === '#' + tabId);
      });

      const titles = {
        'overview': 'Curriculum Overview & Analytics (10 CBOK Courses)',
        'l1-practice': 'Level 1 Question Bank (1,225 Questions)',
        'l2-vignettes': 'Level 2 Case Vignette Explorer (183 Item Sets / 985 Questions)',
        'sim-yield': 'Yield Curve Dynamics Simulator',
        'sim-tree': 'Binomial Interest Rate Tree Engine',
        'sim-equity': 'Equity Valuation: DDM & DuPont Explorer',
        'sim-duration': 'Key Rate Duration Visualizer',
        'sim-frn': 'Floating-Rate Note Pricing Engine',
        'sim-ri-decay': 'Residual Income Persistence Decay',
        'sim-waterfall': 'FCFF → FCFE Cash Flow Waterfall',
        'sim-translation': 'Foreign Currency Translation Engine',
        'sim-prepayment': 'MBS Prepayment Simulator',
        'sim-frontier': 'Markowitz Mean-Variance Frontier & CAL Optimizer',
        'sim-fundamental-law': 'Grinold\'s Fundamental Law of Active Management',
        'sim-rebalancing': 'Dynamic Rebalancing Corridors & Tolerance Bands',
        'sim-bsm': 'Black-Scholes-Merton (BSM) & Option Greeks Engine',
        'sim-quant': 'Quant Monte Carlo GBM, Safety-First & t-Test Engine',
        'sim-alts': 'Hedge Fund Fee Waterfall, Hurdle & HWM Simulator',
        'sim-corp': 'Corporate WACC, Hamada Beta & MM Capital Structure Optimizer',
        'eth-reference': 'I. Ethical & Professional Standards (10 Ch + 50 Exercises)',
        'qm-reference': 'II. Quantitative Methods Reference Library (12 Ch)',
        'econ-reference': 'III. Economics & Global Macro Reference (10 Ch)',
        'fsa-reference': 'IV. FSA Master Reference Library (20 Modules)',
        'corp-reference': 'V. Corporate Issuers Reference Library (9 Ch)',
        'eq-reference': 'VI. Equity Valuation Reference Library & Models (8 Ch)',
        'fi-reference': 'VII. Fixed Income Master Reference & Formulas (8 Ch)',
        'deriv-reference': 'VIII. Derivatives & Risk Management Reference (9 Ch)',
        'alt-reference': 'IX. Alternative Investments Reference Library (9 Ch)',
        'pm-reference': 'X–XII. Portfolio Management, AA & Performance (10 Ch)',
        'reference-diagrams': 'Visual Frameworks & Cheat Sheets',
        'jargon-glossary': 'CFA Terminology & Mathematical Jargon Engine (64 Master Entries)',
        'solved-numericals': 'Master Solved Numericals & Worked Solutions (63 Cases)',
        'curriculum-audit': '2026–2027 CFA CBOK Complete 12-Section Audit Matrix'
      };

      document.getElementById('topTitle').innerHTML = `<h2>${titles[tabId] || 'CFA Master Suite'}</h2>`;
      if (tabId === 'jargon-glossary') {
        renderJargonGlossary();
      }
      if (tabId === 'solved-numericals') {
        renderSolvedNumericals();
      }
      if (window.location.hash !== '#' + tabId) {
        history.replaceState(null, '', '#' + tabId);
      }
      const m = document.querySelector('main');
      if (m) m.scrollTo({ top: 0, behavior: 'smooth' });
      window.scrollTo({ top: 0, behavior: 'smooth' });
      window.dispatchEvent(new Event('resize'));
      if (tabId.endsWith('-reference')) {
        initReferenceNotesCharts();
      }
      renderMath();
    }

    // Theme toggle with persistence
    function toggleTheme() {
      const current = document.documentElement.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('cfa_theme', next);
      window.dispatchEvent(new Event('resize'));
    }

    const savedTheme = localStorage.getItem('cfa_theme');
    if (savedTheme) {
      document.documentElement.setAttribute('data-theme', savedTheme);
    }

    // KaTeX helper & Jargon Auto-Highlighter
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
      // Scan and attach interactive jargon hover cards across rendered text
      if (typeof scanAndHighlightJargon === 'function') {
        scanAndHighlightJargon(document.body);
      }
    }

    function updateScoreBadge() {
      const pct = totalAnswered > 0 ? Math.round((correctCount / totalAnswered) * 100) : 0;
      document.getElementById('scoreDisplay').innerText = `${correctCount} / ${totalAnswered} (${pct}%)`;
      localStorage.setItem('cfa_answered_qs', JSON.stringify(answeredQuestions));
      updateAccuracyChart();
    }

    function resetScores() {
      if (confirm('Are you sure you want to reset all answered questions and practice scores?')) {
        answeredQuestions = {};
        totalAnswered = 0;
        correctCount = 0;
        localStorage.removeItem('cfa_answered_qs');
        updateScoreBadge();
        renderL1Question();
        loadL2Vignette();
      }
    }

    // Shared Subject Mapping & Interactive Chapter Exercise Helpers
    const CBOK_SUBJECTS = [
      'Ethical and Professional Standards',
      'Quantitative Methods',
      'Economics',
      'Financial Statement Analysis',
      'Corporate Issuers',
      'Equity Investments',
      'Fixed Income',
      'Derivatives',
      'Alternative Investments',
      'Portfolio Management'
    ];

    function getSubjectBadgeClass(subj) {
      const m = {
        'Ethical and Professional Standards': 'badge-eth', 'ETH': 'badge-eth',
        'Quantitative Methods': 'badge-qm', 'QM': 'badge-qm',
        'Economics': 'badge-econ', 'ECON': 'badge-econ',
        'Financial Statement Analysis': 'badge-fsa', 'FSA': 'badge-fsa',
        'Corporate Issuers': 'badge-corp', 'CORP': 'badge-corp',
        'Equity Investments': 'badge-eq', 'EQ': 'badge-eq',
        'Fixed Income': 'badge-fi', 'FI': 'badge-fi',
        'Derivatives': 'badge-deriv', 'DERIV': 'badge-deriv',
        'Alternative Investments': 'badge-alt', 'ALT': 'badge-alt',
        'Portfolio Management': 'badge-pm', 'PM': 'badge-pm'
      };
      return m[subj] || 'badge-fsa';
    }

    function getSubjectShortName(subj) {
      const m = {
        'Ethical and Professional Standards': 'Ethics',
        'Quantitative Methods': 'Quant',
        'Economics': 'Econ',
        'Financial Statement Analysis': 'FSA',
        'Corporate Issuers': 'Corp',
        'Equity Investments': 'Equity',
        'Fixed Income': 'FI',
        'Derivatives': 'Deriv',
        'Alternative Investments': 'Alts',
        'Portfolio Management': 'PM'
      };
      return m[subj] || subj;
    }

    function toggleChapterExercises(containerId, expand) {
      const root = document.getElementById(containerId);
      if (!root) return;
      root.querySelectorAll('details.exercise-solution-details').forEach(d => {
        if (expand) d.setAttribute('open', '');
        else d.removeAttribute('open');
      });
    }

    function jumpToSubjectBank(level, subject) {
      if (level === 1) {
        switchTab('l1-practice');
        const sel = document.getElementById('l1SubjectSelect');
        if (sel) {
          sel.value = subject;
          onL1SubjectChange();
        }
      } else {
        switchTab('l2-vignettes');
        const sel = document.getElementById('l2SubjectSelect');
        if (sel) {
          sel.value = subject;
          onL2SubjectChange();
        }
      }
    }

    // Telemetry Charts
    let overviewChart = null;
    let accuracyChart = null;

    function initOverviewChart() {
      const counts = CBOK_SUBJECTS.map(s => questionBank.filter(q => q.subject === s).length);
      const shortLabels = CBOK_SUBJECTS.map((s, i) => `${getSubjectShortName(s)} (${counts[i]} Q)`);
      const ctx = document.getElementById('overviewChart').getContext('2d');
      overviewChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: shortLabels,
          datasets: [{
            data: counts,
            backgroundColor: ['#f85149', '#3b82f6', '#0891b2', '#d29922', '#d97706', '#3fb950', '#39c5cf', '#7c3aed', '#10b981', '#bc8cff'],
            borderColor: '#161b22',
            borderWidth: 2
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { position: 'right', labels: { color: '#8b949e', boxWidth: 10, font: { size: 11 } } }
          }
        }
      });
    }

    function initAccuracyChart() {
      const ctx = document.getElementById('accuracyChart').getContext('2d');
      accuracyChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: CBOK_SUBJECTS.map(getSubjectShortName),
          datasets: [
            { label: 'Correct', data: CBOK_SUBJECTS.map(() => 0), backgroundColor: '#3fb950' },
            { label: 'Incorrect', data: CBOK_SUBJECTS.map(() => 0), backgroundColor: '#f85149' }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: { stacked: true, grid: { color: '#21262d' } },
            y: { stacked: true, grid: { color: '#21262d' } }
          },
          plugins: {
            legend: { position: 'bottom', labels: { color: '#8b949e', boxWidth: 12 } }
          }
        }
      });
      updateAccuracyChart();
    }

    function updateAccuracyChart() {
      if (!accuracyChart) return;
      const correctBySubj = CBOK_SUBJECTS.map(() => 0);
      const incorrectBySubj = CBOK_SUBJECTS.map(() => 0);

      for (const [qid, rec] of Object.entries(answeredQuestions)) {
        const q = questionBank.find(item => item.id === qid);
        if (q) {
          const idx = CBOK_SUBJECTS.indexOf(q.subject);
          if (idx !== -1) {
            if (rec.correct) correctBySubj[idx]++;
            else incorrectBySubj[idx]++;
          }
        }
      }

      accuracyChart.data.datasets[0].data = correctBySubj;
      accuracyChart.data.datasets[1].data = incorrectBySubj;
      accuracyChart.update();
    }

    // ==========================================
    // LEVEL 1 QUESTION BANK LOGIC
    // ==========================================
    function initL1Engine() {
      populateL1Topics();
      filterL1Questions();
    }

    function populateL1Topics() {
      const subj = document.getElementById('l1SubjectSelect').value;
      const topicSelect = document.getElementById('l1TopicSelect');
      topicSelect.innerHTML = '<option value="ALL">All Learning Modules</option>';

      const l1Qs = questionBank.filter(q => q.level === 1 && (subj === 'ALL' || q.subject === subj));
      const topics = [...new Set(l1Qs.map(q => q.module_title || q.topic))].filter(Boolean).sort();

      topics.forEach(t => {
        const opt = document.createElement('option');
        opt.value = t;
        opt.innerText = t;
        topicSelect.appendChild(opt);
      });
    }

    function onL1SubjectChange() {
      populateL1Topics();
      filterL1Questions();
    }

    function onL1TopicChange() {
      filterL1Questions();
    }

    function onL1Search() {
      filterL1Questions();
    }

    let l1TypeFilter = 'ALL';
    let l2TypeFilter = 'ALL';
    let l1PracticeMode = 'study'; // 'study' (immediate solution) or 'unsolved' (reveal on demand)
    let l1ListPage = 0;
    const L1_PAGE_SIZE = 25;

    function setL1PracticeMode(mode) {
      l1PracticeMode = mode;
      const sBtn = document.getElementById('l1ModeSolved');
      const uBtn = document.getElementById('l1ModeUnsolved');
      if (sBtn) sBtn.classList.toggle('active', mode === 'study');
      if (uBtn) uBtn.classList.toggle('active', mode === 'unsolved');
      renderL1Question();
    }

    function revealUnsolvedL1(qId) {
      const box = document.getElementById('expl-' + qId);
      if (box) box.style.display = 'block';
    }

    function isNumericalQuestion(q) {
      const text = (q.question + ' ' + (q.explanation || '')).toLowerCase();
      return text.includes('$$') || text.includes('$$\\') ||
             /\\(frac|sum|times|approx|pm|le|ge|sigma|mu|beta|alpha|rho)\b/.test(text) ||
             /\b(calculate|computed|compute|equals|equal to|closest to|approximate|percentage|basis points|ratio|variance|standard deviation|duration|sharpe|treynor|holding period|npv|irr|wacc|ear|yield|forward price|cap rate|ffo|affo|dpi|tvpi|delta|elasticity|multiplier)\b/i.test(q.question);
    }

    function setL1TypeFilter(type) {
      l1TypeFilter = type;
      document.getElementById('l1TypeAll').classList.toggle('active', type === 'ALL');
      document.getElementById('l1TypeNum').classList.toggle('active', type === 'NUMERICAL');
      document.getElementById('l1TypeTheory').classList.toggle('active', type === 'THEORY');
      filterL1Questions();
    }

    function setL2TypeFilter(type) {
      l2TypeFilter = type;
      document.getElementById('l2TypeAll').classList.toggle('active', type === 'ALL');
      document.getElementById('l2TypeNum').classList.toggle('active', type === 'NUMERICAL');
      document.getElementById('l2TypeTheory').classList.toggle('active', type === 'THEORY');
      loadL2Vignette();
    }

    function filterL1Questions() {
      const subj = document.getElementById('l1SubjectSelect').value;
      const topic = document.getElementById('l1TopicSelect').value;
      const search = (document.getElementById('l1SearchInput').value || '').toLowerCase().trim();

      currentL1List = questionBank.filter(q => {
        if (q.level !== 1) return false;
        if (subj !== 'ALL' && q.subject !== subj) return false;
        if (topic !== 'ALL' && (q.module_title !== topic && q.topic !== topic)) return false;
        if (l1TypeFilter === 'NUMERICAL' && !isNumericalQuestion(q)) return false;
        if (l1TypeFilter === 'THEORY' && isNumericalQuestion(q)) return false;
        if (search) {
          const full = (q.id + ' ' + q.question + ' ' + (q.los || '') + ' ' + (q.module_title || '')).toLowerCase();
          if (!full.includes(search)) return false;
        }
        return true;
      });

      l1CurrentIdx = 0;
      l1ListPage = 0;
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

    function toggleL1ViewMode() {
      l1ViewMode = (l1ViewMode === 'card') ? 'list' : 'card';
      l1ListPage = 0;
      document.getElementById('l1ViewModeBtn').innerText = (l1ViewMode === 'card') ? '📜 Switch to Paginated List View' : '🗂️ Switch to Single Card View';
      renderL1Question();
    }

    function setL1ListPage(p) {
      l1ListPage = p;
      renderL1Question();
      const c = document.getElementById('l1QuestionContainer');
      if (c) c.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    function renderL1SingleCard(q, idx, total) {
      const isAnswered = answeredQuestions[q.id];
      const subjClass = getSubjectBadgeClass(q.subject);
      const showFeedback = isAnswered && l1PracticeMode === 'study';

      let optsHtml = '';
      for (const [key, val] of Object.entries(q.options)) {
        let btnClass = 'option-btn';
        if (isAnswered) {
          if (showFeedback) {
            if (key === q.answer) btnClass += ' correct';
            else if (key === isAnswered.selected) btnClass += ' incorrect';
          } else if (key === isAnswered.selected) {
            btnClass += ' active';
            btnClass += '" style="border-color: var(--accent-blue); background: rgba(59,130,246,0.12);';
          }
        }
        optsHtml += `
          <button class="${btnClass}" ${isAnswered ? 'disabled' : ''} onclick="submitL1Answer('${q.id}', '${key}')">
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

      const revealBtn = (l1PracticeMode === 'unsolved')
        ? `<div style="margin-top:10px;"><button type="button" class="btn btn-secondary" style="font-size:12px; padding:5px 12px;" onclick="revealUnsolvedL1('${q.id}')">👁️ Reveal Answer (${q.answer}) &amp; Solution</button></div>`
        : '';

      return `
        <div class="question-box">
          <div class="question-header">
            <div style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;">
              <span class="question-id-badge">${q.id}</span>
              <span class="subject-badge ${subjClass}">${q.subject}</span>
              <span style="font-size: 12px; color: var(--text-secondary);">${q.module_title || q.topic}</span>
            </div>
            <span class="question-los">${q.los ? 'LOS: ' + q.los : ''}</span>
          </div>
          <div class="question-text">${q.question}</div>
          <div class="options-container">${optsHtml}</div>
          ${revealBtn}
          <div id="expl-${q.id}" class="explanation-box" style="${showFeedback ? 'display: block;' : ''}">
            <div class="explanation-title">Verified Answer: Option ${q.answer} — Detailed Solution &amp; Derivation:</div>
            <div style="line-height: 1.7; font-size: 13.5px;">${q.explanation}</div>
            ${distractorHtml}
          </div>
        </div>
      `;
    }

    function renderL1Question() {
      const container = document.getElementById('l1QuestionContainer');
      const countBadge = document.getElementById('l1CountBadge');

      if (currentL1List.length === 0) {
        container.innerHTML = '<div class="card"><p style="color: var(--text-secondary);">No questions matching current filter criteria.</p></div>';
        countBadge.innerText = 'Showing 0 questions';
        return;
      }

      if (l1ViewMode === 'card') {
        const q = currentL1List[l1CurrentIdx];
        countBadge.innerText = `Showing Question ${l1CurrentIdx + 1} of ${currentL1List.length}`;
        container.innerHTML = renderL1SingleCard(q, l1CurrentIdx, currentL1List.length);
      } else {
        const totalPages = Math.max(1, Math.ceil(currentL1List.length / L1_PAGE_SIZE));
        if (l1ListPage >= totalPages) l1ListPage = totalPages - 1;
        const start = l1ListPage * L1_PAGE_SIZE;
        const slice = currentL1List.slice(start, start + L1_PAGE_SIZE);
        countBadge.innerText = `Showing ${start + 1}–${start + slice.length} of ${currentL1List.length} Questions (Page ${l1ListPage + 1} / ${totalPages})`;
        let listHtml = '';
        if (totalPages > 1) {
          listHtml += `<div class="card" style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px; padding:12px 16px;">
            <span style="font-size:12.5px; color:var(--text-secondary);">Paginated View (${L1_PAGE_SIZE} per page for fast rendering)</span>
            <div style="display:flex; gap:6px; flex-wrap:wrap;">
              <button class="filter-btn" ${l1ListPage===0?'disabled':''} onclick="setL1ListPage(${l1ListPage-1})">← Prev Page</button>
              <button class="filter-btn" ${l1ListPage>=totalPages-1?'disabled':''} onclick="setL1ListPage(${l1ListPage+1})">Next Page →</button>
            </div>
          </div>`;
        }
        slice.forEach((q, idx) => {
          listHtml += renderL1SingleCard(q, start + idx, currentL1List.length);
        });
        container.innerHTML = listHtml;
      }

      renderMath();
    }

    function submitL1Answer(qId, selectedKey) {
      const q = questionBank.find(item => item.id === qId);
      if (!q) return;

      const isCorrect = (selectedKey === q.answer);
      answeredQuestions[qId] = { selected: selectedKey, correct: isCorrect };

      totalAnswered = Object.keys(answeredQuestions).length;
      correctCount = Object.values(answeredQuestions).filter(a => a.correct).length;
      updateScoreBadge();

      renderL1Question();
    }

    // ==========================================
    // LEVEL 2 VIGNETTE ENGINE LOGIC
    // ==========================================
    function initL2Engine() {
      vignettesMap = {};
      questionBank.filter(q => q.level === 2).forEach(q => {
        const vid = q.global_vignette_id || q.vignette_id || 'V_MISC';
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

      populateL2VignetteSelect();
    }

    function populateL2VignetteSelect() {
      const subj = document.getElementById('l2SubjectSelect').value;
      const search = (document.getElementById('l2SearchInput').value || '').toLowerCase().trim();
      const select = document.getElementById('l2VignetteSelect');
      select.innerHTML = '';

      let matchingVids = Object.keys(vignettesMap).filter(vid => {
        const v = vignettesMap[vid];
        if (subj !== 'ALL' && v.subject !== subj) return false;
        if (search) {
          const full = (v.id + ' ' + v.title + ' ' + v.text).toLowerCase();
          if (!full.includes(search)) return false;
        }
        return true;
      });

      matchingVids.sort();

      matchingVids.forEach(vid => {
        const v = vignettesMap[vid];
        const opt = document.createElement('option');
        opt.value = vid;
        const shortSubj = getSubjectShortName(v.subject);
        opt.innerText = `[${shortSubj}] ${v.id}: ${v.title} (${v.questions.length} Qs)`;
        select.appendChild(opt);
      });

      if (matchingVids.length > 0) {
        currentL2VignetteId = matchingVids[0];
        select.value = currentL2VignetteId;
        loadL2Vignette();
      } else {
        document.getElementById('vignetteTextCard').innerHTML = '<p style="color: var(--text-secondary);">No vignettes match criteria.</p>';
        document.getElementById('vignetteQuestionsCard').innerHTML = '';
        document.getElementById('l2VignetteCounter').innerText = '0 of 0';
      }
    }

    function onL2SubjectChange() {
      populateL2VignetteSelect();
    }

    function onL2Search() {
      populateL2VignetteSelect();
    }

    function loadL2Vignette() {
      const vid = document.getElementById('l2VignetteSelect').value;
      currentL2VignetteId = vid;
      const v = vignettesMap[vid];
      if (!v) return;

      const allVids = Array.from(document.getElementById('l2VignetteSelect').options).map(o => o.value);
      const curIdx = allVids.indexOf(vid);
      document.getElementById('l2VignetteCounter').innerText = `Vignette ${curIdx + 1} of ${allVids.length}`;

      const subjClass = getSubjectBadgeClass(v.subject);

      document.getElementById('vignetteTextCard').innerHTML = `
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; flex-wrap: wrap; gap: 8px;">
          <div style="display: flex; gap: 8px; align-items: center;">
            <span class="question-id-badge">${v.id}</span>
            <span class="subject-badge ${subjClass}">${v.subject}</span>
          </div>
          <span style="font-size: 12px; color: var(--text-secondary);">${v.questions.length} Item-Set Questions</span>
        </div>
        <h3 style="font-size: 17px; margin-bottom: 14px; color: var(--accent-cyan); font-weight: 700;">${v.title}</h3>
        <div style="line-height: 1.75; font-size: 13.5px; white-space: pre-line; color: var(--text-primary);">${v.text}</div>
      `;

      let qHtml = '';
      v.questions.forEach((q, idx) => {
        const isNum = isNumericalQuestion(q);
        if (l2TypeFilter === 'NUMERICAL' && !isNum) return;
        if (l2TypeFilter === 'THEORY' && isNum) return;
        const isAnswered = answeredQuestions[q.id];
        let optsHtml = '';
        for (const [key, val] of Object.entries(q.options)) {
          let btnClass = 'option-btn';
          if (isAnswered) {
            if (key === q.answer) btnClass += ' correct';
            else if (key === isAnswered.selected) btnClass += ' incorrect';
          }
          optsHtml += `
            <button class="${btnClass}" ${isAnswered ? 'disabled' : ''} onclick="submitL2Answer('${q.id}', '${key}')">
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
              <span class="question-id-badge">Question ${idx + 1} of ${v.questions.length} (${q.id})</span>
              <span class="question-los">${q.los ? 'LOS: ' + q.los : ''}</span>
            </div>
            <div class="question-text" style="font-size: 14px;">${q.question}</div>
            <div class="options-container">${optsHtml}</div>
            <div id="expl-${q.id}" class="explanation-box" style="${isAnswered ? 'display: block;' : ''}">
              <div class="explanation-title">Solution & Step-by-Step Derivation:</div>
              <div style="line-height: 1.65; font-size: 13px;">${q.explanation}</div>
              ${distractorHtml}
            </div>
          </div>
        `;
      });

      document.getElementById('vignetteQuestionsCard').innerHTML = qHtml;
      renderMath();
    }

    function submitL2Answer(qId, selectedKey) {
      const q = questionBank.find(item => item.id === qId);
      if (!q) return;

      const isCorrect = (selectedKey === q.answer);
      answeredQuestions[qId] = { selected: selectedKey, correct: isCorrect };

      totalAnswered = Object.keys(answeredQuestions).length;
      correctCount = Object.values(answeredQuestions).filter(a => a.correct).length;
      updateScoreBadge();

      loadL2Vignette();
    }

    function nextL2Vignette() {
      const select = document.getElementById('l2VignetteSelect');
      if (select.selectedIndex < select.options.length - 1) {
        select.selectedIndex++;
        loadL2Vignette();
      }
    }

    function prevL2Vignette() {
      const select = document.getElementById('l2VignetteSelect');
      if (select.selectedIndex > 0) {
        select.selectedIndex--;
        loadL2Vignette();
      }
    }

    // ==========================================
    // SIMULATION 1: YIELD CURVE
    // ==========================================
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
        const slopeFactor = (i - 3.5) / 3.5;
        const humpf = 1.0 - Math.abs(i - 3.5) / 3.5;
        const shock = sBps + (tBps * slopeFactor) + (bBps * humpf);
        return parseFloat((r + shock).toFixed(2));
      });

      yieldChart.data.datasets[1].data = shocked;
      yieldChart.update();
    }

    // ==========================================
    // SIMULATION 2: BINOMIAL TREE
    // ==========================================
    function updateTreeSim() {
      const c = parseFloat(document.getElementById('treeCoupon').value);
      const sigma = parseFloat(document.getElementById('treeVol').value) / 100.0;
      const callP = parseFloat(document.getElementById('treeCall').value);

      document.getElementById('treeCouponVal').innerText = c.toFixed(2) + '%';
      document.getElementById('treeVolVal').innerText = (sigma * 100).toFixed(1) + '%';
      document.getElementById('treeCallVal').innerText = callP.toFixed(2) + ' USD';

      const r0 = 0.04;
      const r1_L = 0.045;
      const r1_U = r1_L * Math.exp(2 * sigma);
      const r2_LL = 0.048;
      const r2_LU = r2_LL * Math.exp(2 * sigma);
      const r2_UU = r2_LL * Math.exp(4 * sigma);

      const par = 100.0;
      const coup = (c / 100.0) * par;

      const v2_UU = Math.min((par + coup) / (1 + r2_UU), callP);
      const v2_LU = Math.min((par + coup) / (1 + r2_LU), callP);
      const v2_LL = Math.min((par + coup) / (1 + r2_LL), callP);

      const v1_U = Math.min((0.5 * (v2_UU + coup) + 0.5 * (v2_LU + coup)) / (1 + r1_U), callP);
      const v1_L = Math.min((0.5 * (v2_LU + coup) + 0.5 * (v2_LL + coup)) / (1 + r1_L), callP);

      const v0_callable = (0.5 * (v1_U + coup) + 0.5 * (v1_L + coup)) / (1 + r0);

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
      renderMath();
    }

    // ==========================================
    // SIMULATION 3: EQUITY DDM & DUPONT
    // ==========================================
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
          scales: { y: { beginAtZero: true, grid: { color: '#21262d' } } },
          plugins: { legend: { display: false } }
        }
      });
      updateEquitySim();
    }

    function updateEquitySim() {
      const d0 = parseFloat(document.getElementById('d0Input').value);
      const gs = parseFloat(document.getElementById('gsInput').value) / 100.0;
      const n = parseInt(document.getElementById('nInput').value);
      const gl = parseFloat(document.getElementById('glInput').value) / 100.0;
      const r = parseFloat(document.getElementById('rInput').value) / 100.0;

      document.getElementById('d0Val').innerText = d0.toFixed(2) + ' USD';
      document.getElementById('gsVal').innerText = (gs * 100).toFixed(1) + '%';
      document.getElementById('nVal').innerText = n + ' Years';
      document.getElementById('glVal').innerText = (gl * 100).toFixed(1) + '%';
      document.getElementById('rVal').innerText = (r * 100).toFixed(2) + '%';

      if (r <= gl) {
        document.getElementById('ddmResult').innerHTML = '<span style="color: var(--accent-rose); font-weight: 700;">Error: Required Return ($r$) must exceed Long-term Growth ($g_L$)</span>';
        return;
      }

      let pvDividends = 0;
      let curD = d0;
      for (let t = 1; t <= n; t++) {
        curD *= (1 + gs);
        pvDividends += curD / Math.pow(1 + r, t);
      }

      const terminalDiv = curD * (1 + gl);
      const terminalPrice = terminalDiv / (r - gl);
      const pvTerminal = terminalPrice / Math.pow(1 + r, n);
      const intrinsicValue = pvDividends + pvTerminal;

      document.getElementById('ddmResult').innerHTML = `
        <div><strong>PV of High-Growth Dividends:</strong> ${pvDividends.toFixed(2)} USD</div>
        <div><strong>Terminal Value ($P_{n}$):</strong> ${terminalPrice.toFixed(2)} USD (PV: ${pvTerminal.toFixed(2)} USD)</div>
        <div style="font-size: 16px; font-weight: 700; color: var(--accent-emerald); margin-top: 6px;">
          Intrinsic Value ($V_0$): ${intrinsicValue.toFixed(2)} USD
        </div>
      `;

      const taxBurden = 0.78;
      const intBurden = 0.88;
      const ebitMargin = 0.20;
      const assetTurnover = 1.15;
      const leverage = 1.65;
      const roe = taxBurden * intBurden * ebitMargin * assetTurnover * leverage;

      document.getElementById('dupontResult').innerHTML = `
        <strong>Calculated ROE:</strong> ${(roe * 100).toFixed(2)}% | 
        <em>Formula:</em> $\\text{Tax Burden} \\times \\text{Int Burden} \\times \\text{EBIT Margin} \\times \\text{Turnover} \\times \\text{Leverage}$
      `;
      renderMath();
    }

    // ==========================================
    // SIMULATION 4: KEY RATE DURATION
    // ==========================================
    let krdChart = null;
    function initDurationSim() {
      const ctx = document.getElementById('krdChart').getContext('2d');
      krdChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ['2Y', '5Y', '10Y', '30Y'],
          datasets: [{
            label: 'Key Rate Duration (Years)',
            data: [0.5, 1.2, 7.8, 0.4],
            backgroundColor: ['#58a6ff', '#39c5cf', '#3fb950', '#bc8cff']
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: { title: { display: true, text: 'Key Rate Duration', color: '#8b949e' }, grid: { color: '#21262d' } },
            x: { grid: { color: '#21262d' } }
          }
        }
      });
      updateDurationSim();
    }

    function updateDurationSim() {
      const port = document.getElementById('portfolioSelect').value;
      const s2 = parseFloat(document.getElementById('s2').value);
      const s10 = parseFloat(document.getElementById('s10').value);
      const s30 = parseFloat(document.getElementById('s30').value);

      document.getElementById('s2Val').innerText = (s2 > 0 ? '+' : '') + s2 + ' bps';
      document.getElementById('s10Val').innerText = (s10 > 0 ? '+' : '') + s10 + ' bps';
      document.getElementById('s30Val').innerText = (s30 > 0 ? '+' : '') + s30 + ' bps';

      let krds = [];
      if (port === 'bullet') krds = [0.4, 0.8, 8.2, 0.6];
      else if (port === 'barbell') krds = [4.8, 0.2, 0.4, 4.6];
      else krds = [2.2, 2.5, 2.8, 2.5];

      if (krdChart) {
        krdChart.data.datasets[0].data = krds;
        krdChart.update();
      }

      const s5 = (s2 + s10) / 2.0;
      const deltaP = -1 * (
        (krds[0] * (s2 / 10000.0)) +
        (krds[1] * (s5 / 10000.0)) +
        (krds[2] * (s10 / 10000.0)) +
        (krds[3] * (s30 / 10000.0))
      ) * 100;

      const effDur = krds.reduce((a, b) => a + b, 0);

      document.getElementById('krdResults').innerHTML = `
        <div><strong>Effective Duration:</strong> ${effDur.toFixed(2)} Years</div>
        <div><strong>Estimated Portfolio Price Impact:</strong> 
          <span style="font-weight: 700; color: ${deltaP >= 0 ? 'var(--accent-emerald)' : 'var(--accent-rose)'};">
            ${(deltaP >= 0 ? '+' : '') + deltaP.toFixed(3)}%
          </span>
        </div>
        <div style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">
          Formula: $\\%\\Delta P \\approx -\\sum (KRD_k \\times \\Delta y_k)$
        </div>
      `;
    }

    // ==========================================
    // SIMULATION 5: FRN PRICING
    // ==========================================
    function updateFrnSim() {
      const mrr = parseFloat(document.getElementById('mrrInput').value) / 100.0;
      const qm = parseFloat(document.getElementById('qmInput').value) / 10000.0;
      const dm = parseFloat(document.getElementById('dmInput').value) / 10000.0;
      const m = parseInt(document.getElementById('frnFreq').value);
      const nYears = parseInt(document.getElementById('frnTenor').value);

      document.getElementById('mrrVal').innerText = (mrr * 100).toFixed(2) + '%';
      document.getElementById('qmVal').innerText = (qm * 10000).toFixed(0) + ' bps';
      document.getElementById('dmVal').innerText = (dm * 10000).toFixed(0) + ' bps';
      document.getElementById('frnTenorVal').innerText = nYears + ' Years';

      const N = nYears * m;
      const couponPerPeriod = ((mrr + qm) / m) * 100.0;
      const discountRatePerPeriod = (mrr + dm) / m;

      let pv = 0;
      for (let t = 1; t <= N; t++) {
        pv += couponPerPeriod / Math.pow(1 + discountRatePerPeriod, t);
      }
      pv += 100.0 / Math.pow(1 + discountRatePerPeriod, N);

      let status = '';
      if (Math.abs(qm - dm) < 0.00001) status = '<span style="color: var(--accent-emerald); font-weight: 700;">Trading Exactly at Par (100 USD)</span>';
      else if (qm > dm) status = '<span style="color: var(--accent-blue); font-weight: 700;">Trading at a Premium (&gt; 100 USD)</span>';
      else status = '<span style="color: var(--accent-rose); font-weight: 700;">Trading at a Discount (&lt; 100 USD)</span>';

      document.getElementById('frnResults').innerHTML = `
        <div><strong>Clean FRN Price:</strong> ${pv.toFixed(3)} USD</div>
        <div><strong>Pricing Status:</strong> ${status}</div>
        <div style="font-size: 11.5px; color: var(--text-secondary); margin-top: 6px;">
          *If QM &gt; DM, coupon cash flows exceed investor required margin $\\rightarrow$ Premium bond.<br/>
          *If QM &lt; DM, coupon cash flows fall short of required margin $\\rightarrow$ Discount bond.
        </div>
      `;
    }

    // ==========================================
    // SIMULATION 6: RESIDUAL INCOME DECAY
    // ==========================================
    let riChart = null;
    function initRiSim() {
      const ctx = document.getElementById('riChart').getContext('2d');
      riChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: ['Year 0', 'Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5'],
          datasets: [{
            label: 'Forecast Residual Income (USD)',
            data: [],
            borderColor: '#3fb950',
            backgroundColor: 'rgba(63, 185, 80, 0.1)',
            fill: true,
            tension: 0.2
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: { title: { display: true, text: 'RI ($)', color: '#8b949e' }, grid: { color: '#21262d' } },
            x: { grid: { color: '#21262d' } }
          }
        }
      });
      updateRiSim();
    }

    function updateRiSim() {
      const omega = parseFloat(document.getElementById('omegaInput').value);
      const b0 = parseFloat(document.getElementById('b0Input').value);
      const roe = parseFloat(document.getElementById('roeInput').value) / 100.0;
      const r = parseFloat(document.getElementById('costEqInput').value) / 100.0;

      document.getElementById('omegaVal').innerText = omega.toFixed(2);
      document.getElementById('b0Val').innerText = b0.toFixed(2) + ' USD';
      document.getElementById('roeVal').innerText = (roe * 100).toFixed(1) + '%';
      document.getElementById('costEqVal').innerText = (r * 100).toFixed(1) + '%';

      const ri1 = b0 * (roe - r);
      const riSeries = [0];
      for (let t = 1; t <= 5; t++) {
        riSeries.push(parseFloat((ri1 * Math.pow(omega, t - 1)).toFixed(2)));
      }

      if (riChart) {
        riChart.data.datasets[0].data = riSeries;
        riChart.update();
      }

      const continuingRiPV = ri1 / (1 + r - omega);
      const intrinsicValue = b0 + continuingRiPV;

      document.getElementById('riResultBox').innerHTML = `
        <div><strong>Initial Residual Income ($RI_1$):</strong> ${ri1.toFixed(2)} USD</div>
        <div><strong>PV of Continuing Residual Income:</strong> ${continuingRiPV.toFixed(2)} USD</div>
        <div style="font-size: 15px; font-weight: 700; color: var(--accent-emerald); margin-top: 4px;">
          Intrinsic Value ($V_0$): ${intrinsicValue.toFixed(2)} USD
        </div>
      `;
      renderMath();
    }

    // ==========================================
    // SIMULATION 7: WATERFALL
    // ==========================================
    let waterfallChart = null;
    function initWaterfallSim() {
      const ctx = document.getElementById('waterfallChart').getContext('2d');
      waterfallChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ['EBITDA', 'Taxes', 'CapEx', '$\\Delta$ WC', 'FCFF', 'After-tax Int', 'Net Borrowing', 'FCFE'],
          datasets: [{
            label: 'Cash Flow Component (M USD)',
            data: [],
            backgroundColor: ['#58a6ff', '#f85149', '#f85149', '#f85149', '#39c5cf', '#f85149', '#3fb950', '#3fb950']
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: { y: { grid: { color: '#21262d' } } },
          plugins: { legend: { display: false } }
        }
      });
      updateWaterfallSim();
    }

    function updateWaterfallSim() {
      const ebitda = parseFloat(document.getElementById('ebitdaInput').value);
      const da = parseFloat(document.getElementById('daInput').value);
      const fcinv = parseFloat(document.getElementById('fcinvInput').value);
      const wcinv = parseFloat(document.getElementById('wcinvInput').value);
      const intExp = parseFloat(document.getElementById('intInput').value);
      const netBorrowing = parseFloat(document.getElementById('nbInput').value);
      const taxRate = 0.25;

      document.getElementById('ebitdaVal').innerText = ebitda + ' M USD';
      document.getElementById('daVal').innerText = da + ' M USD';
      document.getElementById('fcinvVal').innerText = fcinv + ' M USD';
      document.getElementById('wcinvVal').innerText = wcinv + ' M USD';
      document.getElementById('intVal').innerText = intExp + ' M USD';
      document.getElementById('nbVal').innerText = (netBorrowing >= 0 ? '+' : '') + netBorrowing + ' M USD';

      const ebit = ebitda - da;
      const taxPaid = ebit * taxRate;
      const fcff = (ebit * (1 - taxRate)) + da - fcinv - wcinv;
      const afterTaxInt = intExp * (1 - taxRate);
      const fcfe = fcff - afterTaxInt + netBorrowing;

      if (waterfallChart) {
        waterfallChart.data.datasets[0].data = [ebitda, -taxPaid, -fcinv, -wcinv, fcff, -afterTaxInt, netBorrowing, fcfe];
        waterfallChart.update();
      }

      document.getElementById('waterfallOutput').innerHTML = `
        <div><strong>EBITDA:</strong> ${ebitda} M USD $\\rightarrow$ <strong>EBIT:</strong> ${ebit} M USD</div>
        <div style="color: var(--accent-cyan); font-weight: 700;">FCFF: ${fcff.toFixed(1)} M USD</div>
        <div>Less: After-tax Interest: -${afterTaxInt.toFixed(1)} M USD | Plus: Net Borrowing: ${netBorrowing >= 0 ? '+' : ''}${netBorrowing} M USD</div>
        <div style="color: var(--accent-emerald); font-weight: 700; font-size: 15px; margin-top: 4px;">FCFE: ${fcfe.toFixed(1)} M USD</div>
      `;
    }

    // ==========================================
    // SIMULATION 8: FX TRANSLATION
    // ==========================================
    function updateTranslationSim() {
      const nma = parseFloat(document.getElementById('fxNma').value);
      const nnma = parseFloat(document.getElementById('fxNnma').value);
      const fx = parseFloat(document.getElementById('fxChange').value);

      document.getElementById('fxNmaVal').innerText = (nma >= 0 ? '+' : '') + nma + ' M LC';
      document.getElementById('fxNnmaVal').innerText = '+' + nnma + ' M LC';
      document.getElementById('fxChangeVal').innerText = (fx >= 0 ? '+' : '') + fx + '% (' + (fx >= 0 ? 'Appreciation' : 'Depreciation') + ')';

      const netBalanceSheetExposureCurrent = nma + nnma;
      const netBalanceSheetExposureTemporal = nma;

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
                ${(currentGainLoss >= 0 ? '+' : '') + currentGainLoss.toFixed(1)} M (OCI / CTA)
              </td>
              <td style="color: ${temporalGainLoss >= 0 ? 'var(--accent-emerald)' : 'var(--accent-rose)'}; font-weight: 700;">
                ${(temporalGainLoss >= 0 ? '+' : '') + temporalGainLoss.toFixed(1)} M (Income Statement)
              </td>
            </tr>
          </tbody>
        </table>
        <div style="font-size: 11px; color: var(--text-secondary); line-height: 1.5;">
          *Current Rate: Translation accumulates in equity OCI (CTA). Temporal: Monetary volatility flows into reported Net Income.
        </div>
      `;
    }

    // ==========================================
    // SIMULATION 9: MBS PREPAYMENT
    // ==========================================
    let prepaymentChart = null;
    function initPrepaymentSim() {
      const ctx = document.getElementById('prepaymentChart').getContext('2d');
      prepaymentChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: Array.from({length: 30}, (_, i) => 'M' + (i + 1)),
          datasets: [
            { label: 'CPR (%)', data: [], borderColor: '#39c5cf', backgroundColor: 'rgba(57, 197, 207, 0.1)', fill: true, tension: 0.3 },
            { label: 'SMM (%)', data: [], borderColor: '#f85149', backgroundColor: 'transparent', borderDash: [5, 5], tension: 0.3 }
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
        <div style="font-weight: 700; color: var(--accent-blue); font-size: 13.5px;">Month ${mSel} Metrics (${psa}% PSA)</div>
        <div><strong>Conditional Prepayment Rate (CPR):</strong> ${(curCpr * 100).toFixed(2)}% annualized</div>
        <div><strong>Single Monthly Mortality (SMM):</strong> ${(curSmm * 100).toFixed(3)}% per month</div>
        <div style="margin-top: 6px; font-size: 12px; line-height: 1.5; border-top: 1px solid var(--border-color); padding-top: 6px;">
          ${riskType}
        </div>
      `;
      renderMath();
    }

    // ==========================================
    // CURRICULUM REFERENCE NOTES CHARTS (10 CHARTS)
    // ==========================================
    // ==========================================
    // SIMULATION 10: MARKOWITZ MEAN-VARIANCE FRONTIER & CAL
    // ==========================================
    let frontierChart = null;

    function initFrontierSim() {
      const ctx = document.getElementById('frontierChart');
      if (!ctx) return;
      frontierChart = new Chart(ctx.getContext('2d'), {
        type: 'scatter',
        data: {
          datasets: [
            {
              label: 'Risky Investment Frontier',
              data: [],
              showLine: true,
              borderColor: '#58a6ff',
              borderWidth: 2.5,
              pointRadius: 0,
              fill: false
            },
            {
              label: 'Capital Allocation Line (CAL)',
              data: [],
              showLine: true,
              borderColor: '#3fb950',
              borderWidth: 2,
              borderDash: [5, 4],
              pointRadius: 0,
              fill: false
            },
            {
              label: 'Optimal Risky Tangency (P*)',
              data: [],
              backgroundColor: '#f85149',
              borderColor: '#ffffff',
              borderWidth: 2,
              pointRadius: 6,
              pointHoverRadius: 8
            },
            {
              label: 'Global Min Variance (GMV)',
              data: [],
              backgroundColor: '#d29922',
              borderColor: '#ffffff',
              borderWidth: 2,
              pointRadius: 6,
              pointHoverRadius: 8
            },
            {
              label: 'Optimal Investor Allocation (C*)',
              data: [],
              backgroundColor: '#bc8cff',
              borderColor: '#ffffff',
              borderWidth: 2,
              pointRadius: 7,
              pointHoverRadius: 9
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: {
              title: { display: true, text: 'Portfolio Volatility σ (%)', color: '#8b949e' },
              grid: { color: '#21262d' }
            },
            y: {
              title: { display: true, text: 'Expected Return E(R) (%)', color: '#8b949e' },
              grid: { color: '#21262d' }
            }
          },
          plugins: {
            legend: { position: 'bottom', labels: { color: '#8b949e', boxWidth: 10, font: { size: 10 } } }
          }
        }
      });
      updateFrontierSim();
    }

    function updateFrontierSim() {
      const r1 = parseFloat(document.getElementById('sim10R1').value) / 100.0;
      const s1 = parseFloat(document.getElementById('sim10Sig1').value) / 100.0;
      const r2 = parseFloat(document.getElementById('sim10R2').value) / 100.0;
      const s2 = parseFloat(document.getElementById('sim10Sig2').value) / 100.0;
      const rho = parseFloat(document.getElementById('sim10Rho').value) / 100.0;
      const rf = parseFloat(document.getElementById('sim10Rf').value) / 100.0;
      const A = parseFloat(document.getElementById('sim10A').value);

      document.getElementById('valSim10R1').innerText = (r1 * 100).toFixed(1) + '%';
      document.getElementById('valSim10Sig1').innerText = (s1 * 100).toFixed(1) + '%';
      document.getElementById('valSim10R2').innerText = (r2 * 100).toFixed(1) + '%';
      document.getElementById('valSim10Sig2').innerText = (s2 * 100).toFixed(1) + '%';
      document.getElementById('valSim10Rho').innerText = rho.toFixed(2);
      document.getElementById('valSim10Rf').innerText = (rf * 100).toFixed(2) + '%';
      document.getElementById('valSim10A').innerText = A.toFixed(1);

      // 1. GMV weight
      const denomGmv = (s1 * s1) + (s2 * s2) - (2 * rho * s1 * s2);
      const w1Gmv = denomGmv !== 0 ? ((s2 * s2) - (rho * s1 * s2)) / denomGmv : 0.5;
      const rGmv = (w1Gmv * r1) + ((1 - w1Gmv) * r2);
      const varGmv = Math.max(0, (w1Gmv * w1Gmv * s1 * s1) + ((1 - w1Gmv) * (1 - w1Gmv) * s2 * s2) + (2 * w1Gmv * (1 - w1Gmv) * rho * s1 * s2));
      const sGmv = Math.sqrt(varGmv);

      // 2. Tangency portfolio weight
      const er1 = r1 - rf;
      const er2 = r2 - rf;
      const numTang = (er1 * s2 * s2) - (er2 * rho * s1 * s2);
      const denomTang = (er1 * s2 * s2) + (er2 * s1 * s1) - ((er1 + er2) * rho * s1 * s2);
      const w1Tang = denomTang !== 0 ? numTang / denomTang : 0.5;
      const w2Tang = 1.0 - w1Tang;
      const rTang = (w1Tang * r1) + (w2Tang * r2);
      const varTang = Math.max(0, (w1Tang * w1Tang * s1 * s1) + (w2Tang * w2Tang * s2 * s2) + (2 * w1Tang * w2Tang * rho * s1 * s2));
      const sTang = Math.sqrt(varTang);
      const sharpeTang = sTang > 0 ? (rTang - rf) / sTang : 0;

      // 3. Optimal investor allocation y* on CAL
      const yOpt = (A * sTang * sTang) > 0 ? (rTang - rf) / (A * sTang * sTang) : 1.0;
      const rOpt = rf + yOpt * (rTang - rf);
      const sOpt = yOpt * sTang;
      const utilityOpt = rOpt - (0.5 * A * sOpt * sOpt);

      // Frontier curve points
      const frontierPts = [];
      for (let w = -0.3; w <= 1.3; w += 0.04) {
        const rp = (w * r1) + ((1 - w) * r2);
        const vp = Math.max(0, (w * w * s1 * s1) + ((1 - w) * (1 - w) * s2 * s2) + (2 * w * (1 - w) * rho * s1 * s2));
        frontierPts.push({ x: +(Math.sqrt(vp) * 100).toFixed(2), y: +(rp * 100).toFixed(2) });
      }

      // CAL line points
      const calPts = [
        { x: 0, y: +(rf * 100).toFixed(2) },
        { x: +(sTang * 100).toFixed(2), y: +(rTang * 100).toFixed(2) },
        { x: +(Math.max(sTang * 1.5, sOpt * 1.2) * 100).toFixed(2), y: +((rf + Math.max(sTang * 1.5, sOpt * 1.2) * sharpeTang) * 100).toFixed(2) }
      ];

      if (frontierChart) {
        frontierChart.data.datasets[0].data = frontierPts;
        frontierChart.data.datasets[1].data = calPts;
        frontierChart.data.datasets[2].data = [{ x: +(sTang * 100).toFixed(2), y: +(rTang * 100).toFixed(2) }];
        frontierChart.data.datasets[3].data = [{ x: +(sGmv * 100).toFixed(2), y: +(rGmv * 100).toFixed(2) }];
        frontierChart.data.datasets[4].data = [{ x: +(sOpt * 100).toFixed(2), y: +(rOpt * 100).toFixed(2) }];
        frontierChart.update();
      }

      document.getElementById('frontierMetricsBox').innerHTML = `
        <div style="font-weight: 700; color: var(--accent-blue); margin-bottom: 6px;">Optimal Portfolio Solution Summary</div>
        <div class="grid-2" style="font-size: 12px; gap: 8px;">
          <div><strong>Tangency Risky Portfolio (P*):</strong><br>
            • Weight Asset 1: ${(w1Tang * 100).toFixed(1)}% | Weight Asset 2: ${(w2Tang * 100).toFixed(1)}%<br>
            • E(R*): ${(rTang * 100).toFixed(2)}% | σ*: ${(sTang * 100).toFixed(2)}%<br>
            • Max Sharpe Ratio: <strong>${sharpeTang.toFixed(3)}</strong>
          </div>
          <div><strong>Investor Optimum on CAL (A = ${A.toFixed(1)}):</strong><br>
            • Allocation to Risky: ${(yOpt * 100).toFixed(1)}% | Risk-Free: ${((1 - yOpt) * 100).toFixed(1)}%<br>
            • Overall E(Rc): ${(rOpt * 100).toFixed(2)}% | σc: ${(sOpt * 100).toFixed(2)}%<br>
            • Expected Utility U: <strong>${(utilityOpt * 100).toFixed(2)}%</strong>
          </div>
        </div>
      `;
      renderMath();
    }

    // ==========================================
    // SIMULATION 11: FUNDAMENTAL LAW OF ACTIVE MGMT
    // ==========================================
    let fundamentalLawChart = null;

    function initFundamentalLawSim() {
      const ctx = document.getElementById('fundamentalLawChart');
      if (!ctx) return;
      fundamentalLawChart = new Chart(ctx.getContext('2d'), {
        type: 'line',
        data: {
          labels: [10, 25, 50, 100, 200, 300, 500, 750, 1000],
          datasets: [
            {
              label: 'Unconstrained IR (TC = 1.0)',
              data: [],
              borderColor: '#39c5cf',
              borderWidth: 2,
              fill: false
            },
            {
              label: 'Constrained Realized IR',
              data: [],
              borderColor: '#f85149',
              borderWidth: 2.5,
              fill: false
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: { title: { display: true, text: 'Breadth (Number of Bets / Year)', color: '#8b949e' }, grid: { color: '#21262d' } },
            y: { title: { display: true, text: 'Information Ratio (IR)', color: '#8b949e' }, grid: { color: '#21262d' } }
          },
          plugins: { legend: { position: 'bottom', labels: { color: '#8b949e', boxWidth: 10 } } }
        }
      });
      updateFundamentalLawSim();
    }

    function updateFundamentalLawSim() {
      const ic = parseFloat(document.getElementById('sim11Ic').value) / 100.0;
      const br = parseFloat(document.getElementById('sim11Br').value);
      const tc = parseFloat(document.getElementById('sim11Tc').value) / 100.0;
      const sigmaA = parseFloat(document.getElementById('sim11SigmaA').value) / 1000.0;
      const srB = parseFloat(document.getElementById('sim11SrB').value) / 100.0;
      const sigmaB = 0.16;

      document.getElementById('valSim11Ic').innerText = ic.toFixed(3);
      document.getElementById('valSim11Br').innerText = Math.round(br) + ' bets';
      document.getElementById('valSim11Tc').innerText = tc.toFixed(2);
      document.getElementById('valSim11SigmaA').innerText = (sigmaA * 100).toFixed(1) + '%';
      document.getElementById('valSim11SrB').innerText = srB.toFixed(2);

      const irUnconstrained = ic * Math.sqrt(br);
      const irConstrained = tc * ic * Math.sqrt(br);
      const expectedAlpha = irConstrained * sigmaA;
      const optSigmaA = (srB > 0) ? (tc * (ic * Math.sqrt(br) / srB) * sigmaB) : 0;
      const srP = Math.sqrt((srB * srB) + (irConstrained * irConstrained));
      const srUnconstrained = Math.sqrt((srB * srB) + (irUnconstrained * irUnconstrained));
      const constraintLoss = srUnconstrained - srP;

      const breadths = [10, 25, 50, 100, 200, 300, 500, 750, 1000];
      const unconstrainedData = breadths.map(b => +(ic * Math.sqrt(b)).toFixed(3));
      const constrainedData = breadths.map(b => +(tc * ic * Math.sqrt(b)).toFixed(3));

      if (fundamentalLawChart) {
        fundamentalLawChart.data.datasets[0].data = unconstrainedData;
        fundamentalLawChart.data.datasets[1].data = constrainedData;
        fundamentalLawChart.update();
      }

      document.getElementById('fundamentalLawMetricsBox').innerHTML = `
        <div style="font-weight: 700; color: var(--accent-emerald); margin-bottom: 6px;">Fundamental Law Active Attribution</div>
        <div class="grid-2" style="font-size: 12px; gap: 8px;">
          <div><strong>Active Skill & Return:</strong><br>
            • Unconstrained IR (TC=1.0): <strong>${irUnconstrained.toFixed(3)}</strong><br>
            • Constrained Realized IR: <strong>${irConstrained.toFixed(3)}</strong><br>
            • Expected Active Return (Alpha): <strong>${(expectedAlpha * 100).toFixed(2)}%</strong>
          </div>
          <div><strong>Total Performance & Risk Budget:</strong><br>
            • Optimal Active Risk (σA*): ${(optSigmaA * 100).toFixed(2)}%<br>
            • Total Portfolio Sharpe Ratio (SRP): <strong>${srP.toFixed(3)}</strong><br>
            • Drag from Constraints (ΔSR): <span style="color: var(--accent-rose); font-weight: 600;">-${constraintLoss.toFixed(3)}</span>
          </div>
        </div>
      `;
      renderMath();
    }

    // ==========================================
    // SIMULATION 12: DYNAMIC REBALANCING CORRIDORS
    // ==========================================
    let rebalanceChart = null;
    let cachedWalkPath = null;

    function initRebalancingSim() {
      const ctx = document.getElementById('rebalanceChart');
      if (!ctx) return;
      rebalanceChart = new Chart(ctx.getContext('2d'), {
        type: 'line',
        data: {
          labels: Array.from({length: 31}, (_, i) => 'Day ' + i),
          datasets: [
            { label: 'Upper Corridor', data: [], borderColor: '#f85149', borderDash: [6, 4], borderWidth: 1.5, pointRadius: 0, fill: false },
            { label: 'Target Weight (w*)', data: [], borderColor: '#3fb950', borderDash: [4, 4], borderWidth: 1.5, pointRadius: 0, fill: false },
            { label: 'Lower Corridor', data: [], borderColor: '#f85149', borderDash: [6, 4], borderWidth: 1.5, pointRadius: 0, fill: false },
            { label: 'Actual Weight Drift', data: [], borderColor: '#58a6ff', borderWidth: 2, pointRadius: 3, pointBackgroundColor: '#58a6ff', fill: false }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: { title: { display: true, text: 'Trading Day', color: '#8b949e' }, grid: { color: '#21262d' } },
            y: { title: { display: true, text: 'Portfolio Asset Weight (%)', color: '#8b949e' }, grid: { color: '#21262d' } }
          },
          plugins: { legend: { position: 'bottom', labels: { color: '#8b949e', boxWidth: 10 } } }
        }
      });
      simulateNewPath();
    }

    function simulateNewPath() {
      cachedWalkPath = null;
      updateRebalancingSim();
    }

    function updateRebalancingSim() {
      const wStar = parseFloat(document.getElementById('sim12Weight').value);
      const tc = parseFloat(document.getElementById('sim12Costs').value);
      const A = parseFloat(document.getElementById('sim12A').value);
      const vol = parseFloat(document.getElementById('sim12Vol').value);
      const rho = parseFloat(document.getElementById('sim12Corr').value) / 100.0;

      document.getElementById('valSim12Weight').innerText = wStar.toFixed(1) + '%';
      document.getElementById('valSim12Costs').innerText = Math.round(tc) + ' bps';
      document.getElementById('valSim12A').innerText = A.toFixed(1);
      document.getElementById('valSim12Vol').innerText = vol.toFixed(1) + '%';
      document.getElementById('valSim12Corr').innerText = rho.toFixed(2);

      // Optimal half-width deltaW calculation
      const deltaW = 5.0 * Math.sqrt(tc / 30.0) * Math.pow(4.0 / A, 0.6) * Math.pow(18.0 / vol, 0.8) * Math.pow((1.0 + rho) / 1.4, 0.5);
      const upperBand = wStar + deltaW;
      const lowerBand = wStar - deltaW;

      // Simulate 30-day drift
      if (!cachedWalkPath) {
        cachedWalkPath = [0];
        let cum = 0;
        for (let i = 1; i <= 30; i++) {
          const step = (Math.random() - 0.49) * (vol / 5.0);
          cum += step;
          cachedWalkPath.push(cum);
        }
      }

      const path = [];
      let currentVal = wStar;
      let rebalanceTriggers = 0;
      for (let i = 0; i <= 30; i++) {
        if (i > 0) {
          const dailyStep = cachedWalkPath[i] - cachedWalkPath[i - 1];
          currentVal += dailyStep;
          if (currentVal > upperBand || currentVal < lowerBand) {
            rebalanceTriggers++;
            currentVal = wStar; // Rebalance trigger resets weight
          }
        }
        path.push(+currentVal.toFixed(2));
      }

      if (rebalanceChart) {
        rebalanceChart.data.datasets[0].data = Array(31).fill(+upperBand.toFixed(2));
        rebalanceChart.data.datasets[1].data = Array(31).fill(+wStar.toFixed(2));
        rebalanceChart.data.datasets[2].data = Array(31).fill(+lowerBand.toFixed(2));
        rebalanceChart.data.datasets[3].data = path;
        rebalanceChart.update();
      }

      document.getElementById('rebalanceMetricsBox').innerHTML = `
        <div style="font-weight: 700; color: var(--accent-amber); margin-bottom: 6px;">Optimal Corridor Calibration</div>
        <div class="grid-2" style="font-size: 12px; gap: 8px;">
          <div><strong>Calibrated Tolerance Bounds:</strong><br>
            • Half-Width (Δw): <strong>±${deltaW.toFixed(2)}%</strong><br>
            • Upper Bound: <strong>${upperBand.toFixed(2)}%</strong> | Lower Bound: <strong>${lowerBand.toFixed(2)}%</strong><br>
            • Target Weight (w*): <strong>${wStar.toFixed(1)}%</strong>
          </div>
          <div><strong>Simulation Behavior (30 Days):</strong><br>
            • Rebalance Events Triggered: <strong>${rebalanceTriggers} times</strong><br>
            • Est. Cost Drag: ${(rebalanceTriggers * tc * (deltaW / 100.0)).toFixed(1)} bps<br>
            • Corridor Trade-off: Transaction costs widen bands; risk aversion & volatility narrow bands.
          </div>
        </div>
      `;
      renderMath();
    }

    // ==========================================
    // SIMULATIONS 13-16: BSM, QUANT MC, ALTS FEE WATERFALL, CORP WACC/MM
    // ==========================================
    let bsmChart = null, quantChart = null, altsChart = null, corpChart = null;

    function normCdfJS(x) {
      const a1 = 0.254829592, a2 = -0.284496736, a3 = 1.421413741, a4 = -1.453152027, a5 = 1.061405429, p = 0.3275911;
      const sign = x < 0 ? -1 : 1;
      const absX = Math.abs(x) / Math.sqrt(2);
      const t = 1.0 / (1.0 + p * absX);
      const y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * Math.exp(-absX * absX);
      return 0.5 * (1.0 + sign * y);
    }

    function normPdfJS(x) {
      return Math.exp(-0.5 * x * x) / Math.sqrt(2 * Math.PI);
    }

    function calcBsmCore(S, K, r, q, sigma, T) {
      const sqT = Math.sqrt(T);
      const d1 = (Math.log(S / K) + (r - q + 0.5 * sigma * sigma) * T) / (sigma * sqT);
      const d2 = d1 - sigma * sqT;
      const Nd1 = normCdfJS(d1), Nd2 = normCdfJS(d2);
      const Nmd1 = normCdfJS(-d1), Nmd2 = normCdfJS(-d2);
      const dq = Math.exp(-q * T), dr = Math.exp(-r * T);
      const call = S * dq * Nd1 - K * dr * Nd2;
      const put = K * dr * Nmd2 - S * dq * Nmd1;
      const deltaC = dq * Nd1, deltaP = dq * (Nd1 - 1);
      const gamma = (dq * normPdfJS(d1)) / (S * sigma * sqT);
      const vega = S * dq * normPdfJS(d1) * sqT * 0.01; // per 1% vol
      const thetaC = (-S * dq * normPdfJS(d1) * sigma / (2 * sqT) - r * K * dr * Nd2 + q * S * dq * Nd1) / 365;
      return { d1, d2, Nd1, Nd2, call, put, deltaC, deltaP, gamma, vega, thetaC };
    }

    function initBsmSim() {
      const el = document.getElementById('bsmChart');
      if (!el) return;
      bsmChart = new Chart(el.getContext('2d'), {
        type: 'line',
        data: {
          labels: [],
          datasets: [
            { label: 'BSM Call Value (t=0)', data: [], borderColor: '#3fb950', tension: 0.25, borderWidth: 2.5 },
            { label: 'Call Intrinsic Value (T=0)', data: [], borderColor: '#58a6ff', borderDash: [5, 5], tension: 0, borderWidth: 1.5 },
            { label: 'BSM Put Value (t=0)', data: [], borderColor: '#f85149', tension: 0.25, borderWidth: 2 }
          ]
        },
        options: {
          responsive: true, maintainAspectRatio: false,
          scales: { x: { title: { display: true, text: 'Spot Price (USD)', color: '#8b949e' }, grid: { color: '#21262d' } }, y: { title: { display: true, text: 'Option Premium (USD)', color: '#8b949e' }, grid: { color: '#21262d' } } },
          plugins: { legend: { position: 'bottom', labels: { color: '#8b949e' } } }
        }
      });
      updateBsmSim();
    }

    function updateBsmSim() {
      const S = parseFloat(document.getElementById('bsmS')?.value || 100);
      const K = parseFloat(document.getElementById('bsmK')?.value || 100);
      const vol = parseFloat(document.getElementById('bsmVol')?.value || 24) / 100;
      const T = parseFloat(document.getElementById('bsmT')?.value || 0.5);
      const r = parseFloat(document.getElementById('bsmR')?.value || 5) / 100;
      const q = parseFloat(document.getElementById('bsmQ')?.value || 2) / 100;
      if (document.getElementById('valBsmS')) document.getElementById('valBsmS').innerText = S + ' USD';
      if (document.getElementById('valBsmK')) document.getElementById('valBsmK').innerText = K + ' USD';
      if (document.getElementById('valBsmVol')) document.getElementById('valBsmVol').innerText = (vol * 100).toFixed(0) + '%';
      if (document.getElementById('valBsmT')) document.getElementById('valBsmT').innerText = T.toFixed(2) + ' yr';
      if (document.getElementById('valBsmRQ')) document.getElementById('valBsmRQ').innerText = `r=${(r*100).toFixed(1)}%, q=${(q*100).toFixed(1)}%`;

      const res = calcBsmCore(S, K, r, q, vol, T);
      if (bsmChart) {
        const spots = [], calls = [], intrs = [], puts = [];
        const lo = Math.max(20, Math.round(K * 0.6)), hi = Math.round(K * 1.4);
        for (let px = lo; px <= hi; px += Math.max(2, Math.round((hi - lo) / 20))) {
          spots.push(px);
          const v = calcBsmCore(px, K, r, q, vol, T);
          calls.push(v.call.toFixed(2));
          intrs.push(Math.max(0, px - K).toFixed(2));
          puts.push(v.put.toFixed(2));
        }
        bsmChart.data.labels = spots;
        bsmChart.data.datasets[0].data = calls;
        bsmChart.data.datasets[1].data = intrs;
        bsmChart.data.datasets[2].data = puts;
        bsmChart.update();
      }
      const box = document.getElementById('bsmMetricsBox');
      if (box) {
        box.innerHTML = `
          <div class="grid-2" style="gap:8px; font-size:12px;">
            <div><strong>BSM Valuation:</strong><br>
              • Call ($c_0$): <strong>${res.call.toFixed(2)} USD</strong> | Put ($p_0$): <strong>${res.put.toFixed(2)} USD</strong><br>
              • $d_1 = ${res.d1.toFixed(3)}$ ($N(d_1) = ${res.Nd1.toFixed(4)}$)<br>
              • $d_2 = ${res.d2.toFixed(3)}$ ($N(d_2) = ${res.Nd2.toFixed(4)}$)
            </div>
            <div><strong>Option Greeks:</strong><br>
              • Call $\\Delta = +${res.deltaC.toFixed(3)}$ | Put $\\Delta = ${res.deltaP.toFixed(3)}$<br>
              • Gamma $\\Gamma = ${res.gamma.toFixed(4)}$ | Vega $= ${res.vega.toFixed(3)}$ / 1% vol<br>
              • Daily Theta $\\Theta_c = ${res.thetaC.toFixed(3)}$ USD/day
            </div>
          </div>`;
        renderMath();
      }
    }

    let quantSeededPaths = [];
    function initQuantSim() {
      const el = document.getElementById('quantChart');
      if (!el) return;
      quantChart = new Chart(el.getContext('2d'), {
        type: 'line',
        data: { labels: ['M0','M1','M2','M3','M4','M5','M6','M7','M8','M9','M10','M11','M12'], datasets: [] },
        options: {
          responsive: true, maintainAspectRatio: false,
          scales: { x: { grid: { color: '#21262d' } }, y: { title: { display: true, text: 'Portfolio Index (Base 100)', color: '#8b949e' }, grid: { color: '#21262d' } } },
          plugins: { legend: { display: false } }
        }
      });
      updateQuantSim(true);
    }

    function randNorm() {
      let u = 0, v = 0;
      while (u === 0) u = Math.random();
      while (v === 0) v = Math.random();
      return Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
    }

    function updateQuantSim(regen = false) {
      const mu = parseFloat(document.getElementById('quantMu')?.value || 9) / 100;
      const sig = parseFloat(document.getElementById('quantSigma')?.value || 18) / 100;
      const rl = parseFloat(document.getElementById('quantRl')?.value || 2) / 100;
      const nObs = parseInt(document.getElementById('quantN')?.value || 36);
      if (document.getElementById('valQuantMu')) document.getElementById('valQuantMu').innerText = (mu * 100).toFixed(1) + '%';
      if (document.getElementById('valQuantSigma')) document.getElementById('valQuantSigma').innerText = (sig * 100).toFixed(1) + '%';
      if (document.getElementById('valQuantRl')) document.getElementById('valQuantRl').innerText = (rl * 100).toFixed(1) + '%';
      if (document.getElementById('valQuantN')) document.getElementById('valQuantN').innerText = nObs;

      if (regen || quantSeededPaths.length === 0) {
        quantSeededPaths = [];
        for (let p = 0; p < 12; p++) {
          const zs = [];
          for (let m = 0; m < 12; m++) zs.push(randNorm());
          quantSeededPaths.push(zs);
        }
      }

      const dt = 1 / 12;
      const datasets = quantSeededPaths.map((zs, idx) => {
        const pts = [100];
        let val = 100;
        for (let m = 0; m < 12; m++) {
          val = val * Math.exp((mu - 0.5 * sig * sig) * dt + sig * Math.sqrt(dt) * zs[m]);
          pts.push(val.toFixed(2));
        }
        return {
          label: 'Path ' + (idx + 1),
          data: pts,
          borderColor: idx === 0 ? '#58a6ff' : 'rgba(57, 197, 207, 0.45)',
          borderWidth: idx === 0 ? 2.5 : 1.3,
          pointRadius: 0,
          tension: 0.2
        };
      });
      if (quantChart) {
        quantChart.data.datasets = datasets;
        quantChart.update();
      }
      const sfr = (mu - rl) / sig;
      const probShortfall = normCdfJS(-sfr) * 100;
      const se = (sig / Math.sqrt(nObs));
      const tStat = (mu - rl) / se;
      const earCont = (Math.exp(mu) - 1) * 100;
      const box = document.getElementById('quantMetricsBox');
      if (box) {
        box.innerHTML = `
          <div class="grid-2" style="gap:8px; font-size:12px;">
            <div><strong>Safety-First &amp; EAR:</strong><br>
              • Roy's Safety-First Ratio: <strong>${sfr.toFixed(3)}</strong><br>
              • Normal Shortfall $P(R &lt; R_L)$: <strong>${probShortfall.toFixed(2)}%</strong><br>
              • Continuous EAR ($e^{\\mu}-1$): <strong>${earCont.toFixed(2)}%</strong>
            </div>
            <div><strong>Hypothesis Test ($H_0: \\mu \\le R_L$):</strong><br>
              • Standard Error ($\\sigma/\\sqrt{n}$): <strong>${(se*100).toFixed(2)}%</strong><br>
              • Sample $t$-Statistic: <strong>${tStat.toFixed(2)}</strong> ($df=${nObs-1}$)<br>
              • Decision ($\\alpha=5\\%$): <strong>${tStat > 1.69 ? 'Reject H0 (Significant Alpha)' : 'Fail to Reject H0'}</strong>
            </div>
          </div>`;
        renderMath();
      }
    }

    function initAltsSim() {
      const el = document.getElementById('altsChart');
      if (!el) return;
      altsChart = new Chart(el.getContext('2d'), {
        type: 'bar',
        data: {
          labels: ['Gross Ending NAV', 'Mgmt Fee (-)', 'Incentive Fee (-)', 'Net Ending LP NAV'],
          datasets: [{ label: 'M USD', data: [118, -2.36, -1.93, 113.71], backgroundColor: ['#58a6ff', '#f85149', '#d29922', '#3fb950'] }]
        },
        options: {
          responsive: true, maintainAspectRatio: false,
          scales: { y: { beginAtZero: false, min: 70, grid: { color: '#21262d' } }, x: { grid: { color: '#21262d' } } },
          plugins: { legend: { display: false } }
        }
      });
      updateAltsSim();
    }

    function updateAltsSim() {
      const gross = parseFloat(document.getElementById('altsGross')?.value || 18) / 100;
      const mgmtRate = parseFloat(document.getElementById('altsMgmt')?.value || 2) / 100;
      const incRate = parseFloat(document.getElementById('altsInc')?.value || 20) / 100;
      const hurdle = parseFloat(document.getElementById('altsHurdle')?.value || 6) / 100;
      const hwm = parseFloat(document.getElementById('altsHwm')?.value || 100);
      const hType = document.getElementById('altsHurdleType')?.value || 'hard';

      if (document.getElementById('valAltsGross')) document.getElementById('valAltsGross').innerText = (gross >= 0 ? '+' : '') + (gross * 100).toFixed(1) + '%';
      if (document.getElementById('valAltsFees')) document.getElementById('valAltsFees').innerText = `${(mgmtRate*100).toFixed(2)}% / ${(incRate*100).toFixed(0)}%`;
      if (document.getElementById('valAltsHurdle')) document.getElementById('valAltsHurdle').innerText = (hurdle * 100).toFixed(1) + '%';
      if (document.getElementById('valAltsHwm')) document.getElementById('valAltsHwm').innerText = hwm + 'M USD';

      const nav0 = 100;
      const navGross = nav0 * (1 + gross);
      const mgmtFee = navGross * mgmtRate;
      const navAfterMgmt = navGross - mgmtFee;
      const baseHwm = Math.max(nav0, hwm);
      const hurdleDollars = nav0 * hurdle;
      let incFee = 0;
      if (navAfterMgmt > baseHwm + hurdleDollars) {
        incFee = hType === 'hard'
          ? (navAfterMgmt - baseHwm - hurdleDollars) * incRate
          : (navAfterMgmt - baseHwm) * incRate;
      }
      const netNav = navAfterMgmt - incFee;
      const netRet = ((netNav - nav0) / nav0) * 100;
      const totalFees = mgmtFee + incFee;

      if (altsChart) {
        altsChart.data.datasets[0].data = [navGross.toFixed(2), mgmtFee.toFixed(2), incFee.toFixed(2), netNav.toFixed(2)];
        altsChart.update();
      }
      const box = document.getElementById('altsMetricsBox');
      if (box) {
        box.innerHTML = `
          <div class="grid-2" style="gap:8px; font-size:12px;">
            <div><strong>GP Fee Breakdown (100M Base):</strong><br>
              • Management Fee: <strong>${mgmtFee.toFixed(2)}M USD</strong><br>
              • Incentive Fee (${hType}): <strong>${incFee.toFixed(2)}M USD</strong><br>
              • Total GP Fee Drag: <strong>${totalFees.toFixed(2)}M USD</strong>
            </div>
            <div><strong>LP Net Outcomes:</strong><br>
              • Net Ending NAV: <strong>${netNav.toFixed(2)}M USD</strong><br>
              • Net LP Return: <strong>${netRet >= 0 ? '+' : ''}${netRet.toFixed(2)}%</strong><br>
              • Next-Yr HWM: <strong>${Math.max(baseHwm, netNav).toFixed(2)}M USD</strong>
            </div>
          </div>`;
      }
    }

    function initCorpSim() {
      const el = document.getElementById('corpChart');
      if (!el) return;
      corpChart = new Chart(el.getContext('2d'), {
        type: 'line',
        data: {
          labels: [],
          datasets: [
            { label: 'WACC (%)', data: [], borderColor: '#3fb950', tension: 0.3, borderWidth: 2.5, yAxisID: 'y' },
            { label: 'Levered Cost of Equity re (%)', data: [], borderColor: '#58a6ff', tension: 0.3, borderWidth: 2, yAxisID: 'y' }
          ]
        },
        options: {
          responsive: true, maintainAspectRatio: false,
          scales: {
            x: { title: { display: true, text: 'Debt-to-Equity Ratio (D/E)', color: '#8b949e' }, grid: { color: '#21262d' } },
            y: { title: { display: true, text: 'Cost of Capital (%)', color: '#8b949e' }, grid: { color: '#21262d' } }
          },
          plugins: { legend: { position: 'bottom', labels: { color: '#8b949e' } } }
        }
      });
      updateCorpSim();
    }

    function updateCorpSim() {
      const de = parseFloat(document.getElementById('corpDE')?.value || 0.6);
      const bu = parseFloat(document.getElementById('corpBu')?.value || 0.95);
      const tax = parseFloat(document.getElementById('corpTax')?.value || 25) / 100;
      const rdBase = parseFloat(document.getElementById('corpRd')?.value || 5.5) / 100;
      const dist = parseFloat(document.getElementById('corpDist')?.value || 1.5) / 100;

      if (document.getElementById('valCorpDE')) document.getElementById('valCorpDE').innerText = de.toFixed(2);
      if (document.getElementById('valCorpBu')) document.getElementById('valCorpBu').innerText = bu.toFixed(2);
      if (document.getElementById('valCorpTax')) document.getElementById('valCorpTax').innerText = (tax * 100).toFixed(0) + '%';
      if (document.getElementById('valCorpRd')) document.getElementById('valCorpRd').innerText = (rdBase * 100).toFixed(2) + '%';
      if (document.getElementById('valCorpDist')) document.getElementById('valCorpDist').innerText = (dist * 100).toFixed(2) + '%';

      const rf = 0.04, erp = 0.055;
      const calcAtDE = (x) => {
        const bL = bu * (1 + (1 - tax) * x);
        const re = rf + bL * erp + dist * 0.4 * (x * x);
        const rdEff = rdBase + dist * (x * x);
        const wd = x / (1 + x), we = 1 / (1 + x);
        const wacc = wd * rdEff * (1 - tax) + we * re;
        return { bL, re, rdEff, wacc };
      };

      const cur = calcAtDE(de);
      if (corpChart) {
        const lbls = [], waccs = [], res = [];
        for (let x = 0; x <= 2.501; x += 0.25) {
          lbls.push(x.toFixed(2));
          const c = calcAtDE(x);
          waccs.push((c.wacc * 100).toFixed(2));
          res.push((c.re * 100).toFixed(2));
        }
        corpChart.data.labels = lbls;
        corpChart.data.datasets[0].data = waccs;
        corpChart.data.datasets[1].data = res;
        corpChart.update();
      }
      const box = document.getElementById('corpMetricsBox');
      if (box) {
        box.innerHTML = `
          <div class="grid-2" style="gap:8px; font-size:12px;">
            <div><strong>Hamada &amp; Component Costs:</strong><br>
              • Relevered Beta ($\\beta_L$): <strong>${cur.bL.toFixed(3)}</strong><br>
              • Levered Cost of Equity ($r_e$): <strong>${(cur.re*100).toFixed(2)}%</strong><br>
              • After-Tax Cost of Debt: <strong>${(cur.rdEff*(1-tax)*100).toFixed(2)}%</strong>
            </div>
            <div><strong>Static Trade-Off WACC:</strong><br>
              • Blended WACC: <strong>${(cur.wacc*100).toFixed(2)}%</strong><br>
              • Weight Debt ($w_d$): <strong>${((de/(1+de))*100).toFixed(1)}%</strong><br>
              • Tax Shield Boost ($t \\cdot w_d$): <strong>${(tax*(de/(1+de))*100).toFixed(1)}%</strong>
            </div>
          </div>`;
        renderMath();
      }
    }

    function initFsaNotesCharts() {
      initReferenceNotesCharts();
    }

    function initReferenceNotesCharts() {
      // 1. Notes DuPont Multiplier Chart
      const ctxDuPont = document.getElementById('notesDupontChart');
      if (ctxDuPont && !Chart.getChart(ctxDuPont)) {
        new Chart(ctxDuPont, {
          type: 'bar',
          data: {
            labels: ['Tax Burden (NI/EBT)', 'Interest Burden (EBT/EBIT)', 'Operating Margin (EBIT/Rev)', 'Asset Turnover (Rev/Assets)', 'Leverage (Assets/Equity)'],
            datasets: [
              {
                label: 'High Margin / Low Debt Firm (ROE: 18%)',
                data: [0.78, 0.95, 0.22, 0.85, 1.35],
                backgroundColor: 'rgba(88, 166, 255, 0.7)'
              },
              {
                label: 'Low Margin / High Debt Firm (ROE: 18%)',
                data: [0.75, 0.65, 0.08, 1.60, 2.88],
                backgroundColor: 'rgba(248, 81, 73, 0.7)'
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { position: 'top' } },
            scales: { y: { beginAtZero: true, grid: { color: '#21262d' } }, x: { grid: { color: '#21262d' } } }
          }
        });
      }

      // 2. Inventory Chart (FIFO vs LIFO vs Weighted Average)
      const ctxInv = document.getElementById('inventoryChart');
      if (ctxInv && !Chart.getChart(ctxInv)) {
        new Chart(ctxInv, {
          type: 'bar',
          data: {
            labels: ['Ending Inventory', 'COGS', 'Gross Profit', 'Taxes Paid', 'Operating Cash Flow (CFO)'],
            datasets: [
              {
                label: 'FIFO (Earliest Costs to COGS)',
                data: [120, 80, 120, 24, 96],
                backgroundColor: 'rgba(63, 185, 80, 0.7)'
              },
              {
                label: 'Weighted Average',
                data: [110, 90, 110, 22, 98],
                backgroundColor: 'rgba(210, 153, 34, 0.7)'
              },
              {
                label: 'LIFO (Latest Costs to COGS)',
                data: [100, 100, 100, 20, 100],
                backgroundColor: 'rgba(248, 81, 73, 0.7)'
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { position: 'top' } },
            scales: { y: { beginAtZero: true, grid: { color: '#21262d' } }, x: { grid: { color: '#21262d' } } }
          }
        });
      }

      // 3. Depreciation Methods Chart
      const ctxDep = document.getElementById('depreciationChart');
      if (ctxDep && !Chart.getChart(ctxDep)) {
        new Chart(ctxDep, {
          type: 'line',
          data: {
            labels: ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5'],
            datasets: [
              {
                label: 'Straight-Line Depreciation (SLN)',
                data: [18000, 18000, 18000, 18000, 18000],
                borderColor: '#58a6ff',
                backgroundColor: 'rgba(88, 166, 255, 0.1)',
                tension: 0.1
              },
              {
                label: 'Double Declining Balance (DDB 40%)',
                data: [40000, 24000, 14400, 8640, 2960],
                borderColor: '#f85149',
                backgroundColor: 'rgba(248, 81, 73, 0.1)',
                tension: 0.1
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { position: 'top' } },
            scales: { y: { beginAtZero: true, grid: { color: '#21262d' } }, x: { grid: { color: '#21262d' } } }
          }
        });
      }

      // 4. Bond Amortization Chart
      const ctxBond = document.getElementById('bondChart');
      if (ctxBond && !Chart.getChart(ctxBond)) {
        new Chart(ctxBond, {
          type: 'line',
          data: {
            labels: ['Issue Date', 'Year 1', 'Year 2', 'Year 3', 'Year 4', 'Maturity (Yr 5)'],
            datasets: [
              {
                label: 'Premium Bond (Carrying Value drops to Par)',
                data: [1075.82, 1063.40, 1049.74, 1034.71, 1018.18, 1000.00],
                borderColor: '#3fb950',
                tension: 0.1
              },
              {
                label: 'Par Bond (Constant at 1,000 USD)',
                data: [1000, 1000, 1000, 1000, 1000, 1000],
                borderColor: '#8b949e',
                borderDash: [5, 5]
              },
              {
                label: 'Discount Bond (Carrying Value pulls to Par)',
                data: [924.18, 936.60, 950.26, 965.29, 981.82, 1000.00],
                borderColor: '#bc8cff',
                tension: 0.1
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { position: 'top' } },
            scales: { y: { beginAtZero: true, grid: { color: '#21262d' } }, x: { grid: { color: '#21262d' } } }
          }
        });
      }

      // 5. Pension Chart
      const ctxPen = document.getElementById('pensionChart');
      if (ctxPen && !Chart.getChart(ctxPen)) {
        new Chart(ctxPen, {
          type: 'bar',
          data: {
            labels: ['Beg Balance', 'Service Cost', 'Interest / Return', 'Contributions', 'Benefits Paid', 'Ending Balance'],
            datasets: [
              {
                label: 'PBO (Pension Obligation)',
                data: [8000, 650, 480, 0, -450, 8680],
                backgroundColor: 'rgba(248, 81, 73, 0.7)'
              },
              {
                label: 'Plan Assets (FVPA)',
                data: [7200, 0, 520, 600, -450, 7870],
                backgroundColor: 'rgba(63, 185, 80, 0.7)'
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { position: 'top' } },
            scales: { y: { beginAtZero: true, grid: { color: '#21262d' } }, x: { grid: { color: '#21262d' } } }
          }
        });
      }

      // 6. FX Translation Chart
      const ctxFx = document.getElementById('fxChart');
      if (ctxFx && !Chart.getChart(ctxFx)) {
        new Chart(ctxFx, {
          type: 'radar',
          data: {
            labels: ['Operating Margin', 'Net Margin', 'Current Ratio', 'Debt / Equity', 'Return on Equity (ROE)'],
            datasets: [
              {
                label: 'Current Rate Method (Pure Translation)',
                data: [85, 85, 90, 80, 88],
                borderColor: '#58a6ff',
                backgroundColor: 'rgba(88, 166, 255, 0.2)'
              },
              {
                label: 'Temporal Method (Mixed Rates Impact)',
                data: [70, 60, 95, 65, 72],
                borderColor: '#f85149',
                backgroundColor: 'rgba(248, 81, 73, 0.2)'
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { position: 'top' } }
          }
        });
      }

      // 7. Fixed Income Notes Curve Chart
      const ctxFiCurve = document.getElementById('fiNotesCurveChart');
      if (ctxFiCurve && !Chart.getChart(ctxFiCurve)) {
        new Chart(ctxFiCurve, {
          type: 'line',
          data: {
            labels: ['1Y', '2Y', '3Y', '5Y', '7Y', '10Y'],
            datasets: [
              {
                label: 'Benchmark Spot Curve (%)',
                data: [2.50, 2.80, 3.10, 3.60, 3.90, 4.20],
                borderColor: '#58a6ff',
                backgroundColor: 'rgba(88, 166, 255, 0.1)',
                borderWidth: 2.5,
                pointRadius: 4,
                tension: 0.2
              },
              {
                label: 'Implied 1-Year Forward Curve (%)',
                data: [2.50, 3.10, 3.70, 4.35, 4.65, 4.90],
                borderColor: '#3fb950',
                backgroundColor: 'rgba(63, 185, 80, 0.1)',
                borderWidth: 2,
                borderDash: [5, 5],
                pointRadius: 3,
                tension: 0.2
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { position: 'top' } },
            scales: { y: { title: { display: true, text: 'Yield (%)', color: '#8b949e' }, grid: { color: '#21262d' } }, x: { grid: { color: '#21262d' } } }
          }
        });
      }

      // 8. Fixed Income Notes Duration vs Convexity Chart
      const ctxFiDur = document.getElementById('fiNotesDurationChart');
      if (ctxFiDur && !Chart.getChart(ctxFiDur)) {
        new Chart(ctxFiDur, {
          type: 'line',
          data: {
            labels: ['-200 bps', '-100 bps', '0 bps', '+100 bps', '+200 bps'],
            datasets: [
              {
                label: 'Actual Convex Price Path',
                data: [119.8, 109.4, 100.0, 91.6, 84.1],
                borderColor: '#3fb950',
                borderWidth: 3,
                tension: 0.3
              },
              {
                label: 'Linear Duration Approximation',
                data: [118.0, 109.0, 100.0, 91.0, 82.0],
                borderColor: '#f85149',
                borderWidth: 2,
                borderDash: [4, 4],
                tension: 0
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { position: 'top' } },
            scales: { y: { title: { display: true, text: 'Bond Price (USD)', color: '#8b949e' }, grid: { color: '#21262d' } }, x: { grid: { color: '#21262d' } } }
          }
        });
      }

      // 9. Equity Notes DDM Sensitivity Chart
      const ctxEqDdm = document.getElementById('eqNotesDdmChart');
      if (ctxEqDdm && !Chart.getChart(ctxEqDdm)) {
        new Chart(ctxEqDdm, {
          type: 'bar',
          data: {
            labels: ['r = 7.0%', 'r = 8.0%', 'r = 9.0%', 'r = 10.0%', 'r = 11.0%'],
            datasets: [
              {
                label: 'Intrinsic Value (USD) (D0 = 2.00 USD, g = 4%)',
                data: [69.33, 52.00, 41.60, 34.67, 29.71],
                backgroundColor: 'rgba(57, 197, 207, 0.7)',
                borderColor: '#39c5cf',
                borderWidth: 1.5
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { position: 'top' } },
            scales: { y: { title: { display: true, text: 'Per Share Intrinsic Value (USD)', color: '#8b949e' }, grid: { color: '#21262d' } }, x: { grid: { color: '#21262d' } } }
          }
        });
      }

      // 10. Equity Notes Free Cash Flow Waterfall Chart
      const ctxEqFcf = document.getElementById('eqNotesFcfChart');
      if (ctxEqFcf && !Chart.getChart(ctxEqFcf)) {
        new Chart(ctxEqFcf, {
          type: 'bar',
          data: {
            labels: ['EBITDA', 'D&A', 'EBIT', 'Taxes', 'CapEx', 'ΔWC', 'FCFF', '+Net Borrowing', 'FCFE'],
            datasets: [
              {
                label: 'Cash Flow Bridge (M USD)',
                data: [150, -30, 120, -25, -40, -10, 75, 15, 65],
                backgroundColor: [
                  '#58a6ff', '#f85149', '#58a6ff', '#f85149', '#f85149', '#f85149', '#3fb950', '#d29922', '#3fb950'
                ]
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } },
            scales: { y: { title: { display: true, text: 'M USD', color: '#8b949e' }, grid: { color: '#21262d' } }, x: { grid: { color: '#21262d' } } }
          }
        });
      }
    }

    // Initialization on window load
    window.addEventListener('DOMContentLoaded', () => {
      initOverviewChart();
      initAccuracyChart();
      initL1Engine();
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
      initFrontierSim();
      initFundamentalLawSim();
      initRebalancingSim();
      initBsmSim();
      initQuantSim();
      initAltsSim();
      initCorpSim();
      initFsaNotesCharts();
      updateScoreBadge();
      renderMath();
      renderSolvedNumericals();

      function routeSubSectionHash(h) {
        const prefixMap = [
          ['eth-', 'eth-reference'],
          ['qm-', 'qm-reference'],
          ['econ-', 'econ-reference'],
          ['corp-', 'corp-reference'],
          ['deriv-', 'deriv-reference'],
          ['alt-', 'alt-reference'],
          ['fi-', 'fi-reference'],
          ['eq-', 'eq-reference'],
          ['pm-', 'pm-reference']
        ];
        for (const [pfx, tab] of prefixMap) {
          if (h.startsWith(pfx)) return tab;
        }
        return 'fsa-reference';
      }

      // Check URL hash for initial tab or sub-section
      const hash = window.location.hash.replace('#', '');
      if (hash) {
        const sec = document.getElementById(hash);
        if (sec && sec.tagName === 'SECTION' && sec.parentElement.tagName === 'MAIN') {
          switchTab(hash);
        } else if (sec) {
          switchTab(routeSubSectionHash(hash));
          setTimeout(() => {
            sec.scrollIntoView({ behavior: 'smooth' });
          }, 150);
        }
      }

      // Hash change listener for browser navigation
      window.addEventListener('hashchange', () => {
        const h = window.location.hash.replace('#', '');
        if (h) {
          const target = document.getElementById(h);
          if (target && target.tagName === 'SECTION' && target.parentElement.tagName === 'MAIN') {
            switchTab(h);
          } else if (target) {
            switchTab(routeSubSectionHash(h));
            setTimeout(() => {
              target.scrollIntoView({ behavior: 'smooth' });
            }, 100);
          }
        }
      });
    });


    // ==========================================
    // CFA JARGON & TERMINOLOGY POPOVER ENGINE
    // ==========================================
    const cfaJargonDictionary = __JARGON_DICTIONARY_DATA__;

    let currentJargonId = null;
    let jargonHistoryStack = [];
    let jargonOpenTimer = null;
    let jargonCloseTimer = null;
    let activeJargonTriggerEl = null;

    let currentGlossarySubj = 'all';
    let currentGlossaryLevel = 'all';
    let currentGlossaryQuery = '';

    let compiledJargonRegex = null;
    let phraseToJargonId = {};

    function initJargonRegex() {
      if (compiledJargonRegex) return;
      const allPhrases = [];
      phraseToJargonId = {};
      
      cfaJargonDictionary.forEach(entry => {
        const list = [entry.term, ...entry.aliases];
        list.forEach(p => {
          const clean = p.trim();
          if (clean.length >= 3) {
            allPhrases.push(clean);
            phraseToJargonId[clean.toLowerCase()] = entry.id;
          }
        });
      });
      
      allPhrases.sort((a, b) => b.length - a.length);
      const escaped = allPhrases.map(p => p.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'));
      compiledJargonRegex = new RegExp('\\b(' + escaped.join('|') + ')\\b', 'gi');
    }

    function scanAndHighlightJargon(rootElement = document.body) {
      if (!window.cfaJargonDictionary || !window.cfaJargonDictionary.length) return;
      initJargonRegex();
      if (!compiledJargonRegex) return;

      const targetSelector = '.question-text, .explanation-box, .vignette-text, .numerical-box-problem, .numerical-box-steps, .reference-content';
      const targets = rootElement.querySelectorAll ? rootElement.querySelectorAll(targetSelector) : [rootElement];

      targets.forEach(target => {
        const walker = document.createTreeWalker(
          target,
          NodeFilter.SHOW_TEXT,
          {
            acceptNode: function(node) {
              if (!node.nodeValue || !node.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
              const parent = node.parentElement;
              if (!parent) return NodeFilter.FILTER_REJECT;
              const tag = parent.tagName.toLowerCase();
              if (['script', 'style', 'noscript', 'textarea', 'input', 'code', 'pre', 'button'].includes(tag)) {
                return NodeFilter.FILTER_REJECT;
              }
              if (parent.closest('.katex') || parent.closest('.cfa-jargon-term') || parent.closest('#cfaJargonPopover') || parent.closest('#jargonGlossaryListContainer')) {
                return NodeFilter.FILTER_REJECT;
              }
              return NodeFilter.FILTER_ACCEPT;
            }
          }
        );

        const textNodes = [];
        while (walker.nextNode()) {
          textNodes.push(walker.currentNode);
        }

        textNodes.forEach(node => {
          const text = node.nodeValue;
          if (!compiledJargonRegex.test(text)) return;
          compiledJargonRegex.lastIndex = 0;

          const fragment = document.createDocumentFragment();
          let lastIdx = 0;
          let match;
          
          while ((match = compiledJargonRegex.exec(text)) !== null) {
            const matchText = match[0];
            const matchIdx = match.index;
            const termId = phraseToJargonId[matchText.toLowerCase()];

            if (matchIdx > lastIdx) {
              fragment.appendChild(document.createTextNode(text.substring(lastIdx, matchIdx)));
            }

            const span = document.createElement('span');
            span.className = 'cfa-jargon-term';
            span.setAttribute('data-jargon-id', termId || '');
            span.textContent = matchText;
            span.setAttribute('tabindex', '0');
            span.setAttribute('role', 'button');
            span.setAttribute('aria-haspopup', 'dialog');
            span.setAttribute('title', 'Hover or tap for CFA definition, formula & numerical example');
            
            span.addEventListener('mouseenter', (e) => handleJargonHover(e, termId));
            span.addEventListener('mouseleave', () => handleJargonLeave());
            span.addEventListener('click', (e) => handleJargonClick(e, termId));
            span.addEventListener('focus', (e) => handleJargonHover(e, termId));
            span.addEventListener('blur', () => handleJargonLeave());

            fragment.appendChild(span);
            lastIdx = matchIdx + matchText.length;
          }

          if (lastIdx < text.length) {
            fragment.appendChild(document.createTextNode(text.substring(lastIdx)));
          }

          if (node.parentNode) {
            node.parentNode.replaceChild(fragment, node);
          }
        });
      });
    }

    function showJargonPopover(termId, triggerEl, isHistoryNav = false) {
      if (!triggerEl && !activeJargonTriggerEl) return;
      if (triggerEl) activeJargonTriggerEl = triggerEl;
      
      const entry = cfaJargonDictionary.find(j => j.id === termId);
      if (!entry) return;

      if (!isHistoryNav && currentJargonId && currentJargonId !== termId) {
        jargonHistoryStack.push(currentJargonId);
      } else if (!isHistoryNav && !currentJargonId) {
        jargonHistoryStack = [];
      }
      currentJargonId = termId;

      const popover = document.getElementById('cfaJargonPopover');
      const header = document.getElementById('cfaJargonPopoverHeader');
      const body = document.getElementById('cfaJargonPopoverBody');
      const backdrop = document.getElementById('cfaJargonBackdrop');
      if (!popover || !header || !body) return;

      const isMobile = window.innerWidth <= 768;
      const backBtnHtml = jargonHistoryStack.length > 0 
        ? `<button class="btn-top" onclick="jargonHistoryBack()" style="padding: 2px 7px; font-size: 11px; margin-right: 6px;">← Back</button>` 
        : '';

      const categoryBadgeClass = getSubjectBadgeClass(entry.category);

      header.innerHTML = `
        <div style="flex: 1; min-width: 0;">
          <div style="display: flex; gap: 6px; align-items: center; margin-bottom: 4px; flex-wrap: wrap;">
            ${backBtnHtml}
            <span class="subject-badge ${categoryBadgeClass}">${entry.category}</span>
            <span class="nav-badge" style="font-size: 10px;">Level: ${entry.level}</span>
            <span style="font-family: var(--font-mono); font-size: 10.5px; color: var(--text-muted);">${entry.id}</span>
          </div>
          <h3 style="font-family: var(--font-serif); font-size: 16px; font-weight: 700; color: var(--text-primary); margin: 0; line-height: 1.3;">
            ${entry.term}
          </h3>
        </div>
        <button onclick="closeJargonPopover()" class="btn-top" style="padding: 2px 8px; font-size: 14px;" title="Close (Esc)">✕</button>
      `;

      let formulaHtml = '';
      if (entry.formula) {
        let renderedFormula = entry.formula;
        if (window.katex && window.katex.renderToString) {
          try {
            renderedFormula = katex.renderToString(entry.formula, { throwOnError: false, displayMode: true });
          } catch (err) {
            renderedFormula = `<code>${entry.formula}</code>`;
          }
        }
        formulaHtml = `
          <div class="cfa-jargon-section-title">Governing CFA Formula:</div>
          <div class="cfa-jargon-formula-box">${renderedFormula}</div>
        `;
      }

      let practicalHtml = '';
      if (entry.practicalUses && entry.practicalUses.length) {
        practicalHtml = `
          <div class="cfa-jargon-section-title">Practical Applications & Exam Context:</div>
          <ul style="margin: 0; padding-left: 18px; font-size: 12.5px; color: var(--text-secondary); line-height: 1.55;">
            ${entry.practicalUses.map(u => `<li style="margin-bottom: 4px;">${u}</li>`).join('')}
          </ul>
        `;
      }

      let pitfallsHtml = '';
      if (entry.commonPitfalls && entry.commonPitfalls.length) {
        pitfallsHtml = `
          <div class="cfa-jargon-section-title" style="color: var(--accent-rose);">⚠️ Common Traps & Exam Pitfalls:</div>
          <div class="cfa-jargon-pitfalls-box">
            <ul style="margin: 0; padding-left: 16px;">
              ${entry.commonPitfalls.map(p => `<li style="margin-bottom: 4px;">${p}</li>`).join('')}
            </ul>
          </div>
        `;
      }

      let numericalHtml = '';
      if (entry.workedNumerical) {
        const wn = entry.workedNumerical;
        numericalHtml = `
          <div class="cfa-jargon-section-title" style="color: var(--accent-amber);">📐 Worked Step-by-Step Numerical Example:</div>
          <div class="cfa-jargon-numerical-box">
            <div class="cfa-jargon-numerical-title">${wn.title}</div>
            <div style="font-weight: 600; font-size: 11.5px; text-transform: uppercase; color: var(--text-muted); margin-bottom: 3px;">Given Inputs:</div>
            <ul style="margin: 0 0 8px 0; padding-left: 16px; color: var(--text-secondary); font-size: 12px;">
              ${wn.given.map(g => `<li>${g}</li>`).join('')}
            </ul>
            <div style="font-weight: 600; font-size: 11.5px; text-transform: uppercase; color: var(--text-muted); margin-bottom: 3px;">Step-by-Step Solution:</div>
            <ol style="margin: 0 0 8px 0; padding-left: 16px; line-height: 1.5; font-size: 12px;">
              ${wn.steps.map(s => `<li style="margin-bottom: 3px;">${s}</li>`).join('')}
            </ol>
            <div class="cfa-jargon-result-badge">
              Final Answer: ${wn.result}
            </div>
          </div>
        `;
      }

      let deepLinksHtml = '';
      if (entry.relatedNumCode || entry.relatedSimTab) {
        deepLinksHtml = `<div style="display: flex; gap: 8px; flex-wrap: wrap; margin-top: 10px;">`;
        if (entry.relatedNumCode) {
          deepLinksHtml += `
            <button class="filter-btn active" style="font-size: 11px; padding: 4px 10px;" onclick="openMasterSolvedCase('${entry.relatedNumCode}')">
              ⚡ Jump to Case ${entry.relatedNumCode} in Solved Numericals
            </button>
          `;
        }
        if (entry.relatedSimTab) {
          deepLinksHtml += `
            <button class="filter-btn" style="font-size: 11px; padding: 4px 10px;" onclick="openInteractiveSim('${entry.relatedSimTab}')">
              📈 Open Simulation Engine
            </button>
          `;
        }
        deepLinksHtml += `</div>`;
      }

      let relatedHtml = '';
      if (entry.relatedTerms && entry.relatedTerms.length) {
        relatedHtml = `
          <div class="cfa-jargon-section-title">Related CFA Terminology:</div>
          <div style="display: flex; flex-wrap: wrap; gap: 4px; margin-top: 4px;">
            ${entry.relatedTerms.map(rtId => {
              const rtEntry = cfaJargonDictionary.find(j => j.id === rtId);
              const label = rtEntry ? rtEntry.term : rtId;
              return `<span class="cfa-jargon-related-tag" onclick="navigateJargon('${rtId}')">🔗 ${label}</span>`;
            }).join('')}
          </div>
        `;
      }

      body.innerHTML = `
        <div class="cfa-jargon-section-title">Intuitive Definition:</div>
        <p style="margin: 0 0 10px 0; font-size: 13.5px; line-height: 1.6;">${entry.definition}</p>
        ${formulaHtml}
        ${practicalHtml}
        ${pitfallsHtml}
        ${numericalHtml}
        ${deepLinksHtml}
        ${relatedHtml}
      `;

      if (window.renderMathInElement) {
        renderMathInElement(body, {
          delimiters: [
            {left: '$$', right: '$$', display: true},
            {left: '$', right: '$', display: false}
          ],
          throwOnError: false
        });
      }

      positionJargonPopover(activeJargonTriggerEl);
      popover.style.display = 'flex';
      requestAnimationFrame(() => popover.classList.add('visible'));

      if (isMobile && backdrop) {
        backdrop.style.display = 'block';
      }
    }

    function positionJargonPopover(triggerEl) {
      const popover = document.getElementById('cfaJargonPopover');
      if (!popover) return;

      const isMobile = window.innerWidth <= 768;
      if (isMobile) {
        popover.style.left = '16px';
        popover.style.right = '16px';
        popover.style.bottom = '16px';
        popover.style.top = 'auto';
        popover.style.width = 'calc(100vw - 32px)';
        popover.style.maxHeight = '75vh';
        return;
      }

      const pWidth = 440;
      popover.style.width = pWidth + 'px';
      popover.style.maxHeight = '480px';
      popover.style.right = 'auto';
      popover.style.bottom = 'auto';

      if (!triggerEl || !triggerEl.getBoundingClientRect) {
        popover.style.left = Math.max(16, (window.innerWidth - pWidth) / 2) + 'px';
        popover.style.top = '80px';
        return;
      }

      const tRect = triggerEl.getBoundingClientRect();
      const vWidth = window.innerWidth;
      const vHeight = window.innerHeight;
      const pHeight = 440;

      const idealX = tRect.left + (tRect.width / 2) - (pWidth / 2);
      const clampedX = Math.max(16, Math.min(idealX, vWidth - pWidth - 16));
      popover.style.left = clampedX + 'px';

      const spaceBelow = vHeight - tRect.bottom - 16;
      const spaceAbove = tRect.top - 16;

      if (spaceBelow < 360 && spaceAbove > spaceBelow) {
        const topPos = Math.max(16, tRect.top - pHeight - 8);
        popover.style.top = topPos + 'px';
        popover.style.maxHeight = Math.min(480, tRect.top - 24) + 'px';
      } else {
        popover.style.top = (tRect.bottom + 8) + 'px';
        popover.style.maxHeight = Math.min(480, spaceBelow) + 'px';
      }
    }

    function handleJargonHover(e, termId) {
      clearTimeout(jargonCloseTimer);
      clearTimeout(jargonOpenTimer);
      const trigger = e.currentTarget || e.target;
      activeJargonTriggerEl = trigger;

      jargonOpenTimer = setTimeout(() => {
        showJargonPopover(termId, trigger);
      }, 200);
    }

    function handleJargonLeave() {
      clearTimeout(jargonOpenTimer);
      jargonCloseTimer = setTimeout(() => {
        closeJargonPopover();
      }, 180);
    }

    function cancelJargonClose() {
      clearTimeout(jargonCloseTimer);
    }

    function handleJargonPopoverLeave() {
      jargonCloseTimer = setTimeout(() => {
        closeJargonPopover();
      }, 180);
    }

    function handleJargonClick(e, termId) {
      if (e) {
        e.preventDefault();
        e.stopPropagation();
      }
      clearTimeout(jargonOpenTimer);
      clearTimeout(jargonCloseTimer);
      showJargonPopover(termId, e ? (e.currentTarget || e.target) : activeJargonTriggerEl);
    }

    function navigateJargon(termId) {
      showJargonPopover(termId, activeJargonTriggerEl, false);
      const body = document.getElementById('cfaJargonPopoverBody');
      if (body) body.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function jargonHistoryBack() {
      if (jargonHistoryStack.length > 0) {
        const prevId = jargonHistoryStack.pop();
        showJargonPopover(prevId, activeJargonTriggerEl, true);
        const body = document.getElementById('cfaJargonPopoverBody');
        if (body) body.scrollTo({ top: 0, behavior: 'smooth' });
      }
    }

    function closeJargonPopover() {
      clearTimeout(jargonOpenTimer);
      clearTimeout(jargonCloseTimer);
      const popover = document.getElementById('cfaJargonPopover');
      const backdrop = document.getElementById('cfaJargonBackdrop');
      if (popover) {
        popover.classList.remove('visible');
        setTimeout(() => {
          popover.style.display = 'none';
          currentJargonId = null;
        }, 150);
      }
      if (backdrop) {
        backdrop.style.display = 'none';
      }
    }

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closeJargonPopover();
      }
    });

    function openMasterSolvedCase(numCode) {
      closeJargonPopover();
      switchTab('solved-numericals');
      setTimeout(() => {
        const input = document.getElementById('numSearchInput');
        if (input) {
          input.value = numCode;
          filterNumericals('all', 'all', numCode);
        }
        const card = document.querySelector(`.numerical-card[id*="${numCode}"]`) || document.querySelector('.numerical-card');
        if (card) {
          card.scrollIntoView({ behavior: 'smooth', block: 'center' });
          card.style.outline = '2px solid var(--accent-amber)';
          setTimeout(() => { card.style.outline = ''; }, 2500);
        }
      }, 250);
    }

    function openInteractiveSim(simTab) {
      closeJargonPopover();
      const tabMap = {
        'yield-curve': 'sim-yield',
        'tree': 'sim-tree',
        'dupont': 'sim-equity',
        'ddm': 'sim-equity',
        'key-rate': 'sim-duration',
        'frn': 'sim-frn',
        'ri': 'sim-ri-decay',
        'cashflow': 'sim-waterfall',
        'translation': 'sim-translation',
        'prepayment': 'sim-prepayment',
        'markowitz': 'sim-frontier',
        'active': 'sim-fundamental-law',
        'rebalancing': 'sim-rebalancing',
        'bsm': 'sim-bsm',
        'quant': 'sim-quant',
        'alts': 'sim-alts',
        'corp': 'sim-corp'
      };
      const targetTab = tabMap[simTab] || simTab;
      switchTab(targetTab);
    }

    function filterJargonGlossary(subj, level, query) {
      if (subj !== undefined) currentGlossarySubj = subj;
      if (level !== undefined) currentGlossaryLevel = level;
      if (query !== undefined) currentGlossaryQuery = query.toLowerCase().trim();

      ['all', 'eth', 'qm', 'econ', 'fsa', 'corp', 'eq', 'fi', 'deriv', 'alt', 'pm'].forEach(s => {
        const btn = document.getElementById('glossSubj-' + s);
        if (btn) btn.classList.toggle('active', (s === 'all' && currentGlossarySubj === 'all') || (s.toUpperCase() === currentGlossarySubj));
      });

      ['all', 'l1', 'l2', 'both'].forEach(l => {
        const btn = document.getElementById('glossLvl-' + l);
        if (btn) btn.classList.toggle('active', (l === 'all' && currentGlossaryLevel === 'all') || (l.toUpperCase() === currentGlossaryLevel.toUpperCase()));
      });

      renderJargonGlossary();
    }

    function renderJargonGlossary() {
      const container = document.getElementById('jargonGlossaryListContainer');
      if (!container || !window.cfaJargonDictionary) return;

      const filtered = cfaJargonDictionary.filter(item => {
        const matchSubj = currentGlossarySubj === 'all' || item.category === currentGlossarySubj;
        const matchLvl = currentGlossaryLevel === 'all' || item.level.toUpperCase() === currentGlossaryLevel.toUpperCase();
        let matchQuery = true;
        if (currentGlossaryQuery) {
          const hay = (item.term + ' ' + item.aliases.join(' ') + ' ' + item.definition + ' ' + item.formula + ' ' + item.category + ' ' + item.id).toLowerCase();
          matchQuery = hay.includes(currentGlossaryQuery);
        }
        return matchSubj && matchLvl && matchQuery;
      });

      const countDisplay = document.getElementById('jargonCountDisplay');
      if (countDisplay) {
        countDisplay.innerText = `${filtered.length} of ${cfaJargonDictionary.length} Master Terminologies`;
      }

      if (filtered.length === 0) {
        container.innerHTML = `
          <div class="card" style="text-align: center; padding: 40px; color: var(--text-secondary);">
            <p style="font-size: 15px;">No terminology matches your selected filters.</p>
            <button class="filter-btn" style="margin-top: 10px;" onclick="filterJargonGlossary('all', 'all', '')">Reset Filters</button>
          </div>
        `;
        return;
      }

      container.innerHTML = filtered.map(item => {
        const catClass = getSubjectBadgeClass(item.category);

        let renderedFormula = item.formula;
        if (window.katex && window.katex.renderToString) {
          try {
            renderedFormula = katex.renderToString(item.formula, { throwOnError: false, displayMode: true });
          } catch (e) {
            renderedFormula = `<code>${item.formula}</code>`;
          }
        }

        const wn = item.workedNumerical;
        let numSection = '';
        if (wn) {
          numSection = `
            <details style="margin-top: 12px; border: 1px solid var(--border-color); border-radius: 4px; padding: 8px 12px; background: var(--bg-tertiary);">
              <summary style="cursor: pointer; font-weight: 600; color: var(--accent-amber); font-family: var(--font-mono); font-size: 12.5px;">
                ▶ Click to Expand Worked Numerical: ${wn.title}
              </summary>
              <div style="margin-top: 10px; font-size: 12.5px;">
                <div style="font-weight: 700; color: var(--text-muted); text-transform: uppercase; font-size: 11px; margin-bottom: 2px;">Given:</div>
                <ul style="margin: 0 0 6px 0; padding-left: 16px; color: var(--text-secondary);">
                  ${wn.given.map(g => `<li>${g}</li>`).join('')}
                </ul>
                <div style="font-weight: 700; color: var(--text-muted); text-transform: uppercase; font-size: 11px; margin-bottom: 2px;">Steps:</div>
                <ol style="margin: 0 0 6px 0; padding-left: 16px;">
                  ${wn.steps.map(s => `<li>${s}</li>`).join('')}
                </ol>
                <div class="cfa-jargon-result-badge">Result: ${wn.result}</div>
              </div>
            </details>
          `;
        }

        return `
          <div class="card" style="margin-bottom: 16px;" id="glossary-card-${item.id}">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 8px; margin-bottom: 8px;">
              <div>
                <div style="display: flex; gap: 6px; align-items: center; margin-bottom: 4px;">
                  <span class="subject-badge ${catClass}">${item.category}</span>
                  <span class="nav-badge">Level: ${item.level}</span>
                  <span style="font-family: var(--font-mono); font-size: 11px; color: var(--text-muted);">${item.id}</span>
                </div>
                <h3 style="font-family: var(--font-serif); font-size: 18px; font-weight: 700; margin: 0; color: var(--text-primary);">
                  ${item.term}
                </h3>
              </div>
              <div style="display: flex; gap: 6px; align-items: center;">
                <button class="filter-btn" style="font-size: 11px; padding: 4px 10px;" onclick="showJargonPopover('${item.id}', this)">
                  👁️ Preview Popover Card
                </button>
                ${item.relatedNumCode ? `<button class="filter-btn active" style="font-size: 11px; padding: 4px 10px;" onclick="openMasterSolvedCase('${item.relatedNumCode}')">⚡ Solved Case</button>` : ''}
              </div>
            </div>
            <p style="font-size: 13.5px; line-height: 1.6; margin: 0 0 10px 0; color: var(--text-primary);">${item.definition}</p>
            <div class="cfa-jargon-formula-box">${renderedFormula}</div>
            <div style="display: flex; gap: 16px; flex-wrap: wrap; margin-top: 10px;">
              <div style="flex: 1 1 300px;">
                <div class="cfa-jargon-section-title">Practical Uses:</div>
                <ul style="margin: 0; padding-left: 16px; font-size: 12.5px; color: var(--text-secondary);">
                  ${item.practicalUses.map(u => `<li>${u}</li>`).join('')}
                </ul>
              </div>
              <div style="flex: 1 1 300px;">
                <div class="cfa-jargon-section-title" style="color: var(--accent-rose);">⚠️ Pitfalls:</div>
                <ul style="margin: 0; padding-left: 16px; font-size: 12.5px; color: var(--text-secondary);">
                  ${item.commonPitfalls.map(p => `<li>${p}</li>`).join('')}
                </ul>
              </div>
            </div>
            ${numSection}
            <div style="margin-top: 10px; display: flex; gap: 4px; flex-wrap: wrap; align-items: center;">
              <span style="font-family: var(--font-mono); font-size: 10.5px; color: var(--text-muted); margin-right: 4px;">Related:</span>
              ${item.relatedTerms.map(rtId => {
                const rt = cfaJargonDictionary.find(j => j.id === rtId);
                return `<span class="cfa-jargon-related-tag" onclick="showJargonPopover('${rtId}', this)">🔗 ${rt ? rt.term : rtId}</span>`;
              }).join('')}
            </div>
          </div>
        `;
      }).join('');

      if (window.renderMathInElement) {
        renderMathInElement(container, {
          delimiters: [
            {left: '$$', right: '$$', display: true},
            {left: '$', right: '$', display: false}
          ],
          throwOnError: false
        });
      }
    }

        // Embedded Master Solved Numericals Bank
    const masterSolvedNumericals = __MASTER_SOLVED_NUMERICALS_DATA__;

    let currentNumSubj = 'all';
    let currentNumDiff = 'all';
    let currentNumQuery = '';

    function toggleDesktopSidebar() {
      const isCollapsed = document.body.classList.toggle('sidebar-collapsed');
      localStorage.setItem('cfa_sidebar_collapsed', isCollapsed ? '1' : '0');
      const expandBtn = document.getElementById('desktopSidebarToggle');
      if (expandBtn) expandBtn.classList.toggle('active', isCollapsed);
      window.dispatchEvent(new Event('resize'));
    }

    // Initialize sidebar collapse state on startup
    if (localStorage.getItem('cfa_sidebar_collapsed') === '1') {
      document.body.classList.add('sidebar-collapsed');
      const expandBtn = document.getElementById('desktopSidebarToggle');
      if (expandBtn) expandBtn.classList.add('active');
    }

    // Keyboard shortcut: Ctrl+B or [ toggles sidebar
    window.addEventListener('keydown', (e) => {
      if ((e.ctrlKey && e.key.toLowerCase() === 'b') || (e.key === '[' && !['INPUT', 'TEXTAREA', 'SELECT'].includes(e.target.tagName))) {
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
      const subjMap = {
        'all': 'numSubj-all',
        'Ethical and Professional Standards': 'numSubj-eth',
        'Quantitative Methods': 'numSubj-qm',
        'Economics': 'numSubj-econ',
        'Financial Statement Analysis': 'numSubj-fsa',
        'Corporate Issuers': 'numSubj-corp',
        'Equity Investments': 'numSubj-eq',
        'Fixed Income': 'numSubj-fi',
        'Derivatives': 'numSubj-deriv',
        'Alternative Investments': 'numSubj-alt',
        'Portfolio Management': 'numSubj-pm'
      };
      const subjId = subjMap[currentNumSubj] || 'numSubj-all';
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
  </script>
</body>
</html>
'''

def build_notes_tabs(active_id: str) -> str:
    tabs = [
        ("eth-reference", "⚖️ I. Ethics (10 Ch + 50 Drills)"),
        ("qm-reference", "📐 II. Quant (12 Ch)"),
        ("econ-reference", "🌍 III. Economics (10 Ch)"),
        ("fsa-reference", "📖 IV. FSA (20 Ch)"),
        ("corp-reference", "🏢 V. Corp Issuers (9 Ch)"),
        ("eq-reference", "📊 VI. Equity (8 Ch)"),
        ("fi-reference", "📈 VII. Fixed Income (8 Ch)"),
        ("deriv-reference", "⚡ VIII. Derivatives (9 Ch)"),
        ("alt-reference", "🏛️ IX. Alternatives (9 Ch)"),
        ("pm-reference", "💼 X–XII. Portfolio Mgmt (10 Ch)"),
    ]
    btns = []
    for tid, label in tabs:
        cls = "notes-tab-btn active" if tid == active_id else "notes-tab-btn"
        btns.append(f'<button class="{cls}" onclick="switchTab(\'{tid}\')">{label}</button>')
    return '<div class="notes-subject-tabs">\n        ' + "\n        ".join(btns) + "\n      </div>"


def generate():
    JARGON_JSON = os.path.join(DATA_DIR, "cfa_jargon_dictionary.json")
    SOLVED_JSON = os.path.join(DATA_DIR, "master_solved_numericals.json")
    ref_files = {
        "__ETH_REFERENCE_CONTENT__": os.path.join(DATA_DIR, "eth_reference_extracted.html"),
        "__QM_REFERENCE_CONTENT__": os.path.join(DATA_DIR, "qm_reference_extracted.html"),
        "__ECON_REFERENCE_CONTENT__": os.path.join(DATA_DIR, "econ_reference_extracted.html"),
        "__FSA_REFERENCE_CONTENT__": FSA_REF_HTML,
        "__CORP_REFERENCE_CONTENT__": os.path.join(DATA_DIR, "corp_reference_extracted.html"),
        "__EQ_REFERENCE_CONTENT__": os.path.join(DATA_DIR, "eq_reference_extracted.html"),
        "__FI_REFERENCE_CONTENT__": os.path.join(DATA_DIR, "fi_reference_extracted.html"),
        "__DERIV_REFERENCE_CONTENT__": os.path.join(DATA_DIR, "deriv_reference_extracted.html"),
        "__ALT_REFERENCE_CONTENT__": os.path.join(DATA_DIR, "alt_reference_extracted.html"),
        "__PM_REFERENCE_CONTENT__": os.path.join(DATA_DIR, "pm_reference_extracted.html"),
    }

    assert os.path.exists(MASTER_JSON), f"Missing {MASTER_JSON}. Run compile_unified_suite.py first."
    assert os.path.exists(JARGON_JSON), f"Missing {JARGON_JSON}."
    assert os.path.exists(SOLVED_JSON), f"Missing {SOLVED_JSON}."
    for k, p in ref_files.items():
        assert os.path.exists(p), f"Missing reference file {p}."

    with open(MASTER_JSON, "r", encoding="utf-8") as f:
        questions = json.load(f)
    with open(JARGON_JSON, "r", encoding="utf-8") as f:
        jargon_entries = json.load(f)
    with open(SOLVED_JSON, "r", encoding="utf-8") as f:
        solved_entries = json.load(f)

    print(f"Loaded {len(questions)} questions from {MASTER_JSON}")
    print(f"Loaded {len(jargon_entries)} CFA jargon entries from {JARGON_JSON}")
    print(f"Loaded {len(solved_entries)} master solved numericals from {SOLVED_JSON}")

    dashboard_html = dashboard_template
    dashboard_html = dashboard_html.replace("__QUESTION_BANK_DATA__", json.dumps(questions, ensure_ascii=False))
    dashboard_html = dashboard_html.replace("__JARGON_DICTIONARY_DATA__", json.dumps(jargon_entries, ensure_ascii=False))
    dashboard_html = dashboard_html.replace("__MASTER_SOLVED_NUMERICALS_DATA__", json.dumps(solved_entries, ensure_ascii=False))

    tab_tokens = {
        "__NOTES_TABS_ETH__": "eth-reference",
        "__NOTES_TABS_QM__": "qm-reference",
        "__NOTES_TABS_ECON__": "econ-reference",
        "__NOTES_TABS_FSA__": "fsa-reference",
        "__NOTES_TABS_CORP__": "corp-reference",
        "__NOTES_TABS_EQ__": "eq-reference",
        "__NOTES_TABS_FI__": "fi-reference",
        "__NOTES_TABS_DERIV__": "deriv-reference",
        "__NOTES_TABS_ALT__": "alt-reference",
        "__NOTES_TABS_PM__": "pm-reference",
    }
    for tok, active_id in tab_tokens.items():
        dashboard_html = dashboard_html.replace(tok, build_notes_tabs(active_id))

    for placeholder, fpath in ref_files.items():
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        dashboard_html = dashboard_html.replace(placeholder, content)
        print(f"Loaded {len(content):,} chars -> {os.path.basename(fpath)}")

    with open(OUTPUT_INDEX, "w", encoding="utf-8") as f:
        f.write(dashboard_html)

    print(f"Generated unified master dashboard at: {OUTPUT_INDEX} ({os.path.getsize(OUTPUT_INDEX)} bytes)")

    # Generate backward-compatibility redirect for fi_eq_dashboard.html
    redirect_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url=index.html">
  <title>Redirecting to Unified CFA Master Platform...</title>
  <link rel="canonical" href="index.html">
  <script>
    window.location.replace("index.html" + window.location.hash);
  </script>
</head>
<body style="font-family: sans-serif; background: #0d1117; color: #e6edf3; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0;">
  <div style="text-align: center; padding: 20px;">
    <h2>Redirecting to the Unified CFA Master Platform...</h2>
    <p style="color: #8b949e;">Fixed Income & Equity has been consolidated into the single master dashboard.</p>
    <p><a href="index.html" style="color: #58a6ff;">Click here if you are not redirected automatically.</a></p>
  </div>
</body>
</html>'''

    with open(OUTPUT_FI_EQ, "w", encoding="utf-8") as f:
        f.write(redirect_html)

    print(f"Generated backward-compatibility redirect at: {OUTPUT_FI_EQ}")

if __name__ == "__main__":
    generate()
