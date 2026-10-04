# Constitution

RULE: Build from masterplan.md, idea.md and my screenshot; borrow language, tools, specs, or open-source code from examples as I choose.
RULE: At the start of the build, check tools, libraries, GitHub login, and this folder's repo on my platforms; show pass/fail.
RULE: After each change, measure the app against the Spec's screen list; show pass/fail.
RULE: After each working step: run all tests, show me proof, commit, and push to GitHub.
RULE: When code and masterplan disagree, propose only major changes, one line each; update the masterplan after I approve.
RULE: Measure UI layout with pixels against reference measurements; never claim "matches" from a visual impression.
RULE: Keep the app responsive while it works, never stuck waiting on data or input.
RULE: Keep a short list of known limitations in the masterplan; update it as we go.
RULE: Run each stage without stopping; stop for my review only at stage end, on a failed test, or when you need my decision.
RULE: Test connections to outside data with real servers before building screens that depend on them. Live network checks need unsandboxed network access for the agent: ask for it at the start of Stage 2.
RULE: Get a simple version running early, then add features one at a time, testing each.

# Spec

## Summary
DX Spotter ("RBN & POTA Spotter"): a macOS graphical bandmap for a CW/DX operator, modelled on the N1MM bandmap (the example app).
- RBN CW spots from the NC7J AR-Cluster (telnet nc7j.com:7373, login N6YU), limited to the Local or Regional skimmers, are drawn on a vertical linear frequency scale, each call sign on a leader line to its frequency.
- POTA.app spots (polled every minute) are on a second scale at the right. RBN is blue, POTA green (the reference screenshot draws POTA dark blue; the Spec's green is followed).
- Spots fade over a 5, 10 or 15 min fade time. Clicking a call sign copies it to the clipboard.
- A side panel holds the controls and status. The app window is resizable.

## Scope of this iteration
All seven `idea.md` features are in, including both data sources (A and B). Nothing is deferred.

## Features
Numbered as in `idea.md`. Defaults: frequency 14.045 MHz, bandwidth 50 kHz, fade time 10 min, spotter Regional (as in the screenshot), server NC7J.

Terms: **fade time** = the "Window (min)" setting (that is only its on-screen label); **span** = the displayed frequency range, centre ± bandwidth/2; **app window** = the OS window. **Age** runs from the time the app received the spot. The **current band** is the HF amateur band containing the centre frequency (Tech table).

1. **Bandmap of RBN spots**: vertical linear scale, higher frequency at the top, spanning centre ± bandwidth/2 (default 14.020 to 14.070 MHz). Each CW spot is a blue call sign (call only) on a leader line to its frequency. The app adds no deduplication beyond one label per call per scale: a new spot of the same call replaces the earlier one (new frequency, age reset); the cluster's own deduplication is otherwise relied on.
   - Test: a spot inside the span is drawn at a position linear in its frequency; a spot outside the span, a non-CW spot, or a spot from a skimmer not in the selected list is not drawn; two spots of one call give one label, at the newer frequency.
2. **Local / Regional switching** (radio buttons). Local: W6YX, AK6RI-1, N6TV. Regional: K6FOD, WA7LNW, ND7K, K7CO, NG7M, N7VVX, N7TUG, KD7EFG, KW7MM, KW7MM-2, plus the Local skimmers (Regional is a superset of Local).
   - Test: exactly one radio is selected; switching shows only the matching list's spots; "Shown: RBN n" matches the spots on screen.
3. **Centre frequency and bandwidth**: type MHz and press Set; pick a bandwidth from the menu. The scale re-centres and spans ± bandwidth/2. A centre frequency in a different HF amateur band changes the server filter to that band and flushes old-band spots; one outside any HF amateur band shows a warning and keeps the last filter. Changing frequency or bandwidth within a band flushes nothing.
   - Test: frequency accepted from 1.8 to 30 MHz inclusive; an out-of-range or non-numeric entry is rejected and the current frequency kept; bandwidth menu is exactly 10, 20, 40, 50, 80, 100 kHz; span = bandwidth (50 kHz at 14.045 shows 14.020 to 14.070).
4. **Click a call sign to copy it** (either scale). No feedback is specified.
   - Test: the clipboard holds exactly that call sign as spotted, including any suffix such as /P (no frequency, no extra text).
5. **Spot fading**: Window (min) menu sets the fade time. A spot is solid when new, grows more transparent with age, is at 15% opacity just before the fade time, and is dropped at age ≥ fade time. Changing the setting applies to all existing spots at once.
   - Test: menu is exactly 5, 10, 15 min; opaque at age 0; transparency rises with age; 15% just before the fade time; dropped at age = fade time (10 min at the default, 15 at 15); "Shown" counts drop when a spot goes. Clear empties both scales at once; new spots continue to arrive. Switching Local/Regional redraws from the store without emptying it.
6. **POTA spots, right-hand scale**: ticks only, green call signs (call only) on leader lines, from the POTA.app API. Same span and fade time as RBN. The list of POTA spots is also deduplicated to one label per call.
   - Test: polled every 60 s; "POTA: last poll Ns ago" counts up and resets after each successful poll, and reads "POTA: not polled yet" until the first one; "Shown: ... POTA n" matches the POTA spots on screen.
7. **Resizable app window** (drag the edges); the layout follows.
   - Test: the control panel and status lines stay fully visible; the scales stretch to the new canvas height.

### Decisions (beyond idea.md)
1. Status dot: green connected, amber connecting, red disconnected. Auto-reconnect with backoff 5, 10, 30 s, then every 60 s; show retry count: the number of reconnect attempts since the last successful connect, reset on success; the status line reads "Cluster: NC7J (retry n)" while n > 0. The dot covers the cluster only; POTA shows its poll age, and a POTA failure does not change the dot.
2. Fade: linear from full opacity to 15% over the selected fade time (5, 10 or 15 min, default 10); never fully invisible; 15% just before the fade time, then drop the spot at age ≥ fade time.
3. Minimum app window size: 400 x 700 px; layout scales above that; the screenshot (492 x 1189) is the reference.
4. Overlapping calls: at least one text height between labels; push crowded labels apart with a thin leader line to the true frequency. Labels are clamped inside the canvas; beyond that, overlap is allowed (see Known limitations).
5. POTA: CW only; drop spots with no frequency. The store keeps every CW POTA spot with a frequency, and only spots inside the span are drawn (span filter at draw time, so a frequency change needs no new poll). Each poll re-lists current reports, so a report seen again (same POTA `spotId`) keeps its original age; a new report from the same call replaces the old one with age reset.
6. Store: RBN spots keep the same rule: the store holds current-band CW spots from every listed skimmer (the Regional list, which includes the Local skimmers), and the span filter and the Local/Regional choice both apply only when drawing (Local draws only the Local skimmers), so changing frequency within a band or switching Local/Regional loses nothing and redraws at once.
7. Clear: empties both scales, forces a cluster reconnect (shown as amber, not counted as a retry), and resends the current band filter. Server menu: only NC7J, does nothing else this iteration.
8. Late old-band spots: an RBN spot from a band other than the one the server filter asks for is dropped on arrival, so stragglers around a band change never reappear.

Side panel status lines: green dot and "Cluster: NC7J" (plus " (retry n)" while retrying); "POTA: last poll Ns ago" ("POTA: not polled yet" before the first successful poll); "Shown: RBN n · POTA n", counting the spots currently drawn.

## Data sources and how we'll check each one
Two sources feed the app; everything else comes from the operator's controls. Parser and filter checks run offline on saved captures; the live connect and poll checks run separately, with pass/fail shown.

### Source A: NC7J AR-Cluster (RBN spots)
- Telnet `nc7j.com` port 7373, login N6YU. Feeds the left scale: CW only, call only, from the selected skimmer list.
- Line format (confirmed from the live capture): `DX de <skimmer>: <freq kHz> <call> CW ...`. Human (non-skimmer) spots have no mode field, e.g. `DX de KF6IWW:  14253.0  N7MES   0015Z`; the parser gives them a blank mode, so they are not CW and are dropped.
- Skimmer match: the line's skimmer equals a list entry, optionally followed by `-<digits>`, then optionally `-#` (live skimmers end in `-#` or `-<n>-#`). AK6RI-1 matches AK6RI-1-# and AK6RI-1-2, not AK6RI-10 or AK6RI. A bare entry matches itself: W6YX matches W6YX, W6YX-#, W6YX-2 and W6YX-2-#. The Regional list stays as written, including KW7MM-2, with the Local skimmers added when Regional is selected.
- CW check: the client-side check is authoritative; server-side mode filtering is not trusted.
- Checks:
  1. Connect: login succeeds within 10 s, meaning the server's post-login prompt (text recorded in step 2.1) is seen, and the dot goes green. Save a raw capture in this folder, before any filtering, of 50 spot lines or 5 minutes, whichever comes first.
  1a. Band filter: after login, the server-side band filter command `set dx filter Band=<n>` is sent and acknowledged by the reply `DX filter set to: Band = <n>` (matched case-insensitively; see Tech). The filter asks for the band containing the current frequency (20 m at the default). After every reconnect the filter for the current band is sent again.
  1b. Band change: on a frequency in a different HF amateur band (Tech table), the `cluster_client` worker thread sends the new band filter, which replaces the old one (each `set dx filter` replaces the whole filter), and the old-band spots are flushed. A frequency outside any HF amateur band shows a warning and keeps the last filter. Tested live by changing bands: the new band's spots arrive and the old band's are gone.
  1c. Clear: the Clear button empties both scales, forces a reconnect (amber, not counted as a retry) and resends the current band filter; the new filter is acknowledged.
  2. Parse: every captured line gives frequency (kHz to MHz), call, mode and skimmer, or an explicit reject. Accepted plus rejected equals lines read.
  3. Filter: only CW lines from the selected list are shown, per the skimmer match and CW check; Local/Regional switching changes the set. The capture must include a matching suffix, a non-matching suffix and a non-CW line; if the 5-minute capture has none, add hand-made lines marked as such.
  4. Range: spots outside the span are kept in the store but not drawn; spots inside are placed linearly.
  5. Failure: dropping the connection turns the dot red, then amber while retrying at 5, 10, 30 s, then every 60 s, with the retry count (attempts since the last successful connect, reset on success); on reconnect it returns to green. Tested by killing the socket and by blocking the network.
  6. Bad data: a malformed or truncated line is skipped, logged, and never crashes the app.

### Source B: POTA.app API (POTA spots)
- The POTA.app spots API; endpoint chosen in Tech (not in `idea.md`). Feeds the right scale: CW only, call only, polled every 60 s.
- Checks:
  1. Poll: a live request succeeds and returns spots. Save one raw response in this folder.
  2. Parse: each spot gives frequency, call and mode, or an explicit reject. Accepted plus rejected equals spots returned.
  3. Filter: non-CW spots and spots with no frequency are dropped; spots outside the span are kept but not drawn (decision 5).
  4. Timing: requests are 60 s apart, within 2 s; "last poll Ns ago" counts up and resets after each poll.
  5. Failure: a timeout, HTTP error or bad JSON keeps the existing POTA spots, does not crash the app, and the next poll after 60 s retries. The poll age keeps counting from the last success.
  6. Counts: "Shown: POTA n" equals the POTA spots on screen.

## Screen list
Source: `screenshot.png` (492 x 1189 px, Linux window; macOS native chrome replaces the title bar). Positions are x, y in screenshot pixels, read by eye, not measured, and approximate.

Check rule: layout checks use the step 1.3 measurements, not the approximate numbers below. An element passes when its measured position is within ±4 px of the measurement. Checks run on the content area at the reference width (492 px) and the screenshot's height minus its title bar (measured in 1.3); the title bar (element 1) is excluded and y values are taken from the top of the content area. Colours stay light whatever the macOS appearance: white canvas, light grey panel. macOS captures are colour-managed (panel grey 217 reads as 212), so layout checks compare positions only, never colours; the right edge of the Shown line (19) is not compared, since its width depends on the counts.

App window
1. Title bar "DX Spotter", centred; window buttons top right (y ~20). Replaced by macOS chrome.
2. Heading "RBN & POTA Spotter", bold, large, centred, full width (y ~68).
3. Horizontal rule under the heading, full width (y ~93).

Left area: bandmap canvas, white background, x 0 to ~298, y ~127 to the bottom
4. Column label "RBN", bold, above the left scale (x ~72, y ~115).
5. Column label "POTA", bold, above the right scale (x ~222, y ~115).
6. RBN scale: vertical line at x ~105; higher frequency at the top. Tick labels to its left at 14.070 (top, y ~149), 14.060 (y ~352), 14.050 (y ~555), 14.040 (y ~760), 14.030 (y ~963), 14.020 (bottom, y ~1168), with small ticks. Tick spacing is bandwidth/5 (five intervals per span: 10 kHz at 50 kHz bandwidth), labels to 3 decimals.
7. RBN spots: call signs right of the line, left-aligned at x ~113, each joined to its frequency by a short leader line; spread apart vertically where frequencies are close; older spots paler.
8. POTA scale: vertical line at x ~284, ticks only, no labels.
9. POTA spots: call signs left of the line, right-aligned (ending x ~273), each on a leader line to its frequency; same fading.

Right area: control panel, light grey, x ~298 to 492, left-aligned at x ~312
10. "Frequency (MHz)" label (y ~123).
11. Frequency text box (x 312 to ~388, y ~148) showing 14.045, "Set" button beside it (x ~397 to 477).
12. "Bandwidth (kHz)" label (y ~184); dropdown below showing 50 (x 312 to ~376, y ~208).
13. "Window (min)" label (y ~245); dropdown below showing 10 (x 312 to ~376, y ~269).
14. "Spotter" label (y ~305); radio buttons stacked below: "Local" (y ~326, unselected), "Regional" (y ~349, selected).
15. "Server" label (y ~380); dropdown below showing "NC7J (AR-Cluster)" (x 312 to ~466, y ~402).
16. "Clear" button, full panel width (x 312 to ~477, y ~443).
17. Green dot and "Cluster: NC7J" (y ~485).
18. "POTA: last poll 57s ago" (y ~507).
19. "Shown: RBN 43 · POTA 26" (y ~527).

# Tech

## Language and tools (chosen by the operator)
| Area | Choice | Why |
|---|---|---|
| Platform | macOS only | Confirmed by the operator; "my platforms" in the Constitution means macOS. |
| Language | Python 3.13 or later (python.org or Homebrew, never `/usr/bin/python3`) with Tk 8.6 or 9.x, venv at `./.venv` | The system Python's Tk is too old. |
| GUI | Tkinter (ttk widgets, Canvas for the bandmap) | The screenshot looks like a Tk app; ships with Python; Canvas suits scales, leader lines and click-to-copy. Fading blends the text colour toward the white background, since Tk has no text transparency. Light colours are forced whatever the macOS appearance. Fonts matched to the reference text widths: Lucida Grande 10 for labels, Arial 10 for status text and call signs, Arial 9 bold for tick labels, Lucida Grande 16 bold for the heading. |
| Cluster link | Standard-library `socket` in a worker thread, spots passed to the GUI through a queue | No extra package; fits Tk's event loop. `telnetlib` is not used (removed in Python 3.13). |
| POTA HTTP | `requests`, polled every 60 s in a worker thread | Simple timeouts and error handling. |
| Screenshot measuring | Pillow | Reads `screenshot.png` pixels (step 1.3) and for layout checks. |
| Tests | pytest | Offline parser and filter tests on saved captures. |

Window testing: Tk only paints inside `mainloop()`, and calling `lift()` before it gives blank captures; capture with `screencapture -R` from the window's Tk geometry (Screen Recording allowed for the terminal, terminal restarted). Do not run UI tests while a capture is running, since a test window can cover the app.

## Modules
Each module has one job and is testable on its own. Only `ui` imports Tk.

Rules between modules:
- `layout` is pure: numbers in, numbers out, no Tk.
- The network clients never call the parsers; they put raw lines and raw records on a queue. That queue is the only link between network and GUI; nothing else is shared between threads.
- On a failure (connection lost, timeout, HTTP error, bad data) a client puts a status item on the queue, never spots. Status items carry the dot state and retry count; a POTA failure status does not reset the poll age.
- `ui` has one loop: a Tk `after()` tick that calls `app.drain()` then redraws. No other loop or polling in the GUI.

1. `cluster_parse`: one raw cluster line to a spot (frequency, call, mode, skimmer) or an explicit reject. Tested on the saved cluster capture.
2. `pota_parse`: one raw POTA record to a spot (frequency, call, mode) or an explicit reject. Tested on the saved POTA response.
3. `spot_filter`: decides if a spot is kept and drawn (skimmer match, client-side CW check, frequency inside the span and the selected Local/Regional list at draw time, POTA drops). Tested with the match and CW cases from Data sources.
4. `spot_store`: holds spots with age, gives opacity (linear to 15%), drops spots at age ≥ fade time (age from receipt), keeps one spot per call per scale (a repeated POTA report keeps its age), counts per source, clears. Tested with a fake clock.
5. `settings`: holds and validates frequency (1.8 to 30 MHz), bandwidth (10, 20, 40, 50, 80, 100), fade time (5, 10, 15) and Local/Regional; a bad entry is rejected and the old value kept. Tested with valid and invalid inputs.
6. `layout`: frequency to vertical position, and spreading crowded labels (at least one text height) while keeping each leader line's true frequency. Tested with numbers only.
7. `cluster_client`: socket worker thread that logs in, sends the band filter, puts raw lines on the queue, reconnects with backoff, and reports state and retry count as status items. Tested against a fake local server.
8. `pota_client`: worker thread that polls every 60 s and puts raw records on the queue; on failure it puts a status item and no spots, so old spots stay and the poll age keeps growing from the last success. Tested with a faked HTTP layer.
9. `app` (approved): `app.drain()` empties the queue, calls the parsers, filter and store, applies status items (dot, retry count, poll age), and gives `ui` what to draw. No Tk, no sockets. Tested by feeding it queued items and checking store and status.
10. `ui`: Tkinter window, canvas and side panel; draws and passes user input on, never waits on data. Tested by measuring its screenshot against the saved measurements.

Also in `spotter/` (not in the numbered list): `models` (the shared `Spot`, `Reject`, `RawLine`, `RawRecords` and `Status` types), `main` (launch: `python -m spotter`) and `bare_window` (the Stage 2 two-list window, superseded by `ui`).

Tools in `tools/`, separate from the app: `measure_screenshot.py` (step 1.3 measurements), `capture_window.py` and `snap_app.py` (window capture), `verify_layout.py` (±4 px layout check), `probe_cluster.py` (live cluster capture), and the live checks `live_check_cluster.py`, `live_check_app.py` and `live_snap.py`.

## HF amateur bands (for the band filter)
Standard US amateur bands, edges inclusive, in MHz. A frequency in a gap or outside the table is "outside any HF amateur band". 60 m is not listed, so it counts as outside.

| Band | Low | High |
|---|---|---|
| 160 m | 1.800 | 2.000 |
| 80 m | 3.500 | 4.000 |
| 40 m | 7.000 | 7.300 |
| 30 m | 10.100 | 10.150 |
| 20 m | 14.000 | 14.350 |
| 17 m | 18.068 | 18.168 |
| 15 m | 21.000 | 21.450 |
| 12 m | 24.890 | 24.990 |
| 10 m | 28.000 | 29.700 |

Edges are the US allocations (FCC Part 97), confirmed by the operator against a published table (2026-09-30); the code table matches it exactly. The app uses the US edges; IARU Region 1 differs on 160 m (1.810 to 2.000), 80 m (to 3.800) and 40 m (to 7.200) and is not used.

## Known limitations
1. When more spots are crowded together than fit on the canvas, labels are clamped inside it and may overlap.
2. At the minimum window width (400 px) the canvas is 207 px wide, so an RBN label and a POTA label at nearly the same frequency can touch.
3. Live 20 m RBN traffic from the listed skimmers is light (about one spot a minute), so full-age fading and Local/Regional switching with many spots are verified by offline fake-clock and canned-capture tests, and live only on a few spots.
4. "Window stays draggable" is checked by replaying 50 spots/s while resizing the window from code (worst tick lateness 10 ms), not by a real mouse drag.
5. macOS screen captures are colour-managed (panel grey 217 reads as 212), so the layout check compares positions, never colours. The Shown line's right edge is not compared, since its width depends on the counts.

## Open until a live session
Each item stays open until taken from a saved live capture, never from memory; name the capture file next to the item when closed.

| Open item | Closed by |
|---|---|
| POTA.app endpoint and JSON fields | **Closed** by `tests/captures/pota_spots_raw.json` (+ `pota_headers.txt`), 2026-09-30: `GET https://api.pota.app/spot/activator` returns a JSON list (59 spots). Call = `activator`; `frequency` = string in kHz (e.g. "14075.63"); `mode` = string, "CW" for CW (some are ""); also `reference`, `spotTime`, `spotter`, `source`. |
| Server-side band filter command and its acknowledgement | **Closed 2026-09-30 from the operator's manual `nc` session (not a saved file; `tests/captures/cluster_session.txt` to replace it).** Command `set dx filter Band=40`; ack `DX filter set to: Band = 40` (match case-insensitively); then only 7000-7300 kHz spots arrive. `Band=20` works the same. Filters persist per callsign, and skimmer spots are OFF by default for a new call, so the client sends its filter commands on every login and checks for the ack. No skimmer-on command is needed for N6YU (operator-confirmed): with only the Band filter, `-#` spots stream. Each `set dx filter` replaces the whole filter, so any combination must be one command. |
| Login prompt text | **Closed 2026-09-30 (manual `nc` session; also in `tests/captures/cluster_session.txt`).** `login: ` with no newline. Post-login prompt: `N6YU de NC7J <dd-Mon> <hhmm>Z arc6>`. |
| Real spot-line format | **Closed 2026-09-30 (one line, manual `nc` session, not a saved file).** `DX de WA7LNW-#:  14020.0  XR4T  CW 13 dB 28 WPM CQ  0007Z`: freq in kHz; skimmers end in `-#` or `-<n>-#`. Raw capture saved: `tests/captures/cluster_session.txt` (51 spot lines in 86 s, 20 m). Human (non-skimmer) spots have no mode field, e.g. `DX de KF6IWW:  14253.0  N7MES   0015Z`; the parser gives them a blank mode. |

# Tasks
Every sub-step follows the Constitution: after each working step, run all tests, show proof, commit and push; after each change to the app, measure it against the Spec's screen list. A stage is not done until its "done when" line is shown as pass.

## Stage 1: Environment
- 1.1 Start-of-build check: Python 3.13+ (python.org or Homebrew, never `/usr/bin/python3`) with Tk 8.6 or 9.x (report the exact fix if not), venv, pip, git identity, GitHub login and SSH (`ssh -T git@github.com`), and this folder's repo; show pass/fail for each. (Repo root and `origin` jcarter-labs/RSGB-3 are already set up and pushed.)
- 1.2 Create `./.venv`, install `requests`, `Pillow` and `pytest`, write the environment steps to `docs/setup.md`, add `.gitignore`; `pytest` runs with one trivial test.
- 1.3 Measure `screenshot.png` with a script and save the measurements to a file in this folder. All layout checks against the Spec's screen list use these measurements, not the approximate positions in the Spec.

Done when: every check in 1.1 passes, `pytest` runs inside the venv, and the measurements file gives a measured position and size for each of the 19 screen-list elements (the title bar height is measured too, to set the content-area reference).

## Stage 2: Data connections
- 2.1 Save a live NC7J session: login prompt text, band filter command and its acknowledgement, and a raw capture of 50 lines or 5 minutes.
- 2.2 Save one live POTA.app response. Record both captures' findings in Tech's "Open until a live session" table, with the capture files named.
- 2.3 `cluster_parse` and `pota_parse`, tested on the saved captures.
- 2.4 `cluster_client` (login, band filter, raw lines and status items on the queue, reconnect at 5, 10, 30 s then every 60 s).
- 2.5 `pota_client` (60 s poll, raw records on the queue, a status item on failure with old spots kept).
- 2.6 Test both clients against the live servers, including a forced disconnect and reconnect, a blocked network, and a POTA failure.
- 2.7 A bare window showing live RBN and POTA spots as two plain text lists (call, freq, age), fed through the queue. No bandmap, layout or styling, and no client-side filtering; each list keeps only its last 50 entries. The server-side band filter stays on, requesting only 20 m (the band containing the default frequency). Depends on 2.1 confirming the filter command; if it cannot, 2.7 drops off-band spots client-side and logs "server filter unconfirmed" until fixed. The window's `after()` tick uses a small temporary drain, which `app` replaces in 3.5. (Done in Stage 2 as `spotter/bare_window.py`; superseded by the real window in Stage 4.)

Done when: both captures are saved and the Tech table is closed, each parser's accepted plus rejected equals the items read, both clients pass the live checks including reconnect with the retry count, and the bare window shows live spots in both lists within 60 s of starting.

## Stage 3: Core logic (offline tests on the captures)
- 3.1 `spot_filter` (skimmer match, client-side CW check, frequency range, POTA drops).
- 3.2 `settings` (frequency, bandwidth, fade time, Local/Regional; bad entry rejected, old value kept).
- 3.3 `spot_store` (age from receipt, linear opacity to 15%, drop at age ≥ fade time, one spot per call per scale, counts, Clear), on a fake clock.
- 3.4 `layout` (frequency to position, label spreading of at least one text height, no Tk import).
- 3.5 `app` (`app.drain()` calls the parsers, filter and store and applies status items).

Done when: all offline tests pass with no network and no window, including the matching, non-matching and non-CW cases, and a crowded-labels case for `layout`; any shortfall is added to the known limitations list.

## Stage 4: Features
Stage 4 guards, done before 4.1:
- G1 Window capture: capture the app by region from Tk geometry (`winfo_rootx/rooty/width/height`) with `screencapture -R`, scaled for Retina 2x; prove it with one capture before any layout step.
- G2 Layout checker: `tools/verify_layout.py` compares a capture to the step 1.3 measurements (content area, ±4 px) and prints a pass/fail table; every layout step ends with its output pasted.
- G3 Label spreading: test the pure layout function first with synthetic crowds (20 spots within 2 kHz; 5 spots at the same frequency; labels at the top and bottom edges) before drawing anything. Two failed fixes means stop and report what was measured.
- G4 Responsiveness: replay a capture at 50 spots/s; the `after()` tick must stay under 300 ms late, and the window must stay draggable.
- G5 Threads: a test fails if any worker thread calls Tk; closing the window exits within 2 s and closes the socket.
- G6 Clipboard: click-to-copy is checked with `pbpaste`, and still works after the app quits.
- G7 Clicks hit the drawn label position (after spreading), not the spot's frequency.

- 4.1 Controls wired to `settings` (Set, Bandwidth, Window (min), Spotter, Server, Clear; Clear also forces a cluster reconnect and resends the band filter), driven by the single `after()` tick that calls `app.drain()` then redraws.
- 4.2 Live RBN spots (left scale): blue call signs, leader lines, cluster status dot and retry count.
- 4.3 Live POTA spots (right scale): green call signs, ticks only, "last poll Ns ago".
- 4.4 Fading: to 15% over the fade time, dropped at age ≥ fade time.
- 4.5 Local/Regional switching.
- 4.6 Click a call sign to copy it.

Done when: against live data, each feature behaves as in Spec Features (frequency, bandwidth and fade time limits, fade values, counts matching what is on screen, exactly the clicked call sign on the clipboard) and the window stays responsive.

## Stage 5: UI
- 5.1 Layout compared with the stage 1 measurements (±4 px, per the Screen list check rule), pass/fail per screen-list element.
- 5.2 Resize: minimum app window size 400 x 700, layout scales above it.
- 5.3 Full screen-list check, both source checks live, failure tests, responsiveness check; update the known limitations list.
- 5.4 One documented launch command, `docs/setup.md` complete, final test run, commit and push.
- 5.5 Final step: review what went wrong during the build (failed tests, rework, surprises, known limitations) and propose masterplan updates, one line each, for the operator's approval. Nothing in the masterplan changes until approved.

Done when: every screen-list element passes by measurement, every check above passes or is listed as a known limitation, the app starts from a fresh clone using only `docs/setup.md`, and the 5.5 review and its proposed updates are shown for approval.
