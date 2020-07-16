#!/usr/bin/env python3

import json
import sys

if __name__ == "__main__":
    print(sys.argv, file=sys.stderr)
    fileparts = sys.argv[1].split('/')
    bq_dataset = fileparts[0].replace('-', '_')
    doctype = fileparts[1].replace('-', '_')
    version = fileparts[2].split('.')[1]
    bq_table = '{}_v{}'.format(doctype, version)
    schema = json.load(sys.stdin)
    meta = schema.setdefault('mozPipelineMetadata', {})
    meta.setdefault('bq_dataset', bq_dataset)
    meta.setdefault('bq_table', bq_table)
    json.dump(schema, sys.stdout, sort_keys=True, indent=2)
    print('')
