"""l1=[1,2,3,12,34,1,2,3]
l2=list(set(l1))
l2.sort(key=l1.index)
print(l2)
l2.sort(reverse=True)
print(l2)"""

f=open('prasad1','a')
print('file is opened')
while True:
    line=input('enter the data')
    if line!='stop':
        f.write(line)
        f.write('\n')
    else:
        break;
f.close()
