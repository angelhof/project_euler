add = 2
a = [1]
while add <= 1000:
	a.append(a[len(a) - 1] + add)
	a.append(a[len(a) - 1] + add)
	a.append(a[len(a) - 1] + add)
	a.append(a[len(a) - 1] + add)
	add += 2

s = 0
for i in a:
	s += i

print s