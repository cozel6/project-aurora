# CLAUDE.md — Project Aurora

> ## ⚠️ DISCLAIMER
>
> **For educational use only.** This is a bachelor's thesis project. Everything related to security
> testing (recon, attacks, spoofing, etc.) runs **strictly locally, in an isolated lab**, on the
> author's own equipment (the lab Raspberry Pi), with no internet access and no real targets. It is
> **not** meant for, and **must not** be used against, any system, network, or person without
> authorization. That's it.
>
> **On AI and code authorship.** Some files in this project were or will be produced with the help of
> AI (documentation, structure, ideas, guidance). Even so, **all code is and must remain hand-written**
> by the author — sometimes under the AI assistant's guidance, but never generated and pasted in "as a
> package". The AI acts as a mentor/consultant, not as the author of the code.

Bachelor's thesis project, educational purpose, isolated lab.

## Core rules

- **Topology:** 3 machines from the same repo. **PC** and **Mac** = development + attacker + ML
  training; **Raspberry Pi 4 (2 GB)** = victim server + sensor + inference + response.
- **ML:** training only on PC/Mac; inference only on the Pi. **No TensorFlow/PyTorch on the Pi.**
- **Git:** do not commit or push unless I explicitly ask.
- **Attack:** attack code only against the lab Pi in the isolated lab (IP from `config/lab.yaml`).

## How to work with the code

Golden rule: **explain, guide, propose structures and pseudocode, review what I write.**
Don't hand me finished code files "as a package" unless I explicitly ask; I write the code by hand.

On top of that, apply the Karpathy guidelines (`andrej-karpathy-skills` plugin):

1. **Think before coding.** Don't assume, don't hide confusion. State your assumptions explicitly; if
   there are multiple interpretations or a simpler option, raise them — don't choose silently.
2. **Simplicity first.** The minimum that solves the problem. No unrequested features, no abstractions
   for single-use code, no speculative "flexibility".
3. **Surgical changes.** Touch only what you must. Don't "improve" adjacent code/comments/formatting
   and don't refactor what isn't broken. Keep the existing style. Dead code unrelated to the task →
   flag it, don't delete it.
4. **Goal-driven execution.** Turn tasks into verifiable criteria (e.g. "add validation" → "write
   tests for invalid input, then make them pass"). For multi-step tasks, give a short plan with a
   verification per step.
