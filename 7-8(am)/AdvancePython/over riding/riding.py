class First:
   def __init__(self,a,b):
       print("The sum of=",a+b)
   def calculator(self,x,y):
        self.x=x
        self.y=y
        print("The no of 1st class  students:",self.x)
        print("The no of 2nd class  students:",self.y)
class Second(First):
    def __init__(self,a,b):
        print("The sub of=",a-b)
        super().__init__(a,b)
    def calculator(self,x,y):
        self.x = x
        self.y = y
        print("The no of 1st class  students:", self.x)
        print("The no of 2nd class  students:", self.y)
#calling block
#f=First(1,2)
#f.calculator(40,50)
"""
Ouput:

The sum of= 3
The no of 1st class  students: 40
The no of 2nd class  students: 50
"""
print("=========================================================")

s=Second(10,20)
s.calculator(66,68)

"""
Output:
The sub of= -10
The sum of= 30
The no of 1st class  students: 66
The no of 2nd class  students: 68

Process finished with exit code 0

"""