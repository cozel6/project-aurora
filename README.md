# Project Aurora

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

🇷🇴 *Versiunea în română: [README.ro.md](README.ro.md)*

## Description

This project is the bachelor's thesis for completing my university studies, and its purpose is purely
educational.

> *More details will be added as the project progresses.*

## Architecture

Three machines share the same repo, each running only its own part:

- **PC / Mac** — development, attacker, and ML training.
- **Raspberry Pi 4 (2 GB RAM)** — the victim server, traffic sensor, ML inference, and automated response.

ML models are trained on PC/Mac and only run (inference) on the Pi — no heavy ML frameworks on the Pi.

## Table of contents

- [Description](#description)
- [Architecture](#architecture)
<!-- to be filled in over time: setup, usage, etc. -->
