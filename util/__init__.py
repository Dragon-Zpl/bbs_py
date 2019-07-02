import datetime

from services.Log.logs import *
path = '/deploy/logs/' + str(datetime.datetime.now().strftime('%Y-%m-%d')) + '_log.txt'
log = Log(file_path=path, level='info')