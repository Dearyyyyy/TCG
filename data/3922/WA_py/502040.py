while True :
	a, b = raw_input().split(" ")
	if int(b) == 0:
		print 'error'
	else :
		a=float(a)/float(b)	
		print int(a+0.5)