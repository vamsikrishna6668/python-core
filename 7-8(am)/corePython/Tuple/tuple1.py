t1=(68,10,32,43,3,5,55,665,3342,123,4321,3456,5432,12,10,66,68,66,68,10,'ismail',True,66.68)
t2 =(12,23,43,12,22,12,22,23,12,43,45,65,67,77,98,88,22,12,22,33,43,12,22,33)
print(t1)
coun =t1.count(68)
print(coun)
print('------------------------------------')
ind =t1.index(68)
print(ind)

print('-------------------------------------')
""" 
t1.insert(1,10)       #AttributeError: 'tuple' object has no attribute 'insert'

print(t1)
"""
print('-----------------------------------------------------------------------------')
""" 
t1.append(t2)    #AttributeError: 'tuple' object has no attribute 'append'
print(t1)
"""
t =1,23,45     # ValueError: too many values to unpack (expected 3)
print(t2)
print(type(t2))
a,b,c=t
print(t1)
print(a)
print('--------------------------------------------------------------------------------')
"""
t2 =(12,23,43,12,22,12,22,23,12,43,45,65,67,77,98,88,22,12,22,33,43,12,22,33)
t2.remove(45)    #AttributeError: 'tuple' object has no attribute 'remove'
print(t2)
"""
print('---------------------------------------------------------------------------------')
"""
t3=(12,23,43,12,22,12,22,23,12,43,45,65,67,77,98,88,22,12,22,33,43,12,22,33)
t3.clear() # AttributeError: 'tuple' object has no attribute 'clear'
"""
print('------------------------------------------------------------------------------------')
