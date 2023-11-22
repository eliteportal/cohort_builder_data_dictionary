# Cohort Builder Data Model

This repository is meant to track the data model for cohort builder.

This data model assumes that files and individual manifests have already been uploaded. Most of the information will come from those manifests. The main collection point is the individual to file mapping manifest.

## Setup

1. Get [schematic](https://github.com/Sage-Bionetworks/schematic)
2. Initialize schematic from the CLI `schematic init --config ~/path/to/config.yml` e.g. `schematic init --config ~/path/to/config.yml`
3. Edit the `config.yml` file with the appropriate information for the project
4. Run `main-workflow.sh` to generate the data model CSV and JSON

## Visualization
