from threading import *
from time import *
def fun1():
    for x in range(1,20):
        print(x)
        sleep(3)
def fun2():
    while True:
        print("Hello World")
        sleep(2)
#call
print(current_thread().getName())
t1=Thread(target=fun1())
t2=Thread(target=fun2())
t1.start()
t2.damenon=True
t2.start()
t2.join()