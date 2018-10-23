l1 =[101,102,103,104,105,106,107,108]
print(l1)
print('-----------------------------------')
l1[6]=68
print(l1)
print('-----------------------------------')
l2 =[1,2,3,4,5,6,7,8,9,10]
print(l2)
print('-----------------------------------')
#l3 =l1+2              # error
#print(l3)
print('-----------------------------------')
l3 =l1+l2
print(l3)    # we can add two different  lists but not able to add the list and integer element
print('-----------------------------------')
#l3 =l1 * l2   # we cannot  multiply the two list we can multiply one list and element or vlaue or integer
#print(l3)
print('-----------------------------------')
l3 =l1 *3
print(l3)
print('-----------------------------------')
l3 =l1+l1
print(l3)
print('-----------------------------------')
l3 =l2 * 4
print(l3)
print('-----------------------------------')
print(l1[-1:-11:-2])
print('-----------------------------------')
print(l1[-9:-1])
print('-----------------------------------')
print(l1[-1:-11])
print('-----------------------------------')
total =sum(l1)
print('The total of sum=',total)
print('-----------------------------------')
big =max(l1)
print('The big of element=',big)
print('-----------------------------------')
small =min(l1)
print('the small of element =',small)
print('-----------------------------------')
length =len(l1)
print('The length number of a number=',length)