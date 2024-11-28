#!/bin/bash
set -e

cd addon

#externals for interactng with anki
# q for quiet, r for recursive, x for exclude
zip -qr ../lexicon.myaddon . -x '**/__pycache__/*'

cd ../lexicon

# lexicon application clean architecture
# q for quiet, r for recursive, x for exclude
zip -qr ../lexicon.myaddon entities -x '**/__pycache__/*'
zip -qr ../lexicon.myaddon entry -x '**/__pycache__/*'
zip -qr ../lexicon.myaddon repo -x '**/__pycache__/*'
zip -qr ../lexicon.myaddon usecase -x '**/__pycache__/*'

cd ..

#install dependencies
mkdir third_party_dependencies
pip install -r requirements/requirements-prod.txt -t third_party_dependencies
# q for quiet, r for recursive, x for exclude
zip -qr lexicon.myaddon third_party_dependencies -x '**/__pycache__/*'

rm -rf third_party_dependencies

#add user_files to the zip file
# q for quiet, r for recursive, x for exclude
zip -qr lexicon.myaddon user_files -x '*.log'

