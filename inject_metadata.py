#!/usr/bin/env python3

"""
Accept a template schema on stdin and inject default metadata fields
before writing to stdout.
"""

import json
import sys

if __name__ == "__main__":
    # TODO: Actually parse arguments; we currently assume that the filepath
    # of the schema is passed as argv[1].
    fileparts = sys.argv[1].split('/')

    # Prepare some default metadata if not overridden in the template schema.
    bq_dataset = fileparts[0].replace('-', '_')
    doctype = fileparts[1].replace('-', '_')
    version = fileparts[2].split('.')[1]
    bq_table = '{}_v{}'.format(doctype, version)

    # Parse the schema and inject default metadata fields.
    schema = json.load(sys.stdin)
    meta = schema.setdefault('mozPipelineMetadata', {})
    meta.setdefault('bq_dataset', bq_dataset)
    meta.setdefault('bq_table', bq_table)

    # Output.
    json.dump(schema, sys.stdout, sort_keys=True, indent=2)

    # Make sure we end the file with a newline.
    print('')
