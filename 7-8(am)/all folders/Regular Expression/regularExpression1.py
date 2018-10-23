# search
import re
mystr ='ismail anji anil  sunil'
result =re.search(r'[a-z]*il',mystr)
print(result.group())
# output:  ismail
print('-----------------------------------')
#find all
result =re.findall(r'[a-z]*il',mystr)
print(result)
# output: ['ismail', 'anil', 'sunil']
print('----------------------------------------')
