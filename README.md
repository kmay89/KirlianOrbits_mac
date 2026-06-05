
# Kirlian Orbits

![App Screenshot](https://github.com/bennjordan/KirlianOrbits_win64/blob/main/korbits.png?raw=true)

---

## ⚡ NEW: Web Edition — runs in your browser, zero setup

### ▶ **[Play it now — live demo](https://kmay89.github.io/KirlianOrbits_mac/)** &nbsp;·&nbsp; or open **[`kirlian_orbits_web.html`](kirlian_orbits_web.html)** locally

A single self-contained HTML file that reimplements the "spinning notes" engine in the
browser. **No install, no Python, no MIDI rig required** — click the link above and it plays a song.
Runs anywhere a modern browser does: **macOS, Windows, Linux, even phones/tablets.**
*(This repo is named `…_mac` because the web build is what unblocks Mac users — but it's
web-first and Mac-**compatible**, not Mac-only.)*

**Why, if the original is a MIDI tool?** Kirlian Orbits is a MIDI *controller* — it makes no
sound itself; it sends notes to a synth/DAW you set up. Brilliant for musicians with that
rig, but a wall for everyone else, and on **macOS there's no built-in synth at all**, so a
first-time Mac user hears nothing. The *idea* — watching notes orbit and chords light up — is
delightful far beyond MIDI, so we gave it **its own voice and visuals** so anyone can try it in
one click — and **it can still send real MIDI** to your DAW/hardware in Chrome/Edge (see below).

**What's in the web edition:**
- 🔊 **Built-in synthesizer** — 4 voices (Kirlian Pluck, Super Saw, FM Bell, Pure Sine) + reverb.
- 🎹 **Optional Web MIDI output** — pick a port in the **Output** menu to drive a DAW or hardware,
  just like the original (desktop **Chrome/Edge** with a USB‑MIDI device; **Bluefy** on iOS).
- 🌈 **Live spectrum wrapped around the ring** (you literally *spin a spectrum*) + a **chord
  constellation** that shows what a chord looks like as it sounds.
- 🎵 **One-click Starter Songs** — generative *Soundscapes* plus a **Music Box** of famous
  public-domain tunes (Twinkle Twinkle, Ode to Joy, Für Elise, Greensleeves).
- 👋 **Welcome + tips** that explain it to musicians *and* total beginners, with a keyboard legend.
- 🎛️ Faithful port of the orbital model (Bézier sweep arm, BPM-%/divisor orbits, the original
  relative-polar collision math, 22 scales, key selection, Kirlian neon look).

**Controls:** **Space** to play · **`1`–`9`** to load a song · **Click** the ring to add a note ·
**drag** notes & the pink handles · **`S`** to spin · **`D`** for direction · **Esc** to deselect ·
**Del** to delete · **C** to clear · **?** for help.

📖 **Full documentation, the rationale, controls table, and roadmap: [`WEB_EDITION.md`](WEB_EDITION.md).**

> **Original concept & Python app: [Benn Jordan](https://www.patreon.com/bennjordan).**
> Web edition by **Karl Meves / ERRERLabs**. Released, like the original, under
> [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.en) — attribution,
> non-commercial. **The original Python app below is untouched.**

---


While DJing last week and staring at the spinning discs of a Rane System One, I started making plans with myself to put neon stickers on the discs, then use webcams to translate the detection of neon colors into MIDI events to use as a sequencer. Then I decided that such an activity would be a lot of work for a solid 7 minutes of enjoyment, and I'd be better served just making a program that can do it in a much more functional, customizable, and accessible way. 

This isn't an original idea, by the way. Circular sequencers date back to Raymond Scott's "Circle Machine" in 1959. There are plenty of similar sequencers out there, but they always left something to be desired for me.





# Features

**Interactive Bezier Warping:** You can grab the three control handles on the sweep arm and bend the spline into weird curves even while it is spinning. The mouse input mathematically rotates backward using an inverse rotation matrix to compensate. Science!

**Concentric Orbital Paths:** Notes orbit at customized speeds. You can set them to orbit at a percentage of the master BPM (10% to 400%) or sync them to integer divisors (like /4 or /8 of the clock).

**Relative Collision Math:** Triggers use relative polar coordinates. That means notes trigger with 100% frame-rate independent accuracy regardless of how fast the line sweeps, how fast the notes orbit, or which direction you spin (Clockwise / CCW).

**Generative Range Mode:** Toggle "Ranges" next to Pitch, Velocity, or Gate Length to instantly split them into separate Min and Max boundaries. Triggers will select a random value inside your boundaries.

**22 Scales & Explicit Key Selection:** Choose from 22 Western, jazz, or exotic scales (like Hungarian Minor, Hijaz, Spanish Gypsy, or Enigmatic) and explicitly set your key signature (C through B). No more off-key accidents.

**Tkinter Session Persistence:** Save/Load your orbital states using standard Ctrl+S and Ctrl+O hotkeys.

**Windows MIDI Diagnostics panel:** Press D to open a real-time diagnostics overlay that acts as a packet logger and tells you if another app is hogging your MIDI ports.
## License

[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.en)

TL;DR: You can use, share, copy, modify, and integrate this sequencer freely with 2 exceptions:

**• Attribution** - Just gimme props bruh

**• Non-Commercial** - If I get Instagram ads trying to sell this to people for $9.99 a month, we're going to have a fucking problem. 

## How to run w/ Python

**1. Grab the prerequisites!**

You'll need Python 3.12+ installed. Then open your terminal and install the dependencies:

```bash
  pip install pygame mido python-rtmidi
```
 (Note: python-rtmidi compiles a C++ wrapper under the hood. If it complains, make sure your Windows C++ Build Tools are installed, or install a pre-compiled wheel).

 **2. Boot it up**
 
 Navigate to the directory and run:

 ```bash
  python main.py
```
Boom. You're in. Click anywhere inside the pink ring to place an orbital note. Drag them to change their track radius. Spacebar starts/pauses the action.

## How to build the exe

I had AI set up a dedicated build script called *build_exe.py* so you don't have to write a 3-mile-long PyInstaller command in your terminal. It compiles the whole program (interpreter, pygame, RTmidi DLLs, assets, and Tkinter dialogues) into a single, self-contained dist/KirlianOrbits.exe file.

**1. Install PyInstaller**


```bash
  pip install pyinstaller
```

 **2. Run the compiler script**

 ```bash
  python build_exe.py
```
The script ~~will~~ should automatically clean your build environment, compile the standalone executable, and sweep away all temporary build folders when it finishes.

Look inside *dist/KirlianOrbits.exe* for your shiny new binary!

## How to just download an exe and run the damn thing. 

It's on my [Patreon](https://www.patreon.com/bennjordan) (in the $1 tier). Just search for "Kirlian Orbits". 

Believe it or not, this exe gatekeeping isn't so I can become filthy rich off of your dollar, it's to prevent other sites from sharing the "freeware" executable file, which increases the likelyhood that someone will fuck with the executable file and secretly watch you on your webcam. 


## Support

There is no support. I fully intend of flushing my brain of this project in about 5 minutes. If you have feature requests, feel free to post them here and maybe someone will be kind enough to update the code or fork their own build.

## AI Disclaimer

Yes, I used a local LLM to help me navigate and understand the process of making something I initially made in Processing into a graphical and functional UI for Windows that conveniently comes in a package smaller than 30mb. 
This is what I believe AI is great for. Doing the boring shit so you can spend more time doing the fun shit and sharing it with people in a broadly accessible way.
But for some reason, I feel like it's ethical that I disclose this. 
