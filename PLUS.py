import datetime
import time

class AplusB(object):
    def _a(a,b,c = datetime.datetime.now()):
        d = a+b
        return d,c

sum_total,time_start = AplusB._a(1, 2)
time_end = datetime.datetime.now()
print(sum_total,time_end - time_start)
time.sleep(2)
sum_total,time_start = AplusB._a(3,4)
time_end = datetime.datetime.now()
print(sum_total,time_end - time_start)