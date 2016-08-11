# Insert Pinboard posts into Elasticsearch

import pinboard_load
import pickle
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

es = Elasticsearch()

def test1():
	""" Test normal posting interface and interaction with PostWrapper"""
	post = pinboard_load.get_posts(date="2014-10-29", count=1).next()
	es.create(**post)

def dummy_post():
	return {'body': {u'description': u'Get your old iPad ready for sale in 5 easy steps',
	          u'extended': u'',
	          u'href': u'http://www.iphonehacks.com/2013/11/ipad-ready-for-sale.html',
	          u'tags': [u'iOS', u'ipad'],
	          u'time': u'2014-10-29T07:26:20Z',
	          u'hash': u'09f4b04da9d9249e501aa5a3f145f273',
	          u'toread': False},
	 'doc_type': 'post',
	 'index': 'pinboard',
	 'id': u'09f4b04da9d9249e501aa5a3f145f273'
	}

def test2():
	""" Test normal posting interface with defined data"""
	post = dummy_post()
	print es.create(**post)

def test3():
	""" Load all pickled post data into Elasticsearch with bulk API"""
	post_data = pickle.load(open("posts.p", "rb"))
	#post_data = [dummy_post()["body"]]
	posts = pinboard_load.BulkPostWrapper(post_data, {"_index":"pinboard", "_type":"post"})
	print bulk(es, posts)

if __name__ == '__main__':
	#es.indices.refresh("pinboard")
	test3()