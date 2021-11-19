i=input()
for _ in range(int(i)):
	n =int(input())
	l=map(int,input().split(" "))
	z=0
	for i,m in enumerate(l):
		if m>i+1:
			z1=max(m-i-1,0)
			if z1>z:
				z=z1

	print(z)