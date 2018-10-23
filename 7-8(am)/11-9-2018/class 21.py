# 21. W.A.P for class name as a employee and Can we define multiple constructors with a same no of parameters in a single class or not create a object without a reference variable
# for a class ?


class Employee:
    def __init__(self):
        print("Iam Constructors of Employee")
    def __init__(self):
        print("Iam costructors of Employeeeee")
    def __init__(self):
        print("Iam constructor of Employeeeeeeeeeeeeeeeeeeee")
#call
Employee()

"""
Output :
Iam constructor of Employeeeeeeeeeeeeeeeeeeee

Process finished with exit code 0


"""


