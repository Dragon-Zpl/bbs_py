from util import e_client
from conf.conf import ADD_SCORE

def GetScoreData():
    datas, none = e_client.get("/weiphone/thread_scor2e")
    if datas is None:
        return none
    datas = eval(datas.decode('utf-8'))
    return datas

def SwapScore(etcd_key ,datas):
    last_datas = GetScoreData()
    datas = datas.strip("[").strip("]")
    datas = datas.replace("'",'"')
    if last_datas is not None:
        for k in datas.keys():
            if k not in last_datas.keys():
                datas[k] += ADD_SCORE
    e_client.put(etcd_key ,datas)


