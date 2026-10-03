#!/usr/bin/env python3
"""
generate_unified_dashboard.py
Compiles the complete, unified CFA Master Study Dashboard into index.html
Housing all 855 questions (FSA, Fixed Income, Equity), 9 financial simulations,
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
  
  <meta name="description" content="Unified CFA Program Level 1 & Level 2 Master Exam Preparation Suite. 855 audited questions across Financial Statement Analysis, Fixed Income, and Equity Investments, with 80 case vignettes, 9 simulation engines, and complete 20-chapter reference library.">
  <link rel="canonical" href="https://rahulxcodex.github.io/cfa-master-suite/">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🎓</text></svg>">
  <meta property="og:title" content="CFA Master Study Platform (855 Questions, 9 Sims, 20 Chapters)">
  <meta property="og:description" content="Comprehensive CFA L1 & L2 prep platform: 855 questions, 80 vignettes, 9 simulations, and full 20-chapter FSA notes with KaTeX & Chart.js.">
  <meta property="og:url" content="https://rahulxcodex.github.io/cfa-master-suite/">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  
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
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif;
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
      margin-left: var(--sidebar-width);
      flex-grow: 1;
      padding: 30px 45px;
      max-width: 1400px;
      overflow-y: auto;
      min-height: 100vh;
    }

    .top-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 25px;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 15px;
      gap: 15px;
      flex-wrap: wrap;
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
      font-size: 11px;
      color: var(--text-secondary);
      max-width: 65%;
      text-align: right;
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

    /* Responsive adjustments */
    @media (max-width: 900px) {
      .menu-toggle-btn { display: inline-flex; }
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
      main { margin-left: 0; padding: 20px 16px; }
      .grid-4, .grid-3, .grid-2 { grid-template-columns: 1fr; }
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
        <h1>🎓 CFA Master Platform</h1>
        <p>Unified Exam Suite (855 Questions)</p>
      </div>
      <button class="btn-top" onclick="closeMobileNav()" style="padding: 4px 8px; font-size: 11px; margin-top: 2px;" title="Close Menu">✕</button>
    </div>
    <ul class="nav-links">
      <li><a href="#overview" class="active" onclick="switchTab('overview')"><span>📊 Overview & Telemetry</span></a></li>
      <li><a href="#l1-practice" onclick="switchTab('l1-practice')"><span>📝 Level 1 Question Bank</span> <span class="nav-badge">425 Q</span></a></li>
      <li><a href="#l2-vignettes" onclick="switchTab('l2-vignettes')"><span>📑 Level 2 Case Vignettes</span> <span class="nav-badge">80 V / 430 Q</span></a></li>
      
      <li class="nav-divider"><span>FINANCIAL SIMULATIONS (9)</span></li>
      <li><a href="#sim-yield" onclick="switchTab('sim-yield')"><span>📈 Yield Curve Simulator</span></a></li>
      <li><a href="#sim-tree" onclick="switchTab('sim-tree')"><span>🌳 Binomial Tree Engine</span></a></li>
      <li><a href="#sim-equity" onclick="switchTab('sim-equity')"><span>📊 DDM & DuPont Explorer</span></a></li>
      <li><a href="#sim-duration" onclick="switchTab('sim-duration')"><span>⚡ Key Rate Duration</span></a></li>
      <li><a href="#sim-frn" onclick="switchTab('sim-frn')"><span>🔢 FRN Pricing Engine</span></a></li>
      <li><a href="#sim-ri-decay" onclick="switchTab('sim-ri-decay')"><span>📉 RI Persistence Decay</span></a></li>
      <li><a href="#sim-waterfall" onclick="switchTab('sim-waterfall')"><span>🌊 FCFF→FCFE Waterfall</span></a></li>
      <li><a href="#sim-translation" onclick="switchTab('sim-translation')"><span>💱 Currency Translation</span></a></li>
      <li><a href="#sim-prepayment" onclick="switchTab('sim-prepayment')"><span>🏠 MBS Prepayment Simulator</span></a></li>
      
      <li class="nav-divider"><span>MASTER REFERENCE</span></li>
      <li><a href="#fsa-reference" onclick="switchTab('fsa-reference')"><span>📖 FSA Reference Notes (Ch 1-20)</span></a></li>
      <li><a href="#reference-diagrams" onclick="switchTab('reference-diagrams')"><span>📐 Visual Frameworks</span></a></li>
    </ul>
  </aside>

  <!-- Main Content Container -->
  <main>
    <div class="top-bar">
      <div style="display: flex; align-items: center; gap: 12px;">
        <button class="menu-toggle-btn" id="menuToggleBtn" onclick="toggleMobileNav()" aria-label="Toggle Navigation">☰ Menu</button>
        <div id="topTitle">
          <h2>Curriculum Overview & Analytics</h2>
        </div>
      </div>
      <div class="stats-pills">
        <div class="stat-pill" style="color: var(--accent-blue);">Total: 855 Questions</div>
        <div class="stat-pill" style="color: var(--accent-emerald);">Score: <span id="scoreDisplay">0 / 0 (0%)</span></div>
        <button class="btn-top" onclick="resetScores()">🔄 Reset Score</button>
        <button class="btn-top" onclick="toggleTheme()">🌓 Theme</button>
      </div>
    </div>

    <!-- 1. OVERVIEW & TELEMETRY -->
    <section id="overview" class="active">
      <div class="grid-4" style="margin-bottom: 24px;">
        <div class="card" style="margin-bottom: 0;">
          <div style="font-size: 11px; color: var(--text-secondary); text-transform: uppercase; font-weight: 700;">Financial Statement Analysis</div>
          <div style="font-size: 28px; font-weight: 700; color: var(--accent-amber); margin-top: 5px;">440 Qs</div>
          <div style="font-size: 11.5px; color: var(--text-secondary); margin-top: 4px;">190 L1 MCQs + 250 L2 (44 Vignettes)</div>
        </div>
        <div class="card" style="margin-bottom: 0;">
          <div style="font-size: 11px; color: var(--text-secondary); text-transform: uppercase; font-weight: 700;">Fixed Income</div>
          <div style="font-size: 28px; font-weight: 700; color: var(--accent-cyan); margin-top: 5px;">205 Qs</div>
          <div style="font-size: 11.5px; color: var(--text-secondary); margin-top: 4px;">120 L1 MCQs + 85 L2 (17 Vignettes)</div>
        </div>
        <div class="card" style="margin-bottom: 0;">
          <div style="font-size: 11px; color: var(--text-secondary); text-transform: uppercase; font-weight: 700;">Equity Investments</div>
          <div style="font-size: 28px; font-weight: 700; color: var(--accent-emerald); margin-top: 5px;">210 Qs</div>
          <div style="font-size: 11.5px; color: var(--text-secondary); margin-top: 4px;">115 L1 MCQs + 95 L2 (19 Vignettes)</div>
        </div>
        <div class="card" style="margin-bottom: 0;">
          <div style="font-size: 11px; color: var(--text-secondary); text-transform: uppercase; font-weight: 700;">Total Master Suite</div>
          <div style="font-size: 28px; font-weight: 700; color: var(--accent-blue); margin-top: 5px;">855 Qs</div>
          <div style="font-size: 11.5px; color: var(--text-secondary); margin-top: 4px;">425 L1 + 430 L2 (80 Vignettes) + 9 Sims</div>
        </div>
      </div>

      <div class="grid-2" style="margin-bottom: 24px;">
        <div class="card" style="margin-bottom: 0;">
          <div class="card-title">Curriculum Distribution & Structure</div>
          <canvas id="overviewChart" height="200"></canvas>
        </div>
        <div class="card" style="margin-bottom: 0;">
          <div class="card-title">Candidate Performance Telemetry</div>
          <canvas id="accuracyChart" height="200"></canvas>
        </div>
      </div>

      <div class="card">
        <div class="card-title">Quick Launch Study Portals</div>
        <div class="grid-4">
          <button class="btn" onclick="switchTab('l1-practice')">📝 Start Level 1 Bank (425 Q)</button>
          <button class="btn btn-secondary" onclick="switchTab('l2-vignettes')">📑 Start Level 2 Cases (80 V)</button>
          <button class="btn btn-secondary" onclick="switchTab('sim-yield')">🔬 Open Simulation Lab (9)</button>
          <button class="btn btn-secondary" onclick="switchTab('fsa-reference')">📖 Read FSA Reference (Ch 1-20)</button>
        </div>
      </div>
    </section>

    <!-- 2. LEVEL 1 QUESTION BANK -->
    <section id="l1-practice">
      <div class="card">
        <div class="card-title">Level 1 Multiple-Choice Question Bank (425 Questions)</div>
        <div class="grid-3" style="margin-bottom: 16px;">
          <div class="control-group">
            <label>Filter Subject:</label>
            <select id="l1SubjectSelect" onchange="onL1SubjectChange()">
              <option value="ALL">All Subjects (425 Questions)</option>
              <option value="Financial Statement Analysis">Financial Statement Analysis (190 Qs)</option>
              <option value="Fixed Income">Fixed Income (120 Qs)</option>
              <option value="Equity Investments">Equity Investments (115 Qs)</option>
            </select>
          </div>
          <div class="control-group">
            <label>Filter Topic / Module:</label>
            <select id="l1TopicSelect" onchange="onL1TopicChange()">
              <option value="ALL">All Learning Modules</option>
            </select>
          </div>
          <div class="control-group">
            <label>Search Keyword / LOS:</label>
            <input type="text" id="l1SearchInput" placeholder="e.g. Duration, FIFO, Goodwill, DuPont..." oninput="onL1Search()">
          </div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid var(--border-color); padding-top: 14px; flex-wrap: wrap; gap: 10px;">
          <div style="font-weight: 600; color: var(--accent-blue);" id="l1CountBadge">
            Showing Question 1 of 425
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
        <div class="card-title">Level 2 Vignette & Item-Set Explorer (80 Vignettes / 430 Questions)</div>
        <div class="grid-3" style="margin-bottom: 16px;">
          <div class="control-group">
            <label>Filter Subject:</label>
            <select id="l2SubjectSelect" onchange="onL2SubjectChange()">
              <option value="ALL">All Subjects (80 Vignettes / 430 Qs)</option>
              <option value="Financial Statement Analysis">Financial Statement Analysis (44 Vignettes / 250 Qs)</option>
              <option value="Fixed Income">Fixed Income (17 Vignettes / 85 Qs)</option>
              <option value="Equity Investments">Equity Investments (19 Vignettes / 95 Qs)</option>
            </select>
          </div>
          <div class="control-group">
            <label>Select Case Vignette:</label>
            <select id="l2VignetteSelect" onchange="loadL2Vignette()"></select>
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
            <canvas id="dupontChart" height="200"></canvas>
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
            <canvas id="krdChart" height="220"></canvas>
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
            <canvas id="riChart" height="230"></canvas>
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
            <canvas id="waterfallChart" height="240"></canvas>
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
            <canvas id="prepaymentChart" height="230"></canvas>
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

    <!-- 13. MASTER FSA REFERENCE NOTES -->
    <section id="fsa-reference">
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
  </main>

  <script>
    // Embedded Master Question Bank (855 Questions)
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
        'sim-translation': 'Foreign Currency Translation Engine',
        'sim-prepayment': 'MBS Prepayment Simulator',
        'fsa-reference': 'FSA Master Reference Library',
        'reference-diagrams': 'Visual Frameworks & Cheat Sheets'
      };

      document.getElementById('topTitle').innerHTML = `<h2>${titles[tabId] || 'CFA Master Suite'}</h2>`;
      if (window.location.hash !== '#' + tabId) {
        history.replaceState(null, '', '#' + tabId);
      }
      window.scrollTo({ top: 0, behavior: 'smooth' });
      window.dispatchEvent(new Event('resize'));
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
          labels: ['FSA (440 Q)', 'Fixed Income (205 Q)', 'Equity Investments (210 Q)'],
          datasets: [{
            data: [440, 205, 210],
            backgroundColor: ['#d29922', '#39c5cf', '#3fb950'],
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
          labels: ['FSA', 'Fixed Income', 'Equity'],
          datasets: [
            { label: 'Correct', data: [0, 0, 0], backgroundColor: '#3fb950' },
            { label: 'Incorrect', data: [0, 0, 0], backgroundColor: '#f85149' }
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
      const subjects = ['Financial Statement Analysis', 'Fixed Income', 'Equity Investments'];
      const correctBySubj = [0, 0, 0];
      const incorrectBySubj = [0, 0, 0];

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

    function filterL1Questions() {
      const subj = document.getElementById('l1SubjectSelect').value;
      const topic = document.getElementById('l1TopicSelect').value;
      const search = (document.getElementById('l1SearchInput').value || '').toLowerCase().trim();

      currentL1List = questionBank.filter(q => {
        if (q.level !== 1) return false;
        if (subj !== 'ALL' && q.subject !== subj) return false;
        if (topic !== 'ALL' && (q.module_title !== topic && q.topic !== topic)) return false;
        if (search) {
          const fullText = (q.id + ' ' + q.question + ' ' + (q.los || '') + ' ' + (q.explanation || '')).toLowerCase();
          if (!fullText.includes(search)) return false;
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
        opt.innerText = `[${v.subject.replace('Financial Statement Analysis', 'FSA')}] ${v.id}: ${v.title} (${v.questions.length} Qs)`;
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
    // FSA REFERENCE NOTES CHARTS (6 CHARTS)
    // ==========================================
    function initFsaNotesCharts() {
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
      initFsaNotesCharts();
      updateScoreBadge();
      renderMath();

      // Check URL hash for initial tab or sub-section
      const hash = window.location.hash.replace('#', '');
      if (hash) {
        const sec = document.getElementById(hash);
        if (sec && sec.tagName === 'SECTION' && sec.parentElement.tagName === 'MAIN') {
          switchTab(hash);
        } else if (sec) {
          switchTab('fsa-reference');
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
  </script>
</body>
</html>
'''

def generate():
    assert os.path.exists(MASTER_JSON), f"Missing {MASTER_JSON}. Run compile_unified_suite.py first."
    assert os.path.exists(FSA_REF_HTML), f"Missing {FSA_REF_HTML}. Run extract_fsa_notes.py first."

    with open(MASTER_JSON, "r", encoding="utf-8") as f:
        questions = json.load(f)

    with open(FSA_REF_HTML, "r", encoding="utf-8") as f:
        fsa_ref_content = f.read()

    print(f"Loaded {len(questions)} questions from {MASTER_JSON}")
    print(f"Loaded {len(fsa_ref_content)} characters of FSA reference library")

    questions_json_str = json.dumps(questions, ensure_ascii=False)

    dashboard_html = dashboard_template.replace("__QUESTION_BANK_DATA__", questions_json_str)
    dashboard_html = dashboard_html.replace("__FSA_REFERENCE_CONTENT__", fsa_ref_content)

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
