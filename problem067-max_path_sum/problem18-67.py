my_file = open("p067_triangle.txt", "r")

a = []
while True:
	x = my_file.readline()
	if x:
		x1 = x.split(" ")
		x2 = []
		while len(x1) > 0:
			x2.append(int(x1.pop()))
		a.append(x2)
	else:
		break

print a
my_file.close()

#Menei na afairoume kathe fora th sthlh pou exei to mikrotero athroisma
#Kalutera na kanw rec function pou na spaei to tree se left kai right kai na epistrefei to max apo ta dio ta opiia 8a briskei kanontas rec
#etsi 8a briskei to megalutero bathia kai tha to epistrefei sto apo panw kai ola 8a odhghthoun sto telos

b = [[0 for j in i] for i in a]
for row in range(0, len(a) - 1):
	for i in range(0, len(a[row])):
		if a[row][i] + b [row][i] > b[row + 1][i]:
			b[row + 1][i] = a[row][i] + b [row][i]
		if a[row][i] + b [row][i] > b[row + 1][i + 1]:
			b[row + 1][i + 1] = a[row][i] + b [row][i]

print b

max = 0
for i in range(0, len(b) - 1):
	if b[len(b) - 1][i] + a[len(b) - 1][i] > max:
		max = b[len(b) - 1][i] + a[len(b) - 1][i]

print max