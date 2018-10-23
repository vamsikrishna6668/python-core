from threading import Thread
from time import sleep
class A(Thread):
    def run(self):
        for x in range(1,34):
            print(x)
            sleep(12)
class B(Thread):
    def run(self):
        for x in range(46,56):
            print(x)
#call
a1=A()
b1=B()
a1.start()
b1.start()