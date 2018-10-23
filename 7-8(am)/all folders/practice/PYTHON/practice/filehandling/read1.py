try:
    obj=open('sample','r')
    for line in obj:
        print(line)
except:
   print('sorry, the file not exist in the system')
finally:
    obj.close()
