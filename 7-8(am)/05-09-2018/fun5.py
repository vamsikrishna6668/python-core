# 5. W.A.P for multiple functions  and  call only one function ?
def fun1():
    print('Function 1')
def fun2():
    fun1()
    print('Function 2')
def fun3():
    fun2()
    print('Function 3')
# call
fun3()

"""
Output:

Function 1
Function 2
Function 3

Process finished with exit code 0


"""