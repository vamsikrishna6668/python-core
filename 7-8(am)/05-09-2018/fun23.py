# 23. W.A.P on function with non default and default parameters with a function name display ?
def display(idno,name='Ismail',salary=890000):
    print("The id no:",idno)
    print("The name is:",name)
    print("The salary :",salary)
    print("Iam Display")
#call
display(101)
"""
Output:
The id no: 101
The name is: Ismail
The salary : 890000
Iam Display

Process finished with exit code 0
"""
print("-----------------------------------")
display(idno=102,name='basha')


"""
Output:
The id no: 102
The name is: basha
The salary : 890000
Iam Display

Process finished with exit code 0
"""
print("======================================")

display(idno=103,salary=68000000)
"""
The id no: 103
The name is: Ismail
The salary : 68000000
Iam Display

Process finished with exit code 0

"""
print("============================================")
display(idno=104,name="ismail basha",salary=30000000)
"""
Output:
 
The id no: 104
The name is: ismail basha
The salary : 30000000
Iam Display

Process finished with exit code 0

"""
print("========================================================")

