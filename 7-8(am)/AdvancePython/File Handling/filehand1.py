try:
    f=open("sample.txt","r")
    val=f.read()
    print(val ,end = ' ')
    f.close()
    print("\nFile is closed")
except FileNotFoundError:
    print("File not found")
