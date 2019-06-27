from conf.conf import FILE_PATH
from services.read.read import read_file
from services.calculation.calcute import CalScore
from services.writeEs.write_es import WriteEs
from boot.elastic import es_client
from services.Listing import *

def run():
    thread_base, thread_data, thread_data_notime, fields, weights = read_file(FILE_PATH)
    cal_score = CalScore(thread_base, thread_data, thread_data_notime, weights)

    score = cal_score.cal_with_timely()
    score_notime = cal_score.cal_without_timely()

    write_es = WriteEs(es_client, thread_data, thread_data_notime, fields)
    write_es.write_thread_score_notime_to_es(score_notime)
    write_es.write_thread_score_to_es(score)


# 定时 run
def cron():
    listing_file(FILE_PATH, run)

if __name__ == '__main__':
    cron()