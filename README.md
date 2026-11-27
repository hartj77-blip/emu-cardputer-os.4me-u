# ZeroOS in your browser

**Try it: https://hartj77-blip.github.io/emu-cardputer-os.4me-u/**

The real ZeroOS home screen and every app from
[CardPuter-Apps.4ME-U](https://github.com/hartj77-blip/CardPuter-Apps.4ME-U), compiled to WebAssembly.
The hardware (battery, Wi-Fi, sensors, audio) is simulated. RF Tools opens, but its radio tools
need a real receiver, so they say so here.

It's a good way to see what ZeroOS is like before you put it on a Cardputer Zero. There is nothing to
install and no account to make, and nothing is kept between visits.

## How to use it

1. Open the page and slide the **power switch** (the red slider at the top right, above `tab`) to
   the right. Sliding it off and on again starts fresh, like the real device.
2. Type on your computer's keyboard. It works like a USB keyboard plugged into the Cardputer: the
   arrows, `Esc`, `Tab`, `Enter`, `Shift` and `Ctrl` do what they do on the device.
3. Or tap the keys drawn on the device. The Cardputer has no arrow keys of its own: arrows are `fn`
   with `F`, `Z`, `X` and `C`, shown in orange. `shift`, `fn` and `sym` don't need holding: tap one and it
   applies to the next key, tap it twice to lock it on, and tap it again to unlock it.
4. `Esc` goes back. Hold it to go to the home screen from anywhere.

The guide under the device on the page has the rest: every key, and what each app does.

## How the page is built

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
| [CardPuter-OS.4ME-U](https://github.com/hartj77-blip/CardPuter-OS.4ME-U) | The OS: the home screen (ZeroShell), the three built-in apps, the hardware layer, the SD card image, OS updates |
| [CardPuter-Apps.4ME-U](https://github.com/hartj77-blip/CardPuter-Apps.4ME-U) | Every other ZeroOS app, the packages the Apps app downloads, and the index that lists them |
| This one | The browser emulator: the real home screen and apps compiled to WebAssembly, [running here](https://hartj77-blip.github.io/emu-cardputer-os.4me-u/) |
| [M5Stack's app store](https://github.com/CardputerZero/packages) | Not ours: about 190 community apps made for M5's own launcher, which ZeroOS can install too. [Which ones work on ZeroOS](https://github.com/hartj77-blip/CardPuter-OS.4ME-U/blob/main/docs/M5-APPS.md) |

Apps from M5Stack's app store don't run in the emulator: they are Linux programs for the real
hardware, and the Apps tab only shows a few of them as examples. The [compatibility checklist](https://github.com/hartj77-blip/CardPuter-OS.4ME-U/blob/main/docs/M5-APPS.md) says which of them work on ZeroOS.

Found a problem? Use **Report a problem** on the page. It opens an issue in the OS repository with
a link that replays the keys you pressed.

## Licence and credits

This repository is MIT licensed, see [LICENSE](LICENSE). The page is built from
[ZeroOS](https://github.com/hartj77-blip/CardPuter-OS.4ME-U#license-and-third-party-code) and
[its apps](https://github.com/hartj77-blip/CardPuter-Apps.4ME-U#licence-and-third-party-code), so
everything credited there is in the page too. These are what the page itself is made with:

| Project | Used for | Licence |
| --- | --- | --- |
| [Emscripten](https://github.com/emscripten-core/emscripten) 3.1.74, set up by [setup-emsdk](https://github.com/mymindstorm/setup-emsdk) | Compiling ZeroOS and the apps to WebAssembly | MIT / UIUC |
| [LVGL](https://github.com/lvgl/lvgl) 9.2.2 | Drawing ZeroOS's screen | MIT |
| The [Ubuntu font](https://design.ubuntu.com/font) and [Font Awesome 5 Free](https://github.com/FortAwesome/Font-Awesome) (as bundled with LVGL) | ZeroOS's text and icons | Ubuntu Font Licence; icons CC BY 4.0, font SIL OFL 1.1 |
| [Space Grotesk](https://fonts.google.com/specimen/Space+Grotesk), [Inter](https://fonts.google.com/specimen/Inter), [JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono) (Google Fonts) | The page around the device | SIL OFL 1.1 |
| Ansel Adams' photographs from the U.S. National Archives ([79-AA-T14](https://commons.wikimedia.org/wiki/File:Ansel_Adams_-_National_Archives_79-AA-T14.jpg), [79-AA-G01](https://commons.wikimedia.org/wiki/File:Adams_The_Tetons_and_the_Snake_River.jpg)) | The home and lock screen wallpapers | Public domain |
| [M5Stack's documentation](https://docs.m5stack.com/en/CardputerZero) and [board drivers](https://github.com/m5stack/m5stack-linux-dtoverlays) | The drawing of the device, and how its keyboard behaves | See those pages |
| [GitHub Pages](https://pages.github.com) | Hosting the page | |

Cardputer and M5Stack are trademarks of M5Stack and are only used here to name the hardware. This is
a community project. It isn't made, endorsed or supported by M5Stack.
