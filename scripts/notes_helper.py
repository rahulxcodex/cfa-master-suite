"""
HTML formatting helpers for CFA Reference Notes, Worked Numericals, and Interactive Chapter Exercises.
"""
import os
from scripts.qbank_helper import check_text_compliance


def worked_box(title: str, body_html: str, color: str = "emerald") -> str:
    palette = {
        "emerald": ("rgba(16, 185, 129, 0.05)", "var(--accent-emerald)"),
        "blue": ("rgba(59, 130, 246, 0.05)", "var(--accent-blue)"),
        "amber": ("rgba(210, 153, 34, 0.06)", "var(--accent-amber)"),
        "purple": ("rgba(188, 140, 255, 0.06)", "var(--accent-purple)"),
        "cyan": ("rgba(57, 197, 207, 0.06)", "var(--accent-cyan)"),
    }
    bg, border = palette.get(color, palette["emerald"])
    return f"""
  <div class="card" style="background: {bg}; border-left: 4px solid {border}; margin: 16px 0;">
    <h4 style="margin: 0 0 10px 0; color: {border};">{title}</h4>
    {body_html}
  </div>"""


def exercise_card(
    ex_id: str,
    title: str,
    prompt_html: str,
    solution_html: str,
    mode: str = "unsolved",
    badge: str = "Chapter Exercise",
) -> str:
    """Render an interactive Solved or Unsolved (Self-Test) Chapter Exercise card."""
    is_solved = mode.lower() == "solved"
    open_attr = " open" if is_solved else ""
    mode_badge = (
        '<span class="badge-diff-easy" style="font-size:10px;">SOLVED WALKTHROUGH</span>'
        if is_solved
        else '<span class="badge-diff-moderate" style="font-size:10px;">UNSOLVED SELF-TEST</span>'
    )
    summary_label = (
        "Solution &amp; Step-by-Step Ruling (Expanded — Click to Collapse)"
        if is_solved
        else "Click to Reveal Answer, Derivation &amp; Exam Ruling"
    )
    return f"""
  <div class="chapter-exercise-card card" id="{ex_id}" style="margin: 14px 0; border-left: 3px solid var(--accent-cyan); background: var(--bg-tertiary);">
    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px; margin-bottom:8px;">
      <strong style="color:var(--text-primary); font-size:14px;">{title}</strong>
      <div style="display:flex; gap:6px; align-items:center;">
        <span class="nav-badge">{badge}</span>
        {mode_badge}
      </div>
    </div>
    <div style="font-size:13.5px; line-height:1.65; margin-bottom:10px;">{prompt_html}</div>
    <details class="exercise-solution-details"{open_attr} style="border:1px solid var(--border-color); border-radius:6px; padding:8px 12px; background:var(--bg-secondary);">
      <summary style="cursor:pointer; font-weight:600; color:var(--accent-cyan); font-size:12.5px;">{summary_label}</summary>
      <div style="margin-top:10px; font-size:13px; line-height:1.65;">{solution_html}</div>
    </details>
  </div>"""


def exercise_toolbar(section_id: str, label: str = "Chapter Exercises") -> str:
    return f"""
  <div class="exercise-toolbar" style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; margin: 18px 0 10px 0; padding:10px 14px; background:var(--bg-secondary); border:1px solid var(--border-color); border-radius:6px;">
    <span style="font-weight:700; font-size:13.5px; color:var(--accent-amber);">{label}</span>
    <div style="display:flex; gap:8px;">
      <button type="button" class="filter-btn" onclick="toggleChapterExercises('{section_id}', false)">Hide All (Unsolved Mode)</button>
      <button type="button" class="filter-btn" onclick="toggleChapterExercises('{section_id}', true)">Reveal All (Solved Mode)</button>
    </div>
  </div>"""


def write_notes_html(html: str, path: str):
    errs = check_text_compliance(html, os.path.basename(path))
    if errs:
        raise ValueError("\n".join(errs[:15]))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {path} ({len(html)} bytes)")
