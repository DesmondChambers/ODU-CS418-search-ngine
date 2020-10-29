Notes:
- This collection contains around 3974 dissertations and 2641 theses
- Each EDT has it's own subfolder denoted by it's unique handle. Each folder contains:
    - a .txt document containing the original metadata for reference
    - a .json conversion of the metadata that is ingestable by elasticsearch
    - documents related to the metadata
- Some folders contain extra files (e.g. .mov, .avi, etc.) I included those files becuase they were referenced in the metadata, however I don't know how relevant the extra files are to their corresponding PDF.
- Some fields like type_dcmitype and format_mimetype in the metadata are dropped when converting into an elasticsearch ingestible form because only a couple records have them and those attributes are obvious. A full list of keys that are kept is listed below.
- The script used for conversion is at the top level of this Google Drive. The original metadata files are included in case the metadata needs to be reconverted.
- I'm unsure what the fields date_adate, date_rdate, and date_sdate mean. Not all the records have those fields, but I decided to keep those dates in case they were important

metadata fields:
    "contributor_author",
    "date_accessioned",
    "date_available",
    "date_issued",
    "identifier_other",
    "identifier_uri",
    "identifier_sourceurl",
    "identifier_oclc",
    "description",
    "description_abstract",
    "description_provenance",
    "description_sponsorship",
    "format_medium",
    "publisher",
    "rights",
    "subject",
    "subject_lcc",
    "subject_lcsh",
    "title",
    "type",
    "language_iso",
    "relation",
    "contributor_department",
    "description_degree",
    "contributor_committeechair",
    "contributor_committeecochair",
    "contributor_committeemember",
    "degree_name",
    "degree_level",
    "degree_grantor",
    "degree_discipline",
    "handle",
    "relation_haspart",
    "date_adate",
    "date_sdate",
    "date_rdate"
