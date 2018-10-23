from abc import ABC,abstractmethod
class saree(ABC):
    @abstractmethod
    def cotton(self):
        pass
class kanchi(saree):
    showroom_name = 'chennai silks'
    showroom_location = 'Tambaram'
    def cotton(self,different_Typesofsarees='All Types of saree are Available in Chennai silks shopping mall Visit once Again'):
        Items_women=int(input('Enter a no of Items purchased by  women:'))
        patussarees=2000
        banarassarees=3000
        dharmavarampatusarees=5000
        mangalagiricottonsarees=2500
        bombaycottonsarees=2100
        women_purchasedscost=10000
        women_discount=(Items_women*women_purchasedscost)*0.25
        total_cost_women=(Items_women*women_purchasedscost)-women_discount
        self.patussarees=patussarees
        self.banarassarees=banarassarees
        self.dharmavarampatusarees=dharmavarampatusarees
        self.mangalagiricottonsarees=mangalagiricottonsarees
        self.bombaycottonsarees=bombaycottonsarees
        self.women_purchasedscost = women_purchasedscost
        self.different_Typesofsarees=different_Typesofsarees
        print("The Cost of patu saree's in chennai :", self.patussarees)
        print(" The Cost of  banaras saree in chennai: ", self.banarassarees)
        print("The Cost of  dharmavarampatu saree's in chennai:", self.dharmavarampatusarees)
        print("The Cost of  mangalagiri cotton saree's in chennai:", self.mangalagiricottonsarees)
        print("The Cost  of Bombay cotton  Saree's in chennai:", self.bombaycottonsarees)
        print(" The Different types of saree's in Chennai:", self.different_Typesofsarees)
        print("This is end of the women's section in the shoppning of chennai")
        if self.patussarees > 2000 and self.banarassarees > 3000:
            print("The women got the Discount for the both the saree's")
        else:
            print("The women does n't have any  Discount for the both the saree's")
        if self.patussarees > 2000 and self.dharmavarampatusarees > 3500:
            print("The women got the Discount for the both the saree's")
        else:
            print("The women does n't have any  Discount for the both the saree's")
        if self.patussarees > 2000 and self.mangalagiricottonsarees > 1500:
            print("The women got the Discount for the both the saree's")
        else:
            print("The women does n't have any  Discount for the both the saree's")
        if self.patussarees > 2000 and self.bombaycottonsarees>2100:
            print("The women got the Discount for the both the saree's")
        else:
            print("The women does n't have any  Discount for the both the saree's")
        if self.banarassarees > 3000 and self.dharmavarampatusarees > 3500:
            print("The women got the Discount for the both the saree's")
        else:
            print("The women does n't have any  Discount for the both the saree's")
        if self.banarassarees > 3000 and self.dharmavarampatusarees > 3500:
            print("The women got the Discount for the both the saree's")
        else:
            print("The women does n't have any  Discount for the both the saree's")
        if self.banarassarees > 3000 and self.mangalagiricottonsarees > 1500:
            print("The women got the Discount for the both the saree's")
        else:
            print("The women does n't have any  Discount for the both the saree's")
        if self.banarassarees > 3000 and self.bombaycottonsarees>2100:
            print("The women got the Discount for the both the saree's")
        else:
            print("The women does n't have any  Discount for the both the saree's")
        if self.dharmavarampatusarees > 3500 and self.bombaycottonsarees>2100:
            print("The women got the Discount for the both the saree's")
        else:
            print("The women does n't have any  Discount for the both the saree's")
        if self.dharmavarampatusarees > 3500 and self.mangalagiricottonsarees > 1500:
            print("The women got Discount for the both the saree's")
        else:
            print("The women does n't have any  Discount for the both the saree's")
        if self.bombaycottonsarees>2100:
            print("The women got Discount for the bombay cotton saree's")
        else:
            print("The women does n't have any  Discount  for thee bombay cotton saree's")
        print('-----------------------------------------------------------------------------------------------------')
        Items_men = int(input('Enter a no of Items  purchased by men:'))
        cotton_shirts = 1500
        silk_shirts = 1200
        cottonandsilk_mix = 2300
        buffalo_shirts = 5000
        flying_machine=5500
        men_purchasedcost = 100000
        self.cotton_shirts=cotton_shirts
        self.silk_shirts=silk_shirts
        self.cottonandsilk_mix=cottonandsilk_mix
        self.buffalo_shirts=buffalo_shirts
        self.flying_machine=flying_machine
        self.men_purchasedcost=men_purchasedcost
        men_discount = (Items_men * men_purchasedcost) * 0.15
        total_cost_men = (Items_men * men_purchasedcost) - men_discount
        print('The cost of the  cotton shirts:',self.cotton_shirts)
        print('The cost of the  silk shirts:',self.silk_shirts)
        print('The cost of the  cotton and silk mix shirts:',self.cottonandsilk_mix)
        print('The cost of the buffalo shirts   shirts:',self.buffalo_shirts)
        print('The cost of the flying machine shirts:',self.flying_machine)
        print("This is the end of the men's section in the shoppning of chennai")
        print("Welcome to chennai shopping mall and Thank you for Visiting the Mall")

        if self.cotton_shirts>2500 and  self.silk_shirts>3000:
            print("The men got Discount for the both the shirt's")
        else:
            print("The men does n't have any  Discount for the both the shirt's")
        if self.cottonandsilk_mix>2500 and  self.buffalo_shirts>3000:
            print("The men got Discount for the both the shirt's")
        else:
            print("The men does n't have any  Discount for the both the shirt's")
        if total_cost_women>20000:
            print("The no of Items purchased by women:",Items_women)
            print("The discount offered for saree of women:",women_discount)
            print("The total amount on purchased items:",total_cost_women)
        else:
            print("The no of Items purchased by women:", Items_women)
            print("The total amount on purchased items:",Items_women*women_purchasedscost)
        if total_cost_men>20000:
            print("The no of Items purchased by men:",Items_men)
            print("The discount offered for shirts for the men:",men_discount)
            print("The total amount on purchased items:", total_cost_men)
        else:
            print("The no of Items purchased by men:",Items_men)
            print("The total amount on purchased items:",Items_men*men_purchasedcost)

#calling block
sare =kanchi()
kanchi.showroom_name
kanchi.showroom_location
sare.cotton()



