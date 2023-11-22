# PACKAGES
import os
import pandas as pd
import numpy as np
import pathlib
from toolbox import utils
from localutils import localcube

# MAIN VARIABLES
csv_model = "cohort-builder-model.csv"
json_model = "cohort-builder-model.jsonld"
manifest_basename = "cohort-builder"

# Get tables to build from
syn = utils.synLogin()

# # Templates
#
# - File Map for Individuals
# - Individuals?
#

# Base columns
dm = pd.read_csv(csv_model)

# File mapping
# ref_df = syn.tableQuery("SELECT * FROM syn52234184").asDataFrame()

# - fileId, fileSize, and currentVersion should already be in synapse
# - dataType, dataSubtype, Assay, fileFormat are annotations that should be pulled in from manifests
# - individual related metadata will be pull from individual manifests within projects
#

new_dm = [
    {
        "Attribute": "Individual Metadata",
        "Description": "Template for mapping individuals to files in synapse",
        "Valid Values": "",
        "DependsOn": "individualId, minAge, maxAge, Sex, Study, Diagnosis",
        "DependsOn Component": "",
        "Required": "False",
        "Properties": "Template",
        "Validation Rules": "",
        "Template": "",
        "Parent": "Template",
        "Ontology": "Sage Bionetworks",
        "UsedIn": "",
        "Module": "Cohort Builder",
    },
    {
        "Attribute": "Study",
        "Description": "",
        "Valid Values": "LLFS",
        "DependsOn": "",
        "DependsOn Component": "",
        "Required": "False",
        "Properties": "",
        "Validation Rules": "",
        "Template": "",
        "Parent": "DataProperty",
        "Ontology": "Sage Bionetworks",
        "UsedIn": "",
        "Module": "Cohort Builder",
    },
    {
        "Attribute": "minAge",
        "Description": "Masked age of individual that is the minimum age found across files",
        "Valid Values": "",
        "DependsOn": "",
        "DependsOn Component": "",
        "Required": "False",
        "Properties": "",
        "Validation Rules": "int",
        "Template": "",
        "Parent": "DataProperty",
        "Ontology": "Sage Bionetworks",
        "UsedIn": "",
        "Module": "Cohort Builder",
    },
    {
        "Attribute": "maxAge",
        "Description": "Masked age of individual that is the maximum age found across files",
        "Valid Values": "",
        "DependsOn": "",
        "DependsOn Component": "",
        "Required": "False",
        "Properties": "",
        "Validation Rules": "int",
        "Template": "",
        "Parent": "DataProperty",
        "Ontology": "Sage Bionetworks",
        "UsedIn": "",
        "Module": "Cohort Builder",
    },
    {
        "Attribute": "Diagnosis",
        "Description": "",
        "Valid Values": "",
        "DependsOn": "",
        "DependsOn Component": "",
        "Required": "False",
        "Properties": "",
        "Validation Rules": "",
        "Template": "",
        "Parent": "DataProperty",
        "Ontology": "Sage Bionetworks",
        "UsedIn": "",
        "Module": "Cohort Builder",
    },
    {
        "Attribute": "LLFS",
        "Description": "",
        "Valid Values": "",
        "DependsOn": "",
        "DependsOn Component": "",
        "Required": "False",
        "Properties": "",
        "Validation Rules": "",
        "Template": "",
        "Parent": "ValidValue",
        "Ontology": "Sage Bionetworks",
        "UsedIn": "",
        "Module": "Cohort Builder",
    },
    {
        "Attribute": "Assay",
        "Description": "",
        "Valid Values": "snpArray, 'wholeGenomeSeq",
        "DependsOn": "",
        "DependsOn Component": "",
        "Required": "False",
        "Properties": "DataProperty",
        "Validation Rules": "",
        "Template": "",
        "Parent": "Template",
        "Ontology": "Sage Bionetworks",
        "UsedIn": "",
        "Module": "Cohort Builder",
    },
    {
        "Attribute": "snpArray",
        "Description": "",
        "Valid Values": "",
        "DependsOn": "",
        "DependsOn Component": "",
        "Required": "False",
        "Properties": "",
        "Validation Rules": "",
        "Template": "",
        "Parent": "ValidValue",
        "Ontology": "Sage Bionetworks",
        "UsedIn": "",
        "Module": "Cohort Builder",
    },
    {
        "Attribute": "wholeGenomeSeq",
        "Description": "",
        "Valid Values": "snpArray, 'wholeGenomeSeq",
        "DependsOn": "",
        "DependsOn Component": "",
        "Required": "False",
        "Properties": "DataProperty",
        "Validation Rules": "",
        "Template": "",
        "Parent": "ValidValue",
        "Ontology": "Sage Bionetworks",
        "UsedIn": "",
        "Module": "Cohort Builder",
    },
    {
        "Attribute": "File to Individual Map",
        "Description": "Template for mapping individuals to files in synapse",
        "Valid Values": "",
        "DependsOn": "fileName, individualId",
        "DependsOn Component": "Individual Metadata",
        "Required": "False",
        "Properties": "Template",
        "Validation Rules": "",
        "Template": "",
        "Parent": "Template",
        "Ontology": "Sage Bionetworks",
        "UsedIn": "",
        "Module": "Cohort Builder",
    },
    {
        "Attribute": "fileName",
        "Description": "Name of the file",
        "Valid Values": "",
        "DependsOn": "",
        "Required": "True",
        "Properties": "DataProperty",
        "Validation Rules": "str",
        "Template": "File to Individual Map",
        "Parent": "DataProperty",
        "Ontology": "Sage Bionetworks",
        "UsedIn": "File to Individual Map",
        "Module": "Cohort Builder",
    },
    {
        "Attribute": "individualId",
        "Description": "Unique individual identifier",
        "Valid Values": "",
        "DependsOn": "",
        "Required": "True",
        "Properties": "DataProperty",
        "Validation Rules": "str",
        "Template": "File to Individual Map",
        "Parent": "DataProperty",
        "Ontology": "Sage Bionetworks",
        "UsedIn": "File to Individual Map",
        "Module": "Cohort Builder",
    },
    {
        "Attribute": "Template",
        "Description": "Template property for data model",
        "Valid Values": "",
        "DependsOn": "",
        "DependsOn Component" "Required": "",
        "Properties": "",
        "Validation Rules": "",
        "Template": "",
        "Parent": "Schema",
        "Ontology": "Sage Bionetworks",
        "UsedIn": "",
        "Module": "",
    },
    {
        "Attribute": "DataProperty",
        "Description": "Column for manifests",
        "Valid Values": "",
        "DependsOn": "",
        "Required": "",
        "Properties": "",
        "Validation Rules": "",
        "Template": "",
        "Parent": "Schema",
        "Ontology": "Sage Bionetworks",
        "UsedIn": "",
        "Module": "",
    },
    {
        "Attribute": "ValidValue",
        "Description": "valid value for dataProperty",
        "Valid Values": "",
        "DependsOn": "",
        "Required": "",
        "Properties": "",
        "Validation Rules": "",
        "Template": "",
        "Parent": "DataProperty",
        "Ontology": "Sage Bionetworks",
        "UsedIn": "",
        "Module": "",
    },
    {
        "Attribute": "Schema",
        "Description": "Schema property used in parent column",
        "Valid Values": "",
        "DependsOn": "",
        "Required": "",
        "Properties": "",
        "Validation Rules": "",
        "Template": "",
        "Parent": "",
        "Ontology": "Sage Bionetworks",
        "UsedIn": "",
        "Module": "",
    },
]

new_dm = pd.concat([dm, pd.DataFrame.from_dict(new_dm)])
print("Duplicates: ", sum(new_dm.duplicated(subset="Attribute")))
new_dm = new_dm.replace("", np.nan)
new_dm = new_dm.drop_duplicates(subset="Attribute", keep="first").sort_values(
    by=["Attribute"]
)

new_dm.to_csv(csv_model, index=False)
