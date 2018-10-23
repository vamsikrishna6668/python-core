boys=int(input('Enter no of boys:'))
girls=int(input('Enter no of girls:'))
boys_holidaytrip=500
girls_holidaytrip=350
boys_discount=(boys_holidaytrip*boys)*0.10
girls_discount=(girls_holidaytrip*girls)*0.10
total_cost_boys=(boys_holidaytrip*boys)-boys_discount
total_cost_girls=(girls_holidaytrip*girls)-girls_discount
if total_cost_boys>500and total_cost_girls>500:
    print('No of boys:',boys)
    print('the discount for boys:',boys_discount)
    print('The total cost for boys:',total_cost_boys)
    print('No of girls:', girls)
    print('the discount for girls:',girls_discount)
    print('The total cost for girls:',total_cost_girls)
else:
    print('No of boys:',boys)
    print('The total cost for boys:',boys*boys_holidaytrip)
    print('No of girls:',girls)
    print('The total cost for girls:',girls*girls_holidaytrip)
print('Thanking  for Enjoying the Summer Holiday Trip Visit Once Again')



