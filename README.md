# The Spec Is the New Schematic: Reproducible Station Software with Spec-Driven Development

RSGB Convention 2026 (9–11 October) · John Carter, N6YU

Spec-Driven Development (SDD) means you write down what a piece of software must do, in plain language with testable numbers, and have an AI coding assistant build it from that document. The spec plays the role the schematic plays in a hardware project: when the build is wrong, you fix the spec, not the output. This repository holds the non-code material from the talk: the prompt files you give Claude Code, a worked example masterplan, a novice-mode test run, and a handout on applying the approach to existing open-source and published projects.

## What's here

| Path | What it is |
|---|---|
| `masterplan/masterplan-generator.md` | Give this to Claude Code. It interviews you and writes a masterplan for your own app. |
| `masterplan/masterplan-starter.md` | 20 prompts, in order, for building a masterplan step by step |
| `masterplan/masterplan-v2.md` | A worked example: the DX Spotter masterplan |
| `examples/bandmap-RSGB-3/` | A novice-mode test run of the generator: `idea.md`, the resulting `masterplan.md`, and a screenshot of the app |
| `handout/Extending_the_SDD_Approach_Beyond_Spotter.pdf` | A4 handout: building, porting and recreating open-source and published projects with SDD |

References are in `references.md`.

## Note on the example
Example copied from a private build repo; references to files and repos outside this tree are not included.

## License
TODO: license
