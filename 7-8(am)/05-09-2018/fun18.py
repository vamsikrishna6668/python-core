# 18.	W.A.P  to  modify the  global variables values ?
s=568
def fun1():
    print('Iam fun1')
    m=566
    global s
    s-=2
    print(s)
    print(m)
    m+=2
    print(m)
#call
print(s)
fun1()
print(s)
# print(m)   # This is a local variable we should not call in calling block its scope is with in the block only.
fun1()

"""
Output:

568
Iam fun1
566
566
568
566
Iam fun1
564
566
568

Process finished with exit code 0
"""