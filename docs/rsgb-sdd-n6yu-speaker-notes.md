# The Spec Is the New Schematic — Speaker Notes (v3)
John Carter, N6YU — RSGB Convention 2026 · ~35 min talk + Q&A

---

## 1. The Spec Is the New Schematic
**Takeaway:** **A spec does for an AI-built program what a schematic does for a radio**

- A schematic lets someone somewhat skilled understand and recreate a project.
- A spec does the same for software: it guides a builder.
- A schematic is not a detailed project description with PCB layout, testing, alignment, and a BOM.
- Taking vibe coding to the next level.

## 2. Presentation Available on GitHub
**Takeaway:** Scan the QR code to follow along with the presentation, now or later.
- Viewing is optional: the QR code opens the presentation, so you can follow along or look at it later.
- The QR code opens the talk repo on GitHub; the slides PDF is linked at the top of the page.
- The talk repo, `github.com/jcarter-labs/rsgb-sdd-n6yu`, also has the Masterplan Generator. The link is repeated on the conclusion slide (17).

## 3. Software Is Replacing Solder
**Takeaway:** AI coding is like building an engineering prototype - not as good as off product line, but fully functional.
- Tools and test: the soldering iron and scope on the older side; modules and software on the newer side. Storage: the file cabinet becomes GitHub.
- For a sense of how big radio software has become, look at a modern logger: rig control, internet, display, database, callsign lookup, propagation, and more.
- There are ways to get around the drawbacks

## 4. Remote Operation in Mojave Desert
**Takeaway:** Like many of us, I am plagued with local noise, so I like to get away. Really far away.
- Shows a camp in the setup process, late in the day arriving, tent not up, sun going down. 17' vertical whip antenna.
- The map shows roughly where in the Mojave 350 mi from home, 120 mi from LA, close to nothing but the desert town "Boron".
- I have Starlink and solar out there, but no panadapter. Just an older but excellent rig, the KX3. I really like panadapters.

## 5. Why Did I Bother? A Poor Man's Panadapter
**Takeaway:** No existing app combined a band-scope, POTA spots, and spotter selection, so I built one.
- I could tap the I/Q outputs and build a 50 kHz scope with FFT and display software, but that is a lot of hardware.  What if I just listen to local spotters?  Isn't that like a panadapter?
- POTA.APP shows maps and spots for hunting, but its interface prioritizes the map, not a bandscope.
- N1MM on Windows shows a bandscope, but not POTA spots.

## 6. Possible SDD Projects for Radio
**Takeaway:** SDD fits almost any shack project, from platform ports to Arduino builds to station control.
- This is a laundry list. SDD suits nearly anything.
- The screenshot is a keyer built from K6GTE's, ported from Linux to Mac.

## 7. Vibe Coding, Can Be Amazing!
**Takeaway:** Vibe coding nails the first 20% but leaves guessed assumptions, brittle code, and a lost chat.
- **POLL:** How many of you have vibe coded?
- **POLL:** How many of you have used GitHub?

## 8. Key Terms
**Takeaway:** A small shared vocabulary is all you need to follow the rest of the talk.
- **Spec:** the AI community's name for a Masterplan, the whole document.
- **Masterplan (MP):** the 4-part Spec for your app: Ground Rules, Project Brief, Architecture, and Task Plan.
- **Masterplan Generator:** a document that guides you in writing a masterplan for your app. It makes complex software buildable without software-engineering skills.
- **SDD:** Spec-Driven Development, a process. The spec stays the source of truth as the code changes.

## 9. A Better Alternative: SDD
**Takeaway:** The model is better at extracting requirements from you than you are at defining them.
- Vibing wasn't working for organizations. SDD is not rigid, comes in many forms, and is still developing.
- The process uses AI to extract requirements: the model is better at extracting requirements from you than you are at defining them.
- Overall time is shorter: more time on the spec, less on coding and debugging. It is also self-documenting.

## 10. Preliminaries: Claude Code & GitHub Setup
**Takeaway:** Claude is vastly more powerful than chat.
- Claude Code is now available in Claude Desktop (little toggle in upper left)
- **GitHub is a Superpower.** Claude can help you figure it out.

## 11. SDD in a Nutshell: Masterplan Generator + Idea + Screenshot
**Takeaway:** **This is the talk in one slide.**
- The name is not special; call it anything. The contents are not unique either. The four sections come from best practices at many tech companies (Amazon, Anthropic, Microsoft).

## 12. Use Generator + Your Idea to Create a Masterplan
**Takeaway:** Ground Rules, Project Brief, Architecture, Task Plan: four steps from idea to a buildable plan.
- **Ground Rules (how we work): another Superpower.** Use the Generator's prompts as-is. They keep you out of vibing trouble.
- **Project Brief (what it does):** give Claude your app idea, and the Generator asks you questions to customize the Project Brief. This is where the unknown unknowns come out.
- **Architecture (built with):** If you don't know the answers, use Claude Desktop (or another Claude Code instance) to help fill it in.
- **Task Plan (in what order):** the Generator structures the project into about 5 chunks: Setup, Connections, Core Logic, Main Features, UI.

## 13. Example: Idea + Screenshot → Masterplan Generator
**Takeaway:** A short idea plus one screenshot is enough input; the generator interviews you for the rest.

## 14. The Masterplan Generator
**Takeaway:** The generator lives on GitHub as plain, readable text anyone can open and reuse.
- Each prompt carries a label: RULE (follow it during the build), DRAFT (write this part now and show me), USER INPUT (ask me first).

## 15. Claude Code with Claude Desktop as Helper (Screenshot)
**Takeaway:** **Superpower:** when Code's output is confusing, ask Desktop to explain and paste the answer back.

## 16. It Works! Multiplatform Screenshots
**Takeaway:** One spec produced the same working app on Mac, Windows, and Linux.

## 17. Conclusion
**Takeaway:** Vibe coding gets you started; the masterplan gets you finished, so start small with your own idea.
- Call back to the opening: like a schematic, the spec is what you keep and share.
- The QR code points to the GitHub repo for this talk, which has the Masterplan Generator and the presentation. Your first masterplan starts here.

## 18. Time for Your Road Trip! Your Idea (Questions?)
**Takeaway:** Close on the road-trip image and open the floor: Claude Code and GitHub are the transportation, your idea is the trip.
- Callback to slide 4: same desert trails. The idea is the destination, Claude Code and GitHub are the vehicle, and the spec is the plan you drive from.
- Invite questions. Leave this slide up through Q&A.
- Keep the slide numbers handy. Type a number to jump: **14** for the generator, **17** for the repo link, **19** for references.

---

## Appendix
### 19. Appendix – References
**Takeaway:** Where to go deeper on SDD and Claude Code.

### 20. Find out more… (closing)
**Takeaway:** How to reach me.
- John Carter, N6YU, john@n6yu.com, `github.com/jcarter-labs`.
