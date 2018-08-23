import globalVar
import time
from threading import Thread,currentThread,activeCount

# time.struct_time(tm_year=2018, tm_mon=6, tm_mday=30, tm_hour=12, tm_min=10, tm_sec=13, tm_wday=5, tm_yday=181, tm_isdst=0)
class travianTime:
    def __init__(self):
        tmp = []
        tmp.append(time.localtime()[3] - globalVar.SERVERTIMEZONE)
        tmp.append(time.localtime()[4])
        tmp.append(time.localtime()[5])
        self.localTime = tmp
        print (self.localTime)
        Thread(target=self.update, args=()).start()

    def update(self):
        while True:
            tmp = []
            tmp.append(time.localtime()[3] - globalVar.SERVERTIMEZONE)
            tmp.append(time.localtime()[4])
            tmp.append(time.localtime()[5])
            self.localTime = tmp
            time.sleep(1)
            print(self.localTime)

se = travianTime()