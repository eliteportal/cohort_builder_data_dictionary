import yaml
import os
from pathlib import Path
import json


def import_config():
    """Import general local configuration for data model building"""
    with open("../config.yml", "r") as f:
        config = yaml.safe_load(f)

    # paths to import files
    # schematic_config = config["paths"]["schematic"]
    csv_model = Path(
        "../" + Path(config["model"]["input"]["location"]).stem + ".csv"
    ).resolve()
    json_model = Path("../" + config["model"]["input"]["location"]).resolve()
    manifest_basename = config["synapse"]["manifest_basename"]

    return csv_model, json_model, manifest_basename


def create_json_model(csv_model, json_model):
    """Create JSON model for DCA

    Args:
        csv_model (string): Full path to CSV model
        json_model (string): Full path to JSON model to write to
    """
    print(
        f"Running \n schematic schema convert {csv_model} --output_jsonld {json_model}"
    )

    os.system(f"schematic schema convert {csv_model} --output_jsonld {json_model}")

    print("Finished")


def get_mainfest_names(json_object):
    """Helper function for create dca config. Relies on having template in the properties column of templates"""
    # Manifest names in data model
    manifest_names_extracted = []

    for i in json_object["@graph"]:
        if i["@id"] == "bts:template":
            manifest_names_extracted += [
                t["@id"].replace("bts:", "") for t in i["schema:domainIncludes"]
            ]

    # display names extracted
    manifest_display_names_extracted = []

    for i in json_object["@graph"]:
        if i["@id"].replace("bts:", "") in (manifest_names_extracted):
            manifest_display_names_extracted.append(i["sms:displayName"])

    # Create dictionary for lookup later
    manifest_name_relationships = dict(
        zip(manifest_names_extracted, manifest_display_names_extracted)
    )

    return manifest_name_relationships


# Data modeling functions for manifest generation
def manifest_schema(k, v, t="file"):
    """Helper function for create dca config"""
    schema = {"display_name": v, "schema_name": k, "type": t}

    return schema


def create_dca_config(json_model):
    # look up dca config
    # if dca config exisits -> update schema version
    # else create dca config

    dca_template = {
        "manifest_schemas": [],
        "service_version": "v23.1.1",
        "schema_version": "v1.1",
    }

    records = ["FileMapToIndividual", "IndividualMetadata"]

    with open(json_model, "r") as jf:
        jo = json.load(jf)

    manifest_dict = get_mainfest_names(jo)

    for k, v in manifest_dict.items():
        if k in records:
            t = "records"
        else:
            t = "file"
        dca_template["manifest_schemas"].append(manifest_schema(k, v, t))

    json_formatted_str = json.dumps(dca_template, indent=2)

    print(json_formatted_str)

    with open(
        "../dca-template-config.json",
        "w",
    ) as f:
        f.write(json_formatted_str)
