d1 ={'101':[1,2,3,4,5,6,7,8,9],
     '102':[20,30,40,50,60,70,80,90],
     '103':[90,80,70,60,50,40,30,20]
     }
for x in d1:
    print(x)    # output: 101
                # output: 102
                # output: 103
print('---------------------------------------------------')

d1 ={'101':[10,20,30,40,50,60,70,80,90],
     '102':[20,30,40,50,60,70,80,90],
     '103':[90,80,70,60,50,40,30,20]
     }
for key,value in d1.items():
    print("idno:" ,key,end=' ')
    print("highest mark:" ,max(value),end=' ')
    print("lowest mark:" ,min(value),end=' ')
    print("total mark :" ,sum(value))
    """ 
    Output: idno: 101 highest mark: 90 lowest mark: 10 total mark : 450
            idno: 102 highest mark: 90 lowest mark: 20 total mark : 440
            idno: 103 highest mark: 90 lowest mark: 20 total mark : 440
   """
print('-----------------------------------------------------')

d2 ={'idno':101,
      'name':'ismail',
       'salary':15000000
    }
for x in d2.keys():
    print(x)
""" 
#output 
    idno
    name
    salary
"""
print('-----------------------------------------')
d2 ={'idno':101,
      'name':'ismail',
       'salary':15000000
    }
for x in d2.values():
    print(x)
""" 
#output
    101
    ismail
    15000000
"""
print('-----------------------------------------')
d2 ={'idno':101,
      'name':'ismail',
       'salary':15000000
    }
for x in d2.items():
    print(x)
"""     
# output:
('idno', 101)
('name', 'ismail')
('salary', 15000000)
"""
print('------------------------------------------------')
d2 ={'idno':101,
      'name':'ismail',
       'salary':15000000
    }
for x in d2:
    print(x, '< >','values')
""" 
#output:
idno < > values
name < > values
salary < > values
"""
print('-------------------------------------------------------')
