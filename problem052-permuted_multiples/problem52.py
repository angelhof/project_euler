import sys, os
sys.path.append('../lib') # or give the full path
from progress_bar import *


def digits(num): 
  digs = []
  x = num
  while x > 0:
    digs.append(x % 10)
    x = x / 10

  return set(digs)

i = 1
while True:
  printProgressBar(i, 142858, prefix = 'Progress:', suffix = 'Complete', length = 50)
  res = [digits(x * i) for x in range(1,7)]
  
  dig_set = res[0]
  ## If all the digit sets are the same
  if(all([dig_set == x for x in res])):
    printProgressBar(100, 100, prefix = 'Progress:', suffix = 'Complete', length = 50)
    print "Found it:", i
    break

  i += 1