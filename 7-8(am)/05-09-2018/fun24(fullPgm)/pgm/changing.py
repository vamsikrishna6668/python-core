# 24. W.A.P on function and use global variable and local variable with three  functions (fun1,fun2,fun3) and  import all the functions ?
n=6680
def fun1(i,j):
    i=10
    j=20
    print(i+j)
    s =68
    global n
    n+=100
    print(n)
    print("The function 1 ")
    s+=60
    print(s)
def fun2():
    k=2500
    global p
    p=120000
    print(p)
    k-=2400
    print(k)
    print("Iam function 2")
def fun3():
    f=14000
    global q
    q=16000
    print("Iam function - 3 of a global variable:",q)
    print(f)
