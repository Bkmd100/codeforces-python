import sys
sys.setrecursionlimit(1500000)
output=50000
seen,wanted= [int(x) for x in input().split()]   



done_values=[]
solutions=[] 

def cnn(n):
	global output
	output=min(n,output)
tota=0

def fucker(n,r):
	global tota
	
	if r>= 15:
		return
	if n in done_values:
		return
	done_values.append(n)	
	if n>=wanted:
		tota+=1
		cnn(r+n-wanted)
		solutions.append(r+n-wanted)
	else:
		
		if (n>1):
			fucker(n-1,r+1)
		fucker(n*2,r+1)	

	
fucker(seen,0)
print((solutions))
print(output)
#print(done_values)
#	print(done_values)
#	
