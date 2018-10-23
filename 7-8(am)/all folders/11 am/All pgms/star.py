n =int(input('enter a number:'))
for row in range(1,n):
    for col in range(row+1):
        if row ==0 or col==5 or row==col:
            print('*',end='')
            print()
             
        
