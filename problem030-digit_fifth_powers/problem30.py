a=[]
for i in range(2,1000000):
	s = 0
	for c in str(i):
		s += int(c) ** 5
		if s > i:
			break
	if s == i:
		a.append(s)

print a
s = 0
for i in a:
	s += i

print s
