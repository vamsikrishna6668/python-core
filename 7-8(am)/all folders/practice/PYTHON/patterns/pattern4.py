n=int(input('enter a n of rows:'))
num=0
for i in range(0,n):
    for j in range(0,i+1):
        num+=1
        print(num,end='  ')
    print('\r')