# Example queries
The queries in this folder replicate the Python examples. They are for testing.

## Set up index and mapping

    curl -XPUT 'localhost:9200/pinboard/?pretty' -H "Content-Type: application/json" -d@queries/mapping.json

## Delete index (to create new mapping)

    curl -XDELETE 'localhost:9200/pinboard/?pretty'

## Import document
    curl -XPOST 'localhost:9200/pinboard/_doc/1?pretty' -H "Content-Type: application/json" -d@queries/post_document.json

## Delete document
    curl -XDELETE 'localhost:9200/pinboard/post/1?pretty'
