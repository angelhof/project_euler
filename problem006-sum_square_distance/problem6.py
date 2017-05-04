def sq_sums_dif(x):
	s1 = 0
	s2 = 0
	for i in range(1,x + 1):
		s1 += i ** 2
		s2 += i
	s2 = s2 ** 2
	return s2 - s1

print sq_sums_dif(100)