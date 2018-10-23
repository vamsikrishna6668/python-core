import threading
from time import sleep
class Thread1(threading.Thread):
    def run(self):
        for i in range(1,50):
            print(i)
            sleep(1)
    def run(self):
        for j in range(51,100):
            print(j)
            sleep(2)
class Thread2(threading.Thread):
    def run(self):
        for k in range(101,110):
            print(k)
            sleep(2)
#call
thre1=Thread1()
thre2=Thread2()
thre1.start()
thre2.start()
