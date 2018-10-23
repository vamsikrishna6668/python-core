from threading import Thread
from time import sleep
class A(Thread):
    def run(self):
        for x in range(1,20):
            print(x)
            sleep(2)
class B(Thread):
    def run(self):
        a1=A()
        a1.start()
        for y in range(21,40):
            print(y)
            sleep(2)
            if y==24:
                a1.join()

#call
b1=B()
b1.start()