# Demo 4
#  importing all from sample

import sample
print(sample.a)
print(sample.fun1(30,60))

#creating object for Employeee class
emp=sample.Employee()
emp.assign("anji")
emp.display()
print(sample.Employee.empsalincrement)
print(sample.Employee. empsalyearlybonus)


"""
output:

The golbal Variable value before a function: 50000
50000
1030
Iam assign of a Employee
anji
Iam Display
300000
20000

Process finished with exit code 0
"""