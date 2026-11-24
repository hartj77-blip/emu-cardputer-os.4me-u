# ZeroOS in your browser

**Try it: https://hartj77-blip.github.io/emu-cardputer-os.4me-u/**

The real ZeroOS home screen and apps for the M5Stack Cardputer Zero, compiled to WebAssembly.
The hardware (battery, Wi-Fi, sensors, audio) is simulated.

This repository only hosts the page. The code is in
[CardPuter-OS.4ME-U](https://github.com/hartj77-blip/CardPuter-OS.4ME-U) (`web/`), and
`.github/workflows/pages.yml` checks every 5 minutes and rebuilds the page when its `main` branch has changed, so a change is
live within about 5-15 minutes.
The Apps tab's list (`apps.json`) comes from
[CardPuter-Apps.4ME-U](https://github.com/hartj77-blip/CardPuter-Apps.4ME-U) the same way, written by
`tools/apps-json.py` from each app's `.pkg` file.

Found a problem? Use **Report a problem** on the page. It opens an issue in the OS repository with
a link that replays the keys you pressed.
