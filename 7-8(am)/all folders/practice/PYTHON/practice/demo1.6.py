import datetime
d1,m1,y1=[int(x) for x in input('enter your date of birth(dd/mm/yyy):').split('/')]
#date_of_birth=datetime.date(y1,m1,d1)
date_of_birth=datetime.date(day=d1,month=m1,year=y1)

print('your date of birth is:',date_of_birth)
