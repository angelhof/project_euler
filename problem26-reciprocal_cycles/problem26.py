from decimal import *

IREP, IPER, IPOS = 0, 1, 2

def find_dominant(src):
  best = (0, 0, 0) # repetitions-1, period, position

  period = 0
  while period < len(src) // max(2, 1 + best[IREP]):
    period += 1
    length = 0

    for pos in range(len(src) - 1 - period, -1, -1):
      if src[pos] == src[pos + period]:
        length += 1
        repetitions = length // period
        if repetitions >= best[IREP]:
          best = (repetitions, period, pos)
      else:
        length = 0

  return best

getcontext().prec = 1500

maxy = -1
for i in xrange(7,1000):
  print i
  curr = Decimal(1) / Decimal(i) 
  s = str(curr)[2:]
  res = find_dominant(s)
  ## What is not in the circle is less than the period all is good
  if(res[1] > maxy):
    maxy = res[1]
    print "Max: ", maxy

    
    
    

