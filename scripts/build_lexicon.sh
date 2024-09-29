#!/bin/bash
set -e

cd addon

#externals for interactng with anki
# q for quiet, r for recursive, x for exclude
zip -qr ../lexicon.myaddon . -x '**/__pycache__/*'

cd ..

# lexicon application clean architecture
# q for quiet, r for recursive, x for exclude
zip -qr lexicon.myaddon lexicon -x '**/__pycache__/*'

# move the zip file contents to the anki addon folder
# d for destination, o for overwrite, q for quiet
unzip -oq lexicon.myaddon -d \
'/Users/ryan/Library/Application Support/Anki2/addons21/lexicon'

rm lexicon.myaddon

