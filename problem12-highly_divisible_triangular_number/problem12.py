def triangle_gen():
	i = 1
	s = 1
	while True:
		yield s
		i += 1
		s += i

def count_divisors(n):
	result = 0
	for i in range(1, int(n ** 0.5) + 1):
		if n % i == 0:
			result += 1
	return 2 * result

def problem12():
	for i in triangle_gen():
		if count_divisors(i) > 500:
			return i


print problem12() 