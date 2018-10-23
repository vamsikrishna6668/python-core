class First:
    def calculate(self,no1,no2):
        print('The sum =',(no1+no2))
        print('The sub=',(no1-no2))
class second(First):
    def calculate(self,no1,no2):
        super().calculate(no1,no2)
        print("The mul=",(no1*no2))
        print("The div=",(no1/no2))
class third(second):
    def calculate(self,no1,no2):
        super().calculate(no1,no2)
        print('The floor div=',(no1//no2))
        print("The modulus=",(no1%no2))
#call

#f1=First()
#f1.calculate(20,30)
"""
The sum = 50
The sub= -10
"""
print("=====================================")
#sec=second()
#sec.calculate(10,20)
"""
Output:
 
The sum = 30
The sub= -10
The mul= 200
The div= 0.5

"""
print("=========================================")

t1=third()
t1.calculate(10,2)

"""" 
output:
The sum = 12
The sub= 8
The mul= 20
The div= 5.0
The floor div= 5
The modulus= 0

Process finished with exit code 0

"""

print('=============================================')