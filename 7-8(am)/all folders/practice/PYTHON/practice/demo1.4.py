n=int(input('enter a number'))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print('the given number is perfect number')
else:
    print('the given number is not perfect number')