class IBM:
    def __init__(self,Empid,Empname):
        self.Empid=Empid
        self.Empname=Empname
    def  Employee(self,x,y):
        self.x=x
        self.y=y
        print("The Empid of IBM=",self.Empid)
        print("The EmpName of IBM=",self.Empname)
        print("The value of x=", self.x)
        print("The value of y=", self.y)
class Deloitte(IBM):
    def __init__(self,Empid,Empname):
        self.Empid=Empid
        self.Empname=Empname
        super().__init__(Empid,Empname)
    def Employee(self,x,y):
        self.x=x
        self.y=y
        super().Employee(x,y)
        print("The value of Deloitte x=",self.x)
        print("The value of Deloitte y=",self.y)
        print("The Empid of Deloitte=",self.Empid)
        print("The Empname of Deloitte=",self.Empname)
# calling block
c1=Deloitte(120,'Ismail')
c1.Employee(1,2)