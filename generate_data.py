import datetime
import json

# Start: Oct 25, 2026. End: Dec 31, 2026
start_date = datetime.date(2026, 10, 25)
end_date = datetime.date(2026, 12, 31)

# Split Templates:
# Day 1 (Sun): Push Hypertrophy (PG Chicken Day!)
# Day 2 (Mon): Pull & Upper Back
# Day 3 (Tue): Legs & Calves (Quads & Hamstrings)
# Day 4 (Wed): Active Recovery, Mobility & Core Flush
# Day 5 (Thu): Upper Body Hypertrophy (Chest, Shoulders & Arms)
# Day 6 (Fri): Lower Athletic & Full Body Calisthenics
# Day 7 (Sat): Deep Mobility, Posture & Active Step Rest

EXERCISES = {
    # PUSH
    "standard_pushup": {"name": "Deficit / Standard Push-ups", "load": "Bodyweight (Hands on DB handles)", "tempo": "3-1-1-0 (3s down, 1s pause, explode up)", "yt": "https://www.youtube.com/watch?v=IODxDxX7oi4", "ytLabel": "Calisthenicmovement — Perfect Push-Up Form"},
    "db_floor_press": {"name": "Dumbbell Floor Press", "load": "2x 10kg (or 2x 5kg in warm-up)", "tempo": "3-1-1-0 (Elbows touch floor softly, pause, press)", "yt": "https://www.youtube.com/watch?v=uUGDRwge4F8", "ytLabel": "Scott Herman — Dumbbell Floor Press Form"},
    "db_hex_press": {"name": "Dumbbell Hex Press (Inner Chest Squeeze)", "load": "2x 5kg (Press dumbbells together hard)", "tempo": "2-2-1-0 (Max squeeze at top)", "yt": "https://www.youtube.com/watch?v=G2j_lJf6ljk", "ytLabel": "Kraken Exercise Library — Dumbbell Squeeze Press"},
    "decline_pushup": {"name": "Feet-Elevated Decline Push-ups", "load": "Bodyweight (Feet on bed/chair)", "tempo": "3-0-1-0 (Upper chest focus)", "yt": "https://www.youtube.com/watch?v=SKPab2YC8BE", "ytLabel": "Scott Herman — Decline Push-Up Form"},
    "db_shoulder_press": {"name": "Seated/Standing DB Overhead Press", "load": "2x 5kg or 2x 10kg", "tempo": "3-0-1-0 (Full lockout overhead)", "yt": "https://www.youtube.com/watch?v=qEwKCR5JCog", "ytLabel": "Scott Herman — DB Shoulder Press Form"},
    "db_arnold_press": {"name": "Dumbbell Arnold Press", "load": "2x 5kg", "tempo": "3-1-1-0 (Rotate smoothly from chest to top)", "yt": "https://www.youtube.com/watch?v=6Z15_WdXmVw", "ytLabel": "Buff Dudes — Arnold Press Tutorial"},
    "db_lateral_raise": {"name": "Strict DB Lateral Raise (Side Delts)", "load": "2x 4kg or 2x 5kg", "tempo": "3-1-1-0 (Lead with elbows, 3s descent)", "yt": "https://www.youtube.com/watch?v=3VcKaXpzqRo", "ytLabel": "Scott Herman — DB Side Lateral Raise"},
    "pike_pushup": {"name": "Pike Push-ups (Vertical Push)", "load": "Bodyweight (Hips high, head down)", "tempo": "3-0-1-0 (Shoulder builder)", "yt": "https://www.youtube.com/watch?v=18mNeuH4D1k", "ytLabel": "FitnessFAQs — How To Pike Push-Up"},
    "db_overhead_tricep": {"name": "Overhead DB Tricep Extension", "load": "1x 10kg (Both hands cupping plate)", "tempo": "3-1-1-0 (Deep elbow flexion)", "yt": "https://www.youtube.com/watch?v=_gsUck-7M74", "ytLabel": "Howcast — Dumbbell Tricep Extension"},
    "chair_dips": {"name": "Chair / Bed Bench Dips", "load": "Bodyweight (Feet extended)", "tempo": "2-1-1-0 (90 deg elbow bend)", "yt": "https://www.youtube.com/watch?v=0326dy_-CzM", "ytLabel": "LIVESTRONG — Triceps Bench Dips"},
    "diamond_pushup": {"name": "Diamond Push-ups", "load": "Bodyweight", "tempo": "2-1-1-0 (Tricep & inner chest overload)", "yt": "https://www.youtube.com/watch?v=J0DnG1_S92I", "ytLabel": "Scott Herman — Diamond Push-Up"},

    # PULL
    "single_arm_row": {"name": "Single-Arm Dumbbell Row", "load": "1x 10kg (One hand on bed/table)", "tempo": "3-1-1-0 (Drive elbow to hip, 1s pause)", "yt": "https://www.youtube.com/watch?v=pYcpY20QaE8", "ytLabel": "Scott Herman — Single-Arm DB Row Form"},
    "two_arm_db_row": {"name": "Bent-Over Two-Arm DB Row", "load": "2x 10kg (or 2x 5kg)", "tempo": "2-1-1-0 (Flat spine, hinge at hips)", "yt": "https://www.youtube.com/watch?v=5PoEksoJNaw", "ytLabel": "Renaissance Periodization — Two Arm Dumbbell Row"},
    "inverted_towel_row": {"name": "Inverted Door/Towel Row", "load": "Bodyweight (Towel anchored to door/sturdy surface)", "tempo": "2-1-1-0 (Retract scapula)", "yt": "https://www.youtube.com/watch?v=rloXYB8M3vU", "ytLabel": "Antranik — Door Towel Incline Rows"},
    "db_rear_delt_fly": {"name": "Bent-Over DB Rear Delt Flyes", "load": "2x 4kg or 2x 5kg", "tempo": "3-1-1-0 (Squeeze upper back & rear delts)", "yt": "https://www.youtube.com/watch?v=ttvfGg9d76c", "ytLabel": "Scott Herman — DB Bent-Over Rear Delt Raise"},
    "db_shrugs": {"name": "Dumbbell Shrugs (Upper Traps)", "load": "2x 10kg", "tempo": "2-2-1-0 (2s hold at top contraction)", "yt": "https://www.youtube.com/watch?v=cJRVVxmytaM", "ytLabel": "Scott Herman — Dumbbell Shrugs"},
    "db_bicep_curl": {"name": "Strict Supinating DB Bicep Curl", "load": "2x 5kg or 2x 10kg", "tempo": "3-1-1-0 (Supinate wrist at peak, 3s down)", "yt": "https://www.youtube.com/watch?v=in7PaeYlhrM", "ytLabel": "Mind Pump TV — Dumbbell Bicep Curls Form"},
    "db_hammer_curl": {"name": "Neutral Grip DB Hammer Curl (Brachialis)", "load": "2x 5kg or 2x 10kg", "tempo": "3-0-1-0 (Arm thickness & forearm grip)", "yt": "https://www.youtube.com/watch?v=zC3nLlEvin4", "ytLabel": "Scott Herman — Hammer Curl Form"},
    "db_concentration_curl": {"name": "Seated Concentration Curl", "load": "1x 5kg or 1x 10kg", "tempo": "3-1-1-0 (Elbow braced against inner thigh)", "yt": "https://www.youtube.com/watch?v=0AUGkch3tzc", "ytLabel": "Howcast — Concentration Curl Form"},

    # LEGS
    "bulgarian_split_squat": {"name": "Bulgarian Split Squat", "load": "1x 10kg (Goblet) or 2x 5kg (Rear foot on bed)", "tempo": "3-1-1-0 (Deep hip descent, brutal quad/glute tension)", "yt": "https://www.youtube.com/watch?v=bwhl_9jN_3o", "ytLabel": "Squat University — Bulgarian Split Squat Form"},
    "db_rdl": {"name": "Dumbbell Romanian Deadlift (RDL)", "load": "2x 10kg", "tempo": "4-1-1-0 (4s eccentric stretch in hamstrings)", "yt": "https://www.youtube.com/watch?v=_oyxCn2iSjU", "ytLabel": "Jeff Nippard — Romanian Deadlift (RDL) Guide"},
    "db_goblet_squat": {"name": "Dumbbell Goblet Squat", "load": "1x 10kg (Holding dumbbell at chest)", "tempo": "3-1-1-0 (Drive knees out, chest upright)", "yt": "https://www.youtube.com/watch?v=MeIiIdhvXT4", "ytLabel": "Scott Herman — Goblet Squat Guide"},
    "walking_lunges": {"name": "Dumbbell Walking Lunges", "load": "2x 5kg or Bodyweight", "tempo": "Controlled 90/90 step", "yt": "https://www.youtube.com/watch?v=L8fvypPrzzs", "ytLabel": "CrossFit — The Walking Lunge Form"},
    "single_leg_rdl": {"name": "Single-Leg DB Romanian Deadlift", "load": "1x 5kg or 1x 10kg", "tempo": "3-1-1-0 (Balance & hamstring hinge)", "yt": "https://www.youtube.com/watch?v=DGavj41F_Cs", "ytLabel": "Scott Herman — DB Single-Leg Stiff Deadlift"},
    "single_leg_calf_raise": {"name": "Single-Leg Deficit Calf Raise", "load": "1x 10kg in hand (Ball of foot on step/book)", "tempo": "3-2-1-0 (2s full stretch at bottom, 2s peak squeeze)", "yt": "https://www.youtube.com/watch?v=ORT4oJ_R8Qs", "ytLabel": "Scott Herman — Single-Leg Calf Raise Form"},
    "glute_bridge": {"name": "Weighted Glute Bridge / Hip Thrust", "load": "1x 10kg on hips (Shoulders on bed or floor)", "tempo": "2-2-1-0 (2s lock at top)", "yt": "https://www.youtube.com/watch?v=8bbE64NuDTU", "ytLabel": "Scott Herman — Glute Bridge Technique"},
    "db_sumo_squat": {"name": "Dumbbell Sumo Squat (Adductors & Glutes)", "load": "1x 10kg (Wide stance, toes 45 deg)", "tempo": "3-1-1-0", "yt": "https://www.youtube.com/watch?v=bRCjBCtBGIo", "ytLabel": "DeltaBolic — Dumbbell Sumo Squat Form"},

    # EVENING CORE & MOBILITY
    "stomach_vacuum": {"name": "Transverse Abdominis Stomach Vacuum", "yt": "https://www.youtube.com/watch?v=cub3xhJXsAA", "ytLabel": "wikiHow — Stomach Vacuum Exercise Guide"},
    "hollow_body": {"name": "Hollow Body Hold", "yt": "https://www.youtube.com/watch?v=44ScXWFaVBs", "ytLabel": "Antranik — Hollow Body Hold Guide"},
    "deadbug": {"name": "Deadbug Core Stabilization", "yt": "https://www.youtube.com/watch?v=0XVbn86Btj0", "ytLabel": "Squat University — Deadbug Core Form"},
    "lying_leg_raise": {"name": "Lying Leg Raises & Reverse Crunches", "yt": "https://www.youtube.com/watch?v=PkLYH3uRtSs", "ytLabel": "TylerPath — Lying Leg Raises Form"},
    "rkc_plank": {"name": "Hardstyle RKC Plank (Maximum Tension)", "yt": "https://www.youtube.com/watch?v=TvxNkmjdhMM", "ytLabel": "P4P Workouts — Proper Plank Form"},
    "bird_dog": {"name": "Bird-Dog Core & Lower Back Flow", "yt": "https://www.youtube.com/watch?v=wiFNA3sqjCA", "ytLabel": "Howcast — Bird Dog Exercise Tutorial"},
    "couch_stretch": {"name": "Couch Stretch (Hip Flexor & Psoas Opener)", "yt": "https://www.youtube.com/watch?v=SLxuJg_zKzw", "ytLabel": "Movementgems — Couch Stretch Guide"},
    "doorway_stretch": {"name": "Shoulder Doorway Stretch", "yt": "https://www.youtube.com/watch?v=O8rJw_TmC1Y", "ytLabel": "Rehab Hero — Doorway Chest & Shoulder Stretch"},
    "t_spine_opener": {"name": "Thoracic Spine Mobility & Desk Posture Opener", "yt": "https://www.youtube.com/watch?v=9LJDGUulS_8", "ytLabel": "Squat University — Thoracic Spine Mobility"},
    "worlds_greatest_stretch": {"name": "World's Greatest Stretch Routine", "yt": "https://www.youtube.com/watch?v=-CiWQ2IvY34", "ytLabel": "Squat University — World's Greatest Stretch"}
}

print("Exercise dictionary loaded successfully!")
