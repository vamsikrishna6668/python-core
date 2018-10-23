# 9. W.A.P for class employee and make display method as a class method and print cls in display method and
#  create a object without a reference variable ?

class Employee:
    @classmethod
    def display(cls):
        print("Iam  Display")
        print(cls)
#call
Employee()
Employee.display()


"""
Output:
Iam  Display
<class '__main__.Employee'>

Process finished with exit code 0

"""








