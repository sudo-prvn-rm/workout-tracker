import json

with open('/home/praveen/personal-projects/workout-tracker/workout_plan.json') as f:
    plan = json.load(f)

lines = []
lines.append("# 🏋️ 68-Day Lean & Muscular Transformation Curriculum")
lines.append("**Dates**: October 25, 2026 – December 31, 2026")
lines.append("**Equipment**: 2 Dumbbells (adjustable with 4x2kg + 3kg plates up to 10kg) + Progressive Calisthenics")
lines.append("**Schedule**: 60 min Morning (Strength/Hypertrophy) + 30 min Evening (Core/Mobility/Steps)")
lines.append("**Diet**: PG-Friendly Indian Budget Nutrition (2 Eggs/day, Sunday PG Chicken, Whey, Creatine, Soya/Chana/Dahi/Sattu)\n")
lines.append("---\n")

curr_phase = 0
for day in plan:
    if day['phase'] != curr_phase:
        curr_phase = day['phase']
        lines.append(f"\n## 🏆 {day['phaseName']}")
        lines.append(f"_{day['tempoNote']}_\n")

    lines.append(f"### Day {day['day']} · {day['weekday']}, {day['date']} — {day['title']}")
    lines.append(f"- **Focus**: {day['bodyPart']} · **Week**: {day['week']}")
    
    # Morning
    lines.append("\n#### ☀️ Morning Session (60 mins — Resistance Training)")
    for ex in day['morning']:
        yt_link = f"[{ex['ytLabel']}]({ex['yt']})" if ex.get('yt') else ""
        lines.append(f"- [ ] **{ex['name']}**: {ex['sets']} sets × {ex['reps']} | **Load**: {ex['load']} | **Tempo**: {ex['tempo']} | **Rest**: {ex['rest']} {yt_link}")
    
    # Evening
    lines.append("\n#### 🌙 Evening Session (30 mins — Core, Mobility & Steps)")
    e = day['evening']
    if 'core' in e and e['core']:
        c = e['core']
        c_yt = f"[{c['ytLabel']}]({c['yt']})" if c.get('yt') else ""
        lines.append(f"- [ ] **Core**: {c['name']} — {c['target']} {c_yt}")
    if 'mobility' in e and e['mobility']:
        m = e['mobility']
        m_yt = f"[{m['ytLabel']}]({m['yt']})" if m.get('yt') else ""
        lines.append(f"- [ ] **Mobility**: {m['name']} — {m['target']} {m_yt}")
    if 'cardio' in e and e['cardio']:
        cd = e['cardio']
        lines.append(f"- [ ] **Cardio/Steps**: {cd['name']} — {cd['target']}")

    # Nutrition
    n = day['nutrition']
    lines.append("\n#### 🥗 PG Nutrition & Supplement Protocol")
    lines.append(f"> **Highlight**: {n['highlight']}")
    lines.append(f"- **Breakfast**: {n['breakfast']}")
    lines.append(f"- **Lunch**: {n['lunch']}")
    lines.append(f"- **Snack**: {n['snack']}")
    lines.append(f"- **Dinner**: {n['dinner']}")
    lines.append(f"- **Supplements & Water**: {n['supplements']}")
    lines.append(f"- **Target Protein**: {n['estProtein']}\n")
    lines.append("---\n")

with open('/home/praveen/personal-projects/workout-tracker/curriculum.md', 'w') as f:
    f.write("\n".join(lines))

print("Generated curriculum.md successfully!")
