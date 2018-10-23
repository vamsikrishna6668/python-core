#calculate the electricity bill depends on units
units=int(input('enter a no of units'))
if units<=150:
    print('no chares for 10 units')
elif units>150 and units<=300:
    price=5.46
    total_price=units*price
    tax=total_price*0.05
    customer_price=total_price+tax
    print('total cost:',total_price)
    print('tax:',tax)
    print('customer price:',customer_price)

else:
    price = 9.46
    total_price = units * price
    tax = total_price * 0.05
    customer_price = total_price + tax
    print('total cost:', total_price)
    print('tax:', tax)
    print('customer price:', customer_price)
