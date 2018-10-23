import datetime
d1,m1,y1=[int(x) for x in input('enter first date (dd/mm/yyy)').split('/')]
d2,m2,y2=[int(x) for x in input('enter second date(dd/mm/yyy)').split('/')]
first_date=datetime.date(y1,m1,d1)
second_date=datetime.date(y2,m2,d2)
delta=first_date-second_date
days=int(delta.days)
print('differnce between two dates of the year:',days//365)
print('differnce between two dates of the months:',days//30)
print('differnce between two dates of the weeks:',days//7)
print('differnce between two dates of the days:',days)
