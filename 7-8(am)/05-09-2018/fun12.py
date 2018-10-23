# 12. W.A.P on function return the multiple values of different  datatypes from a function?
def fun1():
    print('Iam function -1')
    return 10,20.68,66,'ismail'
def fun2():
    print('Iam function -2')
    return 100
def fun3():
    print('Iam function -3')
    return '68,68.66,ismail,anji'
#calli
f=fun1()
print(f)
f=fun2()
print(f)
f=fun3()
print(f)
""" 
Output:
Iam function -1
(10, 20.68, 66, 'ismail')
Iam function -2
100
Iam function -3
68,68.66,ismail,anji
"""
print('======================================')
print(fun1())
print(fun2())
print(fun3())
"""
Output:
Iam function -1
(10, 20.68, 66, 'ismail')
Iam function -2
100
Iam function -3
68,68.66,ismail,anji


"""