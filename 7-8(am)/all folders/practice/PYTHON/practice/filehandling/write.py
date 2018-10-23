obj=open('prasad.txt','w')
print('enter data until the program will be end')
while True:
    line=input()
    if line!='end':
        obj.write(line)
        obj.write('\n')
    else:
        break
obj.close()

