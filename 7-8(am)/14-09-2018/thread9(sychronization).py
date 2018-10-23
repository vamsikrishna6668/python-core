from threading import *
from time import sleep
class RedBus:
    def __init__(self,available):
        self.avaiable=available
        self.lock=Lock()
    def reserve(self,wanted):
        self.lock.acquire()
        if self.avaiable>=wanted:
            name=current_thread().getName()
            print('%d seats are available for %s'%(wanted,name))
            sleep(3)
            self.avaiable-=wanted
        else:
            print("The seats are not Available for 2nd Thread")
        self.lock.release()
class First(Thread):
    def run(self):
        r.reserve(2)
class Second(Thread):
    def run(self):
        r.reserve(2)
#call
r=RedBus(3)
f=First()
s=Second()
f.setName('first Thread')
s.setName('Second Thread')
f.start()
s.start()