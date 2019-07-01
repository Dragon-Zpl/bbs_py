import time
from conf.conf import SAVE_CSV_DIR_PATH
import os

from services.sendemail.send_email import SMTP
from services.tarfile.tar_file import *

def test(csv_path):
    print('now_csv:'+str(csv_path))

def listing_file(file_path, func):
    filemt = time.localtime(os.stat(file_path).st_mtime)
    last_update_time = time.strftime("%Y-%m-%d-%H-%M", filemt)
    print("last_update_time:"+str(last_update_time))
    while True:
        filemt = time.localtime(os.stat(file_path).st_mtime)
        now_update_time = time.strftime("%Y-%m-%d-%H-%M", filemt)
        if now_update_time != last_update_time:
            print("running")
            for csv_path in os.listdir(file_path):
                if ".csv" in csv_path:
                    func(csv_path)
            zipDir(SAVE_CSV_DIR_PATH, "./test.zip")
            t = SMTP()
            t.send_email_("15260826071@163.com","./test.zip")
            last_update_time = now_update_time
            print("change_last_update_time:" + str(last_update_time))
        time.sleep(5)



if __name__ == '__main__':
    listing_file(r"C:\Users\Administrator.sz-pc-ljg-PC\Desktop\test", test)