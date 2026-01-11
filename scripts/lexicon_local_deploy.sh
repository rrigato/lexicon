#!/bin/bash
set -e

scripts/build_lexicon.sh

ANKI_ADDON_DIR=~/Library/'Application Support'/Anki2/addons21/lexicon

if [ -d "$ANKI_ADDON_DIR" ]; then
    echo "$ANKI_ADDON_DIR"

    # Remove all files except for user_files and meta.json
    find "$ANKI_ADDON_DIR" \
        \( \
            -path "*/user_files" -o \
            -name "meta.json" \
        \) -prune \
        -o \
        -mindepth 1 -print \
        -exec rm -rf {} +

    echo "Removed all files except user_files and meta.json"
fi

# Move the zip file contents to the anki addon folder
# d for destination, o for overwrite, q for quiet
unzip -oq lexicon.myaddon -d "$ANKI_ADDON_DIR"

rm lexicon.myaddon

