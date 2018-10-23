def display(id,name=101,sal=125050.00):
    print('id=',id)
    print('name=',name)
    print('sal=',sal)
#calling block
# display()         # This is a error bcz we don't assign the value for a id
print('-----------------------------')
display(102)
print('-----------------------------')
display(200,230,120.2352)
print('-----------------------------')
display(201,sal=25005582.0)