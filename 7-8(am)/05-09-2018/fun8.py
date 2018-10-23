#8. W.A.P on function with parameter(Take two parameter)and without return by using addition and substraction(Take values from keyboard)?
def add(no1,no2):
    print('Iam add:',no1+no2)
def sub(no1,no2):
    print('Iam sub:',no1-no2)
a=int(input('Enter 1st no:'))
b=int(input('Enter 2nd no:'))
# call
add(a,b)
sub(a,b)
print('-------------------------------')
sub(10,20)
add(10,20)

#output:
""" 
Enter 1st no:1
Enter 2nd no:12
Iam add: 13
Iam sub: -11
-------------------------------
Iam sub: -10
Iam add: 30

Process finished with exit code 0

Output 2 :  
Enter 1st no:66
Enter 2nd no:68
Iam add: 134
Iam sub: -2
-------------------------------
Iam sub: -10
Iam add: 30

Process finished with exit code 0

"""