import math
n=45    #n=145 => Strong number
t=n
Sum=0
while n!=0:
	r=n%10
	F=math.factorial(r)
	n//=10
	Sum+=F
if Sum==t:
	print("Strong number") 
else:
    print("Not String number")