def fun1():
    print('This is Fun1')
def fun2():
    fun1()
    print('This is Fun2')
    fun1()
def fun3():
    fun1()
    print('This is Fun3')
    fun2()
#calling
fun3()

