# Masterplan Generator: 20 Prompts for Spec-Driven Development

You answer five questions about your app, then paste the prompts below into Claude Code, the **agent**. The agent builds `masterplan.md` from them: an outline of your app that becomes its source of truth. Later, the agent builds your app from that masterplan.

**Label key** *(for you to read; don't paste)*

- **RULE:** the agent writes it into the masterplan and follows it during the build, not now.
- **DRAFT:** the agent writes that part of the masterplan now, and shows it to you for review.
- **USER INPUT:** the agent asks you first, then writes down your answer.
- **SET:** use it for your own answers and decisions; the agent writes them in as given.
- **PASTE:** a plain instruction to paste as is.

Paste only what's in the grey boxes. Everything else is for you to read.

## Before you start

New to Claude Code, or already using it? Either works. If you have a `CLAUDE.md` with your own standing instructions, keep it: the agent follows it alongside the masterplan.

1. **Install Claude Code** if you haven't (see docs.claude.com).

2. **Open a terminal** (Terminal on Mac, PowerShell on Windows, your terminal on Linux), go to your app's folder, and start the agent. Pick one:

   - **New folder** (`myapp` can be any name):

     ```
     mkdir myapp
     cd myapp
     claude
     ```

   - **Folder you already have** (type `cd` and a space, drag the folder into the window, press Return):

     ```
     cd <your folder>
     claude
     ```

   Everything from here happens in this window.

3. **Give the agent your screenshot** of an app like the one you want. Paste:

   ```
   PASTE: Find my screenshot in this folder, or ask me where it is. Copy it here as screenshot.png, keeping the original. It shows the look I want; don't build anything yet.
   ```

   If the agent asks where it is, drag the screenshot file into the window (that types its location), and press Return.

4. **Write your app brief with the agent.** Paste this; the agent asks you five questions, one at a time, and saves your answers as `idea.md`:

   ```
   PASTE: If idea.md exists, show it and ask what to change. Otherwise, interview me for my app brief, one question at a time. 1) What does my app do, for whom, and is it like an existing app? If so, give a link to it (repo, manual or web page) and which of its behaviours matter to me. 2) Which computer do I build on, and which must it also run on? 3) What are its main features, most important first? 4) What do I enter or set, with typical values or ranges? 5) What does the screen show, and where does its data come from? If an answer is vague, ask me for specifics. Then save my answers as idea.md and show it to me.
   ```

5. **Give your app its own repo.** This works even if a folder above yours is already a repo. Paste:

   ```
   PASTE: Make this folder its own git repo: run git init here, even if a folder above it is a repo, and check that git rev-parse --show-toplevel prints this folder. If it has no GitHub repo, create one, private or public as I choose. Commit and push idea.md and my screenshot.
   ```

6. **Paste the setup line:**

   ```
   PASTE: Create masterplan.md with only four empty section headings: Ground Rules, Project Brief, Architecture, Task Plan; don't fill them in. Put one line under each: Ground Rules, how we work, and they override everything else; Project Brief, what the app does and how we'll check it; Architecture, what it's built with, and it constrains the Task Plan; Task Plan, ordered tasks with dependencies and done-criteria. If it exists, show it instead. Read idea.md, my screenshot, and any CLAUDE.md in this folder; list any conflicts, and any memory notes you're using, one line each, for me to decide.
   ```

7. **Paste the legend** once. This is how the agent learns the labels:

   ```
   PASTE: Each line I send starts with a label. RULE: add it to masterplan.md as written; follow it during the build, not now. DRAFT: write that part of masterplan.md, then show me for review. USER INPUT: ask me first, then write my answer into masterplan.md. SET: write my answer into masterplan.md as given. Put each line in the section it's pasted under. Sections come in order; don't draft ahead.
   ```

## 1. Ground Rules: how we work *(paste all five at once)*

```
RULE: Build from masterplan.md, idea.md and my screenshot; borrow language, tools, specs, or open-source code from examples as I choose.
RULE: At the start of the build, check tools, libraries, GitHub login, that this folder is its own repo root, and that each data source's host and port can be reached, on my platforms; show pass/fail.
RULE: After each change, measure the app against the Project Brief's screen list; show pass/fail.
RULE: After each working step: run all tests, show me proof, commit, and push to GitHub. Keep going within a stage; stop only at stage end, on a failed test, after two failed fixes, or for my decision.
RULE: When code and masterplan disagree, propose only major changes, one line each; update the masterplan after I approve.
```

## 2. Project Brief: what the app does *(one at a time)*

```
DRAFT: Summarize what my app does in a few sentences, from idea.md, my screenshot, and any example app.
```
```
DRAFT: From my screenshot, list screen elements and controls, with where each sits.
```
```
DRAFT: For each feature in idea.md, describe what the user does and sees, with testable ranges where possible.
```
```
DRAFT: List where my app's data comes from, and how we'll check each source works, including after a reconnect. Send every server setting on each connect; never rely on settings from earlier sessions.
```
```
USER INPUT: Ask which features from idea.md my app must do this iteration, and which wait; suggest if I'm unsure.
```

## 3. Architecture: what it's built with *(one at a time)*

```
USER INPUT: Recommend a language and tools, Python unless my example suggests better; explain each and let me choose.
```
```
DRAFT: List what must be installed on each platform in idea.md, and how to check each works.
```
```
RULE: Keep the app responsive while it works, never stuck waiting on data or input.
```
```
DRAFT: Propose a handful of well-structured modules, one line each, each testable on its own.
```
```
RULE: Keep a short list of known limitations in the masterplan; update it as we go.
```

## 4. Task Plan: in what order *(one at a time)*

```
DRAFT: Break the build into about 5 stages: environment (including measuring my screenshot with a script), data connections tested on live servers and ending with a bare window showing live data, core logic, features, and UI. Give each stage sub-steps and one done-when line.
```
```
DRAFT: For each sub-step, say how we'll test it and what result means it works.
```
```
RULE: Test connections to outside data with real servers before building screens that depend on them.
```
```
RULE: Get a simple version running early, then add features one at a time, testing each.
```
```
DRAFT: Add a final step: review what went wrong and propose masterplan updates for my approval.
```

## After you finish

1. **Tighten:**

   ```
   PASTE: Tighten masterplan.md: remove repetition and prose; keep every number, range, rule and done-when line. Show me the line count before and after.
   ```

2. **Review it:**

   ```
   PASTE: Show me masterplan.md.
   ```

   Read it, and tell the agent in plain words anything to change.

3. **Pressure-test:**

   ```
   PASTE: Pressure-test masterplan.md for ambiguity; list unclear items with one-line fixes for my approval.
   ```

4. **Save to GitHub:**

   ```
   PASTE: Commit and push masterplan.md.
   ```

5. **Build.** Type `/exit` to end this session, then type `claude` again to start a fresh one in the same folder, and paste:

   ```
   PASTE: Build from masterplan.md, starting with Task 1. Keep going unless a test fails or you need my decision.
   ```

## Watch for

- **"Looks close" is not a pass.** Eyeballing a screen is not a test; ask the agent for the measured pass/fail output.
- **Two failed fixes on the same bug:** stop, and ask the agent what it measured.
- **"Should work" means untested.** Ask the agent for proof.
- **When a data source fails,** ask the agent for likely causes and fixes.
- **Agent can't reach a server:** Claude Code's sandbox blocks some network ports. Run the command it gives you in a second terminal, or allow it for that host only.
- **Tests:** never let the agent change a test just to make it pass.
- **Borrowed code:** note its license in the commit. GPL code makes your whole app GPL.
- **GitHub:** your app's folder needs its own repo (Before you start, step 5). A folder inside another repo commits to the parent.
- **Keep the masterplan tight, not thin:** cut prose and repetition, but keep every testable number and rule.
