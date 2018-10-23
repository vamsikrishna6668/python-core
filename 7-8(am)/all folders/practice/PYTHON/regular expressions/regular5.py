import re
fobj1=open('emp','r')
fobj2=open('prasad2.txt','w')
fobj2.write('sid   mobile')
fobj2.write('\n')
for line in fobj1:
    lst=re.findall(r'\w{1,}',line)
    if lst!=[]:
        fobj2.write(lst[0]+"\t"+lst[3])
        fobj2.write('\n')
fobj1.close()
fobj2.close()