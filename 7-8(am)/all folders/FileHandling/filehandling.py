try:
    fobj =open('ismail.txt','r')
    print('The file is opened')
    for line in fobj:
        print(line)
except:
    print('The file not exist')
finally:
    fobj=close()
print('Iam finally')
