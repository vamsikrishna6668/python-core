name =input("enter  your name:")
print("name=",name)
length=len(name)
index=0
for x in range(length):
    for y in range(x+1):
        if(index<length):
            print(name[index],end=" ")
            index=index+1
        if index==length:
            print(end=' ')
            break
        print()
print("\n\n Thanks")