import datetime
import json

start_date = datetime.date(2026, 11, 17) # Tuesday
end_date = datetime.date(2026, 12, 31)   # Thursday

# Total days: 45 days to Jan 1st!

VIDEOS = {
    # PUSH
    "standard_pushup": {"name": "Deficit / Standard Push-ups", "yt": "https://www.youtube.com/watch?v=IODxDxX7oi4", "ytLabel": "Calisthenicmovement — Perfect Push-Up Form"},
    "db_floor_press": {"name": "Dumbbell Floor Press", "yt": "https://www.youtube.com/watch?v=uUGDRwge4F8", "ytLabel": "Scott Herman — Dumbbell Floor Press Form"},
    "db_hex_press": {"name": "Dumbbell Hex Press (Inner Chest Squeeze)", "yt": "https://www.youtube.com/watch?v=G2j_lJf6ljk", "ytLabel": "Kraken Exercise Library — Dumbbell Squeeze Press"},
    "decline_pushup": {"name": "Feet-Elevated Decline Push-ups", "yt": "https://www.youtube.com/watch?v=SKPab2YC8BE", "ytLabel": "Scott Herman — Decline Push-Up Form"},
    "db_shoulder_press": {"name": "Seated/Standing DB Overhead Press", "yt": "https://www.youtube.com/watch?v=qEwKCR5JCog", "ytLabel": "Scott Herman — DB Shoulder Press Form"},
    "db_arnold_press": {"name": "Dumbbell Arnold Press", "yt": "https://www.youtube.com/watch?v=6Z15_WdXmVw", "ytLabel": "Buff Dudes — Arnold Press Tutorial"},
    "db_lateral_raise": {"name": "Strict DB Lateral Raise (Side Delts)", "yt": "https://www.youtube.com/watch?v=3VcKaXpzqRo", "ytLabel": "Scott Herman — DB Side Lateral Raise"},
    "pike_pushup": {"name": "Pike Push-ups (Vertical Push)", "yt": "https://www.youtube.com/watch?v=18mNeuH4D1k", "ytLabel": "FitnessFAQs — How To Pike Push-Up"},
    "db_overhead_tricep": {"name": "Overhead DB Tricep Extension", "yt": "https://www.youtube.com/watch?v=_gsUck-7M74", "ytLabel": "Howcast — Dumbbell Tricep Extension"},
    "chair_dips": {"name": "Chair / Bed Bench Dips", "yt": "https://www.youtube.com/watch?v=0326dy_-CzM", "ytLabel": "LIVESTRONG — Triceps Bench Dips"},
    "diamond_pushup": {"name": "Diamond Push-ups (Tricep Overload)", "yt": "https://www.youtube.com/watch?v=J0DnG1_S92I", "ytLabel": "Scott Herman — Diamond Push-Up"},
    
    # PULL
    "single_arm_row": {"name": "Single-Arm Dumbbell Row", "yt": "https://www.youtube.com/watch?v=pYcpY20QaE8", "ytLabel": "Scott Herman — Single-Arm DB Row Form"},
    "two_arm_db_row": {"name": "Bent-Over Two-Arm DB Row", "yt": "https://www.youtube.com/watch?v=5PoEksoJNaw", "ytLabel": "Renaissance Periodization — Two Arm Dumbbell Row"},
    "inverted_towel_row": {"name": "Inverted Door/Towel Row", "yt": "https://www.youtube.com/watch?v=rloXYB8M3vU", "ytLabel": "Antranik — Door Towel Incline Rows"},
    "db_rear_delt_fly": {"name": "Bent-Over DB Rear Delt Flyes", "yt": "https://www.youtube.com/watch?v=ttvfGg9d76c", "ytLabel": "Scott Herman — DB Bent-Over Rear Delt Raise"},
    "db_shrugs": {"name": "Dumbbell Shrugs (Upper Traps)", "yt": "https://www.youtube.com/watch?v=cJRVVxmytaM", "ytLabel": "Scott Herman — Dumbbell Shrugs"},
    "db_bicep_curl": {"name": "Strict Supinating DB Bicep Curl", "yt": "https://www.youtube.com/watch?v=in7PaeYlhrM", "ytLabel": "Mind Pump TV — Dumbbell Bicep Curls Form"},
    "db_hammer_curl": {"name": "Neutral Grip DB Hammer Curl", "yt": "https://www.youtube.com/watch?v=zC3nLlEvin4", "ytLabel": "Scott Herman — Hammer Curl Form"},
    "db_concentration_curl": {"name": "Seated Concentration Curl", "yt": "https://www.youtube.com/watch?v=0AUGkch3tzc", "ytLabel": "Howcast — Concentration Curl Form"},

    # LEGS
    "bulgarian_split_squat": {"name": "Bulgarian Split Squat", "yt": "https://www.youtube.com/watch?v=bwhl_9jN_3o", "ytLabel": "Squat University — Bulgarian Split Squat Form"},
    "db_rdl": {"name": "Dumbbell Romanian Deadlift (RDL)", "yt": "https://www.youtube.com/watch?v=_oyxCn2iSjU", "ytLabel": "Jeff Nippard — Romanian Deadlift (RDL) Guide"},
    "db_goblet_squat": {"name": "Dumbbell Goblet Squat", "yt": "https://www.youtube.com/watch?v=MeIiIdhvXT4", "ytLabel": "Scott Herman — Goblet Squat Guide"},
    "walking_lunges": {"name": "Dumbbell Walking Lunges", "yt": "https://www.youtube.com/watch?v=L8fvypPrzzs", "ytLabel": "CrossFit — The Walking Lunge Form"},
    "single_leg_rdl": {"name": "Single-Leg DB Romanian Deadlift", "yt": "https://www.youtube.com/watch?v=DGavj41F_Cs", "ytLabel": "Scott Herman — DB Single-Leg Stiff Deadlift"},
    "single_leg_calf_raise": {"name": "Single-Leg Deficit Calf Raise", "yt": "https://www.youtube.com/watch?v=ORT4oJ_R8Qs", "ytLabel": "Scott Herman — Single-Leg Calf Raise Form"},
    "glute_bridge": {"name": "Weighted Glute Bridge / Hip Thrust", "yt": "https://www.youtube.com/watch?v=8bbE64NuDTU", "ytLabel": "Scott Herman — Glute Bridge Technique"},
    "db_sumo_squat": {"name": "Dumbbell Sumo Squat (Adductors & Glutes)", "yt": "https://www.youtube.com/watch?v=bRCjBCtBGIo", "ytLabel": "DeltaBolic — Dumbbell Sumo Squat Form"},

    # CORE & MOBILITY
    "stomach_vacuum": {"name": "Transverse Abdominis Stomach Vacuum", "yt": "https://www.youtube.com/watch?v=cub3xhJXsAA", "ytLabel": "wikiHow — Stomach Vacuum Exercise Guide"},
    "hollow_body": {"name": "Hollow Body Hold", "yt": "https://www.youtube.com/watch?v=44ScXWFaVBs", "ytLabel": "Antranik — Hollow Body Hold Guide"},
    "deadbug": {"name": "Deadbug Core Stabilization", "yt": "https://www.youtube.com/watch?v=0XVbn86Btj0", "ytLabel": "Squat University — Deadbug Core Form"},
    "lying_leg_raise": {"name": "Lying Leg Raises & Reverse Crunches", "yt": "https://www.youtube.com/watch?v=PkLYH3uRtSs", "ytLabel": "TylerPath — Lying Leg Raises Form"},
    "rkc_plank": {"name": "Hardstyle RKC Plank (Maximum Tension)", "yt": "https://www.youtube.com/watch?v=TvxNkmjdhMM", "ytLabel": "P4P Workouts — Proper Plank Form"},
    "bird_dog": {"name": "Bird-Dog Core & Lower Back Flow", "yt": "https://www.youtube.com/watch?v=wiFNA3sqjCA", "ytLabel": "Howcast — Bird Dog Exercise Tutorial"},
    "couch_stretch": {"name": "Couch Stretch (Hip Flexor & Psoas Opener)", "yt": "https://www.youtube.com/watch?v=SLxuJg_zKzw", "ytLabel": "Movementgems — Couch Stretch Guide"},
    "doorway_stretch": {"name": "Shoulder Doorway Stretch", "yt": "https://www.youtube.com/watch?v=O8rJw_TmC1Y", "ytLabel": "Rehab Hero — Doorway Chest & Shoulder Stretch"},
    "t_spine_opener": {"name": "Thoracic Spine Mobility & Desk Posture", "yt": "https://www.youtube.com/watch?v=9LJDGUulS_8", "ytLabel": "Squat University — Thoracic Spine Mobility"},
    "worlds_greatest_stretch": {"name": "World's Greatest Stretch Routine", "yt": "https://www.youtube.com/watch?v=-CiWQ2IvY34", "ytLabel": "Squat University — World's Greatest Stretch"}
}

