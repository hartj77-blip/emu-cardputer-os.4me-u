# ZeroOS in your browser

**Try it: https://hartj77-blip.github.io/emu-cardputer-os.4me-u/**

The real ZeroOS home screen and every app from
[CardPuter-Apps.4ME-U](https://github.com/hartj77-blip/CardPuter-Apps.4ME-U), compiled to WebAssembly.
The hardware (battery, Wi-Fi, sensors, audio) is simulated. RF Tools opens, but its radio tools
need a real receiver, so they say so here.

This repository only hosts the page. The code is in
[CardPuter-OS.4ME-U](https://github.com/hartj77-blip/CardPuter-OS.4ME-U) (`web/`), and
`.github/workflows/pages.yml` checks every 5 minutes and rebuilds the page when either repository's `main`
branch has changed, so a change is live within about 5-15 minutes. It runs the OS's `web/build.sh` with
`ZS_APPS` pointing at a checkout of the Apps repository, which compiles every app into the page.
The Apps tab's list (`apps.json`) comes from
[CardPuter-Apps.4ME-U](https://github.com/hartj77-blip/CardPuter-Apps.4ME-U) the same way, written by
`tools/apps-json.py` from each app's `.pkg` file.

Found a problem? Use **Report a problem** on the page. It opens an issue in the OS repository with
a link that replays the keys you pressed.
