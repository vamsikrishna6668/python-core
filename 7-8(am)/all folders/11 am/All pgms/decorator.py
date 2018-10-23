def decor(fun):
    def inner(x):
        val =fun()
        val +=20
        return val
    return inner
@decor
def my_num():
    return 10
#calling block
m =my_num(10)
print(m)
