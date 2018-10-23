try:
    f=open("sample.txt","r")
    for x in f.readline():
        print(x,end=' ')
except FileNotFoundError:
    print("File not found")
f.close()
print("\n File is closed")




