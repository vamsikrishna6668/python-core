f=open("sample.txt",'r')
for x in f:
    print(x,end=' ')
f.close()
print("\nFile is closed")