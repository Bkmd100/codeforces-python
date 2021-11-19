import math
f=math.factorial


t=int(input())
for _ in range(t):
	n=int(input())
	l=list(map(int,input().split(" ")))
	s=sum(l)
	x=float(s*2/n)
	if not x.is_integer():
		print(0)
		continue
	x=int(x)
	black_list=set()
	i=0
	for j,v in enumerate(l[:-1]):

		if v>x or v in black_list:
			continue

		w=x-v
		if w==v:
			z=l[j+1:].count(v)
			if z==2:
				i+=3
			elif z:

				i+=f(z)

				black_list.add(v)
			else:
				continue
			# i += l[j + 1:].count(w)
		else:
			if l.count(w):
				i+=l.count(v)*l.count(w)
				black_list.add(v)
				black_list.add(w)


		# i+=l[j+1:].count(w)


	print(i)


