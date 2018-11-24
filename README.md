# Import Pinboard data into Elasticsearch

Prerequisites:
* An Elasticsearch instance running at localhost:9200
* curl
* [jq](https://stedolan.github.io/jq/)

## Set up index and mapping

    curl -XPUT 'localhost:9200/pinboard/?pretty' -H "Content-Type: application/json" -d@mapping.json

## Delete index (to create new mapping)

    curl -XDELETE 'localhost:9200/pinboard/?pretty'

## Import document
```bash
curl -XPOST 'localhost:9200/pinboard/_doc/1?pretty' -H "Content-Type: application/json" -d@post_document.json
```

## Delete document
    curl -XDELETE 'localhost:9200/pinboard/post/1?pretty'

## Download Pinboard tags (for testing)

    curl 'https://api.pinboard.in/v1/posts/get?auth_token=archangel:XXX&format=json&dt=2018-11-23' > posts.json

Replace the `XXX` placeholder with your API token.

## Convert JSON result set to bulk format

    jq --from-file posts2bulk.jq -c  posts.json > posts.ndjson

## Post bulk data
```bash
curl -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/pinboard/_doc/_bulk --data-binary "@posts.ndjson"
```

See https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-bulk.html
