veg_cake=int(input('No of Veg cakes:'))
nonveg_cake=int(input('No of nonVeg cakes:'))
vegcake_cost=300
nonvegcake_cost=350
vegcake_discount=(veg_cake*vegcake_cost)*0.05
nonvegcake_discount=(nonveg_cake*nonvegcake_cost)*0.04
total_vegcake_cost=(veg_cake*vegcake_cost)-vegcake_discount
total_nonvegcake_cost=(nonveg_cake*nonvegcake_cost)-nonvegcake_discount
if total_vegcake_cost>=600 and total_nonvegcake_cost>=700:
    print('The no of items of veg cake:',veg_cake)
    print('The discount got for a veg cake:',vegcake_discount)
    print('The total amount for the veg cake cost:',total_vegcake_cost)
    print('The no of items of  non-veg cake cost',nonveg_cake)
    print('The discount for the non-veg cake cost',nonvegcake_discount)
    print('The total amount for the non-veg cake cost:',total_nonvegcake_cost)
else:
    print('The no of items of a veg cake:',veg_cake)
    print('The total cost for a veg cake:',total_vegcake_cost)
    print('The no of items of a non -veg cake cost:',nonveg_cake)
    print('The total cost for a non veg cake:',total_nonvegcake_cost)
print('The Welcome for ordering in uber eats visit once again')