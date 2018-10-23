shirts =int(input('No of shirts:'))
pants =int(input('No of pants:'))
shirts_cost =2500
pants_cost =3000
shirts_discount=(shirts*shirts_cost)*0.10
pants_discount=(pants*pants_cost)*0.15
total_shirts_cost=(shirts*shirts_cost)-shirts_discount
total_pants_cost=(pants*pants_cost)-pants_discount
if total_shirts_cost>5000:
    print('No of shirts=',shirts)
    print('No of shirts discount=',shirts_discount)
    print('No of total shirts cost=',total_shirts_cost)
else:
    print('No of shirts=', shirts)
    print('No of total shirts cost=',shirts_cost*shirts)
if total_pants_cost > 6000:
        print('No of pants=', pants)
        print('No of pants discount=',pants_discount)
        print('No of total pants cost=',total_pants_cost)
else:
        print('No of pants=',pants)
        print('No of total pants cost=',pants_cost *pants)
print('WELCOME')


