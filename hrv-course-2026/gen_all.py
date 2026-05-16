#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generates all pages for the HRV course portal (hrv-course-2026/)."""
import sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path

SITE = Path(__file__).parent

# ── Shared design tokens ───────────────────────────────────────────────────────

NAV_LINKS = [
    ("index.html",          "🏠",  "Home"),
    ("teams.html",          "👥",  "Teams"),
    ("individual.html",     "📓",  "My Workbook"),
    ("team-workbook.html",  "📋",  "Team Workbook"),
    ("readings.html",       "📚",  "Readings"),
]

SHARED_CSS = """
:root {
  --bg: #0b1829;
  --surface: #132338;
  --surface2: #1a2f4a;
  --border: #1e3555;
  --text: #ddeaf7;
  --muted: #6a94b8;
  --accent: #38b2ac;
  --accent2: #63d0ff;
  --teal-light: #81e6d9;
  --coral: #e76f51;
  --green: #06a078;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: var(--bg); color: var(--text); font-family: 'Segoe UI', system-ui, sans-serif; font-size: 14px; line-height: 1.6; min-height: 100vh; }

/* NAV */
nav {
  background: #0a1624;
  border-bottom: 1px solid var(--border);
  padding: 0 28px;
  display: flex; align-items: center; gap: 0;
  position: sticky; top: 0; z-index: 100;
  height: 52px;
}
.nav-brand {
  display: flex; align-items: center; gap: 10px;
  margin-right: 28px; text-decoration: none;
}
.nav-icon {
  width: 30px; height: 30px; border-radius: 8px;
  background: linear-gradient(135deg,#1a6fa3,#38b2ac);
  display: flex; align-items: center; justify-content: center; font-size: 14px;
}
.nav-brand-text { font-size: 0.82rem; font-weight: 700; color: var(--text); }
.nav-links { display: flex; gap: 2px; align-items: center; }
.nav-link {
  padding: 6px 12px; border-radius: 7px;
  text-decoration: none; color: var(--muted); font-size: 0.8rem;
  display: flex; align-items: center; gap: 5px;
  transition: all 0.15s;
}
.nav-link:hover { background: var(--surface); color: var(--text); }
.nav-link.active { background: var(--surface2); color: var(--accent); font-weight: 600; }

/* PAGE WRAPPER */
.page { max-width: 940px; margin: 0 auto; padding: 36px 24px 60px; }

/* HERO */
.hero {
  background: linear-gradient(140deg,#0f2540 0%,#0e2d3a 100%);
  padding: 52px 24px 44px;
  text-align: center;
  border-bottom: 1px solid var(--border);
  position: relative; overflow: hidden;
}
.hero::before {
  content:''; position:absolute; width:500px; height:500px;
  background: radial-gradient(circle,rgba(56,178,172,.07) 0%,transparent 70%);
  top:-150px; left:50%; transform:translateX(-50%); pointer-events:none;
}
.badge {
  display:inline-block; background:rgba(56,178,172,.12);
  border:1px solid rgba(56,178,172,.25); border-radius:20px;
  padding:4px 14px; font-size:.72rem; color:var(--teal-light);
  letter-spacing:.08em; text-transform:uppercase; margin-bottom:16px;
}
.hero h1 { font-size: clamp(1.8rem,4vw,2.8rem); font-weight:700; line-height:1.15; margin-bottom:8px; }
.hero h1 span { color: var(--accent); }
.hero p { font-size:.95rem; color:var(--muted); max-width:520px; margin:0 auto; }

/* CARDS */
.card-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(260px,1fr)); gap:16px; margin-top:28px; }
.card {
  background:var(--surface); border:1px solid var(--border);
  border-radius:12px; padding:20px; text-decoration:none; color:inherit;
  transition:all .15s; display:block;
}
.card:hover { border-color:var(--accent); transform:translateY(-2px); box-shadow:0 8px 24px rgba(0,0,0,.3); }
.card-icon { font-size:1.6rem; margin-bottom:10px; }
.card-title { font-size:.95rem; font-weight:700; color:var(--text); margin-bottom:4px; }
.card-desc { font-size:.8rem; color:var(--muted); line-height:1.5; }

/* SECTION */
.section { margin-top:40px; }
.section-title { font-size:1.1rem; font-weight:700; color:var(--accent); margin-bottom:16px; padding-bottom:8px; border-bottom:1px solid var(--border); }

/* TABLE */
.styled-table { width:100%; border-collapse:collapse; font-size:.84rem; }
.styled-table th { background:#004B55; color:#fff; padding:10px 14px; text-align:left; font-size:.75rem; letter-spacing:.04em; }
.styled-table td { padding:10px 14px; border-bottom:1px solid var(--border); color:var(--muted); }
.styled-table td:first-child { color:var(--text); font-weight:600; }
.styled-table tr:nth-child(even) td { background:rgba(56,178,172,.04); }

/* TEAM CARD */
.team-card { background:var(--surface); border:1px solid var(--border); border-radius:12px; overflow:hidden; margin-bottom:20px; }
.team-header { background:var(--surface2); padding:14px 20px; display:flex; align-items:center; gap:14px; border-bottom:1px solid var(--border); }
.team-num { width:40px; height:40px; border-radius:10px; background:linear-gradient(135deg,#006D77,#38b2ac); display:flex; align-items:center; justify-content:center; font-weight:700; font-size:1rem; color:#fff; flex-shrink:0; }
.team-topic { font-size:.95rem; font-weight:700; color:var(--text); margin-bottom:2px; }
.team-ref { font-size:.76rem; color:var(--muted); font-style:italic; }
.team-body { padding:0 20px 16px; }

/* FIELD */
.f { display:flex; flex-direction:column; gap:4px; margin-bottom:12px; }
.f label { font-size:.7rem; text-transform:uppercase; letter-spacing:.07em; color:var(--muted); }
.f input, .f textarea, .f select {
  background:var(--surface2); border:1px solid var(--border); color:var(--text);
  border-radius:8px; padding:9px 12px; font-size:.88rem; font-family:inherit;
  resize:vertical; outline:none; transition:border-color .15s; width:100%;
}
.f input:focus, .f textarea:focus, .f select:focus { border-color:var(--accent); background:rgba(56,178,172,.05); }

/* SAVE BAR */
.save-bar {
  position:fixed; bottom:20px; right:20px;
  display:flex; gap:8px; z-index:50;
}
.btn-save-float {
  padding:10px 20px; border-radius:10px; border:none; cursor:pointer;
  font-size:.82rem; font-weight:600;
  background:linear-gradient(135deg,#1a6fa3,#38b2ac); color:#fff;
  box-shadow:0 4px 16px rgba(0,0,0,.4); transition:all .15s;
}
.btn-save-float:hover { opacity:.9; transform:translateY(-1px); }
.save-toast { padding:10px 16px; border-radius:10px; background:var(--surface); border:1px solid var(--accent); color:var(--accent); font-size:.8rem; font-weight:600; box-shadow:0 4px 16px rgba(0,0,0,.4); display:none; align-items:center; }
.save-toast.show { display:flex; }

/* PRINT */
@media print {
  nav, .save-bar { display:none !important; }
  body { background:#fff; color:#111; }
  .hero { background:#006D77 !important; print-color-adjust:exact; -webkit-print-color-adjust:exact; }
  .hero h1, .hero p, .badge { color:#fff !important; }
  .card, .team-card, .section { background:#fff !important; border:1px solid #ddd !important; }
  .f input, .f textarea { border:none !important; border-bottom:1px solid #bbb !important; background:transparent !important; color:#111 !important; }
}
"""

