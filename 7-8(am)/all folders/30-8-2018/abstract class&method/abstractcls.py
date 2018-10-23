from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class card(payment):
    def pay(self):
        print('pay','paid with a card')
#calling block
c =card()
c.pay()