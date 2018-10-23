obj=open('sample','r')
count=0
for x in obj:
    count+=x.count('python')
print('repeatation is:',count)
obj.close()