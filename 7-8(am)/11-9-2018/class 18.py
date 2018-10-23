# 18. W.A.P for method overloading class name as a Employee and with a default constructor with a default parameters
# and create a method name as a display create a object with a reference variable and create fours objects for class ?


class Employee:
    def __init__(self,emp='Anji',compname='capgemini',compsal=85000057):
        self.emp=emp
        self.compname=compname
        self.compsal=compsal
    def display(self):
        print(self.emp)
        print(self.compname)
        print(self.compsal)
        print("Iam Display Of a Employee")
# call
e1=Employee()
e1.display()
print("===========================================================")
e2=Employee('Anjali')
e2.display()
print("===========================================================")
e2=Employee(emp='Anji Babu')
e2.display()
print("============================================================")
e3=Employee(emp="ismail",compname='UBC')
e3.display()
print("===========================================================")
e4=Employee(compname="delotitee",compsal=45789679)
e4.display()
print("==============================================")
e5=Employee(compname="cognizant",compsal=45789679,emp='balaram')
e5.display()
"""
Output:

Anji
capgemini
85000057
Iam Display Of a Employee
===========================================================
Anjali
capgemini
85000057
Iam Display Of a Employee
===========================================================
Anji Babu
capgemini
85000057
Iam Display Of a Employee
============================================================
ismail
UBC
85000057
Iam Display Of a Employee
===========================================================
Anji
delotitee
45789679
Iam Display Of a Employee
==============================================
balaram
cognizant
45789679
Iam Display Of a Employee

Process finished with exit code 0

"""