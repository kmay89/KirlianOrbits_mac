# Kirlian Orbits — Web Edition

A single, self-contained file — [`kirlian_orbits_web.html`](kirlian_orbits_web.html) — that you
open in a browser. **No install, no Python, no MIDI rig required.** It plays a song the moment you
press start, and you can build your own in seconds.

> **It runs anywhere a modern browser does** — macOS, Windows, Linux, even phones and tablets.
> (This repo is named `…_mac` because the web build is what finally unblocks *Mac* users of the
> original Windows-oriented app — but nothing here is Mac-only. Think of it as **"web, and
> Mac‑compatible,"** not "for Mac.")

---

## Why build this? (If the original is a MIDI tool, what's the point?)

Great question — and worth answering plainly, because it's the whole reason this exists.

The original Kirlian Orbits is a **MIDI sequencer**, and a lovely one. But "MIDI sequencer" means
it **makes no sound on its own** — it *transmits* MIDI notes to a separate synthesizer or DAW that
**you** have to set up. For a musician who already has that rig, it's perfect. For everyone else,
it's a wall:

- Install Python + `pygame` + `python-rtmidi` (which compiles a C++ extension), **or** get the
  Windows `.exe`.
- Create a **virtual MIDI cable** and route it into a DAW or soft-synth.
- On **macOS especially**, there is *no* built-in General‑MIDI synth — so a first-time Mac user
  does all of that and still hears **nothing**.

But the *idea* underneath — notes orbiting, a glowing arm sweeping past them, chords lighting up as
they trigger — is delightful **far beyond MIDI**. So we kept the original's "brain" and gave it the
three things it was missing for a casual audience:

1. **Its own voice** — a built-in Web Audio synthesizer, so it makes sound instantly.
2. **A reason to just *watch* it** — visual-first: a live spectrum wrapped around the ring, chord
   "constellations," and the Kirlian neon glow.
3. **A front door** — one file you open; it auto-plays a song; a welcome panel explains it to both
   musicians and total beginners.

**Net effect:** the barrier to *trying* the concept drops from "an afternoon of setup" to a
double-click. Musicians still get a fast, fun playground; everyone else finally gets to experience
what makes it cool.

> **"But it's not MIDI anymore?"** The built-in synth is the *default*, not a replacement of the
> philosophy — and **real MIDI output is built in too.** In browsers with the Web MIDI API (desktop
> **Chrome/Edge** with a USB‑MIDI device, or **Bluefy** on iOS) you can pick a port in the **Output**
> menu and drive your DAW or hardware, exactly like the original. We just led with built-in sound so
> it works for *everyone* on the very first load.

---

## What we built

### 🔊 Built-in synthesizer
A small polyphonic Web Audio engine so it sounds great with zero setup:
- **4 voices:** Kirlian Pluck, Super Saw, FM Bell, Pure Sine.
- Per-note **ADSR envelope + filter**, velocity sensitivity, and a generated **convolution reverb**
  (adjustable from the top bar).
- Notes are scheduled in real time as the sweep arm crosses them, gated by each note's length.

### 🌈 Live spectrum + chord constellation
- A real **FFT of the audio output**, drawn as a neon spectrum **wrapped radially around the ring** —
  you literally *spin a spectrum*. It has frequency-mapped color, a slow chromatic drift, falling
  **peak-hold caps**, and an inward reflection, all additively blended for glow.
- A **chord constellation** connects notes that fire together, so you can *see what a chord looks
  like* as it sounds.

### 🎹 Web MIDI output (drive a real DAW / hardware)
The original's whole job — sending MIDI — is here too, now optional:
- In browsers that expose the **Web MIDI API** (desktop **Chrome / Edge** with a USB‑MIDI interface
  or device; **Bluefy** on iOS), the **Output** menu lists your MIDI ports.
- Pick a port and notes are sent as standard **Note On / Note Off** messages (with scheduled gates),
  so it plays your DAW or synth. Selecting a port routes there exclusively (the built-in synth mutes
  so your DAW gets a clean signal); the on-screen spectrum reflects the built-in voice, so it idles
  in MIDI mode.
- No Web MIDI support? The menu simply shows the built-in synth and everything still works.

### 🎛️ Faithful engine port
Everything that makes the original tick, re-implemented on HTML5 Canvas:
- The spinning **cubic-Bézier sweep arm** (warp it by dragging its handles).
- **Concentric orbits** with per-note speed in **BPM-%** or **clock divisors** (polymeter).
- The original **frame-rate-independent, relative-polar collision math** for sample-accurate triggers
  regardless of tempo, orbit speed, or spin direction.
- **22 scales** and explicit **key** selection (C–B); new notes snap to the chosen key.
- The **Kirlian neon aesthetic** — coronal glows, electric violet/pink/emerald.

### 🎵 One-click Starter Songs
A grouped menu so anyone hears something gorgeous immediately:
- **Soundscapes** (generative): Kirlian Bloom · Deep Space Pad · Starlight Cascade · Neon Arpeggio ·
  Hypno Pulse.
- **🎵 Music Box (famous public-domain tunes):** **Twinkle Twinkle · Ode to Joy · Für Elise ·
  Greensleeves.** These are laid out like a real **music-box cylinder** — the notes sit on one ring
  with the spin off, and a fixed reader arm at 12 o'clock plays them *in order* as they orbit past,
  then loops.

### 👋 Onboarding that meets you where you are
- A **welcome panel** with two side-by-side explanations — one for total beginners, one for
  musicians.
- A **first-run tips card** with a few quick ideas so anyone can start creating and feel ownership.
- A **`?` button** to reopen the welcome anytime.

### 🛠️ Fixes & polish (these also help the original)
- Fixed a latent **`NameError`** in `main.py` (`COLOR_BORDER` was used but never imported — it would
  crash the `D` diagnostics panel).
- Added a small **pytest suite** for the pure-Python engine and a `.gitignore`, so the repo's CI is
  green and the engine has regression coverage.
- Spin direction is now legible (curved default arm + a glowing rim **comet**); changing **Key/Scale**
  re-tunes every note live; the editor panel no longer jumps when you add notes; the spectrum is
  allocation-free for smooth frame rates.

---

## Quick start

**▶ Live demo (no download): <https://kmay89.github.io/KirlianOrbits_mac/>** — click and press
**Start & Play**.

Prefer local? Double-click `kirlian_orbits_web.html` (or drag it into a browser tab). That's it.

> The live demo is published automatically by a GitHub Actions workflow
> ([`.github/workflows/deploy-pages.yml`](.github/workflows/deploy-pages.yml)) on every push to
> `main` that touches the app — the page root serves the app directly.

### Controls & keyboard legend

| Action | How |
| --- | --- |
| Play / pause | **Space**, or the Play button |
| Load a Starter Song | **`1`–`9`**, or the **Starter Song** menu (1–5 Soundscapes, 6–9 Music Box) |
| Add a note | **Click inside the ring** (it snaps to the current key) |
| Edit a note | **Click a note** → side panel (pitch, velocity, gate, orbit mode/speed) |
| Move a note | **Drag** it — outward raises pitch, around changes its phase |
| Warp the sweep arm | **Drag the pink handles** |
| Toggle spin | **`S`**, or the Spin button |
| Flip direction (CW/CCW) | **`D`**, or the Direction button |
| Tempo down / up | **`[`** / **`]`** (or the Tempo slider) |
| Deselect / close editor | **`Esc`**, or click outside the ring |
| Delete selected note | **`Del` / `Backspace`** |
| Clear everything | **`C`**, or the Clear button |
| Help / how it works | **`?`** (or **`H`**), or the `?` button — reopens the welcome |

Top bar also has: **Tempo**, **Spin** on/off, **Direction** (CW/CCW), **Key**, **Scale**, **Voice**,
**Reverb**, **Output** (built-in synth or a Web MIDI port), and a **Spectrum** toggle.

---

## How it works (for the curious)

It's a **polar sequencer**. Each note's **radius = pitch** (snapped to the key/scale; outer = higher)
and its **angle = phase** around the circle. A Bézier "arm" sweeps around; when it **crosses** a note's
angle at that note's radius, the note fires. Because crossings are computed from **relative polar
angles** rather than positions per frame, triggering is exact no matter the frame rate, tempo, or
direction. The same radius⇄pitch mapping is used everywhere — clicking to add a note, **dragging** one
in/out to retune it, and laying out the Music Box — so the convention is always consistent.

The **Music Box** mode is the same engine with the spin turned **off**: the arm sits still at 12
o'clock and the *notes* orbit past it, so a melody laid out by angle reads out in order and loops —
exactly like the pins on a music-box cylinder passing the comb. Because radius is pitch, each tune's
notes sit at the height of their pitch, so the melody's **up-and-down contour is visible** as the
notes spiral.

---

## Compatibility

- Works in current **Chrome, Edge, Safari, and Firefox** (desktop and mobile).
- Requires the **Web Audio API** (standard in all modern browsers).
- Browsers require **one user gesture before audio** — that's why the first click/"Start" button
  exists. Nothing else is needed.
- **Web MIDI output** needs a browser that exposes the Web MIDI API: desktop **Chrome / Edge** (with a
  USB‑MIDI interface or device), or **Bluefy** on iOS. Safari and Firefox don't expose Web MIDI yet,
  so they fall back to the built-in synth — everything else still works.

---

## Roadmap

- **Save / Load patterns** — export to JSON or a shareable URL (the Python app has Ctrl+S/Ctrl+O).
- **More presets + a "Randomize"** for endless instant variety.
- **MIDI input / clock sync** — react to an external keyboard or sync to a DAW's tempo.

*(Done: **hosted one-click demo** via GitHub Pages — see [Quick start](#quick-start).)*

---

## Credits & license

Original concept, design, and Python application by **[Benn Jordan](https://www.patreon.com/bennjordan)**.

Web edition (this build) — port, built-in synth, spectrum, presets, onboarding, and Web MIDI — by
**Karl Meves / [ERRERLabs](https://github.com/kmay89)**. It's an additive companion: **the original
Python app is untouched.**

Released, like the original, under **[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.en)**:
free to use, share, and modify **with attribution**, **non-commercial**.

> Public-domain note: the four Music Box melodies are centuries old and long out of copyright; only
> the melodies themselves (not any specific recording or arrangement) are used.
