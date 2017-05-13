a = []
for i in range(2,101):
	for j in range(2,101):
		x = i ** j
		if x not in a:
			a.append(x)

print len(a)