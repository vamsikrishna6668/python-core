# 19. W.A.P for class name as a employee and Can we define multiple methods with same name with same no .of parameters in a single class?
class Employee:
    def show(self,idno,name,sal):
        self.idno=idno
        self.name=name
        self.sal=sal
        print(self.idno)
        print(self.name)
        print(self.sal)
        print("Iam show 1 of Employee")
    def show(self,idno,name,sal):
        self.sal = sal
        self.name=name
        self.idno=idno
        print(self.sal)
        print(self.name)
        print(self.idno)
        print("Iam show 2 of Employee")
#call
e1=Employee()
e1.show(102,'ismail',123456789)
print("========================================")

e2=Employee()
e2.show(103,"basha",147896898)

"""
output:

123456789
ismail
102
Iam show 2 of Employee
========================================
147896898
basha
103
Iam show 2 of Employee

Process finished with exit code 0

"""