# 45 Daily Progressive Brain Mastery & Overthinking Protocols
BRAIN_CURRICULUM = [
    # Phase 1: Days 1–10 (Foundation, Dopamine Fast & Nervous System Control)
    {
        "theme": "The 5-Second Rule: Kill Hesitation & Analysis Paralysis",
        "principle": "The human brain creates excuses to hesitate within 5 seconds of an impulse. Counting backwards '5-4-3-2-1' stimulates the prefrontal cortex and shifts you into immediate physical action before the amygdala can trigger overthinking.",
        "action": "Whenever you feel resistance to starting your workout, studying, or getting out of bed, count 5-4-3-2-1 and move physically. No debates.",
        "pillar": "Overthinking Control & Action Bias"
    },
    {
        "theme": "Autonomic Nervous System Reset: The Physiological Sigh",
        "principle": "Two rapid inhales through the nose immediately followed by an extended sigh through the mouth pops open collapsed alveoli in the lungs, rapidly offloads CO2, and triggers the parasympathetic vagus nerve, reducing racing thoughts in under 30 seconds.",
        "action": "Perform 3 consecutive physiological sighs before starting any stressful task or whenever thoughts begin to spiral.",
        "pillar": "Neural State Regulation"
    },
    {
        "theme": "Dopamine Fasting: The 60-Minute Morning Phone Blackout",
        "principle": "Checking notifications or reels upon waking floods the brain with cheap dopamine spikes, causing baseline dopamine to crash below normal for the rest of the day. This creates severe brain fog, irritability, and chronic distraction.",
        "action": "Keep your phone in another room or on airplane mode for the first 60 minutes after waking. Get sunlight and drink 500ml water first.",
        "pillar": "Dopamine & Impulse Mastery"
    },
    {
        "theme": "The Brain Dump: Defusing the Zeigarnik Loop",
        "principle": "The Zeigarnik Effect causes the brain to loop unfinished thoughts because the subconscious fears forgetting them. Writing raw worries down on paper signals to your brain that the information is safely stored, instantly silencing mental loops.",
        "action": "Take 5 minutes to dump every anxious thought or to-do onto a physical notepad. Don't organize it, just get it out of working memory.",
        "pillar": "Overthinking Defusion"
    },
    {
        "theme": "Single-Tasking: The 90-Minute High-IQ Focus Sprint",
        "principle": "Multitasking doesn't exist in human biology—it is rapid 'context switching,' which burns glycogen, spikes cortisol, and temporarily lowers functional IQ by 10-15 points. Single-tasking for 90 minutes doubles cognitive horsepower.",
        "action": "Pick ONE high-leverage task. Silence all alerts, put on focus audio or earplugs, and do not switch windows for 90 minutes.",
        "pillar": "Deep Cognitive Stamina"
    },
    {
        "theme": "Stoic Dichotomy of Control: Eradicating Worry at the Root",
        "principle": "Epictetus's timeless rule: Some things are within our control, and others are not. Overthinking is almost exclusively ruminating over things outside your direct control (other people's reactions, past slip-ups, distant future).",
        "action": "Split today's worry into two columns: 'What I Control' vs 'What I Cannot Control'. Mentally shred the second column.",
        "pillar": "Stoic Mental Toughness"
    },
    {
        "theme": "State Precedes Story: Physiology Over Psychology",
        "principle": "When your body is dehydrated, slumped, and breathing shallowly, your brain manufactures pessimistic, anxious narratives to match your physiological state. You cannot 'think' your way out of a body problem.",
        "action": "When negative self-talk appears, do not argue with it. Drink 500ml cold water, do 15 pushups, or walk outside. Change physiology first.",
        "pillar": "Mind-Body Architecture"
    },
    {
        "theme": "Urge Surfing: Riding Out Distraction Waves",
        "principle": "Neurochemical cravings (to check phone, open YouTube, eat junk) peak like an ocean wave and naturally dissipate within 180 seconds if you do not feed them.",
        "action": "When you feel an impulsive craving to distract yourself, set a 3-minute timer. Observe the urge like a scientist without acting on it. Watch it dissolve.",
        "pillar": "Impulse Control"
    },
    {
        "theme": "Cognitive Defusion: You Are the Sky, Not the Clouds",
        "principle": "Acceptance and Commitment Therapy (ACT) proves that trying to suppress thoughts makes them rebound 2x stronger. Instead, shift from 'I am anxious and overwhelmed' to 'I notice my mind is generating thoughts of overwhelm.'",
        "action": "Label anxious chatter neutrally: 'Interesting thought, but not useful right now.' Let it drift past without boarding the train.",
        "pillar": "Thought Decoupling"
    },
    {
        "theme": "Creatine & Hydration: The Neuro-Metabolic Fuel",
        "principle": "Creatine is not just for muscles—it increases phosphocreatine in the brain, improving ATP recycling in the prefrontal cortex during demanding cognitive tasks. Paired with 3.5L water, it eliminates brain dehydration fatigue.",
        "action": "Take your 3-5g creatine with water. Notice how mental stamina holds steady during your afternoon work block.",
        "pillar": "Neuro-Nutrition"
    },

    # Phase 2: Days 11–22 (Deep Focus, Neuroplasticity & Cognitive Stamina)
    {
        "theme": "The Feynman Technique: True Intelligence is Radical Simplicity",
        "principle": "Jargon and complex explanations hide a lack of understanding. Nobel laureate Richard Feynman proved that if you cannot explain a concept to a 10-year-old child in simple words, you don't actually understand it.",
        "action": "Pick one complex topic from your work or study today. Write a 2-sentence explanation using only everyday, simple words.",
        "pillar": "High-IQ Learning"
    },
    {
        "theme": "Mental Models 1: First Principles Thinking",
        "principle": "Most people think by analogy ('everyone else does it this way'). First principles thinking breaks a problem down to fundamental, undeniable truths, and reasons up from there.",
        "action": "Take a persistent obstacle in your life. Ask: 'What are the absolute undeniable facts here? What assumptions am I making that might be false?'",
        "pillar": "Mental Models"
    },
    {
        "theme": "Mental Models 2: Inversion (Charlie Munger)",
        "principle": "'Invert, always invert.' Instead of asking 'How do I become hyper-successful?', ask 'What habits would guarantee that I stay sluggish, anxious, and unfocused?' (Staying up late, scrolling in bed, skipping workouts). Now systematically avoid them.",
        "action": "List 3 self-sabotaging habits you engaged in last month. Invert them into 3 clear non-negotiable boundaries.",
        "pillar": "Inversion Thinking"
    },
    {
        "theme": "The 80/20 Pareto Rule: Extreme Cognitive Leverage",
        "principle": "Vilfredo Pareto's law: 80% of outputs stem from 20% of inputs. In work and study, 1 or 2 core tasks generate almost all your progress; the other 80% is busywork that tricks your brain into feeling productive.",
        "action": "Identify your 'One Thing' for today. Complete it before touching email, messaging, or minor chores.",
        "pillar": "High-Leverage Execution"
    },
    {
        "theme": "Active Recall vs Passive Reading",
        "principle": "Passive reading gives the illusion of competence through recognition, not retrieval. Forcing your brain to retrieve information from memory strengthens synaptic connections (long-term potentiation) 300% faster.",
        "action": "After reading or studying for 20 minutes, close the book/screen and write down everything you remember on a blank page.",
        "pillar": "Accelerated Learning"
    },
    {
        "theme": "The Pre-Mortem: Killing Anxiety with Worst-Case Preparedness",
        "principle": "Stoic Premeditatio Malorum: Imagine the worst-case scenario happening tomorrow. What is the actual fallout? Can you handle it? Yes. By taking the subconscious fear out of the dark, the amygdala loses its grip over your nervous system.",
        "action": "If a looming event or decision is making you overthink, write down the absolute worst possible outcome. Formulate a 2-step contingency plan. Feel the calm.",
        "pillar": "Fear Deconstruction"
    },
    {
        "theme": "Second-Order Thinking: How Champions Decide",
        "principle": "First-order thinking asks 'What happens right now?' (Skipping the workout feels comfortable now). Second-order thinking asks 'And then what happens?' (Guilt, sluggishness, loss of momentum, self-doubt tomorrow).",
        "action": "Apply second-order thinking to every impulse today before saying yes or no.",
        "pillar": "Strategic Thinking"
    },
    {
        "theme": "Digital Declutter: Reclaiming Working Memory",
        "principle": "Visual clutter in your physical and digital environment constantly drains working memory and executive function bandwidth. Every open browser tab is an unconscious micro-demand on your attention.",
        "action": "Close all unused tabs, turn off notification badges, and clear your desk surface. Feel the immediate mental headroom.",
        "pillar": "Attention Architecture"
    },
    {
        "theme": "Non-Sleep Deep Rest (NSDR) / Yoga Nidra",
        "principle": "A 10-20 minute NSDR protocol restores dopamine levels in the basal ganglia and accelerates memory consolidation without the grogginess of a long daytime nap.",
        "action": "Do a 10-15 minute guided NSDR or body scan lying down with eyes closed in the afternoon. Wake up reset.",
        "pillar": "Neural Recovery"
    },
    {
        "theme": "Hanlon's Razor: Stop Over-Analyzing Others' Actions",
        "principle": "'Never attribute to malice that which is adequately explained by neglect, busyness, or carelessness.' Overthinking relationships or workplace messages usually invents dramatic conflicts that don't exist in reality.",
        "action": "If someone took long to reply or sounded blunt, assume they were busy or distracted. Refuse to write imaginary scripts.",
        "pillar": "Social Overthinking"
    },
    {
        "theme": "The 2-Minute Rule for Micro-Tasks",
        "principle": "If a task takes less than 2 minutes to do (replying to a critical message, putting away workout gear, washing a shaker), do it immediately. Storing 2-minute tasks in your head creates mental debt and overthinking.",
        "action": "Knock out small tasks instantly today instead of letting them linger on your mental radar.",
        "pillar": "Zero Mental Debt"
    },
    {
        "theme": "Cognitive Reframing: Obstacle as Fuel (Amor Fati)",
        "principle": "Cognitive reframing activates the prefrontal cortex to reinterpret a stressful event from a 'threat' to a 'challenge' or 'training test.' Marcus Aurelius: 'The impediment to action advances action. What stands in the way becomes the way.'",
        "action": "When an unexpected inconvenience happens today, instantly ask: 'How does this test make me sharper, tougher, or more adaptable?'",
        "pillar": "Cognitive Reframing"
    },

    # Phase 3: Days 23–34 (Density Overload & Overthinking Immunity)
    {
        "theme": "Worry Time Allocation: Contain the Overthinking Beast",
        "principle": "You cannot forbid your brain from having worries, but you can schedule them. Research shows that allocating a strict 15-minute 'Worry Window' at 5:00 PM prevents worries from leaking into morning focus and nighttime sleep.",
        "action": "If an anxious thought pops up at 11 AM, say: 'Not now. I have scheduled worry time at 5:00 PM.' In 80% of cases, by 5:00 PM the worry is gone.",
        "pillar": "Worry Containment"
    },
    {
        "theme": "The Spotlight Effect: Nobody Is Watching You",
        "principle": "The human brain is naturally egocentric, leading to the 'Spotlight Effect'—we overestimate how much other people notice our flaws, awkward moments, or slip-ups by over 500%. In reality, everyone is busy obsessing over themselves.",
        "action": "Release social self-consciousness. Do your work boldly without obsessing over external judgments.",
        "pillar": "Social Freedom"
    },
    {
        "theme": "Glymphatic Sleep Wash: Physical Brain Cleaning",
        "principle": "During deep slow-wave sleep, cerebrospinal fluid flows through the brain (the glymphatic system), washing away metabolic waste and amyloid plaques accumulated during high-intensity thinking.",
        "action": "Commit to 8 hours of sleep tonight. No screens 45 minutes before sleep; keep the room dark and cool.",
        "pillar": "Brain Cleansing"
    },
    {
        "theme": "Parkinson's Law: Compress Time to Boost Output",
        "principle": "'Work expands to fill the time available for its completion.' If you give yourself all day to finish a task, it takes all day and induces procrastination and overthinking. Giving yourself an aggressive 45-minute countdown forces extreme clarity.",
        "action": "Set a timer for 45 minutes for a task you've been putting off. Race against the clock.",
        "pillar": "Time Compression"
    },
    {
        "theme": "The Sunk Cost Fallacy: Ruthless Elimination",
        "principle": "Sticking with an unproductive method, dead project, or bad habit simply because you already invested time or money into it is irrational. Intelligence is knowing when to cut losses without guilt.",
        "action": "Audit your current activities. What are you holding onto solely because of past effort? Drop it or pivot today.",
        "pillar": "Mental Clarity"
    },
    {
        "theme": "Attention Residue: The Cost of Fragmented Work",
        "principle": "Dr. Sophie Leroy's research proved that when you switch from Task A to Task B, part of your attention remains stuck on Task A ('attention residue'), drastically degrading cognitive performance on Task B.",
        "action": "Complete Task A completely or reach a definitive stopping point before opening Task B.",
        "pillar": "Executive Focus"
    },
    {
        "theme": "Box Breathing: The Elite Operator's Reset",
        "principle": "Used by Navy SEALs to maintain absolute heart rate control during high-stress operations: Inhale 4s, Hold 4s, Exhale 4s, Hold empty 4s. Balances sympathetic and parasympathetic branches of the nervous system.",
        "action": "Do 4 rounds of box breathing before sitting down for demanding work or intense sets.",
        "pillar": "Stress Modulation"
    },
    {
        "theme": "The Illusion of Explanatory Depth",
        "principle": "We believe we understand complex systems until we are asked to draw or explain them step by step. A truly smart person acknowledges what they don't know rather than bluffing themselves.",
        "action": "When learning something new today, draw a diagram on paper showing the cause-and-effect chain.",
        "pillar": "Deep Understanding"
    },
    {
        "theme": "Default Mode Network (DMN) Deactivation",
        "principle": "The DMN is the brain network responsible for mind-wandering, rumination, and past/future anxiety. Heavy compound lifting, progressive tension, and breath-focused attention deactivate the DMN and re-engage the Task-Positive Network (TPN).",
        "action": "In your workout today, focus 100% on the sensation of muscle stretch and contraction. Use physical exertion as a mental cleanse.",
        "pillar": "Mindfulness in Action"
    },
    {
        "theme": "Occam's Razor: The Simplest Solution Wins",
        "principle": "Overthinking loves complicated, convoluted explanations and plans. Occam's Razor states that among competing hypotheses, the one with the fewest assumptions is usually correct.",
        "action": "If a project or problem feels too complex, strip away the layers. What is the simplest, most direct step forward? Take it.",
        "pillar": "Cognitive Simplicity"
    },
    {
        "theme": "Emotional Granularity: Naming Tames the Amygdala",
        "principle": "Dr. Lisa Feldman Barrett's neuroimaging shows that labeling an emotion with precision (e.g., 'I feel impatient due to fatigue' instead of 'I feel bad') immediately reduces amygdala reactivity and restores rational composure.",
        "action": "When you feel stress or irritability today, pinpoint the exact underlying physical cause (hunger, dehydration, sleep debt, lack of movement).",
        "pillar": "Emotional Intelligence"
    },
    {
        "theme": "The Power of Deliberate Boredom",
        "principle": "Constant stimulation (podcasts during walks, scrolling while waiting in line) robs the brain of spontaneous creative synthesis and increases baseline anxiety. Breakthrough insights happen when the mind is at rest.",
        "action": "Take a 15-minute walk today with zero headphones, zero podcasts, and zero phone. Let your mind decompress naturally.",
        "pillar": "Creative Incubation"
    },

    # Phase 4: Days 35–45 (Peak Definition & Unstoppable Mindset)
    {
        "theme": "Flow State Triggers: High Challenge Meets High Skill",
        "principle": "Mihaly Csikszentmihalyi's flow state occurs when task challenge is matched just slightly above your current skill level, accompanied by clear goals and immediate feedback, triggering transient hypofrontality (quieting the inner critic).",
        "action": "Set a clear goal with a visible milestone for today's focus block. Immerse yourself completely.",
        "pillar": "Flow State Mastery"
    },
    {
        "theme": "The Asymmetry of Action: Action Produces Motivation",
        "principle": "Amateurs wait for motivation before taking action; professionals take action, which releases dopamine upon progress, which then creates motivation. Action is the cause, not the consequence.",
        "action": "Start the first 2 minutes of the task you dread most. Let momentum do the heavy lifting.",
        "pillar": "Action Momentum"
    },
    {
        "theme": "Signal vs Noise: Protecting Your Intellectual Intake",
        "principle": "'You are what you eat' applies 10x more to what you feed your brain. Consuming low-value social media, gossip, and outrage pollutes your cognitive clarity and degrades high-level decision making.",
        "action": "Ruthlessly unfollow or mute clickbait accounts. Replace 30 minutes of scrolling with a high-signal technical book or article.",
        "pillar": "Information Diet"
    },
    {
        "theme": "The Circle of Competence (Warren Buffett)",
        "principle": "Knowing the boundary of what you know and what you don't know is far more valuable than being generally brilliant. Staying within your circle of competence and expanding it systematically prevents catastrophic errors in judgment.",
        "action": "Identify one area where you need deeper mastery. Spend 45 minutes studying the core mechanics, not surface opinions.",
        "pillar": "Intellectual Discipline"
    },
    {
        "theme": "Mental Resilience Under Fatigue",
        "principle": "When your body is tired at the end of a long week, the brain's prefrontal cortex experiences temporary ego depletion, making you susceptible to cravings and negative spirals. This is when mental discipline counts double.",
        "action": "When fatigue tries to negotiate a shortcut on your workout or diet today, remind yourself: 'Discipline is doing what needs to be done even when you don't feel like it.'",
        "pillar": "Willpower Armor"
    },
    {
        "theme": "Radical Candor with Yourself",
        "principle": "Self-deception is the greatest enemy of growth. Excuses and rationalizations are cognitive defense mechanisms to protect the ego from feeling inadequate.",
        "action": "Look honestly at your consistency over the last 40 days. Celebrate genuine wins; identify weak spots without shame and tighten them.",
        "pillar": "Self-Honesty"
    },
    {
        "theme": "Cognitive Load Management: Automate Routine Decisions",
        "principle": "Steve Jobs, Einstein, and Obama automated their clothing and meals to preserve decision-making bandwidth for high-leverage choices. Eliminating decision fatigue keeps your mind sharp all afternoon.",
        "action": "Standardize your morning routine, workout time, and PG meals so they require zero debate.",
        "pillar": "Decision Bandwidth"
    },
    {
        "theme": "The Antifragile Mindset (Nassim Taleb)",
        "principle": "The fragile breaks under stress; the robust resists stress; the antifragile grows stronger from stress, volatility, and disorder. View every workout muscle tear and cognitive problem as biological upgrades.",
        "action": "When things don't go according to plan today, say: 'This friction is upgrading my system.'",
        "pillar": "Antifragility"
    },
    {
        "theme": "The Power of Closure: Zero Loose Ends",
        "principle": "Unfinished emails, lingering tasks, and unresolved conflicts create cognitive drag. Clearing out old loops creates an explosive surge in mental vitality.",
        "action": "Spend 30 minutes resolving 3 lingering tasks or messages you have put off all month. Enjoy the profound relief.",
        "pillar": "Cognitive Cleanse"
    },
    {
        "theme": "Identity Shift: 'I Am Someone Who Executes'",
        "principle": "James Clear (Atomic Habits): Lasting change is not about what you achieve, but who you become. Every time you complete your workout, practice deep work, and silence overthinking, you cast a vote for your new identity.",
        "action": "Acknowledge the person you have forged over the past 44 days: lean, focused, resilient, in control.",
        "pillar": "Identity Transformation"
    },
    {
        "theme": "The Jan 1st Launchpad: Entering 2027 at Full Power",
        "principle": "You don't 'start' on New Year's Day—you arrive on New Year's Day already 45 days ahead of everyone else. Your mind is quiet, sharp, and disciplined; your body is lean and muscular.",
        "action": "Complete Day 45's mission. Review your 45-day journey, write down your 2027 vision, and enter the new year with absolute unstoppable momentum!",
        "pillar": "Peak Transformation"
    }
]

