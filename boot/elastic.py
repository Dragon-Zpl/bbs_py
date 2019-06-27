
from elasticsearch import Elasticsearch

from conf.conf import ELASTIC_CONF
es_client = None


def init_es_cli():
    global es_client

    es_client = Elasticsearch(ELASTIC_CONF,timeout=100)
    return

