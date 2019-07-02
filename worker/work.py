from conf.conf import LISTING_DIR_PATH
from services.read.read import read_file
from services.calculation.calcute import CalScore
from services.writeEs.write_es import WriteEs
from boot.elastic import es_client
from services.Listing import *
from services.writecsv.write_csv import *
from util import log
from services.decorators.decorator import Decorators_time


@Decorators_time
def run(file_path):
    # log.INFO('start')
    now_time = datetime.datetime.now()
    thread_base, thread_data, thread_data_notime, fields, weights = read_file('./csv_datas/' + file_path)
    read_time = datetime.datetime.now()
    # log.INFO("读取csv时间：" + str(read_time - now_time))
    cal_score = CalScore(thread_base, thread_data, thread_data_notime, weights)
    score = cal_score.cal_with_timely()
    score_notime = cal_score.cal_without_timely()
    cal_time = datetime.datetime.now()
    # log.INFO("算分时间：" + str(cal_time - read_time))
    # print('insert es')
    # write_es = WriteEs(es_client, thread_data, thread_data_notime, fields)
    # write_es.write_thread_score_notime_to_es(score_notime)
    # write_es.write_thread_score_to_es(score)
    # es_time = datetime.datetime.now()
    # print("写入es时间："+str(es_time-cal_time))
    # log.INFO('write csv')
    file_name = str(file_path).split(".")[0]
    Write_Csv(thread_data, score, fields, file_name)
    file_name = file_name + "_notime"
    Write_Csv_notime(thread_data_notime, score_notime, fields, file_name)
    csv_time = datetime.datetime.now()
    # log.INFO("写入csv时间：" + str(csv_time - cal_time))
    # log.INFO('end')


# 定时 run
def cron():
    listing_file(LISTING_DIR_PATH, run)


if __name__ == '__main__':
    cron()
