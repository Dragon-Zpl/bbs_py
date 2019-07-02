import sys

import os
import time

from conf.conf import *
LEVEL = {
    "debug": 1,
    "info": 2,
    "warning": 3,
    "error": 4,
    "critical": 5
}

class Log:
    def __init__(self, file_path=None, level=LOG_LEVEL):
        self._path = file_path
        self._level = level
        if self._path is not None:
            self.file_op = open(file=self._path, mode="a+")
        else:
            self.file_op = None

    def DEBUG(self, msg):
        if LEVEL[self._level] > 1:
            pass
        else:
            out = ""
            now_time = time.strftime('%Y.%m.%d %H:%M',time.localtime(time.time()))
            out += now_time + " - "
            file_name = os.path.basename(__file__)
            out += file_name + " - "
            line = sys._getframe().f_back.f_lineno
            out += str(line) + " - " + "DEBUG " + msg
            print(out)
            if self.file_op is not None:
                self.file_op.write(out+'\n')

    def INFO(self, msg):
        if LEVEL[self._level] > 2:
            pass
        else:
            out = ""
            now_time = time.strftime('%Y.%m.%d %H:%M',time.localtime(time.time()))
            out += now_time + " - "
            file_name = os.path.basename(__file__)
            out += file_name + " - "
            line = sys._getframe().f_back.f_lineno
            out += str(line) + " - " + "INFO " + msg
            print(out)
            if self.file_op is not None:
                self.file_op.write(out+'\n')

    def WARN(self, msg):
        if LEVEL[self._level] > 3:
            pass
        else:
            out = ""
            now_time = time.strftime('%Y.%m.%d %H:%M',time.localtime(time.time()))
            out += now_time + " - "
            file_name = os.path.basename(__file__)
            out += file_name + " - "
            line = sys._getframe().f_back.f_lineno
            out += str(line) + " - " + "WARNNING " + msg
            print(out)
            if self.file_op is not None:
                self.file_op.write(out+'\n')

    def ERROR(self, msg):
        if LEVEL[self._level] > 4:
            pass
        else:
            out = ""
            now_time = time.strftime('%Y.%m.%d %H:%M',time.localtime(time.time()))
            out += now_time + " - "
            file_name = os.path.basename(__file__)
            out += file_name + " - "
            line = sys._getframe().f_back.f_lineno
            out += str(line) + " - " + "ERROR " + msg
            print(out)
            if self.file_op is not None:
                self.file_op.write(out+'\n')

    def CRITICAL(self, msg):
        out = ""
        now_time = time.strftime('%Y.%m.%d %H:%M', time.localtime(time.time()))
        out += now_time + " - "
        file_name = os.path.basename(__file__)
        out += file_name + " - "
        line = sys._getframe().f_back.f_lineno
        out += str(line) + " - " + "CRITICAL " + msg
        print(out)
        if self.file_op is not None:
            self.file_op.write(out+'\n')


if __name__ == '__main__':
    t = Log("./test.txt", level="debug")
    t.INFO("this info")
    t.DEBUG("this debug")
    t.ERROR("this error")
    t.WARN("this warnning")
    t.CRITICAL("this critical")