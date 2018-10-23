str= input('Enter a name:')
length=len(str)
for x  in range(length):
    for y in range(x+1):
        print(str[y],end=' ')
        for z in range(1,4):
            print('\n',end=' ')

print('Thanks')