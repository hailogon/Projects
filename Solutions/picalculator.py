def picalculator(dp):
	pi = [3]
	for x in range(2,1000000,4):
		pi.append(4./(x*(x+1)*(x+2)))
		pi.append(-4./((x+2)*(x+3)*(x+4)))
	return round(sum(pi),dp)
	
x = input('How many digits of pi?')

if x > 11:
	print "Sorry sir, this calculator is only capable of displaying 11 units of pi"
elif x < 1:
	print "Nobody likes a smart-ass"
else:
	print picalculator(x)
