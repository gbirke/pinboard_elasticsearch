# Example queries
The queries in this folder replicate the Python examples. They are for testing.

## Set up index and mapping

    curl -XPUT 'localhost:9200/pinboard_json?pretty"
    curl -XPUT 'localhost:9200/pinboard_json/_mapping/post?pretty' -d@queries/mapping.json

## Import document
    curl -XPOST 'localhost:9200/pinboard_json/post?pretty' -d@queries/post_document.json

## Delete document
    curl -XDELETE 'localhost:9200/pinboard_json/post/09f4b04da9d9249e501aa5a3f145f273?q=*&pretty'

