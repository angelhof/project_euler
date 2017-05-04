def find_divs(n):
	s = 1
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			s += i
			if n / i != i:
				s += n / i
	return s

a=[i for i in range(11, 28123 / 2 + 1) if find_divs(i) > i]
print a

