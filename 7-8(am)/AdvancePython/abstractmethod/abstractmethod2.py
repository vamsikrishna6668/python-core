from abc import ABC,abstractmethod
class bank(ABC):
    @abstractmethod
    def branch(self):
        pass
class ameerpet(bank):
    def branch(self):
        aadhar=int(input('enter a aadhar number:'))
        self.aadhar=aadhar
        self.pancard=str(input('enter a pancard no:'))
        self.bank=int(input('enter a bank balance:'))
        if self.aadhar==12 and len(self.pancard)==6:
            print('The aadhar card and pan card  details are correct')
        else:
            print('The aadhar and pan card details are not correct')
        if self.bank>=1000:
            print('The user is having sufficient amount in bank')
        else:
            print('The user is not having sufficient amount in bank')

    print('Welcome')
#calling block
a =ameerpet()
a.branch()

""" ,aadhar,pancard,bank 12233334,'cpipm88012',32037037191"""