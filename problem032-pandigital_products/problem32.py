a = []
for i in range(1,11):
	for j in range(999,10001):
		tar = str(i) + str(j) + str(i*j)
		l = list(tar)
		l.sort()
		if len(tar) == 9 and l == ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and not i*j in a:
			a.append(i*j)

for i in range(9,101):
	for j in range(99,1001):
		tar = str(i) + str(j) + str(i*j)
		l = list(tar)
		l.sort()
		if len(tar) == 9 and l == ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and not i*j in a:
			a.append(i*j)

s = 0
for i in a:
	s += i

# print range(1,10)
# print a
print "Found it:", s