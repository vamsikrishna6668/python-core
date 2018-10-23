# 23. W.A.P for class name as a employee and default constructor and method name as a display and magic method as a del create a object
#  with a reference variable for a class ?
class Employee:
    def __init__(self,idno,name):
        self.idno=idno
        self.name=name
        print("Iam constructor ")
    def display(self):
        print(self.idno)
        print(self.name)
        print("Iam Display")
    def __del__(self):
        print("Iam a destructor")
#call
c1=Employee(1254,'ismail')
c1.display()
"""
Output :
Iam constructor 
1254
ismail
Iam Display
Iam a destructor

Process finished with exit code 0
"""