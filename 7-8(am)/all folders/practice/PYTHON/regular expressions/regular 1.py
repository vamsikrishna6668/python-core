import re
mystr='man van ran jan'
result=re.search(r'm[a-z]*',mystr)
print(result.group())

print('=========================================')
result2=re.findall(r'[a-z]*an',mystr)
print(result2)