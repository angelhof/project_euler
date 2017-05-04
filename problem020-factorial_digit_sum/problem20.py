def fact(n, csum):
	while True:                     # change recursion to a while loop
		if n == 0:
			return csum
		n, csum = n - 1, csum * n  


facto = fact(100, 1)
res = sum(map(int, str(facto)))
print res
