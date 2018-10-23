a =10
print(a)
print('This is a global variable decarlation')
def oops(b,f):
    global a
    a+=58
    print('This is a global value = ',a)
    print('This is a oops slot')
class python:
    def __init__(self,d,e):
        self.d ='Everything, whatever you created in python it creates like a object in python'
        self.e ='python can develop any kind of a application'
        print('This is a constructor of a outer class')
    def pycharm(self,f):
        self.g =f
        print(self.d)
        print(self.e)
        global a
        a-=2
        print('This is a global value=',a)
        print('This is a Pycharm method')
    def idle(self):
        self.g ='anaconda'
        print(self.g)
        print('This is a idle method')
class java:
    def __init__(self,h,i):
        self.h ='Java is not a Pure object oriented'
        self.i ='Java will also follow the oops principals'
        print("This is a inner class constructor")
    def eclipse(self,k):
        print(self.h)
        print(self.i)
        self.k ='The java  programs can be written in a eclipse'
        global a
        a+=2
        print('This is a global value=',a)
        print('This is a inner classs Method')
    def jdk(self):
        print(self.k)
        print('This is a inner class of a Jdk method')
#calling block
print(a)
ar =oops(10,65)
p =python('pypy','conda')
p.pycharm('idele')
p.idle()
ja =java('python fun','java fun1')
ja.eclipse('This is a java method')
ja.jdk()