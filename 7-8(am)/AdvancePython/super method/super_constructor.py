class Bikes :
    def __init__(self,x):
        self.x=x
        print("Iam constructor of a Bikes class")
    def petrol(self):

        print("bikes class  Method of a petrol ")
class Cars(Bikes):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        super().__init__(x)
        print("Iam constructor of a cars class ")
    def petrol(self):

        print("Iam cars class  Method of a petrol")
        super().petrol()

class Trucks(Cars):
    def __init__(self,x,y,z):
        self.z=z
        print("Iam constructor of a Trucks class ")
        super().__init__(x,y)
    def petrol(self):
        print("The 'X' Value =",self.x)
        print("The 'Y' Value =",self.y)
        print("The 'Z' Value =",self.z)
        print("Iam trucks class Method of a petrol")
        super().petrol()

#call
#c =Bikes(12)
#c.petrol()
"""
Output:
Iam constructor of a Bikes class
bikes class  Method of a petrol 
"""
car=Cars(6,5)
car.petrol()
"""
Output:

Iam constructor of a Bikes class
Iam constructor of a cars class 
Iam cars class  Method of a petrol
bikes class  Method of a petrol 

"""

t =Trucks(10,20,30)
t.petrol()
"""
Output:
Iam constructor of a Trucks class 
Iam constructor of a Bikes class
Iam constructor of a cars class 
The 'X' Value = 10
The 'Y' Value = 20
The 'Z' Value = 30
Iam trucks class Method of a petrol
Iam cars class  Method of a petrol
bikes class  Method of a petrol 

"""