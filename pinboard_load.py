# Load posts from Pinboard and convert them to iterables with formats fit for Elasticserach

import pinboard
import pickle

def get_posts(**kwargs):
	global PINBOARD_TOKEN
	pb = pinboard.open(token=PINBOARD_TOKEN)
	meta_dict = {"index":"pinboard", "doc_type":"post"}
	return PostWrapper(pb.posts(**kwargs), meta_dict) 

def store_all_posts():
	global PINBOARD_TOKEN
	pb = pinboard.open(token=PINBOARD_TOKEN)
	posts = pb.posts()
	pickle.dump(posts, open("posts.p", "wb"))

class PostWrapper(object):

	def __init__(self, posts, meta_dict={}):
		self.posts = iter(posts)
		self.meta_dict = meta_dict

	def __iter__(self):
		return self

	def next(self):
		try:
			post = self.posts.next()
			post.pop("time_parsed", None)
			if "tags" in post and len(post["tags"]) == 1 and post["tags"][0] == u"":
				post["tags"] = []
			return self.format_post(post)
		except StopIteration as e:
			raise e

	def format_post(self, post):
		wrap = self.meta_dict.copy()
		wrap.update({
			"body": post
		})
		return wrap

class BulkPostWrapper(PostWrapper):
	def format_post(self, post):
		wrap = self.meta_dict.copy()
		wrap.update({
			"_source": post,
			"_id": post["hash"],
			"_timestamp": post["time"]
		})
		return wrap	

if __name__ == '__main__':
	import pprint
	import sys
	try:
		PINBOARD_TOKEN = sys.argv[1]
	except IndexError:
		print "Error: No API token\n"
		print "Usage: {} PINBOARD_API_TOKEN".format(sys.argv[0])

	if len(sys.argv) > 2 and sys.argv[2] == "test":
		for p in get_posts(date="2014-10-29"):
			pprint.pprint(p)
	else:
		store_all_posts()



