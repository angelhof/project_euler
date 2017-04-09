def problem9():
	for i in range(1,1000):
		for j in range(1,1000):
			for k in range(1,1000):
				if i + j + k == 1000:
					if k ** 2 == i ** 2 + j ** 2:
						return i*j*k
					elif i ** 2 == k ** 2 + j ** 2:
						return i*j*k
					elif j ** 2 == i ** 2 + k ** 2:
						return i*j*k

print problem9()