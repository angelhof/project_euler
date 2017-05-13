import sys, os
sys.path.append('../lib') # or give the full path
from progress_bar import *

with open("p081_matrix.txt", 'r') as infile:
  lines = infile.read().rstrip().split("\n")
  data = [map(int, x.split(',')) for x in lines]

dynamic = [[0 for cell in row] for row in data]

N = 80
for i in range(N)[::-1]:
  printProgressBar(N-i, N+1, prefix = 'Progress:', suffix = 'Complete', length = 50)
  for j in range(N)[::-1]:
    dynamic[i][j] += data[i][j]
    if(j == N-1 and i < N-1):
      dynamic[i][j] += dynamic[i+1][j]
    elif(i == N-1 and j < N-1):
      dynamic[i][j] += dynamic[i][j+1]
    elif(i < N-1 and j < N-1):
      if(dynamic[i][j+1] < dynamic[i+1][j]):
        dynamic[i][j] += dynamic[i][j+1]
      else:
        dynamic[i][j] += dynamic[i+1][j]
    # print dynamic[i][j]

printProgressBar(100, 100, prefix = 'Progress:', suffix = 'Complete', length = 50)
print "Found it:", dynamic[0][0]
