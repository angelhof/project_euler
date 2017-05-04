s = 0

for i in xrange(1, 1000):

	m = i % 10
	i = i / 10
	d = i % 10
	i = i / 10
	h = i % 10
	if d == 1:
		if m == 0:
			word = "ten"
		elif m == 1:
			word = "eleven"
		elif m ==2:
			word = "twelve"
		elif m == 3:
			word = "thirteen"
		elif m == 4:
			word = "fourteen"
		elif m == 5:
			word = "fifteen"
		elif m == 6:
			word = "sixteen"
		elif m == 7:
			word = "seventeen"
		elif m == 8:
			word = "eighteen"
		elif m == 9:
			word = "nineteen"
		s += len(word)
	else:
		if m == 0:
			word = ""
		elif m == 1:
			word = "one"
		elif m ==2:
			word = "two"
		elif m == 3:
			word = "three"
		elif m == 4:
			word = "four"
		elif m == 5:
			word = "five"
		elif m == 6:
			word = "six"
		elif m == 7:
			word = "seven"
		elif m == 8:
			word = "eight"
		elif m == 9:
			word = "nine"
		s += len(word)

		if d == 0:
			word = ""
		elif d ==2:
			word = "twenty"
		elif d == 3:
			word = "thirty"
		elif d == 4:
			word = "forty"
		elif d == 5:
			word = "fifty"
		elif d == 6:
			word = "sixty"
		elif d == 7:
			word = "seventy"
		elif d == 8:
			word = "eighty"
		elif d == 9:
			word = "ninety"
		s += len(word)

	if h > 0:
		s += 7 
		if d > 0 or m > 0:
			s += 3
		if h == 1 or h == 2 or h == 6:
			s += 3
		elif h == 4 or h == 5 or h == 9:
			s += 4
		elif h == 3 or h == 7 or h == 8:
			s += 5
	print h, d, m,  s

s += len("onethousand")

print 1000, s