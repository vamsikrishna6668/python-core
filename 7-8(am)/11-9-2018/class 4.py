# 4. W.A.P for class employee and with a static variables and with a method of display and print the Two static variables in display method
#  and in object also and create a object with a reference variable?

class Employee:
    eidno=120
    ename='IBM'
    print("Iam class")
    def display(self):
        print("Iam display")
        print(Employee.eidno)
        print(Employee.ename)

# call
e1=Employee()
print(Employee.eidno)
print(Employee.ename)
e1.display()

"""
Output :
Iam class
120
IBM
Iam display
120
IBM

Process finished with exit code 0
"""