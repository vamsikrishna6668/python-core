minitues=300
costmonthlypay=2000
costperminitue=0.45
taxes=12.5
minituesused=int(input('enter no of minitues'))
if minitues<minituesused:
    taxes=costmonthlypay*12/100
    monthlybill=costmonthlypay+taxes
else:
    difference=minituesused-minitues
    extracost=difference*costperminitue
    taxes=(costmonthlypay+extracost)*12/100
    monthlybill=(costmonthlypay+extracost)+taxes
print('difference=',difference)
print('extracost=',extracost)
print('taxes=',taxes)
print('monthlybill=',monthlybill)
