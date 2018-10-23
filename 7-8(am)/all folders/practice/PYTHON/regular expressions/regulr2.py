import re
mystr='prasad got 95 marks in maths naidu got 76 marks in maths'
result=re.search(r'\d{2}',mystr)
sum=0
for i in result:
    sum+=i
print(sum)