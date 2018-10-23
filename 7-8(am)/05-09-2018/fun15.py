# 15. W.A.P on global variables by using one function and print the function for multiple times ?
a=6666
print("The global variable value before increment:",a)
def fun1():
    global a
    a+=2
    print("The global variable value after the  increment:",a)
#call
print("The global variable value before increment:",a)
fun1()
print("The global variable value after the increment:",a)
fun1()

"""
Output:

The global variable value before increment: 6666
The global variable value before increment: 6666
The global variable value after the  increment: 6668
The global variable value after the increment: 6668
The global variable value after the  increment: 6670

Process finished with exit code 0



"""