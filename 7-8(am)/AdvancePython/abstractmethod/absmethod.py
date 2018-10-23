from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class card(payment):
    def pay(self,amount):
        self.amount=amount
        print(self.amount,'is paid with card')
#calling block
c =card()
c.pay(5000)


