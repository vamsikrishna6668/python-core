n=int(input('enter a number:'))
count=0
for x in range(1,n+1):
    if n%x==0:
        count+=1
if count==2:
        print('the given number is prime number')
else:
    print('not a prime number')