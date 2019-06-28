import datetime
from conf.conf import ES_INDEX, ES_INDEX_NOTIME


class WriteEs:
    def __init__(self, es_cli, thread_data, thread_data_notime, fields):
        self._esCli = es_cli
        self._thread_data = thread_data
        self._thread_data_notime = thread_data_notime
        self._fields = fields

    def write_thread_score_to_es(self, thread_score):
        """
        将帖子得分信息写到es
        :param thread_score: list [thread_id, thread_topic, thread_score]
        :return:
        """
        try:
            doc = []
            index = ES_INDEX + str(datetime.datetime.now().strftime('%Y-%m-%d'))
            for i in range(len(thread_score)):
                data_dic = {}
                doc.append({"index": {}})
                data_dic["tid"] = thread_score[i][0]
                data_dic["topicid"] = thread_score[i][1]
                data_dic["score"] = thread_score[i][2]
                for j in range(len(self._fields)):
                    data_dic[self._fields[j]] = self._thread_data[i][j]
                doc.append(data_dic)
                if i % 5000 == 0 and i != 0:
                    self._esCli.bulk(index=index, body=doc, doc_type="_doc")
                    doc = []
                if i == len(thread_score) - 1:
                    self._esCli.bulk(index=index, body=doc, doc_type="_doc")
        except Exception as e:
            print(e)

    def write_thread_score_notime_to_es(self, thread_score):
        """
        将帖子得分信息（不具备时效性）写到es
        :param thread_score: thread_score: list [thread_id, thread_topic, thread_score]
        :return:
        """
        try:
            doc = []
            index = ES_INDEX_NOTIME + str(datetime.datetime.now().strftime('%Y-%m-%d'))
            for i in range(len(thread_score)):
                data_dic = {}
                doc.append({"index": {}})
                data_dic["tid"] = thread_score[i][0]
                data_dic["topicid"] = thread_score[i][1]
                data_dic["score"] = thread_score[i][2]
                for j in range(len(self._fields[:-1])):
                    data_dic[self._fields[j]] = self._thread_data_notime[i][j]
                doc.append(data_dic)
                if i % 1000 == 0 and i != 0:
                    self._esCli.bulk(index=index, body=doc, doc_type="_doc")
                    doc = []
                if i == len(thread_score) - 1:
                    self._esCli.bulk(index=index, body=doc, doc_type="_doc")
        except Exception as e:
            print(e)
