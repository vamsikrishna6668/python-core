user=input('enter a username:')
passwd=input('enter a passwd:')
if user.startswith('ismail') and passwd.endswith('basha'):
    print('The username and password are correct')
else:
    print('The username and password are not correct')