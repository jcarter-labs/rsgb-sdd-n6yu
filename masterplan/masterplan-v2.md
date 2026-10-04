# DX Spotter — Master Plan (v2)

A desktop app for CW operators: it shows live spots from a selectable
telnet DX cluster and from POTA activators on one frequency bandmap.

## Constitution

1. Build only from this masterplan and the accompanying screenshot —
   never from an existing repo, and never from a prior implementation
   of this app on another platform. At the start of the build, name the
   paths that may be read; anything not named is off-limits. Before
   writing UI code, generate the screenshot element inventory
   (position, alignment, justification) and work from it.
   *Prevents: a "clean-room" build quietly copying a finished one.*
2. No live network action against an external service — DX cluster
   telnet, the POTA API, or any third-party endpoint — starts until
   preflight is 100% complete, even if connection details arrive in the
   same message. Work such endpoints one at a time. An unexpected
   failure stops for your decision; a failure that lands on a
   pre-declared fallback is tried without asking, and reports once the
   list is exhausted. This rule governs external service access only.
   *Prevents: hammering someone else's server on unverified details.*
3. Verify → Build → Test → Commit — confirm any server/network command
   works via a live diagnostic before writing UI around it.
   *Prevents: building UI around a protocol assumption never tested.*
4. Every command given must be copy-paste runnable on the actual target
   platform/shell — no unstated tool-install assumptions, no placeholder
   values, and the working directory stated explicitly. Any command
   documented for the operator to run (launch, test, setup) is not
   "runnable" until you have run it yourself, from a clean shell in that
   directory, and shown the output.
   *Prevents: handing over a command that fails when the operator runs it.*
5. One concern per commit: cosmetic, functional, or infrastructure —
   never mixed.
   *Prevents: a commit that can't be reviewed or reverted as one idea.*
6. State what's unverified explicitly, in code and commit messages —
   never present aspirational behavior as working.
   *Prevents: aspiration reaching a README or commit message as fact.*
7. Ask, don't assume — a diagnostic built on a guess only proves the
   guessed scenario, not the one reported. An unverified premise you
   supplied yourself is a guess, however reasonable it looks.
   *Prevents: a diagnostic that validates the wrong scenario.*
7b. Two things are not assuming, and neither needs a question first:
   (a) **Reading a source you can reach.** Exhaust the reachable
   evidence — the manual, the live endpoint, the files C1 permits, the
   session's own history — before putting a question to the operator.
   When you do ask, state what you already checked.
   (b) **Executing a choice the operator already made.** Trying the next
   entry on a pre-declared fallback list is following an instruction,
   not guessing. Report once, when the list is exhausted.
   *Prevents: turns spent telling you to look something up; escalating
   a decision already made.*
8. UI verification is a required artifact, not a described action —
   the first window-rendering task produces `tools/verify_layout.py`,
   measuring rendered geometry against `docs/reference-measurements.json`.
   No layout task is complete without a fresh run, pass/fail table
   pasted as evidence — not a screenshot. Re-run independently on each
   platform, since display scaling (Retina, Windows DPI, Linux desktop
   scaling) differs enough that one platform's pass doesn't guarantee
   another's.
   *Prevents: a layout gap surviving into the next platform's build.*
9. Always build and run through a project-local venv, never a bare
   `python3`/`python`: `python3.13 -m venv .venv` (Windows: `py -3.13
   -m venv .venv`, using the official `py` launcher — never bare
   `python`/`python3`, which on Windows may resolve to non-functional
   Microsoft Store stubs), then always invoke `.venv/bin/python` /
   `.venv\Scripts\python`. Before writing UI code, verify Tk works
   (`python -c "import tkinter; print(tkinter.TkVersion)"`); if it
   fails, install your OS's Tk package first — macOS:
   `brew install python-tk@3.13`; Debian/Ubuntu: `apt install
   python3-tk`; Windows: reinstall Python from python.org (not the
   Microsoft Store), which bundles Tk by default.
   *Prevents: a Microsoft Store Python stub silently breaking the build.*
10. Two consecutive failed fix attempts on the same defect: stop, report
    the measurement, and do not attempt a third. A third attempt on the
    same evidence is guessing, not fixing.
    *Prevents: a third guess dressed up as a third fix.*
11. One build, one session, one project directory — never carry a
    session across projects.
    *Prevents: a session sprawling across projects and carrying the
    accumulated context cost of all of them.*

## Spec

1. Cross-platform desktop app (Windows/macOS/Linux): Python 3.13+,
   `matplotlib>=3.10`, `requests>=2.31`, tkinter.
