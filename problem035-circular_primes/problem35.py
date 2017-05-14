import sys, os
sys.path.append('../lib') # or give the full path
from progress_bar import *

import is_prime

def problem35(n):

	a = []
	for i in xrange(n+1):
		printProgressBar(i, 2 * (n + 1), prefix = 'Progress:', suffix = 'Complete', length = 50)
		a.append(is_prime.is_prime(i))

	result = []
	for i in xrange(2,n + 1):
		printProgressBar(i + n + 1, 2 * (n + 1), prefix = 'Progress:', suffix = 'Complete', length = 50)
		flag = True
		curr = str(i)

		for j in range(0,len(curr)):
			if not a[int(curr)]:
				flag = False
				break
			
			curr =  curr[-1] + curr[:- 1]
		
		if flag:
			result.append(i)
	return result

# print problem35(100)
a = problem35(1000000)
# print a
printProgressBar(1, 1, prefix = 'Progress:', suffix = 'Complete', length = 50)
print len(a)

