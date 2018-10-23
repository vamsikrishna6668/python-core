from threading import Thread
def fun1():
    for x in range(1,11):
        print(x)

def fun2():
    for x in range(11,21):
        print(x)

#call
t1=Thread(target=fun1())
print("The Thread 1 execution is completed,whenever the Thread 1 execution is completed Then only Thread 2 Execution starts")
t2=Thread(target=fun2())
t1.start()
t2.start()

print("All The Threads are successfully Executed")