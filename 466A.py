rides,rides_per_super,price_normal,price_super= [int(x) for x in input().split()]   


k=int(rides/rides_per_super)

if k*rides_per_super==rides:
	print(min(price_normal*rides,k*price_super))
else  : print(min(price_normal*rides,k*price_super+(rides-k*rides_per_super)*price_normal,price_super*(k+1)))

