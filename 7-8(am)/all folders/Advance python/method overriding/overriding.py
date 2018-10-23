class kerala:
    def __init__(self,x):
        print('This is a constructor of a outer class')
    def display(self,a,b):
        print(a+b)
class thirusur(kerala):
    def __init__(self,x,y):
        print('This is a constructor of inner class')
    def display(self,a,b):
        print(a*b)
#calling block
t =thirusur(1,2)
t.display(1,2)