import sys, os
sys.path.append('../lib') # or give the full path
from progress_bar import *

with open("p082_matrix.txt", 'r') as infile:
# with open("test.txt", 'r') as infile:
  lines = infile.read().rstrip().split("\n")
  data = [map(int, x.split(',')) for x in lines]

dynamic = [[0 for cell in row] for row in data]

N = len(data)
## All < pass
for j in range(N)[::-1]:
  printProgressBar(N-j, N+1, prefix = 'Progress:', suffix = 'Complete', length = 50)
  if(j < N-1):
    ## First the ^ pass
    for i in range(N)[::-1]:
      dynamic[i][j] += data[i][j]
      ## If we are at the final column
      if(j == N-1 and i < N-1):
        dynamic[i][j] += dynamic[i+1][j]
      ## If we are at the final row  
      elif(i == N-1 and j < N-1):
        dynamic[i][j] += dynamic[i][j+1]
      ## If we are at a normal spot
      elif(i < N-1 and j < N-1):
        if(dynamic[i][j+1] < dynamic[i+1][j]):
          dynamic[i][j] += dynamic[i][j+1]
        else:
          dynamic[i][j] += dynamic[i+1][j]

    ## Then the v pass
    for i in range(N):  
      ## If we are not at the first row
      if(i > 0):
        if(dynamic[i-1][j] < dynamic[i][j] - data[i][j]):
          dynamic[i][j] = dynamic[i-1][j] + data[i][j]
  else:
    for i in range(N):
      dynamic[i][j] += data[i][j]
    


printProgressBar(100, 100, prefix = 'Progress:', suffix = 'Complete', length = 50)
print "Found it:", min([dynamic[i][0] for i in range(N)])
