# 10. W.A.P for class employee and @ class method which is accessing static variables and static methods and create a object without a reference variable ?
class Employee:
     empDestination='Software'
     empExperience=15
     @staticmethod
     def assign(i,j):
         i=10
         j=20
         print(i+j)
         print("Iam Assign method")
     @classmethod
     def display(cls):
         print(cls.empDestination)
         print(cls.empExperience)
         cls.assign(1,2)
         print("Iam Display Method")
#call
e1=Employee()
e1.assign(12,23)
e1.display()
Employee.assign(66,68)
Employee.display()
print("========================================")
print(Employee().empExperience)
print(Employee().empDestination)
Employee.assign(56,68)
Employee.display()
print("=========================================")
Employee.display()

"""
Output :
30
Iam Assign method
Software
15
30
Iam Assign method
Iam Display Method
30
Iam Assign method
Software
15
30
Iam Assign method
Iam Display Method
========================================
15
Software
30
Iam Assign method
Software
15
30
Iam Assign method
Iam Display Method
=========================================
Software
15
30
Iam Assign method
Iam Display Method
"""