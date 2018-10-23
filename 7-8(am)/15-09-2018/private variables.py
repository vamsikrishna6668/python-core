class A:
    def __init__(self,amount):
        self.amount=amount
        print("The Amount=",self.amount)
        print("Iam a Constructor of Class A")
    def assign(self,balance):
        self.balance=balance
        print("Iam a Assign Method of a class A ")
    def show(self):
        print("Iam Private variable of class A:",self.balance)
        print("Iam show of a class A ")
        self.b=self.__B

    class __B:
        def __init__(self,bank):
            self.__bank=bank
            print("Iam a Constructor of B")
            print("The instance variable of a private Method:", self.__bank)
        def display(self,mnywithdrawn):
            self.mnywithdrawn=mnywithdrawn
            print("Iam display method of a class B private variable")
#call
a=A(1200000)
a.assign(20000)
a.show()
b1=a.b(1234)
b1.display(3000)

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