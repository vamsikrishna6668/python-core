# 1. W.A.P for class employee and static variables and static methods and local variables and with a method name as a display
# and create a object without a reference variable?

class Employee:
    empid=101
    empname='Basha'
    @staticmethod
    def display():
        a=1000
        print("Iam display")
        print(a)
# call
print(Employee.display())  # If we use the stmt like this """ print(Employee.display()) """ will print the None in the output,
                           # if you are using the stmts like this ""Employee.display()"" then you will not get in output as None.
print(Employee.empid)
print(Employee.empname)
print("=================================")
print(Employee.empid)
print(Employee.empname)
Employee.display()

"""
Output :
Iam display
1000
None
101
Basha
=================================
101
Basha
Iam display
1000
Process finished with exit code 0
"""