import os

import numpy as np
import pandas as pd
from services.decorators.decorator import Decorators_time
from conf.conf import FILE_PATH
from helper.error.error import PathError

@Decorators_time
def read_file(file_path=""):
    """
    read thread info csv
    :return:
        thread_base: type ndarray [thread_id, thread_topicid]
        thread_data: type ndarray thread info
        thread_data_notime type ndarray  thread info without thread create time
    """
    if file_path == "":
        raise PathError("文件路劲不能为空")
    if not os.path.exists(file_path):
        raise PathError("csv 文件不存在" + file_path)
    pd_data = pd.read_csv(file_path, delimiter=',', header=None)
    data = np.array(pd_data)
    fields = data[0, :][3:]
    weights = [float(i) for i in data[1, :][3:]]
    data = np.array(pd.read_csv(file_path, delimiter=',')[1:])

    where_are_nan = np.isnan(data)
    where_are_inf = np.isinf(data)
    data[where_are_nan] = 0
    data[where_are_inf] = 1
    thread_base, thread_data = np.hsplit(data, [3])
    thread_data_notime, tmp_data = np.hsplit(thread_data, [-1])
    return thread_base, thread_data, thread_data_notime, fields, weights


if __name__ == '__main__':
    t1,t2,t3,t4,t5 = read_file('./must_createTime_-30favorite_replies_.csv')
    print(t1)
    print(t2)
    print(t3)
    print(t4)
    print(t5)
