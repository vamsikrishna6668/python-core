#method overriding in different classes
class test:
    def m1(self,a,b):
        print(a+b)
class test1(test):
    def m1(self,a,b):
        print('a*b:',a*b)
        super().m1(a,b)
t=test1()
t.m1(10,20)