# List class method
print('--------------------------------------')
# Append

l1 =[1,2,3,4,5,5,6,7,8,9,0,11]
n =[10,20,30,40,50,60,70]
l1.append(n)                # It will add an item or elements  to the end of the list.
print('append=',l1)
print('------------------------------------------------------------------------------------')

# Extend
l1 =[1,2,3,4,5,5,6,7,8,9,0,11]
print(l1)
l2 =[10,20,303,404,505,407,94,6866,90,81,22]
print(l2)
l1.extend(l2)
print(l1)
print(l2)

l2.extend(l1)
print(l2)
print('------------------------------------------------------------------------------------')
# Index
l1 =[1000,2002,30002,258885986]
l1.insert(1,680)
print(l1)

L2 =[1,2,3,5,6,67,896,698,875,68,66,66986,875457]
l2.insert(0,68)
print(L2)
print('------------------------------------------------------------------------------------')
 # Remove
nag =[102,302,304,405,595,904,3092,4567]
nag.remove(302)
print(nag)

nag.remove(595)
print(nag)
print('------------------------------------------------------------------------------------')

# pop

s1 =[201,301,401,501,601,701]
print(s1)
val =s1.pop(1)
print(val)

val1 =s1.pop(4)
print(val1)
print(s1)
print('--------------------------------------------------------------------------------------------')

# clear

n1 =[66,68,91,23,41,48,46,51,61,62]
val=n1.clear()
print(val)

print('----------------------------------------------------------------------')
# index
n2 =[10,20,30,40,10,20,40,30,60,10]
print(n2)
n2.index()
print(n2)

# sort
se =[1,4,2,7,5,6]
print(se)
se.sort(asce)
print(se)
