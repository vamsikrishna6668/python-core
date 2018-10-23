a =6890    #global variable
def fun1():
    s =2000  # local variable
    print(s)
def fun2():
    print(a)  #using Local variable.
#calling block
print(a)
fun1()
fun2()
fun1()
# print(s)  Here "s"   is not defined we have to call with the fun1 (function name)
