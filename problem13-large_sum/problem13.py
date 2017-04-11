my_file = open("text.txt", "r")

s = 0
while True:
	x = my_file.readline()
	if x:
		s += int(x)
	else:
		break

print s
my_file.close()