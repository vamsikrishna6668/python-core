id =int(input('Enter a idno:'))
na=input('Enter a name:')
no=int(input('Enter a no of subjects:'))
subj=[]

for x in range(no):
    subject=input('enter a name  of subjects:')
    subj.append(subject)

from AdvancePython.inheritance.faculty import facultysathyainfo

#calling block
fs=facultysathyainfo(idno=id,name=na,subjects=subj)
fs.display()