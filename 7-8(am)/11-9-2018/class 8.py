# 8. W.A.P for class employee and with two static variables and with a details methods as a static method and print the two static varibales
#  in the object and create a object with a static variables and create a object with a class name ?

class Employee:
   comp_domain="Python"
   comp_profit=32258897889
   @staticmethod
   def details():
      print("Iam details Method")
      print(Employee.comp_domain)
      print(Employee.comp_profit)
# call
e1=Employee()
print(Employee.comp_domain)
print(Employee.comp_profit)
e1.details()
print("=============================================")
# 2nd Object creation

Employee.details()

print("===============================================")
print(Employee().comp_profit)
print(Employee().comp_domain)

"""
Output :
Python
32258897889
Iam details Method
Python
32258897889
=============================================
Iam details Method
Python
32258897889
===============================================
32258897889
Python

Process finished with exit code 0
"""