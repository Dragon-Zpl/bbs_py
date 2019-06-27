import os
import time

from services.writecsv.write_csv import *
from services.read.read import read_file
from services.calculation.calcute import CalScore
from services.writeEs.write_es import WriteEs
from boot.elastic import es_client
import datetime


def test_read_file():
    thread_base, thread_data, thread_data_notime = read_file("datasource(3).csv")
    # print("thread_base:"+str(thread_base))
    print("thread_data:" + str(thread_data))
    # print("thread_data_notime:" + str(thread_data_notime))


def test_cal():
    thread_base, thread_data, thread_data_notime = read_file("datasource(3).csv")
    cal_score = CalScore(thread_base, thread_data, thread_data_notime)
    score = cal_score.cal_with_timely()
    score_notime = cal_score.cal_without_timely()
    doc = []
    index = "bbs_score_data_" + str(datetime.datetime.now().strftime('%Y-%m-%d'))
    for i in range(len(score)):
        data_dic = {}
        doc.append({"index": {}})
        data_dic["tid"] = score[i][0]
        data_dic["topicid"] = score[i][1]
        data_dic["score"] = score[i][2]
        data_dic["replies"] = thread_data[i][0]
        data_dic["favorite"] = thread_data[i][1]
        data_dic["support"] = thread_data[i][2]
        data_dic["historyPV"] = thread_data[i][3]
        data_dic["yesterdayPV"] = thread_data[i][4]
        data_dic["yesterdayUV"] = thread_data[i][5]
        data_dic["dateline"] = thread_data[i][6]
        doc.append(data_dic)
        if i % 1000 == 0 and i != 0:
            es_client.bulk(index=index, body=doc, doc_type="thread_data")
            doc = []
        if i == len(score) - 1:
            es_client.bulk(index=index, body=doc, doc_type="thread_data")
    doc = []
    index = "bbs_score_data_notime_" + str(datetime.datetime.now().strftime('%Y-%m-%d'))
    for i in range(len(score_notime)):
        data_dic = {}
        doc.append({"index": {}})
        data_dic["tid"] = score_notime[i][0]
        data_dic["topicid"] = score_notime[i][1]
        data_dic["score"] = score_notime[i][2]
        data_dic["replies"] = thread_data_notime[i][0]
        data_dic["favorite"] = thread_data_notime[i][1]
        data_dic["support"] = thread_data_notime[i][2]
        data_dic["historyPV"] = thread_data_notime[i][3]
        data_dic["yesterdayPV"] = thread_data_notime[i][4]
        data_dic["yesterdayUV"] = thread_data_notime[i][5]
        doc.append(data_dic)
        if i % 1000 == 0 and i != 0:
            es_client.bulk(index=index, body=doc, doc_type="thread_data_notime")
            doc = []
        if i == len(score) - 1:
            es_client.bulk(index=index, body=doc, doc_type="thread_data_notime")


def test_run():
    thread_base, thread_data, thread_data_notime = read_file("datasource(3).csv")
    cal_score = CalScore(thread_base, thread_data, thread_data_notime)
    score = cal_score.cal_with_timely()
    score_notime = cal_score.cal_without_timely()

    write_es = WriteEs(es_client, thread_data, thread_data_notime)
    write_es.write_thread_score_notime_to_es(score_notime)
    write_es.write_thread_score_to_es(score)


def test_csv():
    thread_base, thread_data, thread_data_notime = read_file("datasource(3).csv")
    cal_score = CalScore(thread_base, thread_data, thread_data_notime)
    score = cal_score.cal_with_timely()
    score_notime = cal_score.cal_without_timely()
    Write_Csv(thread_data, score)
    Write_Csv_notime(thread_data_notime, score_notime)


def test_listen(file_path):
    filemt = time.localtime(os.stat(file_path).st_mtime)
    last_update_time = time.strftime("%Y-%m-%d-%H-%M", filemt)
    while True:
        filemt = time.localtime(os.stat(file_path).st_mtime)
        now_update_time = time.strftime("%Y-%m-%d-%H-%M", filemt)
        if now_update_time != last_update_time:
            test_run()
            last_update_time = now_update_time
        time.sleep(60 * 30)


if __name__ == '__main__':
    test_csv()