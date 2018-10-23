# 6. W.A.P for class employee and with static variables and with a assign method and with a two parameters without decarling method header
#  and display methods and print the two static variables in display method and create two objects?
class Employee:
    comp_name='Syntel'
    comp_cno=85000580594
    def assign(self):
        self.currentloca='Australia'
        self.woringdomain="Python"
        print("Iam  Assign")
    def display(self):
        print("Iam display")
        print(self.currentloca)
        print(self.woringdomain)
        print(Employee.comp_name)
        print(Employee.comp_cno)
# call
e1=Employee()
# e1.display() # Error
print(Employee.comp_name)
print(Employee.comp_cno)
e1.assign()
e1.display()
print("====================================")
e2=Employee()
print(Employee.comp_name)
print(Employee.comp_cno)
e2.assign()
e2.display()
"""
Output :
Syntel
85000580594
Iam  Assign
Iam display
Australia
Python
Syntel
85000580594
====================================
Syntel
85000580594
Iam  Assign
Iam display
Australia
Python
Syntel
85000580594
Process finished with exit code 0
"""