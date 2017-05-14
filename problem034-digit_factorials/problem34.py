import sys, os
sys.path.append('../lib') # or give the full path
from progress_bar import *

import factorial

fac = factorial.fact

a = [fac(i,1) for i in range(0,10)]
s = 0
for i in range(3, 5000000):
  printProgressBar(i, 5000000, prefix = 'Progress:', suffix = 'Complete', length = 50)
  s1 = 0
  for c in str(i):
    s1 += a[int(c)]
  if s1 == i:
    s += s1
    # print s1

printProgressBar(1, 1, prefix = 'Progress:', suffix = 'Complete', length = 50)  
print s