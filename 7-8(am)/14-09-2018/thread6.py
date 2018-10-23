import threading
class Thread1(threading.Thread):
    def run(self):
        for i in range(1,50):
            print(i)
    def run(self):
        for j in range(51,100):
            print(j)
class Thread2(threading.Thread):
    def run(self):
        for k in range(101,110):
            print(k)
    def run(self):
        for L in range(120,160):
            print(L)
#call
thre1=Thread1()
thre2=Thread2()
thre1.start()
thre2.start()
