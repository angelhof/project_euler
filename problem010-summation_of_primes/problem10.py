def is_relative_prime(x, lis):
	for i in lis:
		if x % i == 0:
			return False
		elif i > x ** 0.5:
			break
	return True


def find_sum_of_primes_below(n):
	primes = [2,3]
	i = 5
	result = 5
	while i < n:
		if is_relative_prime(i, primes):
			primes.append(i)
			result += i
		i += 2
	return result

print find_sum_of_primes_below(10)
print find_sum_of_primes_below(100)
print find_sum_of_primes_below(2000000)