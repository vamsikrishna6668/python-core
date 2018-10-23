# 15. W.A.P for class employee and with a default constructor and with a two parameters and assign the positional values and instance method as a display
# and create a object with a reference variable and create  two objects for class ?

class Employee:
    def __init__(self,idno,name):
        self.idno=idno
        self.name=name

    def display(self):
        print("Iam Display")
        print(self.idno)
        print(self.name)
# calll
e1=Employee(123435,'Babu')
e1.display()
print("==================================")
e2=Employee(6668,'Basha')
e2.display()

"""
Output :

Iam Display
123435
Babu
==================================
Iam Display
6668
Basha

Process finished with exit code 0

"""