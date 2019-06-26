
from services.read.read import read_file
from services.calculation.calcute import CalScore
from services.writeEs.write_es import WriteEs
from boot.elastic import es_client


def test_read_file():
    thread_base, thread_data, thread_data_notime = read_file("test.csv")


def test_cal():
    thread_base, thread_data, thread_data_notime = read_file("test.csv")
    cal_score = CalScore(thread_base, thread_data, thread_data_notime)
    score = cal_score.cal_with_timely()
    score_notime = cal_score.cal_without_timely()


def test_run():
    thread_base, thread_data, thread_data_notime = read_file("test.csv")
    cal_score = CalScore(thread_base, thread_data, thread_data_notime)
    score = cal_score.cal_with_timely()
    score_notime = cal_score.cal_without_timely()

    write_es = WriteEs(es_client)
    write_es.write_thread_score_notime_to_es(score_notime)
    write_es.write_thread_score_to_es(score)