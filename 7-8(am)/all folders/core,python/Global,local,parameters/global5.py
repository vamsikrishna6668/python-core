def fun1():
    global a       # global variable in a function
    a =1000
    print(a)
    print(a)
#calling block
fun1()
print(a)
