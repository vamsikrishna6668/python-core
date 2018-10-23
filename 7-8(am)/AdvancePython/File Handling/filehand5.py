try:
    f=open("sample.txt","r")
    val=f.readline()
    print(val)
    val1=f.readline()
    print(val1)
except FileNotFoundError:
    print("File is not found")

