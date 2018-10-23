
lst =[10,20,30,40,50,60]
lst .insert(2,68)                         # inserting an elmt into a list
print(lst)
print('-----------------------------------')
lst1 =[100,200,300,400,500,600,6668]              # removing a elmt from a list
lst1.remove(300)
print(lst1)
print('-----------------------------------')
lst2 =[201,202,203,204,205,206,207]
lst3 =[301,302,303,304,305,306,307]
lst4 =lst2 +lst3
print(lst4)  # it will take two list and add the two list and it will store all elmts in a another new list.
print('----------------------------------------------------------------------------------------------------=-')
"""
lst5 =[11,12,13,14,15,16,17]
lst6 =lst5+ 18    # we can able to add only two list but not a list and a integer
print(lst6)    # error

"""
print('----------------------------------------------------------------------------------')
lst7 =[1,2,3,4,5,6,7,2,1,6,5,7,2,3,6]
lst7.index(2)
print(lst7)
print('------------------------------------------')
lst8 =[61,62,63,64,65,66,68,69]
print(lst8)
lst8.clear()        # It will clear or remove  all the elements of a list.
print(lst8)
"""
print('-----------------------------------------------------------------------')
lst9 =[501,502,503,504,505,506,507,508,509]
print(lst9)
lst9.append(6668)    # it will add the elmts to the end of the list
print(lst9)
lst10 =[601,602,603,604,605,606,607,608,609]
lst9.append(lst10) # It will add the two  list and the 2nd list elmts are stored at end of the first or second list.
print(lst9)

print('--------------------------------------------------------------------------------')
lst11 =[701,702,703,704,705,706,707]
lst12 =[801,802,803,804,805,806,807]
lst11.extend(lst12)   #Extend it will take two list but it will add into a exisiting list only.
print(lst11)
print(lst12)
print('--------------------------------------------------------------------')
"""  
lst13 =[901,902,903,904,905,906,907,908]
print(lst13)
var =lst13.pop(2)
print(lst13)      # pop will remove the element from a list and returns the removed value.
print('The removed elmt is =',var)
print(var)
print('----------------------------------------------------------------')
lst14 =[661,662,663,664,665,666,668,669]
lst14.reverse()  # It will print the elmts in a reserve order.
print(lst14)
print('---------------------------------------------------------------------')
"""
lst15 =[15,16,17,18,19,20,21,22,23,24,25,26]
print(lst15)
print(lst15[1:6])   # This is a slice operator will print the from 1 to 6
print('----------------------------------------------')
lst16 =[661,662,663,664,665,666,668,669]
print(lst16[-6:-1])
print('--------------------------------------')
print(lst16[-3])
print('---------------------------------------')
print(lst16[-1:-6:-2])
print('-----------------------------------------')
print(lst16[-1:-9:-3])
print('------------------------------------------------------------------')
lst17 =[801,805,802,806,803,804,807,800,808]
lst17.sort()
print(lst17)
lst17.sort(reserve=True)
print(lst17)
print('-------------------------------------------')
lst18=[111,112,113,114,115,116,117,118]
lst18.index[2]
print(lst18)
print('-----------------------------------------------')

"""
"""