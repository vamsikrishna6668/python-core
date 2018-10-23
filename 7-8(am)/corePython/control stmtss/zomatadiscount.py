veg =int(input('No of items of veg:'))
nonveg =int(input('No of items of Non-veg:'))
vegcost=200
nonvegcost=300
vegdiscount=(veg*vegcost)*0.10
nonvegdiscount=(nonveg*nonvegcost)*0.10
totalcostveg=(veg*vegcost)-vegdiscount
totalcostnonveg=(nonveg*nonvegcost)-nonvegdiscount
if totalcostveg>200:
    print('The no of items of veg:',veg)
    print('The no of items for veg discount:', vegdiscount)
    print('The no of items of totalvegcost:',totalcostveg)
else:
    print('The no of items of veg:',veg)
    print('The total cost  of veg:',veg*vegcost)

if totalcostnonveg>300:
    print('The no of items of nonveg:',nonveg)
    print('The no of items for non-veg discount:',nonvegdiscount)
    print('The total cost of the items:',totalcostnonveg)
else:
    print('The no of items of nonveg:',nonveg)
    print('The total no of items of nonveg:',nonveg*nonvegcost)

print('Thanking for ordering in the zomato')
