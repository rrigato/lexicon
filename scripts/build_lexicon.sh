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

#add user_files to the zip file
# q for quiet, r for recursive, x for exclude
zip -qr lexicon.myaddon user_files -x '*.log'

