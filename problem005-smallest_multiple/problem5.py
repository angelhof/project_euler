import math
import is_prime
is_prime = is_prime.is_prime

def prime_power(x):
	result = 0
	for i in range(2, int(math.sqrt(x)) + 1):
		if x % i == 0:
			result = i
			break
	if result > 0:
		while x > 1:
			if x % result == 0:
				x = x / result
			elif x > 1:
				return (False, 1)
		return (True, result)
	else:
		return (True, x)

def problem5(n):
	result = 1
	for i in range(2, n + 1):
		x = prime_power(i)
		if is_prime(i):
			result *= i
		elif x[0]:
			result *= x[1]
	return result

print problem5(20)