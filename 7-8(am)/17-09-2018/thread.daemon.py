from threading import *
from time import *
class A:
    def fun1(self):
        for x in range(1,20):
            print(x)
            sleep(1)
class B:
    def fun2(self):
        while True:
            print("Hello Naga Lakshmi")
            sleep(2)
#call
a1=A()
t1=Thread(target=a1.fun1())
b1=B()
t2=Thread(target=b1.fun2())
t1.start()
t2.dameon=True
t2.start()
