import re
mystr='hello prasad how are you'
result=re.match(r'[a-z]+ad',mystr)
if result is None:
    print('not exists')
else:
    print(result.group())
