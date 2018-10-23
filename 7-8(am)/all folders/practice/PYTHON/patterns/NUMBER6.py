n=int(input('enter a no of rows'))
num=65
for i in range(0,n):
    for j in range(0,i+1):
        ch = chr(num)
        num+=1
        print(ch,end=' ')
    print('\r')
