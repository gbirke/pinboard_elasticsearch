#!/bin/bash

curl --head --silent --fail 'localhost:9200/pinboard'
if [ $? -eq 0 ]; then
    curl -XDELETE 'localhost:9200/pinboard/?pretty'
fi

# Create mappings
curl -XPUT 'localhost:9200/pinboard/?pretty' -H "Content-Type: application/json" -d@mapping.json

if [ -f posts.ndjson ]; then
    curl -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/pinboard/_doc/_bulk --data-binary "@posts.ndjson"
fi
