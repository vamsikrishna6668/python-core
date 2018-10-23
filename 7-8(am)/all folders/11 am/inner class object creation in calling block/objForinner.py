class  hyderabad:
    def __init__(self,a,b):
        self.a ='This is a sathya technologies'
        self.b ='Sathya tech is located in  ameerpet'
        self.q ='This is a training institue'
        # object creation for a inner class
        """ 
        self.A =self.Ameerpet(1,2)
        """
    def sathya(self,c,d):
        self.c='Iam learning python in sathya'
        self.d ='Python supports all kind of a applications'
        print(self.a)
        print(self.b)
        print(self.q)
        print('This is a sathya institute')
    def pythsathya(self,e):
        self.e ='Python is a easy programming language'
        print(self.c)
        print(self.d)
        print(self.e)
    class Ameerpet:
        def __init__(self,i,j):
            self.i ='Iam a Malayalee'
            self.j ='I can speak Tamil'
            self.k ='I want to become a  Researcher in my domain '
            print(self.i)
            print(self.j)
            print(self.k)
        def hydbiryani(self):
            self.z =90
            print('Hyderabad  is famous for a biryani')
        def dumbiry(self):
            self.m= 66
            print(self.z)
            print(self.m)
#calling block
hy =hyderabad('ameer','ismail')
hy.sathya('basha','anji')
hy.pythsathya('chanti')
"""
amer =hy.A
amer.dumbiry()
amer.hydbiryani()

"""
