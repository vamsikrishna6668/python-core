n=5
for i in range(0,n):
    for j in range(0,i):
        print(end =' ')
    for j in range(0,n-i):
        print('*',end='')      # after end if i provide a space then it will another pattern.
    print( )