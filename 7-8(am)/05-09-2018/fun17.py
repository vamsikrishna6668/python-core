#17.	W.A.P   on global variables  without declaring outside a function ?
def fun1():
    print('Iam  fun1')
    global n
    n=1000
    n+=10
    print(n)
#call
fun1()
fun1()
fun1()

"""
Output:
Iam  fun1
1010
Iam  fun1
1010
Iam  fun1
1010

Process finished with exit code 0


"""