import re
mystr='prasadnaidu766@gmail.com , prasadlegend766@redifmail.com ,  naiduprasad766@gmail.com'
results=re.sub(r'g[a-z]*\.com$','outlook.com',mystr)
print(results)
print('======================================')
results2=re.sub(r'g[a-z]*\.com','outlook.com',mystr)
print(results2)
print('==============================')
result3=re.sub(r'.com$','outlook.com',mystr)
print(result3)
