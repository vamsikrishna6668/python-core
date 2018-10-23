#five types of arguments
def assign(*args):#positional arguments
   sum=0
   for i in args:
       sum+=i
   print('output as sum:',sum)
assign(10,20,30)
assign(1,2,3,4,9)
assign(23,34,12)