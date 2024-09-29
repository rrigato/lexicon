#!/bin/bash
set -e

cd addon

#externals for interactng with anki
zip -r ../lexicon.myaddon .

cd ..

# lexicon application clean architecture
zip -r lexicon.myaddon lexicon -x '**/__pycache__/*'

# move the zip file to the anki addon folder
unzip lexicon.myaddon -d \
'/Users/ryan/Library/Application Support/Anki2/addons21/lexicon'