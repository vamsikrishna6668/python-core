#6.	W.A.P for addition and substraction and take the inputs from the keyboard ?
def add():
    a=int(input('enter 1st no of add:'))
    b=int(input('enter 2nd no of add:'))
    print('Iam add:',a+b)
def sub():
    a=int(input('Enter 1st no of sub:'))
    b =int(input('Enter 2nd no of sub:'))
    print('Iam sub:',a-b)
# call
add()
sub()
print('-----------------------------------')
sub()
add()

"""
Output:

enter 1st no of add:10
enter 2nd no of add:20
Iam add: 30
Enter 1st no of sub:10
Enter 2nd no of sub:20
Iam sub: -10
-----------------------------------
Enter 1st no of sub:10
Enter 2nd no of sub:20
Iam sub: -10
enter 1st no of add:10
enter 2nd no of add:20
Iam add: 30

Process finished with exit code 0


"""