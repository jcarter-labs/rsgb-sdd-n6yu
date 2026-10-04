# Masterplan Starter — 20 Prompts for Spec-Driven Development

Four sections, five prompts each. Run them in order in Claude Code, one prompt at a time, and read each reply before sending the next. Claude writes the answers into `masterplan.md`, which becomes the source of truth for your app.

## Before you start

- Install Claude Code, and open a terminal (Mac: Terminal; Windows: PowerShell; Linux: your terminal).
- Make an empty folder for your app, and put a screenshot of the app you want in it.
- In that folder, type `claude` to start, then paste: "Create masterplan.md with four sections: Constitution, Spec, Tech, Tasks."
- Fill in the brackets, such as [example app], before pasting.

## 1. Constitution — how we work

1. Build from masterplan.md and my screenshot; borrow language, tools, specs, or open-source code from examples as I choose.
2. Before any code, check my tools, libraries, GitHub login, and this folder's own repo; give me a pass/fail list.
3. After each change, measure our app against the Spec's screen list; show pass/fail.
4. After each working step: run all tests, show me proof, commit, and push to GitHub.
5. When code and masterplan disagree, propose only major changes, one line each; update the masterplan after I approve.

## 2. Spec — what the app does

1. Describe what my app does in a few sentences, using [example app] and my screenshot as guides.
2. From my screenshot, list screen elements and controls; I'll confirm or correct it.
3. For features, describe what the user does and sees, with testable ranges where possible.
4. List where my app's data comes from; when one fails, show me likely causes and fixes.
5. List what my app must do this iteration, and what it won't do.

## 3. Tech — what it's built with

1. Suggest a language and tools for my app; use Python unless my example or spec suggests better. Explain each.
2. I'm building on [Mac/Windows/Linux]; my app must also run on [Mac/Windows/Linux].
3. Keep the app responsive while it works, so it's not stuck waiting on data or input.
4. Split the code into a handful of well-structured modules, each testable on its own.
5. Keep a short list of known limitations, and update it as we go.

## 4. Tasks — in what order

1. Break the build into small ordered steps, starting with setup and ending with a working app.
2. For each step, say how we'll test it and what result means it works.
3. Test connections to outside data with real servers before building screens that depend on them.
4. Get a simple version running early, then add features one at a time, testing each.
5. Mark steps done only after tests pass; at the end, note what we learned in the masterplan.

## After you finish

- Paste: "Save everything into masterplan.md, keeping each section a short outline."
- Read masterplan.md yourself, and fix anything that doesn't match what you want.
- Paste: "Pressure-test masterplan.md for ambiguity; list unclear items with one-line fixes for my approval."
- Paste: "Create a private or public GitHub repo for this folder, as I choose; commit and push masterplan.md and my screenshot."
- You're ready to build. Start a new Claude Code session and paste: "Build from masterplan.md, starting with Task 1."

## Watch for

- **Borrowed code:** note its license in the commit. GPL code makes your whole app GPL.
- **GitHub:** your app's folder needs its own repo. A folder inside another repo commits to the parent.
- **Tests:** never let Claude change a test just to make it pass.
- **"Looks close"** is not a pass. Ask for the measured pass/fail list.
- **Keep the masterplan short:** it's an outline of what you want, not a record of every detail.
