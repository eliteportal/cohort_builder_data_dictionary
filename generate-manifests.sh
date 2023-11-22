#!/bin/bash

set -e

GREEN='\033[0;32m'
NC='\033[0m' # No Color

# MANIFEST='IndividualMetadata' # only uncomment if creating single manifests

date "+%H:%M:%S %d/%m/%y"
schematic schema convert ./cohort-builder-model.csv \
    --output_jsonld ./cohort-builder-model.jsonld
date "+%H:%M:%S %d/%m/%y"

for MANIFEST in 'FileMapToIndividual' 'IndividualMetadata'; do
    echo "-- ${GREEN}${MANIFEST}${NC}"

    RESULTS=$(schematic manifest --config ./config.yml \
        get -dt $MANIFEST \
        --output_xlsx ./manifest-templates/$MANIFEST \
        --title $MANIFEST \
        --sheet_url)

    # echo $RESULTS
    NOW=$(date)
    echo $NOW "," $MANIFEST "," $RESULTS >>./manifest-templates/manifest-generation-results.csv
    echo -----------------------------
done
