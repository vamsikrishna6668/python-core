s =input("enter a s's  string:")
n =input("enter a n's string:")
p =input("enter a p's string:")
if len(s)>len(n):
    print('s is bigger and n is small')
if len(n)>len(s):
    print("n is bigger and s is small")
if len(p)>len(s):
    print('p is bigger and s is small')
if len(n)>len(p):
    print('n is bigger and p is small')
if len(p)>len(n):
    print('p is bigger and n is small')
if len(s)>len(p):
    print('s is bigger and p is small')
print('Welcome')
