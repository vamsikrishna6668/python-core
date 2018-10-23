obj=open('sample','r')
str=obj.read()
print(str)
print('---------------------')
obj.seek(16)
str1=obj.read()
print(str1)

