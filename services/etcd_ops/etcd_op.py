from util import e_client
from conf.conf import ADD_SCORE
import json


def GetScoreData():
    datas, none = e_client.get("/weiphone/thread_score_all")
    if datas is None:
        return none
    datas = eval(datas.decode('utf-8'))
    return datas


def SwapScore(etcd_key, datas):
    last_datas = GetScoreData()
    if last_datas is not None:
        for k in datas.keys():
            if k not in last_datas.keys():
                datas[k] += ADD_SCORE
    datas_list = sorted(datas, key=lambda x: x[1], reverse=True)[:800]
    e_client.put("/weiphone/thread_score_all", json.dumps(datas))
    datas = {}
    for i in datas_list:
        datas[i[0]] = i[1]

    e_client.put(etcd_key, json.dumps(datas))
