#16. W.A.P on global variables and local variables by using one function and print the function for multiple times ?
s=1000
def fun1():
    n=100
    global s
    s+=10
    print(s)
    print(n)
    n+=10
    print(n)
# call
print(s)
fun1()
print(s)
fun1()
print(s)
fun1()


"""
Output:

1000
1010
100
110
1010
1020
100
110
1020
1030
100
110

Process finished with exit code 0

"""