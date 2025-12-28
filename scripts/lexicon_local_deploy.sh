#!/bin/bash
set -e

scripts/build_lexicon.sh

if [ -d ~/Library/'Application Support'/Anki2/addons21/lexicon ]; then
    echo ~/Library/'Application Support'/Anki2/addons21/lexicon

    # remove all files except for user_files
    find ~/Library/'Application Support'/Anki2/addons21/lexicon \
    -path "*/user_files" -prune -o -mindepth 1 -print \
    -exec rm -rf {} +

    echo "Removed all files except user_files"
fi

# move the zip file contents to the anki addon folder
# d for destination, o for overwrite, q for quiet
unzip -oq lexicon.myaddon -d \
~/Library/'Application Support'/Anki2/addons21/lexicon

rm lexicon.myaddon

