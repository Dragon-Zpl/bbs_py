import datetime
import time
from util import log
from functools import wraps


def Decorators_time(f):
    @wraps(f)
    def wrapped_function(*args, **kwargs):
        now_time = datetime.datetime.now()
        t = f(*args, **kwargs)
        end_time = datetime.datetime.now()
        spend_time = end_time-now_time
        log.INFO(f.__name__+":"+str(spend_time))
        return t
    return wrapped_function



class Test:


    @Decorators_time
    def test(self,s):
        print(s)
        time.sleep(5)


if __name__ == '__main__':
    t = Test()
    t.test('dasda')
