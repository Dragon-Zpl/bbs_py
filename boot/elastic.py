
from elasticsearch import Elasticsearch

from conf.conf import ELASTIC_CONF

es_client = Elasticsearch(ELASTIC_CONF)

