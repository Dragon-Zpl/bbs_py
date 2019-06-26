import numpy as np

from sklearn.preprocessing import StandardScaler


class CalScore:
    def __init__(self, thread_base, thread_data, thread_data_notime):
        self._thread_base = thread_base
        self._thread_data = thread_data
        self._thread_data_notime = thread_data_notime
        self._scaler = StandardScaler()

    def cal_with_timely(self):
        """
        算分（具备时效性）
        :param thread_base : thread_id thread_topic_id
        :param thread_data: thread info
        :return:  list [thread_id, thread_topic_id, thread_score]
        """
        weight = np.array([1, 2]) # todo read mysql get weight

        assert np.shape(self._thread_data)[1] == np.shape(weight)[1], "weight not legal"

        self._scaler.fit(self._thread_data)
        std_data = self._scaler.transform(self._thread_data)

        score = np.dot(std_data, weight)
        score = score.reshape((-1, 1))
        finally_data = np.hstack((self._thread_base, score))

        return finally_data.tolist()

    def cal_without_timely(self):
        """
        算分（不具备时效性）
        :param thread_base : thread_id thread_topic_id
        :param thread_data: thread info without thread create time
        :return:  list [thread_id, thread_topic_id, thread_score]
        """
        weight = np.array([1, 2, 3])  # todo read mysql get weight

        assert np.shape(self._thread_data)[1] == np.shape(weight)[1], "weight not legal"

        self._scaler.fit(self._thread_data_notime)
        std_data = self._scaler.transform(self._thread_data_notime)

        score = np.dot(std_data, weight)
        score = score.reshape((-1, 1))
        finally_data = np.hstack((self._thread_base, score))

        return finally_data.tolist()
