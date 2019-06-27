import os

import numpy as np
import pandas as pd


from conf.conf import FILE_PATH
from helper.error.error import PathError


def read_file(file_path=""):
    """
    read thread info csv
    :return:
        thread_base: type ndarray [thread_id, thread_topicid]
        thread_data: type ndarray thread info
        thread_data_notime type ndarray  thread info without thread create time
    """
    if file_path == "":
        file_path = FILE_PATH
    if not os.path.exists(file_path):
        raise PathError("csv 文件不存在")

    data = np.array(pd.read_csv(file_path, delimiter=',',dtype=float))

    where_are_nan = np.isnan(data)
    data[where_are_nan] = 0
    thread_base, thread_data = np.hsplit(data, [2])
    thread_data_notime, tmp_data = np.hsplit(thread_data, [-1])
    return thread_base, thread_data, thread_data_notime


if __name__ == '__main__':
    read_file()