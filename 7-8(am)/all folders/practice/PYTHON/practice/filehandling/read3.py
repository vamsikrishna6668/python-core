obj=open('sample','r')
c1=0
c2=0
c3=0
for line in obj:
    c1+=1
    wordslist=line.split()
    c2+=len(wordslist)
    c3+=len(line)
print(c1)
print(c2)
print(c3)
