import time



def fact(n, csum):
	while True:                     # change recursion to a while loop
		if n == 0:
			return csum
		n, csum = n - 1, csum * n  


fact(100000, 1)