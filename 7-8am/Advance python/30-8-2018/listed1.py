list1 =[1,2,3,4,5,6]
list2 =[20,30,40,50,60]
list1.append(list2)
print(list1)
print('---------------------------------')
list1 =[1,2,3,4,5,6]
list2 =[20,30,40,50,60]
list1.extend(list2)
print(list1)
print('--------------------------------')
list1 =[1,2,3,4,5,6]
list2 =[20,30,40,50,60]
list1.insert(1,68)
print(list1)
print('-------------------------------')
list1 =[1,2,3,4,5,6]
val =list1.pop(2)
print(val)
print(list1)
print('===============================================')
list1 =[1,2,3,4,5,6]
var =max(list1)
print(var)
print('==============================================')
list2 =[20,30,40,50,60,20,10,62]
var =min(list2)
print(var)
print('=========================================')
list2 =[20,30,40,50,60,20,10,62]
var =sum(list2)
print(var)
print('=======================================')
list2 =[20,30,40,50,60,20,10,62]
var=len(list2)
print(var)
print('=================================')
list2 =[20,30,40,50,60,20,10,62]
var=list2.index(30)
print(var)
print('===========================================')
list2 =[20,30,40,50,60,20,10,62]
var =list2.count(20)
print(var)
print("====================================")
list2 =[20,30,40,50,60,20,10,62]
list2.clear()
print(list2)
print('==========================')
list2 =[20,30,40,50,60,20,10,62]
list2.remove(20)
print(list2)
print('==============================')
list2 =[20,30,40,50,60,20,10,62]
del list2
print(list2)
print('==========================')
"""  
list2=[20,30,40,50,60,20,10,62]
print(list2[1:5])
"""
print('==================================')
l1 =[20,30,40,50,60,20,10,62]
l2=l1[1:5:2]

