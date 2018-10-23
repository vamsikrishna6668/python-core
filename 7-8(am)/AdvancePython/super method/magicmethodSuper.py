class A:
    def __init__(self,x):
        self.x=x
        print('Iam a Constrcutor of class A ')
class B(A):
    def __init__(self,x,y):
        self.y=y
        print("'Iam a Constrcutor of class B")
        super().__init__(x)
class C(B):
    def __init__(self,x,y,z):
        self.z = z
        print("Iam a Constrcutor of class c")
        super().__init__(x,y)
    def assign(self):
        print("x =" ,self.x)
        print("y =",self.y)
        print("z =",self.z)
#call
c1=C(1,2,3)
c1.assign()

"""
Iam a Constrcutor of class c
'Iam a Constrcutor of class B
Iam a Constrcutor of class A 
x = 1
y = 2
z = 3

Process finished with exit code 0

"""