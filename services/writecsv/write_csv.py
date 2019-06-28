import csv
import datetime
from conf.conf import CSV_FILE_NAME, CSV_FILE_NAME_NOTIME

def Write_Csv(datas,score_datas,fields):
    file_name = CSV_FILE_NAME + str(datetime.datetime.now().strftime('%Y-%m-%d')) + '.csv'
    csv_file = open(file_name, "a+", encoding="utf-8", newline='')
    writer = csv.writer(csv_file)
    fields_list = ['tid_url', 'topicid', 'score']
    for field in fields:
        fields_list.append(field)
    writer.writerow(fields_list)
    for data, score_data in zip(datas,score_datas):
        data = list(data)
        score_data = list(score_data)
        score_data[0] = "https://bbs.feng.com/read-htm-tid-" + str(int(float(score_data[0]))) + ".html"
        score_data.extend(data)
        writer.writerow(score_data)

def Write_Csv_notime(datas,score_datas,fields):
    file_name = CSV_FILE_NAME_NOTIME + str(datetime.datetime.now().strftime('%Y-%m-%d')) + '.csv'
    csv_file = open(file_name, "a+", encoding="utf-8", newline='')
    writer = csv.writer(csv_file)
    fields_list = ['tid_url', 'topicid', 'score']
    for field in fields:
        fields_list.append(field)
    writer.writerow(fields_list)
    for data, score_data in zip(datas,score_datas):
        data = list(data)
        score_data = list(score_data)
        score_data[0] = "https://bbs.feng.com/read-htm-tid-" + str(int(float(score_data[0]))) + ".html"
        score_data.extend(data)
        writer.writerow(score_data)