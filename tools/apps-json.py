#!/usr/bin/env python3
"""Write apps.json for the simulator's Apps tab from a CardPuter-Apps checkout.

    tools/apps-json.py <apps-checkout> <out.json> [commit]

Each app folder has <id>.pkg (NAME, SUMMARY, APP_VERSION) and app.cmake,
whose zs_app(<id> ...) lines name the apps it adds (a pack like Dev Tools
adds several). The page tags an app "Try it here" when one of those ids is
built into the simulator.
"""
import json, pathlib, re, sys

root, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
commit = sys.argv[3] if len(sys.argv) > 3 else ""
apps = []
for pkg in sorted(root.glob("apps/*/*.pkg")):
    text = pkg.read_text()
    field = lambda k: (re.search(rf'^{k}="(.*)"', text, re.M) or [None, ""])[1]
    folder = pkg.parent
    cmake = folder / "app.cmake"
    ids = re.findall(r"^\s*zs_app\(\s*([a-z0-9_]+)", cmake.read_text(), re.M) if cmake.exists() else []
    apps.append({
        "id": pkg.stem,
        "ids": ids or [pkg.stem],
        "name": field("NAME") or pkg.stem,
        "summary": field("SUMMARY"),
        "version": field("APP_VERSION"),
        "url": f"https://github.com/hartj77-blip/CardPuter-Apps.4ME-U/tree/main/apps/{folder.name}",
    })
apps.sort(key=lambda a: a["name"].lower())
out.write_text(json.dumps({"commit": commit, "apps": apps}, indent=1) + "\n")
print(f"{out}: {len(apps)} apps")
