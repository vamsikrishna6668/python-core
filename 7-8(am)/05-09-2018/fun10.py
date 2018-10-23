#10. W.A.P  on function without parameter and with return on add,sub,mul,div and call  only one function i.e : DiV\
def add():
    return(10+20)
def sub():
    print(add())
    return(10-20)
def mul():
    print(sub())
    return(10*20)
def div():
    print(mul())
    return(10/20)
#call
print(div())

"""
OUtPUT:
30
-10
200
0.5

Process finished with exit code 0


"""