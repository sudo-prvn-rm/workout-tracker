import datetime
import json

start_date = datetime.date(2026, 10, 25)
end_date = datetime.date(2026, 12, 31)

# Exercise Library with verified video links
VIDEOS = {
    "standard_pushup": {"name": "Deficit / Standard Push-ups", "yt": "https://www.youtube.com/watch?v=IODxDxX7oi4", "ytLabel": "Calisthenicmovement — Perfect Push-Up Form"},
    "db_floor_press": {"name": "Dumbbell Floor Press", "yt": "https://www.youtube.com/watch?v=uUGDRwG4Fjs", "ytLabel": "Athlean-X — Dumbbell Floor Press Guide"},
    "db_hex_press": {"name": "Dumbbell Hex Press (Inner Chest Squeeze)", "yt": "https://www.youtube.com/watch?v=oB9_d9U_Kkg", "ytLabel": "Scott Herman — Hex Press for Chest"},
    "decline_pushup": {"name": "Feet-Elevated Decline Push-ups", "yt": "https://www.youtube.com/watch?v=SKPab2YC8BE", "ytLabel": "Calisthenicmovement — Decline Push-Ups (Upper Chest)"},
    "db_shoulder_press": {"name": "Seated/Standing DB Overhead Press", "yt": "https://www.youtube.com/watch?v=qEwKCR5JCog", "ytLabel": "Scott Herman — DB Shoulder Press Form"},
    "db_arnold_press": {"name": "Dumbbell Arnold Press", "yt": "https://www.youtube.com/watch?v=6Z15_WdXmVw", "ytLabel": "Scott Herman — Arnold Press Technique"},
    "db_lateral_raise": {"name": "Strict DB Lateral Raise (Side Delts)", "yt": "https://www.youtube.com/watch?v=3VcKaXpzqRo", "ytLabel": "Jeff Nippard — Science of Lateral Raises"},
    "pike_pushup": {"name": "Pike Push-ups (Vertical Push)", "yt": "https://www.youtube.com/watch?v=sposDXWEB0A", "ytLabel": "Calisthenicmovement — Pike Push-Ups"},
    "db_overhead_tricep": {"name": "Overhead DB Tricep Extension", "yt": "https://www.youtube.com/watch?v=_gsUck-7M74", "ytLabel": "Scott Herman — Overhead Tricep Extension"},
    "chair_dips": {"name": "Chair / Bed Bench Dips", "yt": "https://www.youtube.com/watch?v=0326dy_-CzM", "ytLabel": "Calisthenicmovement — Bench Dips Technique"},
    "diamond_pushup": {"name": "Diamond Push-ups (Tricep Overload)", "yt": "https://www.youtube.com/watch?v=J0DnG1_S92I", "ytLabel": "Calisthenicmovement — Diamond Push-Ups"},
    
    # PULL
    "single_arm_row": {"name": "Single-Arm Dumbbell Row", "yt": "https://www.youtube.com/watch?v=pYcpY20QaE8", "ytLabel": "Athlean-X — Perfect Single-Arm DB Row"},
    "two_arm_db_row": {"name": "Bent-Over Two-Arm DB Row", "yt": "https://www.youtube.com/watch?v=6TSP13BISI4", "ytLabel": "Scott Herman — Bent Over DB Row"},
    "inverted_towel_row": {"name": "Inverted Door/Towel Row", "yt": "https://www.youtube.com/watch?v=rloXYB8M3vU", "ytLabel": "Calisthenicmovement — Door Towel Rows"},
    "db_rear_delt_fly": {"name": "Bent-Over DB Rear Delt Flyes", "yt": "https://www.youtube.com/watch?v=eaun65zHk2c", "ytLabel": "Athlean-X — Rear Delt Flyes"},
    "db_shrugs": {"name": "Dumbbell Shrugs (Upper Traps)", "yt": "https://www.youtube.com/watch?v=cJRVVxmytaM", "ytLabel": "Scott Herman — Dumbbell Shrugs"},
    "db_bicep_curl": {"name": "Strict Supinating DB Bicep Curl", "yt": "https://www.youtube.com/watch?v=in7PaeYlhrM", "ytLabel": "Jeff Nippard — Bicep Hypertrophy Science"},
    "db_hammer_curl": {"name": "Neutral Grip DB Hammer Curl", "yt": "https://www.youtube.com/watch?v=zC3nLlEvin4", "ytLabel": "Scott Herman — Hammer Curl Form"},
    "db_concentration_curl": {"name": "Seated Concentration Curl", "yt": "https://www.youtube.com/watch?v=0AUGkch3tzc", "ytLabel": "Scott Herman — Concentration Curl"},

    # LEGS
    "bulgarian_split_squat": {"name": "Bulgarian Split Squat", "yt": "https://www.youtube.com/watch?v=1CVecvh_6W0", "ytLabel": "Squat University — Bulgarian Split Squat"},
    "db_rdl": {"name": "Dumbbell Romanian Deadlift (RDL)", "yt": "https://www.youtube.com/watch?v=_oyxCn2iSjU", "ytLabel": "Jeremy Ethier — Dumbbell RDL Form"},
    "db_goblet_squat": {"name": "Dumbbell Goblet Squat", "yt": "https://www.youtube.com/watch?v=MeIiIdhvXT4", "ytLabel": "Athlean-X — Goblet Squat Mastery"},
    "walking_lunges": {"name": "Dumbbell Walking Lunges", "yt": "https://www.youtube.com/watch?v=L8fvypPrzzs", "ytLabel": "Scott Herman — Walking Lunges"},
    "single_leg_rdl": {"name": "Single-Leg DB Romanian Deadlift", "yt": "https://www.youtube.com/watch?v=2Tz8lWzL5Kk", "ytLabel": "Squat University — Single Leg RDL"},
    "single_leg_calf_raise": {"name": "Single-Leg Deficit Calf Raise", "yt": "https://www.youtube.com/watch?v=f2w8v8P7kio", "ytLabel": "Jeff Nippard — Calf Growth Guide"},
    "glute_bridge": {"name": "Weighted Glute Bridge / Hip Thrust", "yt": "https://www.youtube.com/watch?v=8bbE64NuDTU", "ytLabel": "Jeremy Ethier — Glute Bridge & Hip Thrust"},
    "db_sumo_squat": {"name": "Dumbbell Sumo Squat (Adductors & Glutes)", "yt": "https://www.youtube.com/watch?v=9ZuD8vf6nSU", "ytLabel": "Scott Herman — Sumo Squat Technique"},

    # CORE & MOBILITY
    "stomach_vacuum": {"name": "Transverse Abdominis Stomach Vacuum", "yt": "https://www.youtube.com/watch?v=c3-e2u0l1dM", "ytLabel": "Jeremy Ethier — Stomach Vacuum for Slim Waist"},
    "hollow_body": {"name": "Hollow Body Hold", "yt": "https://www.youtube.com/watch?v=44ScXWFaVBs", "ytLabel": "Calisthenicmovement — Hollow Body Hold"},
    "deadbug": {"name": "Deadbug Core Stabilization", "yt": "https://www.youtube.com/watch?v=g_BYB0R-44A", "ytLabel": "Squat University — Deadbug Core Form"},
    "lying_leg_raise": {"name": "Lying Leg Raises & Reverse Crunches", "yt": "https://www.youtube.com/watch?v=Pr1ieGZ5atk", "ytLabel": "Calisthenicmovement — Leg Raises"},
    "rkc_plank": {"name": "Hardstyle RKC Plank (Maximum Tension)", "yt": "https://www.youtube.com/watch?v=TvxNkmjdhMM", "ytLabel": "Calisthenicmovement — Proper Plank Form"},
    "bird_dog": {"name": "Bird-Dog Core & Lower Back Flow", "yt": "https://www.youtube.com/watch?v=wiFNA3sqjCA", "ytLabel": "Squat University — Bird Dog Form"},
    "couch_stretch": {"name": "Couch Stretch (Hip Flexor & Psoas Opener)", "yt": "https://www.youtube.com/watch?v=Kz60qV1gU2o", "ytLabel": "Squat University — Couch Stretch"},
    "t_spine_opener": {"name": "Thoracic Spine Mobility & Desk Posture", "yt": "https://www.youtube.com/watch?v=0h5c5lQvB1c", "ytLabel": "Squat University — Thoracic Mobility"},
    "worlds_greatest_stretch": {"name": "World's Greatest Stretch Routine", "yt": "https://www.youtube.com/watch?v=4sQ9vQf0sXg", "ytLabel": "Squat University — World's Greatest Stretch"}
}

