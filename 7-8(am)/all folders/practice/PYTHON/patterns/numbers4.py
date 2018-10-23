n=int(input('enter a no of rows'))
num=0
for i in range(1,n):
    for j in range(1,i+1):
        num=num+1
        print(num,end='  ')
    print('\r')