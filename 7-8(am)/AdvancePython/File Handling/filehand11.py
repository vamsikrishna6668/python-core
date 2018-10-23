f=open("sample.txt",'r')
for x in f.readlines():
    print(x,end=' ')
f.close()
print("\nFile is closed")