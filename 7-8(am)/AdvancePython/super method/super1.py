class Bank:
    def __init__(self,x):
        self.x=x
        print("Iam constructor of Bank class")
    def assign(self,i):
        self.i=i
        print("Iam display")
class Branch(Bank):
    def __init__(self,x,y):
        self.y=y
        print("Iam Constructor of Branch class")
        super().__init__(x)
    def show(self,j):
        self.j=j
        print("Iam Show Method")
class Location(Branch):
    def __init__(self,x,y,z):
        self.z=z
        print("Iam constructor of Location Branch of c class")
        super().__init__(x,y)
    def display(self,k):
        self.k=k
        print("Iam the value of x:", self.x)
        print("Iam the value of y:",self.y)
        print("Iam the value of z:",self.z)
        print("Iam Display")
#call
loca=Location(99,56,89)
loca.display(12)
loca.show(68)
loca.assign(66)