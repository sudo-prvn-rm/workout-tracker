# 🏋️ 68-Day Transformation Tracker (Lean & Muscular)
 
A daily workout, calisthenics, and PG-friendly budget nutrition tracker designed to build an aesthetic, lean, muscular physique from **October 25, 2026 to December 31, 2026** (68 days).

Designed specifically for home training with **2 dumbbells (up to 10kg)** and **calisthenics progressive overload**, paired with a **budget Indian PG meal protocol**.

---

## ⚡ Key Features

- **No Database Needed**: Works 100% out of the box in any browser using `localStorage`.
- **Automatic Date Detection**: Automatically detects today's date (`new Date()`) and anchors to **Today's Mission**.
- **Every Single Exercise has a Form Video**: Click `▶ Form Video` on any exercise for verified technique breakdowns from top science-based coaches (*Jeff Nippard, Athlean-X, Calisthenicmovement, Squat University, Jeremy Ethier*).
- **Morning & Evening Split**:
  - **Morning (60 min)**: Heavy mechanical tension, compound push/pull/legs, tempo lifts (3-1-1-0), and calisthenics.
  - **Evening (30 min)**: Core sculpting (stomach vacuums, hollow body holds, deadbugs), desk posture & hip mobility, and 3,000 brisk steps.
- **Strict PG-Friendly Nutrition Protocol**:
  - **2 Eggs Daily** (Monday to Saturday, ₹7/egg = ₹14/day).
  - **Sunday Chicken Special**: PG chicken feast on Sundays (eggs skipped on Sunday as scheduled).
  - **Whey Protein (1 scoop)** + **Creatine Monohydrate (3–5g daily)**.
  - **Hydration Tracker**: 4 interactive water badges (3.5L to 4.0L daily).
  - **Cheap Room-Storable Boosters**: Soya chunks (Nutrela), Roasted Bhuna Chana, Roasted Peanuts, Curd/Dahi, and Sattu.
- **Export / Import Backup**: 1-click JSON backup so you can transfer your streak between your phone and laptop without losing progress.
- **Interactive Filtering**: Filter by Phase (1–4), Body Split (Push, Pull, Legs, Upper, Recovery), Completion status, or search for any movement.

---

## 🚀 Quick Start

### Method 1: Open Directly in Browser (No Server Required!)
Simply double-click `index.html` or drag it into Chrome / Brave / Edge / Firefox / Safari. Everything runs client-side with full persistence.

### Method 2: Local Development Server
```bash
node server.js
```
Open **[http://localhost:3000](http://localhost:3000)** in your browser.
*(Running locally will also auto-sync completed tasks to `progress.json` on disk).*

---

## 📅 The 10-Week / 4-Phase Periodization

```
Oct 25 ────────────────────────────────────────────────────────► Dec 31, 2026
[ Phase 1: Foundation ] ──► [ Phase 2: Hypertrophy ] ──► [ Phase 3: Density ] ──► [ Phase 4: V-Taper ]
    Days 1–14 (2 wks)           Days 15–35 (3 wks)          Days 36–56 (3 wks)        Days 57–68 (12 days)
```

| Phase | Days | Date Range | Primary Focus |
| :--- | :--- | :--- | :--- |
| **Phase 1: Foundation & Saturation** | Days 1–14 | Oct 25 – Nov 7 | Movement mechanics, tendon adaptation, strict 3s eccentric tempo, Creatine saturation. |
| **Phase 2: Hypertrophy & Volume** | Days 15–35 | Nov 8 – Nov 28 | Progressive volume overload (4 sets), unilateral overload (Bulgarian split squats, single arm rows). |
| **Phase 3: Density & Drop Sets** | Days 36–56 | Nov 29 – Dec 19 | Mechanical advantage drop sets, bicep/tricep supersets, metabolic stress. |
| **Phase 4: Peak Definition & V-Taper**| Days 57–68 | Dec 20 – Dec 31 | Lateral delt caps, upper chest pop, transverse abdominis stomach vacuums, lean aesthetic finish. |

---

## 🌐 Deploy to Vercel (100% Free)

1. Push your repository to GitHub:
   ```bash
   git add .
   git commit -m "feat: 68-day lean transformation tracker"
   git push origin main
   ```
2. Go to [vercel.com](https://vercel.com) and import the repository.
3. Deploy! You will get a permanent public URL (e.g. `https://workout-tracker.vercel.app`).
   - Your progress will be saved in your browser's `localStorage` on whatever device you open it on.
   - Use the **📥 Export Backup** and **📤 Import Backup** buttons in the header to effortlessly sync data between your mobile phone and laptop.
   - *(Optional)*: If you want automatic cross-device cloud sync, add a free PostgreSQL `DB_URL` (from [Neon.tech](https://neon.tech) or [Supabase](https://supabase.com)) in Vercel Environment Variables.

---

## 📂 File Structure

```
workout-tracker/
├── index.html              # Main interactive dark dashboard (zero dependencies)
├── workout_data.js         # Complete 68-day structured dataset
├── workout_plan.json       # JSON dataset export
├── curriculum.md           # Full 68-day workout & diet reading curriculum
├── server.js               # Node.js server with local progress.json sync
├── package.json            # Project manifest
├── .env.example            # Environment configuration template
└── README.md               # Documentation
```
