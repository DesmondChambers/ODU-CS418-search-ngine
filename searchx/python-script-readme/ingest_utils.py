#!/usr/bin/env python3

import glob
import json
import argparse
from pathlib import Path

"""
Converts ETD metadata files into JSON so it can be added to ElasticSearch
"""

# List of expected keys
# This is used to check for new keys and to drop extraneous keys
_keys = {"contributor_author",
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
        "date_rdate"}

def clean_key(key):
    """
    Standardizes and clean key names. Note that this does not try to remove
    every instance of extraneous information since ElasticSearch can have
    aliases. For example, we will remove '_none' from 'subject_none', but we
    will not remove 'contributor_' from 'contributor_author' becuase:
        1) The distinction of 'contributor may be important'
        2) We can alias it to 'author'
    """
    key = key.replace('-', '_') # Change dash to underscore
    key = key.replace('_none', '') # remove parts like _none

    return key

def add_entry(payload, key, value):
    """
    Add a key value pair to a payload. If a value already exists for a given
    key, that value is turned into an array.

    :param dict payload: json object
    :param str key: object key
    :param value: value to add to under payload[key]
    """
    if key not in payload:
        payload[key] = value
    elif type(payload[key]) is not list:
        payload[key] = [payload[key]]
        payload[key].append(value)
    else:
        payload[key].append(value)

def postprocess(payload):
    """
    Define any processing steps that happen after creating the payload. This
    should be for steps that are easier to perform on a dictionary instead
    of the raw text

    :param dict payload: json payload
    """
    raise NotImplementedError

def process(data):
    if type(data) == str:
        payload = {}
        for line in data.split('\n'):
            # Split on the first colon. This assumes that no key
            # contains a colon
            key = clean_key(line[:line.index(':')].strip())
            value = line[line.index(':')+1:].strip()

            add_entry(payload, key, value)
    return payload


def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
            description='Convert an ETD metadata file to JSON. Metadata files are assumed to be .txt files')
    parser.add_argument('input_path', help='metadata file or directory to process')
    parser.add_argument('-o', '--output_path', help='output path')
    return parser.parse_args()

if __name__ == "__main__":

    args = parse_arguments()
    input_path = Path(args.input_path)
    if args.output_path:
        output_path = Path(args.output_path)

    if input_path.is_dir():
        input_files = input_path.rglob("*.txt")
    else:
        input_files = [input_path]

    num_successfully_processed = 0
    for curr_file in input_files:
        try:
            with open(curr_file, 'r', encoding='utf-8') as f:
                payload = {}
                for line in f.readlines():
                    # Split on the first colon. This assumes that no key
                    # contains a colon
                    key = clean_key(line[:line.index(':')].strip())
                    value = line[line.index(':')+1:].strip()

                    add_entry(payload, key, value)

                # Find keys that aren't in our list of expected keys, print out a
                # message regarding that, then remove them from the dictionary so elasticsearch doesn't
                # complain when ingesting
                outlier_keys = list(set(payload.keys()).difference(_keys))
                if len(outlier_keys) > 0:
                    print('Found new keys in {}: {}'.format(str(curr_file), outlier_keys))
                    for key in outlier_keys:
                        payload.pop(key)

            if args.output_path is None:
                out_file = curr_file.parent / (curr_file.stem + '.json')
            elif output_path.is_dir():
                out_file = output_path / (curr_file.stem + '.json')
            else:
                out_file = output_path
            with open( out_file, 'w') as f:
                # ensure_ascii=False ensures the unicode character dont get decoded
                json.dump(payload, f, indent=2, sort_keys=True, ensure_ascii=False)
            num_successfully_processed += 1
        except Exception as e:
            print("ERROR: failed to convert", str(curr_file))

    print('successfully processed {} files...'.format(num_successfully_processed))
