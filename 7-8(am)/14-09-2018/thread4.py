import threading
class A1(threading.Thread):
    def run(self):
        for x in range(1,4):
            print(x)
class B1(threading.Thread):
    def run(self):
        for x in range(5,9):
            print(x)
#call
a1=A1()
a1.start()
b1=B1()
b1.start()
