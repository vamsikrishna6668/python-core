a =100  # global variable
def fun1():
    a =50   # local variable
    print(a)
def fun2():
    print(a)  # using a global variable
#calling block
print(a)
fun1()
fun2()
fun1()
