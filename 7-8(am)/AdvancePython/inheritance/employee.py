class sathyaemployee:
    comp_name='Sathya'
    comp_cno=8500580594
    def __init__(self,idno,name='none',subjects=[]):
        self.idno=idno
        self.name=name
        self.subjects=subjects
    def  display(self):
        print('The idno is: ',self.idno)
        print(' The name is:',self.name)
        print("faculty subjects")
        for x in self.subjects:
            print(x)

