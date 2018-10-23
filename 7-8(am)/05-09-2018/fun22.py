# 22. W.A.P on function with default parameters values by using a single function of display and creating the object for Multiple times?
def display(idno=101,name='ismail',sal=200000):
    print("Iam Display ")
    print(idno)
    print(name)
    print(sal)

#call
display()
print('--------------')
display(102)
print('------------------')
display(name='basha')
print('----------------')
display(sal=35000000)
print('----------------------')
display(name='ismailbasha',idno=94)


"""
Output:
Iam Display 
101
ismail
200000
--------------
Iam Display 
102
ismail
200000
------------------
Iam Display 
101
basha
200000
----------------
Iam Display 
101
ismail
35000000
----------------------
Iam Display 
94
ismailbasha
200000

Process finished with exit code 0


"""