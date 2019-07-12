import datetime
from etcd3 import client
from services.Log.logs import *
path = './' + str(datetime.datetime.now().strftime('%Y-%m-%d')) + '_log.txt'
log = Log(file_path=path, level='info')

e_client = client(
    host="192.168.183.103",
    port=2379,
)
