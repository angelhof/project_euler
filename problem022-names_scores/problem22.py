my_file = open("p022_names.txt", "r")

x = my_file.readline().split('","')
x.sort()
my_file.close()

sum = 0
for index in range(0, len(x)):
	word = x[index]
	s = 0
	for i in word:
		s += ord(i) - ord('A') + 1
	if word == "COLIN":
		print word, index, s * (index + 1)
	sum += s * (index + 1)

print sum
