# 25. W.A.P for  class name as a employee and constructor and destructor using anomious object ?

class Employee:
    def __init__(self):
        print("Iam Constructor of Employee")
    def __del__(self):
        print("Iam a Destructor of a Employee")
# call
Employee()

print("=================================================")

e1 =Employee()

"""
Output :
Iam Constructor of Employee
Iam a Destructor of a Employee
=================================================
Iam Constructor of Employee
Iam a Destructor of a Employee

Process finished with exit code 0
"""