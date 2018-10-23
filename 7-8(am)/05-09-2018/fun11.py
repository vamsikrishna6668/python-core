#11. W.A.P on function it must return three values from a function?
def fun1():
    #print(fun2())
    #print(fun3())
    print('Iam Function 1')
    return '1,2,3'
def fun2():
    print(fun1())
    print(fun3())
    print('Iam Function 2')
    return  '68,ismail,Anji'
    return   66,'chanti','sathi'   # In a function there must be only one return should be there.
def fun3():
    #print(fun1())
    #print(fun2())
    print('Iam function 3')
    return 66,68,81
#call
f2=fun2()
print(f2)
print('-------------------------------')
fun3()


"""
Output:

Iam Function 1
1,2,3
Iam function 3
(66, 68, 81)
Iam Function 2
68,ismail,Anji
-------------------------------
Iam function 3

Process finished with exit code 0

"""