sathya_python =int(input('Enter a  no of Students in sathya:'))
lokesh_python=int(input('Enter a  no of Students in lokesh:'))
sathya_cost=2500
lokesh_cost=2500
sathya_python_discount=(sathya_python*sathya_cost)*0.10
lokesh_python_discount=(lokesh_python*lokesh_cost)*0.10
total_sathya_cost=(sathya_python*sathya_cost)-sathya_python_discount
total_lokesh_cost=(lokesh_python*lokesh_cost)-lokesh_python_discount
if total_sathya_cost>2500 and total_lokesh_cost>2500:
    print('The No of students in sathya Institute:',sathya_python)
    print('The Discount offered by the sathya Institute:', sathya_python_discount)
    print('The total cost for the python in sathya institute after the discount:',total_sathya_cost)
    print('The No of students in lokesh Institute:', lokesh_python)
    print('The Discount offered by the lokesh Institute:', lokesh_python_discount)
    print('THe total cost for the python in lokesh institute after the discount:',total_sathya_cost)
else:
    print('The No of students in sathya Institute:', sathya_python)
    print('The total cost for the python in sathya institute without any discount:',sathya_python*sathya_cost)
    print('The No of students in lokesh Institute:', lokesh_python)
    print('THe total cost for the python in lokesh institute without any discount:',lokesh_python*lokesh_cost)

