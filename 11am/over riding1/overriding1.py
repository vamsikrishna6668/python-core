class deloitte:
    def __init__(self,x,y):
        print(x*y)
        print('This is a constructor of a outer class')
    def pythondept(self):
        print('This is a python department in Deloitte')
class ibm:
    def __init__(self,x,y):       # This is a inner class  constructor over riding
        print(x+y)
        print('This is a constructor of a inner class')
    def bigdata(self):
        print('This is a big data department')
#calling block
i =ibm(1,2)