
from pickle import load
obj=open('students.bin','rb')
while True:
    try:
        i=load(obj)
        print(i)
    except EOFError:
        obj.close()
        break



