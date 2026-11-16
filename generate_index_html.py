import json

# Read the generated workout plan
with open('/home/praveen/personal-projects/workout-tracker/workout_plan.json') as f_plan:
    workout_plan_json = f_plan.read().strip()

html_template = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>45-Day Total Transformation · Muscle & Brain Mastery (Nov 17 – Dec 31, 2026)</title>
  <meta name="description" content="45-Day Total Transformation: 10kg Dumbbells, Progressive Calisthenics, High-IQ Cognitive Mastery, Ending Overthinking & Budget PG Nutrition. Entering Jan 1, 2027 at Full Power." />
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🧠</text></svg>" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet" />

  <style>
    :root {
      --bg: #07090e;
      --card-bg: rgba(15, 23, 42, 0.88);
      --card-border: rgba(255, 255, 255, 0.08);
      --card-hover: rgba(30, 41, 59, 0.95);
      --t1: #f8fafc;
      --t2: #94a3b8;
      --t3: #475569;
      --accent: #f59e0b;
      --accent-glow: rgba(245, 158, 11, 0.28);
      --orange: #f97316;
      --cyan: #06b6d4;
      --emerald: #10b981;
      --emerald-glow: rgba(16, 185, 129, 0.25);
      --purple: #8b5cf6;
      --purple-glow: rgba(139, 92, 246, 0.28);
      --purple-light: #c084fc;
      --red: #ef4444;
      --glass: rgba(255, 255, 255, 0.03);
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background: var(--bg);
      color: var(--t1);
      min-height: 100vh;
      overflow-x: hidden;
      line-height: 1.5;
    }

    body::before {
      content: '';
      position: fixed;
      inset: 0;
      background:
        radial-gradient(ellipse at 15% 10%, rgba(245, 158, 11, 0.08) 0%, transparent 50%),
        radial-gradient(ellipse at 85% 85%, rgba(6, 182, 212, 0.06) 0%, transparent 50%),
        radial-gradient(ellipse at 50% 50%, rgba(139, 92, 246, 0.06) 0%, transparent 60%);
      pointer-events: none;
      z-index: 0;
    }

    .wrap {
      max-width: 1360px;
      margin: 0 auto;
      padding: 0 20px;
      position: relative;
      z-index: 1;
    }

    /* ─── HERO HEADER ─── */
    .hero {
      background: linear-gradient(180deg, rgba(20, 26, 43, 0.95) 0%, rgba(11, 15, 25, 0.98) 100%);
      border-bottom: 1px solid var(--card-border);
      padding: 24px 0 20px;
      position: relative;
    }
    .hero::after {
      content: '';
      position: absolute;
      bottom: 0; left: 0; right: 0; height: 1px;
      background: linear-gradient(90deg, transparent, var(--accent), var(--purple), transparent);
    }

    .hero-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
      margin-bottom: 20px;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .brand-icon {
      width: 48px;
      height: 48px;
      background: linear-gradient(135deg, #f59e0b, #8b5cf6);
      border-radius: 14px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.5rem;
      box-shadow: 0 0 24px var(--purple-glow);
    }
    .brand-text h1 {
      font-size: 1.35rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: #fff;
    }
    .brand-text p {
      font-size: 0.8rem;
      color: var(--t2);
      font-family: 'JetBrains Mono', monospace;
    }

    .hero-actions {
      display: flex;
      gap: 10px;
      align-items: center;
      flex-wrap: wrap;
    }

    .btn {
      padding: 8px 16px;
      border-radius: 8px;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
      text-decoration: none;
      border: 1px solid var(--card-border);
      background: rgba(255, 255, 255, 0.05);
      color: var(--t1);
    }
    .btn:hover {
      background: rgba(255, 255, 255, 0.1);
      border-color: rgba(255, 255, 255, 0.2);
      transform: translateY(-1px);
    }
    .btn-primary {
      background: linear-gradient(135deg, #f59e0b, #ea580c);
      border: none;
      color: #07090e;
      font-weight: 700;
      box-shadow: 0 0 15px rgba(245, 158, 11, 0.35);
    }
    .btn-primary:hover {
      background: linear-gradient(135deg, #fbbf24, #f97316);
      transform: translateY(-1px);
      box-shadow: 0 0 20px rgba(245, 158, 11, 0.5);
    }
    .btn-purple {
      background: rgba(139, 92, 246, 0.15);
      color: #c084fc;
      border-color: rgba(139, 92, 246, 0.35);
    }
    .btn-purple:hover {
      background: rgba(139, 92, 246, 0.25);
    }
    .btn-emerald {
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border-color: rgba(16, 185, 129, 0.3);
    }
    .btn-emerald:hover {
      background: rgba(16, 185, 129, 0.25);
    }

    /* Stats Grid */
    .stats-bar {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
      gap: 12px;
      margin-top: 14px;
    }
    .stat-pill {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 12px 16px;
      backdrop-filter: blur(8px);
      display: flex;
      flex-direction: column;
      gap: 4px;
    }
    .stat-pill .lbl {
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--t2);
      font-weight: 600;
    }
    .stat-pill .val {
      font-size: 1.45rem;
      font-weight: 800;
      font-family: 'JetBrains Mono', monospace;
      color: #fff;
    }
    .stat-pill .sub {
      font-size: 0.7rem;
      color: var(--t3);
    }

    /* Overall Progress Bar */
    .overall-prog-wrap {
      margin-top: 18px;
    }
    .prog-meta {
      display: flex;
      justify-content: space-between;
      font-size: 0.78rem;
      margin-bottom: 6px;
      font-weight: 600;
    }
    .prog-track {
      height: 10px;
      background: rgba(255, 255, 255, 0.06);
      border-radius: 999px;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.08);
      position: relative;
    }
    .prog-fill {
      height: 100%;
      background: linear-gradient(90deg, #f59e0b, #8b5cf6, #10b981, #06b6d4);
      border-radius: 999px;
      width: 0%;
      transition: width 0.4s ease;
      box-shadow: 0 0 14px var(--accent-glow);
    }

    /* ─── TODAY'S FOCUS HERO CARD ─── */
    .today-focus-card {
      background: linear-gradient(135deg, rgba(245, 158, 11, 0.1) 0%, rgba(139, 92, 246, 0.08) 50%, rgba(15, 23, 42, 0.95) 100%);
      border: 1px solid rgba(245, 158, 11, 0.35);
      border-radius: 18px;
      margin: 28px 0;
      padding: 24px;
      box-shadow: 0 0 35px rgba(139, 92, 246, 0.12);
      position: relative;
      overflow: hidden;
    }
    .today-focus-card::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0; height: 3px;
      background: linear-gradient(90deg, #f59e0b, #8b5cf6, #10b981);
    }
    .tf-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 18px;
      padding-bottom: 14px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.07);
    }
    .tf-title {
      font-size: 1.35rem;
      font-weight: 800;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }
    .tf-badges {
      display: flex;
      gap: 8px;
      align-items: center;
      flex-wrap: wrap;
    }
    .badge {
      font-size: 0.72rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 999px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .badge-today {
      background: linear-gradient(135deg, #f59e0b, #ea580c);
      color: #000;
      animation: pulseGlow 2s infinite;
    }
    @keyframes pulseGlow {
      0%, 100% { box-shadow: 0 0 0 0 rgba(245, 158, 11, 0.4); }
      50% { box-shadow: 0 0 0 6px rgba(245, 158, 11, 0); }
    }
    .badge-phase {
      background: rgba(139, 92, 246, 0.2);
      color: #c084fc;
      border: 1px solid rgba(139, 92, 246, 0.35);
    }
    .badge-body {
      background: rgba(6, 182, 212, 0.2);
      color: #38bdf8;
      border: 1px solid rgba(6, 182, 212, 0.35);
    }

    /* Sections inside Day */
    .tf-sections {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }
    @media (max-width: 900px) {
      .tf-sections { grid-template-columns: 1fr; }
    }

    .sec-box {
      background: rgba(10, 15, 28, 0.75);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 16px;
    }
    .sec-title {
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--accent);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .sec-sub {
      font-size: 0.72rem;
      color: var(--t2);
      font-weight: 500;
    }

    /* ─── BRAIN & COGNITIVE MASTERY BOX ─── */
    .brain-box {
      background: linear-gradient(135deg, rgba(139, 92, 246, 0.12) 0%, rgba(30, 27, 75, 0.6) 100%);
      border: 1px solid rgba(139, 92, 246, 0.35);
      border-radius: 14px;
      padding: 16px;
      position: relative;
      margin-top: 14px;
      box-shadow: 0 0 20px rgba(139, 92, 246, 0.08);
    }
    .brain-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
      flex-wrap: wrap;
      gap: 8px;
    }
    .brain-title {
      font-size: 0.92rem;
      font-weight: 800;
      color: #e9d5ff;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .brain-pillar-tag {
      font-size: 0.68rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      background: rgba(168, 85, 247, 0.25);
      color: #d8b4fe;
      border: 1px solid rgba(168, 85, 247, 0.4);
      padding: 3px 8px;
      border-radius: 999px;
    }
    .brain-principle {
      font-size: 0.8rem;
      color: #cbd5e1;
      background: rgba(0, 0, 0, 0.35);
      border-left: 3px solid #a855f7;
      padding: 8px 12px;
      border-radius: 0 8px 8px 0;
      margin-bottom: 10px;
      line-height: 1.45;
    }
    .brain-principle b {
      color: #c084fc;
    }
    .brain-action {
      font-size: 0.8rem;
      color: #e2e8f0;
      background: rgba(168, 85, 247, 0.1);
      border: 1px solid rgba(168, 85, 247, 0.2);
      padding: 8px 12px;
      border-radius: 8px;
      margin-bottom: 12px;
      line-height: 1.45;
    }
    .brain-action b {
      color: #facc15;
    }
    .brain-habits-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 8px;
    }

    /* Checklist Table / Rows */
    .task-item {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      padding: 10px 12px;
      margin-bottom: 8px;
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 10px;
      transition: all 0.15s ease;
    }
    .task-item:hover {
      background: rgba(255, 255, 255, 0.04);
      border-color: rgba(255, 255, 255, 0.1);
    }
    .task-item.done {
      background: rgba(16, 185, 129, 0.08);
      border-color: rgba(16, 185, 129, 0.25);
    }
    .task-item.brain-task.done {
      background: rgba(139, 92, 246, 0.12);
      border-color: rgba(139, 92, 246, 0.35);
    }
    .task-chk {
      appearance: none;
      -webkit-appearance: none;
      width: 20px;
      height: 20px;
      border: 2px solid var(--t3);
      border-radius: 6px;
      cursor: pointer;
      flex-shrink: 0;
      margin-top: 2px;
      position: relative;
      transition: all 0.2s;
    }
    .task-chk:checked {
      background: var(--emerald);
      border-color: var(--emerald);
    }
    .task-chk.brain-chk:checked {
      background: var(--purple);
      border-color: var(--purple);
    }
    .task-chk:checked::after {
      content: '✓';
      position: absolute;
      color: #07090e;
      font-weight: 900;
      font-size: 13px;
      top: 50%; left: 50%;
      transform: translate(-50%, -50%);
    }

    .task-info {
      flex: 1;
    }
    .task-name {
      font-size: 0.85rem;
      font-weight: 600;
      color: #fff;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 6px;
    }
    .task-item.done .task-name {
      text-decoration: line-through;
      color: var(--t2);
    }
    .task-meta {
      font-size: 0.72rem;
      color: var(--t2);
      margin-top: 3px;
      font-family: 'JetBrains Mono', monospace;
    }
    .task-meta span {
      color: #cbd5e1;
      margin-right: 8px;
    }

    .yt-btn {
      font-size: 0.68rem;
      padding: 3px 8px;
      border-radius: 6px;
      background: rgba(239, 68, 68, 0.15);
      color: #f87171;
      border: 1px solid rgba(239, 68, 68, 0.3);
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-weight: 600;
      transition: all 0.15s;
    }
    .yt-btn:hover {
      background: rgba(239, 68, 68, 0.25);
      border-color: #f87171;
      color: #fff;
    }

    /* PG Diet Section */
    .diet-box {
      margin-top: 18px;
      background: rgba(16, 185, 129, 0.05);
      border: 1px solid rgba(16, 185, 129, 0.25);
      border-radius: 14px;
      padding: 16px;
    }
    .diet-header {
      font-size: 0.88rem;
      font-weight: 700;
      color: #34d399;
      margin-bottom: 10px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
    }
    .diet-highlight {
      font-size: 0.78rem;
      font-weight: 600;
      color: #fde047;
      background: rgba(234, 179, 8, 0.12);
      border: 1px solid rgba(234, 179, 8, 0.25);
      padding: 6px 12px;
      border-radius: 8px;
      margin-bottom: 12px;
    }
    .diet-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 10px;
    }
    .diet-card {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--card-border);
      border-radius: 10px;
      padding: 10px;
      font-size: 0.78rem;
    }
    .diet-card b {
      color: #fff;
      display: block;
      margin-bottom: 3px;
      font-size: 0.74rem;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    /* Water Cups Widget */
    .water-row {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-top: 12px;
      flex-wrap: wrap;
    }
    .water-pill {
      font-size: 0.72rem;
      font-weight: 600;
      padding: 5px 12px;
      border-radius: 999px;
      border: 1px solid rgba(6, 182, 212, 0.3);
      background: rgba(6, 182, 212, 0.1);
      color: #38bdf8;
      cursor: pointer;
      transition: all 0.2s;
    }
    .water-pill.checked {
      background: #06b6d4;
      color: #07090e;
      box-shadow: 0 0 10px rgba(6, 182, 212, 0.4);
    }

    /* ─── CONTROLS & FILTER TABS ─── */
    .controls-wrap {
      margin: 24px 0 16px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }
    .filter-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }
    .tabs-group {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--card-border);
      padding: 4px;
      border-radius: 10px;
    }
    .tab-btn {
      padding: 6px 14px;
      font-size: 0.75rem;
      font-weight: 600;
      border-radius: 7px;
      border: none;
      background: transparent;
      color: var(--t2);
      cursor: pointer;
      transition: all 0.15s;
    }
    .tab-btn:hover {
      color: #fff;
      background: rgba(255, 255, 255, 0.06);
    }
    .tab-btn.active {
      background: linear-gradient(135deg, #f59e0b, #ea580c);
      color: #07090e;
      font-weight: 700;
      box-shadow: 0 0 10px rgba(245, 158, 11, 0.3);
    }

    .search-box {
      position: relative;
      min-width: 260px;
    }
    .search-input {
      width: 100%;
      padding: 8px 12px 8px 32px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--card-border);
      border-radius: 8px;
      color: #fff;
      font-size: 0.8rem;
      font-family: inherit;
    }
    .search-input:focus {
      outline: none;
      border-color: var(--accent);
      background: rgba(255, 255, 255, 0.07);
    }
    .search-icon {
      position: absolute;
      left: 10px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 0.8rem;
      color: var(--t3);
      pointer-events: none;
    }

    /* ─── 45 DAYS LIST ─── */
    .days-grid {
      display: flex;
      flex-direction: column;
      gap: 16px;
      margin-bottom: 60px;
    }

    .day-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      overflow: hidden;
      backdrop-filter: blur(12px);
      transition: all 0.2s ease;
    }
    .day-card:hover {
      border-color: rgba(255, 255, 255, 0.16);
    }
    .day-card.today-card {
      border-color: rgba(245, 158, 11, 0.45);
      box-shadow: 0 0 25px rgba(245, 158, 11, 0.1);
    }
    .day-card.completed-card {
      border-color: rgba(16, 185, 129, 0.35);
    }

    .dc-header {
      padding: 16px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      cursor: pointer;
      background: rgba(255, 255, 255, 0.015);
      border-bottom: 1px solid transparent;
      transition: background 0.15s;
    }
    .dc-header:hover {
      background: rgba(255, 255, 255, 0.035);
    }
    .day-card.expanded .dc-header {
      border-bottom-color: var(--card-border);
    }

    .dc-left {
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .dc-day-num {
      font-family: 'JetBrains Mono', monospace;
      font-weight: 800;
      font-size: 1.15rem;
      color: #fff;
    }
    .dc-title-group h3 {
      font-size: 0.95rem;
      font-weight: 700;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }
    .dc-date-str {
      font-size: 0.72rem;
      color: var(--t2);
      font-family: 'JetBrains Mono', monospace;
    }

    .dc-right {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .dc-prog-mini {
      width: 100px;
      height: 6px;
      background: rgba(255, 255, 255, 0.08);
      border-radius: 999px;
      overflow: hidden;
    }
    .dc-prog-mini-fill {
      height: 100%;
      background: linear-gradient(90deg, #f59e0b, #8b5cf6, #10b981);
      width: 0%;
      transition: width 0.3s;
    }
    .dc-pct {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--t2);
      min-width: 38px;
      text-align: right;
    }
    .dc-toggle-icon {
      font-size: 0.8rem;
      color: var(--t2);
      transition: transform 0.2s;
    }
    .day-card.expanded .dc-toggle-icon {
      transform: rotate(180deg);
    }

    .dc-body {
      padding: 20px;
      display: none;
    }
    .day-card.expanded .dc-body {
      display: block;
    }

    /* Note Textarea */
    .note-box {
      margin-top: 14px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .note-box label {
      font-size: 0.72rem;
      font-weight: 600;
      color: var(--t2);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .note-input {
      width: 100%;
      min-height: 55px;
      padding: 8px 12px;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--card-border);
      border-radius: 8px;
      color: #fff;
      font-family: inherit;
      font-size: 0.8rem;
      resize: vertical;
    }
    .note-input:focus {
      outline: none;
      border-color: var(--purple);
    }

    /* ─── MODAL / DRAWER (CURRICULUM & GUIDE) ─── */
    .modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.8);
      backdrop-filter: blur(8px);
      z-index: 100;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }
    .modal-overlay.open {
      display: flex;
    }
    .modal-card {
      background: #0f172a;
      border: 1px solid var(--card-border);
      border-radius: 18px;
      max-width: 860px;
      width: 100%;
      max-height: 85vh;
      overflow-y: auto;
      padding: 26px;
      box-shadow: 0 0 50px rgba(0,0,0,0.8);
      position: relative;
    }
    .modal-close {
      position: absolute;
      top: 18px; right: 18px;
      background: rgba(255, 255, 255, 0.08);
      border: none;
      color: #fff;
      width: 32px; height: 32px;
      border-radius: 8px;
      cursor: pointer;
      font-size: 1rem;
      font-weight: 700;
    }
    .modal-card h2 {
      font-size: 1.35rem;
      color: #fff;
      margin-bottom: 12px;
    }
    .modal-card h3 {
      font-size: 1.05rem;
      color: var(--accent);
      margin: 20px 0 8px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 6px;
    }
    .modal-card h3.purple-head {
      color: #c084fc;
    }
    .modal-card p, .modal-card li {
      font-size: 0.84rem;
      color: var(--t2);
      line-height: 1.6;
    }
    .modal-card ul {
      margin-left: 20px;
      margin-bottom: 12px;
    }

    /* ─── TOAST ─── */
    .toast {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #1e293b;
      color: #fff;
      border: 1px solid var(--card-border);
      padding: 10px 18px;
      border-radius: 10px;
      font-size: 0.82rem;
      font-weight: 600;
      box-shadow: 0 10px 30px rgba(0,0,0,0.5);
      transform: translateY(100px);
      opacity: 0;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 1000;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .toast.show {
      transform: translateY(0);
      opacity: 1;
    }
    .toast.success { border-color: var(--emerald); background: rgba(16, 185, 129, 0.2); color: #34d399; }
    .toast.purple { border-color: var(--purple); background: rgba(139, 92, 246, 0.2); color: #c084fc; }
    .toast.error { border-color: var(--red); background: rgba(239, 68, 68, 0.2); color: #f87171; }

    #importInput { display: none; }
  </style>
</head>

<body>
  <!-- HERO -->
  <header class="hero">
    <div class="wrap">
      <div class="hero-top">
        <div class="brand">
          <div class="brand-icon">🧠</div>
          <div class="brand-text">
            <h1>45-Day Total Transformation · Muscle & Brain Mastery</h1>
            <p>Nov 17 – Dec 31, 2026 · 10kg Dumbbells + Calisthenics + Cognitive Mastery + PG Diet</p>
          </div>
        </div>

        <div class="hero-actions">
          <button class="btn btn-primary" onclick="jumpToToday()">⚡ Today's Mission</button>
          <button class="btn btn-purple" onclick="openGuideModal()">📖 Blueprint & Brain Guide</button>
          <button class="btn btn-emerald" onclick="exportProgress()">📥 Export Backup</button>
          <label class="btn" for="importInput" style="cursor:pointer">📤 Import Backup</label>
          <input type="file" id="importInput" accept=".json" onchange="importProgress(event)" />
          <button class="btn" onclick="resetProgress()" title="Reset all progress">🔄 Reset</button>
        </div>
      </div>

      <!-- Stats Bar -->
      <div class="stats-bar">
        <div class="stat-pill">
          <div class="lbl">Current Day</div>
          <div class="val" id="statCurDay">Day 1</div>
          <div class="sub" id="statCurDate">Nov 17, 2026</div>
        </div>
        <div class="stat-pill">
          <div class="lbl">Jan 1st Countdown</div>
          <div class="val" id="statCountdown" style="color: #f59e0b;">45 Days</div>
          <div class="sub">New Year Launchpad</div>
        </div>
        <div class="stat-pill">
          <div class="lbl">Overall Completion</div>
          <div class="val" id="statPct">0%</div>
          <div class="sub" id="statTasksCount">0 / 0 tasks checked</div>
        </div>
        <div class="stat-pill" onclick="setStatusFilter('completed')" style="cursor:pointer" title="Filter completed days">
          <div class="lbl">Days Fully Done</div>
          <div class="val" id="statDaysDone">0 / 45</div>
          <div class="sub">100% finished days</div>
        </div>
        <div class="stat-pill">
          <div class="lbl">Brain Protocols</div>
          <div class="val" id="statBrainDone" style="color: #c084fc;">0 / 45</div>
          <div class="sub">Mind mastery habits</div>
        </div>
        <div class="stat-pill">
          <div class="lbl">Active Streak</div>
          <div class="val" id="statStreak">0 🔥</div>
          <div class="sub">Consecutive active days</div>
        </div>
      </div>

      <!-- Overall Progress Bar -->
      <div class="overall-prog-wrap">
        <div class="prog-meta">
          <span>Body & Mind Transformation Trajectory</span>
          <span id="statBarPct">0% Completed</span>
        </div>
        <div class="prog-track">
          <div class="prog-fill" id="mainProgFill"></div>
        </div>
      </div>
    </div>
  </header>

  <!-- MAIN CONTAINER -->
  <main class="wrap">
    <!-- TODAY'S MISSION CARD -->
    <div id="todayFocusContainer"></div>

    <!-- CONTROLS & FILTER TABS -->
    <div class="controls-wrap">
      <div class="filter-row">
        <!-- Phase Tabs -->
        <div class="tabs-group" id="phaseTabs">
          <button class="tab-btn active" onclick="setPhaseFilter(0)">All (45 Days)</button>
          <button class="tab-btn" onclick="setPhaseFilter(1)">Phase 1: Foundation & Dopamine Fast</button>
          <button class="tab-btn" onclick="setPhaseFilter(2)">Phase 2: Hypertrophy & Deep Work</button>
          <button class="tab-btn" onclick="setPhaseFilter(3)">Phase 3: Density & Overthinking Immunity</button>
          <button class="tab-btn" onclick="setPhaseFilter(4)">Phase 4: Peak Definition & High IQ</button>
        </div>

        <!-- Search Box -->
        <div class="search-box">
          <span class="search-icon">🔍</span>
          <input type="text" class="search-input" id="searchInput" placeholder="Search exercises, brain missions, foods..." oninput="handleSearch(this.value)" />
        </div>
      </div>

      <div class="filter-row">
        <!-- Body Part Tabs -->
        <div class="tabs-group" id="bodyTabs">
          <button class="tab-btn active" onclick="setBodyFilter('all')">All Splits</button>
          <button class="tab-btn" onclick="setBodyFilter('Push')">Push</button>
          <button class="tab-btn" onclick="setBodyFilter('Pull')">Pull</button>
          <button class="tab-btn" onclick="setBodyFilter('Legs')">Legs</button>
          <button class="tab-btn" onclick="setBodyFilter('Upper')">Upper</button>
          <button class="tab-btn" onclick="setBodyFilter('Lower')">Lower</button>
          <button class="tab-btn" onclick="setBodyFilter('Recovery')">Recovery & Mobility</button>
        </div>

        <!-- Status Filter -->
        <div class="tabs-group" id="statusTabs">
          <button class="tab-btn active" onclick="setStatusFilter('all')">All Status</button>
          <button class="tab-btn" onclick="setStatusFilter('pending')">Pending</button>
          <button class="tab-btn" onclick="setStatusFilter('completed')">Completed</button>
          <button class="tab-btn" onclick="setStatusFilter('skipped')">Skipped</button>
        </div>
      </div>
    </div>

    <!-- 45 DAYS LIST CONTAINER -->
    <div class="days-grid" id="daysGrid"></div>
  </main>

  <!-- GUIDE MODAL -->
  <div class="modal-overlay" id="guideModal" onclick="closeGuideModal(event)">
    <div class="modal-card" onclick="event.stopPropagation()">
      <button class="modal-close" onclick="closeGuideModal()">✕</button>
      <h2>📖 45-Day Total Transformation: Muscle, Mind & Brain Mastery Blueprint</h2>
      <p>A precision-engineered protocol for achieving peak physical condition, stopping overthinking, gaining high-speed intelligence, and mastering your nervous system before January 1, 2027.</p>

      <h3 class="purple-head">🧠 PART 1: The Neurobiology of Brain Control & Ending Overthinking</h3>
      <p>Your brain is a biological prediction machine, not an enemy. When you understand its operating system, you can direct it with effortless control:</p>
      <ul>
        <li><b>How to Stop Overthinking (The 5-Second Action Rule)</b>: The brain creates reasons to hesitate within 5 seconds of an impulse. When overthinking starts, count backwards <code>5-4-3-2-1</code> and move physically. Counting interrupts the emotional amygdala and engages the prefrontal cortex. Action kills anxiety; thinking feeds it.</li>
        <li><b>The Brain Dump (Defusing the Zeigarnik Effect)</b>: The subconscious loops unfinished thoughts because it fears you will forget them. Whenever your mind feels cluttered, dump every raw worry onto paper. Once externalized, the amygdala releases the loop.</li>
        <li><b>The Physiological Sigh (Instant Autonomic Reset)</b>: Two rapid inhales through the nose followed by an extended sigh through the mouth pops open collapsed alveoli and offloads CO2. This triggers the parasympathetic vagus nerve, dropping your heart rate and racing thoughts within 30 seconds.</li>
        <li><b>Dopamine Fasting (Morning Phone Blackout)</b>: Checking social media or notifications in the first 60 minutes after waking crashes your dopamine baseline below normal, ensuring brain fog and compulsive distraction all day. Protect your morning dopamine.</li>
        <li><b>The Stoic Dichotomy of Control</b>: Epictetus: Split every issue into "What is in my control" vs "What is out of my control". For things out of your control, permit zero mental bandwidth. For things in your control, execute ONE concrete action immediately.</li>
        <li><b>Cognitive Defusion</b>: You are not your thoughts; you are the observer of your thoughts. Shift from "I am overwhelmed" to "I notice my mind is generating thoughts of overwhelm." This psychological distance dissolves panic.</li>
      </ul>

      <h3 class="purple-head">⚡ PART 2: How to Be "Very Smart" (High-Speed Cognitive Architecture)</h3>
      <ul>
        <li><b>The 90-Minute Single-Task Deep Work Rule</b>: Multitasking doesn't exist; it is rapid context switching that drains glycogen and lowers functional IQ by 10-15 points. Ninety minutes of unbroken focus on one hard problem produces more breakthrough output than 8 hours of distracted busywork.</li>
        <li><b>The Feynman Technique (Radical Simplicity)</b>: If you cannot explain a concept to a 10-year-old child using simple language, you do not understand it. True intelligence is distilling complexity into crystal clarity.</li>
        <li><b>Mental Models Arsenal</b>:
          <br>• <i>First Principles Thinking</i>: Break a problem down to fundamental truths, reason up from there.
          <br>• <i>Inversion (Charlie Munger)</i>: Ask "What would guarantee failure and brain fog?" (Late screens, junk food, multitasking) and systematically eliminate them.
          <br>• <i>The 80/20 Rule</i>: 20% of inputs yield 80% of results. Identify your single highest-leverage task each day.
          <br>• <i>Second-Order Thinking</i>: Ask "And then what happens?" before making impulsive decisions.
        </li>
        <li><b>Brain Fuel & Glymphatic Sleep</b>: Creatine (3–5g daily) boosts brain phosphocreatine and working memory speed in clinical trials. Paired with 3.5L hydration and 8 hours of sleep, your brain flushes metabolic waste (the glymphatic cleanse) every single night.</li>
      </ul>

      <h3>⚖️ PART 3: 10kg Dumbbell & Progressive Calisthenics Hypertrophy</h3>
      <p>You have 2 handles, 4 × 2kg plates, and 3kg plates (up to 10kg each):</p>
      <ul>
        <li><b>Light Pair (4kg – 5kg each)</b>: Strict Lateral Raises, Rear Delt Flyes, and Arnold Press.</li>
        <li><b>Medium Pair (7kg – 8kg each)</b>: Supinating Bicep Curls, Floor Press, and Walking Lunges.</li>
        <li><b>Heavy Loaded Single (10kg)</b>: Goblet Squats, Bulgarian Split Squats, Single-Arm DB Rows, Overhead Tricep Extensions!</li>
        <li><b>The 3-Second Eccentric Rule</b>: When you can't add 20kg of metal, lower the weight for 3 full seconds. This triples mechanical tension and stimulates deep hypertrophy.</li>
        <li><b>Calisthenics Elevation</b>: Elevating your feet on your PG bed during pushups shifts 75% of bodyweight onto your upper clavicular chest and shoulders.</li>
      </ul>

      <h3>🍳 PART 4: Budget PG Nutrition & Supplement Protocol</h3>
      <ul>
        <li><b>Sunday Chicken Special</b>: PG serves chicken dinner on Sundays! Eggs are scheduled off on Sundays so you can enjoy your high-protein chicken feast.</li>
        <li><b>Monday–Saturday Eggs</b>: 2 whole boiled eggs daily (₹7 each = ₹14/day).</li>
        <li><b>Whey Protein</b>: 1 scoop (24g–25g protein) post-workout or in the evening.</li>
        <li><b>Creatine Monohydrate</b>: 3g–5g daily. Take it every day at the same time with water or meals. Neuroprotective & muscle volumizing.</li>
        <li><b>Water Target (3.5L – 4.0L)</b>: Mandatory with creatine to prevent cramps and maximize brain processing speed.</li>
        <li><b>Room-Storable Boosters</b>: Soya chunks (Nutrela), Roasted Bhuna Chana, Roasted Peanuts, Curd/Dahi, and Sattu powder.</li>
      </ul>
    </div>
  </div>

  <!-- TOAST NOTIFICATION -->
  <div class="toast" id="toast"></div>

  <!-- LOAD WORKOUT DATA -->
  <script src="workout_data.js"></script>

  <!-- DASHBOARD CONTROLLER -->
  <script>
    // ════════════════════════════════════════════════════════════════════
    // STATE MANAGEMENT & LOCAL STORAGE
    // ════════════════════════════════════════════════════════════════════
    const STORAGE_KEY = 'wt_progress_45day';
    let progressState = {
      checks: {},
      water: {},
      notes: {}
    };

    let activePhaseFilter = 0; // 0 = all
    let activeBodyFilter = 'all';
    let activeStatusFilter = 'all';
    let searchQuery = '';

    // Load state from localStorage
    function loadState() {
      try {
        const saved = localStorage.getItem(STORAGE_KEY);
        if (saved) {
          progressState = JSON.parse(saved);
          if (!progressState.checks) progressState.checks = {};
          if (!progressState.water) progressState.water = {};
          if (!progressState.notes) progressState.notes = {};
        }
      } catch (e) {
        console.error('Failed to load localStorage:', e);
      }
    }

    // Save state to localStorage
    function saveState() {
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(progressState));
        syncWithServer();
      } catch (e) {
        console.error('Failed to save to localStorage:', e);
      }
    }

    // Sync with optional server
    async function syncWithServer() {
      try {
        if (location.protocol.startsWith('http')) {
          await fetch('/api/progress', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(progressState)
          });
        }
      } catch (e) {
        // Silently fallback to pure client-side localStorage
      }
    }

    // Detect current day based on local clock
    function getTodayDayNum() {
      const now = new Date();
      const todayStr = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}-${String(now.getDate()).padStart(2, '0')}`;
      const match = WORKOUT_PLAN.find(d => d.date === todayStr);
      if (match) return match.day;
      if (todayStr <= WORKOUT_PLAN[0].date) return 1;
      if (todayStr > WORKOUT_PLAN[WORKOUT_PLAN.length - 1].date) return WORKOUT_PLAN.length;
      return 1;
    }

    // Calculate skipped workout exercises for a day
    function getDaySkippedWorkouts(dayObj) {
      let skipped = 0;
      dayObj.morning.forEach(ex => {
        if (!isDone(ex.id)) skipped++;
      });
      if (dayObj.evening.core && !isDone(dayObj.evening.core.id)) skipped++;
      if (dayObj.evening.mobility && !isDone(dayObj.evening.mobility.id)) skipped++;
      if (dayObj.evening.cardio && !isDone(dayObj.evening.cardio.id)) skipped++;
      return skipped;
    }

    // Toggle a task checkbox
    function toggleTask(id) {
      progressState.checks[id] = !progressState.checks[id];
      saveState();
      updateAll();
      const isBrain = id.startsWith('b_');
      showToast(progressState.checks[id] ? (isBrain ? '🧠 Brain Habit Logged!' : '✅ Mission Completed!') : '↩️ Task Unchecked', isBrain ? 'purple' : 'success');
    }

    // Toggle water cup
    function toggleWater(day, liter) {
      const key = `w_${day}_${liter}`;
      progressState.water[key] = !progressState.water[key];
      saveState();
      updateAll();
    }

    // Save notes
    function saveNote(day, text) {
      progressState.notes[`note_${day}`] = text;
      saveState();
    }

    // Check if task is done
    function isDone(id) {
      return !!progressState.checks[id];
    }

    // Calculate day completion percentage
    function getDayStats(dayObj) {
      let total = 0;
      let completed = 0;

      // Morning exercises
      dayObj.morning.forEach(ex => {
        total++;
        if (isDone(ex.id)) completed++;
      });

      // Evening routine
      if (dayObj.evening.core) { total++; if (isDone(dayObj.evening.core.id)) completed++; }
      if (dayObj.evening.mobility) { total++; if (isDone(dayObj.evening.mobility.id)) completed++; }
      if (dayObj.evening.cardio) { total++; if (isDone(dayObj.evening.cardio.id)) completed++; }

      // Brain Habits (4 checks)
      if (dayObj.brain && dayObj.brain.habits) {
        dayObj.brain.habits.forEach(h => {
          total++;
          if (isDone(h.id)) completed++;
        });
      }

      // Nutrition checks (4)
      total += 4;
      if (isDone(`n_${dayObj.day}_prot`)) completed++;
      if (isDone(`n_${dayObj.day}_whey`)) completed++;
      if (isDone(`n_${dayObj.day}_creatine`)) completed++;
      if (isDone(`n_${dayObj.day}_snack`)) completed++;

      const pct = total > 0 ? Math.round((completed / total) * 100) : 0;
      return { total, completed, pct, isFullyDone: completed === total && total > 0 };
    }

    // ════════════════════════════════════════════════════════════════════
    // RENDERING LOGIC
    // ════════════════════════════════════════════════════════════════════

    function renderTodayFocus() {
      const todayNum = getTodayDayNum();
      const day = WORKOUT_PLAN.find(d => d.day === todayNum) || WORKOUT_PLAN[0];
      const stats = getDayStats(day);
      const isSunday = day.nutrition.isSunday;

      const now = new Date();
      const todayStr = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}-${String(now.getDate()).padStart(2, '0')}`;
      let statusBadgeText = "🔥 TODAY'S MISSION";
      if (todayStr < day.date) {
        statusBadgeText = "🚀 DAY 1 READY (STARTS TUE)";
      }

      const container = document.getElementById('todayFocusContainer');
      container.innerHTML = `
        <div class="today-focus-card" id="todayCardAnchor">
          <div class="tf-header">
            <div>
              <div class="tf-title">
                <span>⚡ Day ${day.day} · ${day.title}</span>
              </div>
              <div style="font-size:0.8rem;color:var(--t2);margin-top:4px;font-family:'JetBrains Mono',monospace;">
                ${day.weekday}, ${day.date} · W${day.week} · ${day.tempoNote}
              </div>
            </div>
            <div class="tf-badges">
              <span class="badge badge-today">${statusBadgeText}</span>
              <span class="badge badge-phase">${day.phaseName.split('—')[0].trim()}</span>
              <span class="badge badge-body">${day.bodyPart} Split</span>
              <span class="badge" style="background:rgba(16,185,129,0.2);color:#34d399;font-family:'JetBrains Mono'">${stats.pct}% Done</span>
            </div>
          </div>

          <div class="tf-sections">
            <!-- Morning Workout -->
            <div class="sec-box">
              <div class="sec-title">
                <span>☀️ Morning Session (60 mins)</span>
                <span class="sec-sub">Mechanical Tension & Hypertrophy</span>
              </div>
              ${day.morning.map(ex => `
                <div class="task-item ${isDone(ex.id) ? 'done' : ''}">
                  <input type="checkbox" class="task-chk" ${isDone(ex.id) ? 'checked' : ''} onchange="toggleTask('${ex.id}')" />
                  <div class="task-info">
                    <div class="task-name">
                      <span>${ex.name}</span>
                      ${ex.yt ? `<a href="${ex.yt}" target="_blank" rel="noopener noreferrer" class="yt-btn">▶ Form Video</a>` : ''}
                    </div>
                    <div class="task-meta">
                      <span>${ex.sets} sets × ${ex.reps}</span>
                      <span>⚖️ ${ex.load}</span>
                      <span>⏱️ ${ex.tempo}</span>
                    </div>
                  </div>
                </div>
              `).join('')}

              <!-- Evening Core & Mobility -->
              <div style="margin-top:16px;padding-top:14px;border-top:1px solid rgba(255,255,255,0.08);">
                <div class="sec-title" style="color:#38bdf8;">
                  <span>🌙 Evening Session (30 mins)</span>
                  <span class="sec-sub">Core & Posture Flush</span>
                </div>

                ${day.evening.core ? `
                  <div class="task-item ${isDone(day.evening.core.id) ? 'done' : ''}">
                    <input type="checkbox" class="task-chk" ${isDone(day.evening.core.id) ? 'checked' : ''} onchange="toggleTask('${day.evening.core.id}')" />
                    <div class="task-info">
                      <div class="task-name">
                        <span>🧘 ${day.evening.core.name}</span>
                        ${day.evening.core.yt ? `<a href="${day.evening.core.yt}" target="_blank" rel="noopener noreferrer" class="yt-btn">▶ Form Video</a>` : ''}
                      </div>
                      <div class="task-meta"><span>${day.evening.core.target}</span></div>
                    </div>
                  </div>
                ` : ''}

                ${day.evening.mobility ? `
                  <div class="task-item ${isDone(day.evening.mobility.id) ? 'done' : ''}">
                    <input type="checkbox" class="task-chk" ${isDone(day.evening.mobility.id) ? 'checked' : ''} onchange="toggleTask('${day.evening.mobility.id}')" />
                    <div class="task-info">
                      <div class="task-name">
                        <span>🦴 ${day.evening.mobility.name}</span>
                        ${day.evening.mobility.yt ? `<a href="${day.evening.mobility.yt}" target="_blank" rel="noopener noreferrer" class="yt-btn">▶ Form Video</a>` : ''}
                      </div>
                      <div class="task-meta"><span>${day.evening.mobility.target}</span></div>
                    </div>
                  </div>
                ` : ''}

                ${day.evening.cardio ? `
                  <div class="task-item ${isDone(day.evening.cardio.id) ? 'done' : ''}">
                    <input type="checkbox" class="task-chk" ${isDone(day.evening.cardio.id) ? 'checked' : ''} onchange="toggleTask('${day.evening.cardio.id}')" />
                    <div class="task-info">
                      <div class="task-name"><span>🚶 ${day.evening.cardio.name}</span></div>
                      <div class="task-meta"><span>${day.evening.cardio.target}</span></div>
                    </div>
                  </div>
                ` : ''}
              </div>
            </div>

            <!-- Brain & Cognitive Mastery (Right Column) -->
            <div>
              <div class="brain-box">
                <div class="brain-header">
                  <div class="brain-title">
                    <span>🧠 ${day.brain.theme}</span>
                  </div>
                  <span class="brain-pillar-tag">${day.brain.pillar}</span>
                </div>

                <div class="brain-principle">
                  <b>💡 Why It Works:</b> ${day.brain.principle}
                </div>

                <div class="brain-action">
                  <b>🎯 Today's Mission:</b> ${day.brain.action}
                </div>

                <div style="font-size:0.75rem;font-weight:700;color:#c084fc;margin-bottom:8px;text-transform:uppercase;letter-spacing:0.04em;">Daily Cognitive Habit Checkpoints:</div>
                <div class="brain-habits-grid">
                  ${day.brain.habits.map(h => `
                    <div class="task-item brain-task ${isDone(h.id) ? 'done' : ''}" style="margin-bottom:6px;">
                      <input type="checkbox" class="task-chk brain-chk" ${isDone(h.id) ? 'checked' : ''} onchange="toggleTask('${h.id}')" />
                      <div class="task-info">
                        <div class="task-name" style="font-size:0.8rem;"><span>${h.name}</span></div>
                      </div>
                    </div>
                  `).join('')}
                </div>
              </div>

              <!-- Daily Notes for Today -->
              <div class="note-box" style="margin-top:14px;">
                <label>📝 Today's Reps, Notes & Mental Clarity Log</label>
                <textarea class="note-input" placeholder="Record weights, reps, or how you controlled overthinking today..." onchange="saveNote(${day.day}, this.value)">${progressState.notes[`note_${day.day}`] || ''}</textarea>
              </div>
            </div>
          </div>

          <!-- PG Nutrition Protocol for Today -->
          <div class="diet-box">
            <div class="diet-header">
              <span>🥗 PG Nutrition & Supplement Protocol</span>
              <span style="font-family:'JetBrains Mono';font-size:0.75rem;color:#38bdf8;">Target Protein: ${day.nutrition.estProtein}</span>
            </div>
            <div class="diet-highlight">${day.nutrition.highlight}</div>

            <div class="diet-grid">
              <div class="diet-card">
                <b>Breakfast (PG)</b>
                <div>${day.nutrition.breakfast}</div>
              </div>
              <div class="diet-card">
                <b>Lunch (PG Mess)</b>
                <div>${day.nutrition.lunch}</div>
              </div>
              <div class="diet-card">
                <b>Evening Snack</b>
                <div>${day.nutrition.snack}</div>
              </div>
              <div class="diet-card">
                <b>Dinner (PG Mess)</b>
                <div>${day.nutrition.dinner}</div>
              </div>
            </div>

            <!-- Nutrition Checklist -->
            <div style="margin-top:14px;display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:8px;">
              <label class="task-item" style="cursor:pointer;margin:0;">
                <input type="checkbox" class="task-chk" ${isDone(`n_${day.day}_prot`) ? 'checked' : ''} onchange="toggleTask('n_${day.day}_prot')" />
                <div class="task-info"><div class="task-name">${isSunday ? '🍗 PG Chicken Feast' : '🥚 2 Boiled Eggs'}</div></div>
              </label>

              <label class="task-item" style="cursor:pointer;margin:0;">
                <input type="checkbox" class="task-chk" ${isDone(`n_${day.day}_whey`) ? 'checked' : ''} onchange="toggleTask('n_${day.day}_whey')" />
                <div class="task-info"><div class="task-name">🥤 1 Scoop Whey Protein</div></div>
              </label>

              <label class="task-item" style="cursor:pointer;margin:0;">
                <input type="checkbox" class="task-chk" ${isDone(`n_${day.day}_creatine`) ? 'checked' : ''} onchange="toggleTask('n_${day.day}_creatine')" />
                <div class="task-info"><div class="task-name">⚡ 3g–5g Creatine (Brain & Muscle)</div></div>
              </label>

              <label class="task-item" style="cursor:pointer;margin:0;">
                <input type="checkbox" class="task-chk" ${isDone(`n_${day.day}_snack`) ? 'checked' : ''} onchange="toggleTask('n_${day.day}_snack')" />
                <div class="task-info"><div class="task-name">🥜 Daily Protein Booster Snack</div></div>
              </label>
            </div>

            <!-- Hydration Tracker -->
            <div class="water-row">
              <span style="font-size:0.75rem;font-weight:700;color:var(--t2);">💧 Hydration (3.5L–4L for Brain & Creatine):</span>
              <button class="water-pill ${progressState.water[`w_${day.day}_1`] ? 'checked' : ''}" onclick="toggleWater(${day.day}, 1)">1.0 Liter</button>
              <button class="water-pill ${progressState.water[`w_${day.day}_2`] ? 'checked' : ''}" onclick="toggleWater(${day.day}, 2)">2.0 Liters</button>
              <button class="water-pill ${progressState.water[`w_${day.day}_3`] ? 'checked' : ''}" onclick="toggleWater(${day.day}, 3)">3.0 Liters</button>
              <button class="water-pill ${progressState.water[`w_${day.day}_4`] ? 'checked' : ''}" onclick="toggleWater(${day.day}, 4)">4.0 Liters ✨</button>
            </div>
          </div>
        </div>
      `;
    }

    function renderDaysGrid() {
      const todayNum = getTodayDayNum();
      const grid = document.getElementById('daysGrid');

      // Filter days
      const filtered = WORKOUT_PLAN.filter(d => {
        // Phase Filter
        if (activePhaseFilter !== 0 && d.phase !== activePhaseFilter) return false;
        // Body Part Filter
        if (activeBodyFilter !== 'all' && d.bodyPart.toLowerCase() !== activeBodyFilter.toLowerCase()) return false;
        // Status Filter
        const stats = getDayStats(d);
        if (activeStatusFilter === 'completed' && !stats.isFullyDone) return false;
        if (activeStatusFilter === 'pending' && stats.isFullyDone) return false;
        if (activeStatusFilter === 'skipped') {
          if (d.day >= todayNum) return false;
          if (getDaySkippedWorkouts(d) === 0) return false;
        }
        // Search Query
        if (searchQuery) {
          const q = searchQuery.toLowerCase();
          const matchTitle = d.title.toLowerCase().includes(q);
          const matchBody = d.bodyPart.toLowerCase().includes(q);
          const matchEx = d.morning.some(e => e.name.toLowerCase().includes(q));
          const matchDiet = d.nutrition.highlight.toLowerCase().includes(q);
          const matchBrainTheme = d.brain ? d.brain.theme.toLowerCase().includes(q) : false;
          const matchBrainPillar = d.brain ? d.brain.pillar.toLowerCase().includes(q) : false;
          const matchBrainAction = d.brain ? d.brain.action.toLowerCase().includes(q) : false;
          if (!matchTitle && !matchBody && !matchEx && !matchDiet && !matchBrainTheme && !matchBrainPillar && !matchBrainAction) return false;
        }
        return true;
      });

      if (filtered.length === 0) {
        grid.innerHTML = `<div style="text-align:center;padding:60px 20px;color:var(--t2)">No days matched the selected filters.</div>`;
        return;
      }

      grid.innerHTML = filtered.map(day => {
        const stats = getDayStats(day);
        const isToday = day.day === todayNum;
        const isPast = day.day < todayNum;
        const skippedWorkouts = isPast ? getDaySkippedWorkouts(day) : 0;
        const isSunday = day.nutrition.isSunday;

        return `
          <div class="day-card ${isToday ? 'today-card expanded' : ''} ${stats.isFullyDone ? 'completed-card' : ''}" id="dayCard_${day.day}">
            <!-- Header -->
            <div class="dc-header" onclick="toggleDayCard(${day.day})">
              <div class="dc-left">
                <span class="dc-day-num">#${day.day}</span>
                <div class="dc-title-group">
                  <h3>
                    <span>${day.title}</span>
                    ${isToday ? `<span class="badge badge-today" style="font-size:0.65rem;">TODAY</span>` : ''}
                    ${skippedWorkouts > 0 ? `<span class="badge" style="font-size:0.65rem;background:rgba(249,115,22,0.15);color:#fb923c;border:1px solid rgba(249,115,22,0.3);">${skippedWorkouts} SKIPPED</span>` : ''}
                    <span class="badge badge-phase" style="font-size:0.65rem;">${day.bodyPart}</span>
                    <span class="badge" style="font-size:0.65rem;background:rgba(139,92,246,0.15);color:#c084fc;">🧠 ${day.brain.pillar}</span>
                  </h3>
                  <div class="dc-date-str">${day.weekday}, ${day.date} · W${day.week} · ${day.phaseName.split('—')[0].trim()} · ${day.brain.theme}</div>
                </div>
              </div>

              <div class="dc-right">
                <div class="dc-prog-mini">
                  <div class="dc-prog-mini-fill" style="width:${stats.pct}%"></div>
                </div>
                <span class="dc-pct">${stats.pct}%</span>
                <span class="dc-toggle-icon">▼</span>
              </div>
            </div>

            <!-- Body (Collapsible) -->
            <div class="dc-body">
              <div class="tf-sections">
                <!-- Morning & Evening Physical Training -->
                <div class="sec-box">
                  <div class="sec-title">
                    <span>☀️ Morning Session (60 mins)</span>
                    <span class="sec-sub">${day.tempoNote}</span>
                  </div>
                  ${day.morning.map(ex => `
                    <div class="task-item ${isDone(ex.id) ? 'done' : ''}">
                      <input type="checkbox" class="task-chk" ${isDone(ex.id) ? 'checked' : ''} onchange="toggleTask('${ex.id}')" />
                      <div class="task-info">
                        <div class="task-name">
                          <span>${ex.name}</span>
                          ${ex.yt ? `<a href="${ex.yt}" target="_blank" rel="noopener noreferrer" class="yt-btn">▶ Form Video</a>` : ''}
                        </div>
                        <div class="task-meta">
                          <span>${ex.sets} sets × ${ex.reps}</span>
                          <span>⚖️ ${ex.load}</span>
                          <span>⏱️ ${ex.tempo}</span>
                        </div>
                      </div>
                    </div>
                  `).join('')}

                  <!-- Evening Routine -->
                  <div style="margin-top:14px;padding-top:12px;border-top:1px solid rgba(255,255,255,0.06);">
                    <div class="sec-title" style="color:#38bdf8;font-size:0.82rem;">
                      <span>🌙 Evening Core & Recovery (30 mins)</span>
                    </div>

                    ${day.evening.core ? `
                      <div class="task-item ${isDone(day.evening.core.id) ? 'done' : ''}">
                        <input type="checkbox" class="task-chk" ${isDone(day.evening.core.id) ? 'checked' : ''} onchange="toggleTask('${day.evening.core.id}')" />
                        <div class="task-info">
                          <div class="task-name">
                            <span>🧘 ${day.evening.core.name}</span>
                            ${day.evening.core.yt ? `<a href="${day.evening.core.yt}" target="_blank" rel="noopener noreferrer" class="yt-btn">▶ Form Video</a>` : ''}
                          </div>
                          <div class="task-meta"><span>${day.evening.core.target}</span></div>
                        </div>
                      </div>
                    ` : ''}

                    ${day.evening.mobility ? `
                      <div class="task-item ${isDone(day.evening.mobility.id) ? 'done' : ''}">
                        <input type="checkbox" class="task-chk" ${isDone(day.evening.mobility.id) ? 'checked' : ''} onchange="toggleTask('${day.evening.mobility.id}')" />
                        <div class="task-info">
                          <div class="task-name">
                            <span>🦴 ${day.evening.mobility.name}</span>
                            ${day.evening.mobility.yt ? `<a href="${day.evening.mobility.yt}" target="_blank" rel="noopener noreferrer" class="yt-btn">▶ Form Video</a>` : ''}
                          </div>
                          <div class="task-meta"><span>${day.evening.mobility.target}</span></div>
                        </div>
                      </div>
                    ` : ''}

                    ${day.evening.cardio ? `
                      <div class="task-item ${isDone(day.evening.cardio.id) ? 'done' : ''}">
                        <input type="checkbox" class="task-chk" ${isDone(day.evening.cardio.id) ? 'checked' : ''} onchange="toggleTask('${day.evening.cardio.id}')" />
                        <div class="task-info">
                          <div class="task-name"><span>🚶 ${day.evening.cardio.name}</span></div>
                          <div class="task-meta"><span>${day.evening.cardio.target}</span></div>
                        </div>
                      </div>
                    ` : ''}
                  </div>
                </div>

                <!-- Cognitive Protocol & Notes -->
                <div>
                  <div class="brain-box">
                    <div class="brain-header">
                      <div class="brain-title"><span>🧠 ${day.brain.theme}</span></div>
                      <span class="brain-pillar-tag">${day.brain.pillar}</span>
                    </div>

                    <div class="brain-principle"><b>💡 Why It Works:</b> ${day.brain.principle}</div>
                    <div class="brain-action"><b>🎯 Mission:</b> ${day.brain.action}</div>

                    <div style="font-size:0.75rem;font-weight:700;color:#c084fc;margin-bottom:6px;">Habits:</div>
                    ${day.brain.habits.map(h => `
                      <div class="task-item brain-task ${isDone(h.id) ? 'done' : ''}" style="margin-bottom:6px;">
                        <input type="checkbox" class="task-chk brain-chk" ${isDone(h.id) ? 'checked' : ''} onchange="toggleTask('${h.id}')" />
                        <div class="task-info">
                          <div class="task-name" style="font-size:0.8rem;"><span>${h.name}</span></div>
                        </div>
                      </div>
                    `).join('')}
                  </div>

                  <div class="note-box">
                    <label>📝 Day ${day.day} Notes & Reps</label>
                    <textarea class="note-input" placeholder="Record weights, reps, or thoughts..." onchange="saveNote(${day.day}, this.value)">${progressState.notes[`note_${day.day}`] || ''}</textarea>
                  </div>
                </div>
              </div>

              <!-- Nutrition -->
              <div class="diet-box">
                <div class="diet-header">
                  <span>🥗 PG Diet · ${day.nutrition.highlight}</span>
                  <span style="font-family:'JetBrains Mono';font-size:0.75rem;color:#38bdf8;">${day.nutrition.estProtein}</span>
                </div>
                <div class="diet-grid">
                  <div class="diet-card"><b>Breakfast</b><div>${day.nutrition.breakfast}</div></div>
                  <div class="diet-card"><b>Lunch</b><div>${day.nutrition.lunch}</div></div>
                  <div class="diet-card"><b>Snack</b><div>${day.nutrition.snack}</div></div>
                  <div class="diet-card"><b>Dinner</b><div>${day.nutrition.dinner}</div></div>
                </div>

                <div style="margin-top:10px;display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:8px;">
                  <label class="task-item" style="cursor:pointer;margin:0;">
                    <input type="checkbox" class="task-chk" ${isDone(`n_${day.day}_prot`) ? 'checked' : ''} onchange="toggleTask('n_${day.day}_prot')" />
                    <div class="task-info"><div class="task-name">${isSunday ? '🍗 PG Chicken Feast' : '🥚 2 Boiled Eggs'}</div></div>
                  </label>
                  <label class="task-item" style="cursor:pointer;margin:0;">
                    <input type="checkbox" class="task-chk" ${isDone(`n_${day.day}_whey`) ? 'checked' : ''} onchange="toggleTask('n_${day.day}_whey')" />
                    <div class="task-info"><div class="task-name">🥤 1 Scoop Whey</div></div>
                  </label>
                  <label class="task-item" style="cursor:pointer;margin:0;">
                    <input type="checkbox" class="task-chk" ${isDone(`n_${day.day}_creatine`) ? 'checked' : ''} onchange="toggleTask('n_${day.day}_creatine')" />
                    <div class="task-info"><div class="task-name">⚡ 3g–5g Creatine</div></div>
                  </label>
                  <label class="task-item" style="cursor:pointer;margin:0;">
                    <input type="checkbox" class="task-chk" ${isDone(`n_${day.day}_snack`) ? 'checked' : ''} onchange="toggleTask('n_${day.day}_snack')" />
                    <div class="task-info"><div class="task-name">🥜 Protein Snack</div></div>
                  </label>
                </div>

                <!-- Water Tracker -->
                <div class="water-row">
                  <span style="font-size:0.72rem;font-weight:700;color:var(--t2);">💧 Water:</span>
                  <button class="water-pill ${progressState.water[`w_${day.day}_1`] ? 'checked' : ''}" onclick="toggleWater(${day.day}, 1)">1.0L</button>
                  <button class="water-pill ${progressState.water[`w_${day.day}_2`] ? 'checked' : ''}" onclick="toggleWater(${day.day}, 2)">2.0L</button>
                  <button class="water-pill ${progressState.water[`w_${day.day}_3`] ? 'checked' : ''}" onclick="toggleWater(${day.day}, 3)">3.0L</button>
                  <button class="water-pill ${progressState.water[`w_${day.day}_4`] ? 'checked' : ''}" onclick="toggleWater(${day.day}, 4)">4.0L ✨</button>
                </div>
              </div>
            </div>
          </div>
        `;
      }).join('');
    }

    function toggleDayCard(dayNum) {
      const card = document.getElementById(`dayCard_${dayNum}`);
      if (card) {
        card.classList.toggle('expanded');
      }
    }

    function updateStatsHeader() {
      const todayNum = getTodayDayNum();
      const todayObj = WORKOUT_PLAN.find(d => d.day === todayNum) || WORKOUT_PLAN[0];

      document.getElementById('statCurDay').textContent = `Day ${todayObj.day}`;
      document.getElementById('statCurDate').textContent = `${todayObj.weekday.slice(0,3)}, ${todayObj.date}`;

      // Countdown to Jan 1st, 2027
      const now = new Date();
      const targetDate = new Date(2027, 0, 1);
      const diffMs = targetDate - now;
      const daysLeft = Math.max(0, Math.ceil(diffMs / (1000 * 60 * 60 * 24)));
      document.getElementById('statCountdown').textContent = `${daysLeft} Days`;

      let totalTasks = 0;
      let totalCompleted = 0;
      let days100 = 0;
      let totalBrainHabitsDone = 0;

      WORKOUT_PLAN.forEach(d => {
        const s = getDayStats(d);
        totalTasks += s.total;
        totalCompleted += s.completed;
        if (s.isFullyDone) days100++;

        if (d.brain && d.brain.habits) {
          d.brain.habits.forEach(h => {
            if (isDone(h.id)) totalBrainHabitsDone++;
          });
        }
      });

      const overallPct = totalTasks > 0 ? Math.round((totalCompleted / totalTasks) * 100) : 0;
      document.getElementById('statPct').textContent = `${overallPct}%`;
      document.getElementById('statTasksCount').textContent = `${totalCompleted} / ${totalTasks} tasks checked`;
      document.getElementById('statDaysDone').textContent = `${days100} / ${WORKOUT_PLAN.length}`;
      document.getElementById('statBrainDone').textContent = `${totalBrainHabitsDone} / ${WORKOUT_PLAN.length * 4}`;

      document.getElementById('mainProgFill').style.width = `${overallPct}%`;
      document.getElementById('statBarPct').textContent = `${overallPct}% Completed`;

      // Streak calculation
      let streak = 0;
      for (let i = 0; i < WORKOUT_PLAN.length; i++) {
        const s = getDayStats(WORKOUT_PLAN[i]);
        if (s.completed > 0) {
          streak++;
        } else if (WORKOUT_PLAN[i].day >= todayNum) {
          break;
        }
      }
      document.getElementById('statStreak').textContent = `${streak} 🔥`;
    }

    function updateAll() {
      renderTodayFocus();
      renderDaysGrid();
      updateStatsHeader();
    }

    // ════════════════════════════════════════════════════════════════════
    // FILTER CONTROLLERS
    // ════════════════════════════════════════════════════════════════════
    function setPhaseFilter(phase) {
      activePhaseFilter = phase;
      document.querySelectorAll('#phaseTabs .tab-btn').forEach((b, idx) => {
        b.classList.toggle('active', idx === phase);
      });
      renderDaysGrid();
    }

    function setBodyFilter(bodyPart) {
      activeBodyFilter = bodyPart;
      document.querySelectorAll('#bodyTabs .tab-btn').forEach(b => {
        b.classList.toggle('active', b.textContent.toLowerCase().includes(bodyPart.toLowerCase()) || (bodyPart === 'all' && b.textContent.includes('All')));
      });
      renderDaysGrid();
    }

    function setStatusFilter(status) {
      activeStatusFilter = status;
      document.querySelectorAll('#statusTabs .tab-btn').forEach(b => {
        b.classList.toggle('active', b.textContent.toLowerCase() === status.toLowerCase() || (status === 'all' && b.textContent.includes('All')));
      });
      renderDaysGrid();
    }

    function handleSearch(val) {
      searchQuery = val.trim();
      renderDaysGrid();
    }

    function jumpToToday() {
      const el = document.getElementById('todayCardAnchor');
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }

    // ════════════════════════════════════════════════════════════════════
    // EXPORT / IMPORT BACKUP
    // ════════════════════════════════════════════════════════════════════
    function exportProgress() {
      const dataStr = 'data:text/json;charset=utf-8,' + encodeURIComponent(JSON.stringify(progressState, null, 2));
      const a = document.createElement('a');
      a.setAttribute('href', dataStr);
      a.setAttribute('download', `total_transformation_progress_${new Date().toISOString().slice(0, 10)}.json`);
      document.body.appendChild(a);
      a.click();
      a.remove();
      showToast('📥 Backup exported successfully!', 'success');
    }

    function importProgress(event) {
      const file = event.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = function(e) {
        try {
          const parsed = JSON.parse(e.target.result);
          if (parsed && typeof parsed === 'object') {
            progressState = parsed;
            saveState();
            updateAll();
            showToast('📤 Progress imported successfully!', 'success');
          }
        } catch (err) {
          showToast('❌ Invalid JSON backup file', 'error');
        }
      };
      reader.readAsText(file);
      event.target.value = ''; // Reset input
    }

    function resetProgress() {
      if (confirm('Are you sure you want to restart everything from Day 1? This will clear all checked tasks for a 100% clean slate to Jan 1st.')) {
        progressState = { checks: {}, water: {}, notes: {} };
        saveState();
        updateAll();
        showToast('🔄 Reset complete! 45-day fresh start begins now.', 'success');
      }
    }

    // Guide Modal
    function openGuideModal() {
      document.getElementById('guideModal').classList.add('open');
    }
    function closeGuideModal(e) {
      if (!e || e.target.id === 'guideModal' || e.target.classList.contains('modal-close')) {
        document.getElementById('guideModal').classList.remove('open');
      }
    }

    // Toast
    function showToast(msg, type = '') {
      const t = document.getElementById('toast');
      t.textContent = msg;
      t.className = `toast show ${type}`;
      setTimeout(() => {
        t.className = 'toast';
      }, 3000);
    }

    // ════════════════════════════════════════════════════════════════════
    // INITIALIZATION
    // ════════════════════════════════════════════════════════════════════
    document.addEventListener('DOMContentLoaded', () => {
      loadState();
      updateAll();
    });
  </script>
</body>
</html>
'''

inline_block = f"""  <!-- LOAD WORKOUT DATA -->\n  <!-- INLINE 45-DAY TOTAL TRANSFORMATION DATA (Muscle & Brain Mastery) -->\n  <script>\n    const WORKOUT_PLAN = {workout_plan_json};\n    if (typeof window !== 'undefined') window.WORKOUT_PLAN = WORKOUT_PLAN;\n  </script>"""
final_html = html_template.replace('  <!-- LOAD WORKOUT DATA -->\n  <script src="workout_data.js"></script>', inline_block, 1)

with open('/home/praveen/personal-projects/workout-tracker/index.html', 'w') as f:
    f.write(final_html)

print("Generated index.html successfully with inlined 45-day dataset!")
