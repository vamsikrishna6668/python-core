#count ,replace,length, upper, lower of the string
str='hello prasad how are you? where are you prasad'
print(len(str))
s2=str.count('prasad')
print(s2)
s3=str.replace('prasad','raju')
s5=str.replace('hello','hi')
print(s5)
print(s3)
s4=str.upper()
print(s4)
str2='hello prasad how are you'
s6=str2.lower()
print(s6)
username='prasadnaidu766@gmail.com'
password=9052766763
print(username.startswith('prasad'))
print(username.endswith('.in'))
str4='12345'
print(str4.isdigit())
str5='12345r'
print(str5.isdigit())
my_str='python', 'bigdata', 'datascience'
print(my_str.split(','))

