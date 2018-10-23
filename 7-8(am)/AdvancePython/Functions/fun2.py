def fun1(f1):
    print("Iam fun1 Method")
    return 'Hello '+f1
def fun2():
    print("Iam fun2 Method")
    return 'world'
#call
f= fun1(fun2())
print(f)