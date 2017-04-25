d = 5
m = 0
yy = 1901

s = 0

while True:
	d_before = d
	if m in [0,2,4,6,7,9,11]:
		d = (d + 7) % 31
	elif m in [3,5,8,10]:
		d = (d + 7) % 30
	else:
		#menei o febrouarios kai to add sto sum an einai 1 tou mhna
		if (yy % 4 == 0 and yy % 100 != 0) or yy % 400 == 0:
			d = (d + 7) % 29
		else:
			d = (d + 7) % 28
	if d == 0:
		s += 1
	if d < d_before:
		m += 1
		if m == 12:
			m = 0
			yy += 1
			if yy > 2000:
				print s
				break

print s
