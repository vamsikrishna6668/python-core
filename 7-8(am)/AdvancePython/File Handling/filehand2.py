f=open("sample.txt",'r')
for x in f.readline():
    print(x,end=' ')
f.close()
print("\nFile is closed")