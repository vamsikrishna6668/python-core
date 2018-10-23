class drinks:              # outer  class
    def __init__(self):         # outer class constructor
        print('This is  a constructor of outer class block')
    def bottle(self,s,p):        # This is a instance method ,s&p are local variables
        self.a =s
        self.f =p
        print('This is a glass bottle slot')
    def pupbottle(self):
        self.a ='sprite'        # instance variables
        self.f ='frooti'
        print(self.a)
        print(self.f)
        print('This is a pupbottle slot')
        print('This is a end of the outer class ')
class wine:               # another  class
    def __init__(self):       # another class constructor
        print('This is a inner class constructor')
    def redwine(self,w):           # instance method of a inner class
        self.w ='sula wine'        # instance variables
        self.q ='whisky'
        print('This is a redwine slot')
    def bluewine(self):
        print(self.w)
        print(self.q)
        print('This is a bluewine')
        print('This is a end of the inner class')
#calling block
d =drinks()                    # outer class calling
d.bottle('pepsi','frooti')
d.pupbottle()

f =wine()                    # inner class calling
f.redwine('Rum')
f.bluewine()
