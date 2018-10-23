from threading import Thread
class A:
    def fun1(self):
        for x in range(1,26):
            print(x)
class B:
    def fun2(self):
        for x in range(26,36):
            print(x)
# call
a1=A()
b1=B()
t1=Thread(a1.fun1())
t2=Thread(b1.fun2())
t1.start()
t2.start()