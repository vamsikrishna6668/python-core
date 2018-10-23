# 13. W.A.P for class employee and with a constructor and instance method as a show and create a object without a reference variable
# and with a reference variable?

class Employee:
    def __init__(self,idno,name):
        self.idno=idno
        self.name=name
        print(self.idno)
        print(self.name)
        print("Iam a constructor of Employee class ")
    def show(self):
        print("Iam show Method of a Employee")

# call

c1=Employee(101,'basha')
c1.show()
print("===============================================")
Employee(idno=102,name='lakshmi').show()
print("===============================================")
Employee(idno=103,name='Anji').show()
print("===============================================")


"""
Output :
101
basha
Iam a constructor of Employee class 
Iam show Method of a Employee
===============================================
102
lakshmi
Iam a constructor of Employee class 
Iam show Method of a Employee
===============================================
103
Anji
Iam a constructor of Employee class 
Iam show Method of a Employee
===============================================
Process finished with exit code 0
"""
