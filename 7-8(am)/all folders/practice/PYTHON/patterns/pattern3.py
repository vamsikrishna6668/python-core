n=int(input('enter no of rows:'))
num=0
for i in range(0,n):
    num=0
    for j in range(0,i+1):
        num+=1
        print(num,end='  ')
    print('\r')