days_data = []
curr = start_date
day_num = 1

while curr <= end_date:
    date_str = curr.strftime("%Y-%m-%d")
    weekday_str = curr.strftime("%A")
    week_num = (day_num - 1) // 7 + 1
    
    # Phase calculation
    if day_num <= 14:
        phase = 1
        phase_name = "Phase 1 — Foundation & Creatine Saturation"
        tempo_note = "Focus: 3s eccentric descent, strict form, 2 RIR."
        rest_time = "75s"
        sets_count = 3
    elif day_num <= 35:
        phase = 2
        phase_name = "Phase 2 — Hypertrophy & Progressive Volume Overload"
        tempo_note = "Focus: 3-1-1-0 tempo, 1s pause at peak, 1–2 RIR."
        rest_time = "60–75s"
        sets_count = 4
    elif day_num <= 56:
        phase = 3
        phase_name = "Phase 3 — Mechanical Density & Calisthenics Mastery"
        tempo_note = "Focus: High tension, mechanical drop sets, 0–1 RIR."
        rest_time = "60s"
        sets_count = 4
    else:
        phase = 4
        phase_name = "Phase 4 — Peak Muscular Definition & V-Taper"
        tempo_note = "Focus: Peak definition, density supersets, strict mind-muscle connection."
        rest_time = "45–60s"
        sets_count = 4

    day_of_cycle = (day_num - 1) % 7 # 0=Sun, 1=Mon, 2=Tue, 3=Wed, 4=Thu, 5=Fri, 6=Sat

    # Build morning workout
    morning_exercises = []
    evening_routine = {}
    nutrition = {}
    body_part = ""
    title = ""

    if day_of_cycle == 0:  # Sunday
        body_part = "Push"
        title = "Push Hypertrophy & Chest Ignition"
        morning_exercises = [
            {"id": f"m_{day_num}_1", "name": VIDEOS["standard_pushup"]["name"], "sets": sets_count, "reps": "12–15 reps", "load": "Bodyweight", "tempo": "3-1-1-0", "rest": rest_time, "yt": VIDEOS["standard_pushup"]["yt"], "ytLabel": VIDEOS["standard_pushup"]["ytLabel"]},
            {"id": f"m_{day_num}_2", "name": VIDEOS["db_floor_press"]["name"], "sets": sets_count, "reps": "10–12 reps", "load": "2x 10kg (or 2x 5kg)", "tempo": "3-1-1-0", "rest": rest_time, "yt": VIDEOS["db_floor_press"]["yt"], "ytLabel": VIDEOS["db_floor_press"]["ytLabel"]},
            {"id": f"m_{day_num}_3", "name": VIDEOS["db_shoulder_press"]["name"], "sets": sets_count, "reps": "10–12 reps", "load": "2x 5kg or 2x 10kg", "tempo": "3-0-1-0", "rest": rest_time, "yt": VIDEOS["db_shoulder_press"]["yt"], "ytLabel": VIDEOS["db_shoulder_press"]["ytLabel"]},
            {"id": f"m_{day_num}_4", "name": VIDEOS["db_lateral_raise"]["name"], "sets": sets_count + 1, "reps": "12–15 reps", "load": "2x 4kg or 2x 5kg", "tempo": "3-1-1-0 (Elbows lead)", "rest": "60s", "yt": VIDEOS["db_lateral_raise"]["yt"], "ytLabel": VIDEOS["db_lateral_raise"]["ytLabel"]},
            {"id": f"m_{day_num}_5", "name": VIDEOS["db_overhead_tricep"]["name"], "sets": sets_count, "reps": "12 reps", "load": "1x 10kg (both hands)", "tempo": "3-1-1-0", "rest": "60s", "yt": VIDEOS["db_overhead_tricep"]["yt"], "ytLabel": VIDEOS["db_overhead_tricep"]["ytLabel"]}
        ]
        evening_routine = {
            "core": {"id": f"e_{day_num}_1", "name": VIDEOS["stomach_vacuum"]["name"], "target": "4 sets x 20–25s vacuum hold on empty stomach", "yt": VIDEOS["stomach_vacuum"]["yt"], "ytLabel": VIDEOS["stomach_vacuum"]["ytLabel"]},
            "mobility": {"id": f"e_{day_num}_2", "name": VIDEOS["couch_stretch"]["name"], "target": "2 mins each side (opens tight hip flexors)", "yt": VIDEOS["couch_stretch"]["yt"], "ytLabel": VIDEOS["couch_stretch"]["ytLabel"]},
            "cardio": {"id": f"e_{day_num}_3", "name": "Brisk Evening Walk", "target": "25 mins (approx 3,000 steps) for recovery & digestion", "yt": None, "ytLabel": None}
        }
        nutrition = {
            "isSunday": True,
            "highlight": "🍗 PG Sunday Special Chicken Feast! (Eggs skipped today as requested)",
            "breakfast": "PG Breakfast + 1 glass Milk + 1 Banana",
            "lunch": "PG Mess Lunch (Rice, Dal, Sabzi, Curd/Dahi)",
            "snack": "1 Scoop Whey Protein + 35g Roasted Chana (pre/post workout)",
            "dinner": "PG Chicken Curry / Chicken Dinner (3–4 rotis + chicken portion for high protein)",
            "supplements": "Creatine 3–5g (mix with warm water or lunch) · 3.5L Water target",
            "estProtein": "~115–125g"
        }

    elif day_of_cycle == 1:  # Monday
        body_part = "Pull"
        title = "Pull Hypertrophy & V-Taper Lats"
        morning_exercises = [
            {"id": f"m_{day_num}_1", "name": VIDEOS["single_arm_row"]["name"], "sets": sets_count, "reps": "12–15 reps / side", "load": "1x 10kg", "tempo": "3-1-1-0 (1s squeeze at top)", "rest": rest_time, "yt": VIDEOS["single_arm_row"]["yt"], "ytLabel": VIDEOS["single_arm_row"]["ytLabel"]},
            {"id": f"m_{day_num}_2", "name": VIDEOS["inverted_towel_row"]["name"], "sets": sets_count, "reps": "10–12 reps", "load": "Bodyweight (Door/Towel)", "tempo": "2-1-1-0", "rest": rest_time, "yt": VIDEOS["inverted_towel_row"]["yt"], "ytLabel": VIDEOS["inverted_towel_row"]["ytLabel"]},
            {"id": f"m_{day_num}_3", "name": VIDEOS["db_rear_delt_fly"]["name"], "sets": sets_count + 1, "reps": "15 reps", "load": "2x 4kg or 2x 5kg", "tempo": "3-1-1-0", "rest": "60s", "yt": VIDEOS["db_rear_delt_fly"]["yt"], "ytLabel": VIDEOS["db_rear_delt_fly"]["ytLabel"]},
            {"id": f"m_{day_num}_4", "name": VIDEOS["db_bicep_curl"]["name"], "sets": sets_count, "reps": "10–12 reps", "load": "2x 5kg or 2x 10kg", "tempo": "3-1-1-0 (Supinate wrist)", "rest": "60s", "yt": VIDEOS["db_bicep_curl"]["yt"], "ytLabel": VIDEOS["db_bicep_curl"]["ytLabel"]},
            {"id": f"m_{day_num}_5", "name": VIDEOS["db_hammer_curl"]["name"], "sets": sets_count, "reps": "10–12 reps", "load": "2x 5kg or 2x 10kg", "tempo": "3-0-1-0", "rest": "60s", "yt": VIDEOS["db_hammer_curl"]["yt"], "ytLabel": VIDEOS["db_hammer_curl"]["ytLabel"]}
        ]
        evening_routine = {
            "core": {"id": f"e_{day_num}_1", "name": VIDEOS["deadbug"]["name"], "target": "3 sets x 12 reps per side (Anti-extension core)", "yt": VIDEOS["deadbug"]["yt"], "ytLabel": VIDEOS["deadbug"]["ytLabel"]},
            "mobility": {"id": f"e_{day_num}_2", "name": VIDEOS["t_spine_opener"]["name"], "target": "3 mins thoracic spine rotations (fixes desk posture)", "yt": VIDEOS["t_spine_opener"]["yt"], "ytLabel": VIDEOS["t_spine_opener"]["ytLabel"]},
            "cardio": {"id": f"e_{day_num}_3", "name": "Brisk Evening Walk", "target": "25 mins (approx 3,000 steps)", "yt": None, "ytLabel": None}
        }
        nutrition = {
            "isSunday": False,
            "highlight": "🥚 2 Boiled Eggs + Soya Chunks Powerhouse (~115g Protein)",
            "breakfast": "2 Whole Boiled Eggs (₹14) + PG Breakfast + 1 Banana",
            "lunch": "PG Mess Lunch (2–3 Rotis, Rice, 2 katoris Dal, Sabzi)",
            "snack": "1 Scoop Whey Protein + 40g Roasted Bhuna Chana",
            "dinner": "35–40g Soya Chunks (boiled with salt) added to PG Dal/Sabzi + 3 Rotis",
            "supplements": "Creatine 3–5g with water · 3.5–4.0L Water target",
            "estProtein": "~115–122g"
        }

    elif day_of_cycle == 2:  # Tuesday
        body_part = "Legs"
        title = "Legs & Posterior Chain Hypertrophy"
        morning_exercises = [
            {"id": f"m_{day_num}_1", "name": VIDEOS["bulgarian_split_squat"]["name"], "sets": sets_count, "reps": "10–12 reps / leg", "load": "1x 10kg (Goblet) or 2x 5kg", "tempo": "3-1-1-0 (Deep hip crease)", "rest": "90s", "yt": VIDEOS["bulgarian_split_squat"]["yt"], "ytLabel": VIDEOS["bulgarian_split_squat"]["ytLabel"]},
            {"id": f"m_{day_num}_2", "name": VIDEOS["db_rdl"]["name"], "sets": sets_count, "reps": "10–12 reps", "load": "2x 10kg", "tempo": "4-1-1-0 (Deep hamstring stretch)", "rest": rest_time, "yt": VIDEOS["db_rdl"]["yt"], "ytLabel": VIDEOS["db_rdl"]["ytLabel"]},
            {"id": f"m_{day_num}_3", "name": VIDEOS["db_goblet_squat"]["name"], "sets": sets_count, "reps": "12–15 reps", "load": "1x 10kg", "tempo": "3-1-1-0", "rest": rest_time, "yt": VIDEOS["db_goblet_squat"]["yt"], "ytLabel": VIDEOS["db_goblet_squat"]["ytLabel"]},
            {"id": f"m_{day_num}_4", "name": VIDEOS["glute_bridge"]["name"], "sets": sets_count, "reps": "15 reps", "load": "1x 10kg on hips", "tempo": "2-2-1-0 (2s hold at peak)", "rest": "60s", "yt": VIDEOS["glute_bridge"]["yt"], "ytLabel": VIDEOS["glute_bridge"]["ytLabel"]},
            {"id": f"m_{day_num}_5", "name": VIDEOS["single_leg_calf_raise"]["name"], "sets": sets_count + 1, "reps": "15–20 reps / leg", "load": "1x 10kg in hand (Book/step)", "tempo": "3-2-1-0 (2s full stretch at bottom)", "rest": "45s", "yt": VIDEOS["single_leg_calf_raise"]["yt"], "ytLabel": VIDEOS["single_leg_calf_raise"]["ytLabel"]}
        ]
        evening_routine = {
            "core": {"id": f"e_{day_num}_1", "name": VIDEOS["lying_leg_raise"]["name"], "target": "3 sets x 15 reps (Lower abs & pelvis tuck)", "yt": VIDEOS["lying_leg_raise"]["yt"], "ytLabel": VIDEOS["lying_leg_raise"]["ytLabel"]},
            "mobility": {"id": f"e_{day_num}_2", "name": VIDEOS["worlds_greatest_stretch"]["name"], "target": "3 mins hip & ankle mobility flow", "yt": VIDEOS["worlds_greatest_stretch"]["yt"], "ytLabel": VIDEOS["worlds_greatest_stretch"]["ytLabel"]},
            "cardio": {"id": f"e_{day_num}_3", "name": "Brisk Leg Flush Walk", "target": "20 mins steady walking to clear leg fatigue", "yt": None, "ytLabel": None}
        }
        nutrition = {
            "isSunday": False,
            "highlight": "🥚 2 Boiled Eggs + Curd (Dahi) Gut & Muscle Rebuild (~112g Protein)",
            "breakfast": "2 Whole Boiled Eggs + PG Breakfast + 1 Banana",
            "lunch": "PG Mess Lunch (Rice, Dal, Sabzi) + 1 packet Curd/Dahi (₹15)",
            "snack": "1 Scoop Whey Protein + 40g Roasted Peanuts",
            "dinner": "PG Mess Dinner (3 Rotis, 2 bowls Dal, Sabzi) + 20g Roasted Chana munch",
            "supplements": "Creatine 3–5g with post-workout meal · 3.5–4.0L Water",
            "estProtein": "~112–120g"
        }

    elif day_of_cycle == 3:  # Wednesday
        body_part = "Recovery"
        title = "Active Recovery, Mobility & Core Flush"
        morning_exercises = [
            {"id": f"m_{day_num}_1", "name": VIDEOS["couch_stretch"]["name"], "sets": 3, "reps": "90s / side", "load": "Bodyweight", "tempo": "Deep breathing", "rest": "30s", "yt": VIDEOS["couch_stretch"]["yt"], "ytLabel": VIDEOS["couch_stretch"]["ytLabel"]},
            {"id": f"m_{day_num}_2", "name": VIDEOS["t_spine_opener"]["name"], "sets": 3, "reps": "10 reps / side", "load": "Bodyweight", "tempo": "Slow rotation", "rest": "30s", "yt": VIDEOS["t_spine_opener"]["yt"], "ytLabel": VIDEOS["t_spine_opener"]["ytLabel"]},
            {"id": f"m_{day_num}_3", "name": VIDEOS["bird_dog"]["name"], "sets": 3, "reps": "12 reps / side", "load": "Bodyweight", "tempo": "2s hold at full reach", "rest": "45s", "yt": VIDEOS["bird_dog"]["yt"], "ytLabel": VIDEOS["bird_dog"]["ytLabel"]},
            {"id": f"m_{day_num}_4", "name": VIDEOS["rkc_plank"]["name"], "sets": 3, "reps": "30–45s max tension", "load": "Bodyweight", "tempo": "Max squeeze glutes & abs", "rest": "60s", "yt": VIDEOS["rkc_plank"]["yt"], "ytLabel": VIDEOS["rkc_plank"]["ytLabel"]}
        ]
        evening_routine = {
            "core": {"id": f"e_{day_num}_1", "name": VIDEOS["stomach_vacuum"]["name"], "target": "4 sets x 25s vacuum hold (Waist slimming)", "yt": VIDEOS["stomach_vacuum"]["yt"], "ytLabel": VIDEOS["stomach_vacuum"]["ytLabel"]},
            "mobility": {"id": f"e_{day_num}_2", "name": VIDEOS["worlds_greatest_stretch"]["name"], "target": "3 mins deep whole-body stretch", "yt": VIDEOS["worlds_greatest_stretch"]["yt"], "ytLabel": VIDEOS["worlds_greatest_stretch"]["ytLabel"]},
            "cardio": {"id": f"e_{day_num}_3", "name": "Brisk Outdoor Walk", "target": "30 mins (approx 4,000 steps) active flush", "yt": None, "ytLabel": None}
        }
        nutrition = {
            "isSunday": False,
            "highlight": "🥚 2 Boiled Eggs + Sattu Drink Flush (~108g Protein)",
            "breakfast": "2 Whole Boiled Eggs + PG Breakfast",
            "lunch": "PG Mess Lunch (Rotis, thick Dal, Sabzi)",
            "snack": "1 Scoop Whey Protein + 1 glass Sattu drink (3 tbsp sattu in water/salt)",
            "dinner": "PG Mess Dinner + 40g Roasted Chana / 1 cup Curd",
            "supplements": "Creatine 3–5g · 4.0L Water (Joint & kidney flush)",
            "estProtein": "~108–115g"
        }

    elif day_of_cycle == 4:  # Thursday
        body_part = "Upper"
        title = "Upper Body Sculpt & Boulder Shoulders"
        morning_exercises = [
            {"id": f"m_{day_num}_1", "name": VIDEOS["decline_pushup"]["name"], "sets": sets_count, "reps": "10–12 reps", "load": "Bodyweight (Feet on bed)", "tempo": "3-1-1-0", "rest": rest_time, "yt": VIDEOS["decline_pushup"]["yt"], "ytLabel": VIDEOS["decline_pushup"]["ytLabel"]},
            {"id": f"m_{day_num}_2", "name": VIDEOS["db_arnold_press"]["name"], "sets": sets_count, "reps": "10–12 reps", "load": "2x 5kg", "tempo": "3-1-1-0 (Full rotation)", "rest": rest_time, "yt": VIDEOS["db_arnold_press"]["yt"], "ytLabel": VIDEOS["db_arnold_press"]["ytLabel"]},
            {"id": f"m_{day_num}_3", "name": VIDEOS["two_arm_db_row"]["name"], "sets": sets_count, "reps": "12 reps", "load": "2x 10kg (or 2x 5kg)", "tempo": "2-1-1-0", "rest": rest_time, "yt": VIDEOS["two_arm_db_row"]["yt"], "ytLabel": VIDEOS["two_arm_db_row"]["ytLabel"]},
            {"id": f"m_{day_num}_4", "name": VIDEOS["db_lateral_raise"]["name"], "sets": sets_count + 1, "reps": "15 reps", "load": "2x 4kg or 2x 5kg", "tempo": "3-1-1-0 (Strict side delts)", "rest": "60s", "yt": VIDEOS["db_lateral_raise"]["yt"], "ytLabel": VIDEOS["db_lateral_raise"]["ytLabel"]},
            {"id": f"m_{day_num}_5", "name": VIDEOS["diamond_pushup"]["name"], "sets": sets_count, "reps": "10–12 reps", "load": "Bodyweight", "tempo": "2-1-1-0", "rest": "60s", "yt": VIDEOS["diamond_pushup"]["yt"], "ytLabel": VIDEOS["diamond_pushup"]["ytLabel"]},
            {"id": f"m_{day_num}_6", "name": VIDEOS["db_concentration_curl"]["name"], "sets": sets_count, "reps": "10–12 reps / arm", "load": "1x 5kg or 1x 10kg", "tempo": "3-1-1-0", "rest": "45s", "yt": VIDEOS["db_concentration_curl"]["yt"], "ytLabel": VIDEOS["db_concentration_curl"]["ytLabel"]}
        ]
        evening_routine = {
            "core": {"id": f"e_{day_num}_1", "name": VIDEOS["hollow_body"]["name"], "target": "3 sets x 30–35s hollow body hold", "yt": VIDEOS["hollow_body"]["yt"], "ytLabel": VIDEOS["hollow_body"]["ytLabel"]},
            "mobility": {"id": f"e_{day_num}_2", "name": VIDEOS["couch_stretch"]["name"], "target": "2 mins each side", "yt": VIDEOS["couch_stretch"]["yt"], "ytLabel": VIDEOS["couch_stretch"]["ytLabel"]},
            "cardio": {"id": f"e_{day_num}_3", "name": "Brisk Walk", "target": "25 mins (3,000 steps)", "yt": None, "ytLabel": None}
        }
        nutrition = {
            "isSunday": False,
            "highlight": "🥚 2 Boiled Eggs + Soya Chunks Hypertrophy (~120g Protein)",
            "breakfast": "2 Whole Boiled Eggs + PG Breakfast + 1 Banana",
            "lunch": "PG Mess Lunch (Rice, Dal, Sabzi, Dahi)",
            "snack": "1 Scoop Whey Protein + 40g Roasted Peanuts",
            "dinner": "40g Soya Chunks (boiled & seasoned) with PG Dal/Sabzi + 3 Rotis",
            "supplements": "Creatine 3–5g · 3.5–4.0L Water",
            "estProtein": "~118–125g"
        }

    elif day_of_cycle == 5:  # Friday
        body_part = "Legs"
        title = "Athletic Lower Body & Core Power"
        morning_exercises = [
            {"id": f"m_{day_num}_1", "name": VIDEOS["db_goblet_squat"]["name"], "sets": sets_count, "reps": "15 reps", "load": "1x 10kg", "tempo": "3-1-1-0", "rest": rest_time, "yt": VIDEOS["db_goblet_squat"]["yt"], "ytLabel": VIDEOS["db_goblet_squat"]["ytLabel"]},
            {"id": f"m_{day_num}_2", "name": VIDEOS["walking_lunges"]["name"], "sets": sets_count, "reps": "10 reps / leg (20 total)", "load": "2x 5kg or Bodyweight", "tempo": "Controlled 90/90 step", "rest": rest_time, "yt": VIDEOS["walking_lunges"]["yt"], "ytLabel": VIDEOS["walking_lunges"]["ytLabel"]},
            {"id": f"m_{day_num}_3", "name": VIDEOS["single_leg_rdl"]["name"], "sets": sets_count, "reps": "10–12 reps / leg", "load": "1x 5kg or 1x 10kg", "tempo": "3-1-1-0", "rest": rest_time, "yt": VIDEOS["single_leg_rdl"]["yt"], "ytLabel": VIDEOS["single_leg_rdl"]["ytLabel"]},
            {"id": f"m_{day_num}_4", "name": VIDEOS["db_sumo_squat"]["name"], "sets": sets_count, "reps": "12–15 reps", "load": "1x 10kg", "tempo": "3-1-1-0", "rest": rest_time, "yt": VIDEOS["db_sumo_squat"]["yt"], "ytLabel": VIDEOS["db_sumo_squat"]["ytLabel"]},
            {"id": f"m_{day_num}_5", "name": VIDEOS["single_leg_calf_raise"]["name"], "sets": sets_count + 1, "reps": "15–20 reps / leg", "load": "1x 10kg in hand", "tempo": "3-2-1-0", "rest": "45s", "yt": VIDEOS["single_leg_calf_raise"]["yt"], "ytLabel": VIDEOS["single_leg_calf_raise"]["ytLabel"]}
        ]
        evening_routine = {
            "core": {"id": f"e_{day_num}_1", "name": VIDEOS["deadbug"]["name"], "target": "3 sets x 12 reps / side", "yt": VIDEOS["deadbug"]["yt"], "ytLabel": VIDEOS["deadbug"]["ytLabel"]},
            "mobility": {"id": f"e_{day_num}_2", "name": VIDEOS["worlds_greatest_stretch"]["name"], "target": "3 mins deep hips & ankles", "yt": VIDEOS["worlds_greatest_stretch"]["yt"], "ytLabel": VIDEOS["worlds_greatest_stretch"]["ytLabel"]},
            "cardio": {"id": f"e_{day_num}_3", "name": "Brisk Walk", "target": "25 mins (3,000 steps)", "yt": None, "ytLabel": None}
        }
        nutrition = {
            "isSunday": False,
            "highlight": "🥚 2 Boiled Eggs + Roasted Bhuna Chana (~114g Protein)",
            "breakfast": "2 Whole Boiled Eggs + PG Breakfast + 1 Banana",
            "lunch": "PG Mess Lunch (Rice, Dal, Sabzi)",
            "snack": "1 Scoop Whey Protein + 50g Roasted Bhuna Chana",
            "dinner": "PG Mess Dinner (3 Rotis, 2 bowls Dal) + 1 cup Curd (Dahi)",
            "supplements": "Creatine 3–5g · 3.5–4.0L Water",
            "estProtein": "~112–120g"
        }

    else:  # Saturday (day_of_cycle == 6)
        body_part = "Recovery"
        title = "Systemic Rest, Deep Mobility & Prep"
        morning_exercises = [
            {"id": f"m_{day_num}_1", "name": VIDEOS["worlds_greatest_stretch"]["name"], "sets": 3, "reps": "5 reps / side", "load": "Bodyweight", "tempo": "Deep breath at extension", "rest": "30s", "yt": VIDEOS["worlds_greatest_stretch"]["yt"], "ytLabel": VIDEOS["worlds_greatest_stretch"]["ytLabel"]},
            {"id": f"m_{day_num}_2", "name": VIDEOS["couch_stretch"]["name"], "sets": 3, "reps": "90s / side", "load": "Bodyweight", "tempo": "Relax into hip", "rest": "30s", "yt": VIDEOS["couch_stretch"]["yt"], "ytLabel": VIDEOS["couch_stretch"]["ytLabel"]},
            {"id": f"m_{day_num}_3", "name": VIDEOS["t_spine_opener"]["name"], "sets": 3, "reps": "10 reps / side", "load": "Bodyweight", "tempo": "Slow rotation", "rest": "30s", "yt": VIDEOS["t_spine_opener"]["yt"], "ytLabel": VIDEOS["t_spine_opener"]["ytLabel"]},
            {"id": f"m_{day_num}_4", "name": VIDEOS["stomach_vacuum"]["name"], "sets": 4, "reps": "25s vacuum hold", "load": "Bodyweight", "tempo": "Max exhalation & pull navel in", "rest": "45s", "yt": VIDEOS["stomach_vacuum"]["yt"], "ytLabel": VIDEOS["stomach_vacuum"]["ytLabel"]}
        ]
        evening_routine = {
            "core": {"id": f"e_{day_num}_1", "name": VIDEOS["rkc_plank"]["name"], "target": "3 sets x 30s plank hold", "yt": VIDEOS["rkc_plank"]["yt"], "ytLabel": VIDEOS["rkc_plank"]["ytLabel"]},
            "mobility": {"id": f"e_{day_num}_2", "name": "Shoulder Doorway Stretch", "target": "2 mins chest & anterior delt opening", "yt": None, "ytLabel": None},
            "cardio": {"id": f"e_{day_num}_3", "name": "Relaxed Evening Walk", "target": "30 mins (3,500 steps) fresh air & recovery", "yt": None, "ytLabel": None}
        }
        nutrition = {
            "isSunday": False,
            "highlight": "🥚 2 Boiled Eggs + Room Restock Day (~110g Protein)",
            "breakfast": "2 Whole Boiled Eggs + PG Breakfast",
            "lunch": "PG Mess Lunch (Rotis, Dal, Sabzi)",
            "snack": "1 Scoop Whey Protein + 1 glass Sattu or 40g Peanuts",
            "dinner": "PG Mess Dinner + Restock snacks (Chana, Eggs, Dahi for next week)",
            "supplements": "Creatine 3–5g · 3.5L Water · Aim for 8 hrs sleep tonight",
            "estProtein": "~110–118g"
        }

    day_obj = {
        "day": day_num,
        "date": date_str,
        "weekday": weekday_str,
        "week": week_num,
        "phase": phase,
        "phaseName": phase_name,
        "bodyPart": body_part,
        "title": title,
        "tempoNote": tempo_note,
        "morning": morning_exercises,
        "evening": evening_routine,
        "nutrition": nutrition
    }

    days_data.append(day_obj)
    curr += datetime.timedelta(days=1)
    day_num += 1

print(f"Generated {len(days_data)} days successfully!")

# Write to workout_data.js
js_content = f"// 68-Day Lean & Muscular Transformation Dataset (Oct 25 to Dec 31, 2026)\nconst WORKOUT_PLAN = {json.dumps(days_data, indent=2)};\n"
with open("/home/praveen/personal-projects/workout-tracker/workout_data.js", "w") as f:
    f.write(js_content)

# Write to workout_plan.json
with open("/home/praveen/personal-projects/workout-tracker/workout_plan.json", "w") as f:
    json.dump(days_data, f, indent=2)

print("Saved workout_data.js and workout_plan.json!")
