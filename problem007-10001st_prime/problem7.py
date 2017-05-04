def is_relative_prime(x, lis):
	for i in lis:
		if x % i == 0:
			return False
	return True

def find_nth_prime(n):
	primes = [3]
	i = 5
	while len(primes) + 1 < n:
		if is_relative_prime(i, primes):
			primes.append(i)
		i += 2
	return primes[len(primes) - 1]

print find_nth_prime(2)
print find_nth_prime(5)
print find_nth_prime(10001)