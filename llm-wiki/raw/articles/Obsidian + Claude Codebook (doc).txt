THE OBSIDIAN + CLAUDE
CODE CODEBOOK
12 commands to build for your second brain
Vin (Internet Vin) uses Obsidian and Claude Code together as a personal operatingsystem. He built custom slash commands that let Claude Code read his entire vault,surface patterns across years of notes, and generate ideas he would never see on hisown.
This guide breaks down 12 commands Vin demonstrated. Each one turns your notesinto a different kind of thinking tool. You can build all of them yourself.
Inside: the core setup, how to create commands, and 12 slash commands with exampleprompts.
Tools Referenced
Claude Code
Obsidian
Obsidian CLI
The Setup
Claude Code can control your computer through natural language. Obsidian stores yournotes as interlinked markdown files. Obsidian CLI connects them.
Once connected, Claude Code can see both your files AND the relationships betweenthem. It knows that your note on filmmaking links to your note on world building. It cantrace how an idea evolved over months. It can find patterns you missed.

The key insight: the quality of context you feed the agent determines what it can do foryou. Your vault is that context.
How to Build These Commands
You don't need to code. You ask Claude Code to create the command for you.
Example:
None
Create a slash command called /trace that tracks how a specificidea has evolved over time across my Obsidian vault. It should:
1. Take a topic as input
2. Search the vault for all mentions of that topic
3. Use Obsidian CLI to follow backlinks and find related notes
4. Output a timeline showing when the idea first appeared, how itevolved, and what it's connected to now
Claude Code will generate the command and save it. Then you just type /trace to runit.
Start with one command. Test it. Refine the prompt if needed. Then build the next one.
The Commands
Each command is a different way to use your vault as a thinking partner.
1. /context
What it does: Loads your full life and work state into Claude Code. Projects,preferences, priorities, current focus.
When to use it: At the start of any session where you want the agent to knoweverything relevant about you.

None
Read my vault and summarize my current context. Include activeprojects, recent reflections, and any priorities I've mentionedin the last 7 days.
2. Itoday
What it does: Pulls your calendar, tasks, and daily notes into a prioritized plan for theday.
When to use it: Morning planning. When you're overwhelmed and need clarity on whatmatters.
None
Read my daily note, calendar, and task list. Generate aprioritized plan for today based on what I've said is importantthis week.
3. Itrace
What it does: Tracks how a specific idea has evolved over time across your notes.
When to use it: When you want to see the arc of your thinking. When an idea keepscoming up and you want to understand why.
None
Trace the idea of [topic] across my vault. Show me when it firstappeared, how it evolved, and what it's connected to now.
4. Iconnect
What it does: Bridges two domains using the link graph in your vault. Finds unexpectedconnections between topics.

When to use it: When you're stuck. When you suspect two ideas are related but can'tsee how.
None
Find connections between [topic A] and [topic B] in my vault.Show me the notes that link them and any patterns you see.
5. Ighost
What it does: Answers a question the way you would, based on your writing and statedbeliefs.
When to use it: When you want to externalize your own thinking. When you need adraft response that sounds like you.
None
Based on my vault, how would I answer this question: [question]?
Use my voice and reference specific notes where relevant.
6. /challenge
What it does: Pressure-tests your current beliefs. Finds contradictions or weak pointsin your thinking.
When to use it: Before making a big decision. When you want to stress-test an idea.
None
Review my notes on [topic]. Where am I contradicting myself? Whatassumptions am I making that might be wrong?
7. lideas
What it does: Scans your vault and generates a full idea report. Tools to build, peopleto meet, subjects to investigate, things to write.

When to use it: When you want fresh ideas grounded in your actual interests andpatterns.
None
Scan my vault for emerging patterns. Generate ideas for: tools Ishould build, people I should reach out to, topics I shouldinvestigate, and things I should write.
8. Igraduate
What it does: Extracts undeveloped ideas from daily notes and promotes them intostandalone files.
When to use it: Weekly review. When your daily notes are full of half-formed thoughtsthat deserve their own space.
None
Scan my daily notes from the past 14 days. Find ideas thatdeserve their own note. For each one, create a standalone filewith the core claim, context, and connections to other notes.
9. Icloseday
What it does: Captures what happened today and what you learned. The counterpartto /today.
When to use it: End of day. When you want to log progress and clear your head beforetomorrow.
None
Review what I worked on today. Summarize progress, capture anynew ideas that came up, and note anything unfinished that shouldcarry over to tomorrow.

10. /drift
What it does: Surfaces loosely connected ideas that keep appearing across your noteswithout a clear thread.
When to use it: When you sense something emerging but can't name it. When youwant to see what your subconscious is circling.
None
Scan my vault for recurring themes or phrases that appear acrossunrelated notes. What ideas am I drifting toward withoutrealizing it?
11. /emerge
What it does: Identifies patterns that are starting to coalesce into something bigger.
When to use it: When you want to see what ideas are ready to become projects. Whenscattered thoughts are starting to cluster.
None
Find clusters of related ideas in my vault that could become aproject, essay, or product. Show me what's emerging and whatnotes connect to it.
12. Ischedule
What it does: Reads your priorities and calendar, then suggests how to allocate yourtime.
When to use it: Weekly planning. When you need to map your stated priorities to actualtime blocks.

None
Based on my current projects and priorities, suggest a schedulefor this week. Flag any conflicts between what I say matters andhow I'm spending time.
Final Note
Start by writing daily. The commands only work if your vault has context. Pick onecommand from this list. Ask Claude Code to build it. Run it. See what surfaces. Refinethe prompt if needed, then build the next one.
The more you write, the more the agent can do for you.
Want To Learn More?
Follow Vin on X and YouTube. Explore his site at internetvin.com.
"The quality of information that the agent has entirely determineswhat it can do for you. If it doesn't know a lot about you, it's not goingto be able to do a lot for you."
- Vin