2. Layout: centered bold title; leader line (90% width ±2%, centered)
   separating the title from column headers; vertical bandmap below —
   RBN left / POTA right, mirrored, each with its own spine, ticks, and
   declutter pass, headers aligned to each lane.
3. Controls panel embedded in the main window (not a popup):
   Band(MHz) / Bandwidth / Window / Spotter-tier / Cluster-server, plus
   Clear (clears displayed spots, forces a cluster reconnect, resends
   filter setup). Status block — connection dot + cluster name, POTA
   poll age, shown-spot counts — lives in this panel, not on the plot.
4. Frame: no boxed border on the scope — left frequency spine + tick
   labels only, transparent plot background.
5. Band scope: static frequency strip (no time axis), center ±
   bandwidth, 1/5/10/30-minute window, alpha-fade aging (floors at
   0.15, never to zero), click-to-copy callsign. The window also sets
   the store's prune horizon — spots older than it are dropped.
6. Band control: numeric MHz entry + Set, not a name dropdown.
7. Cluster filtering: server is user-selectable (profile picker,
   persisted to config) — each profile carries its own filter-command
   dialect, since cluster software families differ. Only one profile
   (NC7J, AR-Cluster) is wired; the picker and persistence are deferred
   by decision. Each cluster profile may declare an ordered list of
   hosts; on connection failure the next is tried automatically, and
   only an exhausted list reports to the operator. CW-only: server-side
   filter where a profile marks it trustworthy, client-side check as
   the authoritative fallback otherwise. Dedup: suppress the same
   call+band within 2 minutes (cluster spots only). Spotter tier: radio
   group (Local = vetted core, Regional = larger superset), matched
   client-side before dedup. Bandwidth options: 10/20/40/50/80/100 kHz.
   Operator callsign, spotter lists, the filtered band set, and the
   host list are configuration inputs, not source constants.
8. POTA lane: public API, no auth, CW-only, own thread/queue,
   60-second poll, same tick/declutter/leader-line rendering as RBN
   (mirrored), no dedup.
9. Settings persist to `~/.config/<app>/config.json` on every platform
   — deliberately uniform, not OS-idiomatic. Settings are written on
   change, not only on clean exit.
10. Out of scope: simultaneous multi-cluster connections, ADIF/contest/
    log upload, a database, audio alerts, awards tracking, POTA/RBN
    correlation, CAT control.

## Tech

1. Concurrency: Tk main loop + one daemon worker thread per feed
   (cluster, POTA), each with its own queue, drained by the main
   loop's ~200ms poll. Only cluster spots pass through the dedup cache.
2. Spot store: keyed by (call, band, feed) so cluster and POTA spots
   never evict each other; two independent render lanes, each clipped
   to the visible frequency window.
3. Modules: main (UI/poll loop) · cluster (telnet, parser, spot model)
   · cluster profiles (per-server filter dialects) · POTA client (API
   worker) · bandmap (scope widget) · controls (panel + status) ·
   filters (dedup) · spot store · config · scope utils.
4. Filter-setup commands must dispatch off the UI thread — sending
   several commands inline blocks for seconds and reads as a hang.
5. Known limitations to track: POTA poll age reports the last attempt,
   not the last success — a failing feed still shows a healthy age, and
   request errors are swallowed silently; the UI wiring itself has no
   automated test (manual smoke-test only); reconnect backoff timing is
   unasserted.

## Tasks

Work through these in order without per-task approval. Stop only for:
a live action against a third-party service, the first push or a repo
visibility change, a genuine ambiguity in this document, or a failed
verification. This governs sequencing within an approved task list;
step-by-step confirmation still applies to environment work,
remediation, and anything not listed here.

0. Environment — venv, Tk, git identity, `gh` auth, repo name and
   visibility, all resolved and verified with real output before the
   first commit.
1. Cluster connection & parser — connect via telnet, parse spots,
   verify live against a real server with a diagnostic script before
   building UI around it.
2. Filter engine & config — per-profile server-side filtering plus
   client-side dedup and mode-check fallback.
3. Embedded-controls UI — band scope with controls built into the main
   window, wired to live filter dispatch with no blocking. This is the
   first task that produces a runnable app: include the verified run
   command in the README as part of this task.
4. POTA integration — independent polling thread, own render lane,
   tests for spot parsing.
5. UI polish pass — title, leader line, lane headers, mirrored POTA
   spine/ticks, status block in the controls panel; verify per-element
   and per-platform with `tools/verify_layout.py` (Constitution 8).
6. End-of-build addendum — before the final commit, review this
   session's human turns, identify each correction and environment fix,
   and propose the rule that would have prevented it as a diff to this
   document. Append any platform deltas discovered.
