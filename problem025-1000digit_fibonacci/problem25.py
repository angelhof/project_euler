def fibonacci_gen():
	yield (1, 1)
	yield (2, 1)
	a = 1
	b = 1
	i = 3
	while True:
		c = a + b
		yield (i, c)
		i += 1
		a = b
		b = c

for i in fibonacci_gen():
	if len(str(i[1])) >= 1000:
		print i[0], i[1]
		break

y = fibonacci_gen().next()