#13. W.A.P on function with parameter and with return on add, sub and take values from keyboard and by using the print stmt create the object ?
def add(no1,no2):
    return no1+no2
a = int(input('Enter 1st no of addition:'))
b = int(input('Enter 2nd no of addition:'))
def sub(no1,no2):
    return no1 + no2
x = int(input('Enter 1st no of substraction:'))
y = int(input('Enter 2nd no of substraction:'))
#calling
print('The add=',add(a,b))
print('The sub=',sub(x,y))
""" 
OUTPUT:
Enter 1st no of addition:1
Enter 2nd no of addition:2
Enter 1st no of substraction:1
Enter 2nd no of substraction:2
The add= 3
The sub= 3

"""
print('====================================================')
# same pgm by using the only one input function.
def add(no1,no2):
    return no1+no2
def sub(no1,no2):
    return no1-no2
a=int(input('enter 1St no:'))
b=int(input('enter 2nd no:'))
#call
print("The sum =",add(a,b))
print("The sub=",sub(a,b))
""" 
OUTPUT:
enter 1St no:1
enter 2nd no:2
The sum = 3
The sub= -1
Process finished with exit code 0
"""