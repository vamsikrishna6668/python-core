Rolex=int(input('Enter no of Rolex Watches:'))
fastrack=int(input('Enter no of Fastrack Watches:'))
Rolex_watchcost=30000
fastrack_watchcost=10000
Rolex_discount=(Rolex*Rolex_watchcost)*0.25
fastrack_discount=(fastrack*fastrack_watchcost)*0.15
total_Rolex_watchcost=(Rolex*Rolex_watchcost)-Rolex_discount
total_fastrack_watchcost=(fastrack*fastrack_watchcost)-fastrack_discount
if total_Rolex_watchcost>30000 or total_fastrack_watchcost>10000:
    print('The No of watches of Rolex:',Rolex)
    print('The Discount got for watch of Rolex:',Rolex_discount)
    print('The total cost of the watch for Rolex after the Discount:',total_Rolex_watchcost)
    print('The No of watches of fasttrack:',fastrack)
    print('The Discount got for watch of fasttrack:', fastrack_discount)
    print('The total cost of the watch for fasttrack after the Discount:',total_fastrack_watchcost)
else:
    print('The No of watches of Rolex:', Rolex)
    print('The total cost of the watch for Rolex without  the Discount:',Rolex*total_Rolex_watchcost)
    print('The No of watches of fastrack:',fastrack)
    print('The total cost of the watch for fastrack without  the Discount:',fastrack*total_fastrack_watchcost)
print('Thanking for visiting your store and you are Welcome')