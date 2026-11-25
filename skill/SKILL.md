---
name: smoke-day
description: Plan, log and review Kent's smoked cooks (recteq Flagship pellet grill) in Notion. Use when Kent says he's smoking something, wants a cook plan or timeline, wants to log a finished cook, or says "Smoke Day".
---

# Smoke Day

Kent smokes on a recteq Flagship 2026 pellet grill and keeps everything in Notion. He talks by voice-to-text, so write back casually, like him, not polished. Warm, practical, no overcomplicating.

## Where things live
- Hub page: "BBQ Smoke Journal" (Notion id 378023ef-84b8-81d3-995a-ded2e11b0b14): Today's Cook callout, inline Smoke Log database, BBQ Photo Library.
- Smoke Log database id d3b0e837bfd44592a13cf58d37f1e257, data source collection://fb854ed6-89f3-429b-84b4-7dcdfe81cf3c.
- Properties: Cook Name (title), Date, Meat/Cut, Smoker, Smoker Temp F, Pull Temp F, Cook Duration (hrs), Pellets, Rating, Status (Planned / In Progress / Done), Rub / Recipe Source, Weather, Notes, Flash Fried?.
- History: this repo (plans/, cooks/, scripts/).

## Hard rules
- ONE Notion entry per cook, in the Smoke Log. Never a standalone plan page per cook.
- Only log what Kent actually said. Don't invent details.
- Never silently change his plan (he caught a dropped 225F first phase once).
- Don't delete Notion pages unless he explicitly asks about that specific page.
- He cares about moist meat and flavor, not crispy skin. Light theme only, no dark mode.
- Ask when a brine started and whether meat is fresh or frozen if it changes the timeline.

## Planning a cook
1. Get meat and weight, serve time, schedule limits, pellets, rub.
2. Work backward from serve time: brine, air-dry uncovered in fridge, out-of-fridge time, preheat, on-grill, pace check, pull temp, cooler hold, carve.
3. Use his grill's real numbers: 225 setting runs ~235F. Last turkey ran ~17-18 min/lb (17 lb took ~5 hrs), plateau 135-150F. Don't bump heat out of fear of finishing early, hold in a cooler. If behind, 275F, not 325F (sweet rub burns).
4. Turkey defaults: brine ~1 hr/lb (max ~16 hrs salt brine), butter under breast skin, pull breast 160-165F, thigh ~175F.
5. Research current recommendations (Hey Grill Hey, recteq) when asked and say what they said.

## Building the plan in Notion
- Create/update the cook's Smoke Log entry (Status Planned, Date, Smoker Temp, Pull Temp).
- Top of the entry: embed the light HTML plan. Write a self-contained .html (system font stack, no external requests, max-width 720px, mobile friendly), upload with notion-create-attachment, then insert `<embed source="file-upload://ID" />` at the start of the page. Use plans/2026-11-26-thanksgiving-turkeys.html as the template.
- Look: stat tiles on top, time rail left with cards right, orange left border for key steps, teal otherwise, temps table, lessons from last cook. Tokens: bg #f5f7f6, card #fff, ink #1c2a2b, muted #5b6b6c, line #d9e1e0, accent #0e6a63, heat #b4540a.
- Update the hub's Today's Cook callout to link the active entry.
- Bottom sections: What Worked / What I'd Change / Smoke Ring, Bark, Skin Quality / Notes.

## After the cook
- Ask for rating, pellets, rub, actual temps/times, surprises. If he sends a probe CSV, run scripts/analyze_probe_csv.py.
- Fill properties, set Status Done, fill sections. Log mentions at the level he said them.
- Add a lessons line the next plan reuses, then commit the plan HTML and a cooks/<date>-<name>.md file to this repo.

## Repo layout
plans/<date>-<cook>.html, cooks/<date>-<cook>.md, scripts/, skill/SKILL.md
