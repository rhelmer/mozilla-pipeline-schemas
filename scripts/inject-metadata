#!/usr/bin/env python3

"""
Accept a template schema on stdin and inject default metadata fields
before writing to stdout.
"""

import argparse
import json
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('target')
    args = parser.parse_args()

    fileparts = args.target.split('/')

    # Prepare some default metadata if not overridden in the template schema.
    bq_dataset_family = fileparts[0].replace('-', '_')
    doctype = fileparts[1].replace('-', '_')
    version = fileparts[2].split('.')[1]
    bq_table = '{}_v{}'.format(doctype, version)

    # Parse the schema and inject default metadata fields.
    schema = json.load(sys.stdin)
    meta = schema.setdefault('mozPipelineMetadata', {})
    meta.setdefault('bq_dataset_family', bq_dataset_family)
    meta.setdefault('bq_table', bq_table)
    meta.setdefault('uri_scheme', 'structured')

    # Output.
    json.dump(schema, sys.stdout, sort_keys=True, indent=2)

    # Make sure we end the file with a newline.
    print('')
