#19. W.A.P  for local variables  and without the creating a reference variable and print the local variable in calling block ?
def fun1():
    print('Iam fun1')
    L=668
    print(L)
    L+=200
    print(L)
# call
fun1()
# print(L)    # Error- Bcz the local variable scope is with in the block itself only.
fun1()
# print(L)    # Error- Bcz the local variable scope is with in the block itself only.


"""
Output:
Iam fun1
668
868
Iam fun1
668
868

Process finished with exit code 0

"""