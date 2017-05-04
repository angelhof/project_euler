import itertools
index = 0
for i in itertools.permutations([0,1,2,3,4,5,6,7,8,9]):
	index += 1
	if index == 1000000:
		print i
		break
