import time

import os


def listing_file(file_path, func):
    filemt = time.localtime(os.stat(file_path).st_mtime)
    last_update_time = time.strftime("%Y-%m-%d-%H-%M", filemt)

    while True:
        filemt = time.localtime(os.stat(file_path).st_mtime)
        now_update_time = time.strftime("%Y-%m-%d-%H-%M", filemt)

        if now_update_time != last_update_time:
            print("running")
            func()
            last_update_time = now_update_time
        time.sleep(60*30)