days_data = []
curr = start_date
day_num = 1

while curr <= end_date:
    date_str = curr.strftime("%Y-%m-%d")
    weekday_str = curr.strftime("%A")
    week_num = (day_num - 1) // 7 + 1
    weekday_idx = curr.weekday() # Mon=0, Tue=1, Wed=2, Thu=3, Fri=4, Sat=5, Sun=6

    # Phase calculation (45 days periodization)
    if day_num <= 10:
        phase = 1
        phase_name = "Phase 1 — Foundation, Dopamine Fast & Nervous System Control"
        tempo_note = "Focus: 3s eccentric descent, strict form, 2 RIR, morning dopamine reset."
        rest_time = "75s"
        sets_count = 3
    elif day_num <= 22:
        phase = 2
        phase_name = "Phase 2 — Hypertrophy Overload & Deep Work Stamina"
        tempo_note = "Focus: 3-1-1-0 tempo, 1s pause at peak, 1–2 RIR, Feynman learning sprints."
        rest_time = "60–75s"
        sets_count = 4
    elif day_num <= 34:
        phase = 3
        phase_name = "Phase 3 — Mechanical Density & Overthinking Immunity"
        tempo_note = "Focus: High tension, mechanical drop sets, Stoic thought-decoupling, 0–1 RIR."
        rest_time = "60s"
        sets_count = 4
    else:
        phase = 4
        phase_name = "Phase 4 — Peak Physical Definition & High-IQ Cognitive Mastery"
        tempo_note = "Focus: Peak V-Taper, lateral delt caps, flow states, entering Jan 1 at 100%."
        rest_time = "45–60s"
        sets_count = 4

    # Build morning workout, evening, nutrition based on day of week
    morning_exercises = []
    evening_routine = {}
    nutrition = {}
    body_part = ""
    title = ""

    if weekday_idx == 6:  # Sunday
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
            "highlight": "🍗 PG Sunday Special Chicken Feast! (Eggs skipped today as scheduled)",
            "breakfast": "PG Breakfast + 1 glass Milk + 1 Banana",
            "lunch": "PG Mess Lunch (Rice, Dal, Sabzi, Curd/Dahi)",
            "snack": "1 Scoop Whey Protein + 35g Roasted Chana (pre/post workout)",
            "dinner": "PG Chicken Curry / Chicken Dinner (3–4 rotis + generous chicken portion)",
            "supplements": "Creatine 3–5g (mix with warm water or lunch) · 3.5L Water target",
            "estProtein": "~115–125g"
        }

    elif weekday_idx == 0:  # Monday
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

    elif weekday_idx == 1:  # Tuesday
        body_part = "Legs"
        title = "Quads, Hamstrings & Calves Power"
        morning_exercises = [
            {"id": f"m_{day_num}_1", "name": VIDEOS["bulgarian_split_squat"]["name"], "sets": sets_count, "reps": "10–12 reps / leg", "load": "1x 10kg (Goblet)", "tempo": "3-1-1-0 (Deep hip descent)", "rest": rest_time, "yt": VIDEOS["bulgarian_split_squat"]["yt"], "ytLabel": VIDEOS["bulgarian_split_squat"]["ytLabel"]},
            {"id": f"m_{day_num}_2", "name": VIDEOS["db_rdl"]["name"], "sets": sets_count, "reps": "12 reps", "load": "2x 10kg", "tempo": "4-1-1-0 (Max hamstring stretch)", "rest": rest_time, "yt": VIDEOS["db_rdl"]["yt"], "ytLabel": VIDEOS["db_rdl"]["ytLabel"]},
            {"id": f"m_{day_num}_3", "name": VIDEOS["db_goblet_squat"]["name"], "sets": sets_count, "reps": "15 reps", "load": "1x 10kg", "tempo": "3-1-1-0", "rest": rest_time, "yt": VIDEOS["db_goblet_squat"]["yt"], "ytLabel": VIDEOS["db_goblet_squat"]["ytLabel"]},
            {"id": f"m_{day_num}_4", "name": VIDEOS["single_leg_calf_raise"]["name"], "sets": sets_count + 1, "reps": "15–20 reps / side", "load": "1x 10kg", "tempo": "3-2-1-0 (2s pause at stretch)", "rest": "45s", "yt": VIDEOS["single_leg_calf_raise"]["yt"], "ytLabel": VIDEOS["single_leg_calf_raise"]["ytLabel"]},
            {"id": f"m_{day_num}_5", "name": VIDEOS["glute_bridge"]["name"], "sets": sets_count, "reps": "15 reps", "load": "1x 10kg on hips", "tempo": "2-2-1-0 (2s squeeze at top)", "rest": "60s", "yt": VIDEOS["glute_bridge"]["yt"], "ytLabel": VIDEOS["glute_bridge"]["ytLabel"]}
        ]
        evening_routine = {
            "core": {"id": f"e_{day_num}_1", "name": VIDEOS["hollow_body"]["name"], "target": "4 sets x 20–30s hold (Lower back glued to floor)", "yt": VIDEOS["hollow_body"]["yt"], "ytLabel": VIDEOS["hollow_body"]["ytLabel"]},
            "mobility": {"id": f"e_{day_num}_2", "name": VIDEOS["couch_stretch"]["name"], "target": "2 mins each side (releases tight quad/hip)", "yt": VIDEOS["couch_stretch"]["yt"], "ytLabel": VIDEOS["couch_stretch"]["ytLabel"]},
            "cardio": {"id": f"e_{day_num}_3", "name": "Brisk Evening Walk", "target": "25 mins (approx 3,000 steps) for leg recovery", "yt": None, "ytLabel": None}
        }
        nutrition = {
            "isSunday": False,
            "highlight": "🥚 2 Boiled Eggs + Roasted Chana Recovery (~112g Protein)",
            "breakfast": "2 Whole Boiled Eggs + PG Breakfast",
            "lunch": "PG Mess Lunch (Rice, Dal, Sabzi, Curd/Dahi)",
            "snack": "1 Scoop Whey Protein + 45g Roasted Bhuna Chana",
            "dinner": "PG Mess Dinner (3 Rotis, 2 bowls Dal) + 1 cup Curd (Dahi)",
            "supplements": "Creatine 3–5g · 3.5–4.0L Water",
            "estProtein": "~112–118g"
        }

    elif weekday_idx == 2:  # Wednesday
        body_part = "Recovery"
        title = "Active Recovery, Mobility & Core Flush"
        morning_exercises = [
            {"id": f"m_{day_num}_1", "name": VIDEOS["worlds_greatest_stretch"]["name"], "sets": 3, "reps": "5 reps / side", "load": "Bodyweight", "tempo": "Slow and deep breathing", "rest": "30s", "yt": VIDEOS["worlds_greatest_stretch"]["yt"], "ytLabel": VIDEOS["worlds_greatest_stretch"]["ytLabel"]},
            {"id": f"m_{day_num}_2", "name": VIDEOS["doorway_stretch"]["name"], "sets": 3, "reps": "60s hold", "load": "Bodyweight", "tempo": "Chest & anterior delt opener", "rest": "30s", "yt": VIDEOS["doorway_stretch"]["yt"], "ytLabel": VIDEOS["doorway_stretch"]["ytLabel"]},
            {"id": f"m_{day_num}_3", "name": VIDEOS["t_spine_opener"]["name"], "sets": 3, "reps": "10 reps / side", "load": "Bodyweight", "tempo": "Thoracic mobilization", "rest": "30s", "yt": VIDEOS["t_spine_opener"]["yt"], "ytLabel": VIDEOS["t_spine_opener"]["ytLabel"]},
            {"id": f"m_{day_num}_4", "name": VIDEOS["lying_leg_raise"]["name"], "sets": 4, "reps": "12–15 reps", "load": "Bodyweight", "tempo": "Slow 3s eccentric descent", "rest": "45s", "yt": VIDEOS["lying_leg_raise"]["yt"], "ytLabel": VIDEOS["lying_leg_raise"]["ytLabel"]}
        ]
        evening_routine = {
            "core": {"id": f"e_{day_num}_1", "name": VIDEOS["stomach_vacuum"]["name"], "target": "4 sets x 20–25s vacuum hold on empty stomach", "yt": VIDEOS["stomach_vacuum"]["yt"], "ytLabel": VIDEOS["stomach_vacuum"]["ytLabel"]},
            "mobility": {"id": f"e_{day_num}_2", "name": VIDEOS["couch_stretch"]["name"], "target": "2 mins each side", "yt": VIDEOS["couch_stretch"]["yt"], "ytLabel": VIDEOS["couch_stretch"]["ytLabel"]},
            "cardio": {"id": f"e_{day_num}_3", "name": "Brisk Evening Walk", "target": "30 mins (3,500 steps) for lymphatic drainage", "yt": None, "ytLabel": None}
        }
        nutrition = {
            "isSunday": False,
            "highlight": "🥚 2 Boiled Eggs + Sattu/Dahi Cleanse (~110g Protein)",
            "breakfast": "2 Whole Boiled Eggs + PG Breakfast",
            "lunch": "PG Mess Lunch (Rotis, Dal, Sabzi, Salad)",
            "snack": "1 Scoop Whey Protein + 1 Glass Chilled Sattu or Curd",
            "dinner": "PG Mess Dinner (3 Rotis, Dal, Sabzi) + 30g Peanuts",
            "supplements": "Creatine 3–5g · 4.0L Water target (deep hydration day)",
            "estProtein": "~110–116g"
        }

    elif weekday_idx == 3:  # Thursday
        body_part = "Upper"
        title = "Upper Body Hypertrophy (Chest, Shoulders & Arms)"
        morning_exercises = [
            {"id": f"m_{day_num}_1", "name": VIDEOS["decline_pushup"]["name"], "sets": sets_count, "reps": "12–15 reps", "load": "Bodyweight (Feet on bed)", "tempo": "3-1-1-0 (Upper chest focus)", "rest": rest_time, "yt": VIDEOS["decline_pushup"]["yt"], "ytLabel": VIDEOS["decline_pushup"]["ytLabel"]},
            {"id": f"m_{day_num}_2", "name": VIDEOS["two_arm_db_row"]["name"], "sets": sets_count, "reps": "12 reps", "load": "2x 10kg", "tempo": "2-1-1-0 (Flat spine)", "rest": rest_time, "yt": VIDEOS["two_arm_db_row"]["yt"], "ytLabel": VIDEOS["two_arm_db_row"]["ytLabel"]},
            {"id": f"m_{day_num}_3", "name": VIDEOS["db_arnold_press"]["name"], "sets": sets_count, "reps": "10–12 reps", "load": "2x 5kg", "tempo": "3-1-1-0", "rest": rest_time, "yt": VIDEOS["db_arnold_press"]["yt"], "ytLabel": VIDEOS["db_arnold_press"]["ytLabel"]},
            {"id": f"m_{day_num}_4", "name": VIDEOS["db_hex_press"]["name"], "sets": sets_count, "reps": "12 reps", "load": "2x 5kg (Squeeze hard)", "tempo": "2-2-1-0", "rest": "60s", "yt": VIDEOS["db_hex_press"]["yt"], "ytLabel": VIDEOS["db_hex_press"]["ytLabel"]},
            {"id": f"m_{day_num}_5", "name": VIDEOS["diamond_pushup"]["name"], "sets": sets_count, "reps": "10–12 reps", "load": "Bodyweight", "tempo": "3-1-1-0", "rest": "60s", "yt": VIDEOS["diamond_pushup"]["yt"], "ytLabel": VIDEOS["diamond_pushup"]["ytLabel"]}
        ]
        evening_routine = {
            "core": {"id": f"e_{day_num}_1", "name": VIDEOS["rkc_plank"]["name"], "target": "3 sets x 30s maximum tension plank", "yt": VIDEOS["rkc_plank"]["yt"], "ytLabel": VIDEOS["rkc_plank"]["ytLabel"]},
            "mobility": {"id": f"e_{day_num}_2", "name": VIDEOS["bird_dog"]["name"], "target": "3 sets x 10 reps per side (Spine stabilization)", "yt": VIDEOS["bird_dog"]["yt"], "ytLabel": VIDEOS["bird_dog"]["ytLabel"]},
            "cardio": {"id": f"e_{day_num}_3", "name": "Brisk Evening Walk", "target": "25 mins (approx 3,000 steps)", "yt": None, "ytLabel": None}
        }
        nutrition = {
            "isSunday": False,
            "highlight": "🥚 2 Boiled Eggs + Soya Chunks Upper Body Fuel (~116g Protein)",
            "breakfast": "2 Whole Boiled Eggs + PG Breakfast + 1 Banana",
            "lunch": "PG Mess Lunch (Rice, Dal, Sabzi, Curd)",
            "snack": "1 Scoop Whey Protein + 40g Roasted Chana",
            "dinner": "35g Soya Chunks (boiled) mixed into PG Dinner + 3 Rotis",
            "supplements": "Creatine 3–5g · 3.5L Water",
            "estProtein": "~116–122g"
        }

    elif weekday_idx == 4:  # Friday
        body_part = "Lower"
        title = "Lower Athletic & Full Body Calisthenics"
        morning_exercises = [
            {"id": f"m_{day_num}_1", "name": VIDEOS["walking_lunges"]["name"], "sets": sets_count, "reps": "12 reps / leg", "load": "2x 5kg or Bodyweight", "tempo": "Controlled 90/90 step", "rest": rest_time, "yt": VIDEOS["walking_lunges"]["yt"], "ytLabel": VIDEOS["walking_lunges"]["ytLabel"]},
            {"id": f"m_{day_num}_2", "name": VIDEOS["single_leg_rdl"]["name"], "sets": sets_count, "reps": "10 reps / leg", "load": "1x 10kg", "tempo": "3-1-1-0 (Balance & hinge)", "rest": rest_time, "yt": VIDEOS["single_leg_rdl"]["yt"], "ytLabel": VIDEOS["single_leg_rdl"]["ytLabel"]},
            {"id": f"m_{day_num}_3", "name": VIDEOS["db_sumo_squat"]["name"], "sets": sets_count, "reps": "15 reps", "load": "1x 10kg", "tempo": "3-1-1-0 (Adductors & glutes)", "rest": rest_time, "yt": VIDEOS["db_sumo_squat"]["yt"], "ytLabel": VIDEOS["db_sumo_squat"]["ytLabel"]},
            {"id": f"m_{day_num}_4", "name": VIDEOS["pike_pushup"]["name"], "sets": sets_count, "reps": "8–10 reps", "load": "Bodyweight (Hips high)", "tempo": "3-0-1-0", "rest": rest_time, "yt": VIDEOS["pike_pushup"]["yt"], "ytLabel": VIDEOS["pike_pushup"]["ytLabel"]},
            {"id": f"m_{day_num}_5", "name": VIDEOS["single_leg_calf_raise"]["name"], "sets": sets_count + 1, "reps": "15 reps / side", "load": "1x 10kg", "tempo": "3-2-1-0", "rest": "45s", "yt": VIDEOS["single_leg_calf_raise"]["yt"], "ytLabel": VIDEOS["single_leg_calf_raise"]["ytLabel"]}
        ]
        evening_routine = {
            "core": {"id": f"e_{day_num}_1", "name": VIDEOS["hollow_body"]["name"], "target": "4 sets x 25s hollow body hold", "yt": VIDEOS["hollow_body"]["yt"], "ytLabel": VIDEOS["hollow_body"]["ytLabel"]},
            "mobility": {"id": f"e_{day_num}_2", "name": VIDEOS["doorway_stretch"]["name"], "target": "2 mins chest & shoulder decompression", "yt": VIDEOS["doorway_stretch"]["yt"], "ytLabel": VIDEOS["doorway_stretch"]["ytLabel"]},
            "cardio": {"id": f"e_{day_num}_3", "name": "Brisk Evening Walk", "target": "25 mins (approx 3,000 steps)", "yt": None, "ytLabel": None}
        }
        nutrition = {
            "isSunday": False,
            "highlight": "🥚 2 Boiled Eggs + Peanut/Chana Booster (~112g Protein)",
            "breakfast": "2 Whole Boiled Eggs + PG Breakfast",
            "lunch": "PG Mess Lunch (Rice, Dal, Sabzi, Curd)",
            "snack": "1 Scoop Whey Protein + 40g Roasted Peanuts",
            "dinner": "PG Mess Dinner (3 Rotis, 2 bowls Dal) + 1 cup Curd (Dahi)",
            "supplements": "Creatine 3–5g · 3.5–4.0L Water",
            "estProtein": "~112–120g"
        }

    else:  # Saturday (weekday_idx == 5)
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
            "mobility": {"id": f"e_{day_num}_2", "name": VIDEOS["doorway_stretch"]["name"], "target": "2 mins chest & anterior delt opening", "yt": VIDEOS["doorway_stretch"]["yt"], "ytLabel": VIDEOS["doorway_stretch"]["ytLabel"]},
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

    # Brain Mastery & Overthinking Protocol for this day
    brain_info = BRAIN_CURRICULUM[day_num - 1]
    brain_obj = {
        "theme": brain_info["theme"],
        "pillar": brain_info["pillar"],
        "principle": brain_info["principle"],
        "action": brain_info["action"],
        "habits": [
            {"id": f"b_{day_num}_sun", "name": "🌅 Sun Exposure & 3x Physiological Sighs (No Phone 60m)"},
            {"id": f"b_{day_num}_deepwork", "name": "⚡ 90-Min Deep Work Sprint (Single-Task Focus Block)"},
            {"id": f"b_{day_num}_overthinking", "name": "🧘 5-Sec Action / Brain Dump (Tame Overthinking Loop)"},
            {"id": f"b_{day_num}_shutdown", "name": "🌙 Night Cognitive Closure (Tomorrow's Top 2 + Screen Curfew)"}
        ]
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
        "brain": brain_obj,
        "evening": evening_routine,
        "nutrition": nutrition
    }

    days_data.append(day_obj)
    curr += datetime.timedelta(days=1)
    day_num += 1

print(f"Generated {len(days_data)} days successfully!")

# Write to workout_data.js
js_content = f"// 45-Day Total Transformation Dataset: Muscle & Brain Mastery (Nov 17 - Dec 31, 2026)\nconst WORKOUT_PLAN = {json.dumps(days_data, indent=2)};\n"
with open("/home/praveen/personal-projects/workout-tracker/workout_data.js", "w") as f:
    f.write(js_content)

# Write to workout_plan.json
with open("/home/praveen/personal-projects/workout-tracker/workout_plan.json", "w") as f:
    json.dump(days_data, f, indent=2)

print("Saved workout_data.js and workout_plan.json!")
