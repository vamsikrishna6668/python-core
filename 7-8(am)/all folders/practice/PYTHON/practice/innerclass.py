class mobile:
    def __init__(self):
        self.mobilemodel='samsung'
        self.s=self.sim()
    def display(self):
        print('model nameis :',self.mobilemodel)
    class sim:
       def __init__(self):

           self.simprovider = 'jio'


       def dispalysim(self):

           print('sim provider is:', self.simprovider)



m=mobile()
m.display()
x=m.s
x.dispalysim()


