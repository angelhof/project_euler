def length_of_seq(x):
	result = 0
	while x > 1:
		if x % 2 == 0:
			x = x / 2
		else:
			x = 3 * x + 1
		result += 1
	return result

max = 0
maxx = 0
for i in range(2, 1000001):
	if length_of_seq(i) > max:
		max = length_of_seq(i)
		maxx = i

print max, maxx