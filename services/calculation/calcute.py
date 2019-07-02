import numpy as np

from sklearn.preprocessing import StandardScaler
from services.decorators.decorator import Decorators_time

class CalScore:
    def __init__(self, thread_base, thread_data, thread_data_notime, weights):
        self._thread_base = thread_base
        self._thread_data = thread_data
        self._thread_data_notime = thread_data_notime
        self._scaler = StandardScaler()
        self._weights = weights

    @Decorators_time
    def cal_with_timely(self):
        """
        算分（具备时效性）
        :param thread_base : thread_id thread_topic_id
        :param thread_data: thread info
        :return:  list [thread_id, thread_topic_id, thread_score]
        """
        # [0.229046, 0.212894, 0.180076, 0.166511, 0.130550, 0.080924, -0.016670]
        # todo read mysql get weight
        weight = np.array(self._weights)
        # if np.shape(self._thread_data)[1] != np.shape(weight)[0]:
        #     raise Exception("weight not legal")
        # assert np.shape(self._thread_data)[1] == np.shape(weight)[0], "weight not legal"

        self._scaler.fit(self._thread_data)
        std_data = self._scaler.transform(self._thread_data)

        score = np.dot(std_data, weight)
        score = score.reshape((-1, 1))
        finally_data = np.hstack((self._thread_base, score))
        for data in finally_data:
            data[0] = int(data[0])
            data[1] = int(data[1])
            data[2] = round(data[2], 3)
        return finally_data.tolist()

    @Decorators_time
    def cal_without_timely(self):
        """
        算分（不具备时效性）
        :param thread_base : thread_id thread_topic_id
        :param thread_data: thread info without thread create time
        :return:  list [thread_id, thread_topic_id, thread_score]
        """
        weight = np.array(self._weights[:-1])  # todo read mysql get weight
        # if np.shape(self._thread_data)[1] != np.shape(weight)[0]:
        #     raise Exception("weight not legal")
        # assert np.shape(self._thread_data)[1] == np.shape(weight)[1], "weight not legal"

        self._scaler.fit(self._thread_data_notime)
        std_data = self._scaler.transform(self._thread_data_notime)

        score = np.dot(std_data, weight)
        score = score.reshape((-1, 1))
        finally_data = np.hstack((self._thread_base, score))
        for data in finally_data:
            data[0] = int(data[0])
            data[1] = int(data[1])
            data[2] = round(data[2], 3)
        return finally_data.tolist()
