import threading
from time import sleep
class A(threading.Thread):
    def run(self):
        for x in range(1,26):
            print(x)
class B(threading.Thread):
    def run(self):
        for x in range(30,45):
            print(x)
#call
a1=A()
b1=B()
a1.start()
b1.start()
