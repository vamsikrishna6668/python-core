# 2. W.A.P for Multiple functions and call that functions in a random order ?
def  fun1():
    print('Function 1')
def fun2():
    print('Function 2')
def fun3():
    print('Function 3')
#calling block.
fun2()
fun1()
fun3()
fun1()
print('---------------------------------------')
fun1()
fun2()
fun3()
print("Thanks")


"""

output: 
 
Function 2
Function 1
Function 3
Function 1
---------------------------------------
Function 1
Function 2
Function 3
Thanks

Process finished with exit code 0

"""