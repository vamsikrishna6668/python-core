a =100
def glob():
    global a
    a =5000
    print(a)
#calling block
print(a)
glob()
print(a)

