# ElasticSearch importer for Pinboard posts

This a a collection of small Python scripts to import Pinboard posts in ElasticSearch.

## Usage
Until these scripts have developed into a coherent update process, you'll have to manually call three scripts:

    python init_el.py

This sets up the ElasticSearch index and mapping. The following command downloads all your pinboard posts and stores them in a file:

    python pinboard_load.py YOUR_PINBOARD_API_TOKEN

The file storage is for develpoing the mapping and post scripts so when indexing goes wrong or you change the mapping you don't have to re-download them and run into the rate limit.

Finally store all the posts form the file in Elasticsearch:

    python post_el.py


## Pinboard library
Pinboard library is from https://github.com/mgan59/python-pinboard