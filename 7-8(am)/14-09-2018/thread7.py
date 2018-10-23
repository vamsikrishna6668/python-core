from threading import Thread
from time import sleep
class A(Thread):
    def run(self):
        for x in range(1,21):
            print(x)
            sleep(2)

class B(Thread):
    def run(self):
        a=A()
        a.start()
        for y in range(21,41):
            print(y)
            sleep(5)
            if y==26:
                a.join()
#call
b=B()
b.start()