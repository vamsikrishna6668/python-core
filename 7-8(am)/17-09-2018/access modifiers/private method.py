__a=68
print("The Global Variable value:",__a)

def __fun1(i,j):
    i=50
    __j=70
    print(__a+i)
    print(__a+__j)
    print("Iam function of a private")


class Employee:
    __b=66
    print(__b)
    def __init__(self):
        __s=26
        print("Iam a constructor of Employee Class")
        self.id=101
        self.cno=8500580594
        print("The Employee ID No:", self.id)
        print("The Employee contact No:",self.cno)
        self.wemp = self.__worker_emp()      # created the object for the inner class.

    def __show(self):  # we Cann't able to access the private methods outside a class.
        self.cmp_name='IBM'
        print("The Company Name:",self.cmp_name)
        print("Iam a show Method of Employee")
        global __a
        __a += 10
        print("The global Variable value after the increment:", __a)

    class __worker_emp:
        def __init__(self):
            print("Iam a Constructor of worker Employee class")

        def assign(self):   # we Cann't able to access the private methods outside a class.
            self.__sal_incre=120000  # we can able to access the private variables outside a class also.
            print("Iam assign of a  Employeeworker class")

        def display(self):
            self.__sal_bonus="1.8Lpa"  # we can able to access the private variables outside a class also.
            print("The EmployeeWorker salary Incerement :",self.__sal_incre)
            print("The EmployeeWorker salary Bonus:",self.__sal_bonus)
            print("Iam a Display of a EmployeeWorker class")
#call
print(__a)
a=__fun1(1,2)
c=Employee()
#c.__show()
e=c.wemp
e.assign()
e.display()

"""
Private Functions:

Like most languages, Python has the concept of private elements:

1. Private functions, which can't be called from outside their module
2. Private class methods, which can't be called from outside their class
3. Private attributes, which can't be accessed from outside their class.
4. Unlike in most languages, whether a Python function, method, or attribute is private or public is determined entirely by its name.

5.If the name of a Python function, class method, or attribute starts with (but doesn't end with) two underscores, it's private; everything else is public.
   Python has no concept of protected class methods (accessible only in their own class and descendant classes). 
   Class methods are either private (accessible only in their own class) or public (accessible from anywhere).

"""