def nav(active_file):
    links = ""
    for href, icon, label in NAV_LINKS:
        cls = "nav-link active" if href == active_file else "nav-link"
        links += f'<a href="{href}" class="{cls}">{icon} {label}</a>\n'
    return f"""
<nav>
  <a class="nav-brand" href="index.html">
    <div class="nav-icon">♥</div>
    <span class="nav-brand-text">HRV Biofeedback Course</span>
  </a>
  <div class="nav-links">{links}</div>
</nav>"""

def page(title, active_file, body, extra_css="", extra_js=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — HRV Biofeedback Course 2026</title>
<style>{SHARED_CSS}{extra_css}</style>
</head>
<body>
{nav(active_file)}
{body}
{extra_js}
</body>
</html>"""

# ── INDEX ─────────────────────────────────────────────────────────────────────

def make_index():
    VIDEO_ID = "1J29DV_VXMK5kCiUxLkYhR4Nd0B5uERH9"
    video_section = f"""
<div class="section">
  <div class="section-title">Introduction video</div>
  <div class="video-wrap">
    <iframe class="video"
      src="https://drive.google.com/file/d/{VIDEO_ID}/preview"
      allow="autoplay"
      allowfullscreen
      title="Course introduction">
    </iframe>
  </div>
</div>"""

    schedule_rows = """
<tr><td>May 14–20</td><td>Meeting 0</td><td>Team launch, charter, check-in pairs — online</td></tr>
<tr><td>May 21</td><td>Session 1</td><td>HRV biofeedback introduction — on-site Reykjavík</td></tr>
<tr><td>May 21–26</td><td>Meeting 1</td><td>Session 1 debrief, first reflections, teaching prep — online</td></tr>
<tr><td>May 27</td><td>Session 2</td><td>Team teaching — on-site Reykjavík</td></tr>
<tr><td>May 27–31</td><td>Meeting 2</td><td>Teaching debrief, HRV Week 2, experiment design — online</td></tr>
<tr><td>June 1–5</td><td>Session 3</td><td>On-site intensive — Reykjavík</td></tr>
<tr><td>June 6–10</td><td>Meeting 3</td><td>Post on-site debrief, data analysis, capstone start — online</td></tr>
<tr><td>June 10–15</td><td>Meeting 4</td><td>Report week, project tracker, presentation prep — online</td></tr>
<tr><td>June 15–16</td><td>Meeting 5</td><td>Final meeting, presentations, celebration — on-site</td></tr>"""

    body = f"""
<div class="hero">
  <div class="badge">NeurotechEU Summer School · May–June 2026</div>
  <h1>Applied Psychophysiology<br><span>&amp; Biofeedback</span></h1>
  <p>Your interactive course workspace · HRV practice · team collaboration · teaching &amp; research</p>
</div>
<div class="page">
  <div class="card-grid">
    <a class="card" href="individual.html">
      <div class="card-icon">📓</div>
      <div class="card-title">My Individual Workbook</div>
      <div class="card-desc">5-week HRV practice log, reflection exercises, implementation planning</div>
    </a>
    <a class="card" href="team-workbook.html">
      <div class="card-icon">📋</div>
      <div class="card-title">Team Workbook</div>
      <div class="card-desc">Interactive team workspace for all 6 meetings — editable, auto-saved</div>
    </a>
    <a class="card" href="teams.html">
      <div class="card-icon">👥</div>
      <div class="card-title">Teams &amp; Assignments</div>
      <div class="card-desc">Team members, teaching topics, and suggested starting references</div>
    </a>
    <a class="card" href="readings.html">
      <div class="card-icon">📚</div>
      <div class="card-title">Course Materials</div>
      <div class="card-desc">Curriculum, reading for Session 1, and course resources</div>
    </a>
  </div>

  {video_section}

  <div class="section">
    <div class="section-title">Course Schedule</div>
    <table class="styled-table">
      <thead><tr><th>Dates</th><th>Event</th><th>What</th></tr></thead>
      <tbody>{schedule_rows}</tbody>
    </table>
  </div>

  <div class="section">
    <div class="section-title">Practical information</div>
    <div class="info-grid">
      <div class="info-item"><span class="info-label">Instructor</span><span class="info-val">Sigrún Þóra Sveinsdóttir · Reykjavík University</span></div>
      <div class="info-item"><span class="info-label">Contact</span><span class="info-val"><a href="mailto:sigrunths@ru.is" style="color:var(--accent)">sigrunths@ru.is</a></span></div>
      <div class="info-item"><span class="info-label">HRV app</span><span class="info-val">FlowMD — download before Session 1</span></div>
      <div class="info-item"><span class="info-label">Breathing tool</span><span class="info-val">Built into the workbooks — no app needed</span></div>
      <div class="info-item"><span class="info-label">Assessment</span><span class="info-val">Completed team workbook + individual workbook + capstone report</span></div>
      <div class="info-item"><span class="info-label">Canvas</span><span class="info-val">All submissions via Canvas Module 1</span></div>
    </div>
  </div>
</div>"""

    extra_css = """
.video-wrap { margin-top: 12px; }
.video-placeholder {
  background: var(--surface); border: 2px dashed var(--border);
  border-radius: 12px; padding: 48px; text-align: center;
  display: flex; flex-direction: column; align-items: center; gap: 8px;
}
iframe.video { width: 100%; height: 420px; border: none; border-radius: 12px; }
.vp-icon { font-size: 2.5rem; opacity: .4; }
.vp-text { color: var(--muted); font-weight: 600; }
.vp-sub { color: var(--muted); font-size: .75rem; opacity: .7; }
.info-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
.info-item { background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 12px 16px; display: flex; flex-direction: column; gap: 3px; }
.info-label { font-size: .68rem; text-transform: uppercase; letter-spacing: .08em; color: var(--muted); }
.info-val { font-size: .88rem; color: var(--text); }
"""
    return page("Home", "index.html", body, extra_css)

# ── TEAMS ─────────────────────────────────────────────────────────────────────

TEAMS = [
    ("1", "Neurofeedback: mechanisms and applications",
     "Hammond (2011); Arns et al. (2014)",
     [("Felicia Alw","Medical Biotechnology","KTH Royal Institute of Technology","Master"),
      ("Dragoș Mihai Corcan","Neuroscience","UMF Iuliu Hațieganu Cluj-Napoca","PhD"),
      ("Kübra Eren","Biomedical Engineering / Neuroengineering","Boğaziçi University","PhD"),
      ("Ilenia Bonini","Autonomic Nervous System","Medical University Innsbruck","Master")]),
    ("2", "EMG biofeedback and the body in stress",
     "Peper et al. (2016); Whatmore & Kohli (1968)",
     [("Lars Baumann","Medical Engineering","KTH Stockholm","Master"),
      ("Elena Richert","Psychology","Reykjavik University","PhD"),
      ("Ana Chirakadze","Clinical Psychology & Cognitive Neuropsychology","Karolinska Institutet","Master"),
      ("Andreea Mihaela Barb","Medicine",'"Iuliu Hațieganu" University of Medicine','PhD')]),
    ("3", "Interoception: what it is and why it matters",
     "Craig (2002); Garfinkel & Critchley (2013)",
     [("Clara Maria Azzano","Medical Engineering","KTH Royal Institute of Technology","Master"),
      ("Noé Gouwy","Neuropsychology / Cognitive Sciences","Université de Lille","Master"),
      ("Negar Kazemi","Molecular Medicine","Medical University of Innsbruck","Master"),
      ("Márk Komóczi","Health Sciences","University of Debrecen","PhD")]),
    ("4", "Skin conductance and sympathetic arousal",
     "Dawson et al. (2017) — Handbook of Psychophysiology",
     [("Saumya Roy","Data-Driven Health","KTH Royal Institute of Technology","Master"),
      ("Sonia-Stefania Tivadar","Neuroscience",'UMF "Iuliu Hațieganu" Cluj-Napoca',"PhD"),
      ("Alice Vaccaro","Psychology / Applied Behaviour Analysis","Université de Lille","Master"),
      ("María Sanchez Bonmati","Pharmacy and Nutrition","UMH Universidad Miguel Hernández","PhD")]),
    ("5", "Thermal biofeedback and peripheral regulation",
     "Shellenberger & Green (1986); Schwartz & Andrasik (2017)",
     [("Lalith Rahul Murugan Palanisamy","Medical Engineering","KTH Royal Institute of Technology","Master"),
      ("Zhe Xu","Innovative Technology for Healthy Living","KTH Royal Institute of Technology","Master"),
      ("Fatemeh Safarmohammadloo","Neurosciences","University of Bonn","Master"),
      ("Konstantin Popov","Sleep Medicine","Reykjavik University","PhD"),
      ("Denisa Teodorescu","Medicine","Iuliu Hațieganu University of Medicine","PhD")]),
    ("6", "Biofeedback in sport and performance",
     "Blumenstein & Orbach (2014); Lagos et al. (2008)",
     [("Candela Martinez Rodriguez","Sports Technology","KTH Royal Institute of Technology","Master"),
      ("Noah Vastmans","Sports Technology","KTH","Master"),
      ("Aleksandr Maksimov","Neuroscience","University of Bonn","Master"),
      ("Yagmur Can Altundas","Biomedical Engineering","Bogazici University","PhD"),
      ("Larisa-Ioana Sabau","Medicine","Iuliu Hațieganu University of Medicine","PhD")]),
]

def make_teams():
    cards = ""
    for num, topic, refs, members in TEAMS:
        rows = "".join(
            f"<tr><td>{n}</td><td>{field}</td><td>{uni}</td><td>{level}</td></tr>"
            for n, field, uni, level in members
        )
        cards += f"""
<div class="team-card">
  <div class="team-header">
    <div class="team-num">{num}</div>
    <div>
      <div class="team-topic">Group {num} — {topic}</div>
      <div class="team-ref">Starting point: {refs}</div>
    </div>
  </div>
  <div class="team-body">
    <table class="styled-table" style="margin-top:12px">
      <thead><tr><th>Name</th><th>Field</th><th>University</th><th>Level</th></tr></thead>
      <tbody>{rows}</tbody>
    </table>
  </div>
</div>"""

    body = f"""
<div class="hero" style="padding:36px 24px 28px">
  <div class="badge">Session 2 · May 27</div>
  <h1>Teams &amp; <span>Assignments</span></h1>
  <p>You have been assigned to an interdisciplinary team. Your team will meet before Session 1, work together throughout the course, and teach the full cohort in Session 2 on May 27.</p>
</div>
<div class="page">
  <div class="section">
    <div class="section-title">The 6 teams</div>
    {cards}
  </div>
  <div class="section">
    <p style="color:var(--muted);font-size:.85rem">Questions about your team? Contact: <a href="mailto:sigrunths@ru.is" style="color:var(--accent)">sigrunths@ru.is</a> · Team Workbook and Meeting 0 guide are in Canvas Module 1.</p>
  </div>
</div>"""
    return page("Teams & Assignments", "teams.html", body)

# ── READINGS ──────────────────────────────────────────────────────────────────

def make_readings():
    body = """
<div class="hero" style="padding:36px 24px 28px">
  <div class="badge">Course Materials</div>
  <h1>Readings &amp; <span>Resources</span></h1>
  <p>Course curriculum and required reading for Session 1</p>
</div>
<div class="page">
  <div class="section">
    <div class="section-title">Course Curriculum</div>
    <p style="color:var(--muted);font-size:.85rem;margin-bottom:12px">Full curriculum — Applied Psychophysiology & Biofeedback, May–June 2026</p>
    <div class="pdf-wrap">
      <iframe class="pdf-frame" src="assets/curriculum.pdf#toolbar=1&navpanes=0" title="Course Curriculum"></iframe>
    </div>
    <a class="dl-btn" href="assets/curriculum.pdf" download>⬇ Download curriculum PDF</a>
  </div>

  <div class="section">
    <div class="section-title">Required reading — Session 1</div>
    <div class="reading-card">
      <div class="reading-meta">Lehrer &amp; Gevirtz · 2014 · Frontiers in Psychology</div>
      <div class="reading-title">Heart Rate Variability Biofeedback: How Does It Work and Why?</div>
      <p class="reading-abs">This paper explains the physiological mechanisms behind HRV biofeedback — why breathing at resonance frequency maximises HRV, and what the evidence says about its clinical and performance effects. Read before Session 1 on May 21.</p>
    </div>
    <div class="pdf-wrap" style="margin-top:14px">
      <iframe class="pdf-frame" src="assets/lehrer-gevirtz-2014.pdf#toolbar=1&navpanes=0" title="Lehrer & Gevirtz 2014"></iframe>
    </div>
    <a class="dl-btn" href="assets/lehrer-gevirtz-2014.pdf" download>⬇ Download paper PDF</a>
  </div>
</div>"""

    extra_css = """
.pdf-wrap { width:100%; border-radius:10px; overflow:hidden; border:1px solid var(--border); margin-bottom:10px; }
.pdf-frame { width:100%; height:620px; border:none; background:#fff; }
.dl-btn {
  display:inline-flex; align-items:center; gap:6px;
  background:var(--surface); border:1px solid var(--border);
  color:var(--muted); border-radius:8px; padding:8px 16px;
  font-size:.8rem; text-decoration:none; transition:all .15s; margin-bottom:8px;
}
.dl-btn:hover { color:var(--text); border-color:var(--accent); }
.reading-card { background:var(--surface); border:1px solid var(--border); border-left:3px solid var(--accent); border-radius:8px; padding:16px 18px; }
.reading-meta { font-size:.72rem; color:var(--muted); text-transform:uppercase; letter-spacing:.06em; margin-bottom:4px; }
.reading-title { font-size:1rem; font-weight:700; color:var(--text); margin-bottom:8px; }
.reading-abs { font-size:.84rem; color:var(--muted); line-height:1.7; }
"""
    return page("Readings", "readings.html", body, extra_css)

# ── INDIVIDUAL WORKBOOK ───────────────────────────────────────────────────────

def make_individual():

    def f(id, label="", ph="", rows=2):
        tag = f'<input type="text" id="{id}" placeholder="{ph}" oninput="save()">' if rows==1 else f'<textarea id="{id}" rows="{rows}" placeholder="{ph}" oninput="save()"></textarea>'
        lbl = f'<label>{label}</label>' if label else ''
        return f'<div class="f">{lbl}{tag}</div>'

    def slider(id, label, lo, hi):
        return f"""
<div class="slider-wrap">
  <label>{label}</label>
  <div class="slider-row">
    <span class="sl-lo">{lo}</span>
    <input type="range" id="{id}" min="0" max="10" value="5" oninput="updateSlider('{id}');save()">
    <span class="sl-val" id="{id}_val">5</span>
    <span class="sl-hi">{hi}</span>
  </div>
</div>"""

    def week_log(wk, dates):
        days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
        rows = ""
        for d in days:
            rows += f"""<tr>
  <td>{d}</td>
  <td><select id="w{wk}_{d}_type" onchange="save()"><option>—</option><option>B</option><option>RF</option><option>S</option><option>RF+S</option></select></td>
  <td><input type="text" id="w{wk}_{d}_min" placeholder="–" oninput="save()"></td>
  <td><input type="text" id="w{wk}_{d}_rmssd" placeholder="–" oninput="save()"></td>
  <td><input type="text" id="w{wk}_{d}_lf_hf" placeholder="–" oninput="save()"></td>
  <td><input type="text" id="w{wk}_{d}_note" placeholder="note…" oninput="save()"></td>
</tr>"""
        return f"""
<div class="activity iw-card">
  <div class="iw-header">
    <span class="iw-num">Week {wk}</span>
    <span class="iw-title">{dates}</span>
  </div>
  <div class="iw-body">
    <p class="hint">Session types: <strong>B</strong> = Baseline · <strong>RF</strong> = Resonance Breathing (4 in / 6 out) · <strong>S</strong> = Stress Response · <strong>RF+S</strong> = Both</p>
    <div class="log-wrap">
      <table class="log-table">
        <thead><tr><th>Day</th><th>Type</th><th>Minutes</th><th>RMSSD</th><th>LF/HF</th><th>Notes</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
    {f(f"w{wk}_reflect","Weekly reflection — what did you notice?","One honest sentence…",rows=2)}
    {f(f"w{wk}_challenge","Biggest challenge this week:",ph="What made it harder?",rows=1)}
    {f(f"w{wk}_insight","Key insight or shift:",ph="Something you noticed or learned…",rows=1)}
  </div>
</div>"""

    pre_session = f"""
<div class="iw-section-label">Pre-session exercises · complete after Session 1 on May 21</div>

<div class="iw-card">
  <div class="iw-header"><span class="iw-num">1</span><span class="iw-title">Finding My Why</span></div>
  <div class="iw-body">
    {f("why_1","Why is managing your stress or physiological regulation important to you right now?",rows=3)}
    {f("why_2","What would be different in your daily life if you got better at this?",rows=2)}
    {f("why_3","In one sentence — my reason for doing this practice:",rows=1)}
  </div>
</div>

<div class="iw-card">
  <div class="iw-header"><span class="iw-num">2</span><span class="iw-title">Importance &amp; Confidence</span></div>
  <div class="iw-body">
    <p class="hint">Circle or mark your number on each scale (0 = not at all, 10 = extremely)</p>
    {slider("imp_scale","How important is it to you to do this HRV practice regularly?","Not important","Extremely important")}
    {slider("conf_scale","How confident are you that you can do it?","Not confident","Completely confident")}
    {f("imp_why","Why that number for importance — not lower?",rows=2)}
    {f("conf_why","What would help your confidence go up one point?",rows=2)}
  </div>
</div>

<div class="iw-card">
  <div class="iw-header"><span class="iw-num">3</span><span class="iw-title">Implementation Intention</span></div>
  <div class="iw-body">
    <p class="hint">Research shows that specifying WHEN, WHERE, and HOW makes you 2–3× more likely to follow through.</p>
    {f("impl_when","I will do my HRV practice at this time:","e.g. 7:30 am, right after I wake up",rows=1)}
    {f("impl_where","In this place:","e.g. at my desk, before opening my laptop",rows=1)}
    {f("impl_how","For this long, using:","e.g. 20 minutes using FlowMD with headphones",rows=1)}
    {f("impl_anchor","I will anchor it to (what do you always do before/after?):","e.g. After I make my morning coffee",rows=1)}
  </div>
</div>

<div class="iw-card">
  <div class="iw-header"><span class="iw-num">4</span><span class="iw-title">If-Then Barrier Planning</span></div>
  <div class="iw-body">
    <p class="hint">Barriers are predictable. Planning your response in advance makes you 2× more likely to overcome them.</p>
    {f("ifthen_1","If I feel too tired to practice, then I will…",rows=1)}
    {f("ifthen_2","If I skip a day, then I will…",rows=1)}
    {f("ifthen_3","If I feel like it is not working, then I will…",rows=1)}
    {f("ifthen_4","My biggest predicted barrier is… and I will handle it by…",rows=2)}
  </div>
</div>"""

    week5_reflect = f"""
<div class="iw-card">
  <div class="iw-header"><span class="iw-num">Week 5</span><span class="iw-title">Looking Back on 5 Weeks · June 15–17</span></div>
  <div class="iw-body">
    <div class="iw-section-label" style="margin-bottom:12px">Progress summary</div>
    <table class="log-table styled-table" style="margin-bottom:16px">
      <thead><tr><th>Week</th><th>Sessions completed</th><th>Average RMSSD</th><th>Key observation</th></tr></thead>
      <tbody>
        {''.join(f'<tr><td>Week {i}</td><td><input type="text" id="sum_w{i}_sessions" oninput="save()"></td><td><input type="text" id="sum_w{i}_rmssd" oninput="save()"></td><td><input type="text" id="sum_w{i}_obs" oninput="save()"></td></tr>' for i in range(1,6))}
      </tbody>
    </table>
    <div class="iw-section-label" style="margin-bottom:12px">Deep reflection</div>
    {f("ref_changed","What has changed — in your body, your mind, or your day — since you started?",rows=3)}
    {f("ref_surprised","What surprised you most about the practice?",rows=2)}
    {f("ref_hard","What was harder than you expected? What helped?",rows=2)}
    {f("ref_continue","How will you continue this practice after the course?",rows=2)}
    {f("ref_advice","What would you tell someone starting this practice tomorrow?",rows=2)}
    <div class="done-box" style="margin-top:16px">Thank you for showing up for yourself — every session, every week.<br><em>Sigrún Þóra Sveinsdóttir · Reykjavík University · NeurotechEU</em></div>
  </div>
</div>"""

    body = f"""
<div class="hero" style="padding:36px 24px 28px">
  <div class="badge">Individual Practice · 5 weeks</div>
  <h1>My HRV Practice <span>Workbook</span></h1>
  <p>Your personal record of 5 weeks of HRV biofeedback practice — fill in as you go</p>
</div>
<div class="page">
  <div class="iw-intro">
    <p>Over the next five weeks you will measure your heart rate variability (HRV) every day using the FlowMD app. This is not just data collection — it is a scientific experiment with you as both the researcher and the subject. This workbook is your personal record.</p>
  </div>

  {pre_session}

  <div class="iw-section-label" style="margin-top:32px">5-week practice log</div>
  {week_log(1,"May 21–27, 2026")}
  {week_log(2,"May 28 – June 3, 2026")}
  {week_log(3,"June 4–10, 2026")}
  {week_log(4,"June 11–14, 2026")}
  {week5_reflect}
</div>

<div class="save-bar">
  <div class="save-toast" id="toast">✓ Saved</div>
  <button class="btn-save-float" onclick="_doSave()">💾 Save</button>
  <button class="btn-save-float" style="background:var(--surface);border:1px solid var(--border);color:var(--muted)" onclick="window.print()">📄 PDF</button>
</div>"""

    extra_css = """
.iw-intro { background:var(--surface); border:1px solid var(--border); border-radius:10px; padding:16px 20px; margin-bottom:20px; color:var(--muted); font-size:.88rem; line-height:1.7; }
.iw-section-label { font-size:.72rem; text-transform:uppercase; letter-spacing:.09em; color:var(--accent); font-weight:700; margin-bottom:14px; }
.iw-card { background:var(--surface); border:1px solid var(--border); border-radius:12px; overflow:hidden; margin-bottom:16px; }
.iw-header { background:var(--surface2); padding:12px 18px; display:flex; align-items:center; gap:12px; border-bottom:1px solid var(--border); }
.iw-num { background:linear-gradient(135deg,#006D77,#38b2ac); color:#fff; border-radius:6px; padding:3px 10px; font-size:.75rem; font-weight:700; white-space:nowrap; }
.iw-title { font-size:.92rem; font-weight:700; color:var(--text); }
.iw-body { padding:16px 18px; display:flex; flex-direction:column; gap:12px; }
.hint { font-size:.8rem; color:var(--muted); font-style:italic; }

.slider-wrap { display:flex; flex-direction:column; gap:6px; }
.slider-wrap label { font-size:.72rem; text-transform:uppercase; letter-spacing:.07em; color:var(--muted); }
.slider-row { display:flex; align-items:center; gap:10px; }
.sl-lo, .sl-hi { font-size:.72rem; color:var(--muted); white-space:nowrap; min-width:80px; }
.sl-hi { text-align:right; }
.sl-val { font-size:1.2rem; font-weight:700; color:var(--accent); min-width:28px; text-align:center; }
input[type=range] { flex:1; accent-color:var(--accent); }

.log-wrap { overflow-x:auto; }
.log-table { width:100%; border-collapse:collapse; font-size:.82rem; min-width:520px; }
.log-table th { background:#004B55; color:#fff; padding:8px 10px; text-align:left; font-size:.72rem; letter-spacing:.04em; }
.log-table td { padding:6px 8px; border-bottom:1px solid var(--border); }
.log-table tr:nth-child(even) td { background:rgba(56,178,172,.04); }
.log-table input { width:100%; background:transparent; border:none; color:var(--text); font-size:.82rem; font-family:inherit; outline:none; }
.log-table input:focus { border-bottom:1px solid var(--accent); }
.log-table select { background:var(--surface2); border:1px solid var(--border); color:var(--text); border-radius:5px; padding:2px 5px; font-size:.78rem; }

.done-box { background:rgba(72,187,120,.08); border:1px solid rgba(72,187,120,.2); border-radius:10px; padding:16px 20px; text-align:center; color:#68d391; font-size:.88rem; }
.done-box em { display:block; margin-top:4px; font-size:.78rem; color:var(--muted); }
"""

    extra_js = """<script>
function updateSlider(id) {
  document.getElementById(id+'_val').textContent = document.getElementById(id).value;
}
function save() { clearTimeout(window._st); window._st = setTimeout(_doSave, 800); }
function _doSave() {
  const d = {};
  document.querySelectorAll('input[id],textarea[id],select[id]').forEach(el => { if(el.id) d[el.id]=el.value; });
  localStorage.setItem('iw_data', JSON.stringify(d));
  const t = document.getElementById('toast');
  if(t) { t.classList.add('show'); setTimeout(()=>t.classList.remove('show'),2000); }
}
function loadData() {
  const raw = localStorage.getItem('iw_data');
  if(!raw) return;
  try {
    const d = JSON.parse(raw);
    Object.entries(d).forEach(([id,val]) => {
      const el = document.getElementById(id);
      if(el) { el.value = val; if(el.type==='range') updateSlider(id); }
    });
  } catch(e) {}
}
document.addEventListener('DOMContentLoaded', loadData);
</script>"""

    return page("My Workbook", "individual.html", body, extra_css, extra_js)

# ── WRITE ALL FILES ────────────────────────────────────────────────────────────
files = {
    "index.html":      make_index(),
    "teams.html":      make_teams(),
    "readings.html":   make_readings(),
    "individual.html": make_individual(),
}

for fname, content in files.items():
    path = SITE / fname
    path.write_text(content, encoding='utf-8')
    print(f"  {fname}  ({path.stat().st_size // 1024} KB)")

print("\nDone. Open hrv-course-2026/index.html in a browser.")
