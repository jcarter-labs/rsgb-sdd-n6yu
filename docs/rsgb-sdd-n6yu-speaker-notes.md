# The Spec Is the New Schematic — Speaker Notes (v3)
John Carter, N6YU — RSGB Convention 2026 · ~35 min talk + Q&A

---

## 1. The Spec Is the New Schematic
**Takeaway:** **A spec does for an AI-built program what a schematic does for a radio**
- The title only hints at the talk; it is really about taking vibe coding to the next level.
- A schematic lets someone somewhat skilled understand and recreate a project.
- A spec does the same for software: it guides a builder. It is not a detailed description with PCB layout, testing, alignment, and a BOM.

## 2. Presentation on GitHub
**Takeaway:** Scan the QR code to get the presentation PDF from GitHub.
- The QR code opens the presentation PDF in the talk repo, `github.com/jcarter-labs/rsgb-sdd-n6yu`.
- The repo also has the Masterplan Generator. The links are repeated in the appendix (slide 19).

## 3. Remote Operation in Mojave Desert
**Takeaway:** Like many of us, I am plagued with local noise, so I like to get away. Really far away.
- Shows a camp in the setup process, late in the day arriving, tent not up, sun going down.  17' vertical whip behind 
- The map shows roughly where in the Mojave 350 mi from home, 120 mi from LA, close to nothing but the desert town "Boron".
- I have Starlink and solar out there, but no bandscope. Just an older but excellent rig, the KX3. I really like bandscopes.

## 4. Software Is Replacing Solder
**Takeaway:** AI coding is good enough for radio projects, but on its own it is neither repeatable nor structured.
- Tools and test: the soldering iron and scope on the older side; modules and software on the newer side. Storage: the file cabinet becomes GitHub.
- For a sense of how big radio software has become, look at a modern logger: rig control, internet, display, database, callsign lookup, propagation, and more.
- There are ways to get around the drawbacks

## 5. Key Terms
**Takeaway:** A small shared vocabulary is all you need to follow the rest of the talk.
- **Specs:** your app's features and behaviors, in plain language with testable numbers.
- **Masterplan:** the spec plus the rules, the tech choices, and the ordered tasks for building your app.
- **Masterplan Generator:** a document that guides you in writing a masterplan for your app. It makes complex software buildable without software-engineering skills.
- **SDD:** an AI-updated plan of record. The spec stays the source of truth as the code changes.

## 6. Why Did I Bother? A Poor Man's Panadapter
**Takeaway:** No existing tool combined a bandscope, POTA spots, and spotter selection, so I built one.
- I could tap the I/Q outputs and build a 50 kHz scope with FFT and display software, but that is a lot of hardware.  What if I just listen to local spotters?  Isn't that like a panadapter?
- POTA.APP shows maps and spots for hunting, but its interface prioritizes the map, not a bandscope.
- N1MM on Windows shows a bandscope, but not POTA spots.

## 7. Possible SDD Projects for Radio
**Takeaway:** SDD fits almost any shack project, from platform ports to Arduino builds to station control.
- This is a laundry list. SDD suits nearly anything.
- The screenshot is a keyer built from K6GTE's, ported from Linux to Mac.

## 8. Vibe Coding, Can Be Amazing!
**Takeaway:** Vibe coding nails the first 20% but leaves guessed assumptions, brittle code, and a lost chat.
- **POLL:** How many of you have vibe coded?
- **POLL:** How many of you have used GitHub?

## 9. A Better Alternative: SDD
**Takeaway:** This is the talk in one sentence
- More time up front, but faster and self documenting

## 10. Preliminaries: Claude Code & GitHub Setup
**Takeaway:** Claude is vastly more powerful than chat.
- Claude Code is now available in Claude Desktop (little toggle in upper left)
- **GitHub is a Superpower.** Claude can help you figure it out.

## 11. Masterplan Generator + Idea + Screenshot
**Takeaway:** **This is the talk in one slide.**
- The name is not special; call it anything. The contents are not unique either. The four sections come from best practices at many tech companies (Amazon, Anthropic, Microsoft).

