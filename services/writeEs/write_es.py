import datetime


class WriteEs:
    def __init__(self, es_cli, thread_data, thread_data_notime):
        self._esCli = es_cli
        self._thread_data = thread_data
        self._thread_data_notime = thread_data_notime

    def write_thread_score_to_es(self, thread_score):
        """
        将帖子得分信息写到es
        :param thread_score: list [thread_id, thread_topic, thread_score]
        :return:
        """
        try:
            doc = []
            index = "bbs_score_data_" + str(datetime.datetime.now().strftime('%Y-%m-%d'))
            for i in range(len(thread_score)):
                data_dic = {}
                doc.append({"index": {}})
                data_dic["tid"] = thread_score[i][0]
                data_dic["topicid"] = thread_score[i][1]
                data_dic["score"] = thread_score[i][2]
                data_dic["replies"] = self._thread_data[i][0]
                data_dic["favorite"] = self._thread_data[i][1]
                data_dic["support"] = self._thread_data[i][2]
                data_dic["historyPV"] = self._thread_data[i][3]
                data_dic["yesterdayPV"] = self._thread_data[i][4]
                data_dic["yesterdayUV"] = self._thread_data[i][5]
                data_dic["dateline"] = self._thread_data[i][6]
                doc.append(data_dic)
                if i % 1000 == 0 and i != 0:
                    self._esCli.bulk(index=index, body=doc, doc_type="thread_data")
                    doc = []
                if i == len(thread_score) - 1:
                    self._esCli.bulk(index=index, body=doc, doc_type="thread_data")
        except Exception as e:
            pass

    def write_thread_score_notime_to_es(self, thread_score):
        """
        将帖子得分信息（不具备时效性）写到es
        :param thread_score: thread_score: list [thread_id, thread_topic, thread_score]
        :return:
        """
        try:
            doc = []
            index = "bbs_score_data_notime_" + str(datetime.datetime.now().strftime('%Y-%m-%d'))
            for i in range(len(thread_score)):
                data_dic = {}
                doc.append({"index": {}})
                data_dic["tid"] = thread_score[i][0]
                data_dic["topicid"] = thread_score[i][1]
                data_dic["score"] = thread_score[i][2]
                data_dic["replies"] = self._thread_data_notime[i][0]
                data_dic["favorite"] = self._thread_data_notime[i][1]
                data_dic["support"] = self._thread_data_notime[i][2]
                data_dic["historyPV"] = self._thread_data_notime[i][3]
                data_dic["yesterdayPV"] = self._thread_data_notime[i][4]
                data_dic["yesterdayUV"] = self._thread_data_notime[i][5]
                doc.append(data_dic)
                if i % 1000 == 0 and i != 0:
                    self._esCli.bulk(index=index, body=doc, doc_type="thread_data_notime")
                    doc = []
                if i == len(thread_score) - 1:
                    self._esCli.bulk(index=index, body=doc, doc_type="thread_data_notime")
        except Exception as e:
            pass