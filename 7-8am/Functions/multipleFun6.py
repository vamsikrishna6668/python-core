def fun1():
    print('fun1')
def fun2():
    print('fun2')
    fun1()
    fun1()
def fun3():
    fun1()
    print('fun3')
    fun1()
    fun2()
#calling
fun3()