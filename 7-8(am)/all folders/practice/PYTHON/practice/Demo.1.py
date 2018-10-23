class reservation:
    available_seats=100#static variable
    def __init__(self,required_seats):# constructor
        self.required_seats=required_seats
    def reserve(self):#instance method
        if reservation.available_seats>=self.required_seats:
            reservation.available_seats-=self.required_seats
            return 'seats are reserved'
        else:
            return 'sorry {} are available'.format(reservation.available_seats)
r1=reservation(50)
msg=r1.reserve()
print(msg)
print('--------------------------------------------')
r2=reservation(75)
msg1=r2.reserve()
print(msg1)





