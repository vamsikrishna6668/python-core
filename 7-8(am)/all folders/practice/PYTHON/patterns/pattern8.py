n=int(input('enter a no of rows:'))
num=0
for i in range(n,0,-1):
    for j in range(0,i+1):
        num+=1
        print(num,end=' ')
    print('\r')