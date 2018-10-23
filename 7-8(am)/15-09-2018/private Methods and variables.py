class mobile:
    def __init__(self):
        self.model="Nokia"
        self.price=12000
        print("The mobile is:", self.model)
        print("The price of a Mobile is:",self.price)
        print("Iam Constructor of a Mobile class")
        self.sm=self.__sim()
    class __sim:
        def __init__(self):
            self.provider='Aircel'
            print("Iam a constructor of Sim class")
        def __display(self):
            print("Iam Display")
            print("The service provider is:", self.provider)
#calling block
m=mobile()
s=m.sm
#s.display()

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