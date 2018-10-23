# 25.W.A.P on function by using the global, local, parameters and write multiple functions ?

a=2000         # global variable.
print(a)
def fun1(b,c):
    b=20
    c=30
    print("The b and c values are:" ,b+c)
    global a
    a += 1200   # incrementing the global  variable.
    print("The global  variable:",a)  # incrementing the global  variable.
    s=2000      # local variable .
    print("The local variable Value:",s)   # local variable - Here the global variable and local variable, referaence variable is same but if we increment also it will not effect on the local variable(The local variable values will not change) .
    print("Iam fun1")
def fun2(d,e):
    print(d+e)
    global f
    f=8000000000
    print("The global  variable:",f)
    g=123123123123123
    print(g)
    f+=1000
    print("The global variable Value:",f)
    g-=123
    print("The local variable Value:",g)
    print("Iam fun2 ")
def fun3(h,i):
    print(h*i)
    j=87123
    print("The local variable Value:",j)
    global k
    k=120003
    print("The global variable Value:",k)
    j+=4456
    print(j)
    k+=789685
    print("The global variable Value:",k)
    print("Iam fun3")
def fun4(m,n):
    print(a+m)
    print(a+n)
    q=7776
    print("The local variable value:",q)
    print("Iam fun4")

# call
print(a)
fun1(68,66)
fun2(86,96)
fun3(12,35)
fun4(68,76)

"""
Output:

2000
2000
The b and c values are: 50
The global  variable: 3200
The local variable Value: 2000
Iam fun1
182
The global  variable: 8000000000
123123123123123
The global variable Value: 8000001000
The local variable Value: 123123123123000
Iam fun2 
420
The local variable Value: 87123
The global variable Value: 120003
91579
The global variable Value: 909688
Iam fun3
3268
3276
The local variable value: 7776
Iam fun4

Process finished with exit code 0



"""