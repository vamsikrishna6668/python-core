"""list1=[10,20,30,40]
list2=[20,30,40,50]
list3=list1+list2
list4=list3*2
print(list4)
print('-----------------------------------------------')

print(list1*2)
print('-----------------------------------------------')
print(list2*3)
print('-----------------------------------------------')
list5=[10,20,30,40]
list6=[1,2,3]
list5.extend(list6)
print(list)
print('--------------------------------------------------')
list7=[10,20,30]
list7.append(40)
list7.append(50)
print(list7)
print('---------------------------------------------------')
list8=[100,200,300,400]
list8.insert(3,500)
print(list8)
print('-------------------------------------------------------')

list9=[10,True,23,2,1,67]
print(max(list9))
print(min(list9))
print(sum(list9))
del list9[3]
print(list9)
print('-----------------------------------------------------------')
mylist=['p','a','r','l','l','e','l']
del mylist[2:4]
print(mylist)
print('---------------------------------------------------------------')
mylist2=[10,20,30,40]
del mylist2
print(mylist2)
print('----------------------------------------------------------------')

mylist3=[100,200,300,400,1,2,3]
m2=mylist3.sort()
print('ascending orderr is:',mylist3)
print('---------------------------------------------')
m3=mylist3.sort(reverse=True)
print('desending order is:',mylist3)
mylist4=[['ravi,1122,200000'],['prasad',3344,23000],['abhi',1022,10000]]
mylist4.sort()
print(mylist4)
print('------------------------------------------')
mylist4.sort(reverse=True)
print(mylist4)
print('------------------------------------------------------')
mylist4=[['ravi,1122,200000'],['prasad',3344,23000],['abhi',1022,10000]]
mylist4.sort(key=lambda x:x[0][2],reverse=True)
print(mylist4)
mylist5=['advpython',2500,45]
course,fee,days=mylist5
print(course)
print(days)
print(fee)
mylist6=[x for x in input('enter the values  separrate with camma'). split(',')]
print(mylist6)"""
mylist7=[x for x in range(1,100) if x%2!=0]
print(mylist7)
