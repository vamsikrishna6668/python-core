from threading import Thread
def fun1():
    for x in range(0,21):
        print(x)
def fun2():
    for x in range(21,36):
        print(x)
#call
t1=Thread(target=fun1())
print("The thread 1 execution is completed")
t2=Thread(target=fun2())
t1.start()
t2.start()