# 22. W.A.P for class name as a employee and Can we define 3  or multiple constructors with a different parameters in a single class and
# create a object without a reference variable for a class ?

class Employee:
    def __init__(self):
        print("Iam constructor 0 of Employee")

    def __init__(self,idno):
        print("Iam constructor 1 of Employee")
        print(idno)
    def __init__(self,idno,name):
        print("Iam constructor 2 of Employee")
    def __init__(self,idno,name,salary):
        print("Iam constructor 3 of Employee")
        print(idno)
        print(name)
        print(salary)
#calling
Employee(1235,"ismail",123456789)

"""
Output :
Iam constructor 3 of Employee
1235
ismail
123456789
Process finished with exit code 0
"""