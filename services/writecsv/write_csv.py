import csv
import datetime
import time

from services.decorators.decorator import Decorators_time
from conf.conf import SAVE_CSV_DIR_PATH

@Decorators_time
def Write_Csv(datas, score_datas, fields, filename):
    file_name = SAVE_CSV_DIR_PATH + '/' + filename + '_' + str(datetime.datetime.now().strftime('%Y-%m-%d')) + '.csv'
    csv_file = open(file_name, "a+", encoding="utf-8", newline='')
    writer = csv.writer(csv_file)
    fields_list = ['tid_url', 'topicid', 'create_time', 'score']
    for field in fields:
        fields_list.append(field)
    writer.writerow(fields_list)
    for data, score_data in zip(datas, score_datas):
        data = list(data)
        score_data = list(score_data)
        score_data[0] = "https://bbs.feng.com/read-htm-tid-" + str(int(float(score_data[0]))) + ".html"
        timeArray = time.localtime(int(score_data[2]))
        score_data[2] = str(time.strftime("%Y--%m--%d %H:%M:%S", timeArray))
        score_data.extend(data)
        writer.writerow(score_data)

@Decorators_time
def Write_Csv_notime(datas, score_datas, fields, filename):
    file_name = SAVE_CSV_DIR_PATH + '/' + filename + '_' + str(datetime.datetime.now().strftime('%Y-%m-%d')) + '.csv'
    csv_file = open(file_name, "a+", encoding="utf-8", newline='')
    writer = csv.writer(csv_file)
    fields_list = ['tid_url', 'topicid', 'create_time', 'score']
    for field in fields:
        fields_list.append(field)
    writer.writerow(fields_list)
    for data, score_data in zip(datas, score_datas):
        data = list(data)
        score_data = list(score_data)
        score_data[0] = "https://bbs.feng.com/read-htm-tid-" + str(int(float(score_data[0]))) + ".html"
        timeArray = time.localtime(int(score_data[2]))
        score_data[2] = str(time.strftime("%Y--%m--%d %H:%M:%S", timeArray))
        score_data.extend(data)
        writer.writerow(score_data)
