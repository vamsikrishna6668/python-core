a =1000
def fun1():
    global a
    a =100
    print(a)
#calling block
print(a)
fun1()
print(a)
