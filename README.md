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

| Repository | What's in it |
| --- | --- |
| [CardPuter-OS.4ME-U](https://github.com/hartj77-blip/CardPuter-OS.4ME-U) | The OS: the home screen (ZeroShell), the four built-in apps, the hardware layer, the SD card image, OS updates |
| [CardPuter-Apps.4ME-U](https://github.com/hartj77-blip/CardPuter-Apps.4ME-U) | Every other ZeroOS app, the packages the Apps app downloads, and the index that lists them |
| This one | The browser emulator: the real home screen and apps compiled to WebAssembly, [running here](https://hartj77-blip.github.io/emu-cardputer-os.4me-u/) |
| [M5Stack's app store](https://github.com/CardputerZero/packages) | Not ours: about 180 community apps made for M5's own launcher, which ZeroOS can install too. [Which ones work on ZeroOS](https://github.com/hartj77-blip/CardPuter-OS.4ME-U/blob/main/docs/M5-APPS.md) |

Apps from M5Stack's app store don't run in the emulator: they are Linux programs for the real
hardware, and the Apps tab only shows a few of them as examples. The [compatibility checklist](https://github.com/hartj77-blip/CardPuter-OS.4ME-U/blob/main/docs/M5-APPS.md) says which of them work on ZeroOS.

Found a problem? Use **Report a problem** on the page. It opens an issue in the OS repository with
a link that replays the keys you pressed.
