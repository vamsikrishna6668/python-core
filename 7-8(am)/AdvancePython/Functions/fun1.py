def fun1(fun):
    return 'hello ' +fun
def fun2():
    return 'World'
#calling block
f=fun1(fun2())
print(f)