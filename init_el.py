# Initialize elasticsearch index for pinboard

from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

INDEX_NAME = "pinboard"

if not es.indices.exists(index=INDEX_NAME):
	es.indices.create(index=INDEX_NAME)

post_mapping = {
	"_timestamp": { 
		"enabled": True,
		"path": "time"
	},
	"_id": {
		"path": "hash"
	},
	"dynamic": "strict",
	"properties": {
		"description": {"type" : "string"},
		"extended": {"type" : "string"},
		"tags": {
			"type" : "string",
			"fields": {
				"cnt": {
					"type" : "token_count",
                    "store" : "yes",
                    "analyzer" : "standard"
				}
			}
		},
		"href": {"type" : "string"},
		"unread": {"type": "boolean"},
		"shared": {"type": "boolean"},
		"hash": {"type": "string", "index": "not_analyzed" },
		"meta": {"type": "string", "index": "not_analyzed" },
		"time": {"type": "date"}
	}
}
es.indices.put_mapping(index=INDEX_NAME, doc_type="post", body=post_mapping)