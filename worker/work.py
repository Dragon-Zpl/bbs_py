from conf.conf import FILE_PATH
from services.read.read import read_file
from services.calculation.calcute import CalScore
from services.writeEs.write_es import WriteEs
from boot.elastic import es_client
from services.Listing import *
from services.writecsv.write_csv import *

def run():
    print('start')
    now_time = datetime.datetime.now()
    thread_base, thread_data, thread_data_notime, fields, weights = read_file(FILE_PATH)
    read_time = datetime.datetime.now()
    print("读取csv时间："+str(read_time-now_time))
    cal_score = CalScore(thread_base, thread_data, thread_data_notime, weights)
    score = cal_score.cal_with_timely()
    score_notime = cal_score.cal_without_timely()
    cal_time = datetime.datetime.now()
    print("算分时间："+str(cal_time-read_time))
    print('insert es')
    write_es = WriteEs(es_client, thread_data, thread_data_notime, fields)
    write_es.write_thread_score_notime_to_es(score_notime)
    write_es.write_thread_score_to_es(score)
    es_time = datetime.datetime.now()
    print("写入es时间："+str(es_time-cal_time))
    print('write csv')
    Write_Csv(thread_data,score)
    Write_Csv_notime(thread_data_notime,score_notime)
    csv_time = datetime.datetime.now()
    print("写入csv时间："+str(csv_time-es_time))
    print('end')

# 定时 run
def cron():
    run()
    listing_file(FILE_PATH, run)


if __name__ == '__main__':
    cron()

