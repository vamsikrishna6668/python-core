from threading import Thread
from time import sleep
def fun1():
    for x in range(1,16):
        print(x)
        sleep(2)
def fun2():
    for x in range(16,26):
        print(x)
        sleep(3)
def fun3():
    for x in range(26,36):
        print(x)
        sleep(1)
#call
t1=Thread(target=fun1())
print("The Thread 1 execution is completed,whenever the Thread 1 execution is completed Then only Thread 2 Execution starts")
t2=Thread(target=fun2())
print("The Thread 2 execution is completed,whenever the Thread 2 execution is completed Then only Thread 3 Execution starts")
t3=Thread(target=fun3())
t1.start()
t2.start()
t3.start()
print("All The Threads are successfully Executed")