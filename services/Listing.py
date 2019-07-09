from __future__ import print_function
import time
import os
from util import log
from services.sendemail.send_email import SMTP
from services.tarfile.tar_file import *
from conf.conf import SAVE_CSV_DIR_PATH, LISTING_DIR_PATH
import asyncio
import base64
import logging
import os
import shutil
import sys
from datetime import datetime
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


WATCH_PATH = '/deploy/source_csv'  # 监控目录



# def test(csv_path):
#     log.INFO('now_csv:' + str(csv_path))
#
#
# def listing_file(file_path, func):
#     filemt = time.localtime(os.stat(file_path).st_mtime)
#     last_update_time = time.strftime("%Y-%m-%d-%H-%M", filemt)
#     log.INFO("last_update_time:" + str(last_update_time))
#     while True:
#         filemt = time.localtime(os.stat(file_path).st_mtime)
#         now_update_time = time.strftime("%Y-%m-%d-%H-%M", filemt)
#         if now_update_time != last_update_time:
#             log.INFO("running")
#             for csv_path in os.listdir(file_path):
#                 if ".csv" in csv_path:
#                     run(csv_path)
#             zipDir(SAVE_CSV_DIR_PATH, "./data.zip")
#             t = SMTP()
#             t.send_email_("15260826071@163.com", "./data.zip")
#             os.remove("./data.zip")
#             for i in os.listdir(SAVE_CSV_DIR_PATH):
#                 os.remove(SAVE_CSV_DIR_PATH + "/" + i)
#             last_update_time = now_update_time
#             log.INFO("change_last_update_time:" + str(last_update_time))
#         time.sleep(5)


class FileMonitorHandler(FileSystemEventHandler):
    def __init__(self, func, **kwargs):
        super(FileMonitorHandler, self).__init__(**kwargs)
        # 监控目录 目录下面以device_id为目录存放各自的图片
        self._watch_path = WATCH_PATH
        self.func = func
    # 重写文件改变函数，文件改变都会触发文件夹变化

    def on_modified(self, event):
        log.INFO("文件发生变化")
        if not event.is_directory:
            # 文件改变都会触发文件夹变化
            file_path = event.src_path
            if "listen" in str(file_path):
                log.INFO("running")
                with open("/deploy/source_csv/listen.txt", 'r') as fp:
                    field_number = int(fp.read())
                for csv_path in os.listdir(LISTING_DIR_PATH):
                    if ".csv" in csv_path:
                        self.func(csv_path, field_number)
                zipDir(SAVE_CSV_DIR_PATH, "./data.zip")
                t = SMTP()
                t.send_email_("15260826071@163.com", "./data.zip")
                # t.send_email_("weiming.lin@office.feng.com", "./data.zip")
                # t.send_email_("rumin.liu@office.feng.com", "./data.zip")
                # t.send_email_("ran.huo@office.feng.com", "./data.zip")
                os.remove("./data.zip")
                for i in os.listdir(SAVE_CSV_DIR_PATH):
                    os.remove(SAVE_CSV_DIR_PATH + "/" + i)


# if __name__ == "__main__":
#     event_handler = FileMonitorHandler()
#     observer = Observer()
#     observer.schedule(event_handler, path=WATCH_PATH, recursive=True)  # recursive递归的
#     observer.start()
#     observer.join()
#
#
# if __name__ == '__main__':
#     listing_file("../get_csv_data", test)
