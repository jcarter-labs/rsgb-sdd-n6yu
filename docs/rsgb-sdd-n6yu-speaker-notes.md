# The Spec Is the New Schematic — Speaker Notes (v2)
John Carter, N6YU — RSGB Convention 2026 · ~35 min talk + Q&A

---

## 1. The Spec Is the New Schematic
**Takeaway:** The spec is the durable design artifact for station software, just as the schematic is for hardware.
- Two goals started this: sharing projects easily in RadCom, and getting a spotter for my Elecraft KX3.
- I like Mad Max–style trips off the grid on desert public lands. I have Starlink and solar out there, but no bandscope.
- Computer science has an idea that if you fully specify an app's behavior and fully test it, the spec *defines* the software.
- I wanted to see whether that idea is practical, so I tried combining vibe coding with specifications.
- AI is extremely powerful here. Most engineers I know will never go back to coding without it.

## 2. Software Is Replacing Solder
**Takeaway:** AI coding is good enough for radio projects, but on its own it is neither repeatable nor structured.
- The 2×2 matrix is conceptual. Station builders now use modules and software where we used to use solder smoke and leaded parts.
- For a sense of how big radio software has become, look at a modern logger: rig control, internet, display, database, callsign lookup, propagation, and more.

## 3. Key Terms
**Takeaway:** A small shared vocabulary is all you need to follow the rest of the talk.
- The terms in green come up throughout the talk.
- The talk is nominally about SDD, but the spec also carries rules of engagement and a schedule. Spec plus schedule is what I call a **masterplan**.
- **Masterplan Generator:** a document that guides you in writing a spec for your app. It makes complex software buildable without software-engineering skills.

## 4. Why Did I Bother? A Poor Man's Panadapter
**Takeaway:** No existing tool combined a bandscope with POTA spots, so I built one.
- I really like panadapters, but older rigs like the KX3 don't have one.
- I could tap the I/Q outputs and build a 50 kHz scope with FFT and display software, but that is a lot of hardware.
- It has also always bugged me that POTA.app lacks the band-scope view that many loggers now offer.
- I'm a CW operator. If you filter to local skimmers, the spots are a good indication of where the action is.

## 5. Possible SDD Projects for Radio
**Takeaway:** SDD fits almost any shack project, from platform ports to Arduino builds to station control.
- This is a laundry list. SDD suits nearly anything.
- The most interesting possibilities:
  - helping experimenters build open-source projects from GitHub
  - porting apps if you don't run Windows
  - building from magazine articles
- The screenshot shows a keyer by K6GTE, ported from Linux to Mac.

## 6. Vibe Coding, Can Be Amazing!
**Takeaway:** Vibe coding nails the first 20% but leaves guessed assumptions, brittle code, and a lost chat.
- **POLL:** How many of you have vibe coded?
- **POLL:** How many of you have used GitHub?
- Software is complicated. You can describe an idea, but it's very hard for AI to guess the UI, the data interfaces, the OS it runs on, and so on.

## 7. A Better Alternative: SDD
**Takeaway:** Spec, build, test, update the spec: the spec, not the code, becomes the deliverable.
- I find it far less frustrating to spend more time up front and then have the code compile, pass its tests, and work reliably.
- The illustrative schedules show the difference: more time up front, but much less total time to a robust app.
- The flow diagram compares this with typical software development, where you write a spec and then abandon it once coding starts.
- SDD treats the spec as the code.

## 8. Vibe Prompt vs. SDD
**Takeaway:** SDD trades a slower start for tested, repeatable, shareable results you can change later.
- Give the AI the basic idea *plus a screenshot*, then have it build the spec, i.e. the masterplan.

## 9. Preliminaries: Claude Code & GitHub Setup
**Takeaway:** A $20 plan plus GitHub gets you started, and GitHub lets you find your work years later.
- Claude Code runs in a terminal (e.g. PowerShell) or in the desktop app.
- Compared with chat, Code does real work. It interacts with your machine, apps, and websites, and you keep granular control.
- Why dwell on GitHub? **Superpower.** It lets me find what I built.
- GitHub combined with Claude Code is self-documenting.

## 10. Masterplan Generator + Idea + Screenshot
**Takeaway:** The generator walks you through building a masterplan tailored to your app.
- **This is the talk in one slide.**
- `idea.md` is a 5–7 sentence description. Code converts it to Markdown.
- The Generator is just a Markdown file. Markdown is plain text with simple formatting.
- It helps you create a plan, including your spec, for prompting the AI to build your app.
- The name is not special; call it anything.
- The contents are not unique either. The four sections come from best practices at many tech companies.
- Each section has 5 prompts. The Generator walks you through creating a spec so you can breeze through the coding.

## 11. Use Generator + Your App Idea to Create Detailed Masterplan
**Takeaway:** Constitution, Spec, Tech, Tasks: four steps from idea to a buildable plan.
- **Constitution: another Superpower.** It sets the rules: don't invent, copy the screenshot exactly, test every step.
- **This keeps you out of vibing trouble!**
- **Spec** fleshes out your idea.
- **Tech** steers the approach the AI takes for each component.
  - If you don't know the answers, use Claude Desktop (or another Claude Code instance) to help fill it in.
  - You can also point to an existing app, even a commercial one, or a similar open-source project. Claude can find those by searching.
- **Tasks:** you can usually race through these. I recommend about 5 for most apps.

## 12. The Masterplan-Generator (GitHub is Readable!)
**Takeaway:** The generator lives on GitHub as plain, readable text anyone can open and reuse.
- This is the core of the Generator document. The Constitution is simply pasted in as a chat.
- The other sections have 5 prompts each. Five is an arbitrary level of detail; I arrived at it by building the spotter on several platforms and rebuilding it two more times.

## 13. Claude Code and Claude Desktop as Helper
**Takeaway:** When Code's output is confusing, ask Desktop to explain and paste the answer back.
- **Superpower.**
- I have a technical background but I'm not current on modern tech stacks. I keep a Claude Desktop session open to decode Claude Code's often wordy, confusing output.
- When stuck, paste Code's output into Desktop, ask for help, then paste Desktop's answer back into Code.
- One agent ends up guiding a completely separate agent.

## 14. DX Spotter | The Working Result
**Takeaway:** The spec-built app works: live RBN bandmap, POTA hunting, and three cluster types.
- Supports three cluster types: AR-Cluster 6, CC Cluster, and DX Spider.
- Regional skimmers serve contesting; local skimmers act as a panadapter stand-in.

## 15. Multiplatform Screenshots (also runs on Linux)
**Takeaway:** One spec produced the same app on Mac, Windows, and Linux.
- Built on three platforms: Windows 11, Ubuntu 26.04, and macOS 26.
- Repeated builds: Windows ×3, Mac ×2.
- Sometimes a build came out better, so I used its screenshot as the new reference. The idea itself never changed.

## 16. Conclusion
**Takeaway:** Vibe coding gets you started; the masterplan gets you finished, so start small with your own idea.
- Jot down the idea, have the agent build the masterplan, *then* have it build the code.
- Build and test every task step, update the masterplan as you go, and let GitHub remember it.
- Start small: Generator prompts, a screenshot, and your app idea. Your first masterplan starts here.

---

## Appendix
### 17. Appendix – GitHub Links
**Takeaway:** Everything shown today is in two public repos.

### 18. Appendix – References
**Takeaway:** Where to go deeper on SDD and Claude Code.

### 19. Find out more… (closing)
**Takeaway:** How to reach me.
