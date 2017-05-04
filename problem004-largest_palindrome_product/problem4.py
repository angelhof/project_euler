def is_palindrome(x):
	x = str(x)
	for i in range(0, len(x) / 2 + 1):
		if x[i] != x[len(x) - 1 - i]:
			return False
	return True

def generate():
	result = []
	for i in range(900, 1000)[::-1]:
		for j in range(900, 1000)[::-1]:
			if is_palindrome(i * j) and len(str(i * j)) >= 6:
				result.append(i * j)
	result.sort()
	return result[len(result) - 1]

print generate()
