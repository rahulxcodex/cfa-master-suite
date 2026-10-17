#!/usr/bin/env python3
"""
generate_unified_dashboard.py
Compiles the complete, unified CFA Master Study Dashboard into index.html
Housing all 875 questions (FSA, Fixed Income, Equity), 9 financial simulations,
and the full 20-chapter FSA reference library with KaTeX math rendering and Chart.js telemetry.
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
  <title>CFA Master Study Platform: FSA, Fixed Income & Equity (L1 & L2)</title>
  
  <meta name="description" content="Unified CFA Program Level 1 & Level 2 Master Exam Preparation Suite. 875 audited questions across Financial Statement Analysis, Fixed Income, and Equity Investments, with 84 case vignettes, 9 simulation engines, and complete 20-chapter reference library.">
  <link rel="canonical" href="https://rahulxcodex.github.io/cfa-master-suite/">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🎓</text></svg>">
  <meta property="og:title" content="CFA Master Study Platform (875 Questions, 9 Sims, 20 Chapters)">
  <meta property="og:description" content="Comprehensive CFA L1 & L2 prep platform: 875 questions, 84 vignettes, 9 simulations, and full 20-chapter FSA notes with KaTeX & Chart.js.">
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

    .table-container {
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
      gap: 12px;
      margin-bottom: 24px;
      flex-wrap: wrap;
    }
    .notes-tab-btn {
      padding: 10px 18px;
      border-radius: 6px;
      font-size: 13.5px;
      font-weight: 600;
      cursor: pointer;
      border: 1px solid var(--border-color);
      background: var(--bg-secondary);
      color: var(--text-secondary);
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 8px;
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
    .notes-chapter, section, [id^="m"], [id^="fi-"], [id^="eq-"], #master-gaap-ifrs, #master-formulas, #fi-formulas, #eq-formulas {
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
        <p style="font-family: var(--font-mono); font-size: 11px; color: var(--text-secondary); margin-top: 3px;">1,085 Certified Questions</p>
      </div>
      <div style="display: flex; gap: 4px; align-items: center;">
        <button class="btn-collapse-sidebar" onclick="toggleDesktopSidebar()" title="Collapse Left Sidebar (Ctrl+B)">◀ Collapse</button>
        <button class="btn-top sidebar-close-btn" onclick="closeMobileNav()" title="Close Menu">✕</button>
      </div>
    </div>
    <ul class="nav-links">
      <li><a href="#overview" class="active" onclick="switchTab('overview')"><span>Overview & Telemetry</span></a></li>
      <li><a href="#l1-practice" onclick="switchTab('l1-practice')"><span>Level 1 Question Bank</span> <span class="nav-badge">545 Q</span></a></li>
      <li><a href="#l2-vignettes" onclick="switchTab('l2-vignettes')"><span>Level 2 Case Vignettes</span> <span class="nav-badge">102 V / 540 Q</span></a></li>
      
      <li class="nav-divider"><span>PRACTICE & WORKED SOLUTIONS</span></li>
      <li><a href="#solved-numericals" onclick="switchTab('solved-numericals')"><span>Master Solved Numericals</span> <span class="nav-badge" style="color: var(--accent-amber); border-color: var(--accent-amber);">27 Worked</span></a></li>
      <li><a href="#curriculum-audit" onclick="switchTab('curriculum-audit')"><span>Curriculum Audit & Gaps</span> <span class="nav-badge">2024–2026</span></a></li>
      
      <li class="nav-divider"><span>FINANCIAL SIMULATIONS (12)</span></li>
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
      
      <li class="nav-divider"><span>CURRICULUM REFERENCE NOTES</span></li>
      <li><a href="#fsa-reference" onclick="switchTab('fsa-reference')"><span>📖 FSA Reference Notes (Ch 1-20)</span></a></li>
      <li><a href="#fi-reference" onclick="switchTab('fi-reference')"><span>📈 Fixed Income Master Notes</span></a></li>
      <li><a href="#eq-reference" onclick="switchTab('eq-reference')"><span>📊 Equity Valuation Reference</span></a></li>
      <li><a href="#pm-reference" onclick="switchTab('pm-reference')"><span>💼 Portfolio Management Notes</span></a></li>
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
        <div class="stat-pill" style="color: var(--accent-blue);">Total: 1,085 Questions</div>
        <div class="stat-pill" style="color: var(--accent-emerald);">Score: <span id="scoreDisplay">0 / 0 (0%)</span></div>
        <button class="btn-top" onclick="resetScores()">🔄 Reset Score</button>
        <button class="btn-top" onclick="toggleTheme()">🌓 Theme</button>
      </div>
    </div>

    <!-- 1. OVERVIEW & TELEMETRY -->
    <section id="overview" class="active">
      <div class="grid-5" style="margin-bottom: 24px;">
        <div class="card" style="margin-bottom: 0;">
          <div style="font-size: 11px; color: var(--text-secondary); text-transform: uppercase; font-weight: 700;">Financial Statement Analysis</div>
          <div style="font-size: 26px; font-weight: 700; color: var(--accent-amber); margin-top: 5px;">460 Qs</div>
          <div style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">190 L1 + 270 L2 (48 Vignettes)</div>
        </div>
        <div class="card" style="margin-bottom: 0;">
          <div style="font-size: 11px; color: var(--text-secondary); text-transform: uppercase; font-weight: 700;">Fixed Income</div>
          <div style="font-size: 26px; font-weight: 700; color: var(--accent-cyan); margin-top: 5px;">205 Qs</div>
          <div style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">120 L1 + 85 L2 (17 Vignettes)</div>
        </div>
        <div class="card" style="margin-bottom: 0;">
          <div style="font-size: 11px; color: var(--text-secondary); text-transform: uppercase; font-weight: 700;">Equity Investments</div>
          <div style="font-size: 26px; font-weight: 700; color: var(--accent-emerald); margin-top: 5px;">210 Qs</div>
          <div style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">115 L1 + 95 L2 (19 Vignettes)</div>
        </div>
        <div class="card" style="margin-bottom: 0;">
          <div style="font-size: 11px; color: var(--text-secondary); text-transform: uppercase; font-weight: 700;">Portfolio Management</div>
          <div style="font-size: 26px; font-weight: 700; color: var(--accent-purple); margin-top: 5px;">210 Qs</div>
          <div style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">120 L1 + 90 L2 (18 Vignettes)</div>
        </div>
        <div class="card" style="margin-bottom: 0;">
          <div style="font-size: 11px; color: var(--text-secondary); text-transform: uppercase; font-weight: 700;">Total Master Suite</div>
          <div style="font-size: 26px; font-weight: 700; color: var(--accent-blue); margin-top: 5px;">1,085 Qs</div>
          <div style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">545 L1 + 540 L2 (102 V) + 12 Sims</div>
        </div>
      </div>

      <div class="grid-2" style="margin-bottom: 24px;">
        <div class="card" style="margin-bottom: 0;">
          <div class="card-title">Curriculum Distribution & Structure</div>
          <div class="chart-canvas-wrap" style="height: 250px;">
            <canvas id="overviewChart"></canvas>
          </div>
        </div>
        <div class="card" style="margin-bottom: 0;">
          <div class="card-title">Candidate Performance Telemetry</div>
          <div class="chart-canvas-wrap" style="height: 250px;">
            <canvas id="accuracyChart"></canvas>
          </div>
        </div>
      </div>

      <div class="card">
        <div class="card-title">Quick Launch Study Portals</div>
        <div class="grid-3" style="margin-bottom: 12px;">
          <button class="btn" onclick="switchTab('l1-practice')">📝 Level 1 Question Bank (545 Q)</button>
          <button class="btn btn-secondary" onclick="switchTab('l2-vignettes')">📑 Level 2 Case Vignettes (102 V)</button>
          <button class="btn btn-secondary" onclick="switchTab('sim-yield')">🔬 Financial Simulations Lab (12)</button>
        </div>
        <div class="grid-4">
          <button class="btn btn-secondary" onclick="switchTab('fsa-reference')">📖 FSA Reference Notes</button>
          <button class="btn btn-secondary" onclick="switchTab('fi-reference')">📈 Fixed Income Notes</button>
          <button class="btn btn-secondary" onclick="switchTab('eq-reference')">📊 Equity Valuation Notes</button>
          <button class="btn btn-secondary" onclick="switchTab('pm-reference')">💼 Portfolio Management</button>
        </div>
      </div>
    </section>

    <!-- 2. LEVEL 1 QUESTION BANK -->
    <section id="l1-practice">
      <div class="card">
        <div class="card-title">Level 1 Multiple-Choice Question Bank (545 Questions)</div>
        <div class="grid-4" style="margin-bottom: 16px;">
          <div class="control-group">
            <label>Filter Subject:</label>
            <select id="l1SubjectSelect" onchange="onL1SubjectChange()">
              <option value="ALL">All Subjects (545 Questions)</option>
              <option value="Financial Statement Analysis">Financial Statement Analysis (190 Qs)</option>
              <option value="Fixed Income">Fixed Income (120 Qs)</option>
              <option value="Equity Investments">Equity Investments (115 Qs)</option>
              <option value="Portfolio Management">Portfolio Management (120 Qs)</option>
            </select>
          </div>
          <div class="control-group">
            <label>Filter Topic / Module:</label>
            <select id="l1TopicSelect" onchange="onL1TopicChange()">
              <option value="ALL">All Learning Modules</option>
            </select>
          </div>
          <div class="control-group">
            <label>Question Type Filter:</label>
            <div class="filter-pills">
              <button class="filter-pill active" id="l1TypeAll" onclick="setL1TypeFilter('ALL')">All</button>
              <button class="filter-pill" id="l1TypeNum" onclick="setL1TypeFilter('NUMERICAL')">🧮 Numericals</button>
              <button class="filter-pill" id="l1TypeTheory" onclick="setL1TypeFilter('THEORY')">📖 Theory</button>
            </div>
          </div>
          <div class="control-group">
            <label>Search Keyword / LOS:</label>
            <input type="text" id="l1SearchInput" placeholder="e.g. Duration, CAPM, Sharpe, Beta..." oninput="onL1Search()">
          </div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid var(--border-color); padding-top: 14px; flex-wrap: wrap; gap: 10px;">
          <div style="font-weight: 600; color: var(--accent-blue);" id="l1CountBadge">
            Showing Question 1 of 545
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
        <div class="card-title">Level 2 Vignette & Item-Set Explorer (102 Vignettes / 540 Questions)</div>
        <div class="grid-4" style="margin-bottom: 16px;">
          <div class="control-group">
            <label>Filter Subject:</label>
            <select id="l2SubjectSelect" onchange="onL2SubjectChange()">
              <option value="ALL">All Subjects (102 Vignettes / 540 Qs)</option>
              <option value="Financial Statement Analysis">Financial Statement Analysis (48 V / 270 Qs)</option>
              <option value="Fixed Income">Fixed Income (17 V / 85 Qs)</option>
              <option value="Equity Investments">Equity Investments (19 V / 95 Qs)</option>
              <option value="Portfolio Management">Portfolio Management (18 V / 90 Qs)</option>
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

    <!-- 13. MASTER FSA REFERENCE NOTES -->
    <section id="fsa-reference">
      <div class="notes-subject-tabs">
        <button class="notes-tab-btn active" onclick="switchTab('fsa-reference')">📖 Financial Statement Analysis (20 Modules)</button>
        <button class="notes-tab-btn" onclick="switchTab('fi-reference')">📈 Fixed Income Master Notes (8 Modules)</button>
        <button class="notes-tab-btn" onclick="switchTab('eq-reference')">📊 Equity Valuation Reference (8 Modules)</button>
        <button class="notes-tab-btn" onclick="switchTab('pm-reference')">💼 Portfolio Management (8 Modules)</button>
      </div>

      <div class="card">
        <div class="card-title">📖 Comprehensive Financial Statement Analysis Reference Library</div>
        <p style="color: var(--text-secondary); margin-bottom: 16px;">
          20 Chapters of in-depth theoretical notes, comparative IFRS vs US GAAP matrices, and the master financial ratio formula sheet.
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

    <!-- 14. FIXED INCOME REFERENCE NOTES -->
    <section id="fi-reference">
      <div class="notes-subject-tabs">
        <button class="notes-tab-btn" onclick="switchTab('fsa-reference')">📖 Financial Statement Analysis (20 Modules)</button>
        <button class="notes-tab-btn active" onclick="switchTab('fi-reference')">📈 Fixed Income Master Notes (8 Modules)</button>
        <button class="notes-tab-btn" onclick="switchTab('eq-reference')">📊 Equity Valuation Reference (8 Modules)</button>
        <button class="notes-tab-btn" onclick="switchTab('pm-reference')">💼 Portfolio Management (8 Modules)</button>
      </div>

      <div class="fsa-ref-container">
        __FI_REFERENCE_CONTENT__
      </div>
    </section>

    <!-- 15. EQUITY INVESTMENTS REFERENCE NOTES -->
    <section id="eq-reference">
      <div class="notes-subject-tabs">
        <button class="notes-tab-btn" onclick="switchTab('fsa-reference')">📖 Financial Statement Analysis (20 Modules)</button>
        <button class="notes-tab-btn" onclick="switchTab('fi-reference')">📈 Fixed Income Master Notes (8 Modules)</button>
        <button class="notes-tab-btn active" onclick="switchTab('eq-reference')">📊 Equity Valuation Reference (8 Modules)</button>
        <button class="notes-tab-btn" onclick="switchTab('pm-reference')">💼 Portfolio Management (8 Modules)</button>
      </div>

      <div class="fsa-ref-container">
        __EQ_REFERENCE_CONTENT__
      </div>
    </section>

    <!-- 16. PORTFOLIO MANAGEMENT REFERENCE NOTES -->
    <section id="pm-reference">
      <div class="notes-subject-tabs">
        <button class="notes-tab-btn" onclick="switchTab('fsa-reference')">📖 Financial Statement Analysis (20 Modules)</button>
        <button class="notes-tab-btn" onclick="switchTab('fi-reference')">📈 Fixed Income Master Notes (8 Modules)</button>
        <button class="notes-tab-btn" onclick="switchTab('eq-reference')">📊 Equity Valuation Reference (8 Modules)</button>
        <button class="notes-tab-btn active" onclick="switchTab('pm-reference')">💼 Portfolio Management (8 Modules)</button>
      </div>

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
        'overview': 'Curriculum Overview & Analytics',
        'l1-practice': 'Level 1 Question Bank (425 Questions)',
        'l2-vignettes': 'Level 2 Case Vignette Explorer (80 Item Sets)',
        'sim-yield': 'Yield Curve Dynamics Simulator',
        'sim-tree': 'Binomial Interest Rate Tree Engine',
        'sim-equity': 'Equity Valuation: DDM & DuPont Explorer',
        'sim-duration': 'Key Rate Duration Visualizer',
        'sim-frn': 'Floating-Rate Note Pricing Engine',
        'sim-ri-decay': 'Residual Income Persistence Decay',
        'sim-waterfall': 'FCFF → FCFE Cash Flow Waterfall',
        'l1-practice': 'Level 1 Question Bank (545 Questions)',
        'l2-vignettes': 'Level 2 Case Vignette Explorer (102 Item Sets)',
        'sim-translation': 'Foreign Currency Translation Engine',
        'sim-prepayment': 'MBS Prepayment Simulator',
        'sim-frontier': 'Markowitz Mean-Variance Frontier & CAL Optimizer',
        'sim-fundamental-law': 'Grinold\'s Fundamental Law of Active Management',
        'sim-rebalancing': 'Dynamic Rebalancing Corridors & Tolerance Bands',
        'fsa-reference': 'FSA Master Reference Library (20 Modules)',
        'fi-reference': 'Fixed Income Master Reference & Formulas (8 Modules)',
        'eq-reference': 'Equity Valuation Reference Library & Models (8 Modules)',
        'pm-reference': 'Portfolio Management Master Reference & Formulas (8 Modules)',
        'reference-diagrams': 'Visual Frameworks & Cheat Sheets',
        'solved-numericals': 'Master Solved Numericals & Worked Solutions (27 Cases)',
        'curriculum-audit': '2024–2026 CFA Curriculum Completeness Audit & Gaps'
      };

      document.getElementById('topTitle').innerHTML = `<h2>${titles[tabId] || 'CFA Master Suite'}</h2>`;
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
      if (tabId === 'fsa-reference' || tabId === 'fi-reference' || tabId === 'eq-reference' || tabId === 'pm-reference') {
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

    // KaTeX helper
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

    // Telemetry Charts
    let overviewChart = null;
    let accuracyChart = null;

    function initOverviewChart() {
      const ctx = document.getElementById('overviewChart').getContext('2d');
      overviewChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: ['FSA (460 Q)', 'Fixed Income (205 Q)', 'Equity Investments (210 Q)', 'Portfolio Management (210 Q)'],
          datasets: [{
            data: [460, 205, 210, 210],
            backgroundColor: ['#d29922', '#39c5cf', '#3fb950', '#bc8cff'],
            borderColor: '#161b22',
            borderWidth: 2
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { position: 'bottom', labels: { color: '#8b949e', boxWidth: 12 } }
          }
        }
      });
    }

    function initAccuracyChart() {
      const ctx = document.getElementById('accuracyChart').getContext('2d');
      accuracyChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ['FSA', 'Fixed Income', 'Equity', 'Portfolio Mgmt'],
          datasets: [
            { label: 'Correct', data: [0, 0, 0, 0], backgroundColor: '#3fb950' },
            { label: 'Incorrect', data: [0, 0, 0, 0], backgroundColor: '#f85149' }
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
      const subjects = ['Financial Statement Analysis', 'Fixed Income', 'Equity Investments', 'Portfolio Management'];
      const correctBySubj = [0, 0, 0, 0];
      const incorrectBySubj = [0, 0, 0, 0];

      for (const [qid, rec] of Object.entries(answeredQuestions)) {
        const q = questionBank.find(item => item.id === qid);
        if (q) {
          const idx = subjects.indexOf(q.subject);
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

    function isNumericalQuestion(q) {
      const text = (q.question + ' ' + (q.explanation || '')).toLowerCase();
      return text.includes('$$') || text.includes('$$\\') ||
             /\\(frac|sum|times|approx|pm|le|ge|sigma|mu|beta|alpha|rho)\\b/.test(text) ||
             /\b(calculate|computed|compute|equals|equal to|closest to|approximate|percentage|basis points|ratio|variance|standard deviation|duration|sharpe|treynor|holding period)\b/i.test(q.question);
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
      document.getElementById('l1ViewModeBtn').innerText = (l1ViewMode === 'card') ? '📜 Switch to Full List View' : '🗂️ Switch to Card View';
      renderL1Question();
    }

    function renderL1SingleCard(q, idx, total) {
      const isAnswered = answeredQuestions[q.id];
      const subjClass = q.subject === 'Financial Statement Analysis' ? 'badge-fsa' : (q.subject === 'Fixed Income' ? 'badge-fi' : 'badge-eq');

      let optsHtml = '';
      for (const [key, val] of Object.entries(q.options)) {
        let btnClass = 'option-btn';
        if (isAnswered) {
          if (key === q.answer) btnClass += ' correct';
          else if (key === isAnswered.selected) btnClass += ' incorrect';
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
          <div id="expl-${q.id}" class="explanation-box" style="${isAnswered ? 'display: block;' : ''}">
            <div class="explanation-title">Detailed Solution & Derivation:</div>
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
        countBadge.innerText = `Showing All ${currentL1List.length} Questions (List View)`;
        let listHtml = '';
        currentL1List.forEach((q, idx) => {
          listHtml += renderL1SingleCard(q, idx, currentL1List.length);
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
        const shortSubj = v.subject === 'Financial Statement Analysis' ? 'FSA' : (v.subject === 'Equity Investments' ? 'Equity' : (v.subject === 'Fixed Income' ? 'FI' : (v.subject === 'Portfolio Management' ? 'PM' : v.subject)));
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

      const subjClass = v.subject === 'Financial Statement Analysis' ? 'badge-fsa' : (v.subject === 'Fixed Income' ? 'badge-fi' : 'badge-eq');

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
      initFsaNotesCharts();
      updateScoreBadge();
      renderMath();
      renderSolvedNumericals();

      // Check URL hash for initial tab or sub-section
      const hash = window.location.hash.replace('#', '');
      if (hash) {
        const sec = document.getElementById(hash);
        if (sec && sec.tagName === 'SECTION' && sec.parentElement.tagName === 'MAIN') {
          switchTab(hash);
        } else if (sec) {
          if (hash.startsWith('fi-')) {
            switchTab('fi-reference');
          } else if (hash.startsWith('eq-')) {
            switchTab('eq-reference');
          } else if (hash.startsWith('pm-')) {
            switchTab('pm-reference');
          } else {
            switchTab('fsa-reference');
          }
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
            switchTab('fsa-reference');
            setTimeout(() => {
              target.scrollIntoView({ behavior: 'smooth' });
            }, 100);
          }
        }
      });
    });

    // Embedded Master Solved Numericals Bank
    const masterSolvedNumericals = [{"id": "NUM-3.1.1", "num_code": "3.1.1", "subject": "Financial Statement Analysis", "difficulty": "Easy / Foundational", "problem": "Apex Corp reported net income of 1,200,000 USD for the fiscal year ended December 31, 2025. On January 1, 2025, Apex had 500,000 common shares outstanding. On May 1, 2025, Apex issued 120,000 additional common shares. Apex paid 100,000 USD in preferred dividends on its non-convertible cumulative preferred stock. Calculate Apex Corp's Basic EPS.", "methodology": "`Weighted Average Shares Outstanding (WASO) = sum(Shares_i * (Months_i / 12))`  \n`Basic EPS = (Net Income - Preferred Dividends) / WASO`", "steps": "1. Calculate WASO:\n   - Initial shares: `500,000 * (12 / 12) = 500,000`\n   - New shares issued May 1 (outstanding for 8 months): `120,000 * (8 / 12) = 80,000`\n   - `WASO = 500,000 + 80,000 = 580,000 shares`\n2. Earnings Available to Common Shareholders:\n   - `Net Income - Preferred Dividends = 1,200,000 USD - 100,000 USD = 1,100,000 USD`\n3. Basic EPS:\n   - `Basic EPS = 1,100,000 USD / 580,000 = 1.8966 USD` (rounded to 1.90 USD per share).", "final_answer": "**1.90 USD per share**.  \n*Exam Trap Warning*: Cumulative preferred dividends must be subtracted from Net Income whether declared/paid or not!"}, {"id": "NUM-3.1.2", "num_code": "3.1.2", "subject": "Financial Statement Analysis", "difficulty": "Moderate / Intermediate", "problem": "Sigma Holdings reported net income of 4,500,000 USD for 2025 with 1,000,000 common shares outstanding throughout the year. The company had two potentially dilutive securities outstanding:\n1. 50,000 shares of 6% cumulative convertible preferred stock, par value 100 USD (each preferred share is convertible into 4 common shares).\n2. 200,000 stock options with an exercise price of 30 USD per share. The average market price of common shares during the year was 50 USD.\nThe corporate tax rate is 25%. Calculate Sigma's Diluted EPS.", "methodology": "Treasury Stock Method for Options:\n`Incremental Shares = Options * (1 - (Exercise Price / Average Market Price))`  \nIf-Converted Method for Convertible Preferred:\n`Incremental Earnings = Preferred Dividend saved = Shares_pref * Par * Dividend Rate`  \n`Incremental Shares = Shares_pref * Conversion Ratio`  \nCheck for antidilution: Incremental EPS must be lower than Basic EPS.", "steps": "1. Basic EPS:\n   - Preferred Dividend: `50,000 * 100 USD * 0.06 = 300,000 USD`\n   - Numerator: `4,500,000 USD - 300,000 USD = 4,200,000 USD`\n   - Denominator: `1,000,000 shares`\n   - `Basic EPS = 4,200,000 USD / 1,000,000 = 4.20 USD`\n2. Options Test (Treasury Stock Method):\n   - `Incremental Shares = 200,000 * (1 - (30 / 50)) = 200,000 * 0.40 = 80,000 shares`\n   - Incremental EPS for options = `0 USD / 80,000 = 0.00 USD` (strongly dilutive).\n3. Convertible Preferred Test (If-Converted Method):\n   - Preferred Dividend added back: `+300,000 USD` (no tax effect on dividends).\n   - Incremental Shares: `50,000 * 4 = 200,000 shares`.\n   - Incremental EPS: `300,000 USD / 200,000 = 1.50 USD`.\n   - Since `1.50 USD < 4.20 USD`, the convertible preferred is dilutive.\n4. Total Diluted EPS Calculation:\n   - Diluted Numerator = `4,200,000 USD + 300,000 USD = 4,500,000 USD`\n   - Diluted Denominator = `1,000,000 + 80,000 + 200,000 = 1,280,000 shares`\n   - `Diluted EPS = 4,500,000 USD / 1,280,000 = 3.5156 USD`", "final_answer": "**3.52 USD per share**.  \n*Exam Trap Warning*: Preferred dividends are NOT tax-deductible; do NOT multiply preferred dividends by `(1 - t)` when adding back to the numerator!"}, {"id": "NUM-3.1.3", "num_code": "3.1.3", "subject": "Financial Statement Analysis", "difficulty": "Difficult / Vignette Multi-Step", "problem": "Vanguard Industrial has Net Income of 8,000,000 USD. Throughout 2025, 2,000,000 common shares were outstanding. The marginal tax rate is 21%. During 2025, the following securities were outstanding:\n- 10,000,000 USD face value of 7% convertible bonds issued at par. Each 1,000 USD bond is convertible into 25 common shares.\n- 100,000 shares of 8% cumulative convertible preferred stock, 100 USD par. Each preferred share converts into 2 common shares.\n- 150,000 executive stock warrants with an exercise price of 40 USD. The average common share price was 60 USD.\nDetermine which securities are dilutive by ranking incremental EPS from most to least dilutive, and calculate the final Diluted EPS reported in SEC Form 10-K.", "methodology": "1. Basic EPS benchmark: `(Net Income - Preferred Div) / WASO`\n2. Individual Incremental EPS ranking:\n   - Warrants: `0 USD / Incremental Shares`\n   - Convertible Bonds: `Interest * (1 - t) / Incremental Shares`\n   - Convertible Preferred: `Preferred Dividend / Incremental Shares`\n3. Sequentially incorporate the most dilutive security into the running EPS until incremental EPS exceeds running EPS.", "steps": "1. Basic EPS:\n   - Preferred Dividend: `100,000 * 100 USD * 0.08 = 800,000 USD`\n   - Net Income to Common: `8,000,000 USD - 800,000 USD = 7,200,000 USD`\n   - `Basic EPS = 7,200,000 USD / 2,000,000 = 3.60 USD`\n2. Incremental EPS for each security:\n   - **Warrants**:\n     - Shares = `150,000 * (1 - (40 / 60)) = 150,000 * (1/3) = 50,000 shares`\n     - Incremental EPS = `0 / 50,000 = 0.00 USD` (Rank 1 - Most dilutive).\n   - **Convertible Bonds**:\n     - After-tax interest saved = `10,000,000 USD * 0.07 * (1 - 0.21) = 700,000 USD * 0.79 = 553,000 USD`\n     - Incremental Shares = `(10,000,000 / 1,000) * 25 = 10,000 * 25 = 250,000 shares`\n     - Incremental EPS = `553,000 USD / 250,000 = 2.212 USD` (Rank 2).\n   - **Convertible Preferred**:\n     - Dividend saved = `800,000 USD`\n     - Incremental Shares = `100,000 * 2 = 200,000 shares`\n     - Incremental EPS = `800,000 USD / 200,000 = 4.00 USD` (Rank 3).\n3. Sequential Dilution Inclusion:\n   - **Step 1 (Include Warrants)**:\n     - Numerator: `7,200,000 USD`\n     - Denominator: `2,000,000 + 50,000 = 2,050,000 shares`\n     - Running EPS: `7,200,000 / 2,050,000 = 3.5122 USD`\n   - **Step 2 (Include Convertible Bonds)**:\n     - Incremental EPS (`2.212 USD`) < Running EPS (`3.5122 USD`) -> Dilutive!\n     - Numerator: `7,200,000 USD + 553,000 USD = 7,753,000 USD`\n     - Denominator: `2,050,000 + 250,000 = 2,300,000 shares`\n     - Running EPS: `7,753,000 / 2,300,000 = 3.3709 USD`\n   - **Step 3 (Test Convertible Preferred)**:\n     - Incremental EPS is `4.00 USD`.\n     - Since `4.00 USD > Running EPS (3.3709 USD)`, including the convertible preferred would **increase** EPS back to `(7,753,000 + 800,000) / (2,300,000 + 200,000) = 8,553,000 / 2,500,000 = 3.4212 USD`.\n     - Therefore, the convertible preferred stock is **ANTIDILUTIVE** and must be excluded from Diluted EPS!", "final_answer": "**Diluted EPS = 3.37 USD per share** (Convertible Preferred excluded as antidilutive)."}, {"id": "NUM-3.2.1", "num_code": "3.2.1", "subject": "Financial Statement Analysis", "difficulty": "Easy / Foundational", "problem": "At the beginning of 2025, Global Logistics had a LIFO reserve of 140,000 USD. At the end of 2025, the LIFO reserve was 210,000 USD. For 2025, the company reported Cost of Goods Sold (COGS) under LIFO of 2,800,000 USD. Calculate COGS under FIFO for 2025.", "methodology": "`LIFO Reserve = Inventory_FIFO - Inventory_LIFO`  \n`Change in LIFO Reserve (Delta LIFO Reserve) = Ending LIFO Reserve - Beginning LIFO Reserve`  \n`COGS_FIFO = COGS_LIFO - Delta LIFO Reserve`", "steps": "1. `Delta LIFO Reserve = 210,000 USD - 140,000 USD = +70,000 USD`\n2. `COGS_FIFO = 2,800,000 USD - 70,000 USD = 2,730,000 USD`", "final_answer": "**2,730,000 USD**.  \n*Exam Takeaway*: When prices are rising, FIFO COGS is lower than LIFO COGS by the exact increase in the LIFO Reserve."}, {"id": "NUM-3.2.2", "num_code": "3.2.2", "subject": "Financial Statement Analysis", "difficulty": "Moderate / Intermediate", "problem": "Pacifica Inc. reports under US GAAP and uses LIFO for inventory valuation. For 2025, Pacifica reported:\n- LIFO Ending Inventory: 850,000 USD\n- Beginning LIFO Reserve: 120,000 USD; Ending LIFO Reserve: 195,000 USD\n- LIFO Net Income: 420,000 USD\n- Effective Tax Rate: 25%\n- Total Debt: 1,500,000 USD; Total Equity: 2,000,000 USD\nConvert Pacifica's financial statements to FIFO and compute the adjusted Debt-to-Equity ratio.", "methodology": "`Inventory_FIFO = Inventory_LIFO + Ending LIFO Reserve`  \n`Retained Earnings_FIFO = Retained Earnings_LIFO + [Ending LIFO Reserve * (1 - t)]`  \n`Cash adjustment (Cumulative taxes paid under FIFO) = -[Ending LIFO Reserve * t]`  \n`Equity_FIFO = Equity_LIFO + [Ending LIFO Reserve * (1 - t)]`  \n`Debt-to-Equity_FIFO = Total Debt / Equity_FIFO`", "steps": "1. Adjust Inventory to FIFO:\n   - `Inventory_FIFO = 850,000 USD + 195,000 USD = 1,045,000 USD`\n2. Adjust Equity to FIFO:\n   - Cumulative after-tax addition to Retained Earnings: `195,000 USD * (1 - 0.25) = 195,000 USD * 0.75 = 146,250 USD`\n   - `Equity_FIFO = 2,000,000 USD + 146,250 USD = 2,146,250 USD`\n3. Debt remains unchanged at `1,500,000 USD`.\n4. Calculate Debt-to-Equity:\n   - Original LIFO D/E: `1,500,000 / 2,000,000 = 0.750`\n   - Adjusted FIFO D/E: `1,500,000 / 2,146,250 = 0.6989` (or `69.89%`).", "final_answer": "**FIFO D/E Ratio = 0.70 (or 69.89%)** (leverage decreases under FIFO during rising prices)."}, {"id": "NUM-3.2.3", "num_code": "3.2.3", "subject": "Financial Statement Analysis", "difficulty": "Difficult / LIFO Liquidation", "problem": "Continental Steel experienced a LIFO liquidation in 2025 due to supply chain disruptions. In 2025, Continental sold 100,000 units of steel at 80 USD per unit. During the year, Continental produced only 70,000 units at an average cost of 55 USD per unit. The remaining 30,000 units were liquidated from beginning LIFO inventory base layers, which had an average historical cost of 25 USD per unit. The corporate tax rate is 30%.\nCalculate:\n1. The reported LIFO COGS and Gross Profit.\n2. The pre-tax and after-tax Gross Profit windfall directly attributable to the LIFO liquidation.\n3. The adjusted Gross Profit if Continental had not experienced a LIFO liquidation (i.e., if all 100,000 units sold had been produced at the current cost of 55 USD).", "methodology": "`LIFO COGS = (Current Units Produced * Current Cost) + (Liquidated Units * Historical Cost)`  \n`LIFO Liquidation Pre-Tax Windfall = Liquidated Units * (Current Replacement Cost - Historical Layer Cost)`  \n`After-Tax Windfall = Pre-Tax Windfall * (1 - t)`  \n`Normal (Sustainable) COGS = Total Units Sold * Current Replacement Cost`", "steps": "1. Reported LIFO COGS & Gross Profit:\n   - Cost from current production: `70,000 units * 55 USD = 3,850,000 USD`\n   - Cost from liquidated inventory layers: `30,000 units * 25 USD = 750,000 USD`\n   - `Total Reported LIFO COGS = 3,850,000 USD + 750,000 USD = 4,600,000 USD`\n   - Revenue: `100,000 units * 80 USD = 8,000,000 USD`\n   - `Reported Gross Profit = 8,000,000 USD - 4,600,000 USD = 3,400,000 USD`\n2. LIFO Liquidation Windfall:\n   - Per unit cost distortion: `55 USD (current) - 25 USD (historical) = 30 USD per unit`\n   - `Pre-Tax Windfall = 30,000 units * 30 USD = 900,000 USD`\n   - `After-Tax Windfall = 900,000 USD * (1 - 0.30) = 630,000 USD`\n3. Normalized (Sustainable) Figures:\n   - `Normalized COGS = 100,000 * 55 USD = 5,500,000 USD`\n   - `Normalized Gross Profit = 8,000,000 USD - 5,500,000 USD = 2,500,000 USD`\n   - Notice: `Reported Gross Profit (3,400,000 USD) - Pre-tax Windfall (900,000 USD) = 2,500,000 USD`.", "final_answer": "**Reported Gross Profit = 3,400,000 USD; Pre-tax Liquidation Windfall = 900,000 USD (After-tax = 630,000 USD); Normalized Gross Profit = 2,500,000 USD**."}, {"id": "NUM-3.3.1", "num_code": "3.3.1", "subject": "Financial Statement Analysis", "difficulty": "Easy / Foundational", "problem": "At the start of 2025, Horizon Corp's Defined Benefit Pension Plan had a Projected Benefit Obligation (PBO) of 12,000,000 USD and Plan Assets of 10,500,000 USD. During 2025:\n- Employer contributions paid to the trust: 800,000 USD\n- Actual return on plan assets: 950,000 USD\n- Benefit payments made to retirees: 600,000 USD\nCalculate the fair value of Plan Assets at the end of 2025.", "methodology": "`Ending Plan Assets = Beginning Plan Assets + Actual Return + Employer Contributions - Benefits Paid`", "steps": "`Ending Plan Assets = 10,500,000 USD + 950,000 USD + 800,000 USD - 600,000 USD = 11,650,000 USD`", "final_answer": "**11,650,000 USD**."}, {"id": "NUM-3.3.2", "num_code": "3.3.2", "subject": "Financial Statement Analysis", "difficulty": "Moderate / Intermediate", "problem": "Omega Energy reports pension accounting under IFRS (IAS 19). At the beginning of 2025:\n- Defined Benefit Obligation (DBO) = 25,000,000 EUR\n- Fair Value of Plan Assets = 22,000,000 EUR\n- Net Pension Liability = 3,000,000 EUR\n- Discount rate = 4.0%\nDuring 2025:\n- Current service cost = 1,400,000 EUR\n- Past service cost (plan amendment) = 300,000 EUR\n- Actual return on plan assets = 1,200,000 EUR\n- Actuarial loss from changes in demographic assumptions = 500,000 EUR\nCalculate:\n1. The Net Interest Expense / Income recognized in Profit & Loss (P&L).\n2. The Total Periodic Pension Cost recognized in P&L under IFRS.\n3. The Remeasurement recognized in Other Comprehensive Income (OCI).", "methodology": "Under IFRS (IAS 19):\n`Net Interest Expense = Net Pension Liability (or Asset) * Discount Rate`  \n`P&L Components = Current Service Cost + Past Service Cost + Net Interest Expense`  \n`OCI Remeasurement = Actuarial Gains/Losses - (Actual Return - Expected Return based on discount rate)`  \nwhere `Expected Return = Plan Assets * Discount Rate`.", "steps": "1. Net Interest Expense:\n   - `Net Pension Liability = 25,000,000 EUR - 22,000,000 EUR = 3,000,000 EUR`\n   - `Net Interest Expense = 3,000,000 EUR * 4.0% = 120,000 EUR`\n2. Total Pension Expense in P&L:\n   - Current Service Cost: `1,400,000 EUR`\n   - Past Service Cost (immediately expensed in P&L under IFRS): `300,000 EUR`\n   - Net Interest Expense: `120,000 EUR`\n   - `Total P&L Pension Cost = 1,400,000 EUR + 300,000 EUR + 120,000 EUR = 1,820,000 EUR`\n3. OCI Remeasurements:\n   - Interest income on assets = `22,000,000 EUR * 4.0% = 880,000 EUR`\n   - Asset return remeasurement = `Actual Return (1,200,000 EUR) - Expected Return (880,000 EUR) = +320,000 EUR (gain)`\n   - Actuarial loss on DBO = `-500,000 EUR (loss)`\n   - `Net OCI Remeasurement = -500,000 EUR + 320,000 EUR = -180,000 EUR (net loss in OCI)`", "final_answer": "**P&L Cost = 1,820,000 EUR; Net OCI Loss = 180,000 EUR** (under IFRS, OCI remeasurements are never recycled to P&L)."}, {"id": "NUM-3.3.3", "num_code": "3.3.3", "subject": "Financial Statement Analysis", "difficulty": "Difficult / US GAAP vs. IFRS Reconciliation", "problem": "Using the exact parameters of Omega Energy above, now assume the company reports under US GAAP (ASC 715) with an Expected Long-Term Rate of Return on Plan Assets (ERR) of 6.5%. Unrecognized prior service costs are amortized over a 10-year expected service life at 30,000 EUR per year. The corridor approach applies for actuarial gains/losses (corridor = 10% of the greater of beginning PBO or Plan Assets).\nCalculate:\n1. The Periodic Pension Cost recognized in the Income Statement under US GAAP.\n2. The exact numerical difference between IFRS P&L pension expense and US GAAP Income Statement pension cost, highlighting why analyst adjustments are necessary.", "methodology": "US GAAP Income Statement Periodic Pension Cost:\n`P&L Cost = Service Cost + Interest Cost on PBO - Expected Return on Plan Assets + Amortization of Prior Service Cost + Amortization of Actuarial Loss (if exceeding corridor)`  \n`Interest Cost on PBO = Beginning PBO * Discount Rate`  \n`Expected Return on Assets = Beginning Plan Assets * ERR`", "steps": "1. US GAAP Pension Expense Components:\n   - Current Service Cost: `1,400,000 EUR`\n   - Interest Cost on PBO: `25,000,000 EUR * 4.0% = 1,000,000 EUR`\n   - Expected Return on Plan Assets: `22,000,000 EUR * 6.5% = -1,430,000 EUR`\n   - Amortization of Prior Service Cost: `+30,000 EUR`\n   - Corridor check: `10% of max(25M, 22M) = 2.5M EUR`. Unamortized net actuarial losses (`500,000 - 320,000 = 180,000 EUR`) are well within the 2,500,000 EUR corridor, so amortization is `0 EUR`.\n   - `Total US GAAP P&L Pension Cost = 1,400,000 + 1,000,000 - 1,430,000 + 30,000 = 1,000,000 EUR`\n2. Comparative Analysis:\n   - IFRS P&L Expense: `1,820,000 EUR`\n   - US GAAP P&L Expense: `1,000,000 EUR`\n   - **Variance**: US GAAP reports **820,000 EUR lower operating expense** (higher operating profit).\n   - Drivers:\n     a) Under US GAAP, the full 300,000 EUR prior service cost was capitalized into OCI and amortized at only 30,000 EUR (270,000 EUR difference).\n     b) Under US GAAP, an aggressive expected return on assets (6.5% vs. 4.0% discount rate) suppressed expense by `22,000,000 * (6.5% - 4.0%) = 550,000 EUR`.\n     c) Total variance: `270,000 EUR + 550,000 EUR = 820,000 EUR`.", "final_answer": "**US GAAP Pension Cost = 1,000,000 EUR (820,000 EUR lower than IFRS)**."}, {"id": "NUM-4.1.1", "num_code": "4.1.1", "subject": "Fixed Income", "difficulty": "Easy / Foundational", "problem": "A 1,000 USD par value, 6.0% annual coupon corporate bond matures exactly 4 years from today. The current market yield-to-maturity (YTM) for comparable risk bonds is 5.2% per annum. Calculate the fair price of the bond.", "methodology": "`PV = sum_{t=1}^N [ Coupon / (1 + YTM)^t ] + [ Par / (1 + YTM)^N ]`  \nUsing financial calculator keystrokes:\n`N = 4`, `I/Y = 5.2`, `PMT = 60`, `FV = 1000` -> Solve for `PV`.", "steps": "1. Annual Coupon = `1,000 USD * 0.06 = 60 USD`.\n2. Present Value of Annuity of Coupons:\n   - Year 1: `60 / (1.052)^1 = 57.034 USD`\n   - Year 2: `60 / (1.052)^2 = 54.215 USD`\n   - Year 3: `60 / (1.052)^3 = 51.535 USD`\n   - Year 4: `60 / (1.052)^4 = 48.988 USD`\n   - Sum of Coupons = `211.772 USD`\n3. Present Value of Principal:\n   - `1,000 / (1.052)^4 = 816.467 USD`\n4. Total Bond Price:\n   - `Price = 211.772 USD + 816.467 USD = 1,028.239 USD`", "final_answer": "**1,028.24 USD** (Trading at a premium because Coupon Rate 6.0% > YTM 5.2%)."}, {"id": "NUM-4.1.2", "num_code": "4.1.2", "subject": "Fixed Income", "difficulty": "Moderate / Full Price vs. Flat Price", "problem": "An 8% semi-annual coupon bond with 1,000 USD par value pays coupons on March 15 and September 15. The bond is settled on June 27, 2025. The stated annual YTM on a semi-annual bond basis is 6.5%. The market convention is 30/360.\nThe number of days from the last coupon (March 15) to settlement (June 27) is 102 days. The total number of days in the coupon period is 180 days.\nThere are 8 full semi-annual periods remaining after September 15, 2025 (i.e., total remaining maturity after next coupon is 4 years).\nCalculate:\n1. The Full (Dirty) Price of the bond per 1,000 USD par.\n2. The Accrued Interest (AI).\n3. The Flat (Clean) Price of the bond quoted on dealer screens.", "methodology": "`Fraction of coupon period elapsed (t / T) = 102 / 180 = 0.56667`  \n`Semi-annual coupon (PMT) = (8% * 1,000) / 2 = 40 USD`  \n`Semi-annual yield (r) = 6.5% / 2 = 3.25% (0.0325)`  \n`PV_0 (Value at March 15) = PV of 9 remaining coupons of 40 USD plus 1,000 USD par at 3.25%`  \n`Full Price = PV_0 * (1 + r)^(t / T)`  \n`Accrued Interest (AI) = PMT * (t / T)`  \n`Flat Price = Full Price - Accrued Interest`", "steps": "1. Calculate `PV_0` on previous coupon date (March 15, 9 periods total):\n   - `PV_0 = 40 * [ (1 - (1 + 0.0325)^(-9)) / 0.0325 ] + 1000 * (1 + 0.0325)^(-9)`\n   - Annuity Factor = `(1 - 0.74955) / 0.0325 = 7.70615`\n   - `PV of Coupons = 40 * 7.70615 = 308.246 USD`\n   - `PV of Par = 1000 * 0.74955 = 749.550 USD`\n   - `PV_0 = 308.246 + 749.550 = 1,057.796 USD`\n2. Full (Dirty) Price on settlement date (June 27):\n   - `Full Price = 1,057.796 USD * (1 + 0.0325)^(102 / 180)`\n   - `(1.0325)^0.56667 = 1.01832`\n   - `Full Price = 1,057.796 * 1.01832 = 1,077.174 USD`\n3. Accrued Interest:\n   - `AI = 40 USD * (102 / 180) = 22.667 USD`\n4. Flat (Clean) Price:\n   - `Flat Price = 1,077.174 USD - 22.667 USD = 1,054.507 USD`", "final_answer": "**Full Price = 1,077.17 USD; Accrued Interest = 22.67 USD; Flat Price = 1,054.51 USD**."}, {"id": "NUM-4.1.3", "num_code": "4.1.3", "subject": "Fixed Income", "difficulty": "Difficult / Matrix Pricing Interpolation", "problem": "An illiquid, newly issued 7-year, 5.0% annual coupon corporate bond (Bond X) needs to be priced via matrix pricing. The following liquid benchmark corporate bonds with similar credit ratings are trading in the secondary market:\n- Bond A: 5-year maturity, 4.5% coupon, priced at 101.50 (YTM = 4.161%).\n- Bond B: 5-year maturity, 6.0% coupon, priced at 107.80 (YTM = 4.238%).\n- Bond C: 9-year maturity, 5.2% coupon, priced at 98.20 (YTM = 5.460%).\n- Bond D: 9-year maturity, 4.0% coupon, priced at 89.60 (YTM = 5.520%).\nCalculate:\n1. The estimated 5-year and 9-year benchmark required yields.\n2. The interpolated 7-year required yield for Bond X using linear interpolation.\n3. The estimated matrix price per 100 par for Bond X.", "methodology": "`Benchmark YTM_5 = (YTM_A + YTM_B) / 2`  \n`Benchmark YTM_9 = (YTM_C + YTM_D) / 2`  \n`Linear Interpolation: YTM_7 = YTM_5 + [ (7 - 5) / (9 - 5) ] * (YTM_9 - YTM_5)`  \n`Price = sum_{t=1}^7 [ 5 / (1 + YTM_7)^t ] + [ 100 / (1 + YTM_7)^7 ]`", "steps": "1. Benchmark Average Yields:\n   - `5-Year Average YTM = (4.161% + 4.238%) / 2 = 4.1995%`\n   - `9-Year Average YTM = (5.460% + 5.520%) / 2 = 5.4900%`\n2. Linear Interpolation for 7-Year Maturity:\n   - `Spread = 5.4900% - 4.1995% = 1.2905%`\n   - `Maturity Fraction = (7 - 5) / (9 - 5) = 2 / 4 = 0.50`\n   - `YTM_7 = 4.1995% + (0.50 * 1.2905%) = 4.1995% + 0.64525% = 4.84475% (4.845%)`\n3. Price of Bond X (N = 7, PMT = 5, FV = 100, YTM = 4.84475%):\n   - Annuity factor for 7 years at 4.84475%:\n     `AF = [ 1 - (1.0484475)^(-7) ] / 0.0484475 = (1 - 0.71872) / 0.0484475 = 5.8058`\n   - `PV of Coupons = 5 * 5.8058 = 29.029`\n   - `PV of Par = 100 * 0.71872 = 71.872`\n   - `Price = 29.029 + 71.872 = 100.901`", "final_answer": "**Interpolated YTM = 4.845%; Estimated Matrix Price = 100.90 per 100 par**."}, {"id": "NUM-4.2.1", "num_code": "4.2.1", "subject": "Fixed Income", "difficulty": "Easy / Foundational", "problem": "A portfolio manager holds a 10,000,000 USD par position in a bond trading at 98.50 per 100 par. The bond has a Modified Duration of 6.40 years and an Annualized Convexity of 55.2. Market yields suddenly increase by 75 basis points (0.75%).\nEstimate the percentage and dollar price change of the bond using both duration and convexity.", "methodology": "`Percentage Price Change (% Delta P) = [ -ModDur * Delta Y ] + [ 0.5 * Convexity * (Delta Y)^2 ]`  \n`Dollar Price Change (Delta P_dollar) = % Delta P * Current Portfolio Market Value`", "steps": "1. Duration Effect:\n   - `-ModDur * Delta Y = -6.40 * (+0.0075) = -0.0480 (or -4.80%)`\n2. Convexity Adjustment:\n   - `+0.5 * Convexity * (Delta Y)^2 = 0.5 * 55.2 * (0.0075)^2`\n   - `(0.0075)^2 = 0.00005625`\n   - `0.5 * 55.2 * 0.00005625 = 27.6 * 0.00005625 = +0.0015525 (or +0.15525%)`\n3. Net Percentage Price Change:\n   - `% Delta P = -4.80% + 0.15525% = -4.64475%`\n4. Dollar Price Change:\n   - Current Market Value = `10,000,000 USD * (98.50 / 100) = 9,850,000 USD`\n   - `Dollar Loss = 9,850,000 USD * (-0.0464475) = -457,508 USD`", "final_answer": "**Percentage Price Change = -4.64%; Dollar Value Loss = -457,508 USD**."}, {"id": "NUM-4.2.2", "num_code": "4.2.2", "subject": "Fixed Income", "difficulty": "Moderate / Key Rate Duration & Yield Curve Twists", "problem": "An institutional fixed-income portfolio has a market value of 50,000,000 USD with Key Rate Durations (KRD) distributed across four benchmark maturities:\n- 2-year KRD = 0.85\n- 5-year KRD = 2.10\n- 10-year KRD = 4.25\n- 30-year KRD = 1.60\nTotal Effective Duration = `0.85 + 2.10 + 4.25 + 1.60 = 8.80 years`.\nThe yield curve experiences an asymmetrical steepening twist:\n- 2-year yield decreases by 40 bps (-0.40%)\n- 5-year yield decreases by 10 bps (-0.10%)\n- 10-year yield increases by 25 bps (+0.25%)\n- 30-year yield increases by 60 bps (+0.60%)\nCalculate:\n1. The contribution of each key rate bucket to portfolio return.\n2. The total expected percentage change in portfolio market value.\n3. The difference between the actual KRD-based return and the naive return obtained using single effective duration with the average curve shift (+8.75 bps).", "methodology": "`Portfolio % Delta P = -sum(KRD_k * Delta Y_k)`", "steps": "1. Individual Bucket Contributions:\n   - 2-Year Bucket: `-0.85 * (-0.0040) = +0.00340 (or +0.340%)`\n   - 5-Year Bucket: `-2.10 * (-0.0010) = +0.00210 (or +0.210%)`\n   - 10-Year Bucket: `-4.25 * (+0.0025) = -0.010625 (or -1.0625%)`\n   - 30-Year Bucket: `-1.60 * (+0.0060) = -0.00960 (or -0.960%)`\n2. Total Portfolio % Change:\n   - `% Delta P = +0.340% + 0.210% - 1.0625% - 0.960% = -1.4725%`\n   - Total Dollar Impact = `50,000,000 USD * (-0.014725) = -736,250 USD`.\n3. Naive Effective Duration Benchmark:\n   - Average yield change: `(-40 - 10 + 25 + 60) / 4 = +35 / 4 = +8.75 bps (+0.000875)`\n   - Naive estimate: `-8.80 * (+0.000875) = -0.00770 (or -0.770%)`\n   - **Variance**: The naive model underestimates the loss by `0.7025%` (a 351,250 USD forecasting error) because the heaviest portfolio exposure (10-year KRD = 4.25) coincided with substantial yield increases.", "final_answer": "**KRD Portfolio Return = -1.47% (Dollar loss = -736,250 USD); Naive Duration Error = 0.70% (351,250 USD)**."}, {"id": "NUM-4.3.1", "num_code": "4.3.1", "subject": "Fixed Income", "difficulty": "Difficult / Backward Induction for Callable Bond", "problem": "A 2-year, 5.0% annual coupon corporate bond with 100 par value is callable at par (100) at the end of Year 1 (immediately after the Year 1 coupon is paid).\nThe 1-year spot rate today is `r_0 = 3.5%`.\nThe calibrated 1-year forward rates on the binomial tree at Year 1 are:\n- Upper state (higher interest rate): `r_{1,U} = 5.80%`\n- Lower state (lower interest rate): `r_{1,D} = 3.90%`\nThe probability of each state is 0.50.\nCalculate:\n1. The value of an option-free (straight) bond.\n2. The value of the callable bond using backward induction.\n3. The embedded call option value held by the issuer.", "methodology": "`Value at Year 2 = Par + Coupon = 100 + 5 = 105`  \n`Straight Value at Year 1 node = (Par + Coupon) / (1 + r_1)`  \n`Callable Bond Value at Year 1 node = min(Call Price, (Par + Coupon) / (1 + r_1))`  \n`Value at Node 0 = [ 0.5 * (Value_{1,U} + Coupon) + 0.5 * (Value_{1,D} + Coupon) ] / (1 + r_0)`  \n`Call Option Value = Value_{straight} - Value_{callable}`", "steps": "1. Option-Free (Straight) Bond Value:\n   - At Node `1,U`: `V_{1,U} = 105 / (1 + 0.0580) = 99.2439`\n   - At Node `1,D`: `V_{1,D} = 105 / (1 + 0.0390) = 101.0587`\n   - At Node 0:\n     `V_0 = [ 0.5 * (99.2439 + 5) + 0.5 * (101.0587 + 5) ] / (1 + 0.035)`\n     `V_0 = [ 0.5 * 104.2439 + 0.5 * 106.0587 ] / 1.035 = 105.1513 / 1.035 = 101.5955`\n   - `Straight Bond Value = 101.60 per 100 par`.\n2. Callable Bond Value (Call Price = 100):\n   - At Node `1,U`: Unconstrained value is `99.2439`. Since `99.2439 <= 100`, the issuer will **not call**. Node value = `99.2439`.\n   - At Node `1,D`: Unconstrained value is `101.0587`. Since `101.0587 > 100`, the issuer **will exercise the call** at 100! Node value = `100.0000`.\n   - At Node 0:\n     `V_{callable,0} = [ 0.5 * (99.2439 + 5) + 0.5 * (100.0000 + 5) ] / (1 + 0.035)`\n     `V_{callable,0} = [ 0.5 * 104.2439 + 0.5 * 105.0000 ] / 1.035 = 104.62195 / 1.035 = 101.0840`\n   - `Callable Bond Value = 101.08 per 100 par`.\n3. Embedded Option Value:\n   - `Option Value = Value_{straight} - Value_{callable} = 101.5955 - 101.0840 = 0.5115 per 100 par`.", "final_answer": "**Straight Bond Value = 101.60; Callable Bond Value = 101.08; Embedded Call Option = 0.51 per 100 par**."}, {"id": "NUM-5.1.1", "num_code": "5.1.1", "subject": "Equity Investments", "difficulty": "Easy / Foundational", "problem": "An investor buys 1,000 shares of TechCorp on margin at 50 USD per share. The initial margin requirement is 40%, and the maintenance margin requirement is 25%.\nCalculate:\n1. The initial equity contributed by the investor and the borrowed margin loan.\n2. The price at which the investor will receive a margin call.", "methodology": "`Total Investment = Shares * Initial Price`  \n`Initial Equity = Total Investment * Initial Margin %`  \n`Margin Loan = Total Investment - Initial Equity`  \n`Margin Call Trigger Price (P_call) = P_0 * [ (1 - Initial Margin %) / (1 - Maintenance Margin %) ]`", "steps": "1. Initial Position:\n   - `Total Investment = 1,000 * 50 USD = 50,000 USD`\n   - `Initial Equity = 50,000 USD * 0.40 = 20,000 USD`\n   - `Margin Loan = 50,000 USD - 20,000 USD = 30,000 USD`\n2. Margin Call Trigger Price:\n   - `P_call = 50 USD * [ (1 - 0.40) / (1 - 0.25) ]`\n   - `P_call = 50 USD * (0.60 / 0.75) = 50 USD * 0.80 = 40.00 USD`\n3. Verification:\n   - At 40 USD, Total Value = `1,000 * 40 USD = 40,000 USD`.\n   - Equity = `40,000 USD - 30,000 USD loan = 10,000 USD`.\n   - Equity % = `10,000 USD / 40,000 USD = 25.0%` (exact maintenance threshold).", "final_answer": "**Initial Equity = 20,000 USD; Margin Call Price = 40.00 USD per share**."}, {"id": "NUM-5.1.2", "num_code": "5.1.2", "subject": "Equity Investments", "difficulty": "Moderate / Return on Leveraged Margin Long", "problem": "An investor purchases 500 shares of BioPharm at 80 USD per share using 50% initial margin. The broker charges a call money interest rate of 6.0% per annum on the margin loan. During the 1-year holding period, BioPharm pays a dividend of 2.00 USD per share. At the end of the year, the investor sells the shares at 96 USD per share. The commission paid on purchase is 0.20 USD per share and on sale is 0.20 USD per share.\nCalculate the investor's leveraged return on equity investment.", "methodology": "`Initial Equity = (500 * 80 * 0.50) + (500 * 0.20 commission)`  \n`Margin Loan = 500 * 80 * 0.50`  \n`Interest Paid = Margin Loan * 6.0%`  \n`Total Dividends Received = 500 * 2.00`  \n`Net Sales Proceeds = (500 * 96) - (500 * 0.20 commission) - Margin Loan - Interest Paid`  \n`Leveraged Return = (Net Sales Proceeds + Dividends - Initial Equity) / Initial Equity`", "steps": "1. Initial Outflow:\n   - Share purchase: `500 * 80 USD = 40,000 USD`\n   - Margin Loan: `40,000 USD * 0.50 = 20,000 USD`\n   - Initial Equity invested: `20,000 USD + (500 * 0.20 USD) = 20,100 USD`\n2. Carrying Costs & Dividends:\n   - Margin loan interest: `20,000 USD * 0.06 = 1,200 USD`\n   - Dividends received: `500 * 2.00 USD = +1,000 USD`\n3. Terminal Liquidation Outflow:\n   - Gross sale value: `500 * 96 USD = 48,000 USD`\n   - Selling commission: `500 * 0.20 USD = -100 USD`\n   - Repay margin loan principal: `-20,000 USD`\n   - Repay margin interest: `-1,200 USD`\n   - Cash received at sale: `48,000 - 100 - 20,000 - 1,200 = 26,700 USD`\n4. Net Total Return:\n   - Total Cash Inflow = `26,700 USD + 1,000 USD dividends = 27,700 USD`\n   - Profit = `27,700 USD - 20,100 USD initial equity = 7,600 USD`\n   - `Return on Equity = 7,600 USD / 20,100 USD = 0.3781 (or 37.81%)`\n   - Compare with unleveraged return: `(96 - 80 + 2 - 0.40) / 80.20 = 17.60 / 80.20 = 21.94%`. Leverage increased return by 15.87%!", "final_answer": "**Leveraged Return on Equity = 37.81%**."}, {"id": "NUM-5.2.1", "num_code": "5.2.1", "subject": "Equity Investments", "difficulty": "Easy / Gordon Growth & PVGO", "problem": "Crestline Energy currently earns 6.00 USD per share (EPS_1) and pays out 40% of its earnings as dividends. The required rate of return on equity is 10.0%.\n1. If the sustainable return on equity (ROE) is 15.0%, calculate the intrinsic value per share using the Gordon Growth Model.\n2. Decompose the intrinsic value into the value of assets in place (no-growth value) and the Present Value of Growth Opportunities (PVGO).", "methodology": "`Retention rate (b) = 1 - Dividend Payout Ratio`  \n`Sustainable growth rate (g) = b * ROE`  \n`Expected Dividend (D_1) = EPS_1 * Payout Ratio`  \n`Intrinsic Value (P_0) = D_1 / (r - g)`  \n`No-Growth Value per share = EPS_1 / r`  \n`PVGO = P_0 - (EPS_1 / r)`", "steps": "1. Growth & Dividend:\n   - `Retention rate b = 1 - 0.40 = 0.60`\n   - `g = 0.60 * 15.0% = 9.0% (0.09)`\n   - `D_1 = 6.00 USD * 0.40 = 2.40 USD`\n2. Gordon Growth Model Value:\n   - `P_0 = 2.40 USD / (0.10 - 0.09) = 2.40 USD / 0.01 = 240.00 USD`\n3. PVGO Decomposition:\n   - `No-Growth Value = 6.00 USD / 0.10 = 60.00 USD`\n   - `PVGO = 240.00 USD - 60.00 USD = 180.00 USD`\n   - `PVGO % of Stock Price = 180.00 USD / 240.00 USD = 75.0%`.", "final_answer": "**Intrinsic Value = 240.00 USD; No-Growth Value = 60.00 USD; PVGO = 180.00 USD (75% of firm value)**."}, {"id": "NUM-5.2.2", "num_code": "5.2.2", "subject": "Equity Investments", "difficulty": "Moderate / The H-Model Valuation", "problem": "Apex Semiconductor just paid an annual dividend of `D_0 = 2.50 USD` per share. Due to competitive patent expiration, the current high growth rate of 18.0% (`g_S`) is projected to decline linearly over a transition period of 8 years to a long-term mature sustainable growth rate of 4.0% (`g_L`). The required rate of return for Apex is 9.0%.\nCalculate the intrinsic value per share using the Fuller-Hsia H-Model.", "methodology": "`H = Transition Period (years) / 2`  \n`P_0 = [ D_0 * (1 + g_L) / (r - g_L) ] + [ D_0 * H * (g_S - g_L) / (r - g_L) ]`  \nor equivalently:  \n`P_0 = [ D_0 / (r - g_L) ] * [ (1 + g_L) + H * (g_S - g_L) ]`", "steps": "1. Parameters:\n   - `D_0 = 2.50 USD`\n   - `r = 0.09`\n   - `g_S = 0.18`\n   - `g_L = 0.04`\n   - `Transition period = 8 years -> Half-life H = 8 / 2 = 4 years`\n   - `Denominator = r - g_L = 0.09 - 0.04 = 0.05`\n2. Base Terminal Value Component:\n   - `Base Value = [ 2.50 USD * (1 + 0.04) ] / 0.05 = [ 2.50 * 1.04 ] / 0.05 = 2.60 / 0.05 = 52.00 USD`\n3. High-Growth Linear Transition Premium Component:\n   - `Growth Premium = [ 2.50 USD * 4 * (0.18 - 0.04) ] / 0.05`\n   - `2.50 * 4 = 10.00`\n   - `10.00 * 0.14 = 1.40 USD`\n   - `Growth Premium = 1.40 USD / 0.05 = 28.00 USD`\n4. Total H-Model Value:\n   - `P_0 = 52.00 USD + 28.00 USD = 80.00 USD per share`.", "final_answer": "**Intrinsic Value = 80.00 USD per share** (Base value = 52.00 USD, Linear transition excess value = 28.00 USD)."}, {"id": "NUM-5.2.3", "num_code": "5.2.3", "subject": "Equity Investments", "difficulty": "Difficult / Reverse-Solving H-Model for Implied Return", "problem": "NovaTech stock currently trades in the market at `P_0 = 65.00 USD`. The company just paid a dividend of `D_0 = 1.80 USD`. Equity research consensus projects an initial extraordinary growth rate of `g_S = 16.0%`, declining linearly over a 6-year transition period to a perpetual growth rate of `g_L = 4.5%`.\nAn analyst wants to determine the market-implied required rate of return (`r`) embedded in NovaTech's current market price. Calculate `r`.", "methodology": "Rearranging the H-Model equation for `r`:\n`P_0 * (r - g_L) = D_0 * [ (1 + g_L) + H * (g_S - g_L) ]`  \n`r = g_L + [ (D_0 / P_0) * [ (1 + g_L) + H * (g_S - g_L) ] ]`", "steps": "1. Parameters:\n   - `P_0 = 65.00 USD`\n   - `D_0 = 1.80 USD`\n   - `g_S = 0.16`\n   - `g_L = 0.045`\n   - `Transition period = 6 years -> H = 6 / 2 = 3`\n2. Calculate the dividend adjustment factor:\n   - `Base factor = 1 + g_L = 1 + 0.045 = 1.045`\n   - `Excess growth factor = H * (g_S - g_L) = 3 * (0.16 - 0.045) = 3 * 0.115 = 0.345`\n   - `Total multiplier = 1.045 + 0.345 = 1.390`\n3. Solve for `r`:\n   - `Effective Adjusted Dividend = 1.80 USD * 1.390 = 2.502 USD`\n   - `Spread over g_L = 2.502 USD / 65.00 USD = 0.038492 (or 3.849%)`\n   - `r = g_L + 3.849% = 4.50% + 3.849% = 8.349% (8.35%)`", "final_answer": "**Market-Implied Required Rate of Return r = 8.35%**."}, {"id": "NUM-5.3.1", "num_code": "5.3.1", "subject": "Equity Investments", "difficulty": "Difficult / Comprehensive FCFF to FCFE Reconciliation", "problem": "Zeta Corp reported the following financial statement figures for fiscal year 2025:\n- Net Income = 450,000 USD\n- Non-Cash Charges (Depreciation & Amortization) = 180,000 USD\n- Capital Expenditures (FCInv) = 220,000 USD\n- Increase in Working Capital (WCInv) = 45,000 USD\n- Interest Expense = 80,000 USD\n- Corporate Tax Rate = 25%\n- Long-term debt issued during year = 120,000 USD\n- Long-term debt retired during year = 50,000 USD\n- Target Debt-to-Capital Ratio = 35%\nCalculate:\n1. Free Cash Flow to the Firm (FCFF) starting from Net Income.\n2. Free Cash Flow to Equity (FCFE) starting from FCFF.\n3. Verify FCFE starting directly from Net Income.", "methodology": "`FCFF = Net Income + Non-Cash Charges + [ Interest * (1 - t) ] - FCInv - WCInv`  \n`Net Borrowing = Debt Issued - Debt Repaid`  \n`FCFE = FCFF - [ Interest * (1 - t) ] + Net Borrowing`  \n`Direct FCFE = Net Income + Non-Cash Charges - FCInv - WCInv + Net Borrowing`", "steps": "1. Calculate FCFF:\n   - `Net Income = 450,000 USD`\n   - `+ Non-Cash Charges = +180,000 USD`\n   - `+ After-tax Interest = 80,000 USD * (1 - 0.25) = +60,000 USD`\n   - `- Fixed Capital Investment (FCInv) = -220,000 USD`\n   - `- Working Capital Investment (WCInv) = -45,000 USD`\n   - `FCFF = 450,000 + 180,000 + 60,000 - 220,000 - 45,000 = 425,000 USD`\n2. Calculate FCFE from FCFF:\n   - `Net Borrowing = 120,000 USD (issued) - 50,000 USD (retired) = +70,000 USD`\n   - `FCFE = 425,000 USD - 60,000 USD (after-tax interest) + 70,000 USD (net borrowing)`\n   - `FCFE = 435,000 USD`\n3. Direct Verification:\n   - `Direct FCFE = 450,000 (NI) + 180,000 (NCC) - 220,000 (FCInv) - 45,000 (WCInv) + 70,000 (Net Borrowing)`\n   - `Direct FCFE = 630,000 - 265,000 + 70,000 = 435,000 USD` (Exact reconciliation verified).", "final_answer": "**FCFF = 425,000 USD; FCFE = 435,000 USD**."}, {"id": "NUM-6.1.1", "num_code": "6.1.1", "subject": "Portfolio Management", "difficulty": "Easy / MWR vs. TWR", "problem": "An investor opens a brokerage account on January 1, 2025:\n- Jan 1, 2025: Deposits 100,000 USD and purchases shares.\n- June 30, 2025: Portfolio value is 120,000 USD (prior to deposit). Investor deposits an additional 50,000 USD cash (new total value = 170,000 USD).\n- Dec 31, 2025: Portfolio value is 153,000 USD.\nCalculate:\n1. The Time-Weighted Return (TWR) for 2025.\n2. The Money-Weighted Return (MWR / IRR) for 2025.\n3. Explain which metric accurately evaluates the manager's investment performance.", "methodology": "`HPR_1 = (End Value_1 - Beginning Value_1) / Beginning Value_1`  \n`HPR_2 = (End Value_2 - (Beginning Value_2 + Deposit)) / (Beginning Value_2 + Deposit)`  \n`1 + TWR = (1 + HPR_1) * (1 + HPR_2)`  \n`MWR (IRR): PV(Outflows) = PV(Inflows)`  \n`100,000 USD + [ 50,000 USD / (1 + r)^0.5 ] = 153,000 USD / (1 + r)`", "steps": "1. Time-Weighted Return (TWR):\n   - Period 1 (Jan 1 to June 30):\n     `HPR_1 = (120,000 - 100,000) / 100,000 = +20.0% (+0.20)`\n   - Period 2 (June 30 to Dec 31):\n     Portfolio starting base = `120,000 + 50,000 = 170,000 USD`\n     `HPR_2 = (153,000 - 170,000) / 170,000 = -17,000 / 170,000 = -10.0% (-0.10)`\n   - Full Year TWR:\n     `1 + TWR = (1 + 0.20) * (1 - 0.10) = 1.20 * 0.90 = 1.080`\n     `TWR = +8.0% (0.08)`\n2. Money-Weighted Return (MWR / IRR):\n   - Cash Flow 0 (Jan 1): `-100,000 USD`\n   - Cash Flow 0.5 (June 30): `-50,000 USD`\n   - Cash Flow 1.0 (Dec 31): `+153,000 USD`\n   - Set up semi-annual discount equation:\n     `100,000 + [ 50,000 / (1 + r_{semi}) ] = 153,000 / (1 + r_{semi})^2`\n     Let `x = 1 / (1 + r_{semi})`:\n     `153,000 * x^2 - 50,000 * x - 100,000 = 0`\n     Divide by 1,000: `153 * x^2 - 50 * x - 100 = 0`\n     Using quadratic formula:\n     `x = [ 50 + sqrt((-50)^2 - 4 * 153 * (-100)) ] / (2 * 153)`\n     `sqrt(2500 + 61,200) = sqrt(63,700) = 252.388`\n     `x = (50 + 252.388) / 306 = 302.388 / 306 = 0.98820`\n     `1 + r_{semi} = 1 / 0.98820 = 1.01194 -> r_{semi} = 1.194%`\n     Annualized compounded MWR = `(1 + 0.01194)^2 - 1 = 1.0240 - 1 = +2.40%`\n3. Performance Evaluation Context:\n   - `TWR = +8.0%` vs. `MWR = +2.40%`.\n   - The manager generated an 8.0% return on invested assets. The MWR is drastically lower (+2.40%) solely because the **client deposited 50,000 USD right before the market declined 10%**.\n   - Because investment managers typically do not control client cash deposit/withdrawal timing, GIPS mandates **TWR** for evaluating portfolio manager skill!", "final_answer": "**Time-Weighted Return (TWR) = +8.0%; Money-Weighted Return (MWR) = +2.40%**."}, {"id": "NUM-6.1.2", "num_code": "6.1.2", "subject": "Portfolio Management", "difficulty": "Moderate / Three-Asset Portfolio Variance Expansion", "problem": "An institutional endowment allocates its fund across three asset classes:\n- US Large-Cap Equities (Asset 1): Weight `w_1 = 0.50`, Standard Deviation `sigma_1 = 18.0%`\n- Global Developed Bonds (Asset 2): Weight `w_2 = 0.35`, Standard Deviation `sigma_2 = 7.0%`\n- Private Real Estate (Asset 3): Weight `w_3 = 0.15`, Standard Deviation `sigma_3 = 12.0%`\nThe correlation matrix `rho_{i,j}` between the asset classes is:\n- `rho_{1,2} = -0.15` (Equities vs. Bonds)\n- `rho_{1,3} = +0.45` (Equities vs. Real Estate)\n- `rho_{2,3} = +0.05` (Bonds vs. Real Estate)\nCalculate:\n1. The Covariance between each pair of asset classes.\n2. The total Portfolio Variance (`sigma_p^2`) and Portfolio Standard Deviation (`sigma_p`).", "methodology": "`Cov(i, j) = rho_{i, j} * sigma_i * sigma_j`  \n`Portfolio Variance (sigma_p^2) = sum_{i=1}^3 (w_i^2 * sigma_i^2) + 2 * sum_{i < j} (w_i * w_j * Cov(i, j))`", "steps": "1. Pairwise Covariances:\n   - `Cov(1, 2) = -0.15 * 0.18 * 0.07 = -0.001890`\n   - `Cov(1, 3) = +0.45 * 0.18 * 0.12 = +0.009720`\n   - `Cov(2, 3) = +0.05 * 0.07 * 0.12 = +0.000420`\n2. Weighted Individual Variances:\n   - Asset 1: `(0.50)^2 * (0.18)^2 = 0.25 * 0.0324 = 0.008100`\n   - Asset 2: `(0.35)^2 * (0.07)^2 = 0.1225 * 0.0049 = 0.000600`\n   - Asset 3: `(0.15)^2 * (0.12)^2 = 0.0225 * 0.0144 = 0.000324`\n   - `Sum of individual terms = 0.008100 + 0.000600 + 0.000324 = 0.009024`\n3. Weighted Cross-Product Covariances (multiplied by 2):\n   - Term 1,2: `2 * 0.50 * 0.35 * (-0.001890) = 0.35 * (-0.001890) = -0.0006615`\n   - Term 1,3: `2 * 0.50 * 0.15 * (+0.009720) = 0.15 * (+0.009720) = +0.0014580`\n   - Term 2,3: `2 * 0.35 * 0.15 * (+0.000420) = 0.105 * (+0.000420) = +0.0000441`\n   - `Sum of covariance terms = -0.0006615 + 0.0014580 + 0.0000441 = +0.0008406`\n4. Total Portfolio Variance & Volatility:\n   - `sigma_p^2 = 0.009024 + 0.0008406 = 0.0098646`\n   - `sigma_p = sqrt(0.0098646) = 0.09932 (or 9.93%)`\n   - Notice: Weighted average standard deviation = `0.50 * 18% + 0.35 * 7% + 0.15 * 12% = 9.0% + 2.45% + 1.8% = 13.25%`. Diversification reduced portfolio risk from 13.25% to 9.93%!", "final_answer": "**Portfolio Variance = 0.009865; Portfolio Standard Deviation = 9.93%**."}, {"id": "NUM-6.2.1", "num_code": "6.2.1", "subject": "Portfolio Management", "difficulty": "Moderate / Unconstrained Fundamental Law", "problem": "An equity long-only quantitative manager follows an unconstrained stock selection strategy (`Transfer Coefficient TC = 1.0`):\n- Number of independent stock return forecasts per year (`Breadth BR`) = 400 stocks\n- Information Coefficient per stock forecast (`IC`) = 0.06\n- Benchmark Sharpe Ratio (`SR_B`) = 0.40\n- Benchmark Standard Deviation (`sigma_B`) = 15.0%\nCalculate:\n1. The Information Ratio (IR) of the active manager.\n2. The expected maximum active return (`E(R_A)`) if active risk (`sigma_A`) is budgeted at 4.0%.\n3. The Sharpe Ratio of the actively managed portfolio (`SR_P`).", "methodology": "Grinold's Fundamental Law of Active Management:\n`IR = TC * IC * sqrt(BR)` (where `TC = 1.0` for unconstrained portfolios)  \n`Expected Active Return E(R_A) = IR * sigma_A`  \n`Sharpe Ratio Expansion: SR_P = sqrt(SR_B^2 + IR^2)`", "steps": "1. Information Ratio (IR):\n   - `sqrt(BR) = sqrt(400) = 20`\n   - `IR = 1.0 * 0.06 * 20 = 1.20`\n2. Expected Active Return:\n   - For `sigma_A = 4.0%`:\n   - `E(R_A) = 1.20 * 4.0% = 4.80% (0.048)`\n3. Portfolio Total Sharpe Ratio:\n   - `SR_B^2 = (0.40)^2 = 0.16`\n   - `IR^2 = (1.20)^2 = 1.44`\n   - `SR_P^2 = 0.16 + 1.44 = 1.60`\n   - `SR_P = sqrt(1.60) = 1.2649 (1.26)`", "final_answer": "**Information Ratio IR = 1.20; Expected Active Return = 4.80%; Portfolio Sharpe Ratio = 1.26**."}, {"id": "NUM-6.2.2", "num_code": "6.2.2", "subject": "Portfolio Management", "difficulty": "Difficult / Constrained Fundamental Law & Optimal Active Risk", "problem": "A real-world portfolio manager is subject to long-only constraints, sector neutrality caps, and turnover limits, resulting in a Transfer Coefficient `TC = 0.65`.\nThe manager covers an investment universe of `BR = 196` independent decisions per year with skill `IC = 0.08`.\nThe benchmark Sharpe Ratio is `SR_B = 0.45`.\nCalculate:\n1. The constrained Information Ratio (`IR_constrained`).\n2. The optimal active risk (`sigma_A^*`) the manager should target if the benchmark volatility `sigma_B = 16.0%`.\n3. The resulting total portfolio Sharpe Ratio (`SR_P`).", "methodology": "`IR_constrained = TC * IC * sqrt(BR)`  \n`Optimal Active Risk sigma_A^* = (IR / SR_B) * sigma_B * TC` (or `sigma_A^* = (IR_constrained / SR_B) * sigma_B`)  \n`SR_P = sqrt(SR_B^2 + IR_constrained^2)`", "steps": "1. Constrained Information Ratio:\n   - `sqrt(BR) = sqrt(196) = 14`\n   - Unconstrained IR = `0.08 * 14 = 1.12`\n   - `IR_constrained = 0.65 * 1.12 = 0.728`\n2. Optimal Active Risk:\n   - `sigma_A^* = (IR_constrained / SR_B) * sigma_B`\n   - `sigma_A^* = (0.728 / 0.45) * 16.0% = 1.6178 * 16.0% = 25.88%`\n   - Note: If constrained active risk is capped by the investment mandate (e.g., at `sigma_A = 5.0%`), expected active return would be:\n     `E(R_A) = IR_constrained * sigma_A = 0.728 * 5.0% = 3.64%`.\n3. Constrained Sharpe Ratio Expansion:\n   - `SR_P = sqrt((0.45)^2 + (0.728)^2) = sqrt(0.2025 + 0.52998) = sqrt(0.73248) = 0.8558 (0.86)`", "final_answer": "**Constrained IR = 0.73; Optimal Active Risk = 25.88%; Portfolio Sharpe Ratio = 0.86**."}, {"id": "NUM-6.3.1", "num_code": "6.3.1", "subject": "Portfolio Management", "difficulty": "Difficult / Perold 4-Component Implementation Shortfall", "problem": "A portfolio manager decides to buy 50,000 shares of Meridian Tech.\n- **Decision Date (Monday 9:30 AM)**: Benchmark Decision Price = `50.00 USD`.\n- Order is released to the trading desk at 11:00 AM when the market price is `50.60 USD` (Arrival Price).\n- **Execution Day 1 (Monday)**: Desk buys 30,000 shares at an average execution price of `51.20 USD`. Explicit commission is `0.05 USD` per share.\n- Monday closing price is `51.50 USD`.\n- **Execution Day 2 (Tuesday)**: Desk buys 12,000 shares at an average execution price of `52.10 USD`. Explicit commission is `0.05 USD` per share.\n- Tuesday closing price is `52.80 USD`.\n- **Cancellation**: The manager cancels the remaining 8,000 shares on Tuesday afternoon as the price has run away.\nCalculate the total Implementation Shortfall in dollars and basis points, and decompose it into its 4 distinct components:\n1. Explicit Fees (Commissions)\n2. Execution Cost (Delay / Market Impact on filled shares relative to Arrival Price)\n3. Delay Cost (Slippage from decision time to order release time)\n4. Opportunity Cost (Cost of unfilled / cancelled shares)", "methodology": "`Paper Portfolio Return = Total Target Shares * (Closing Price - Decision Price)`  \n`Actual Portfolio Return = sum(Executed Shares_d * Closing Price) - sum(Executed Shares_d * Execution Price_d) - Total Commissions`  \n`Total Implementation Shortfall (IS) = Paper Return - Actual Return`  \nComponent Breakdown:\n1. `Explicit Costs = sum(Executed Shares_d * Commission_per_share)`\n2. `Delay Cost = Total Executed Shares * (Arrival Price - Decision Price)`\n3. `Realized Execution Cost = sum(Executed Shares_d * (Execution Price_d - Arrival Price))`\n4. `Opportunity Cost (Unfilled) = Unfilled Shares * (Final Cancellation Price - Decision Price)`", "steps": "1. Total Target Shares = `50,000`; Decision Price = `50.00 USD`.\n   - Total base capital = `50,000 * 50.00 USD = 2,500,000 USD`.\n2. Total Executed Shares = `30,000 + 12,000 = 42,000 shares`.\n   - Unfilled Shares = `50,000 - 42,000 = 8,000 shares`.\n3. Component Calculations:\n   - **Component 1: Explicit Costs**:\n     - `42,000 shares * 0.05 USD = 2,100 USD` (or `2,100 / 2,500,000 = 8.4 bps`).\n   - **Component 2: Delay Cost (Between Decision Price 50.00 and Arrival Price 50.60)**:\n     - `Executed Shares * (Arrival Price - Decision Price)`\n     - `42,000 * (50.60 USD - 50.00 USD) = 42,000 * 0.60 USD = 25,200 USD` (or `25,200 / 2,500,000 = 100.8 bps`).\n   - **Component 3: Realized Execution Cost (Market Impact above Arrival Price 50.60)**:\n     - Day 1: `30,000 * (51.20 USD - 50.60 USD) = 30,000 * 0.60 USD = 18,000 USD`\n     - Day 2: `12,000 * (52.10 USD - 50.60 USD) = 12,000 * 1.50 USD = 18,000 USD`\n     - `Total Execution Cost = 18,000 USD + 18,000 USD = 36,000 USD` (or `36,000 / 2,500,000 = 144.0 bps`).\n   - **Component 4: Opportunity Cost (Unfilled Shares 8,000)**:\n     - Final Benchmark Price at cancellation (Tuesday close) = `52.80 USD`.\n     - `8,000 shares * (52.80 USD - 50.00 USD) = 8,000 * 2.80 USD = 22,400 USD` (or `22,400 / 2,500,000 = 89.6 bps`).\n4. Total Implementation Shortfall Reconciliation:\n   - `Total IS = 2,100 USD (Explicit) + 25,200 USD (Delay) + 36,000 USD (Execution) + 22,400 USD (Opportunity)`\n   - `Total IS = 85,700 USD`\n   - In basis points: `85,700 USD / 2,500,000 USD = 0.03428 (or 342.8 bps)`.\n   - Verification via Paper Portfolio:\n     - Paper Profit = `50,000 * (52.80 - 50.00) = 140,000 USD`.\n     - Actual Profit = `(42,000 * 52.80) - (30,000 * 51.20) - (12,000 * 52.10) - 2,100`\n     - Actual Profit = `2,217,600 - 1,536,000 - 625,200 - 2,100 = 54,300 USD`.\n     - `Shortfall = Paper Profit (140,000 USD) - Actual Profit (54,300 USD) = 85,700 USD` (Reconciliation matches down to the dollar!).", "final_answer": "**Total Implementation Shortfall = 85,700 USD (342.8 bps)**:\n- **Explicit Commissions**: 2,100 USD (8.4 bps)\n- **Delay Cost**: 25,200 USD (100.8 bps)\n- **Realized Execution Cost**: 36,000 USD (144.0 bps)\n- **Opportunity Cost**: 22,400 USD (89.6 bps)."}, {"id": "NUM-6.4.1", "num_code": "6.4.1", "subject": "Portfolio Management", "difficulty": "Difficult / Sector Allocation vs. Stock Selection", "problem": "An active equity portfolio and its benchmark have returns and weights across three sectors over a quarterly evaluation period:\n\n| Sector | Portfolio Weight (`w_i`) | Benchmark Weight (`W_i`) | Portfolio Return (`R_i`) | Benchmark Return (`B_i`) |\n| :--- | :---: | :---: | :---: | :---: |\n| Technology | 45.0% | 30.0% | 14.0% | 12.0% |\n| Financials | 25.0% | 35.0% | 6.0% | 5.0% |\n| Healthcare | 30.0% | 35.0% | -2.0% | 1.0% |\n| **Total / Benchmark** | **100.0%** | **100.0%** | — | — |\n\nCalculate:\n1. The total return of the benchmark (`R_B`) and the portfolio (`R_P`).\n2. The Active Return (`R_P - R_B`).\n3. Decompose the Active Return using the **Brinson-Fachler model** into:\n   - Sector Allocation Effect\n   - Within-Sector Selection Effect\n   - Interaction Effect.", "methodology": "`Benchmark Return R_B = sum(W_i * B_i)`  \n`Portfolio Return R_P = sum(w_i * R_i)`  \nBrinson-Fachler Attribution Formulas:\n`Allocation Effect (A_i) = (w_i - W_i) * (B_i - R_B)`  \n`Selection Effect (S_i) = W_i * (R_i - B_i)`  \n`Interaction Effect (I_i) = (w_i - W_i) * (R_i - B_i)`  \n`Active Return = sum(A_i) + sum(S_i) + sum(I_i)`", "steps": "1. Portfolio and Benchmark Total Returns:\n   - Benchmark: `(0.30 * 12%) + (0.35 * 5%) + (0.35 * 1%) = 3.60% + 1.75% + 0.35% = 5.70% (0.057)`\n   - Portfolio: `(0.45 * 14%) + (0.25 * 6%) + (0.30 * -2%) = 6.30% + 1.50% - 0.60% = 7.20% (0.072)`\n   - `Active Return = 7.20% - 5.70% = +1.50% (+0.0150 or +150 bps)`\n2. Allocation Effect (Brinson-Fachler: Evaluates over/underweighting relative to overall benchmark return `R_B = 5.70%`):\n   - Tech: `(0.45 - 0.30) * (12.0% - 5.70%) = +0.15 * (+6.30%) = +0.9450% (+94.5 bps)`\n   - Financials: `(0.25 - 0.35) * (5.0% - 5.70%) = -0.10 * (-0.70%) = +0.0700% (+7.0 bps)`\n   - Healthcare: `(0.30 - 0.35) * (1.0% - 5.70%) = -0.05 * (-4.70%) = +0.2350% (+23.5 bps)`\n   - `Total Allocation Effect = +0.9450% + 0.0700% + 0.2350% = +1.2500% (+125 bps)`\n3. Selection Effect:\n   - Tech: `0.30 * (14.0% - 12.0%) = 0.30 * (+2.0%) = +0.6000% (+60.0 bps)`\n   - Financials: `0.35 * (6.0% - 5.0%) = 0.35 * (+1.0%) = +0.3500% (+35.0 bps)`\n   - Healthcare: `0.35 * (-2.0% - 1.0%) = 0.35 * (-3.0%) = -1.0500% (-105.0 bps)`\n   - `Total Selection Effect = +0.6000% + 0.3500% - 1.0500% = -0.1000% (-10 bps)`\n4. Interaction Effect:\n   - Tech: `(0.45 - 0.30) * (14.0% - 12.0%) = +0.15 * (+2.0%) = +0.3000% (+30.0 bps)`\n   - Financials: `(0.25 - 0.35) * (6.0% - 5.0%) = -0.10 * (+1.0%) = -0.1000% (-10.0 bps)`\n   - Healthcare: `(0.30 - 0.35) * (-2.0% - 1.0%) = -0.05 * (-3.0%) = +0.1500% (+15.0 bps)`\n   - `Total Interaction Effect = +0.3000% - 0.1000% + 0.1500% = +0.3500% (+35 bps)`\n5. Verification:\n   - `Sum = +1.25% (Allocation) - 0.10% (Selection) + 0.35% (Interaction) = +1.50%` (Exact match with active return).", "final_answer": "**Active Return = +150 bps (+1.50%)**:\n- **Allocation Effect**: +125 bps (+1.25%) -> Driven primarily by a strong overweight in outperforming Technology.\n- **Selection Effect**: -10 bps (-0.10%) -> Good tech and bank selection was offset by severe healthcare stock underperformance.\n- **Interaction Effect**: +35 bps (+0.35%)."}];

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
  </script>
</body>
</html>
'''

def generate():
    FI_REF_HTML = os.path.join(DATA_DIR, "fi_reference_extracted.html")
    EQ_REF_HTML = os.path.join(DATA_DIR, "eq_reference_extracted.html")
    PM_REF_HTML = os.path.join(DATA_DIR, "pm_reference_extracted.html")

    assert os.path.exists(MASTER_JSON), f"Missing {MASTER_JSON}. Run compile_unified_suite.py first."
    assert os.path.exists(FSA_REF_HTML), f"Missing {FSA_REF_HTML}. Run extract_fsa_notes.py first."
    assert os.path.exists(FI_REF_HTML), f"Missing {FI_REF_HTML}. Run generate_notes_libraries.py first."
    assert os.path.exists(EQ_REF_HTML), f"Missing {EQ_REF_HTML}. Run generate_notes_libraries.py first."
    assert os.path.exists(PM_REF_HTML), f"Missing {PM_REF_HTML}. Run generate_notes_libraries.py first."

    with open(MASTER_JSON, "r", encoding="utf-8") as f:
        questions = json.load(f)

    with open(FSA_REF_HTML, "r", encoding="utf-8") as f:
        fsa_ref_content = f.read()

    with open(FI_REF_HTML, "r", encoding="utf-8") as f:
        fi_ref_content = f.read()

    with open(EQ_REF_HTML, "r", encoding="utf-8") as f:
        eq_ref_content = f.read()

    with open(PM_REF_HTML, "r", encoding="utf-8") as f:
        pm_ref_content = f.read()

    print(f"Loaded {len(questions)} questions from {MASTER_JSON}")
    print(f"Loaded {len(fsa_ref_content)} characters of FSA reference library")
    print(f"Loaded {len(fi_ref_content)} characters of FI reference library")
    print(f"Loaded {len(eq_ref_content)} characters of EQ reference library")
    print(f"Loaded {len(pm_ref_content)} characters of PM reference library")

    questions_json_str = json.dumps(questions, ensure_ascii=False)

    dashboard_html = dashboard_template.replace("__QUESTION_BANK_DATA__", questions_json_str)
    dashboard_html = dashboard_html.replace("__FSA_REFERENCE_CONTENT__", fsa_ref_content)
    dashboard_html = dashboard_html.replace("__FI_REFERENCE_CONTENT__", fi_ref_content)
    dashboard_html = dashboard_html.replace("__EQ_REFERENCE_CONTENT__", eq_ref_content)
    dashboard_html = dashboard_html.replace("__PM_REFERENCE_CONTENT__", pm_ref_content)

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
