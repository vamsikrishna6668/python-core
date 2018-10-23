from abc import ABC,abstractmethod
class pizza(ABC):
    @abstractmethod
    def calucatebill(self):
        pass
class veg(pizza):
    def calucatebill(self,items,cost):
        self.items=items
        self.cost=cost
        self.with_discount=(self.items*self.cost)*0.04
        self.total=(self.cost*self.items)-self.with_discount
        if items>2:
            if self.total > 2000:
                print('The user will get Discount')
                print('The no of items=',self.items)
                print('The no of cost=', self.cost)
                print('The user got discount=', self.with_discount)
                print('The total amount=',self.total)
            else:
                print('The user will not get any discount')


        else:
            print('total of cost without discount',self.total)
            print(self.items)
            print(self.cost)
            print(self.total)
class nonveg(pizza):
    def calucatebill(self,items,cost):
        self.items=items
        self.cost=cost
        self.discount1=(self.cost*self.items)*0.10
        self.total_cost1=(self.cost*self.items)-self.discount1
        if items>1:
            if self.total_cost1>2000:
                print('The no of items =', self.items)
                print('The cost of a non-veg pizza=', self.cost)
                print('The discount for a pizza=', self.discount1)
                print('The total cost of a Pizza=',self.total_cost1)
            else:
                print('The user will not get any Discount')
        else:
            print('The total cost of the pizza without discount',self.total_cost1)

#calling block
c =veg()
c.calucatebill(4,1000)
print('-------------------------')
n =nonveg()
n.calucatebill(4,1000)