

class WriteEs:
    def __init__(self, es_cli):
        self._esCli = es_cli

    def write_thread_score_to_es(self, thread_score):
        """
        将帖子得分信息写到es
        :param thread_score: list [thread_id, thread_topic, thread_score]
        :return:
        """
        pass

    def write_thread_score_notime_to_es(self, thread_score):
        """
        将帖子得分信息（不具备时效性）写到es
        :param thread_score: thread_score: list [thread_id, thread_topic, thread_score]
        :return:
        """
        pass