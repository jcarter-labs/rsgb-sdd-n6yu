# App Brief: RBN & POTA Spotter

## 1. Purpose
A graphical bandmap, like the N1MM bandmap, for a CW/DX operator (N6YU).
- Shows locally received DE spots from anywhere (DX) from an RBN AR-Cluster, on a linear frequency scale.
- Each spot is a call sign with a leader line to its frequency.
- Relies on the cluster's own deduplication.
- Also shows POTA.app spots on a second, right-hand frequency scale, from the POTA.app API.
- Reference look: `screenshot.png` (window title "DX Spotter", heading "RBN & POTA Spotter").

## 2. Platform
- Build on macOS.
- Run on macOS.
- No other platforms required.
- The screenshot was taken on Linux. Match its layout, but use the native macOS look, not the Linux window chrome.

## 3. Features (most important first)
1. Linear-frequency bandmap of RBN spots, with call signs on leader lines.
2. Local/Regional spotter toggle (radio buttons).
3. Center frequency and bandwidth controls.
4. Click a call sign to copy it to the clipboard, for pasting into a logger or QRZ.com lookup.
5. Spot fading over time.
6. POTA spots on the right-hand scale.
7. Resizable window.

## 4. Inputs and settings
| Control | Values |
|---|---|
| Frequency (MHz) | Text box plus Set button. Default 14.045. Range 1.8 to 30 MHz (HF only). An out-of-range entry is rejected and the current frequency is kept. |
| Bandwidth (kHz) | Menu: 10, 20, 40, 50, 80, 100. Default 50. |
| Window (min) | Menu: 5, 10, 15. Fade time. Default 10. |
| Spotter | Radio buttons: Local, Regional. |
| Server | Menu, NC7J (AR-Cluster) selected. |
| Clear | Button, clears displayed spots. |

Cluster connection:
- `telnet nc7j.com 7373`
- Login callsign: N6YU

Spotter lists (filter which RBN skimmers' spots are shown):
- Local: W6YX, AK6RI-1, N6TV
- Regional: K6FOD, WA7LNW, ND7K, K7CO, NG7M, N7VVX, N7TUG, KD7EFG, KW7MM, KW7MM-2

## 5. Display and data sources
- Left scale, "RBN": spots from NC7J, CW only, call sign only, blue.
- Right scale, "POTA": spots from the POTA.app API, polled every 1 minute, call sign only, green.
- Frequency scale: linear, vertical. The left (RBN) scale has tick labels; the right (POTA) scale has ticks only, no labels, as in the screenshot. The window is center frequency +/- bandwidth/2.
- Fading: spot transparency decreases with age. A spot goes from solid to gone over the Window (min) setting, then disappears. At the default of 10, spots vanish at 10 minutes; at 15, at 15 minutes.
- Clicking a call sign copies it to the clipboard.
- Side panel, as in the screenshot:
  - Status dot and "Cluster: NC7J" (green = connected).
  - "POTA: last poll Ns ago".
  - "Shown: RBN n · POTA n" counts.
- Window is resizable.
- Colors: the screenshot shows spots in dark navy; these are overridden to blue (RBN) and green (POTA).
