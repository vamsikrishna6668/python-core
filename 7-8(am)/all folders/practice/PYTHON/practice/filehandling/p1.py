import student
from pickle import dump
x=int(input('enter how many objects you want to serilize'))
obj=open('students.bin','wb')
for i in range(1,x+1):
    m=int(input('enter id '))
    n=input('enter name')
    stu=student.college(m,n)
    dump(stu,obj)
print('serilize is competed')
obj.close()