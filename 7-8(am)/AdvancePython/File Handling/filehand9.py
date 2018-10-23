try:
    #f=open("C:\\Users\\Azeem\\Desktop\\sample1.txt","r")
    f = open(r"C:\Users\Azeem\Desktop\sample1.txt", "r")
    val=f.read()
    print(val,end='')
    f.close()
    print("File is closed")
except FileNotFoundError:
    print("\n File not found")

