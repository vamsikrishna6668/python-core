from threading import Thread
from time import sleep
class A:
    def fun1(self):
        for x in range(1,11):
            print(x)
            sleep(3)
    def fun2(self):
        for x in range(11,21):
            print(x)
            sleep(1)
class B:
    def fun3(self):
        for x in range(21,26):
            print(x)
            sleep(2)
    def fun4(self):
        for x in range(50,60):
            print(x)
            sleep(4)
#call
a=A()
b=B()
t1=Thread(a.fun1())
print("The Thread 1 execution is completed,whenever the Thread 1 execution is completed Then only Thread 2 Execution starts")
t2=Thread(a.fun2())
print("The Thread 2 execution is completed,whenever the Thread 2 execution is completed Then only Thread 3 Execution starts")
t3=Thread(b.fun3())
print("The Thread 3 execution is completed,whenever the Thread 3 execution is completed Then only Thread 4 Execution starts")
t4=Thread(b.fun4())
t1.start()
t2.start()
t3.start()
t4.start()
print("All The Threads are successfully Executed")