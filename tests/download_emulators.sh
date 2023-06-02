#!/usr/bin/env bash
set -e

SITE="https://data.detahard.io/dev/firmware/releases/emulators/"
cd "$(dirname "$0")"

# download all emulators without index files, without directories and only if not present
wget -e robots=off \
    --no-verbose \
    --no-clobber \
    --no-parent \
    --no-directories \
    --no-host-directories \
    --recursive \
    --reject "index.html*" \
    --reject "-arm" \
    -P emulators/ \
    $SITE

chmod u+x emulators/detahard-emu-*

cd ..
# are we in Nix(OS)?
command -v nix-shell >/dev/null && nix-shell --run 'NIX_BINTOOLS=$NIX_BINTOOLS_FOR_TARGET autoPatchelf tests/emulators'
