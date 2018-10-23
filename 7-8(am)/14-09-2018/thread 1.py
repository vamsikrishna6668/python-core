from threading import Thread
from time import sleep
def fun1():
    for x in range(1,6):
        print(x)
        sleep(5)
def fun2():
    for x in  range(10,16):
        print(x)
        sleep(2)
#call
t1 =Thread(target=fun1())
print("The Thread 1 execution is completed,whenever the Thread 1 execution is completed Then only Thread 2 Execution starts")
t2=Thread(target=fun2())
t1.start()
t2.start()

print("All The Threads are successfully Executed")