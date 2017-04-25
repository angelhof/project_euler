def find_divs(n):
	s = 1
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			s += i
			if n / i != i:
				s += n / i
	return s

a = [find_divs(i) for i in range(0,10000)]

b = []
for i in range(1,10000):
	if a[i] < 10000 - 1:
		if a[a[i]] == i and not i == a[i]:
			if i not in b:
				b.append(i)
			if a[i] not in b:
				b.append(a[i])

print b
s = 0
for i in b:
	s += i

print s

print find_divs(220)
print find_divs(284)



