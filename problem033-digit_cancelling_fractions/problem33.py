a = []
for i in (i for i in range(11, 100) if i % 10 > 0):
	for j in (j for j in range(i + 1, 100) if j % 10 > 0):
		if str(i)[0] == str(j)[0]:
			if float(i) / float(j) == float(str(i)[1]) / float(str(j)[1]):
				a.append((i,j))
		elif str(i)[0] == str(j)[1]:
			if float(i) / float(j) == float(str(i)[1]) / float(str(j)[0]):
				a.append((i,j))
		elif str(i)[1] == str(j)[0]:
			if float(i) / float(j) == float(str(i)[0]) / float(str(j)[1]):
				a.append((i,j))	
		elif str(i)[1] == str(j)[1]:
			if float(i) / float(j) == float(str(i)[0]) / float(str(j)[0]):
				a.append((i,j))	

print a


			
				
