f=open("sample.txt","r")
while True:
    val=f.readline()
    if val=="":
        break
    else:
        print(val,end='')
f.close()