## 12. Use Generator + Your Idea to Create a Masterplan
**Takeaway:** Constitution, Spec, Tech, Tasks: four steps from idea to a buildable plan.
- **Constitution (how we work): another Superpower.** Use the Generator's prompts as-is. These are ground rules, and they keep you out of vibing trouble.
- **Spec (what it does):** give Claude your app idea, and the Generator asks you questions to customize the spec. This is where the unknown unknowns come out.
- **Tech (built with):** If you don't know the answers, use Claude Desktop (or another Claude Code instance) to help fill it in.

## 13. Example: Idea + Screenshot → Masterplan Generator
**Takeaway:** A short idea plus one screenshot is enough input; the generator interviews you for the rest.

## 14. The Masterplan Generator (Download from Link in Appendix)
**Takeaway:** The generator lives on GitHub as plain, readable text anyone can open and reuse.
- Each prompt carries a label: RULE (follow it during the build), DRAFT (write this part now and show me), USER INPUT (ask me first).

## 15. Claude Code and Claude Desktop as Helper
**Takeaway:** **Superpower:** when Code's output is confusing, ask Desktop to explain and paste the answer back.

## 16. It Works! Multiplatform Screenshots
**Takeaway:** One spec produced the same working app on Mac, Windows, and Linux.

## 17. Conclusion
**Takeaway:** Vibe coding gets you started; the masterplan gets you finished, so start small with your own idea.
- Call back to the opening: like a schematic, the spec is what you keep and share.
- The QR code points to the GitHub repo for this talk, which has the Masterplan Generator and the presentation. Your first masterplan starts here.

## 18. Time for Your Road Trip! Your Idea (Questions?)
**Takeaway:** Close on the road-trip image and open the floor: Claude Code and GitHub are the transportation, your idea is the trip.
- Callback to slide 3: same desert trails. The idea is the destination, Claude Code and GitHub are the vehicle, and the spec is the plan you drive from.
- Invite questions. Leave this slide up through Q&A.
- Keep the slide numbers handy. Type a number to jump: **14** for the generator, **19** for the repo links, **20** for references, **23** for the DX Spotter feature list.
- If someone asks for the side-by-side of vibe coding and SDD, slide 22 is in the backup section.

---

## Appendix
### 19. Appendix – GitHub Links
**Takeaway:** Everything shown today is in two repos, one for the talk and one for the app.
- Talk repo: `github.com/jcarter-labs/rsgb-sdd-n6yu`. It has the slides, the example masterplan, and the Masterplan Generator.
- Code repo: `github.com/jcarter-labs/dx-spotter-app`. It has the DX Spotter app.
- The QR codes on the slide point to each repo.
- Contact: John Carter, N6YU, john@n6yu.com, `github.com/jcarter-labs`.

### 20. Appendix – References
**Takeaway:** Where to go deeper on SDD and Claude Code.

### 21. Find out more… (closing)
**Takeaway:** How to reach me.
- John Carter, N6YU, john@n6yu.com, `github.com/jcarter-labs`.

---

## Backup
These two slides sit after the closing slide in the deck. They are not in the main flow.

### 22. Vibe Prompt vs. SDD
**Takeaway:** SDD trades a slower start for tested, repeatable, shareable results you can change later.
- Give the AI the basic idea *plus a screenshot*, then have it build the spec, i.e. the masterplan.
- Walk the rows: Prompt, Details, Testing, Speed, Later.
- The honest cost is the Speed row: SDD has a slower start and more work up front. The payoff is the Later row: edit the spec, rebuild from GitHub, add features or change OS.

### 23. DX Spotter | The Working Result
**Takeaway:** The spec-built app works: live RBN bandmap, POTA hunting, and three cluster types.
- Bandmap: live RBN spots with an adjustable window, working (compared with N1MM).
- POTA.APP hunting view: working (compared with POTA.APP).
- Frequency, bandscope window width, and timeout menu.
- Spotter selection: Local (within about 50 miles) and Regional (within about 250 miles).
- Cluster server menu: three major server types supported.
- Status indication for the RBN and POTA servers.
- Out of scope today: DE (spotter) specification, CAT control, and a mobile UI.
- One build produced green spots for POTA, so I kept that one as the starter screenshot.
