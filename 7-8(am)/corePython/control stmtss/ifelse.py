adults=int(input('No of adults:'))
childs=int(input('No of childs:'))
adult_cost=500
child_cost=500/2
adult_discount=(adult_cost*adults)*0.05
child_discount=(adult_cost*childs)*0.10
total_cost_adults=(adult_cost*adults)-adult_discount
total_cost_childs=(adult_cost*childs)-child_discount
if total_cost_adults>2000:
    print('no of adults:',adults)
    print('adults discount:',adult_discount)
    print('total cost of adults:',total_cost_adults)
else:
    print('no of adults:', adults)
    print('totalcost of ticket:',adults*adult_cost)
print('Welcome')
if total_cost_childs>1000:
    print('no of childs:',childs)
    print('adults discount:',child_discount)
    print('total cost of childs:',total_cost_childs)
else:
    print('no of childs:',childs)
    print('totalcost of ticket:',adults*child_cost)
