import csv
import datetime

def Write_Csv(datas,score_datas):
    file_name = "bbs_score_data_" + str(datetime.datetime.now().strftime('%Y-%m-%d')) + '.csv'
    csv_file = open(file_name, "a+", encoding="utf-8", newline='')
    writer = csv.writer(csv_file)
    writer.writerow(['tid_url', 'topicid', 'score', 'replies', 'favorite', 'support', 'historyPV', 'yesterdayPV', 'yesterdayUV', 'dateline'])
    for data, score_data in zip(datas,score_datas):
        data = list(data)
        score_data = list(score_data)
        score_data[0] = "https://bbs.feng.com/read-htm-tid-" + str(int(float(score_data[0]))) + ".html"
        score_data.extend(data)
        print(score_data)
        writer.writerow(score_data)

def Write_Csv_notime(datas,score_datas):
    file_name = "bbs_score_data_notime_" + str(datetime.datetime.now().strftime('%Y-%m-%d')) + '.csv'
    csv_file = open(file_name, "a+", encoding="utf-8", newline='')
    writer = csv.writer(csv_file)
    writer.writerow(['tid_url', 'topicid', 'score', 'replies', 'favorite', 'support', 'historyPV', 'yesterdayPV', 'yesterdayUV'])
    for data, score_data in zip(datas,score_datas):
        data = list(data)
        score_data = list(score_data)
        score_data[0] = "https://bbs.feng.com/read-htm-tid-" + str(int(float(score_data[0]))) + ".html"
        score_data.extend(data)
        print(score_data)
        writer.writerow(score_data)