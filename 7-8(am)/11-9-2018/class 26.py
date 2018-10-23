# 26 . W.A.P for class employee and with a default  constructor and with a two parameters and assign the default values and instance method as a
# display and create a object with a reference variable and create two objects for class ?

class Employee:
    def __init__(self,emploc='hyd',empdes='senior Associate Enigeer',empidno=7776):
        print("Iam Constructor of a Employee")
        self.emploc = emploc
        self.empdes = empdes
        self.empidno=empidno

    def display(self):
        print("Iam display of a  Employeee")
        print(self.emploc)
        print(self.empdes)
        print(self.empidno)


#call
e1=Employee()
e1.display()
print("==========================")
e2=Employee(12245)
e2.display()
print("==============================")
e3=Employee(empidno=6668)
e3.display()
print("================================")

e4=Employee(emploc='Delhi')
e4.display()
print("===================")
e5=Employee(empdes="software Engineer",empidno=9477)
e5.display()
print("================================================")

e6=Employee(empidno=6890,empdes='software',emploc='Madras')
e6.display()

"""
Output :
Iam Constructor of a Employee
Iam display of a  Employeee
hyd
senior Associate Enigeer
7776
==========================
Iam Constructor of a Employee
Iam display of a  Employeee
12245
senior Associate Enigeer
7776
==============================
Iam Constructor of a Employee
Iam display of a  Employeee
hyd
senior Associate Enigeer
6668
================================
Iam Constructor of a Employee
Iam display of a  Employeee
Delhi
senior Associate Enigeer
7776
===================
Iam Constructor of a Employee
Iam display of a  Employeee
hyd
software Engineer
9477
================================================
Iam Constructor of a Employee
Iam display of a  Employeee
Madras
software
6890

Process finished with exit code 0
"""