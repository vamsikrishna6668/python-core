from threading import *
from time import sleep
class Railway:
    def __init__(self,available):
        self.available=available
        self.lock=Lock()
    def reserve(self,wanted):
        self.lock.acquire()
        if self.available>=wanted:
            name=current_thread().getName()
            print('%d  seats are  Alloted to %s'%(wanted,name))
            sleep(2)

            self.available-=wanted
        else:
            print("sorry the seats are not Available for second thread")
        self.lock.release()
class First(Thread):
    def run(self):
        r.reserve(2)

class Second(Thread):
    def run(self):
        r.reserve(2)
#call
r=Railway(5)
f=First()
s=Second()
f.setName('First Thread')
s.setName('Second Thread')
f.start()
s.start()


