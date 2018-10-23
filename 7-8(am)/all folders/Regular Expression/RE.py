# match
import re
mystr ='Ismail anji Basha babu Vamsi'
rslt=re.match(r'I\w\w',mystr,re.IGNORECASE)
if rslt is None:
    print('not exist')
else:
    print(rslt.group())
# output: Ism --> It is printing only the Matched, first three characters of a string.
