#  14. W.A.P for class employee and with a default constructor and with a two parameters and don't decalre in the constructor header body
# and assign the default values and instance method as a display and create a object with a reference variable and create two objects for class ?

class Employee:
    def __init__(self):
        print("Iam Constructor of a Employee")
        self.compbranches ="In Ten Locations"
        self.compheadquaters = "USA"
        self.compincome="14.5lpa"

    def display(self):
        print("Iam display of a  Employeee")
        print(self.compbranches)
        print(self.compheadquaters)
        print(self.compincome)


#call
e1=Employee()
e1.display()
print("==========================")
e2=Employee()
e2.display()

"""
output :

Iam Constructor of a Employee
Iam display of a  Employeee
In Ten Locations
USA
14.5lpa
==========================
Iam Constructor of a Employee
Iam display of a  Employeee
In Ten Locations
USA
14.5lpa

Process finished with exit code 0



"""